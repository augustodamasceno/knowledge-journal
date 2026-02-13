# Facade Pattern Interview Prep

## Overview
Facade provides a unified interface to a set of interfaces in a subsystem, making the subsystem easier to use by hiding internal complexity.

## Theoretical Q&A
1. **How does Facade simplify usage?** It aggregates complex workflows behind a simple API, orchestrating calls to multiple subsystem components.
2. **Can Facade expose lower-level access?** Yes, but doing so carefully preserves the simplified pathway and prevents tight coupling.
3. **How does Facade interact with the Single Responsibility Principle?** It can centralize orchestration logic while subsystems retain their specialized responsibilities.

## Practical Exercises
- Extend the sample home theater facade with diagnostics while keeping the client API simple.
- Discuss how to log subsystem calls without leaking the facade abstraction.
- Compare Facade to Adapter when wrapping third-party libraries.

### Code Samples
- C++: [cpp/facade.cpp](cpp/facade.cpp)
- C#: [csharp/FacadeDemo.cs](csharp/FacadeDemo.cs)
- Java: [java/FacadeDemo.java](java/FacadeDemo.java)
- Python: [python/facade_demo.py](python/facade_demo.py)
