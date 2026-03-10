"""__init_subclass__, __class_getitem__, and __set_name__ metaprogramming."""


# ── __init_subclass__: hook into subclass creation ───────────────────────────
class Validator:
    """Base class; subclasses must declare `field` and `check` class attributes."""

    _registry: dict[str, type] = {}

    def __init_subclass__(cls, field: str = "", **kwargs):
        super().__init_subclass__(**kwargs)
        if field:
            if not hasattr(cls, "check"):
                raise TypeError(f"{cls.__name__} must define a 'check' method")
            cls.field = field
            Validator._registry[field] = cls

    def validate(self, value) -> bool:
        return self.__class__.check(value)


class PositiveInt(Validator, field="positive_int"):
    @staticmethod
    def check(value) -> bool:
        return isinstance(value, int) and value > 0


class NonEmptyStr(Validator, field="nonempty_str"):
    @staticmethod
    def check(value) -> bool:
        return isinstance(value, str) and len(value.strip()) > 0


print(Validator._registry)

# Validate using the registry
def validate(field: str, value) -> bool:
    cls = Validator._registry.get(field)
    if cls is None:
        raise ValueError(f"No validator for '{field}'")
    return cls().validate(value)

print(validate("positive_int", 5))    # True
print(validate("positive_int", -1))   # False
print(validate("nonempty_str", "hi")) # True
print(validate("nonempty_str", "  ")) # False


# ── __class_getitem__: enable cls[T] syntax ────────────────────────────────────
class TypeCheckedList(list):
    """
    TypeCheckedList[int]() → a list that only accepts ints.
    Uses __class_getitem__ to return a specialised subclass.
    """
    _item_type: type = object

    def __class_getitem__(cls, item_type: type) -> type:
        new_cls = type(
            f"{cls.__name__}[{item_type.__name__}]",
            (cls,),
            {"_item_type": item_type},
        )
        return new_cls

    def append(self, value) -> None:
        if not isinstance(value, self._item_type):
            raise TypeError(
                f"Expected {self._item_type.__name__}, got {type(value).__name__}"
            )
        super().append(value)

    def __iadd__(self, values):
        for v in values:
            self.append(v)
        return self


IntList = TypeCheckedList[int]
il = IntList([1, 2, 3])
il.append(4)
try:
    il.append("x")
except TypeError as e:
    print(e)   # Expected int, got str

StrList = TypeCheckedList[str]
sl = StrList()
sl.append("hello")
print(sl)


# ── __set_name__: descriptor is told its attribute name ──────────────────────
class Bounded:
    """Descriptor that enforces min/max bounds."""

    def __init__(self, lo=None, hi=None):
        self.lo, self.hi = lo, hi
        self._name       = None

    def __set_name__(self, owner, name):
        self._name = f"_{name}"

    def __get__(self, obj, objtype=None):
        return self if obj is None else getattr(obj, self._name, None)

    def __set__(self, obj, value):
        if self.lo is not None and value < self.lo:
            raise ValueError(f"{self._name[1:]} must be >= {self.lo}")
        if self.hi is not None and value > self.hi:
            raise ValueError(f"{self._name[1:]} must be <= {self.hi}")
        setattr(obj, self._name, value)


class RGBColor:
    r = Bounded(0, 255)
    g = Bounded(0, 255)
    b = Bounded(0, 255)

    def __init__(self, r, g, b):
        self.r, self.g, self.b = r, g, b

    def __repr__(self):
        return f"RGB({self.r}, {self.g}, {self.b})"


c = RGBColor(120, 200, 50)
print(c)

try:
    c.r = 300
except ValueError as e:
    print(e)   # r must be <= 255
