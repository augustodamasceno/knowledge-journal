-- ============================================================
-- DML — INSERT / UPDATE / DELETE / SELECT
-- Run after 01_ddl_schema.sql
-- ============================================================

USE shop;

-- ── Seed data ─────────────────────────────────────────────────
INSERT INTO categories (name) VALUES
    ('Electronics'), ('Books'), ('Accessories'), ('Clothing');

INSERT INTO categories (name, parent_id) VALUES
    ('Audio',   1),   -- child of Electronics
    ('Laptops', 1);

INSERT INTO employees (name, role, manager_id) VALUES
    ('CEO', 'Executive', NULL);                 -- id 1
INSERT INTO employees (name, role, manager_id) VALUES
    ('VP Engineering', 'VP', 1),               -- id 2
    ('VP Sales',       'VP', 1);               -- id 3
INSERT INTO employees (name, role, manager_id) VALUES
    ('Engineer A', 'SWE', 2),
    ('Engineer B', 'SWE', 2),
    ('Sales Rep',  'Rep', 3);

INSERT INTO customers (email, name, city) VALUES
    ('alice@example.com',   'Alice',   'New York'),
    ('bob@example.com',     'Bob',     'Austin'),
    ('carol@example.com',   'Carol',   'New York'),
    ('dave@example.com',    'Dave',    'Seattle'),
    ('eve@example.com',     'Eve',     'Austin');

INSERT INTO products (sku, name, price, stock, category_id) VALUES
    ('HDX-100', 'Wireless Headphones', 79.99,  200, 5),
    ('HDX-200', 'Studio Monitor Headphones', 199.99, 50, 5),
    ('CAB-001', 'USB-C Cable 1m',       9.99,  500, 3),
    ('STD-010', 'Aluminium Laptop Stand', 34.99, 150, 3),
    ('BK-ALGO', 'Introduction to Algorithms (CLRS)', 59.99, 80, 2),
    ('LPT-PRO', 'Pro Laptop 15"', 1299.99, 30, 6);

INSERT INTO orders (customer_id, status, ordered_at) VALUES
    (1, 'delivered', '2024-01-10 09:00:00'),
    (1, 'delivered', '2024-03-15 14:30:00'),
    (2, 'shipped',   '2024-03-20 11:00:00'),
    (3, 'pending',   '2024-04-01 08:00:00'),
    (4, 'delivered', '2024-02-14 16:00:00'),
    (5, 'cancelled', '2024-01-25 10:00:00');

INSERT INTO order_items (order_id, product_id, quantity, unit_price) VALUES
    (1, 1, 1, 79.99),
    (1, 3, 2, 9.99),
    (2, 2, 1, 199.99),
    (2, 5, 1, 59.99),
    (3, 4, 1, 34.99),
    (4, 1, 1, 79.99),
    (5, 6, 1, 1299.99),
    (6, 1, 1, 79.99);

INSERT INTO reviews (product_id, customer_id, rating, body) VALUES
    (1, 1, 5, 'Amazing sound quality!'),
    (1, 2, 4, 'Good but a bit tight on the head.'),
    (5, 4, 5, 'Best algorithms book.'),
    (6, 4, 5, 'Fast laptop, worth every cent.');

-- ── Basic SELECT ──────────────────────────────────────────────
-- All products sorted by price descending
SELECT name, price, stock
FROM   products
ORDER  BY price DESC;

-- Filtering: cheap accessories in stock
SELECT name, price
FROM   products
WHERE  category_id = 3
  AND  price < 20
  AND  stock > 0
ORDER  BY price;

-- BETWEEN, LIKE, IN
SELECT * FROM products WHERE price BETWEEN 50 AND 200;
SELECT * FROM customers WHERE email LIKE '%@example.com';
SELECT * FROM orders   WHERE status IN ('pending', 'processing');

-- NULL check
SELECT name FROM customers WHERE phone IS NULL;

-- Pagination: page 2 (10 rows per page)
SELECT product_id, name, price
FROM   products
ORDER  BY product_id
LIMIT  10 OFFSET 10;

-- ── UPDATE ────────────────────────────────────────────────────
-- Apply 10% discount to all Electronics
UPDATE products
SET    price = ROUND(price * 0.90, 2)
WHERE  category_id IN (SELECT category_id FROM categories WHERE name = 'Electronics');

-- Conditional update using CASE
UPDATE orders
SET    status = CASE
    WHEN TIMESTAMPDIFF(DAY, ordered_at, NOW()) > 30 THEN 'cancelled'
    ELSE status
END
WHERE  status = 'pending';

-- ── DELETE ────────────────────────────────────────────────────
-- Safe delete: cancelled orders older than 90 days
DELETE FROM orders
WHERE  status = 'cancelled'
  AND  ordered_at < DATE_SUB(NOW(), INTERVAL 90 DAY);

-- TRUNCATE (DDL): fast, resets AUTO_INCREMENT — use with care
-- TRUNCATE TABLE reviews;
