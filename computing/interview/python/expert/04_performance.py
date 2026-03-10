"""Performance: profiling, benchmarking, and optimisation techniques."""
import cProfile
import pstats
import timeit
import dis
import io


# ── 1. cProfile + pstats ──────────────────────────────────────────────────────
def sort_strings(n: int = 100_000) -> list[str]:
    import random, string
    data = ["".join(random.choices(string.ascii_lowercase, k=8)) for _ in range(n)]
    return sorted(data)

buf = io.StringIO()
pr  = cProfile.Profile()
pr.enable()
sort_strings()
pr.disable()
stats = pstats.Stats(pr, stream=buf).sort_stats("cumulative")
stats.print_stats(5)
print(buf.getvalue())


# ── 2. timeit for micro-benchmarks ────────────────────────────────────────────
setup   = "data = list(range(10_000))"
slow    = "result = []\nfor x in data:\n    result.append(x**2)"
fast    = "result = [x**2 for x in data]"
faster  = "result = list(map(lambda x: x**2, data))"

for label, stmt in [("for+append", slow), ("list comp", fast), ("map(lambda)", faster)]:
    t = timeit.timeit(stmt=stmt, setup=setup, number=500)
    print(f"  {label:<15}: {t:.3f}s")


# ── 3. Bytecode inspection ────────────────────────────────────────────────────
def add(a, b):
    return a + b

print("\nBytecode for add(a, b):")
dis.dis(add)


# ── 4. Local vs global lookup ─────────────────────────────────────────────────
import math

def global_sin(data):
    return [math.sin(x) for x in data]

def local_sin(data):
    _sin = math.sin          # cache in local variable — ~20% faster in tight loops
    return [_sin(x) for x in data]

data = list(range(10_000))
t_global = timeit.timeit(lambda: global_sin(data), number=500)
t_local  = timeit.timeit(lambda:  local_sin(data), number=500)
print(f"\nglobal lookup: {t_global:.3f}s")
print(f"local  lookup: {t_local:.3f}s  ({(t_global-t_local)/t_global*100:.1f}% faster)")


# ── 5. String concatenation ───────────────────────────────────────────────────
words = [f"word{i}" for i in range(1_000)]

def concat_plus(ws):
    s = ""
    for w in ws: s += w + " "
    return s

def concat_join(ws):
    return " ".join(ws)

t_plus = timeit.timeit(lambda: concat_plus(words), number=1_000)
t_join = timeit.timeit(lambda: concat_join(words), number=1_000)
print(f"\nstr +=  : {t_plus:.3f}s")
print(f"str join: {t_join:.3f}s")


# ── 6. Avoid repeated attribute lookups ───────────────────────────────────────
def slow_append(n):
    result = []
    for i in range(n):
        result.append(i)    # attribute lookup on each iteration
    return result

def fast_append(n):
    result = []
    _app   = result.append  # single lookup
    for i in range(n):
        _app(i)
    return result

t_slow = timeit.timeit(lambda: slow_append(10_000), number=1_000)
t_fast = timeit.timeit(lambda: fast_append(10_000), number=1_000)
print(f"\nresult.append (attr): {t_slow:.3f}s")
print(f"_app = result.append: {t_fast:.3f}s")


# ── 7. Bit tricks ─────────────────────────────────────────────────────────────
def is_power_of_2(n: int) -> bool:
    return n > 0 and (n & (n - 1)) == 0

def count_bits(n: int) -> int:
    return bin(n).count("1")   # Python built-in popcount

def lowest_set_bit(n: int) -> int:
    return n & (-n)

print(f"\nis_power_of_2(16)={is_power_of_2(16)}, (15)={is_power_of_2(15)}")
print(f"count_bits(255)={count_bits(255)}")        # 8
print(f"lowest_set_bit(12)={lowest_set_bit(12)}")  # 4 (0b0100)


# ── 8. Memory profiling with tracemalloc ─────────────────────────────────────
import tracemalloc

tracemalloc.start()
big_list = [i * 2 for i in range(1_000_000)]
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()
print(f"\nPeak memory for [i*2 for i in range(1M)]: {peak / 1024**2:.1f} MB")

# Generator uses ~0 MB
tracemalloc.start()
big_gen = sum(i * 2 for i in range(1_000_000))
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()
print(f"Peak memory for sum(i*2 for i in range(1M)): {peak / 1024**2:.4f} MB")
