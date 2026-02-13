# Template Method Pattern Interview Prep

## Overview
Template Method defines the skeleton of an algorithm in an operation, deferring some steps to subclasses to customize behavior without changing the overall structure.

## Theoretical Q&A
1. **What is the key idea?** Superclass outlines algorithm steps, subclasses override specific hooks to vary portions of the algorithm.
2. **How does it enforce ordering?** The template method calls steps in a fixed sequence, guaranteeing the algorithm flow.
3. **What are potential downsides?** Rigid inheritance hierarchies and difficulty mixing behaviors without multiple inheritance.

## Practical Exercises
- Add instrumentation hooks to the sample data processor and capture metrics.
- Discuss how Template Method compares to Strategy for algorithm customization.
- Explore how hooks can be made optional for subclasses.

### Code Samples
- C++: [cpp/template_method.cpp](cpp/template_method.cpp)
- C#: [csharp/TemplateMethodDemo.cs](csharp/TemplateMethodDemo.cs)
- Java: [java/TemplateMethodDemo.java](java/TemplateMethodDemo.java)
- Python: [python/template_method_demo.py](python/template_method_demo.py)
