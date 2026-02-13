# Prototype Pattern Interview Prep

## Overview
Prototype enables object cloning without binding code to specific classes, letting clients duplicate existing instances that serve as prototypes.

## Theoretical Q&A
1. **What types of copy can Prototype perform?** Shallow or deep copies depending on whether referenced objects must be duplicated or shared.
2. **Why use Prototype over constructors?** When creating objects is expensive or must preserve runtime configuration that constructors cannot easily rebuild.
3. **How do registries support Prototype?** A registry stores named prototypes that clients clone on demand, centralizing reference management.

## Practical Exercises
- Extend the sample drawing to support deep copies of nested structures.
- Discuss copy-on-write strategies when prototypes share heavy data.
- Describe how Prototype fits into undo/redo implementations.

### Code Samples
- C++: [cpp/prototype.cpp](cpp/prototype.cpp)
- C#: [csharp/PrototypeDemo.cs](csharp/PrototypeDemo.cs)
- Java: [java/PrototypeDemo.java](java/PrototypeDemo.java)
- Python: [python/prototype_demo.py](python/prototype_demo.py)
