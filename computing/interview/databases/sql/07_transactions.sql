-- ============================================================
-- Transactions & ACID
-- ============================================================

USE shop;

-- ── Simple transfer — atomicity in practice ───────────────────
-- Both updates must succeed or neither should apply.
CREATE TABLE accounts (
    account_id INT          PRIMARY KEY AUTO_INCREMENT,
    owner      VARCHAR(100) NOT NULL,
    balance    DECIMAL(12, 2) NOT NULL DEFAULT 0 CHECK (balance >= 0)
);

INSERT INTO accounts (owner, balance) VALUES ('Alice', 1000.00), ('Bob', 500.00);

START TRANSACTION;

UPDATE accounts SET balance = balance - 200.00 WHERE account_id = 1;
UPDATE accounts SET balance = balance + 200.00 WHERE account_id = 2;

-- Verify before committing
SELECT * FROM accounts;

COMMIT;

-- ── Rollback on error ─────────────────────────────────────────
START TRANSACTION;

UPDATE accounts SET balance = balance - 9999.00 WHERE account_id = 1;
-- CHECK constraint would fail; in application code you'd catch the error:
-- IF error THEN ROLLBACK; END IF;

ROLLBACK;   -- undo all changes in this transaction

-- ── Savepoints ────────────────────────────────────────────────
START TRANSACTION;

INSERT INTO orders (customer_id, status) VALUES (1, 'pending');
-- Assume @@last_insert_id gives us the new order_id
SAVEPOINT order_created;

INSERT INTO order_items (order_id, product_id, quantity, unit_price)
VALUES (LAST_INSERT_ID(), 1, 2, 79.99);

SAVEPOINT items_added;

-- Simulate an error on a second batch of items
INSERT INTO order_items (order_id, product_id, quantity, unit_price)
VALUES (LAST_INSERT_ID(), 999, 1, 0);   -- product 999 does not exist → FK error

-- Roll back only the failed batch, keep the first items
ROLLBACK TO SAVEPOINT items_added;

COMMIT;   -- commits order + first items

-- ── Isolation levels ─────────────────────────────────────────
-- Default in MySQL InnoDB: REPEATABLE READ
SHOW VARIABLES LIKE 'transaction_isolation';

-- Set for the current session
SET SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED;

-- Demonstrate READ COMMITTED vs REPEATABLE READ
-- (requires two concurrent sessions to fully demonstrate)
--
-- Session A                          Session B
-- START TRANSACTION;
-- SELECT balance FROM accounts       < not yet visible in A under REPEATABLE READ
-- WHERE account_id = 1;  -> 800
--                                    START TRANSACTION;
--                                    UPDATE accounts SET balance = 900 WHERE account_id = 1;
--                                    COMMIT;
-- SELECT balance FROM accounts
-- WHERE account_id = 1;  -> 800 (REPEATABLE READ) | 900 (READ COMMITTED)
-- COMMIT;

-- ── Locking ──────────────────────────────────────────────────
-- SELECT ... FOR UPDATE: pessimistic lock (row-level, blocks other writers)
START TRANSACTION;
SELECT * FROM accounts WHERE account_id = 1 FOR UPDATE;
UPDATE accounts SET balance = balance - 100 WHERE account_id = 1;
COMMIT;

-- SELECT ... LOCK IN SHARE MODE: shared lock (multiple readers, blocks writers)
START TRANSACTION;
SELECT * FROM products WHERE product_id = 1 LOCK IN SHARE MODE;
COMMIT;

-- ── Deadlock example (educational) ───────────────────────────
-- Session A: locks row 1, then tries to lock row 2
-- Session B: locks row 2, then tries to lock row 1
-- → InnoDB detects the cycle and rolls back the younger transaction.
-- Prevention: always acquire locks in the same global order.

-- Reset isolation level to default
SET SESSION TRANSACTION ISOLATION LEVEL REPEATABLE READ;
