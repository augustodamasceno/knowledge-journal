# Design Patterns

This folder organizes all 23 Gang of Four design patterns into three categories: **Creational**, **Structural**, and **Behavioral**. Each pattern includes theoretical explanations and practical code examples.

## Overview

Design patterns are reusable solutions to common programming problems. They represent best practices and can accelerate development by providing proven templates for code structure and interaction.

## Creational Patterns

Patterns that deal with object creation mechanisms.

- **Abstract Factory** – Create families of related objects without specifying their concrete classes.
- **Builder** – Construct complex objects step by step, separating construction from representation.
- **Factory Method** – Create objects through a method rather than direct instantiation.
- **Prototype** – Create new objects by cloning an existing prototype.
- **Singleton** – Ensure a class has only one instance with global access.

See [creational/README.md](creational/README.md) for detailed examples.

## Structural Patterns

Patterns that deal with object composition and relationships between entities.

- **Adapter** – Convert an interface to another that clients expect.
- **Bridge** – Decouple an abstraction from its implementation.
- **Composite** – Compose objects into tree structures to represent hierarchies.
- **Decorator** – Attach additional responsibilities to objects dynamically.
- **Facade** – Provide a unified interface to a set of interfaces in a subsystem.
- **Flyweight** – Share fine-grained objects efficiently to support large numbers of them.
- **Proxy** – Provide a surrogate for another object to control access.

See [structural/README.md](structural/README.md) for detailed examples.

## Behavioral Patterns

Patterns that deal with object collaboration and responsibility distribution.

- **Chain of Responsibility** – Pass requests along a chain of handlers.
- **Command** – Encapsulate a request as an object.
- **Interpreter** – Define a representation for a language's grammar and an interpreter.
- **Iterator** – Access elements of a collection sequentially without exposing its representation.
- **Mediator** – Define an object that encapsulates how a set of objects interact.
- **Memento** – Capture and externalize an object's internal state for later restoration.
- **Observer** – Define a one-to-many dependency where state changes trigger notifications.
- **State** – Allow an object to alter its behavior when its state changes.
- **Strategy** – Define a family of algorithms, encapsulate each, and make them interchangeable.
- **Template Method** – Define the skeleton of an algorithm in a method, deferring steps to subclasses.
- **Visitor** – Represent operations on objects without changing their classes.

See [behavioral/README.md](behavioral/README.md) for detailed examples.

## How to Use

1. **Study the pattern** – Read the explanation and intent.
2. **Review the code** – Examine language-specific implementations (C++, C#, Java, Python).
3. **Practice** – Adapt examples to your own projects or interview scenarios.
4. **Compare patterns** – Understand when and why to choose one pattern over another.

## Key Questions to Ask

- What problem does this pattern solve?
- When should I use this pattern?
- What are its advantages and disadvantages?
- How does it compare to similar patterns?
- Can I implement this without the pattern?

