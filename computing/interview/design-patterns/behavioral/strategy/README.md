# Strategy Pattern Interview Prep

## Overview
Strategy defines a family of algorithms, encapsulates each one, and makes them interchangeable. Clients can vary algorithms independently from the code that uses them.

## Theoretical Q&A
1. **When is Strategy useful?** When multiple algorithms can solve the same problem and you want to switch among them at runtime.
2. **How does Strategy reduce conditionals?** It eliminates switch statements by delegating work to a selected strategy object implementing a common interface.
3. **What trade-offs exist?** More objects and indirection; clients must know which strategy to choose and manage their lifecycles.

## Practical Exercises
- Add a merge sort strategy to the sample sorter and compare performance.
- Discuss how to inject strategies using dependency injection containers.
- Explore how Strategy interacts with caching to reuse expensive computations.

### Code Samples
- C++: [cpp/strategy.cpp](cpp/strategy.cpp)
- C#: [csharp/StrategyDemo.cs](csharp/StrategyDemo.cs)
- Java: [java/StrategyDemo.java](java/StrategyDemo.java)
- Python: [python/strategy_demo.py](python/strategy_demo.py)
