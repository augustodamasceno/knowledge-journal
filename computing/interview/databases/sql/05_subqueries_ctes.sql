-- ============================================================
-- Subqueries & CTEs
-- ============================================================

USE shop;

-- ── Scalar subquery in SELECT ─────────────────────────────────
SELECT
    name,
    price,
    (SELECT ROUND(AVG(price), 2) FROM products) AS overall_avg,
    price - (SELECT AVG(price) FROM products)   AS diff_from_avg
FROM products;

-- ── Subquery in WHERE ─────────────────────────────────────────
-- Products more expensive than the category average
SELECT p.name, p.price, c.name AS category
FROM   products p
JOIN   categories c ON p.category_id = c.category_id
WHERE  p.price > (
    SELECT AVG(p2.price)
    FROM   products p2
    WHERE  p2.category_id = p.category_id      -- correlated subquery
);

-- ── EXISTS ────────────────────────────────────────────────────
-- Customers who have placed at least one delivered order
SELECT name
FROM   customers c
WHERE  EXISTS (
    SELECT 1 FROM orders o
    WHERE  o.customer_id = c.customer_id
      AND  o.status = 'delivered'
);

-- Customers who have NEVER ordered (NOT EXISTS)
SELECT name
FROM   customers c
WHERE  NOT EXISTS (
    SELECT 1 FROM orders o WHERE o.customer_id = c.customer_id
);

-- ── IN / NOT IN ───────────────────────────────────────────────
-- Orders containing Electronics products
SELECT DISTINCT o.order_id, o.ordered_at
FROM   orders o
JOIN   order_items oi USING (order_id)
WHERE  oi.product_id IN (
    SELECT p.product_id
    FROM   products p
    JOIN   categories c ON p.category_id = c.category_id
    WHERE  c.name = 'Electronics'
);

-- ── Derived table (subquery in FROM) ─────────────────────────
SELECT customer, total
FROM (
    SELECT c.name AS customer,
           SUM(oi.quantity * oi.unit_price) AS total
    FROM   customers   c
    JOIN   orders      o  USING (customer_id)
    JOIN   order_items oi USING (order_id)
    WHERE  o.status != 'cancelled'
    GROUP  BY c.customer_id
) AS customer_totals
WHERE total > 100
ORDER BY total DESC;

-- ── CTE — readable alternative to derived tables ─────────────
WITH customer_totals AS (
    SELECT
        c.customer_id,
        c.name,
        SUM(oi.quantity * oi.unit_price) AS lifetime_value
    FROM   customers   c
    JOIN   orders      o  USING (customer_id)
    JOIN   order_items oi USING (order_id)
    WHERE  o.status != 'cancelled'
    GROUP  BY c.customer_id, c.name
),
top_customers AS (
    SELECT * FROM customer_totals
    WHERE  lifetime_value > (SELECT AVG(lifetime_value) FROM customer_totals)
)
SELECT name, lifetime_value
FROM   top_customers
ORDER  BY lifetime_value DESC;

-- ── Multiple CTEs chained ────────────────────────────────────
WITH
product_revenue AS (
    SELECT
        oi.product_id,
        SUM(oi.quantity * oi.unit_price) AS revenue,
        SUM(oi.quantity)                 AS units_sold
    FROM   order_items oi
    JOIN   orders o USING (order_id)
    WHERE  o.status = 'delivered'
    GROUP  BY oi.product_id
),
ranked_products AS (
    SELECT
        p.name,
        c.name AS category,
        pr.revenue,
        pr.units_sold,
        RANK() OVER (PARTITION BY p.category_id ORDER BY pr.revenue DESC) AS cat_rank
    FROM   product_revenue pr
    JOIN   products    p ON pr.product_id = p.product_id
    JOIN   categories  c ON p.category_id = c.category_id
)
SELECT category, name, revenue, units_sold
FROM   ranked_products
WHERE  cat_rank = 1;   -- best-selling product per category

-- ── Recursive CTE — organisational hierarchy ─────────────────
WITH RECURSIVE org_tree AS (
    -- Anchor: root employees (no manager)
    SELECT employee_id, name, role, manager_id, 0 AS depth,
           CAST(name AS CHAR(500)) AS path
    FROM   employees
    WHERE  manager_id IS NULL

    UNION ALL

    -- Recursive step: employees whose manager is already in the tree
    SELECT e.employee_id, e.name, e.role, e.manager_id,
           ot.depth + 1,
           CONCAT(ot.path, ' > ', e.name)
    FROM   employees e
    JOIN   org_tree  ot ON e.manager_id = ot.employee_id
)
SELECT LPAD('', depth * 4, ' ') AS indent, name, role, depth, path
FROM   org_tree
ORDER  BY path;
