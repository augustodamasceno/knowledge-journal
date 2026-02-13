# Mediator Pattern Interview Prep

## Overview
Mediator encapsulates how a set of objects interact, promoting loose coupling by preventing objects from referring to each other explicitly.

## Theoretical Q&A
1. **How does Mediator reduce coupling?** Colleagues communicate through the mediator instead of referencing each other directly, simplifying dependencies.
2. **When should you apply Mediator?** When interactions among objects are complex but are better centralized for maintainability.
3. **What risks exist?** The mediator can become a god object if it takes on too much logic.

## Practical Exercises
- Extend the sample chat mediator with user presence notifications.
- Discuss how Mediator works with event-driven architectures.
- Compare Mediator to Observer for broadcasting messages.

### Code Samples
- C++: [cpp/mediator.cpp](cpp/mediator.cpp)
- C#: [csharp/MediatorDemo.cs](csharp/MediatorDemo.cs)
- Java: [java/MediatorDemo.java](java/MediatorDemo.java)
- Python: [python/mediator_demo.py](python/mediator_demo.py)
