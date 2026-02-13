# C++ Interview Questions

This section collects frequently asked C++ interview questions with concise answers and supporting code samples.

## Questions with Code

### 1. What is the Rule of Five and when should you implement the special member functions?
Implement the special member functions (destructor, copy constructor, copy assignment operator, move constructor, move assignment operator) whenever your type manually manages a resource. Doing so prevents double free, leaks, and dangling ownership. Example walk-through in [question1.cpp](question1.cpp).

### 2. How do `std::unique_ptr` and `std::shared_ptr` differ in ownership semantics?
`std::unique_ptr` provides exclusive ownership and cannot be copied, making transfers explicit and cheap. `std::shared_ptr` supports shared ownership via reference counting but introduces atomic overhead and potential cycles (fixable with `std::weak_ptr`). Sample code illustrating ownership hand-off and custom deleters lives in [question2.cpp](question2.cpp).

### 3. How can SFINAE or `std::enable_if` restrict template overloads?
Use `std::enable_if` to remove overloads from the candidate set at compile time, allowing you to steer overload resolution based on traits. The [question3.cpp](question3.cpp) sample enables a function only for containers exposing `value_type` and demonstrating fallback behavior.

### 4. How do you visit `std::variant` alternatives without manual `std::holds_alternative` checks?
Wrap callable types in an `overloaded` helper so the visitor can dispatch to the correct overload. `std::visit` ensures exhaustive handling at compile time. See [question4.cpp](question4.cpp) for a pattern matching style example.

### 5. Which C++11 features should you emphasize in interviews?
Highlight range-based for loops, automatic type deduction, lambdas, and move-aware resource management. Together they let you write succinct, exception-safe code without hand-rolled ownership logic. Walk through the combined example in [question5.cpp](question5.cpp).

### 6. How did C++14 refine everyday usage of C++11 features?
C++14 added `std::make_unique`, generic lambdas, and return type deduction for simple functions, smoothing the ergonomics of idioms introduced in C++11. Demonstrate the refinements with [question6.cpp](question6.cpp).

### 7. Which C++20 additions should you showcase quickly?
Concepts, ranges, and coroutines headlined C++20. Even a short concept-constrained algorithm paired with a ranges pipeline signals mastery of the new toolbox. The filter-and-average demo in [question7.cpp](question7.cpp) illustrates the talking points.

### 8. How can you demonstrate C++23 updates succinctly?
C++23 introduced `if consteval`, `std::expected`, and additional range utilities. Mention how they simplify error handling and compile-time branching. Explore `if consteval` and an `std::expected` parse helper in [question8.cpp](question8.cpp).

### 9. How do you summarize the evolution from C++11 to the forthcoming C++26 standard?
Use the table below to keep milestones straight and call out that C++26 is still in flux.

| Standard | Theme | Interview takeaway |
| --- | --- | --- |
| C++11 (2011) | Modernization 1.0 | Move semantics, lambdas, auto, concurrency primitives (`std::thread`, `std::async`). |
| C++14 (2014) | Polish | Generic lambdas, `std::make_unique`, relaxed constexpr, binary literals. |
| C++20 (2020) | Big feature wave | Concepts, ranges, coroutines, modules, `constexpr` expansion, calendar/tz library. |
| C++23 (2023) | Quality-of-life | `std::expected`, `if consteval`, more ranges adapters, `std::mdspan`, networking still pending. |
| C++26 (in progress) | Next objectives | Pattern matching, senders/receivers, executor model, contracts revival, reflection proposals—emphasize status as ongoing WG21 work. |

### 10. How do you manage thread lifetimes with `std::jthread` and `std::stop_token`?
`std::jthread` joins automatically and cooperates with `std::stop_token`, making cancellation safe even under early exits. Demonstrate the idiom in [question10.cpp](question10.cpp).

### 11. How do acquire/release atomics establish a happens-before relationship?
Pair a `store` with `memory_order_release` on the producer side and a `load` with `memory_order_acquire` on the consumer side to publish data safely. See [question11.cpp](question11.cpp) for a minimal flag handoff.

### 12. When should you reach for `std::span`?
Use `std::span` to present a uniform view over contiguous memory without copying, enabling APIs to accept `std::array`, `std::vector`, or raw arrays interchangeably. A normalization routine lives in [question12.cpp](question12.cpp).

### 13. Why adopt polymorphic allocators (`std::pmr`) in modern codebases?
`std::pmr` containers decouple allocation strategy from container type, unlocking arena allocation and reduced fragmentation with minimal refactoring. Explore the monotonic buffer example in [question13.cpp](question13.cpp).

## Study Tips
- Rehearse answers aloud while stepping through the linked code to solidify understanding.
- When adapting snippets, prefer modern C++ (17+) features unless targeting legacy code bases.
- Pair these questions with hands-on practice implementing additional variations such as allocator-aware types or concurrency primitives.
- Compile the snippets with the matching standard switch (e.g., `-std=c++20` or `/std:c++20`) to ensure the showcased features are enabled.

## Comprehensive C++ Interview Questions

This curated list covers foundational through senior-level C++ topics. Use it as a checklist; only create supporting samples when they illuminate uncertainty.

### Fundamentals & Basics

1. What are the differences between C and C++?<br>
	**Answer:** C++ extends C with classes, templates, exceptions, stronger type checking, namespaces, overloading, and a rich standard library while remaining largely source compatible with C.
2. Explain the concept of object-oriented programming and its four pillars.<br>
	**Answer:** OOP models software as interacting objects and relies on encapsulation, abstraction, inheritance, and polymorphism to manage complexity and reuse behavior.
3. What is the difference between struct and class in C++?<br>
	**Answer:** The only language-level difference is default access: structs default to public members and inheritance, while classes default to private; otherwise they are identical.
4. What are access specifiers in C++? Explain public, private, and protected.<br>
	**Answer:** Public members are accessible everywhere, protected members are accessible within the class and its derived classes, and private members are accessible only within the declaring class.
5. What is encapsulation and how is it achieved in C++?<br>
	**Answer:** Encapsulation hides internal representation behind a stable interface, typically enforced through access specifiers, getters/setters, and invariants maintained inside the class.
6. Explain the difference between stack and heap memory.<br>
	**Answer:** Stack memory is automatically managed with function scope lifetimes and very fast allocation, while heap memory is dynamically allocated, persists beyond scopes, and requires explicit management or smart pointers.
7. What is the size of a class/struct with no members?<br>
	**Answer:** The size is at least one byte so each distinct object has a unique address, even when the type is empty.
8. What are inline functions? When should you use them?<br>
	**Answer:** Inline functions hint that the compiler may substitute the function body at call sites; use them for small, frequently called functions where function-call overhead might be significant.
9. Explain the difference between `#include <file>` and `#include "file"`.<br>
	**Answer:** Angle brackets search only system include paths, while quotes search the current directory first and then fall back to system paths.
10. What is the purpose of the `const` keyword?<br>
	 **Answer:** `const` expresses immutability, preventing unintended modification of data, enabling compiler optimizations, and improving API contracts.
11. What is the difference between `const int*`, `int const*`, and `int* const`?<br>
	 **Answer:** `const int*` and `int const*` mean a pointer to constant int (pointee immutable), whereas `int* const` is a constant pointer to mutable int (pointer immutable).
12. What are references in C++? How do they differ from pointers?<br>
	 **Answer:** References are aliases that must bind to valid objects at initialization and cannot be reseated, while pointers can be null, reassigned, and require dereferencing.
13. Can you have a reference to a reference?<br>
	 **Answer:** Not directly; references collapse (e.g., `T& &` becomes `T&`), so multi-level references are not distinct types like pointer-to-pointer.
14. What is the difference between pass by value, pass by reference, and pass by pointer?<br>
	 **Answer:** Pass by value copies the argument, pass by reference aliases the original object with no copying, and pass by pointer passes an address that may be null and requires dereferencing.
15. What is the scope resolution operator (`::`)?<br>
	 **Answer:** `::` qualifies names to a specific namespace or class scope and can also reference the global namespace.

### Memory Management

16. What is RAII (Resource Acquisition Is Initialization)?<br>
	**Answer:** RAII binds resource lifetime to object lifetime so acquisition happens in constructors and automatic cleanup occurs in destructors, ensuring exception-safe management.
17. Explain the difference between `new`/`delete` and `malloc`/`free`.<br>
	**Answer:** `new`/`delete` allocate typed objects and call constructors/destructors, whereas `malloc`/`free` operate on raw memory without invoking object lifecycle hooks.
18. What are memory leaks and how can you prevent them?<br>
	**Answer:** A memory leak occurs when allocated memory is not released; prevent them by using RAII, smart pointers, containers, and diligent ownership tracking.
19. What is a dangling pointer?<br>
	**Answer:** A dangling pointer references memory that has been freed or gone out of scope, leading to undefined behavior when dereferenced.
20. What is the difference between shallow copy and deep copy?<br>
	**Answer:** A shallow copy duplicates only pointer values, while a deep copy duplicates the pointed-to resources so each object owns its own data.
21. What are smart pointers? Explain `unique_ptr`, `shared_ptr`, and `weak_ptr`.<br>
	**Answer:** Smart pointers manage dynamic memory automatically: `unique_ptr` enforces sole ownership, `shared_ptr` maintains shared ownership via reference counts, and `weak_ptr` observes shared objects without affecting lifetime.
22. When would you use `make_unique` and `make_shared`?<br>
	**Answer:** Use `make_unique` to create `unique_ptr` safely and concisely, and `make_shared` to create `shared_ptr` with a single allocation for the control block and object.
23. What is the rule of three/five/zero?<br>
	**Answer:** It states that if a class manages resources, implement (at least) destructor, copy constructor, and copy assignment; with C++11 add move constructor and move assignment; ideally design to need none (rule of zero) by delegating to RAII members.
24. How does move semantics improve performance?<br>
	**Answer:** Move semantics transfer resource ownership without copying the underlying data, eliminating expensive deep copies for temporaries and movable objects.
25. What are rvalue references and how do they relate to move semantics?<br>
	**Answer:** Rvalue references (`T&&`) bind to temporaries, allowing move constructors and move assignment operators to steal resources from expiring objects safely.
26. Explain perfect forwarding in C++.<br>
	**Answer:** Perfect forwarding preserves the value category of arguments when passing them through templates, typically implemented using forwarding references and `std::forward`.
27. What is placement new?<br>
	**Answer:** Placement new constructs an object in pre-allocated memory by invoking its constructor at a specified address without allocating additional storage.
28. How do you detect memory leaks in C++?<br>
	**Answer:** Use tools such as Valgrind, AddressSanitizer, Visual Studio diagnostics, or custom allocation trackers to identify allocations that are never freed.
29. What is the purpose of `std::move`?<br>
	**Answer:** `std::move` casts an object to an xvalue, signaling that its resources may be moved from without performing a copy.
30. What happens when you delete a `void` pointer?<br>
	**Answer:** Deleting a `void*` is undefined behavior because the compiler lacks the static type information needed to call the correct destructor.

### Object-Oriented Programming

31. What is polymorphism? Explain compile-time vs runtime polymorphism.<br>
	**Answer:** Polymorphism lets the same interface represent different underlying types; compile-time polymorphism uses overloading/templates resolved by the compiler, while runtime polymorphism uses virtual dispatch based on dynamic type.
32. What are virtual functions and how do they work?<br>
	**Answer:** Virtual functions allow derived classes to override behavior; the compiler uses a vtable/vptr mechanism to dispatch calls through base class pointers or references at runtime.
33. What is a pure virtual function?<br>
	**Answer:** A pure virtual function is declared with `= 0`, has no implementation in the base class, and forces derived classes to provide one, making the base abstract.
34. What is an abstract class?<br>
	**Answer:** An abstract class contains at least one pure virtual function and cannot be instantiated directly but provides a common interface for derived classes.
35. Can you instantiate an abstract class?<br>
	**Answer:** No; you must instantiate a concrete derived class that implements all pure virtual functions.
36. What is a virtual destructor and why is it important?<br>
	**Answer:** A virtual destructor ensures the correct derived destructor runs when deleting objects through base pointers, preventing resource leaks and incomplete cleanup.
37. What is the virtual table (vtable) and vptr?<br>
	**Answer:** The vtable is a compiler-generated table of virtual function pointers for a class, and each polymorphic object stores a hidden vptr pointing to its class's vtable.
38. What is function overloading?<br>
	**Answer:** Function overloading allows multiple functions with the same name but different parameter lists or constness, resolved by the compiler based on argument types.
39. What is operator overloading? Which operators cannot be overloaded?<br>
	**Answer:** Operator overloading provides custom behavior for operators on user-defined types; you cannot overload `::`, `.?`, `sizeof`, `typeid`, or conditional `?:`.
40. What is the difference between overloading and overriding?<br>
	**Answer:** Overloading defines multiple functions with the same name but different signatures in the same scope, whereas overriding replaces a virtual function's implementation in a derived class.
41. What is multiple inheritance? What problems can it cause?<br>
	**Answer:** Multiple inheritance allows a class to inherit from more than one base; it can cause ambiguity, diamond inheritance issues, and increased complexity.
42. What is the diamond problem and how do you solve it?<br>
	**Answer:** The diamond problem occurs when two base classes share a common ancestor, leading to duplicated subobjects; virtual inheritance ensures only one shared base subobject exists.
43. What is virtual inheritance?<br>
	**Answer:** Virtual inheritance shares a single base class instance among multiple inheritance paths, preventing duplication but requiring explicit constructor initialization.
44. What are access specifiers in inheritance (public, private, protected)?<br>
	**Answer:** Public inheritance preserves base access levels, protected inheritance makes public and protected members protected, and private inheritance makes them private in the derived class.
45. Can you call a virtual function from a constructor?<br>
	**Answer:** You can, but it resolves to the current class version because derived parts are not yet constructed, so relying on overrides is unsafe.
46. What is the Curiously Recurring Template Pattern (CRTP)?<br>
	**Answer:** CRTP is when a class template takes a derived class as a parameter, enabling static polymorphism and compile-time mixins.
47. Explain the difference between early binding and late binding.<br>
	**Answer:** Early binding resolves function calls at compile time (non-virtual functions), while late binding resolves at runtime via virtual dispatch.
48. What is a friend function and friend class?<br>
	**Answer:** Friends are non-member functions or classes granted access to a class's private and protected members for tightly coupled functionality.
49. What is the purpose of the `this` pointer?<br>
	**Answer:** `this` points to the current object inside member functions, enabling access to members and the object's address for chaining or disambiguation.
50. Can the `this` pointer be NULL?<br>
	**Answer:** In well-formed code `this` is never null; it is only null in contrived scenarios involving placement new or undefined behavior.

### Constructors & Destructors

51. What is a constructor? What types of constructors exist?<br>
	**Answer:** A constructor initializes an object; types include default, parameterized, copy, move, conversion, delegating, and inherited constructors.
52. What is a default constructor?<br>
	**Answer:** A default constructor takes no arguments (or all have defaults) and initializes objects when no explicit arguments are provided.
53. What is a copy constructor and when is it called?<br>
	**Answer:** A copy constructor takes a const reference to the same type and is invoked when copying objects, passing by value, or returning by value in certain contexts.
54. What is a move constructor?<br>
	**Answer:** A move constructor takes an rvalue reference and transfers resources from a temporary or expiring object, leaving it in a valid but unspecified state.
55. What is constructor chaining?<br>
	**Answer:** Constructor chaining is the process of one constructor calling another (within the same class or through base constructors) to reuse initialization logic.
56. What is a conversion constructor?<br>
	**Answer:** A conversion constructor allows implicit or explicit conversion from another type when it has a single parameter unless marked `explicit`.
57. What is the `explicit` keyword and why is it used?<br>
	**Answer:** `explicit` prevents unintended implicit conversions by requiring callers to construct objects intentionally with that constructor.
58. What is a destructor and when is it called?<br>
	**Answer:** A destructor cleans up resources and is called automatically when an object goes out of scope, is deleted, or the program exits.
59. Can a constructor be virtual?<br>
	**Answer:** No; constructors cannot be virtual because the object does not yet have a dynamic type during construction.
60. Can a destructor be virtual?<br>
	**Answer:** Yes, and polymorphic base classes should have virtual destructors to ensure proper cleanup via base pointers.
61. What is the order of constructor and destructor calls in inheritance?<br>
	**Answer:** Constructors run from base to derived and then member objects; destructors run in the reverse order (members, derived, base).
62. What is constructor delegation in C++11?<br>
	**Answer:** Delegating constructors call another constructor of the same class using an initializer list to centralize initialization logic.
63. What happens if you throw an exception from a constructor?<br>
	**Answer:** The partially constructed object is destroyed, already constructed members are cleaned up, and the exception propagates to the caller.
64. What is the copy-and-swap idiom?<br>
	**Answer:** It implements copy assignment by copying the argument, swapping state with `*this`, and letting the temporary destruct, providing strong exception safety.
65. What are initializer lists and why should you use them?<br>
	**Answer:** Initializer lists initialize base classes and members before the constructor body runs, ensuring correct order and efficiency, especially for const or reference members.

### Templates

66. What are templates in C++?<br>
	**Answer:** Templates let you write generic code that the compiler instantiates for specific types or values, enabling type-safe reuse.
67. What is the difference between function templates and class templates?<br>
	**Answer:** Function templates generate overloaded functions for different types, whereas class templates generate classes/structs parameterized by types or values.
68. What is template specialization?<br>
	**Answer:** Specialization provides a custom implementation for specific template arguments, overriding the generic version.
69. What is partial template specialization?<br>
	**Answer:** Partial specialization customizes templates when only some parameters meet certain criteria, leaving others generic.
70. What is SFINAE (Substitution Failure Is Not An Error)?<br>
	**Answer:** SFINAE removes template overloads from consideration when substitution fails, allowing fallback overload resolution without compilation errors.
71. What are variadic templates?<br>
	**Answer:** Variadic templates accept a parameter pack of arbitrary length, enabling functions or classes to handle any number of template arguments.
72. What is `std::enable_if` and when would you use it?<br>
	**Answer:** `std::enable_if` conditionally participates in overload resolution, typically used to constrain templates based on traits or expressions.
73. What is the difference between `typename` and `class` in templates?<br>
	**Answer:** In template parameter lists they are interchangeable, but `typename` is required inside templates to tell the compiler a dependent name denotes a type.
74. What are template template parameters?<br>
	**Answer:** They allow a template to accept another template as a parameter, enabling higher-order generic constructs.
75. What is template metaprogramming?<br>
	**Answer:** Template metaprogramming performs compile-time computation using templates, enabling static polymorphism, traits, and optimized code generation.
76. What are concepts in C++20?<br>
	**Answer:** Concepts are named predicates that constrain template parameters, providing clearer diagnostics and intent.
77. What is the difference between compile-time and runtime polymorphism?<br>
	**Answer:** Compile-time polymorphism uses overloads/templates resolved by the compiler, while runtime polymorphism uses virtual functions resolved during execution.
78. How do you debug template errors?<br>
	**Answer:** Simplify expressions, break code into smaller templates, use `static_assert`, compiler diagnostics, and tools like `-ftemplate-backtrace-limit` or `type_name` helpers.
79. What are fold expressions in C++17?<br>
	**Answer:** Fold expressions reduce parameter packs using a binary operator, compactly expressing operations like summation or logical conjunction.
80. What is `constexpr` and how does it relate to templates?<br>
	**Answer:** `constexpr` indicates values or functions evaluable at compile time, complementing templates by enabling constant expressions and metaprogramming.

### STL (Standard Template Library)

81. What are the main components of STL?<br>
	**Answer:** STL consists of containers, iterators, algorithms, function objects, and allocators that work together generically.
82. What is the difference between `vector` and `array`?<br>
	**Answer:** `std::vector` has dynamic size with heap storage, while `std::array` has fixed size determined at compile time and stored inline.
83. What is the difference between `vector` and `list`?<br>
	**Answer:** `vector` provides contiguous storage with random access and efficient push_back, whereas `list` is a doubly linked list with efficient insert/erase anywhere but poor locality.
84. What is the difference between `map` and `unordered_map`?<br>
	**Answer:** `map` is an ordered associative container backed by balanced trees with O(log n) operations, while `unordered_map` uses hashing for average O(1) operations without ordering.
85. What is the difference between `set` and `multiset`?<br>
	**Answer:** `set` stores unique keys, whereas `multiset` allows duplicate keys; both maintain sorted order.
86. When would you use `deque` instead of `vector`?<br>
	**Answer:** Use `deque` when you need efficient insertion/removal at both ends while still retaining random access, such as double-ended queues.
87. What are iterators? Explain different types of iterators.<br>
	**Answer:** Iterators generalize pointers for traversing containers; categories include input, output, forward, bidirectional, and random access iterators.
88. What is the difference between `begin()` and `cbegin()`?<br>
	**Answer:** `begin()` returns a mutable iterator (or const in const contexts), while `cbegin()` always returns a const iterator preventing modification.
89. What are algorithms in STL? Name some common ones.<br>
	**Answer:** Algorithms are generic operations on iterator ranges; examples include `std::sort`, `std::find`, `std::accumulate`, and `std::transform`.
90. What is the difference between `std::find` and `std::binary_search`?<br>
	**Answer:** `std::find` performs linear search on any range, while `std::binary_search` requires sorted ranges and performs logarithmic search.
91. What are function objects (functors)?<br>
	**Answer:** Functors are objects that implement `operator()` so they can be called like functions, often carrying state for algorithms.
92. What are lambda expressions?<br>
	**Answer:** Lambdas are inline, anonymous function objects introduced in C++11 with captured variables and concise syntax.
93. How do you capture variables in lambda expressions?<br>
	**Answer:** Use capture lists to capture by value (`=`), by reference (`&`), or specify individual captures like `[x, &y]`.
94. What is `std::function`?<br>
	**Answer:** `std::function` is a polymorphic function wrapper that can store any callable matching a signature, enabling type erasure for callables.
95. What is `std::bind`?<br>
	**Answer:** `std::bind` creates a callable by binding arguments to a function or functor, producing partial application placeholders.
96. What is the complexity of operations in `vector`, `list`, `map`?<br>
	**Answer:** `vector` offers O(1) random access and amortized O(1) push_back, `list` gives O(1) insert/erase given an iterator, and `map` provides O(log n) insert/find/erase.
97. What causes vector reallocation and how can you prevent it?<br>
	**Answer:** Exceeding capacity triggers reallocation and element moves; use `reserve` to pre-allocate when the size is known.
98. What is the difference between `emplace_back` and `push_back`?<br>
	**Answer:** `emplace_back` constructs elements in place using forwarded arguments, avoiding temporaries, while `push_back` copies or moves an existing object into the container.
99. What are `std::pair` and `std::tuple`?<br>
	**Answer:** `std::pair` holds two heterogeneous values, while `std::tuple` can hold an arbitrary number of heterogeneous values.
100. How do you iterate through a map?<br>
	 **Answer:** Use iterators (`for (auto& [key, value] : map)`) or explicit iterator loops to traverse key-value pairs in order.

### Modern C++ (C++11/14/17/20)

101. What are the new features introduced in C++11?<br>
	**Answer:** Key additions include move semantics, lambdas, `auto`, range-for, smart pointers, `nullptr`, variadic templates, and a standardized threading library.
102. What is `auto` keyword and type inference?<br>
	**Answer:** `auto` lets the compiler deduce variable types from initializers, reducing verbosity while preserving static typing.
103. What is `decltype`?<br>
	**Answer:** `decltype` yields the type of an expression without evaluating it, useful for template metaprogramming and deducing return types.
104. What is `nullptr` and how is it different from `NULL`?<br>
	**Answer:** `nullptr` is a typed null pointer constant of type `std::nullptr_t`, avoiding overload ambiguity that arises with `NULL` being an integer literal.
105. What are range-based for loops?<br>
	**Answer:** Range-based for loops iterate over containers or arrays using `for (auto& elem : container)` syntax, improving readability.
106. What is `std::array`?<br>
	**Answer:** `std::array` is a fixed-size container that wraps C-style arrays with STL-friendly interface and stack storage.
107. What are scoped enumerations (`enum class`)?<br>
	**Answer:** Scoped enums avoid implicit conversions to integers and scope their enumerators within the enum type.
108. What are uniform initialization and list initialization?<br>
	**Answer:** Brace initialization provides consistent syntax for constructing objects and prohibits narrowing conversions.
109. What is `static_assert`?<br>
	**Answer:** `static_assert` checks compile-time conditions, emitting descriptive errors if the predicate is false.
110. What are user-defined literals?<br>
	**Answer:** User-defined literals add custom suffixes to literals to create strongly typed values (e.g., `42_km`).
111. What is `std::thread` and how do you use it?<br>
	**Answer:** `std::thread` launches a new thread executing a callable; you manage its lifetime via `join()` or `detach()`.
112. What are mutexes and condition variables?<br>
	**Answer:** Mutexes provide mutual exclusion for critical sections, while condition variables coordinate threads waiting for state changes.
113. What is `std::async` and `std::future`?<br>
	**Answer:** `std::async` runs a function asynchronously and returns a `std::future` for retrieving the result or synchronizing completion.
114. What are atomics in C++?<br>
	**Answer:** Atomic types support lock-free or lock-based operations that are indivisible, preventing data races without explicit locks.
115. What is the memory model in C++11?<br>
	**Answer:** It formally defines visibility and ordering guarantees for multi-threaded programs, underpinning atomics and synchronization.
116. What is `std::optional` in C++17?<br>
	**Answer:** `std::optional` represents an optional value that may or may not be present, offering safer alternatives to sentinel values or pointers.
117. What is `std::variant`?<br>
	**Answer:** `std::variant` is a type-safe union that can hold one of multiple types at a time, requiring visitation to access.
118. What is `std::any`?<br>
	**Answer:** `std::any` stores a type-erased value with runtime type information, allowing storage of arbitrary types with casting.
119. What are structured bindings in C++17?<br>
	**Answer:** Structured bindings unpack tuples, pairs, or structs into named variables using tuple-like decomposition.
120. What is `if constexpr`?<br>
	**Answer:** `if constexpr` performs compile-time conditional branching, discarding branches that are not instantiated.
121. What are modules in C++20?<br>
	**Answer:** Modules provide a compiled interface mechanism that reduces build times and avoids macro pollution compared to headers.
122. What are coroutines?<br>
	**Answer:** Coroutines are functions that can suspend and resume, enabling asynchronous programming or lazy generators with minimal overhead.
123. What is `std::span`?<br>
	**Answer:** `std::span` is a non-owning view over contiguous sequences, allowing safe slicing without copying data.
124. What are three-way comparison operators (spaceship operator)?<br>
	**Answer:** The spaceship operator (`<=>`) performs unified comparisons, automatically generating relational operators and supporting partial ordering.
125. What are ranges in C++20?<br>
	**Answer:** Ranges provide composable, lazy views and algorithms that operate directly on range objects, reducing boilerplate.

### Exception Handling

126. What is exception handling in C++?<br>
	**Answer:** Exception handling provides language support for signaling and recovering from errors using `throw`, `try`, and `catch` constructs with automatic unwinding.
127. What are `try`, `catch`, and `throw` keywords?<br>
	**Answer:** `try` establishes a block that may throw, `throw` raises an exception object, and `catch` handles specific exception types.
128. What is the difference between `throw` and `throw()`?<br>
	**Answer:** `throw` raises an exception, whereas the deprecated `throw()` specification indicated a function would not throw; now replaced by `noexcept`.
129. What are exception specifications?<br>
	**Answer:** They declare which exceptions a function may throw; old dynamic specifications are removed, leaving only `noexcept` as the supported form.
130. What is `noexcept`?<br>
	**Answer:** `noexcept` indicates a function is guaranteed not to throw; violating it calls `std::terminate`.
131. What is stack unwinding?<br>
	**Answer:** Stack unwinding automatically destroys stack objects as control leaves scopes during exception propagation.
132. Can you catch all exceptions? How?<br>
	**Answer:** Yes, using `catch (...)` but it should be used carefully to avoid swallowing critical errors.
133. What is the exception hierarchy in C++?<br>
	**Answer:** Standard exceptions derive from `std::exception`, including `std::runtime_error`, `std::logic_error`, and others for specific conditions.
134. What happens if an exception is not caught?<br>
	**Answer:** The program calls `std::terminate`, typically aborting execution after any remaining stack unwinding.
135. What is `std::exception`?<br>
	**Answer:** `std::exception` is the base class for standard exceptions, providing a virtual `what()` message function.
136. What is the difference between error codes and exceptions?<br>
	**Answer:** Error codes require manual checking and propagation, while exceptions separate error paths from normal flow with automatic unwinding.
137. When should you use exceptions vs error codes?<br>
	**Answer:** Use exceptions for unexpected failures where normal flow cannot continue; use error codes for expected conditions or constrained environments.
138. What happens if an exception is thrown in a destructor?<br>
	**Answer:** If it propagates during stack unwinding, `std::terminate` is invoked; destructors should swallow or propagate via alternative mechanisms.
139. What is exception safety? Explain strong, basic, and no-throw guarantees.<br>
	**Answer:** Basic guarantee leaves objects valid but unspecified, strong guarantee provides rollback semantics, and no-throw guarantee promises operations will not throw.
140. What is `std::terminate`?<br>
	**Answer:** `std::terminate` aborts the program when an unhandled exception or `noexcept` violation occurs, invoking a customizable handler.

### Casting & Type Conversion

141. What are the different types of casts in C++?<br>
	**Answer:** Modern casts include `static_cast`, `dynamic_cast`, `const_cast`, and `reinterpret_cast`, each signaling intent and safety level.
142. What is `static_cast` and when should you use it?<br>
	**Answer:** `static_cast` performs compile-time conversions such as numeric casts, up/down casts within class hierarchies (when safe), and lvalue-to-rvalue transformations.
143. What is `dynamic_cast` and when should you use it?<br>
	**Answer:** `dynamic_cast` safely downcasts polymorphic types at runtime, returning `nullptr` or throwing `bad_cast` when the cast fails.
144. What is `const_cast`?<br>
	**Answer:** `const_cast` adds or removes cv-qualification; modifying original const objects after removal is undefined behavior.
145. What is `reinterpret_cast`?<br>
	**Answer:** `reinterpret_cast` reinterprets bit patterns between unrelated types and should be reserved for low-level tasks that respect strict aliasing rules.
146. What is the difference between C-style cast and C++ casts?<br>
	**Answer:** C-style casts attempt multiple conversions silently, masking intent; C++ casts are explicit, safer, and easier to search.
147. What is type punning?<br>
	**Answer:** Type punning treats a memory region as a different type, typically using unions or casts; it risks undefined behavior if not done carefully.
148. What is the difference between implicit and explicit type conversion?<br>
	**Answer:** Implicit conversions happen automatically (e.g., integer promotion), while explicit conversions require casts or constructors and express programmer intent.
149. When does `dynamic_cast` return `nullptr`?<br>
	**Answer:** It returns `nullptr` when the dynamic type of the object is not compatible with the requested type during pointer casts.
150. Can you cast away constness? Should you?<br>
	**Answer:** You can with `const_cast`, but you should only do so when the original object is non-const; otherwise, modifying it triggers undefined behavior.

### Multithreading & Concurrency

151. What is a race condition?<br>
	**Answer:** A race condition occurs when multiple threads access shared data without proper synchronization and the outcome depends on execution order.
152. What is a deadlock? How can you prevent it?<br>
	**Answer:** Deadlock happens when threads wait indefinitely for each other; prevent it via lock ordering, lock hierarchy, timeouts, or lock-free designs.
153. What is thread safety?<br>
	**Answer:** Thread safety means the code functions correctly even when accessed concurrently by multiple threads, typically through synchronization or immutability.
154. What is the difference between mutex and semaphore?<br>
	**Answer:** A mutex provides mutual exclusion for a single resource, while a semaphore counts available resources and can allow multiple simultaneous holders.
155. What is `std::lock_guard`?<br>
	**Answer:** `std::lock_guard` is an RAII wrapper that locks a mutex upon construction and unlocks it upon destruction.
156. What is `std::unique_lock`?<br>
	**Answer:** `std::unique_lock` offers flexible locking with deferred locking, timed locking, and manual unlock control, often used with condition variables.
157. What is `std::scoped_lock`?<br>
	**Answer:** `std::scoped_lock` is an RAII lock that can lock multiple mutexes at once without deadlock by using a deadlock-avoidance algorithm.
158. What is the difference between `std::thread::join` and `detach`?<br>
	**Answer:** `join()` waits for a thread to finish and cleans up resources; `detach()` lets the thread run independently with no future synchronization.
159. What is a condition variable and when would you use it?<br>
	**Answer:** A condition variable allows threads to wait for specific conditions while releasing a mutex, commonly used in producer-consumer scenarios.
160. What is `std::atomic` and when should you use it?<br>
	**Answer:** `std::atomic` provides atomic operations on variables, ensuring lock-free or thread-safe updates without explicit mutexes when possible.
161. What is memory ordering in atomics?<br>
	**Answer:** Memory ordering defines visibility guarantees of atomic operations across threads, with modes like relaxed, acquire/release, and sequentially consistent.
162. What is the ABA problem?<br>
	**Answer:** The ABA problem occurs when an atomic compares equal but the value changed to a different value and back, potentially misleading lock-free algorithms.
163. What is a spin lock?<br>
	**Answer:** A spin lock is a CPU-intensive lock where threads repeatedly check the lock variable, suitable for short critical sections.
164. What is thread local storage?<br>
	**Answer:** Thread local storage provides each thread its own instance of a variable using `thread_local`, avoiding synchronization for thread-specific data.
165. What is the producer-consumer problem?<br>
	**Answer:** It models coordinating producers that generate data and consumers that process it, requiring synchronization to manage shared queues.

### Advanced Concepts

166. What is alignment and padding in structs?<br>
	**Answer:** Alignment ensures data members reside at addresses suitable for the CPU, and padding bytes may be inserted to satisfy alignment requirements.
167. What is the purpose of `#pragma pack`?<br>
	**Answer:** `#pragma pack` changes structure packing to reduce padding, often used for binary protocols but may degrade performance and portability.
168. What are POD (Plain Old Data) types?<br>
	**Answer:** POD types have trivial constructors, destructors, and standard layout, making them compatible with C and safe for memcpy or binary IO.
169. What is the difference between aggregate and non-aggregate types?<br>
	**Answer:** Aggregates can be initialized with brace lists without constructors, while non-aggregates require constructors or have private members/inheritance.
170. What is the One Definition Rule (ODR)?<br>
	**Answer:** ODR mandates that each program entity has exactly one definition across the program to avoid linker conflicts and undefined behavior.
171. What is name mangling?<br>
	**Answer:** Name mangling encodes function signatures into symbol names to support overloading and namespaces during linkage.
172. What is `extern "C"`?<br>
	**Answer:** `extern "C"` suppresses C++ name mangling to allow linkage with C code or external libraries.
173. What is the difference between declaration and definition?<br>
	**Answer:** A declaration introduces a symbol's name and type, while a definition allocates storage or provides the function/body implementation.
174. What are forward declarations?<br>
	**Answer:** Forward declarations declare the existence of types or functions without defining them, reducing dependencies and compile times.
175. What is Argument Dependent Lookup (ADL)?<br>
	**Answer:** ADL extends function lookup to include namespaces associated with argument types, facilitating operator overloading and custom functions.
176. What is Return Value Optimization (RVO) and Named RVO (NRVO)?<br>
	**Answer:** RVO and NRVO allow compilers to elide temporary objects when returning values, constructing results directly in the caller's space.
177. What is the as-if rule?<br>
	**Answer:** The as-if rule lets compilers perform any optimization as long as observable program behavior remains unchanged.
178. What is undefined behavior (UB)?<br>
	**Answer:** UB occurs when code violates language rules, allowing compilers to produce unpredictable results without guarantees.
179. What is implementation-defined behavior?<br>
	**Answer:** Implementation-defined behavior is specified by the compiler for certain constructs (e.g., integer sizes) and documented for portability.
180. What is unspecified behavior?<br>
	**Answer:** Unspecified behavior has multiple allowed outcomes with no guaranteed choice, such as the order of function argument evaluation (pre-C++17).
181. What is sequence point?<br>
	**Answer:** A sequence point (now sequenced-before relationship) ensures evaluations before it complete before the next step, preventing undefined behavior from reordering.
182. What are volatile variables?<br>
	**Answer:** `volatile` tells the compiler the value may change unexpectedly (e.g., hardware registers) and prevents certain optimizations.
183. What is `restrict` keyword (C99/C++)?<br>
	**Answer:** `restrict` (available in C++ via extensions) promises that pointers do not alias, enabling optimization; use `__restrict` or compiler-specific forms.
184. What is the `mutable` keyword?<br>
	**Answer:** `mutable` allows modification of a member even inside const member functions, useful for caches or lazy initialization.
185. What is the `register` keyword (deprecated)?<br>
	**Answer:** `register` suggested storing variables in CPU registers for speed; modern compilers ignore it, and it is deprecated.

### Design Patterns

186. What is the Singleton pattern? How do you implement it in C++?<br>
	**Answer:** Singleton guarantees a single instance and global access, typically using a private constructor and a static accessor with thread-safe initialization.
187. What is the Factory pattern?<br>
	**Answer:** Factory encapsulates object creation logic, returning base pointers based on input without exposing concrete types.
188. What is the Abstract Factory pattern?<br>
	**Answer:** Abstract Factory creates families of related objects through interfaces, letting clients switch product variants without code changes.
189. What is the Observer pattern?<br>
	**Answer:** Observer establishes a publish-subscribe relationship where subjects notify registered observers of state changes.
190. What is the Strategy pattern?<br>
	**Answer:** Strategy encapsulates interchangeable algorithms behind a common interface, enabling runtime selection.
191. What is the Decorator pattern?<br>
	**Answer:** Decorator wraps objects to add responsibilities dynamically without altering the original class.
192. What is the Adapter pattern?<br>
	**Answer:** Adapter converts one interface into another expected by clients, allowing interoperability with legacy or third-party components.
193. What is PIMPL (Pointer to Implementation) idiom?<br>
	**Answer:** PIMPL hides implementation details behind an opaque pointer, reducing compile dependencies and stabilizing ABI.
194. What is the Dependency Injection pattern?<br>
	**Answer:** Dependency Injection supplies dependencies from outside a class (via constructors, setters, or interfaces) to decouple components and ease testing.
195. What is the RAII pattern?<br>
	**Answer:** RAII acquires resources in constructors and releases them in destructors, ensuring deterministic cleanup.

### Compilation & Linking

196. What are the stages of compilation?<br>
	**Answer:** Source code passes through preprocessing, compilation to object files, optional optimization, and linking into executables or libraries.
197. What is the difference between compilation and linking?<br>
	**Answer:** Compilation translates individual translation units to object code, whereas linking resolves symbols across objects to produce final binaries.
198. What are translation units?<br>
	**Answer:** A translation unit is a source file after preprocessing, including all headers and expansions.
199. What is a header file and why do we use header guards?<br>
	**Answer:** Header files declare interfaces; guards or `#pragma once` prevent multiple inclusion leading to redefinition errors.
200. What is `#pragma once`?<br>
	**Answer:** `#pragma once` is a non-standard but widely supported directive that ensures a header is included only once per translation unit.
201. What are static libraries vs shared/dynamic libraries?<br>
	**Answer:** Static libraries are archives linked into executables at build time, while shared libraries are loaded at runtime and can be shared among processes.
202. What is symbol visibility?<br>
	**Answer:** Symbol visibility determines whether functions or variables are exported outside a translation unit or library; controlling it minimizes API surface and link conflicts.
203. What is the difference between static linking and dynamic linking?<br>
	**Answer:** Static linking copies library code into the executable, increasing size but simplifying deployment; dynamic linking defers loading to runtime, enabling updates and smaller binaries.
204. What are weak symbols?<br>
	**Answer:** Weak symbols allow definitions to be overridden by strong ones during linking, commonly used for optional hooks.
205. What is precompiled header?<br>
	**Answer:** A precompiled header stores processed header content, speeding compilation by reusing common includes across translation units.
206. What is Link Time Optimization (LTO)?<br>
	**Answer:** LTO performs whole-program optimization at link time by analyzing and optimizing across object file boundaries.
207. What are compile-time vs link-time vs runtime errors?<br>
	**Answer:** Compile-time errors arise during translation, link-time errors occur when resolving symbols, and runtime errors happen while executing the program.
208. What is the difference between `-O0`, `-O1`, `-O2`, `-O3` optimization levels?<br>
	**Answer:** These compiler flags control optimization aggressiveness, with `-O0` disabling most optimizations, `-O2` providing balanced optimizations, and `-O3` enabling aggressive optimizations potentially increasing code size.
209. What is Position Independent Code (PIC)?<br>
	**Answer:** PIC can execute correctly regardless of its load address, a requirement for shared libraries to support ASLR and relocation.
210. What is the difference between debug and release builds?<br>
	**Answer:** Debug builds include symbols and minimal optimization for easier debugging, while release builds optimize for performance and reduce binary size.

### Performance & Optimization

211. What is cache locality and why does it matter?<br>
	**Answer:** Cache locality refers to accessing data close together in time or space, improving cache hit rates and performance.
212. What is branch prediction?<br>
	**Answer:** CPUs guess the outcome of conditional branches to keep pipelines full; mispredictions incur penalties, so predictable branches run faster.
213. What is loop unrolling?<br>
	**Answer:** Loop unrolling duplicates loop bodies to reduce overhead and increase instruction-level parallelism, at the cost of code size.
214. What is inlining and when is it beneficial?<br>
	**Answer:** Inlining replaces a function call with its body, eliminating call overhead; it benefits small, frequently called functions and enables further optimization.
215. What is the difference between `-O2` and `-O3` optimization?<br>
	**Answer:** `-O2` applies safe optimizations for speed without significantly increasing size, while `-O3` enables more aggressive optimizations that may bloat binaries.
216. What is the `likely`/`unlikely` attribute?<br>
	**Answer:** Attributes or builtins (e.g., `[[likely]]`) hint to the compiler about branch probability, guiding layout for fewer mispredictions.
217. What tools can you use for profiling C++ code?<br>
	**Answer:** Tools include `perf`, VTune, Instruments, Visual Studio Profiler, gprof, and sampling profilers integrated into IDEs.
218. What is the cost of virtual function calls?<br>
	**Answer:** Virtual calls add indirection through the vtable and inhibit inlining, marginally increasing latency compared to direct calls.
219. What is Small String Optimization (SSO)?<br>
	**Answer:** SSO stores short strings inside the string object itself, avoiding heap allocations for common cases.
220. What is the cost of exception handling?<br>
	**Answer:** Zero-cost implementations incur overhead only when exceptions are thrown, but thrown exceptions require unwinding tables and runtime processing.
221. What is the difference between `std::vector` and `std::array` in terms of performance?<br>
	**Answer:** `std::vector` involves heap allocation and potential reallocations, whereas `std::array` resides inline and has no allocation overhead.
222. What is copy elision and when does it happen?<br>
	**Answer:** Copy elision allows compilers to omit copy/move operations, especially when returning local objects or constructing temporaries.
223. What is zero-cost abstraction?<br>
	**Answer:** Zero-cost abstraction means high-level constructs compile down to code as efficient as hand-written low-level implementations.
224. How do you minimize cache misses?<br>
	**Answer:** Use contiguous data structures, align memory, prefetch, avoid random access patterns, and batch operations for improved locality.
225. What is data-oriented design?<br>
	**Answer:** Data-oriented design organizes programs around data layout and access patterns to exploit caches, SIMD, and modern hardware efficiently.

### Best Practices & Code Quality

226. What is SOLID principle?<br>
	**Answer:** SOLID is a set of five design principles promoting maintainable code: single responsibility, open/closed, Liskov substitution, interface segregation, and dependency inversion.
227. What is DRY (Don't Repeat Yourself)?<br>
	**Answer:** DRY encourages eliminating duplicate logic by centralizing code, reducing bugs and maintenance effort.
228. What is KISS (Keep It Simple, Stupid)?<br>
	**Answer:** KISS advocates for simple solutions, avoiding unnecessary complexity that hinders understanding and maintenance.
229. What is YAGNI (You Aren't Gonna Need It)?<br>
	**Answer:** YAGNI advises against implementing features before they are necessary, preventing overengineering.
230. What are code smells?<br>
	**Answer:** Code smells are patterns signaling potential design issues, such as large classes, duplicated code, or long parameter lists.
231. What is technical debt?<br>
	**Answer:** Technical debt describes shortcuts in design or implementation that incur future maintenance costs.
232. What is the difference between composition and inheritance?<br>
	**Answer:** Composition builds complex behavior by combining objects, while inheritance derives new types from existing ones.
233. When should you use composition over inheritance?<br>
	**Answer:** Prefer composition when you need flexible behavior changes at runtime or to avoid tight coupling inherent in inheritance.
234. What is dependency inversion?<br>
	**Answer:** Dependency inversion states that high-level modules should depend on abstractions, not concrete implementations.
235. What is interface segregation?<br>
	**Answer:** Interface segregation recommends providing small, focused interfaces so clients only implement what they need.
236. What are coding standards and why are they important?<br>
	**Answer:** Coding standards ensure consistent style and practices, improving readability and facilitating team collaboration.
237. What tools can you use for static code analysis?<br>
	**Answer:** Tools include clang-tidy, cppcheck, PVS-Studio, and SonarQube, which detect potential bugs and style issues.
238. What is the purpose of const correctness?<br>
	**Answer:** Const correctness communicates immutability, enables compiler optimizations, and prevents accidental modifications.
239. What is defensive programming?<br>
	**Answer:** Defensive programming anticipates misuse or unexpected inputs, validating assumptions and failing safely.
240. What are assertions and when should you use them?<br>
	**Answer:** Assertions verify program invariants during development; they should guard internal assumptions but often compile out in production.

### Testing & Debugging

241. What is unit testing?<br>
	**Answer:** Unit testing verifies individual components in isolation to ensure correctness and prevent regressions.
242. What are some C++ unit testing frameworks?<br>
	**Answer:** Common frameworks include GoogleTest, Catch2, doctest, and Boost.Test.
243. What is Test-Driven Development (TDD)?<br>
	**Answer:** TDD cycles through writing tests first, implementing code, and refactoring, promoting small, verifiable increments.
244. What is mocking in unit tests?<br>
	**Answer:** Mocking replaces real dependencies with test doubles to isolate the unit under test and control behavior.
245. What is the difference between `assert` and `static_assert`?<br>
	**Answer:** `assert` checks runtime conditions, while `static_assert` validates compile-time expressions and prevents compilation when false.
246. What tools can you use for debugging C++ code?<br>
	**Answer:** Debbugers like gdb, lldb, Visual Studio Debugger, and IDE-integrated tools assist with breakpoints and inspection.
247. What is Valgrind and what does it do?<br>
	**Answer:** Valgrind is a runtime analysis tool that detects memory leaks, invalid accesses, and threading issues.
248. What is AddressSanitizer?<br>
	**Answer:** AddressSanitizer (ASan) is a compiler sanitizer detecting buffer overflows, use-after-free, and other memory errors.
249. What is ThreadSanitizer?<br>
	**Answer:** ThreadSanitizer (TSan) detects data races and threading errors by instrumenting code during compilation.
250. What is UndefinedBehaviorSanitizer?<br>
	**Answer:** UBSan detects undefined behavior at runtime, such as signed integer overflow or invalid type punning.
251. How do you debug memory leaks?<br>
	**Answer:** Use tools like Valgrind, ASan, or custom allocators with tracking, and analyze allocation/deallocation paths.
252. How do you debug race conditions?<br>
	**Answer:** Employ TSan, logging, determinism techniques, or reduce concurrency to isolate problematic interleavings.
253. What is core dump?<br>
	**Answer:** A core dump captures a program's memory and state at crash time, useful for post-mortem debugging.
254. What is a debugger breakpoint?<br>
	**Answer:** A breakpoint pauses execution at a specified location to allow inspection of state.
255. What is watchpoint?<br>
	**Answer:** A watchpoint (data breakpoint) halts execution when a monitored memory location is read or written.

### File I/O & Streams

256. What is the difference between `iostream`, `fstream`, and `sstream`?<br>
	**Answer:** `iostream` handles console I/O, `fstream` manages file streams, and `stringstream` operates on in-memory strings.
257. What is the difference between `>>` and `getline()`?<br>
	**Answer:** Extraction `>>` stops at whitespace and ignores leading whitespace, whereas `getline()` reads entire lines including spaces.
258. How do you read/write binary files in C++?<br>
	**Answer:** Open file streams with the `std::ios::binary` flag and use `read`/`write` or stream operators on raw buffers.
259. What is the difference between text mode and binary mode?<br>
	**Answer:** Text mode may translate newline characters and treat special control characters, while binary mode preserves bytes as-is.
260. What are stream manipulators?<br>
	**Answer:** Stream manipulators like `std::hex`, `std::setw`, `std::fixed`, and `std::setprecision` adjust formatting for stream operations.
261. What is `std::setprecision`?<br>
	**Answer:** `std::setprecision` controls the number of digits printed for floating-point values.
262. What is `std::setw`?<br>
	**Answer:** `std::setw` sets the width of the next field inserted into the stream, padding if necessary.
263. How do you check if a file was opened successfully?<br>
	**Answer:** After opening, test the stream with `if (!file)` or `file.is_open()` to ensure the operation succeeded.
264. What is the difference between `ifstream`, `ofstream`, and `fstream`?<br>
	**Answer:** `ifstream` reads from files, `ofstream` writes to files, and `fstream` supports both reading and writing.
265. What are stream states (good, bad, fail, eof)?<br>
	**Answer:** `good` means the stream is usable, `bad` indicates irrecoverable errors, `fail` marks recoverable read/write failures, and `eof` signals end-of-file.

### Preprocessor

266. What is the preprocessor?<br>
	**Answer:** The preprocessor runs before compilation to handle directives like includes, macros, and conditional compilation.
267. What is the difference between `#define` and `const`?<br>
	**Answer:** `#define` performs textual substitution without type safety, whereas `const` creates typed constants recognized by the compiler.
268. What are macros? What are the dangers of using macros?<br>
	**Answer:** Macros are preprocessor substitutions; they can cause hard-to-debug issues due to lack of scope, type checking, and unexpected expansions.
269. What is the difference between `#ifdef` and `#if defined`?<br>
	**Answer:** Both test macro presence; `#ifdef` is shorthand for `#if defined(MACRO)` while `#if defined` can combine expressions with logical operators.
270. What is `#undef`?<br>
	**Answer:** `#undef` removes a macro definition, preventing further substitutions.
271. What are predefined macros (`__FILE__`, `__LINE__`, etc.)?<br>
	**Answer:** They provide compiler-set information like current file name, line number, and compilation date/time for diagnostics.
272. What is conditional compilation?<br>
	**Answer:** Conditional compilation includes or excludes code based on macros, enabling platform-specific or feature toggles.
273. What is the difference between `#include` and `import` (C++20)?<br>
	**Answer:** `#include` textually inserts headers, while `import` uses modules with compiled interfaces for better encapsulation and build times.
274. What are header guards and why are they needed?<br>
	**Answer:** Header guards prevent multiple inclusion of the same header, avoiding duplicate definitions during compilation.
275. What is the `##` operator in macros?<br>
	**Answer:** The `##` token-pasting operator concatenates tokens to form new identifiers during macro expansion.

### Namespace

276. What are namespaces and why are they used?<br>
	**Answer:** Namespaces group related identifiers to avoid name collisions and organize code.
277. What is the `std` namespace?<br>
	**Answer:** `std` contains all standard library symbols defined by the C++ standard.
278. What is the using directive vs using declaration?<br>
	**Answer:** A using directive (`using namespace`) imports all names from a namespace, while a using declaration imports a specific symbol.
279. Why is `using namespace std;` considered bad practice?<br>
	**Answer:** It pollutes the global namespace, risking name clashes and ambiguous overload resolution, especially in headers.
280. What are anonymous/unnamed namespaces?<br>
	**Answer:** Anonymous namespaces give internal linkage to symbols, confining them to the translation unit.
281. What are inline namespaces?<br>
	**Answer:** Inline namespaces allow versioned APIs while keeping symbols accessible without qualification.
282. What is namespace aliasing?<br>
	**Answer:** Namespace aliasing creates a shorter alias for a namespace, improving readability for deeply nested names.
283. What is ADL (Argument Dependent Lookup) and namespaces?<br>
	**Answer:** ADL extends function lookup to include namespaces associated with argument types, enabling operator overloading patterns.
284. Can you have nested namespaces?<br>
	**Answer:** Yes, nested namespaces organize code hierarchically and can be declared compactly (`namespace a::b {}`).
285. What is namespace pollution?<br>
	**Answer:** Namespace pollution occurs when too many names are introduced into broader scopes, causing conflicts and ambiguity.

### Miscellaneous

286. What is the difference between array and pointer?<br>
	**Answer:** Arrays have fixed size and store elements inline, while pointers hold an address and can point to varying sequences.
287. What is array decay?<br>
	**Answer:** Array decay occurs when arrays convert to pointers to their first element in most expressions, losing size information.
288. What is the `sizeof` operator?<br>
	**Answer:** `sizeof` yields the size in bytes of a type or object at compile time.
289. What is the difference between `++i` and `i++`?<br>
	**Answer:** `++i` pre-increments and returns the incremented value, while `i++` post-increments and returns the old value, potentially creating a temporary.
290. What is short-circuit evaluation?<br>
	**Answer:** Logical operators `&&` and `||` evaluate operands left to right and stop once the result is determined.
291. What is the ternary operator?<br>
	**Answer:** The ternary operator `condition ? expr1 : expr2` selects one of two expressions based on a boolean condition.
292. What is the comma operator?<br>
	**Answer:** The comma operator evaluates two expressions sequentially and yields the value of the second.
293. What are bitwise operators?<br>
	**Answer:** Bitwise operators (`&`, `|`, `^`, `~`, `<<`, `>>`) manipulate individual bits of integral types.
294. What is bit manipulation and when is it useful?<br>
	**Answer:** Bit manipulation adjusts bits for tasks like flags, hashing, cryptography, or low-level performance optimizations.
295. What is the difference between `&` and `&&`?<br>
	**Answer:** `&` performs bitwise AND or references, while `&&` performs logical AND with short-circuiting or denotes rvalue references in declarations.
296. What is the difference between `|` and `||`?<br>
	**Answer:** `|` performs bitwise OR, and `||` performs logical OR with short-circuiting.
297. What is type aliasing (`typedef` vs `using`)?<br>
	**Answer:** Both create aliases for types; `using` is more flexible, especially for templates, while `typedef` is the older syntax.
298. What are attributes in C++ (e.g., `[[nodiscard]]`)?<br>
	**Answer:** Attributes provide metadata to compilers about code behavior, influencing warnings or optimizations.
299. What is `[[nodiscard]]` and when should you use it?<br>
	**Answer:** `[[nodiscard]]` warns when a function's return value is ignored, useful for error codes and important results.
300. What is `[[deprecated]]`?<br>
	**Answer:** `[[deprecated]]` marks entities as discouraged, generating warnings when used to aid migration.

### Advanced Topics

301. What is template metaprogramming?<br>
	**Answer:** Template metaprogramming performs computations at compile time using templates, enabling static dispatch and optimized code paths.
302. What is expression templates?<br>
	**Answer:** Expression templates build abstract syntax trees of expressions to defer evaluation and eliminate temporaries, common in numeric libraries.
303. What is policy-based design?<br>
	**Answer:** Policy-based design composes class behavior from template parameters representing policies, allowing configurable strategies.
304. What is type erasure?<br>
	**Answer:** Type erasure hides concrete types behind a uniform interface at runtime, often via virtual functions or wrappers like `std::function`.
305. What is the Barton-Nackman trick?<br>
	**Answer:** It's a CRTP pattern implementing operators in base templates that depend on derived types, enabling static polymorphism.
306. What is SFINAE and how is it used?<br>
	**Answer:** SFINAE removes invalid template instantiations from overload resolution, allowing fallback implementations and trait-based enablement.
307. What are tag dispatch techniques?<br>
	**Answer:** Tag dispatch selects overloads based on type traits by passing tag objects, delivering compile-time polymorphism with readable code.
308. What is the Empty Base Optimization (EBO)?<br>
	**Answer:** EBO lets compilers eliminate storage for empty base classes so derived objects don't waste space.
309. What is the `[[no_unique_address]]` attribute?<br>
	**Answer:** It allows the compiler to reuse storage for empty members, extending EBO-like optimizations to member variables.
310. What is the spaceship operator and how does it simplify comparisons?<br>
	**Answer:** The `<=>` operator returns strong/weak ordering results and can auto-generate the traditional relational operators.
311. What are concepts and constraints in C++20?<br>
	**Answer:** Concepts define compile-time predicates on template parameters, enabling constrained templates with clearer diagnostics.
312. What are `requires` expressions?<br>
	**Answer:** `requires` expressions check compile-time conditions within concepts or templates, specifying valid operations on types.
313. What is `std::is_same` and other type traits?<br>
	**Answer:** Type traits are compile-time utilities to query type properties (`std::is_same`, `std::is_trivially_copyable`, etc.), guiding template logic.
314. What is compile-time if (`if constexpr`)?<br>
	**Answer:** `if constexpr` evaluates conditions at compile time, discarding untrue branches and preventing substitution errors.
315. What is `std::invoke`?<br>
	**Answer:** `std::invoke` uniformly calls any callable (function, member pointer, functor) with provided arguments, respecting reference wrappers.

### Real-World Scenarios

316. How would you implement a thread-safe singleton?<br>
	**Answer:** Use a `static` local variable inside an accessor (Meyers' singleton) or `std::call_once` to ensure thread-safe lazy initialization.
317. How would you implement a custom allocator?<br>
	**Answer:** Derive from `std::allocator` or implement the required allocator interface managing memory blocks, often using pools or arenas.
318. How would you implement a custom iterator?<br>
	**Answer:** Define iterator traits, provide required operators (`*`, `->`, `++`, comparison), and model the appropriate iterator category.
319. How would you implement type-safe `printf` using variadic templates?<br>
	**Answer:** Parse the format string at compile time and use variadic templates with fold expressions or recursion to validate argument types and emit output.
320. How would you implement observer pattern in C++?<br>
	**Answer:** Maintain a list of observer callbacks (interfaces or `std::function`) in the subject and notify them on state changes.
321. How do you handle resource cleanup in the presence of exceptions?<br>
	**Answer:** Employ RAII wrappers, smart pointers, and scope guards to ensure deterministic release regardless of control flow.
322. How would you implement a cache with LRU eviction policy?<br>
	**Answer:** Combine a hash map for lookups with a doubly linked list to track usage order, moving accessed items to the front and evicting from the back.
323. How would you implement a producer-consumer queue?<br>
	**Answer:** Use a thread-safe queue protected by a mutex and condition variable, or a lock-free structure if latencies require.
324. How would you implement a memory pool?<br>
	**Answer:** Pre-allocate a large block and manage free lists of fixed-size chunks, handing out memory without calling the general allocator.
325. How would you implement a circular buffer?<br>
	**Answer:** Store elements in a fixed-size array with head/tail indices that wrap around, overwriting or blocking when full depending on policy.

### Code Review Questions

326. What are potential issues with this code: `char* str = "Hello";`?<br>
	**Answer:** String literals are immutable; assigning to `char*` invites unintended modification and should be `const char*`.
327. What's wrong with: `if (ptr = nullptr)`?<br>
	**Answer:** It assigns nullptr instead of comparing, always evaluates false, and overwrites the pointer; use `==` for comparisons.
328. Why is `delete this;` dangerous?<br>
	**Answer:** It assumes heap allocation and careful lifetime management; misuse leads to double deletes or dangling references.
329. What's the problem with returning a reference to a local variable?<br>
	**Answer:** The local variable is destroyed when the function returns, leaving a dangling reference and undefined behavior.
330. What's wrong with comparing floating-point numbers using `==`?<br>
	**Answer:** Floating-point rounding errors make exact equality unreliable; compare using tolerances or relative error checks.
331. Why should you avoid calling virtual functions in constructors/destructors?<br>
	**Answer:** During construction/destruction the dynamic type is not fully formed, so virtual dispatch may call base implementations unexpectedly.
332. What's the issue with not checking return values of `new`?<br>
	**Answer:** Although `new` throws on failure by default, using `nothrow` requires checking; ignoring it can hide allocation failures.
333. Why is it dangerous to use dangling pointers?<br>
	**Answer:** Dangling pointers reference freed or invalid memory, causing undefined behavior when accessed.
334. What's wrong with: `std::vector<bool>`?<br>
	**Answer:** It stores bits via proxy references rather than real bools, causing surprising behavior with references and pointers.
335. Why should you avoid inheriting from STL containers?<br>
	**Answer:** STL containers lack virtual destructors and are not designed for inheritance, risking slicing and violating Liskov substitution; prefer composition.

### Behavioral & Problem-Solving

336. How would you debug a crash in production?<br>
	**Answer:** Collect logs and crash dumps, reproduce in a controlled environment, and use debuggers or symbolicated traces to identify root causes.
337. How do you approach performance optimization?<br>
	**Answer:** Measure first with profilers, formulate hypotheses, make targeted changes, and validate improvements with benchmarks.
338. Describe a challenging C++ problem you solved.<br>
	**Answer:** Provide a specific example detailing the problem, tools used, trade-offs considered, and final outcome.
339. How do you keep up with C++ standards and best practices?<br>
	**Answer:** Follow WG21 papers, cppreference updates, community blogs, conferences, and experiment with new features.
340. What's your experience with different C++ compilers (GCC, Clang, MSVC)?<br>
	**Answer:** Discuss projects targeting multiple compilers, platform-specific quirks, and how you manage portability.
341. How do you handle memory constraints in embedded systems?<br>
	**Answer:** Use static allocation, fixed-size buffers, custom allocators, and rigorous profiling to stay within limits.
342. How would you refactor legacy C++ code?<br>
	**Answer:** Establish tests, refactor incrementally, modernize APIs, and remove technical debt while ensuring behavior stays intact.
343. What metrics do you use to measure code quality?<br>
	**Answer:** Metrics include defect rates, cyclomatic complexity, code coverage, static analysis results, and code review findings.
344. How do you balance performance and maintainability?<br>
	**Answer:** Opt for clear designs first, optimize hotspots with profiling data, and document trade-offs for future maintainers.
345. Describe your experience with cross-platform C++ development.<br>
	**Answer:** Highlight build system strategies, conditional compilation, and testing across environments like Windows, Linux, and macOS.

### System Programming

346. What is system call?<br>
	**Answer:** A system call is a controlled interface for user-space programs to request kernel services like I/O or process control.
347. What is the difference between process and thread?<br>
	**Answer:** Processes have separate memory spaces and resources, while threads share a process's memory but run independently.
348. What is Inter-Process Communication (IPC)?<br>
	**Answer:** IPC encompasses mechanisms (pipes, shared memory, sockets) that allow processes to exchange data and synchronize.
349. What are sockets and how do they work?<br>
	**Answer:** Sockets are endpoints for network communication, using protocols like TCP or UDP to send and receive data across hosts.
350. What is memory-mapped I/O?<br>
	**Answer:** Memory-mapped I/O maps device registers or files into the process address space, enabling direct read/write access.
351. What is DMA (Direct Memory Access)?<br>
	**Answer:** DMA allows peripherals to transfer data directly to memory without CPU intervention, improving throughput.
352. What is endianness (big-endian vs little-endian)?<br>
	**Answer:** Endianness defines byte order of multi-byte values; big-endian stores most significant byte first, little-endian stores least significant first.
353. What is alignment and why does it matter in embedded systems?<br>
	**Answer:** Alignment ensures data is accessed on boundary-friendly addresses, impacting performance and correctness on strict architectures.
354. What is a page fault?<br>
	**Answer:** A page fault occurs when a program accesses a page not in physical memory, prompting the OS to fetch or allocate it.
355. What is virtual memory?<br>
	**Answer:** Virtual memory abstracts physical memory, providing each process with a large address space and supporting isolation and paging.

### Standards & Compatibility

356. What are the differences between C++98, C++03, C++11, C++14, C++17, C++20?<br>
	**Answer:** C++98/03 established templates and STL; C++11 introduced modern features; C++14 refined them; C++17 added structured bindings, parallel algorithms; C++20 delivered concepts, ranges, coroutines, and modules.
357. What is backward compatibility in C++?<br>
	**Answer:** Backward compatibility ensures older code continues to compile and run under newer standards, subject to deprecations and corner-case changes.
358. What is the difference between compiler extensions and standard C++?<br>
	**Answer:** Extensions add non-standard features that may hinder portability; standard C++ features are portable across conforming compilers.
359. How do you write portable C++ code?<br>
	**Answer:** Stick to standard features, avoid undefined behavior, use feature test macros, and test across compilers and platforms.
360. What is the impact of different compiler implementations?<br>
	**Answer:** Compilers differ in diagnostics, optimization, supported extensions, and implementation-defined behaviors, affecting portability.
361. What are platform-specific differences you need to consider?<br>
	**Answer:** Differences include endianness, word size, ABI, filesystem semantics, threading models, and available libraries.
362. What is the role of the C++ Standards Committee?<br>
	**Answer:** WG21 develops and maintains the C++ standard, drafting new features and resolving defects.
363. What are Technical Specifications in C++?<br>
	**Answer:** Technical Specifications (TS) are provisional documents for experimental features that may be integrated into future standards.
364. How do you handle deprecated features?<br>
	**Answer:** Monitor compiler warnings, refactor to recommended alternatives, and use feature macros or conditional compilation during migration.
365. What is the difference between hosted and freestanding implementations?<br>
	**Answer:** Hosted implementations provide the full standard library; freestanding implementations target embedded environments with limited library support.

### Final Advanced Questions

366. Explain the memory model and happens-before relationships.<br>
	**Answer:** The memory model defines ordering and visibility rules; a happens-before relationship guarantees that writes become visible to subsequent reads in other threads.
367. What is the difference between sequential consistency and relaxed atomics?<br>
	**Answer:** Sequential consistency imposes a single global order of operations, while relaxed atomics provide atomicity without ordering guarantees.
368. How do you implement lock-free data structures?<br>
	**Answer:** Use atomic operations, compare-and-swap loops, hazard pointers, and careful memory ordering to avoid locks while ensuring progress.
369. What is the ABA problem in lock-free programming?<br>
	**Answer:** ABA occurs when a value changes from A to B back to A, making a CAS appear successful despite intermediate modifications.
370. What are transactional memory concepts?<br>
	**Answer:** Transactional memory executes blocks atomically, rolling back on conflicts; C++ has experimental support through TS libraries or hardware features.
371. How do you optimize for cache-line alignment?<br>
	**Answer:** Align data structures using `alignas` or allocator strategies so frequently accessed data fits within cache lines to reduce misses.
372. What is false sharing and how do you avoid it?<br>
	**Answer:** False sharing happens when threads modify different data sharing a cache line; avoid it by padding or aligning data to separate cache lines.
373. Explain the difference between strong and weak memory ordering.<br>
	**Answer:** Strong ordering (seq_cst) enforces global order, while weak ordering allows more reordering but requires explicit fences for synchronization.
374. What is the cost of context switching?<br>
	**Answer:** Context switching saves/restores thread state and flushes caches, incurring latency; minimizing unnecessary switches improves performance.
375. How do you profile and optimize multicore applications?<br>
	**Answer:** Use parallel profilers, analyze contention, ensure load balancing, and reduce synchronization bottlenecks.
376. What are SIMD instructions and how do you use them in C++?<br>
	**Answer:** SIMD processes multiple data elements per instruction; use compiler intrinsics, vector libraries, or `std::experimental::simd`.
377. What is the difference between hot path and cold path optimization?<br>
	**Answer:** Hot paths are frequently executed and need aggressive optimization; cold paths run rarely and can prioritize readability or size.
378. How do you handle C++ exceptions in a real-time system?<br>
	**Answer:** Many real-time systems avoid exceptions due to unpredictable latency, using error codes or carefully bounded exception handling.
379. What are the trade-offs between different container types?<br>
	**Answer:** Trade-offs involve memory footprint, iteration speed, insertion/removal complexity, and cache behavior; choose based on workload.
380. How do you design for testability in C++?<br>
	**Answer:** Use dependency injection, small cohesive classes, clear interfaces, and separate side effects to facilitate unit testing.
381. What is the Pimpl idiom and when should you use it?<br>
	**Answer:** Pimpl hides implementation details to reduce rebuilds, preserve ABI, and encapsulate private members; use it for stable public headers.
382. How do you manage dependencies in large C++ projects?<br>
	**Answer:** Employ build systems like CMake, use package managers, modularize code, and enforce layering or interface boundaries.
383. What are the challenges of C++ in embedded systems?<br>
	**Answer:** Challenges include limited memory, lack of standard library features, real-time constraints, and hardware-specific integration.
384. How do you handle versioning in C++ libraries?<br>
	**Answer:** Follow semantic versioning, maintain ABI compatibility, provide inline namespaces for versions, and document breaking changes.
385. What is your approach to API design in C++?<br>
	**Answer:** Favor clear, minimal interfaces, const-correctness, RAII semantics, and consistent error handling strategies.
386. How do you optimize compile times in large C++ projects?<br>
	**Answer:** Use precompiled headers, modules, unity builds, forward declarations, and avoid unnecessary header inclusion.
387. What is the impact of inlining on code size and performance?<br>
	**Answer:** Inlining reduces call overhead but can increase code size, potentially hurting instruction cache behavior; balance based on profiling.
388. How do you balance type safety and performance?<br>
	**Answer:** Prefer strong typing but measure and replace only critical hotspots with lower-level constructs, documenting trade-offs.
389. What are the considerations for exception safety in generic code?<br>
	**Answer:** Ensure templates provide at least basic guarantees, document requirements on operations, and design interfaces that support strong guarantees when possible.
390. How do you design for extensibility in C++?<br>
	**Answer:** Use abstract interfaces, policy templates, and composition to allow new functionality without modifying existing code.
391. What is your experience with C++ build systems (CMake, Make, etc.)?<br>
	**Answer:** Discuss practical experience configuring projects, handling dependencies, and integrating testing or packaging workflows.
392. How do you handle platform-specific code in cross-platform projects?<br>
	**Answer:** Isolate platform-dependent logic behind abstractions, use conditional compilation, and maintain per-platform build configurations.
393. What are the considerations for ABI compatibility?<br>
	**Answer:** ABI stability requires avoiding changes to class layout, virtual tables, inline implementations, and symbol visibility between versions.
394. How do you approach memory-constrained environments?<br>
	**Answer:** Optimize data structures, reuse buffers, eliminate dynamic allocation, and carefully track memory usage.
395. What is your experience with C++ static analysis tools?<br>
	**Answer:** Highlight usage of tools like clang-tidy, Coverity, or SonarQube to enforce coding standards and detect defects.
396. How do you handle undefined behavior in production code?<br>
	**Answer:** Avoid by adhering to standards, leveraging sanitizers during testing, and enforcing defensive programming practices.
397. What are the trade-offs between compile-time and runtime polymorphism?<br>
	**Answer:** Compile-time polymorphism offers zero runtime overhead but increases template complexity; runtime polymorphism is flexible but costs virtual dispatch.
398. How do you optimize for both latency and throughput?<br>
	**Answer:** Balance by reducing critical path length, batching work where acceptable, and employing concurrency or pipelining strategies.
399. What is your approach to error handling in C++?<br>
	**Answer:** Use exceptions for exceptional conditions, error codes for expected results, and maintain consistent policies documented for API users.
400. How do you mentor others on C++ best practices?<br>
	**Answer:** Provide code reviews, share resources, pair program, and curate guidelines that emphasize readability, safety, and performance.

---

**Total: 400 questions spanning fundamentals, tooling, and advanced real-world C++.**
