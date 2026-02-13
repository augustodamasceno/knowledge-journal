# Builder Pattern Interview Prep

## Overview
The builder pattern separates object construction from its representation, letting the same creation process assemble different configurations step by step.

## Theoretical Q&A
1. **When is Builder preferable to telescoping constructors?** When objects have many optional parameters or can be assembled in varying sequences that would otherwise lead to fragile constructor overloads.
2. **How does Builder relate to Director?** The Director orchestrates the construction steps defined by the Builder interface, enabling reusable assembly workflows.
3. **What risks exist with mutable builders?** Concurrent use can corrupt state, and forgetting to reset builders can leak data between builds.

## Practical Exercises
- Modify the sample meal builder to produce vegetarian and protein-heavy menus.
- Add validation inside the builder to prevent inconsistent configurations.
- Discuss thread-safety options for builders used across requests.

### Code Samples
- C++: [cpp/builder.cpp](cpp/builder.cpp)
- C#: [csharp/BuilderDemo.cs](csharp/BuilderDemo.cs)
- Java: [java/BuilderDemo.java](java/BuilderDemo.java)
- Python: [python/builder_demo.py](python/builder_demo.py)
