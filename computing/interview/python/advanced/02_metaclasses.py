"""Metaclasses: type, class creation, and practical patterns."""


# ── type() as a class factory ─────────────────────────────────────────────────
# type(name, bases, namespace) creates a class dynamically
Dog = type("Dog", (object,), {
    "sound": "Woof",
    "speak": lambda self: self.sound,
    "__repr__": lambda self: "Dog()",
})
d = Dog()
print(d.speak())   # Woof


# ── Custom metaclass ──────────────────────────────────────────────────────────
class Meta(type):
    """Metaclass that prints class creation and enforces a naming convention."""

    def __new__(mcs, name, bases, namespace):
        # Enforce: all public method names must be lowercase
        for attr, val in namespace.items():
            if callable(val) and not attr.startswith("_") and attr != attr.lower():
                raise TypeError(
                    f"Method '{attr}' in class '{name}' must be lowercase"
                )
        cls = super().__new__(mcs, name, bases, namespace)
        print(f"[Meta] Created class: {name}")
        return cls

    def __init__(cls, name, bases, namespace):
        super().__init__(name, bases, namespace)

    def __call__(cls, *args, **kwargs):
        instance = super().__call__(*args, **kwargs)
        print(f"[Meta] Created instance of {cls.__name__}")
        return instance


class Service(metaclass=Meta):
    def start(self): print("starting")
    def stop(self):  print("stopping")

s = Service()
s.start()


# ── Singleton via metaclass ───────────────────────────────────────────────────
class SingletonMeta(type):
    _instances: dict = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class Database(metaclass=SingletonMeta):
    def __init__(self, url: str = "localhost"):
        self.url = url

db1 = Database("db://host1")
db2 = Database("db://host2")
print(db1 is db2)          # True — same instance
print(db1.url)             # db://host1


# ── Auto-register subclasses via metaclass ────────────────────────────────────
class PluginMeta(type):
    registry: dict[str, type] = {}

    def __new__(mcs, name, bases, namespace):
        cls = super().__new__(mcs, name, bases, namespace)
        if bases:   # skip the Plugin base class itself
            key = namespace.get("name", name.lower())
            mcs.registry[key] = cls
        return cls


class Plugin(metaclass=PluginMeta):
    name: str = ""


class PDFPlugin(Plugin):
    name = "pdf"
    def process(self): return "processing PDF"


class CSVPlugin(Plugin):
    name = "csv"
    def process(self): return "processing CSV"


class JSONPlugin(Plugin):   # key = "jsonplugin" (no explicit name)
    def process(self): return "processing JSON"


print(PluginMeta.registry)

def get_plugin(fmt: str) -> Plugin:
    cls = PluginMeta.registry.get(fmt)
    if cls is None:
        raise ValueError(f"Unknown format: {fmt}")
    return cls()

print(get_plugin("pdf").process())
print(get_plugin("csv").process())


# ── __prepare__: customise the class namespace ────────────────────────────────
class OrderedMeta(type):
    """Records attribute definition order."""
    @classmethod
    def __prepare__(mcs, name, bases):
        from collections import OrderedDict
        return OrderedDict()

    def __new__(mcs, name, bases, namespace):
        cls = super().__new__(mcs, name, bases, dict(namespace))
        cls._field_order = [k for k in namespace if not k.startswith("_")]
        return cls


class Config(metaclass=OrderedMeta):
    host    = "localhost"
    port    = 5432
    db_name = "mydb"
    timeout = 30

print(Config._field_order)   # ['host', 'port', 'db_name', 'timeout']
