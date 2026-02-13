# Object-Oriented Programming Interview Prep

## Overview
This module consolidates essential OOP theory and practice for interview preparation. Review the guiding questions, rehearse concise answers, and study the multilingual code samples.

## Theoretical Q&A
1. **What are the four pillars of OOP?** Encapsulation, abstraction, inheritance, and polymorphism.
2. **How does encapsulation improve software maintainability?** It hides implementation details behind stable interfaces, reducing the impact of internal changes on dependent code.
3. **When would you favor composition over inheritance?** Prefer composition when behavior should be assembled at runtime or when reuse should not expose the entire superclass interface.
4. **How does polymorphism support extensibility?** Shared interfaces allow new types to integrate without modifying callers, enabling open/closed design.
5. **What role do interfaces or abstract classes play in testability?** They enable substituting test doubles that satisfy the same contract, isolating units under test.

## Practical Exercises
- Study and adapt the multilingual Shape hierarchy example to demonstrate encapsulation, inheritance, and polymorphism.
- Extend the example with a new shape and discuss how the change affects callers.
- Explore how dynamic dispatch differs across the languages provided below.

### Code Samples
- C++: [cpp/shape_example.cpp](cpp/shape_example.cpp)
- C#: [csharp/ShapeExample.cs](csharp/ShapeExample.cs)
- Java: [java/ShapeExample.java](java/ShapeExample.java)
- Python: [python/shape_example.py](python/shape_example.py)
