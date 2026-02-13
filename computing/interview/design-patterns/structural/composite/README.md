# Composite Pattern Interview Prep

## Overview
Composite lets clients treat individual objects and compositions uniformly by organizing them into tree structures that share a common interface.

## Theoretical Q&A
1. **When is Composite useful?** When you need to represent part-whole hierarchies (e.g., GUIs, file systems) and allow recursive operations over them.
2. **How does Composite enable uniform treatment?** Leaf and composite nodes implement the same component interface, so callers do not need type checks.
3. **What challenges arise with child management?** Composite must manage addition and removal of children while keeping the interface minimal for leaf nodes.

## Practical Exercises
- Extend the sample file system with aggregated size calculations.
- Add lazy loading for subtrees and discuss caching implications.
- Compare Composite with the Visitor pattern for tree traversal logic.

### Code Samples
- C++: [cpp/composite.cpp](cpp/composite.cpp)
- C#: [csharp/CompositeDemo.cs](csharp/CompositeDemo.cs)
- Java: [java/CompositeDemo.java](java/CompositeDemo.java)
- Python: [python/composite_demo.py](python/composite_demo.py)
