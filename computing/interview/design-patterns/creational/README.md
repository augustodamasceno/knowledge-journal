# Creational Patterns

Creational patterns focus on object creation mechanisms. They abstract the instantiation process to make systems independent of how objects are composed and represented.

## Patterns

### Abstract Factory
**Intent:** Provide an interface for creating families of related or dependent objects without specifying their concrete classes.

**Use when:**
- A system needs to work with multiple families of products
- You want to provide a library of products revealing only interfaces
- You need to ensure related products are used together

### Builder
**Intent:** Separate the construction of a complex object from its representation so the same construction process can create different representations.

**Use when:**
- An object can be constructed with many optional parameters
- You want to create different representations of an object
- Construction requires multiple steps

### Factory Method
**Intent:** Define an interface for creating an object, but let subclasses decide which class to instantiate.

**Use when:**
- A class can't anticipate the type of objects it needs to create
- You want to delegate object creation to subclasses
- You need to centralize object creation logic

### Prototype
**Intent:** Specify the kinds of objects to create using a prototype instance, and create new objects by copying this prototype.

**Use when:**
- Object creation is expensive
- You need to clone objects to create new instances
- You want to avoid subclassing for object creation

### Singleton
**Intent:** Ensure a class has only one instance and provide a global point of access to it.

**Use when:**
- A class needs exactly one instance
- The instance must be accessible globally
- You want to control lazy initialization

## Guidelines

- Choose Abstract Factory when dealing with families of related objects
- Use Builder for complex objects with many constructor parameters
- Prefer Factory Method for simple object creation delegation
- Apply Prototype when cloning is more efficient than creation
- Reserve Singleton for truly single-instance resources (e.g., loggers, connection pools)

