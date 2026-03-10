"""Multiple inheritance and the C3 Method Resolution Order (MRO)."""


# ── Classic diamond problem ────────────────────────────────────────────────────
class A:
    def greet(self):
        return "A"

class B(A):
    def greet(self):
        return "B → " + super().greet()

class C(A):
    def greet(self):
        return "C → " + super().greet()

class D(B, C):
    def greet(self):
        return "D → " + super().greet()

d = D()
print(d.greet())        # D → B → C → A
print(D.__mro__)
# (<class 'D'>, <class 'B'>, <class 'C'>, <class 'A'>, <class 'object'>)

# Each super() in the chain uses the MRO to find the NEXT class —
# not necessarily the direct parent. This ensures A.greet() is called once.


# ── Mixin pattern ─────────────────────────────────────────────────────────────
class JsonMixin:
    def to_json(self) -> str:
        import json
        return json.dumps(self.__dict__, default=str)

    @classmethod
    def from_json(cls, data: str) -> "JsonMixin":
        import json
        obj = cls.__new__(cls)
        obj.__dict__.update(json.loads(data))
        return obj


class LogMixin:
    def log(self, msg: str) -> None:
        import logging
        logging.info(f"[{type(self).__name__}] {msg}")

    def warning(self, msg: str) -> None:
        import logging
        logging.warning(f"[{type(self).__name__}] {msg}")


class ValidationMixin:
    _validators: dict = {}

    def validate(self) -> list[str]:
        errors = []
        for field, check in self._validators.items():
            value = getattr(self, field, None)
            if not check(value):
                errors.append(f"Validation failed for '{field}': {value!r}")
        return errors


class User(LogMixin, JsonMixin, ValidationMixin):
    _validators = {
        "name":  lambda v: isinstance(v, str) and len(v) > 0,
        "email": lambda v: isinstance(v, str) and "@" in v,
        "age":   lambda v: isinstance(v, int) and 0 <= v <= 150,
    }

    def __init__(self, name: str, email: str, age: int):
        self.name  = name
        self.email = email
        self.age   = age


u = User("Alice", "alice@example.com", 30)
print(u.to_json())
print(u.validate())    # []

u2 = User("", "not-an-email", -1)
print(u2.validate())   # three errors

# ── super() in __init__ ───────────────────────────────────────────────────────
class Base:
    def __init__(self, x):
        print(f"Base.__init__(x={x})")
        self.x = x

class Left(Base):
    def __init__(self, x, y):
        print(f"Left.__init__(x={x}, y={y})")
        super().__init__(x)     # passes up the MRO
        self.y = y

class Right(Base):
    def __init__(self, x, z):
        print(f"Right.__init__(x={x}, z={z})")
        super().__init__(x)
        self.z = z

# For cooperative multiple inheritance all __init__ signatures must be
# compatible (use **kwargs to pass unknown args along the MRO).
class Combined(Left, Right):
    def __init__(self, x, y, z):
        # Left → Right → Base (MRO order)
        # Simple two-path case: call parents explicitly
        Left.__init__(self, x, y)
        Right.__init__(self, x, z)

c = Combined(1, 2, 3)
print(vars(c))   # {'x': 1, 'y': 2, 'z': 3}

# ── Checking MRO ─────────────────────────────────────────────────────────────
print([cls.__name__ for cls in User.__mro__])
print(isinstance(u, (LogMixin, JsonMixin)))   # True
print(issubclass(User, ValidationMixin))      # True
