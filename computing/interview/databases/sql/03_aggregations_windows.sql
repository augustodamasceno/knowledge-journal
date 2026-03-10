-- ============================================================
-- Aggregations & Window Functions
-- ============================================================

USE shop;

-- ── Basic aggregations ────────────────────────────────────────
SELECT
    c.name                           AS category,
    COUNT(p.product_id)              AS total_products,
    ROUND(AVG(p.price), 2)           AS avg_price,
    MIN(p.price)                     AS min_price,
    MAX(p.price)                     AS max_price,
    SUM(p.stock * p.price)           AS inventory_value
FROM  products  p
JOIN  categories c ON p.category_id = c.category_id
GROUP BY c.category_id, c.name
HAVING AVG(p.price) > 20
ORDER  BY inventory_value DESC;

-- ── COUNT DISTINCT ───────────────────────────────────────────
SELECT COUNT(DISTINCT customer_id) AS unique_buyers FROM orders;

-- ── GROUP BY with ROLLUP (adds subtotal + grand total rows) ──
SELECT
    c.name     AS category,
    p.name     AS product,
    SUM(oi.quantity * oi.unit_price) AS revenue
FROM  order_items oi
JOIN  products    p  ON oi.product_id = p.product_id
JOIN  categories  c  ON p.category_id = c.category_id
GROUP BY c.name, p.name WITH ROLLUP;

-- ── Window functions ─────────────────────────────────────────
-- ROW_NUMBER / RANK / DENSE_RANK per category
SELECT
    p.name,
    c.name                                         AS category,
    p.price,
    ROW_NUMBER() OVER w                            AS row_num,
    RANK()       OVER w                            AS rnk,
    DENSE_RANK() OVER w                            AS dense_rnk,
    PERCENT_RANK() OVER w                          AS pct_rank
FROM products p
JOIN categories c ON p.category_id = c.category_id
WINDOW w AS (PARTITION BY p.category_id ORDER BY p.price DESC);

-- Top-1 product per category (using CTE + ROW_NUMBER)
WITH ranked AS (
    SELECT p.name, c.name AS category, p.price,
           ROW_NUMBER() OVER (PARTITION BY p.category_id ORDER BY p.price DESC) AS rn
    FROM   products p
    JOIN   categories c ON p.category_id = c.category_id
)
SELECT category, name, price
FROM   ranked
WHERE  rn = 1;

-- ── Running total and moving average ─────────────────────────
WITH daily_revenue AS (
    SELECT
        DATE(o.ordered_at)               AS day,
        SUM(oi.quantity * oi.unit_price) AS revenue
    FROM   orders o
    JOIN   order_items oi USING (order_id)
    WHERE  o.status != 'cancelled'
    GROUP  BY DATE(o.ordered_at)
)
SELECT
    day,
    revenue,
    SUM(revenue)  OVER (ORDER BY day ROWS UNBOUNDED PRECEDING) AS running_total,
    AVG(revenue)  OVER (ORDER BY day ROWS 6 PRECEDING)         AS moving_avg_7d
FROM daily_revenue
ORDER BY day;

-- ── LAG / LEAD — compare to adjacent rows ────────────────────
WITH daily_revenue AS (
    SELECT DATE(o.ordered_at) AS day,
           SUM(oi.quantity * oi.unit_price) AS revenue
    FROM   orders o JOIN order_items oi USING (order_id)
    WHERE  o.status != 'cancelled'
    GROUP  BY DATE(o.ordered_at)
)
SELECT
    day,
    revenue,
    LAG (revenue, 1, 0) OVER (ORDER BY day) AS prev_day_revenue,
    LEAD(revenue, 1, 0) OVER (ORDER BY day) AS next_day_revenue,
    ROUND(revenue - LAG(revenue, 1, 0) OVER (ORDER BY day), 2) AS day_over_day_change
FROM daily_revenue;

-- ── FIRST_VALUE / LAST_VALUE ─────────────────────────────────
SELECT
    name,
    price,
    FIRST_VALUE(name) OVER (PARTITION BY category_id ORDER BY price ASC
                            ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING)
        AS cheapest_in_category,
    LAST_VALUE(name)  OVER (PARTITION BY category_id ORDER BY price ASC
                            ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING)
        AS priciest_in_category
FROM products;

-- ── NTILE — divide rows into N buckets ───────────────────────
SELECT
    name, price,
    NTILE(4) OVER (ORDER BY price) AS price_quartile
FROM products;
