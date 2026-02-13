# Singleton Pattern Interview Prep

## Overview
Singleton ensures a class has only one instance while providing a global access point, often for shared resources such as configuration or logging.

## Theoretical Q&A
1. **Why can Singleton be controversial?** It can hide dependencies, complicate testing, and effectively act as a global variable if overused.
2. **How do you make a Singleton thread-safe?** Use eager initialization, synchronization, or language-specific constructs like `std::call_once`, `Lazy<T>`, or enum singletons.
3. **What testing strategy mitigates Singleton coupling?** Abstract the singleton behind an interface or pass it explicitly so tests can swap fakes.

## Practical Exercises
- Investigate the thread-safety approach used in each language sample.
- Add lazy initialization and discuss startup cost trade-offs.
- Refactor the logger singleton to support dependency injection in tests.

### Code Samples
- C++: [cpp/singleton.cpp](cpp/singleton.cpp)
- C#: [csharp/SingletonDemo.cs](csharp/SingletonDemo.cs)
- Java: [java/SingletonDemo.java](java/SingletonDemo.java)
- Python: [python/singleton_demo.py](python/singleton_demo.py)
