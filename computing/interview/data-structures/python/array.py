# Array — Python list (dynamic array) and array.array (typed, memory-efficient)
import array

# --- Python list: dynamic array, O(1) amortised append ---
lst = [5, 3, 1, 4, 2]
lst.sort()                    # in-place sort O(n log n)
print("Sorted list:", lst)

lst.append(6)                 # O(1) amortised
lst.insert(0, 0)              # O(n) — shifts elements
lst.pop(2)                    # O(n) — shifts elements
print("After insert/pop:", lst)
print("Element at index 1:", lst[1])   # O(1) random access

# Slicing creates a new list — O(k)
print("Slice [1:4]:", lst[1:4])

# List comprehension — idiomatic Python
squares = [x ** 2 for x in range(6)]
print("Squares:", squares)

# --- array.array: typed, more memory-efficient than list ---
typed = array.array('i', [10, 20, 30, 40])   # 'i' = signed int
typed.append(50)
print("Typed array:", list(typed))
