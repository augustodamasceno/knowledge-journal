# Memento Pattern Interview Prep

## Overview
Memento captures and externalizes an object's internal state without violating encapsulation, allowing the object to be restored to that state later.

## Theoretical Q&A
1. **What are the roles?** Originator creates and restores mementos, Memento stores state, and Caretaker manages mementos without inspecting them.
2. **When is Memento practical?** For implementing undo/redo or checkpoints where internal state must be preserved.
3. **What is the main trade-off?** Mementos can consume significant memory if state snapshots are large or frequent.

## Practical Exercises
- Extend the sample text editor with redo support using two stacks.
- Discuss serialization of mementos for cross-session undo history.
- Compare Memento with Command-based undo strategies.

### Code Samples
- C++: [cpp/memento.cpp](cpp/memento.cpp)
- C#: [csharp/MementoDemo.cs](csharp/MementoDemo.cs)
- Java: [java/MementoDemo.java](java/MementoDemo.java)
- Python: [python/memento_demo.py](python/memento_demo.py)
