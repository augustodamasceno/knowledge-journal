# Observer Pattern Interview Prep

## Overview
Observer defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically.

## Theoretical Q&A
1. **When is Observer effective?** When multiple subscribers need to react to changes in a subject without tight coupling.
2. **How do push vs. pull models differ?** Push sends detailed updates to observers; pull provides minimal info so observers query as needed.
3. **What problems arise?** Observers can experience cascading updates or receive stale data if notifications are not synchronized.

## Practical Exercises
- Extend the sample to support asynchronous notifications.
- Discuss how to avoid memory leaks with observer deregistration.
- Compare Observer with Pub/Sub messaging systems.

### Code Samples
- C++: [cpp/observer.cpp](cpp/observer.cpp)
- C#: [csharp/ObserverDemo.cs](csharp/ObserverDemo.cs)
- Java: [java/ObserverDemo.java](java/ObserverDemo.java)
- Python: [python/observer_demo.py](python/observer_demo.py)
