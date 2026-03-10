"""Import system: finders, loaders, sys.modules, hooks, and lazy imports."""
import sys
import importlib
import importlib.abc
import importlib.machinery
import importlib.util
import types


# ── sys.modules: the import cache ────────────────────────────────────────────
print("json" in sys.modules)         # False (not yet imported)
import json
print("json" in sys.modules)         # True
print(sys.modules["json"] is json)   # True — same object

# Import the same module twice: Python reuses the cached version
import json as json2
print(json is json2)   # True


# ── Import search path ────────────────────────────────────────────────────────
print("\nsys.path entries (first 3):")
for p in sys.path[:3]:
    print(f"  {p!r}")

print("\nsys.meta_path finders:")
for finder in sys.meta_path:
    print(f"  {type(finder).__name__}")


# ── importlib.import_module: programmatic imports ────────────────────────────
module_name = "collections"
mod = importlib.import_module(module_name)
print(f"\nImported: {mod.__name__}")
print(getattr(mod, "Counter"))


# ── Reloading a module ────────────────────────────────────────────────────────
# Useful during development or for plugin systems
import math as _math
importlib.reload(_math)   # re-executes module code; updates existing references


# ── Lazy import: avoid top-level cost ────────────────────────────────────────
def get_numpy():
    """Import numpy only when first used — avoids startup cost."""
    if "numpy" not in sys.modules:
        try:
            import numpy as _np
            return _np
        except ImportError:
            return None
    return sys.modules["numpy"]


# ── Audit importer (meta path finder) ────────────────────────────────────────
class AuditFinder(importlib.abc.MetaPathFinder):
    """Logs every module that gets imported."""
    _blocked: set[str] = set()

    def find_spec(self, fullname, path, target=None):
        if fullname in self._blocked:
            raise ImportError(f"Import of '{fullname}' is blocked")
        # print(f"[audit] importing: {fullname}")
        return None   # None = let the next finder handle it

audit = AuditFinder()
sys.meta_path.insert(0, audit)

import textwrap   # will be silently logged
sys.meta_path.remove(audit)


# ── Custom in-memory importer ─────────────────────────────────────────────────
_SOURCE = {
    "dynamic_module": """\
MESSAGE = "Hello from a dynamically created module!"

def greet(name):
    return f"{MESSAGE} Hi {name}!"
"""
}

class MemoryFinder(importlib.abc.MetaPathFinder):
    def find_spec(self, fullname, path, target=None):
        if fullname in _SOURCE:
            loader = MemoryLoader(_SOURCE[fullname])
            return importlib.machinery.ModuleSpec(fullname, loader)
        return None

class MemoryLoader(importlib.abc.Loader):
    def __init__(self, source: str):
        self.source = source

    def create_module(self, spec):
        return None   # use default module creation

    def exec_module(self, module):
        exec(compile(self.source, "<memory>", "exec"), module.__dict__)

sys.meta_path.append(MemoryFinder())

import dynamic_module                             # type: ignore
print(dynamic_module.greet("World"))
print(dynamic_module.MESSAGE)

# Clean up
sys.meta_path.pop()
del sys.modules["dynamic_module"]


# ── importlib.util.find_spec: check if a module is available ─────────────────
for name in ["json", "numpy", "nonexistent_lib"]:
    spec = importlib.util.find_spec(name)
    print(f"  {name}: {'found' if spec else 'NOT found'}")


# ── Import a file by absolute path ───────────────────────────────────────────
def import_path(module_name: str, filepath: str) -> types.ModuleType:
    spec   = importlib.util.spec_from_file_location(module_name, filepath)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module

# Example (commented out — requires an actual file):
# m = import_path("my_plugin", "/path/to/plugin.py")
