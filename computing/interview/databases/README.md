# Databases for Interviews

A structured reference covering the SQL and NoSQL topics most commonly tested in technical and system-design interviews. Examples are grouped by category with links to runnable SQL scripts and Python/shell snippets.

---

## Contents

### SQL
1. [Core Concepts](#1-core-concepts)
2. [DDL — Schema Design](#2-ddl--schema-design)
3. [DML — Querying](#3-dml--querying)
4. [Aggregations & Window Functions](#4-aggregations--window-functions)
5. [Joins](#5-joins)
6. [Subqueries & CTEs](#6-subqueries--ctes)
7. [Indexes](#7-indexes)
8. [Transactions & ACID](#8-transactions--acid)
9. [Normalization](#9-normalization)
10. [Performance & Query Plans](#10-performance--query-plans)

### NoSQL
11. [NoSQL Overview & CAP Theorem](#11-nosql-overview--cap-theorem)
12. [Document Store — MongoDB](#12-document-store--mongodb)
13. [Key-Value Store — Redis](#13-key-value-store--redis)
14. [Wide-Column Store — Cassandra](#14-wide-column-store--cassandra)
15. [Graph Database — Neo4j](#15-graph-database--neo4j)
16. [SQL vs NoSQL Decision Guide](#16-sql-vs-nosql-decision-guide)

### References
17. [References](#17-references)

---

## SQL

### 1. Core Concepts

| Concept | One-line definition |
|---------|---------------------|
| **RDBMS** | Stores data in tables with rows and columns; enforces schema |
| **Primary Key** | Uniquely identifies each row; never NULL |
| **Foreign Key** | References a PK in another table; enforces referential integrity |
| **Constraint** | Rule enforced by the DB engine (NOT NULL, UNIQUE, CHECK, DEFAULT) |
| **View** | Named stored query; virtual table |
| **Stored Procedure** | Precompiled SQL logic stored in the DB |
| **Trigger** | Automatic procedure fired on INSERT / UPDATE / DELETE |
| **Sequence / AUTO_INCREMENT** | Auto-generated numeric key |

### 2. DDL — Schema Design

DDL (Data Definition Language) commands create and modify the structure of the database.

```sql
-- Create a database
CREATE DATABASE shop;
USE shop;

-- Create tables with constraints
CREATE TABLE customers (
    customer_id INT          PRIMARY KEY AUTO_INCREMENT,
    email       VARCHAR(255) NOT NULL UNIQUE,
    name        VARCHAR(100) NOT NULL,
    created_at  TIMESTAMP    DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE products (
    product_id  INT            PRIMARY KEY AUTO_INCREMENT,
    name        VARCHAR(200)   NOT NULL,
    price       DECIMAL(10, 2) NOT NULL CHECK (price >= 0),
    stock       INT            NOT NULL DEFAULT 0
);

CREATE TABLE orders (
    order_id    INT       PRIMARY KEY AUTO_INCREMENT,
    customer_id INT       NOT NULL,
    ordered_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status      ENUM('pending','shipped','delivered','cancelled') DEFAULT 'pending',
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE
);

CREATE TABLE order_items (
    order_id   INT            NOT NULL,
    product_id INT            NOT NULL,
    quantity   INT            NOT NULL CHECK (quantity > 0),
    unit_price DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (order_id, product_id),
    FOREIGN KEY (order_id)   REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Alter an existing table
ALTER TABLE customers ADD COLUMN phone VARCHAR(20);
ALTER TABLE products  ADD COLUMN category VARCHAR(50);

-- Drop a table (irreversible)
-- DROP TABLE order_items;
```

Full example: [sql/01_ddl_schema.sql](sql/01_ddl_schema.sql)

---

### 3. DML — Querying

DML (Data Manipulation Language) covers INSERT, UPDATE, DELETE, and SELECT.

```sql
-- INSERT
INSERT INTO customers (email, name) VALUES
    ('alice@example.com', 'Alice'),
    ('bob@example.com',   'Bob');

-- UPDATE with WHERE (always use WHERE to avoid full-table update)
UPDATE products SET stock = stock - 1 WHERE product_id = 42;

-- DELETE with WHERE
DELETE FROM orders WHERE status = 'cancelled' AND ordered_at < '2024-01-01';

-- Basic SELECT with filtering and ordering
SELECT name, price
FROM   products
WHERE  price BETWEEN 10 AND 100
  AND  category = 'electronics'
ORDER  BY price DESC
LIMIT  10 OFFSET 20;   -- page 3 (page size 10)

-- Pattern matching
SELECT * FROM customers WHERE email LIKE '%@gmail.com';

-- NULL handling
SELECT * FROM customers WHERE phone IS NULL;
```

Full example: [sql/02_dml_queries.sql](sql/02_dml_queries.sql)

---

### 4. Aggregations & Window Functions

```sql
-- ── Aggregate functions ──────────────────────────────────────
SELECT
    category,
    COUNT(*)                       AS total_products,
    AVG(price)                     AS avg_price,
    MIN(price)                     AS min_price,
    MAX(price)                     AS max_price,
    SUM(stock * price)             AS inventory_value
FROM  products
GROUP BY category
HAVING AVG(price) > 50            -- filter on aggregated result
ORDER BY inventory_value DESC;

-- ── Window functions ─────────────────────────────────────────
-- ROW_NUMBER, RANK, DENSE_RANK
SELECT
    name,
    price,
    category,
    ROW_NUMBER()  OVER (PARTITION BY category ORDER BY price DESC) AS row_num,
    RANK()        OVER (PARTITION BY category ORDER BY price DESC) AS rnk,
    DENSE_RANK()  OVER (PARTITION BY category ORDER BY price DESC) AS dense_rnk
FROM products;

-- Running total
SELECT
    order_id,
    ordered_at,
    total,
    SUM(total) OVER (ORDER BY ordered_at ROWS UNBOUNDED PRECEDING) AS running_total
FROM (
    SELECT o.order_id, o.ordered_at,
           SUM(oi.quantity * oi.unit_price) AS total
    FROM   orders o JOIN order_items oi USING (order_id)
    GROUP  BY o.order_id, o.ordered_at
) t;

-- LAG / LEAD — compare with previous / next row
SELECT
    ordered_at,
    total,
    LAG(total)  OVER (ORDER BY ordered_at) AS prev_total,
    LEAD(total) OVER (ORDER BY ordered_at) AS next_total
FROM ...;
```

Full example: [sql/03_aggregations_windows.sql](sql/03_aggregations_windows.sql)

---

### 5. Joins

```
INNER JOIN  → only matching rows in BOTH tables
LEFT JOIN   → all rows from left + matched rows from right (NULL if no match)
RIGHT JOIN  → all rows from right + matched rows from left
FULL JOIN   → all rows from both (MySQL: emulate with UNION)
CROSS JOIN  → cartesian product
SELF JOIN   → a table joined with itself
```

```sql
-- INNER JOIN: only customers who have placed orders
SELECT c.name, COUNT(o.order_id) AS order_count
FROM   customers c
INNER JOIN orders o ON c.customer_id = o.customer_id
GROUP  BY c.customer_id;

-- LEFT JOIN: ALL customers, even those with no orders
SELECT c.name, COUNT(o.order_id) AS order_count
FROM   customers c
LEFT  JOIN orders o ON c.customer_id = o.customer_id
GROUP  BY c.customer_id;

-- Multi-table JOIN
SELECT c.name, p.name AS product, oi.quantity, oi.unit_price
FROM   customers c
JOIN   orders     o  ON c.customer_id  = o.customer_id
JOIN   order_items oi ON o.order_id    = oi.order_id
JOIN   products    p  ON oi.product_id = p.product_id
WHERE  o.status = 'delivered';

-- SELF JOIN: find customers in the same city as customer 5
SELECT a.name AS customer, b.name AS same_city_as
FROM   customers a
JOIN   customers b ON a.city = b.city AND a.customer_id <> 5
WHERE  b.customer_id = 5;
```

Full example: [sql/04_joins.sql](sql/04_joins.sql)

---

### 6. Subqueries & CTEs

```sql
-- ── Subquery in WHERE ────────────────────────────────────────
-- Products more expensive than average
SELECT name, price FROM products
WHERE  price > (SELECT AVG(price) FROM products);

-- EXISTS: customers who have at least one order
SELECT name FROM customers c
WHERE  EXISTS (SELECT 1 FROM orders o WHERE o.customer_id = c.customer_id);

-- IN: orders for specific product IDs
SELECT order_id FROM order_items
WHERE  product_id IN (SELECT product_id FROM products WHERE category = 'books');

-- ── CTE (Common Table Expression) ───────────────────────────
WITH customer_totals AS (
    SELECT c.customer_id, c.name,
           SUM(oi.quantity * oi.unit_price) AS lifetime_value
    FROM   customers c
    JOIN   orders     o  USING (customer_id)
    JOIN   order_items oi USING (order_id)
    GROUP  BY c.customer_id
)
SELECT name, lifetime_value
FROM   customer_totals
WHERE  lifetime_value > 1000
ORDER  BY lifetime_value DESC;

-- ── Recursive CTE: organisational hierarchy ──────────────────
WITH RECURSIVE org AS (
    SELECT employee_id, name, manager_id, 1 AS depth
    FROM   employees
    WHERE  manager_id IS NULL           -- root (CEO)
    UNION ALL
    SELECT e.employee_id, e.name, e.manager_id, o.depth + 1
    FROM   employees e
    JOIN   org o ON e.manager_id = o.employee_id
)
SELECT depth, name FROM org ORDER BY depth, name;
```

Full example: [sql/05_subqueries_ctes.sql](sql/05_subqueries_ctes.sql)

---

### 7. Indexes

An index is a data structure (usually a B-Tree or hash) that speeds up lookups at the cost of extra storage and slower writes.

```sql
-- Single-column index
CREATE INDEX idx_products_category ON products(category);

-- Composite index — order matters: useful for (category), (category, price)
-- but NOT for (price) alone
CREATE INDEX idx_products_cat_price ON products(category, price);

-- Unique index (also enforces uniqueness)
CREATE UNIQUE INDEX idx_customers_email ON customers(email);

-- Covering index: all columns needed by a query are in the index
CREATE INDEX idx_order_items_cover
    ON order_items(order_id, product_id, quantity, unit_price);

-- Full-text index (MySQL)
CREATE FULLTEXT INDEX idx_products_name ON products(name);
SELECT * FROM products WHERE MATCH(name) AGAINST('wireless headphones' IN BOOLEAN MODE);

-- Show existing indexes
SHOW INDEX FROM products;

-- Drop index
DROP INDEX idx_products_category ON products;
```

**Key interview points:**
- Primary keys always have an index automatically.
- `EXPLAIN` / `EXPLAIN ANALYZE` shows whether an index is used.
- The **selectivity** of a column determines how useful an index is (high cardinality → better).
- Too many indexes slow down writes; only index columns used in WHERE, JOIN ON, ORDER BY, GROUP BY.

Full example: [sql/06_indexes.sql](sql/06_indexes.sql)

---

### 8. Transactions & ACID

**ACID properties:**

| Property | Meaning |
|----------|---------|
| **Atomicity** | All operations in a transaction succeed or all are rolled back |
| **Consistency** | The DB stays in a valid state before and after the transaction |
| **Isolation** | Concurrent transactions behave as if they ran sequentially |
| **Durability** | Committed changes survive crashes |

```sql
-- Basic transaction
START TRANSACTION;

UPDATE accounts SET balance = balance - 500 WHERE account_id = 1;
UPDATE accounts SET balance = balance + 500 WHERE account_id = 2;

-- Only commit if both succeeded
COMMIT;

-- Rollback on error
ROLLBACK;

-- Savepoints: partial rollback
START TRANSACTION;
INSERT INTO orders (...) VALUES (...);
SAVEPOINT after_order;

INSERT INTO order_items (...) VALUES (...);

-- If second insert fails, roll back only to savepoint
ROLLBACK TO SAVEPOINT after_order;
COMMIT;
```

**Isolation levels** (weakest → strongest):

| Level | Dirty Read | Non-repeatable Read | Phantom Read |
|-------|-----------|---------------------|--------------|
| READ UNCOMMITTED | ✅ possible | ✅ possible | ✅ possible |
| READ COMMITTED | ❌ prevented | ✅ possible | ✅ possible |
| REPEATABLE READ | ❌ | ❌ | ✅ (MySQL InnoDB mitigates) |
| SERIALIZABLE | ❌ | ❌ | ❌ |

```sql
SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;
```

Full example: [sql/07_transactions.sql](sql/07_transactions.sql)

---

### 9. Normalization

Normalization reduces data redundancy and improves integrity by decomposing tables into well-structured relations.

| Normal Form | Rule |
|-------------|------|
| **1NF** | Atomic values; no repeating groups; each row uniquely identifiable |
| **2NF** | 1NF + no partial dependencies (every non-key column depends on the *whole* PK) |
| **3NF** | 2NF + no transitive dependencies (non-key → non-key) |
| **BCNF** | Every determinant is a candidate key (stricter 3NF) |

```
-- Unnormalised (violates 1NF)
orders: order_id | customer_name | customer_email | products (comma list) | ...

-- After 1NF: atomic values
orders: order_id | customer_name | customer_email | ...
order_items: order_id | product_id | quantity | ...

-- After 2NF: remove partial dependency
-- (if PK is (order_id, product_id), product_name depends only on product_id)
products: product_id | product_name | price | ...

-- After 3NF: remove transitive dependency
-- (customer_email → customer_name → city: city depends on name, not on email)
customers: customer_id | customer_email | customer_name | city | ...
```

**When to denormalise:** read-heavy analytics, data warehouses (star/snowflake schema), when JOIN cost exceeds duplication cost.

---

### 10. Performance & Query Plans

```sql
-- EXPLAIN shows the query execution plan
EXPLAIN SELECT * FROM orders WHERE customer_id = 5;

-- EXPLAIN ANALYZE (MySQL 8+ / PostgreSQL) also runs the query and shows actual times
EXPLAIN ANALYZE
SELECT c.name, SUM(oi.quantity * oi.unit_price) AS total
FROM   customers c
JOIN   orders     o  USING (customer_id)
JOIN   order_items oi USING (order_id)
WHERE  o.status = 'delivered'
GROUP  BY c.customer_id;
```

**Key EXPLAIN columns (MySQL):**

| Column | What to look for |
|--------|-----------------|
| `type` | `const` > `ref` > `range` > `index` > `ALL` (ALL = full table scan = bad) |
| `key` | Index actually used (NULL = no index) |
| `rows` | Estimated rows examined (lower is better) |
| `Extra` | `Using index` (covering), `Using filesort` (bad), `Using temporary` (bad) |

**Quick wins:**
- Add missing indexes on WHERE / JOIN / ORDER BY columns
- Avoid `SELECT *` — fetch only needed columns
- Avoid functions on indexed columns in WHERE: `WHERE YEAR(created_at) = 2024` prevents index use; use `WHERE created_at BETWEEN '2024-01-01' AND '2024-12-31'`
- Use `LIMIT` early; push filters as close to the data as possible
- Pagination: keyset (`WHERE id > last_seen_id LIMIT 10`) is faster than `OFFSET` at large pages

Full example: [sql/08_performance.sql](sql/08_performance.sql)

---

## NoSQL

### 11. NoSQL Overview & CAP Theorem

**CAP Theorem** — a distributed system can guarantee at most **two** of:

| Property | Meaning |
|----------|---------|
| **Consistency** | Every read receives the most recent write |
| **Availability** | Every request gets a (possibly stale) response |
| **Partition Tolerance** | The system continues operating despite network splits |

Since network partitions are unavoidable in practice, systems choose between **CP** (consistent, may be unavailable during partition) and **AP** (available, may return stale data).

**NoSQL categories:**

| Type | Examples | Best for | CAP |
|------|----------|----------|-----|
| Document | MongoDB, Firestore, CouchDB | Flexible schemas, hierarchical data | CP or AP |
| Key-Value | Redis, DynamoDB, Memcached | Caching, sessions, counters | AP (Redis: CP in cluster) |
| Wide-Column | Cassandra, HBase, Bigtable | Massive write-heavy time-series | AP |
| Graph | Neo4j, Amazon Neptune | Relationships, social networks | CP |
| Search | Elasticsearch, OpenSearch | Full-text search, analytics | AP |
| Time-Series | InfluxDB, TimescaleDB | Metrics, IoT, monitoring | AP or CP |

---

### 12. Document Store — MongoDB

Documents are JSON-like objects (BSON). No fixed schema — fields vary per document. Collections ≈ SQL tables; documents ≈ rows.

```js
// ── Create / insert ──────────────────────────────────────────
db.products.insertOne({
  name: "Wireless Headphones",
  price: 79.99,
  category: "electronics",
  tags: ["audio", "bluetooth"],
  specs: { driver: "40mm", impedance: 32 }
});

db.products.insertMany([
  { name: "USB-C Cable", price: 9.99, category: "accessories" },
  { name: "Laptop Stand", price: 34.99, category: "accessories" }
]);

// ── Read / query ─────────────────────────────────────────────
db.products.find({ category: "electronics", price: { $lt: 100 } });
db.products.find({ tags: { $in: ["bluetooth"] } });
db.products.find({ "specs.driver": "40mm" });   // nested field

// Projection (include / exclude fields)
db.products.find({}, { name: 1, price: 1, _id: 0 });

// Sort, limit, skip
db.products.find().sort({ price: -1 }).limit(10).skip(20);

// ── Update ───────────────────────────────────────────────────
db.products.updateOne(
  { name: "USB-C Cable" },
  { $set: { price: 12.99 }, $inc: { stock: 50 } }
);

db.products.updateMany(
  { category: "accessories" },
  { $set: { on_sale: true } }
);

// Upsert: insert if not found
db.products.updateOne(
  { sku: "HDX-200" },
  { $set: { name: "HD Camera", price: 199.99 } },
  { upsert: true }
);

// ── Delete ───────────────────────────────────────────────────
db.products.deleteOne({ name: "Laptop Stand" });
db.products.deleteMany({ stock: 0 });

// ── Aggregation pipeline ─────────────────────────────────────
db.orders.aggregate([
  { $match: { status: "delivered" } },
  { $unwind: "$items" },
  { $group: {
      _id: "$items.product_id",
      total_sold:    { $sum: "$items.quantity" },
      total_revenue: { $sum: { $multiply: ["$items.quantity", "$items.price"] } }
  }},
  { $sort: { total_revenue: -1 } },
  { $limit: 5 }
]);

// ── Indexes ───────────────────────────────────────────────────
db.products.createIndex({ category: 1, price: -1 });   // compound
db.products.createIndex({ name: "text" });              // full-text
db.products.createIndex({ email: 1 }, { unique: true });
```

Full example: [nosql/mongodb_examples.js](nosql/mongodb_examples.js)

---

### 13. Key-Value Store — Redis

Stores data as key-value pairs. Entire dataset fits in RAM; supports persistence. Values can be strings, lists, sets, sorted sets, hashes, streams, bitmaps, HyperLogLogs.

```bash
# ── Strings ───────────────────────────────────────────────────
SET user:1001:name "Alice"
GET user:1001:name
SETEX session:abc123 3600 "user_id=1001"  # expire in 3600s
INCR page_views:home                       # atomic counter

# ── Hashes (map of fields) ────────────────────────────────────
HSET product:42 name "Headphones" price 79.99 stock 150
HGET product:42 price
HGETALL product:42
HINCRBY product:42 stock -1

# ── Lists (ordered, allows duplicates) ───────────────────────
RPUSH task_queue "job:1" "job:2" "job:3"
LPOP task_queue                # dequeue from front
LRANGE task_queue 0 -1         # all elements

# ── Sets (unordered, unique) ─────────────────────────────────
SADD online_users user:1 user:2 user:3
SISMEMBER online_users user:2   # 1 = yes
SMEMBERS online_users
SINTER online_users premium_users  # intersection

# ── Sorted Sets (score-ranked) ────────────────────────────────
ZADD leaderboard 1500 "alice" 2300 "bob" 900 "carol"
ZREVRANGE leaderboard 0 2 WITHSCORES   # top 3
ZINCRBY leaderboard 100 "alice"        # update score
ZRANK leaderboard "alice"              # rank (0-based)

# ── Expiry ────────────────────────────────────────────────────
EXPIRE user:1001:name 86400    # TTL 1 day
TTL    user:1001:name          # seconds remaining
PERSIST user:1001:name         # remove TTL

# ── Pub/Sub ───────────────────────────────────────────────────
SUBSCRIBE notifications
PUBLISH  notifications "new_order:9981"

# ── Transactions ──────────────────────────────────────────────
MULTI
INCR inventory:42
DECR cart:user1:42
EXEC
```

Full example: [nosql/redis_examples.sh](nosql/redis_examples.sh)

---

### 14. Wide-Column Store — Cassandra

Data is organized in tables but columns can vary per row. Optimised for massive write throughput and horizontal scaling. No JOINs; queries must match a partition key.

```sql
-- ── Keyspace (like a database) ───────────────────────────────
CREATE KEYSPACE shop
WITH replication = {
  'class': 'SimpleStrategy',
  'replication_factor': 3
};

USE shop;

-- ── Table design: primary key = partition key + clustering columns ──
-- Partition key: determines which node holds the data
-- Clustering columns: sort data within a partition
CREATE TABLE orders_by_customer (
    customer_id  UUID,
    ordered_at   TIMESTAMP,
    order_id     UUID,
    total        DECIMAL,
    status       TEXT,
    PRIMARY KEY ((customer_id), ordered_at, order_id)
) WITH CLUSTERING ORDER BY (ordered_at DESC);

-- ── Write (upsert by default) ─────────────────────────────────
INSERT INTO orders_by_customer
    (customer_id, ordered_at, order_id, total, status)
VALUES
    (uuid(), toTimestamp(now()), uuid(), 79.99, 'pending');

-- ── Read: MUST include the partition key ─────────────────────
SELECT * FROM orders_by_customer
WHERE  customer_id = 550e8400-e29b-41d4-a716-446655440000
ORDER  BY ordered_at DESC
LIMIT  10;

-- ── Time-to-live (TTL) ────────────────────────────────────────
INSERT INTO sessions (session_id, user_id, data)
VALUES (uuid(), uuid(), 'token=abc')
USING TTL 3600;

-- ── Lightweight transactions (compare-and-set) ────────────────
UPDATE users SET email = 'new@example.com'
WHERE  user_id = ?
IF     email = 'old@example.com';
```

**Key design rules:**
- Design tables around **query patterns**, not entities.
- A partition should not exceed ~100 MB (wide partition problem).
- Avoid `ALLOW FILTERING` in production (full partition scan).

Full example: [nosql/cassandra_examples.cql](nosql/cassandra_examples.cql)

---

### 15. Graph Database — Neo4j

Data is stored as **nodes** and **relationships** (edges). Relationships are first-class citizens with properties. Query language: **Cypher**.

```cypher
// ── Create nodes ────────────────────────────────────────────
CREATE (:Person {name: "Alice", age: 30})
CREATE (:Person {name: "Bob",   age: 25})
CREATE (:Product {name: "Headphones", price: 79.99, category: "electronics"})

// ── Create relationships ─────────────────────────────────────
MATCH (a:Person {name: "Alice"}), (b:Person {name: "Bob"})
CREATE (a)-[:KNOWS {since: 2020}]->(b);

MATCH (p:Person {name: "Alice"}), (pr:Product {name: "Headphones"})
CREATE (p)-[:PURCHASED {on: date("2024-03-01"), qty: 1}]->(pr);

// ── Read / pattern matching ───────────────────────────────────
// All friends of Alice
MATCH (alice:Person {name: "Alice"})-[:KNOWS]->(friend:Person)
RETURN friend.name, friend.age;

// Products purchased by friends of Alice (2-hop)
MATCH (alice:Person {name: "Alice"})-[:KNOWS]->(friend)-[:PURCHASED]->(p:Product)
RETURN DISTINCT p.name, p.price;

// Shortest path between two nodes
MATCH path = shortestPath(
    (alice:Person {name: "Alice"})-[*]-(target:Person {name: "Carol"})
)
RETURN path;

// ── Aggregation ───────────────────────────────────────────────
MATCH (p:Person)-[:PURCHASED]->(pr:Product)
RETURN pr.name, COUNT(p) AS buyers, AVG(pr.price) AS avg_price
ORDER BY buyers DESC LIMIT 5;

// ── Update / Merge ────────────────────────────────────────────
// MERGE = "create if not exists"
MERGE (p:Person {name: "Carol"})
ON CREATE SET p.age = 28, p.created = timestamp()
ON MATCH  SET p.last_seen = timestamp();

// ── Delete ────────────────────────────────────────────────────
MATCH (p:Person {name: "Bob"})
DETACH DELETE p;   -- removes all relationships too
```

Full example: [nosql/neo4j_examples.cypher](nosql/neo4j_examples.cypher)

---

### 16. SQL vs NoSQL Decision Guide

| Criterion | Choose SQL | Choose NoSQL |
|-----------|-----------|--------------|
| **Schema** | Well-defined, stable | Flexible, evolving, document-like |
| **Relationships** | Complex multi-table JOINs | Embedded documents or graph |
| **Consistency** | Strong ACID required | Eventual consistency acceptable |
| **Scale** | Vertical (scale-up) | Horizontal (scale-out, sharding) |
| **Query complexity** | Ad-hoc, complex analytics | Predefined, high-throughput patterns |
| **Write volume** | Moderate | Massive (Cassandra, Redis) |
| **Data size** | GBs–TBs (with tuning) | TBs–PBs natively |
| **Transactions** | Multi-row / cross-table | Single document (Mongo 4+) or none |

**Hybrid patterns:**
- **CQRS** — write to a relational DB; materialise read models in Redis/Elasticsearch
- **Cache-aside** — read from Redis; on miss, load from PostgreSQL and cache
- **Event sourcing** — append events to Kafka/Cassandra; project state into SQL for reads

---

## 17. References

### Quick Learning
- [SQLZoo](https://sqlzoo.net/) — interactive SQL exercises in the browser
- [Mode SQL Tutorial](https://mode.com/sql-tutorial/) — beginner to advanced with real datasets
- [LeetCode — Database problems](https://leetcode.com/problemset/database/) — interview-style SQL questions
- [MongoDB University](https://learn.mongodb.com/) — free official courses
- [Redis University](https://university.redis.com/) — free official Redis courses
- [Use The Index, Luke](https://use-the-index-luke.com/) — deep dive into SQL indexes

### Deeper Dives
- [PostgreSQL Documentation](https://www.postgresql.org/docs/) — gold-standard SQL reference
- [Designing Data-Intensive Applications](https://dataintensive.net/) (Kleppmann) — the definitive system-design book covering SQL, NoSQL, replication, partitioning, consensus
- [High Performance MySQL](https://www.oreilly.com/library/view/high-performance-mysql/9781492080503/) — indexing, query optimisation, replication
- [CMU Database Group — YouTube](https://www.youtube.com/c/CMUDatabaseGroup) — free university-level DB lectures
- [CAP Theorem — Brewer's original talk](https://www.cs.berkeley.edu/~brewer/cs262b-2004/PODC-keynote.pdf)

