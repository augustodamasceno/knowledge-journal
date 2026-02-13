# Adapter Pattern Interview Prep

## Overview
Adapter converts the interface of a class into another interface clients expect, enabling collaboration between otherwise incompatible components.

## Theoretical Q&A
1. **When do you prefer object adapters over class adapters?** Object adapters (composition) work with multiple adaptees and avoid inheritance constraints, while class adapters require language support for multiple inheritance.
2. **How can Adapter hide legacy quirks?** The adapter normalizes odd parameter orders, units, or error codes before handing results to modern clients.
3. **What is the risk of too many adapters?** They can mask the need to refactor or retire obsolete interfaces, leading to adapter chains.

## Practical Exercises
- Extend the sample to adapt both imperial and metric rectangle APIs.
- Discuss exception translation strategies within adapters.
- Identify when a facade would be a better fit than an adapter.

### Code Samples
- C++: [cpp/adapter.cpp](cpp/adapter.cpp)
- C#: [csharp/AdapterDemo.cs](csharp/AdapterDemo.cs)
- Java: [java/AdapterDemo.java](java/AdapterDemo.java)
- Python: [python/adapter_demo.py](python/adapter_demo.py)
