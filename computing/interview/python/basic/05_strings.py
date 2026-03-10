"""String formatting, methods, and common interview operations."""

# ── f-strings ─────────────────────────────────────────────────────────────────
name, price = "Widget", 9.99
print(f"{name!r} costs ${price:.2f}")   # 'Widget' costs $9.99

# Debug expression (3.8+)
value = 42
print(f"{value=}")          # value=42

# Alignment and fill
print(f"{'left':<12}|{'center':^12}|{'right':>12}")
print(f"{'█' * 8}")

# Numbers
print(f"{1_000_000:,}")       # 1,000,000
print(f"{0.00012345:.2e}")    # 1.23e-04
print(f"{255:#010x}")         # 0x000000ff
print(f"{255:#010b}")         # 0b11111111   (with 0b prefix + zero-fill)
print(f"{3.14159:.4f}")       # 3.1416

# ── Common string methods ─────────────────────────────────────────────────────
s = "  Hello, World!  "
print(s.strip())                    # "Hello, World!"
print(s.lstrip(), s.rstrip())
print(s.lower(), s.upper())
print(s.title())                    # "  Hello, World!  " → "  Hello, World!  "
print("hello world".title())        # "Hello World"
print(s.replace("World", "Python"))
print(s.find("World"))              # index of first occurrence, -1 if not found
print("abcabc".count("ab"))         # 2
print(",".join(["a", "b", "c"]))    # a,b,c
print("a,b,,c".split(","))          # ['a', 'b', '', 'c']
print("a,b,,c".split(",", maxsplit=1))  # ['a', 'b,,c']

# Check methods
print("Hello123".isalnum())   # True
print("Hello".isalpha())      # True
print("123".isdigit())        # True
print("  ".isspace())         # True
print("Hello".startswith("He"), "World!".endswith("!"))

# ── Strings are sequences ─────────────────────────────────────────────────────
s = "Python"
print(s[0])        # P
print(s[-1])       # n
print(s[1:4])      # yth
print(s[::-1])     # nohtyP

# ── String multiplication and containment ─────────────────────────────────────
print("ha" * 3)        # hahaha
print("yt" in "Python")  # True

# ── Multiline strings ─────────────────────────────────────────────────────────
ml = """\
Line 1
Line 2
Line 3"""
print(ml.splitlines())   # ['Line 1', 'Line 2', 'Line 3']

# ── String → bytes / encoding ─────────────────────────────────────────────────
raw = "café"
b_utf8  = raw.encode("utf-8")
b_latin = raw.encode("latin-1")
print(b_utf8.hex())   # 636166c3a9
print(b_utf8.decode("utf-8"))

# ── Common interview patterns ─────────────────────────────────────────────────

# Check palindrome
def is_palindrome(s: str) -> bool:
    s = s.lower().replace(" ", "")
    return s == s[::-1]

print(is_palindrome("A man a plan a canal Panama".replace(" ", "")))  # True

# Count characters
from collections import Counter
c = Counter("abracadabra")
print(c.most_common(3))   # [('a', 5), ('b', 2), ('r', 2)]

# Anagram check
def is_anagram(a: str, b: str) -> bool:
    return Counter(a.lower()) == Counter(b.lower())

print(is_anagram("listen", "silent"))   # True

# Reverse words
def reverse_words(s: str) -> str:
    return " ".join(s.split()[::-1])

print(reverse_words("Hello World Python"))  # Python World Hello

# Caesar cipher
def caesar(text: str, shift: int) -> str:
    result = []
    for ch in text:
        if ch.isalpha():
            base = ord("A") if ch.isupper() else ord("a")
            result.append(chr((ord(ch) - base + shift) % 26 + base))
        else:
            result.append(ch)
    return "".join(result)

print(caesar("Hello, World!", 3))   # Khoor, Zruog!
