# Factory Method Pattern Interview Prep

## Overview
Factory Method delegates instantiation to subclasses, letting creators decide which concrete products to return while keeping client code dependent only on abstractions.

## Theoretical Q&A
1. **What motivates Factory Method?** To allow frameworks to call into application code for concrete products without hard-coding types in the framework.
2. **How do Creator and Product collaborate?** The Creator defines the factory method and relies on Product interfaces, while subclasses override the factory method to supply specific Product implementations.
3. **When is Factory Method overused?** When simple constructors suffice; excessive subclassing can add needless indirection.

## Practical Exercises
- Extend the report creator hierarchy with a new HTML report type.
- Compare exception handling strategies when the factory cannot create a product.
- Explore how dependency injection can supply the concrete creator at runtime.

### Code Samples
- C++: [cpp/factory_method.cpp](cpp/factory_method.cpp)
- C#: [csharp/FactoryMethodDemo.cs](csharp/FactoryMethodDemo.cs)
- Java: [java/FactoryMethodDemo.java](java/FactoryMethodDemo.java)
- Python: [python/factory_method_demo.py](python/factory_method_demo.py)
