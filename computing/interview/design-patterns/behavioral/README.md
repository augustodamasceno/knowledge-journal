# Behavioral Patterns

Behavioral patterns focus on object collaboration and the distribution of responsibility. They characterize the ways objects interact and how responsibilities are distributed among them.

## Patterns

### Chain of Responsibility
**Intent:** Avoid coupling the sender of a request to its receiver by giving more than one object a chance to handle the request.

**Use when:**
- Multiple objects may handle a request
- You don't know in advance which object should handle the request
- You want to issue a request without specifying the receiver

### Command
**Intent:** Encapsulate a request as an object, thereby letting you parameterize clients with different requests, queue requests, and support undoable operations.

**Use when:**
- You need to parameterize objects with an action to perform
- You want to queue, log, or support undo/redo operations
- You need to decouple the object that invokes a command from the one that executes it

### Interpreter
**Intent:** Define a representation for a language's grammar and an interpreter to interpret sentences in that language.

**Use when:**
- You need to define a simple language
- You want to represent sentences in the language as syntax trees
- Performance is not a critical concern

### Iterator
**Intent:** Provide a way to access elements of a collection sequentially without exposing its underlying representation.

**Use when:**
- You want to access collection elements without exposing its structure
- You need to support multiple simultaneous traversals
- You want to provide a uniform interface for traversing different collections

### Mediator
**Intent:** Define an object that encapsulates how a set of objects interact, promoting loose coupling.

**Use when:**
- Objects communicate in complex but well-defined ways
- Reusing objects is difficult due to many dependencies
- Behavior distributed between several classes should be customizable

### Memento
**Intent:** Capture and externalize an object's internal state without violating encapsulation, allowing the object to be restored later.

**Use when:**
- You need to save and restore object state
- You want to provide an undo mechanism
- You don't want to violate object encapsulation

### Observer
**Intent:** Define a one-to-many dependency between objects so that when one object changes state, all its dependents are notified automatically.

**Use when:**
- A change to one object requires changing others
- The number of dependent objects is unknown
- An object should notify dependents without making assumptions about them

### State
**Intent:** Allow an object to alter its behavior when its internal state changes, appearing to change its class.

**Use when:**
- Object behavior depends on its state and changes at runtime
- Operations have large conditional statements based on state
- State-specific behavior should be isolated

### Strategy
**Intent:** Define a family of algorithms, encapsulate each one, and make them interchangeable.

**Use when:**
- You have multiple algorithms for a task
- You want to avoid conditional statements selecting algorithms
- Algorithms may be chosen at runtime

### Template Method
**Intent:** Define the skeleton of an algorithm in a method, deferring some steps to subclasses.

**Use when:**
- Multiple classes have duplicate algorithm structure
- Common behavior should be in a base class
- You want to avoid code duplication in subclasses

### Visitor
**Intent:** Represent an operation to be performed on elements of an object structure, letting you define new operations without changing the classes of the elements.

**Use when:**
- You need to perform operations on complex object structures
- Many unrelated operations are needed on objects
- You want to add new operations without modifying object classes

## Guidelines

- Use Chain of Responsibility for request handling pipelines
- Apply Command for parameterized actions and undo/redo
- Use Interpreter for domain-specific languages
- Choose Iterator for collection traversal
- Apply Mediator to reduce object coupling
- Use Memento for undo/save functionality
- Choose Observer for event notification systems
- Apply State when behavior depends on internal state
- Use Strategy for algorithm families
- Apply Template Method to avoid code duplication
- Use Visitor for operations across object hierarchies

