-- ============================================================
-- Indexes — creation, usage, and analysis
-- ============================================================

USE shop;

-- ── Show existing indexes ────────────────────────────────────
SHOW INDEX FROM products;
SHOW INDEX FROM orders;

-- ── Single-column index ───────────────────────────────────────
CREATE INDEX idx_products_category ON products(category_id);
CREATE INDEX idx_orders_status     ON orders(status);
CREATE INDEX idx_orders_customer   ON orders(customer_id);

-- ── Unique index (also enforces constraint) ───────────────────
CREATE UNIQUE INDEX idx_products_sku ON products(sku);

-- ── Composite index ───────────────────────────────────────────
-- Useful for: WHERE category_id = ? AND price < ?
-- Also helps: ORDER BY price within a category
CREATE INDEX idx_products_cat_price ON products(category_id, price);

-- Rule: the index is used for queries that match a LEFT PREFIX of the columns.
-- (category_id)           → uses the index ✓
-- (category_id, price)    → uses the index ✓
-- (price)                 → does NOT use this index ✗
-- (price, category_id)    → does NOT use this index ✗

-- ── Covering index — all needed columns are in the index ──────
-- Query: SELECT order_id, product_id, quantity, unit_price FROM order_items WHERE order_id = ?
-- This index covers the query completely (no table lookup needed)
CREATE INDEX idx_order_items_cover
    ON order_items(order_id, product_id, quantity, unit_price);

-- ── Full-text index (MySQL InnoDB) ───────────────────────────
CREATE FULLTEXT INDEX idx_products_name ON products(name, description);

-- Natural language mode
SELECT name FROM products
WHERE MATCH(name, description) AGAINST('wireless headphones');

-- Boolean mode (supports +, -, *)
SELECT name FROM products
WHERE MATCH(name, description) AGAINST('+wireless -cheap' IN BOOLEAN MODE);

-- ── EXPLAIN — check whether index is used ────────────────────
-- Look for: type = ref/range (good), key = your index (good), type = ALL (bad)
EXPLAIN SELECT name, price FROM products WHERE category_id = 1 AND price < 100;
EXPLAIN SELECT * FROM orders WHERE customer_id = 2 ORDER BY ordered_at DESC;

-- ── Common anti-patterns that prevent index use ───────────────

-- BAD: function on indexed column — full scan
EXPLAIN SELECT * FROM orders WHERE YEAR(ordered_at) = 2024;

-- GOOD: range on the column itself
EXPLAIN SELECT * FROM orders
WHERE ordered_at BETWEEN '2024-01-01' AND '2024-12-31 23:59:59';

-- BAD: leading wildcard — full scan
EXPLAIN SELECT * FROM customers WHERE email LIKE '%@gmail.com';

-- GOOD: trailing wildcard can use an index
EXPLAIN SELECT * FROM customers WHERE email LIKE 'alice%';

-- BAD: implicit type cast nullifies index
-- (customer_id is INT but comparing to a string)
EXPLAIN SELECT * FROM orders WHERE customer_id = '2';   -- often still uses index, but avoid

-- ── Drop index ────────────────────────────────────────────────
-- DROP INDEX idx_products_category ON products;
