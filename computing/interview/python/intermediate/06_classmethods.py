"""Class methods, static methods, and instance methods."""


class BankAccount:
    _interest_rate: float = 0.05   # class variable

    def __init__(self, owner: str, balance: float = 0.0):
        self.owner   = owner
        self._balance = balance    # "private" by convention

    # ── Instance method ───────────────────────────────────────────────────────
    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("amount must be positive")
        self._balance += amount

    def withdraw(self, amount: float) -> None:
        if amount > self._balance:
            raise ValueError("insufficient funds")
        self._balance -= amount

    @property
    def balance(self) -> float:        # read-only property
        return self._balance

    def apply_interest(self) -> None:
        self._balance *= (1 + self._interest_rate)

    def __repr__(self) -> str:
        return f"BankAccount(owner={self.owner!r}, balance={self._balance:.2f})"

    # ── Class method ──────────────────────────────────────────────────────────
    @classmethod
    def set_interest_rate(cls, rate: float) -> None:
        if not (0 <= rate <= 1):
            raise ValueError("rate must be in [0, 1]")
        cls._interest_rate = rate

    @classmethod
    def from_dict(cls, data: dict) -> "BankAccount":
        """Alternative constructor — factory from dict."""
        return cls(data["owner"], data.get("balance", 0.0))

    @classmethod
    def zero_account(cls, owner: str) -> "BankAccount":
        return cls(owner, 0.0)

    # ── Static method ─────────────────────────────────────────────────────────
    @staticmethod
    def is_valid_amount(amount: float) -> bool:
        """Pure utility — no access to instance or class."""
        return isinstance(amount, (int, float)) and amount > 0

    @staticmethod
    def currency_format(amount: float) -> str:
        return f"${amount:,.2f}"


# Usage
acc = BankAccount("Alice", 1000.0)
acc.deposit(500)
acc.apply_interest()
print(acc)
print(acc.balance)

acc2 = BankAccount.from_dict({"owner": "Bob", "balance": 200.0})
print(acc2)

BankAccount.set_interest_rate(0.03)
acc2.apply_interest()
print(acc2)

print(BankAccount.is_valid_amount(-5))    # False
print(BankAccount.currency_format(1234.56))  # $1,234.56


# ── Difference summary ────────────────────────────────────────────────────────
class Demo:
    class_var = "class"

    def instance_method(self):
        print(f"instance_method: self={self}, class_var={self.class_var}")

    @classmethod
    def class_method(cls):
        print(f"class_method: cls={cls}, class_var={cls.class_var}")

    @staticmethod
    def static_method():
        print("static_method: no self or cls")


d = Demo()
d.instance_method()    # has self
Demo.class_method()    # has cls; can also call d.class_method()
Demo.static_method()   # no implicit first arg; callable on class or instance
