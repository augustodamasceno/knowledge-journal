# Bridge Pattern Interview Prep

## Overview
Bridge decouples an abstraction from its implementation so the two can vary independently, often via composition over inheritance.

## Theoretical Q&A
1. **How does Bridge differ from Adapter?** Bridge is designed up front to separate abstraction and implementation, while Adapter retrofits compatibility.
2. **What motivates Bridge in UI toolkits?** It separates platform-specific rendering from widget logic, allowing both to evolve without combinatorial subclasses.
3. **When can Bridge be excessive?** When the abstraction and implementation will never vary independently, the extra layer adds needless complexity.

## Practical Exercises
- Add a new renderer to the sample without modifying existing shapes.
- Discuss how Bridge can help manage cross-platform plugins.
- Compare Bridge to Strategy for run-time swapping of behavior.

### Code Samples
- C++: [cpp/bridge.cpp](cpp/bridge.cpp)
- C#: [csharp/BridgeDemo.cs](csharp/BridgeDemo.cs)
- Java: [java/BridgeDemo.java](java/BridgeDemo.java)
- Python: [python/bridge_demo.py](python/bridge_demo.py)
