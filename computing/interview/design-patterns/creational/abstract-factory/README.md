# Abstract Factory Pattern Interview Prep

## Overview
Use the abstract factory pattern to create families of related objects without hard-coding their concrete classes, keeping client code portable across product variants.

## Theoretical Q&A
1. **What problem does Abstract Factory solve?** It encapsulates object creation for a set of related products so clients can work with an interface regardless of the concrete family in use.
2. **How does it differ from Factory Method?** Abstract Factory returns families of multiple products via object factories, while Factory Method typically creates a single product via subclass specialization.
3. **What are the key participants?** The AbstractFactory defines creation methods, ConcreteFactories implement them, AbstractProducts declare product interfaces, and ConcreteProducts provide implementations.

## Practical Exercises
- Swap between the sample GUI factories and confirm no client changes are required.
- Add a new control to the product family and adjust factories accordingly.
- Discuss how dependency injection frameworks can wire abstract factories.

### Code Samples
- C++: [cpp/abstract_factory.cpp](cpp/abstract_factory.cpp)
- C#: [csharp/AbstractFactory.cs](csharp/AbstractFactory.cs)
- Java: [java/AbstractFactoryDemo.java](java/AbstractFactoryDemo.java)
- Python: [python/abstract_factory.py](python/abstract_factory.py)
