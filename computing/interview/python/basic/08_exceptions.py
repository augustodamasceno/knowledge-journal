"""Exception handling: catch, raise, chain, and custom exceptions."""

# ── Basic try/except/else/finally ─────────────────────────────────────────────
def safe_divide(a: float, b: float) -> float:
    try:
        result = a / b
    except ZeroDivisionError as e:
        print(f"Error: {e}")
        return float("inf")
    except TypeError as e:
        print(f"Wrong type: {e}")
        raise
    else:
        print("Division succeeded")   # only if no exception
        return result
    finally:
        print("always runs")          # cleanup, even after re-raise

print(safe_divide(10, 2))
print(safe_divide(10, 0))

# ── Exception hierarchy ───────────────────────────────────────────────────────
# BaseException
#   ├─ SystemExit
#   ├─ KeyboardInterrupt
#   └─ Exception
#        ├─ ArithmeticError (ZeroDivisionError, OverflowError)
#        ├─ LookupError    (KeyError, IndexError)
#        ├─ TypeError
#        ├─ ValueError
#        ├─ OSError        (FileNotFoundError, PermissionError, …)
#        └─ RuntimeError   (RecursionError, …)

# ── Multiple exceptions ───────────────────────────────────────────────────────
def parse(value):
    try:
        return int(value)
    except (TypeError, ValueError) as e:
        print(f"Cannot parse {value!r}: {e}")
        return None

# ── Exception chaining ────────────────────────────────────────────────────────
def load_config(path: str) -> dict:
    try:
        with open(path) as f:
            import json
            return json.load(f)
    except FileNotFoundError as e:
        raise RuntimeError(f"Config file missing: {path}") from e
    except json.JSONDecodeError as e:
        raise RuntimeError("Config is not valid JSON") from e

# ── Suppress specific exceptions ──────────────────────────────────────────────
from contextlib import suppress

with suppress(FileNotFoundError):
    open("nonexistent.txt")

# ── Custom exceptions ─────────────────────────────────────────────────────────
class AppError(Exception):
    """Base class for app-specific errors."""

class NotFoundError(AppError):
    def __init__(self, resource: str, id: int):
        super().__init__(f"{resource} with id={id} not found")
        self.resource = resource
        self.id = id

class ValidationError(AppError):
    def __init__(self, field: str, message: str):
        super().__init__(f"Validation failed for '{field}': {message}")
        self.field   = field
        self.message = message

class InsufficientFundsError(AppError):
    def __init__(self, amount: float, balance: float):
        super().__init__(
            f"Cannot withdraw {amount:.2f}; balance is {balance:.2f}"
        )
        self.amount  = amount
        self.balance = balance

def withdraw(balance: float, amount: float) -> float:
    if amount <= 0:
        raise ValidationError("amount", "must be positive")
    if amount > balance:
        raise InsufficientFundsError(amount, balance)
    return balance - amount

try:
    withdraw(100.0, 200.0)
except InsufficientFundsError as e:
    print(e)
    print(f"Attempted: {e.amount}, Available: {e.balance}")

# ── Re-raising ────────────────────────────────────────────────────────────────
import logging

def process(data):
    try:
        return int(data)
    except ValueError:
        logging.error("Invalid data received", exc_info=True)
        raise   # re-raise preserving original traceback

# ── Exception groups (Python 3.11+) ──────────────────────────────────────────
# try:
#     raise ExceptionGroup("batch", [ValueError("bad"), TypeError("wrong")])
# except* ValueError as eg:
#     print(f"Value errors: {eg.exceptions}")
# except* TypeError as eg:
#     print(f"Type errors: {eg.exceptions}")
