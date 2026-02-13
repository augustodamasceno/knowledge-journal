# Interpreter Pattern Interview Prep

## Overview
Interpreter defines a representation for a simple language along with an interpreter that uses the representation to evaluate sentences in that language.

## Theoretical Q&A
1. **When is Interpreter appropriate?** For simple grammars that change frequently and when efficiency is not critical compared to maintainability.
2. **What are the components?** AbstractExpression, TerminalExpression, NonterminalExpression, Context, and a client that builds or parses the sentence tree.
3. **What are the drawbacks?** Complex grammars lead to class explosions; performance can suffer compared to dedicated parsers.

## Practical Exercises
- Extend the sample boolean language with parentheses and precedence handling.
- Discuss how to replace Interpreter with the Visitor pattern for expression evaluation.
- Compare this pattern to using parser generators when the grammar grows.

### Code Samples
- C++: [cpp/interpreter.cpp](cpp/interpreter.cpp)
- C#: [csharp/InterpreterDemo.cs](csharp/InterpreterDemo.cs)
- Java: [java/InterpreterDemo.java](java/InterpreterDemo.java)
- Python: [python/interpreter_demo.py](python/interpreter_demo.py)
