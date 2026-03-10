-- ============================================================
-- DDL — Schema Design
-- Dialect: MySQL 8 / MariaDB (minor syntax differences noted)
-- ============================================================

CREATE DATABASE IF NOT EXISTS shop CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE shop;

-- ── Customers ────────────────────────────────────────────────
CREATE TABLE customers (
    customer_id INT            PRIMARY KEY AUTO_INCREMENT,
    email       VARCHAR(255)   NOT NULL UNIQUE,
    name        VARCHAR(100)   NOT NULL,
    phone       VARCHAR(30),
    city        VARCHAR(100),
    created_at  TIMESTAMP      NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at  TIMESTAMP      NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- ── Categories ───────────────────────────────────────────────
CREATE TABLE categories (
    category_id   INT          PRIMARY KEY AUTO_INCREMENT,
    name          VARCHAR(100) NOT NULL UNIQUE,
    parent_id     INT,                            -- self-referencing FK for subcategories
    FOREIGN KEY (parent_id) REFERENCES categories(category_id)
);

-- ── Products ─────────────────────────────────────────────────
CREATE TABLE products (
    product_id  INT            PRIMARY KEY AUTO_INCREMENT,
    sku         VARCHAR(50)    NOT NULL UNIQUE,
    name        VARCHAR(200)   NOT NULL,
    description TEXT,
    price       DECIMAL(10, 2) NOT NULL CHECK (price >= 0),
    stock       INT            NOT NULL DEFAULT 0 CHECK (stock >= 0),
    category_id INT,
    created_at  TIMESTAMP      NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES categories(category_id) ON DELETE SET NULL
);

-- ── Orders ───────────────────────────────────────────────────
CREATE TABLE orders (
    order_id    INT       PRIMARY KEY AUTO_INCREMENT,
    customer_id INT       NOT NULL,
    status      ENUM('pending', 'processing', 'shipped', 'delivered', 'cancelled')
                          NOT NULL DEFAULT 'pending',
    ordered_at  TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    shipped_at  TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE
);

-- ── Order Items (junction table with payload) ─────────────────
CREATE TABLE order_items (
    order_id   INT            NOT NULL,
    product_id INT            NOT NULL,
    quantity   INT            NOT NULL CHECK (quantity > 0),
    unit_price DECIMAL(10, 2) NOT NULL CHECK (unit_price >= 0),
    PRIMARY KEY (order_id, product_id),
    FOREIGN KEY (order_id)   REFERENCES orders(order_id)   ON DELETE CASCADE,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE RESTRICT
);

-- ── Reviews ──────────────────────────────────────────────────
CREATE TABLE reviews (
    review_id   INT       PRIMARY KEY AUTO_INCREMENT,
    product_id  INT       NOT NULL,
    customer_id INT       NOT NULL,
    rating      TINYINT   NOT NULL CHECK (rating BETWEEN 1 AND 5),
    body        TEXT,
    created_at  TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    UNIQUE KEY uq_review (product_id, customer_id),   -- one review per customer per product
    FOREIGN KEY (product_id)  REFERENCES products(product_id)  ON DELETE CASCADE,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE
);

-- ── Employees (self-referencing for hierarchy) ────────────────
CREATE TABLE employees (
    employee_id INT         PRIMARY KEY AUTO_INCREMENT,
    name        VARCHAR(100) NOT NULL,
    role        VARCHAR(50),
    manager_id  INT,
    FOREIGN KEY (manager_id) REFERENCES employees(employee_id)
);

-- ── Altering tables ───────────────────────────────────────────
ALTER TABLE customers ADD COLUMN loyalty_points INT NOT NULL DEFAULT 0;
ALTER TABLE products  MODIFY COLUMN description TEXT NOT NULL;
ALTER TABLE products  ADD COLUMN is_active TINYINT(1) NOT NULL DEFAULT 1;

-- Rename a column (MySQL 8+)
-- ALTER TABLE customers RENAME COLUMN phone TO phone_number;

-- Drop a column
-- ALTER TABLE customers DROP COLUMN loyalty_points;

-- ── Views ─────────────────────────────────────────────────────
CREATE OR REPLACE VIEW vw_product_summary AS
SELECT
    p.product_id,
    p.name,
    p.price,
    p.stock,
    c.name        AS category,
    AVG(r.rating) AS avg_rating,
    COUNT(r.review_id) AS review_count
FROM     products p
LEFT JOIN categories c ON p.category_id = c.category_id
LEFT JOIN reviews    r ON p.product_id  = r.product_id
GROUP BY p.product_id, p.name, p.price, p.stock, c.name;
