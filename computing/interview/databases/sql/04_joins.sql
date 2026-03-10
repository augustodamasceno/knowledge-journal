-- ============================================================
-- Joins
-- ============================================================

USE shop;

-- ── INNER JOIN ────────────────────────────────────────────────
-- Only customers who have placed at least one order
SELECT c.name, COUNT(o.order_id) AS order_count
FROM   customers c
INNER JOIN orders o ON c.customer_id = o.customer_id
GROUP  BY c.customer_id, c.name
ORDER  BY order_count DESC;

-- ── LEFT JOIN — include rows with no match ────────────────────
-- ALL customers; order_count = 0 for those with no orders
SELECT c.name, COUNT(o.order_id) AS order_count
FROM   customers c
LEFT  JOIN orders o ON c.customer_id = o.customer_id
GROUP  BY c.customer_id, c.name;

-- Customers who have NEVER ordered (anti-join pattern)
SELECT c.name
FROM   customers c
LEFT  JOIN orders o ON c.customer_id = o.customer_id
WHERE  o.order_id IS NULL;

-- ── RIGHT JOIN ────────────────────────────────────────────────
-- All orders, including those with missing customer records (data integrity check)
SELECT o.order_id, c.name
FROM   customers c
RIGHT JOIN orders o ON c.customer_id = o.customer_id
WHERE  c.customer_id IS NULL;

-- ── FULL OUTER JOIN (MySQL emulation with UNION) ──────────────
SELECT c.name AS customer, o.order_id
FROM   customers c
LEFT  JOIN orders o ON c.customer_id = o.customer_id
UNION
SELECT c.name, o.order_id
FROM   customers c
RIGHT JOIN orders o ON c.customer_id = o.customer_id
WHERE  c.customer_id IS NULL;

-- ── Multi-table JOIN ─────────────────────────────────────────
-- Full order invoice
SELECT
    c.name                                   AS customer,
    o.order_id,
    o.ordered_at,
    o.status,
    p.name                                   AS product,
    oi.quantity,
    oi.unit_price,
    oi.quantity * oi.unit_price              AS line_total
FROM   customers   c
JOIN   orders      o  ON c.customer_id  = o.customer_id
JOIN   order_items oi ON o.order_id     = oi.order_id
JOIN   products    p  ON oi.product_id  = p.product_id
ORDER  BY o.order_id, p.name;

-- ── SELF JOIN — hierarchy traversal (one level) ───────────────
-- Each employee paired with their direct manager
SELECT
    e.name  AS employee,
    m.name  AS manager
FROM   employees e
LEFT  JOIN employees m ON e.manager_id = m.employee_id
ORDER  BY m.name, e.name;

-- ── CROSS JOIN — cartesian product ────────────────────────────
-- All possible (customer, product) pairs — can be large!
SELECT c.name AS customer, p.name AS product
FROM   customers c
CROSS  JOIN products p
LIMIT  20;

-- ── JOIN with aggregation and HAVING ─────────────────────────
-- Products with avg rating >= 4 and at least 2 reviews
SELECT
    p.name,
    ROUND(AVG(r.rating), 2) AS avg_rating,
    COUNT(r.review_id)      AS review_count
FROM   products p
JOIN   reviews  r ON p.product_id = r.product_id
GROUP  BY p.product_id, p.name
HAVING AVG(r.rating) >= 4 AND COUNT(r.review_id) >= 2
ORDER  BY avg_rating DESC;

-- ── Non-equi JOIN ────────────────────────────────────────────
-- Products whose price is higher than another product in the same category
SELECT
    a.name  AS product,
    b.name  AS cheaper_alternative,
    a.price - b.price AS price_diff
FROM  products a
JOIN  products b ON a.category_id = b.category_id
                 AND a.price > b.price
ORDER BY price_diff DESC;
