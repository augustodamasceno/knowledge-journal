# Decorator Pattern Interview Prep

## Overview
Decorator dynamically attaches additional responsibilities to objects, providing a flexible alternative to subclassing for feature extension.

## Theoretical Q&A
1. **How does Decorator preserve interfaces?** Decorators implement the same component interface and wrap another component, forwarding calls while adding behavior.
2. **What problems can Decorator solve?** It enables combination of features (e.g., encryption, buffering) without an explosion of subclasses.
3. **When might Decorator be overkill?** When there are only a few fixed variations, static inheritance or simple conditionals can be clearer.

## Practical Exercises
- Stack multiple decorators in the sample and reason about order sensitivity.
- Implement a caching decorator and analyze invalidation strategies.
- Compare Decorator and Proxy in terms of transparency and intent.

### Code Samples
- C++: [cpp/decorator.cpp](cpp/decorator.cpp)
- C#: [csharp/DecoratorDemo.cs](csharp/DecoratorDemo.cs)
- Java: [java/DecoratorDemo.java](java/DecoratorDemo.java)
- Python: [python/decorator_demo.py](python/decorator_demo.py)
