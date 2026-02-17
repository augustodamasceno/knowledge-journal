# Structural Patterns

Structural patterns focus on how classes and objects can be combined to form larger structures. They help ensure that changes to one part of a system don't require changes to all related parts.

## Patterns

### Adapter
**Intent:** Convert the interface of a class into another interface clients expect, allowing incompatible interfaces to work together.

**Use when:**
- You want to use an existing class but its interface doesn't match your needs
- You need to create a reusable class that cooperates with unrelated or unforeseen classes
- Multiple differing interfaces need to be supported

### Bridge
**Intent:** Decouple an abstraction from its implementation so the two can vary independently.

**Use when:**
- You want to avoid permanent binding between abstraction and implementation
- Changes in implementation should not affect clients
- You want to share implementation among multiple objects

### Composite
**Intent:** Compose objects into tree structures to represent part-whole hierarchies, letting clients treat individual objects and compositions uniformly.

**Use when:**
- You want to represent hierarchies of objects
- Clients should ignore differences between object compositions and individual objects
- You need to work with tree structures

### Decorator
**Intent:** Attach additional responsibilities to an object dynamically, providing a flexible alternative to subclassing.

**Use when:**
- You need to add responsibilities to individual objects without affecting others
- Extension by subclassing is impractical
- You need to add features that can be combined in various ways

### Facade
**Intent:** Provide a unified, simplified interface to a set of interfaces in a subsystem.

**Use when:**
- You want to provide a simple interface to a complex subsystem
- You want to decouple clients from subsystem components
- You need to layer subsystems

### Flyweight
**Intent:** Use sharing to support large numbers of fine-grained objects efficiently.

**Use when:**
- An application uses many objects
- Storage costs are high due to object quantity
- Objects can be shared in an immutable fashion

### Proxy
**Intent:** Provide a surrogate or placeholder for another object to control access to it.

**Use when:**
- You need lazy initialization
- You want to control access to another object
- You need to add logging, caching, or access control

## Guidelines

- Use Adapter to bridge incompatible interfaces
- Apply Bridge to separate abstraction from implementation
- Choose Composite for tree-like hierarchies
- Use Decorator for flexible feature addition
- Apply Facade to simplify complex subsystems
- Use Flyweight to optimize memory for many similar objects
- Choose Proxy for access control, logging, or lazy loading

