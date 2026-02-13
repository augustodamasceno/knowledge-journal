# Chain of Responsibility Pattern Interview Prep

## Overview
Chain of Responsibility passes requests along a chain of handlers until one handles it, promoting loose coupling between senders and receivers.

## Theoretical Q&A
1. **When is Chain of Responsibility useful?** When multiple handlers might process a request and you want to decouple senders from concrete handler classes.
2. **How do you terminate the chain?** When a handler processes the request and either stops or optionally forwards it for further processing.
3. **What risks exist?** Requests may go unhandled if the chain is misconfigured, and debugging can be tricky when chains are long or dynamic.

## Practical Exercises
- Add a new handler to the logging chain and explore configuration order.
- Discuss how to make the chain dynamic at runtime via dependency injection.
- Demonstrate fallback behavior when no handler accepts a request.

### Code Samples
- C++: [cpp/chain_of_responsibility.cpp](cpp/chain_of_responsibility.cpp)
- C#: [csharp/ChainOfResponsibilityDemo.cs](csharp/ChainOfResponsibilityDemo.cs)
- Java: [java/ChainOfResponsibilityDemo.java](java/ChainOfResponsibilityDemo.java)
- Python: [python/chain_of_responsibility_demo.py](python/chain_of_responsibility_demo.py)
