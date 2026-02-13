# Command Pattern Interview Prep

## Overview
Command encapsulates a request as an object, letting you parameterize clients with queues, undo/redo, and logging of operations.

## Theoretical Q&A
1. **What are the main participants?** Command declares an interface, ConcreteCommand implements it, Invoker calls `execute`, and Receiver performs the work.
2. **How does Command enable undo?** Commands store state necessary to reverse their action and provide an `undo` method invoked by the invoker.
3. **When is Command overkill?** When only a single simple action is needed without queuing or undo requirements, direct method calls may suffice.

## Practical Exercises
- Expand the sample editor commands to support redo using a stack.
- Discuss serialization of commands for audit trails.
- Compare Command to Strategy when handling GUI button callbacks.

### Code Samples
- C++: [cpp/command.cpp](cpp/command.cpp)
- C#: [csharp/CommandDemo.cs](csharp/CommandDemo.cs)
- Java: [java/CommandDemo.java](java/CommandDemo.java)
- Python: [python/command_demo.py](python/command_demo.py)
