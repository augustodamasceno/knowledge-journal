# Stack — Python list (O(1) push/pop at end) or collections.deque
from collections import deque


def is_balanced(s: str) -> bool:
    """Classic use-case: balanced parentheses checker."""
    stack = []
    matching = {')': '(', ']': '[', '}': '{'}
    for ch in s:
        if ch in '([{':
            stack.append(ch)
        elif ch in ')]}':
            if not stack or stack[-1] != matching[ch]:
                return False
            stack.pop()
    return len(stack) == 0


# --- list as stack (append = push, pop = pop) ---
stack = []
stack.append(1)   # O(1) amortised
stack.append(2)
stack.append(3)
print("Top:", stack[-1])   # peek — O(1)
stack.pop()                # O(1)
print("After pop:", stack)

# --- deque as stack (slightly faster for large stacks) ---
dq = deque()
dq.append(10)
dq.append(20)
print("deque top:", dq[-1])
dq.pop()
print("deque after pop:", list(dq))

# --- Balanced parentheses demo ---
print(f'"({{[]}})" balanced: {is_balanced("({[]})")}')
print(f'"({{[})" balanced:  {is_balanced("({[})")}')
