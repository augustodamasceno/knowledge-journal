# Visitor Pattern Interview Prep

## Overview
Visitor represents an operation to be performed on elements of an object structure, allowing new operations to be defined without changing the classes of the elements on which it operates.

## Theoretical Q&A
1. **When is Visitor beneficial?** When a structure has stable classes but new operations need to be added frequently.
2. **How does double dispatch help?** Visitor relies on element.accept(visitor) to dispatch based on both visitor type and element type at runtime.
3. **What downsides exist?** Adding new element types requires updating all visitors, and access to internals can break encapsulation.

## Practical Exercises
- Extend the sample AST visitor with a pretty printer.
- Discuss how Visitor compares to pattern matching in modern languages.
- Explore how to avoid visitor explosion with default methods and adapters.

### Code Samples
- C++: [cpp/visitor.cpp](cpp/visitor.cpp)
- C#: [csharp/VisitorDemo.cs](csharp/VisitorDemo.cs)
- Java: [java/VisitorDemo.java](java/VisitorDemo.java)
- Python: [python/visitor_demo.py](python/visitor_demo.py)
