"""C extensions and ctypes: calling native code from Python."""
import ctypes
import ctypes.util
import struct
import sys


# ── ctypes: calling libc functions ────────────────────────────────────────────
if sys.platform == "win32":
    libc_name = "msvcrt"
else:
    libc_name = ctypes.util.find_library("c")

libc = ctypes.CDLL(libc_name)

# strlen
libc.strlen.restype  = ctypes.c_size_t
libc.strlen.argtypes = [ctypes.c_char_p]
print(f"strlen('hello') = {libc.strlen(b'hello')}")   # 5

# abs (integer absolute value)
libc.abs.restype  = ctypes.c_int
libc.abs.argtypes = [ctypes.c_int]
print(f"abs(-42) = {libc.abs(-42)}")   # 42


# ── ctypes data types cheatsheet ──────────────────────────────────────────────
# Python type → ctypes type
# int          → c_int, c_long, c_longlong
# float        → c_float, c_double
# bytes        → c_char_p (null-terminated)
# bool         → c_bool
# void *       → c_void_p
# T *          → POINTER(T)
# T[n]         → T * n (e.g., c_int * 5)


# ── Structures ────────────────────────────────────────────────────────────────
class Point2D(ctypes.Structure):
    _fields_ = [("x", ctypes.c_double),
                ("y", ctypes.c_double)]

p = Point2D(3.0, 4.0)
print(f"Point({p.x}, {p.y})")

# Access raw bytes
raw = bytes(p)
print(f"Raw bytes: {raw.hex()}")
x_back, y_back = struct.unpack("dd", raw)
print(f"Unpacked:  ({x_back}, {y_back})")


# ── Callbacks: passing a Python function to C ─────────────────────────────────
# Define the C callback type: int (*comparator)(const void *, const void *)
COMPARATOR = ctypes.CFUNCTYPE(ctypes.c_int,
                               ctypes.c_void_p,
                               ctypes.c_void_p)

def py_comparator(a_ptr, b_ptr):
    a = ctypes.cast(a_ptr, ctypes.POINTER(ctypes.c_int)).contents.value
    b = ctypes.cast(b_ptr, ctypes.POINTER(ctypes.c_int)).contents.value
    return (a > b) - (a < b)

# Use qsort from libc
if sys.platform != "win32":
    libc.qsort.restype  = None
    libc.qsort.argtypes = [
        ctypes.c_void_p,
        ctypes.c_size_t,
        ctypes.c_size_t,
        COMPARATOR,
    ]

    IntArray5 = ctypes.c_int * 5
    arr = IntArray5(5, 1, 3, 2, 4)
    libc.qsort(arr, 5, ctypes.sizeof(ctypes.c_int), COMPARATOR(py_comparator))
    print(f"qsort result: {list(arr)}")   # [1, 2, 3, 4, 5]


# ── Sketch: Writing a C extension module ─────────────────────────────────────
# File: myext.c
# #include <Python.h>
#
# static PyObject *
# py_add(PyObject *self, PyObject *args)
# {
#     long a, b;
#     if (!PyArg_ParseTuple(args, "ll", &a, &b))
#         return NULL;
#     return PyLong_FromLong(a + b);
# }
#
# static PyMethodDef methods[] = {
#     {"add", py_add, METH_VARARGS, "Add two integers."},
#     {NULL, NULL, 0, NULL}
# };
#
# static struct PyModuleDef module = {
#     PyModuleDef_HEAD_INIT, "myext", NULL, -1, methods
# };
#
# PyMODINIT_FUNC
# PyInit_myext(void) { return PyModule_Create(&module); }

# Build:
#   python setup.py build_ext --inplace
#
# Or use cffi (API mode — safer, easier):
# from cffi import FFI
# ffi = FFI()
# ffi.cdef("long add(long a, long b);")
# lib = ffi.verify("long add(long a, long b) { return a + b; }")
# print(lib.add(3, 4))   # 7

# Or use pybind11 for C++ with no boilerplate:
# #include <pybind11/pybind11.h>
# namespace py = pybind11;
# PYBIND11_MODULE(myext, m) {
#     m.def("add", [](int a, int b) { return a + b; });
# }


# ── struct module: binary packing ────────────────────────────────────────────
packed = struct.pack("!HI", 0xBEEF, 0xDEADC0DE)   # big-endian unsigned short + uint
print(f"Packed:  {packed.hex()}")                  # beefdead...
h, i = struct.unpack("!HI", packed)
print(f"Unpacked: 0x{h:04x}, 0x{i:08x}")

# Useful for parsing binary protocols, file formats, network packets
