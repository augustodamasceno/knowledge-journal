-- ============================================================
-- Apache Cassandra — CQL examples
-- Tested on: Cassandra 4.x / DataStax Astra
-- Run with: cqlsh -f cassandra_examples.cql
-- ============================================================

-- ── Keyspace ─────────────────────────────────────────────────
-- SimpleStrategy: single data centre (dev/test)
CREATE KEYSPACE IF NOT EXISTS shop
WITH replication = {
  'class': 'SimpleStrategy',
  'replication_factor': 3
}
AND durable_writes = true;

USE shop;

-- ── Key design principle ──────────────────────────────────────
-- Primary key = (partition key) + [clustering columns]
-- Partition key: determines which node(s) hold the data.
-- Clustering columns: sort data within a partition.
-- Design tables around ACCESS PATTERNS, not entities.

-- ── Table: orders by customer (query: "all orders for customer X") ──
CREATE TABLE IF NOT EXISTS orders_by_customer (
    customer_id  UUID,
    ordered_at   TIMESTAMP,
    order_id     UUID,
    status       TEXT,
    total        DECIMAL,
    items        LIST<FROZEN<MAP<TEXT, TEXT>>>,   -- embedded short lists OK
    PRIMARY KEY ((customer_id), ordered_at, order_id)
) WITH CLUSTERING ORDER BY (ordered_at DESC, order_id ASC)
  AND default_time_to_live = 0;

-- ── Table: orders by status (query: "all pending orders") ────
CREATE TABLE IF NOT EXISTS orders_by_status (
    status      TEXT,
    ordered_at  TIMESTAMP,
    order_id    UUID,
    customer_id UUID,
    total       DECIMAL,
    PRIMARY KEY ((status), ordered_at, order_id)
) WITH CLUSTERING ORDER BY (ordered_at DESC);

-- ── Table: product catalog ────────────────────────────────────
CREATE TABLE IF NOT EXISTS products (
    product_id  UUID         PRIMARY KEY,
    sku         TEXT,
    name        TEXT,
    price       DECIMAL,
    stock       INT,
    category    TEXT,
    tags        SET<TEXT>,        -- unordered, deduplicated
    specs       MAP<TEXT, TEXT>   -- arbitrary key-value attributes
);

-- ── Table: sessions with TTL ─────────────────────────────────
CREATE TABLE IF NOT EXISTS user_sessions (
    session_id  TEXT PRIMARY KEY,
    user_id     UUID,
    data        TEXT,
    created_at  TIMESTAMP
);

-- ── Table: metrics / time-series ─────────────────────────────
CREATE TABLE IF NOT EXISTS server_metrics (
    server_id   TEXT,
    metric_name TEXT,
    bucket_day  DATE,           -- partition per day to bound partition size
    ts          TIMESTAMP,
    value       DOUBLE,
    PRIMARY KEY ((server_id, metric_name, bucket_day), ts)
) WITH CLUSTERING ORDER BY (ts DESC);

-- ── INSERT (upsert by default) ────────────────────────────────
INSERT INTO orders_by_customer
    (customer_id, ordered_at, order_id, status, total)
VALUES
    (uuid(), toTimestamp(now()), uuid(), 'pending', 79.99);

INSERT INTO products
    (product_id, sku, name, price, stock, category, tags, specs)
VALUES
    (uuid(), 'HDX-100', 'Wireless Headphones', 79.99, 200, 'electronics',
     {'audio', 'bluetooth', 'wireless'},
     {'driver': '40mm', 'impedance': '32', 'weight_g': '250'});

-- INSERT with explicit TTL (row expires after 3600 seconds)
INSERT INTO user_sessions (session_id, user_id, data, created_at)
VALUES ('sess-abc123', uuid(), '{"theme":"dark"}', toTimestamp(now()))
USING TTL 3600;

-- Time-series metric insert
INSERT INTO server_metrics (server_id, metric_name, bucket_day, ts, value)
VALUES ('web-01', 'cpu_pct', '2024-03-20', toTimestamp(now()), 42.5);

-- ── SELECT ────────────────────────────────────────────────────
-- MUST include the full partition key in WHERE

-- All orders for a customer (newest first)
SELECT order_id, ordered_at, status, total
FROM   orders_by_customer
WHERE  customer_id = 550e8400-e29b-41d4-a716-446655440000
ORDER  BY ordered_at DESC
LIMIT  10;

-- Orders within a time range (clustering column range query)
SELECT * FROM orders_by_customer
WHERE  customer_id = 550e8400-e29b-41d4-a716-446655440000
  AND  ordered_at >= '2024-01-01 00:00:00+0000'
  AND  ordered_at <= '2024-03-31 23:59:59+0000';

-- ── UPDATE ────────────────────────────────────────────────────
UPDATE orders_by_customer
SET    status = 'shipped'
WHERE  customer_id = 550e8400-e29b-41d4-a716-446655440000
  AND  ordered_at  = '2024-03-15 14:30:00+0000'
  AND  order_id    = 550e8400-e29b-41d4-a716-446655441111;

-- Increment a counter (requires COUNTER type)
-- Counter tables have special rules: only counter columns + PK allowed
CREATE TABLE IF NOT EXISTS product_views (
    product_id UUID PRIMARY KEY,
    view_count COUNTER
);
UPDATE product_views SET view_count = view_count + 1
WHERE  product_id = 550e8400-e29b-41d4-a716-446655440000;

-- ── DELETE ────────────────────────────────────────────────────
DELETE FROM orders_by_customer
WHERE  customer_id = 550e8400-e29b-41d4-a716-446655440000
  AND  ordered_at  = '2024-03-15 14:30:00+0000'
  AND  order_id    = 550e8400-e29b-41d4-a716-446655441111;

-- Delete a specific column (sets it to tombstone)
DELETE status FROM orders_by_customer
WHERE  customer_id = 550e8400-e29b-41d4-a716-446655440000
  AND  ordered_at  = '2024-03-15 14:30:00+0000'
  AND  order_id    = 550e8400-e29b-41d4-a716-446655441111;

-- ── Lightweight Transactions (LWT) — compare-and-set ─────────
-- Use sparingly: LWT uses Paxos and is ~4× slower than normal writes
INSERT INTO user_sessions (session_id, user_id, data, created_at)
VALUES ('sess-xyz', uuid(), '{}', toTimestamp(now()))
IF NOT EXISTS;

UPDATE products
SET    stock = 199
WHERE  product_id = 550e8400-e29b-41d4-a716-446655440000
IF     stock = 200;

-- ── BATCH ─────────────────────────────────────────────────────
-- Only use for atomic writes to the SAME partition or for unlogged batches
-- Logged batch (atomic, but slow -- avoid cross-partition)
BEGIN BATCH
  INSERT INTO orders_by_customer (customer_id, ordered_at, order_id, status, total)
  VALUES (uuid(), toTimestamp(now()), uuid(), 'pending', 159.98);

  INSERT INTO orders_by_status (status, ordered_at, order_id, customer_id, total)
  VALUES ('pending', toTimestamp(now()), uuid(), uuid(), 159.98);
APPLY BATCH;

-- ── Materialized Views (Cassandra 3.x+) ──────────────────────
-- MV = auto-maintained view derived from a base table with a different PK
CREATE MATERIALIZED VIEW IF NOT EXISTS products_by_category AS
    SELECT * FROM products
    WHERE  category IS NOT NULL AND product_id IS NOT NULL
    PRIMARY KEY ((category), product_id);

SELECT * FROM products_by_category WHERE category = 'electronics';

-- ── Secondary Index (use sparingly; prefer new tables) ────────
CREATE INDEX IF NOT EXISTS idx_products_sku ON products(sku);

-- ── Show schema ───────────────────────────────────────────────
DESCRIBE TABLE orders_by_customer;
DESCRIBE KEYSPACE shop;
