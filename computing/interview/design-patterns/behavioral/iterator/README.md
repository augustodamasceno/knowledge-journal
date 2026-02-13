# Iterator Pattern Interview Prep

## Overview
Iterator provides a way to access the elements of an aggregate object sequentially without exposing its underlying representation.

## Theoretical Q&A
1. **Why use Iterator?** It decouples traversal logic from collection structure, enabling multiple traversal strategies.
2. **How do external vs. internal iterators differ?** External iterators give client-controlled traversal, while internal iterators perform iteration on behalf of the client via callbacks.
3. **What about fail-fast behavior?** Iterators can detect structural modifications to prevent undefined behavior.

## Practical Exercises
- Implement a reverse iterator for the sample collection.
- Discuss thread-safety concerns when iterating mutable collections.
- Compare language-provided iterators with custom implementations.

### Code Samples
- C++: [cpp/iterator.cpp](cpp/iterator.cpp)
- C#: [csharp/IteratorDemo.cs](csharp/IteratorDemo.cs)
- Java: [java/IteratorDemo.java](java/IteratorDemo.java)
- Python: [python/iterator_demo.py](python/iterator_demo.py)
