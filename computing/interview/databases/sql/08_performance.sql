-- ============================================================
-- Performance & Query Plans
-- ============================================================

USE shop;

-- ── EXPLAIN basics ───────────────────────────────────────────
-- Key columns to read:
--   type:  const > eq_ref > ref > range > index > ALL   (ALL = full table scan)
--   key:   index used (NULL = none)
--   rows:  estimated rows scanned
--   Extra: "Using index" (good), "Using filesort" (sort not via index), "Using temporary"

EXPLAIN SELECT name, price FROM products WHERE category_id = 1;

-- EXPLAIN ANALYZE (MySQL 8.0.18+ / PostgreSQL): runs the query, shows actual times
-- EXPLAIN ANALYZE SELECT * FROM orders WHERE customer_id = 2 ORDER BY ordered_at DESC;

-- ── Force / ignore an index (testing only) ───────────────────
EXPLAIN SELECT * FROM products USE INDEX (idx_products_cat_price)
WHERE category_id = 1 AND price < 50;

-- ── Anti-pattern: function on indexed column ─────────────────
-- BAD — skips index on ordered_at
EXPLAIN SELECT * FROM orders WHERE DATE(ordered_at) = '2024-03-20';

-- GOOD — range scan on index
EXPLAIN SELECT * FROM orders
WHERE ordered_at >= '2024-03-20 00:00:00'
  AND ordered_at <  '2024-03-21 00:00:00';

-- ── Anti-pattern: SELECT * ────────────────────────────────────
-- Fetches unnecessary columns, can prevent covering-index optimisation
-- BAD:
-- SELECT * FROM order_items WHERE order_id = 1;
-- GOOD:
SELECT order_id, product_id, quantity, unit_price
FROM   order_items
WHERE  order_id = 1;

-- ── Anti-pattern: OFFSET pagination ──────────────────────────
-- BAD: OFFSET 90000 scans and discards 90000 rows
SELECT product_id, name FROM products ORDER BY product_id LIMIT 10 OFFSET 90000;

-- GOOD: Keyset (cursor) pagination — O(log n) instead of O(n)
-- Client remembers last_seen_id from previous page
SELECT product_id, name FROM products
WHERE  product_id > 90000         -- last_seen_id from previous page
ORDER  BY product_id
LIMIT  10;

-- ── Anti-pattern: N+1 query ──────────────────────────────────
-- BAD: one query per row (done in application, not SQL)
-- for each order in orders: SELECT * FROM order_items WHERE order_id = ?

-- GOOD: single JOIN
SELECT o.order_id, p.name, oi.quantity
FROM   orders      o
JOIN   order_items oi USING (order_id)
JOIN   products    p  ON oi.product_id = p.product_id
WHERE  o.customer_id = 1;

-- ── Optimising GROUP BY ───────────────────────────────────────
-- Without index: filesort + temp table
EXPLAIN SELECT category_id, COUNT(*) FROM products GROUP BY category_id;

-- Adding an index on the GROUP BY column eliminates sorting
CREATE INDEX idx_products_category_only ON products(category_id);
EXPLAIN SELECT category_id, COUNT(*) FROM products GROUP BY category_id;

-- ── Query optimisation with deferred join ─────────────────────
-- When paginating a large table with an expensive JOIN, filter IDs first.
-- BAD:
SELECT c.name, o.order_id, o.ordered_at
FROM   customers c JOIN orders o USING (customer_id)
ORDER  BY o.ordered_at DESC
LIMIT  10 OFFSET 10000;

-- GOOD: inner query fetches only IDs (index only), outer join is small
SELECT c.name, o.order_id, o.ordered_at
FROM (
    SELECT order_id FROM orders ORDER BY ordered_at DESC LIMIT 10 OFFSET 10000
) ids
JOIN orders    o ON ids.order_id    = o.order_id
JOIN customers c ON o.customer_id  = c.customer_id;

-- ── Profiling (MySQL) ─────────────────────────────────────────
-- SET profiling = 1;
-- SELECT ...;
-- SHOW PROFILE FOR QUERY 1;
