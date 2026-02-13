# Flyweight Pattern Interview Prep

## Overview
Flyweight minimizes memory usage by sharing common object state (intrinsic data) across many fine-grained objects, externalizing varying state.

## Theoretical Q&A
1. **What is intrinsic vs. extrinsic state?** Intrinsic state is shared and stored inside the flyweight; extrinsic state is supplied by clients per-use to avoid duplication.
2. **When does Flyweight provide value?** When many objects share identical data, such as characters in a document or tiles in a game map.
3. **How do factories support Flyweight?** A flyweight factory manages object caching and ensures reuse of shared instances.

## Practical Exercises
- Modify the sample text formatter to track flyweight reuse counts.
- Explore thread-safety strategies for flyweight factories under heavy contention.
- Discuss trade-offs between memory savings and added lookup overhead.

### Code Samples
- C++: [cpp/flyweight.cpp](cpp/flyweight.cpp)
- C#: [csharp/FlyweightDemo.cs](csharp/FlyweightDemo.cs)
- Java: [java/FlyweightDemo.java](java/FlyweightDemo.java)
- Python: [python/flyweight_demo.py](python/flyweight_demo.py)
