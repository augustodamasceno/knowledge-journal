"""Descriptors: __get__, __set__, __delete__, __set_name__."""


# ── Non-data descriptor (only __get__) ────────────────────────────────────────
class CachedProperty:
    """Compute on first access, then cache on the instance."""
    def __init__(self, func):
        self.func      = func
        self.attr_name = None

    def __set_name__(self, owner, name):
        self.attr_name = name   # called when class is defined

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self         # accessed on the class itself → return descriptor
        value = self.func(obj)
        setattr(obj, self.attr_name, value)   # shadow the descriptor on the instance
        return value


class DataSet:
    def __init__(self, data: list[float]):
        self.data = data

    @CachedProperty
    def mean(self) -> float:
        print("[computing mean]")
        return sum(self.data) / len(self.data)

    @CachedProperty
    def variance(self) -> float:
        print("[computing variance]")
        m = self.mean
        return sum((x - m) ** 2 for x in self.data) / len(self.data)


ds = DataSet([1, 2, 3, 4, 5])
print(ds.mean)      # computes, caches
print(ds.mean)      # returns cached value (no print)
print(ds.variance)


# ── Data descriptor (both __get__ and __set__) ────────────────────────────────
class Typed:
    def __init__(self, expected_type, nullable: bool = False):
        self.expected_type = expected_type
        self.nullable      = nullable
        self.name          = None

    def __set_name__(self, owner, name):
        self.name = f"_{name}"   # store under private name to avoid recursion

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return getattr(obj, self.name, None)

    def __set__(self, obj, value):
        if value is None and self.nullable:
            setattr(obj, self.name, None)
            return
        if not isinstance(value, self.expected_type):
            raise TypeError(
                f"'{self.name[1:]}' expected {self.expected_type.__name__}, "
                f"got {type(value).__name__}"
            )
        setattr(obj, self.name, value)

    def __delete__(self, obj):
        setattr(obj, self.name, None)


class Employee:
    name  = Typed(str)
    age   = Typed(int)
    email = Typed(str, nullable=True)

    def __init__(self, name: str, age: int, email: str = None):
        self.name  = name
        self.age   = age
        self.email = email

    def __repr__(self) -> str:
        return f"Employee(name={self.name!r}, age={self.age}, email={self.email!r})"


e = Employee("Alice", 30, "alice@example.com")
print(e)

try:
    e.age = "thirty"
except TypeError as err:
    print(err)   # 'age' expected int, got str

try:
    e.name = None
except TypeError as err:
    print(err)   # 'name' expected str, got NoneType

# email is nullable
e.email = None
print(e)


# ── property as a built-in data descriptor ────────────────────────────────────
class Temperature:
    def __init__(self, celsius: float):
        self._celsius = celsius

    @property
    def celsius(self) -> float:
        return self._celsius

    @celsius.setter
    def celsius(self, value: float):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero")
        self._celsius = value

    @property
    def fahrenheit(self) -> float:
        return self._celsius * 9 / 5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value: float):
        self.celsius = (value - 32) * 5 / 9


t = Temperature(0)
print(t.fahrenheit)     # 32.0
t.fahrenheit = 212.0
print(t.celsius)        # 100.0
