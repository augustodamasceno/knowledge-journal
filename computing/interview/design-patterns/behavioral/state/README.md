# State Pattern Interview Prep

## Overview
State allows an object to alter its behavior when its internal state changes; the object appears to change its class by delegating work to state objects.

## Theoretical Q&A
1. **When is State useful?** When an object's behavior depends on its state and it must change behavior at runtime without complex conditional logic.
2. **How does it reduce conditionals?** Each state encapsulates behavior for that state, and the context delegates to the current state object.
3. **What risks exist?** Proliferation of state classes if the state machine is simple, or tight coupling if states need intimate context knowledge.

## Practical Exercises
- Extend the sample audio player states with a buffering state.
- Discuss how to log transitions without bloating state classes.
- Compare State to Strategy regarding the ability to change behavior dynamically.

### Code Samples
- C++: [cpp/state.cpp](cpp/state.cpp)
- C#: [csharp/StateDemo.cs](csharp/StateDemo.cs)
- Java: [java/StateDemo.java](java/StateDemo.java)
- Python: [python/state_demo.py](python/state_demo.py)
