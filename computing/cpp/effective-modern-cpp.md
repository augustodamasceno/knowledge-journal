# Notes for S. Meyers' Effective Modern C++  

# Attribution

> The content in this file is entirely human-made.  

# Introduction

## Terminology  
| Term I Use | Language Versions I Mean |
|---|---|
| C++ | All |
| C++98 | C++98 and C++03 |
| C++11 | C++11 and C++14 |
| C++14 | C++14 |

## You can take the expression address?
> Yes: probably is lvalue  
> No: probably is rvalue  

## Parameters are lvalue  

## Widget:  arbitrary user-defined type

## rhs (right-hand side) and lhs (left-hand side)
```cpp
Matrix operator+(const Matrix& lhs, const Matrix& rhs);
```

## ... means other code could go here

## copy: object initialized with other object of the same type (no terminology in C++ to distinguish between copy-constructed and move-constructed)  

## Function objects created through lambda expressions are known as closures  

## function templates (templates that generate functions) and template functions (the functions generated from function templates). Ditto for class templates and template classes. 

## Declaration and definition
```cpp
bool func(const Widget& w); // Declaration

bool func(const Widget& w) // Definition
{ return w.size() < 10; }
```

## Signature in the book is just parameters and return
> The official definition of signature sometimes omits return types.
```cpp
// Signature from 
// bool func(const Widget& w)
// { return w.size() < 10; }
bool(const Widget&)
```

## ⚠️ Avoid deprecates, they are on standardization death row.  

## “constructor” is ctor and “destructor” is dtor.

## Reporting bugs and suggesting improvements: emc++@aristeia.com 

## Errata: http://www.aristeia.com/BookErrata/emc++-errata.html.

# 1. Deducing Types  

## 1.1 Intro

* C++98: function templates  
* C++11: add auto and decltype  
* C++14: extends usage contexts for auto and decltype  
* Fore compilers to make the results of their type deductions visible  

## 1.2 Item 1: Understand template type deduction  

* ParamType cases:    
  * 1: pointer or reference and not universal reference  
    * if expr type is reference, ignore the reference part then pattern-match expr type agains ParamType to determine T  
    * the constness of the object becomes part of the type deducted for T  
    * then reference-ness is ignored during type deduction  
    * **errata for page 12, third paragraph**:
    >  The third paragraph (beginning with "These examples all
    >  show lvalue reference  parameters, but type deduction
    >  works exactly the same way for rvalue reference
    >  parameters") should be removed. When the type of param
    >  in the template f on page 11 is changed to an rvalue
    >  reference (i.e., to have type "T&&"), it becomes a
    >  universal reference, and then the rules for Case 2
    >  (on pages 13-14) apply.
    * From 
    ```cpp
    template<typename T>
    void f(T& param);
    ``` 
    to
    ```cpp
    template<typename T>
    void f(const T& param);
    ``` 
    there's no longer a need for const to be deduced as part of T because it's assuming that param is a reference-to-cost. Same thing if param is a pointer:
    ```cpp
    template<typename T>
    void f(T* param);
    ```
    If param is a const int *, T is const int because  it's assuming that param is a pointer.
  * 2: universal reference    
  * 3: neither pointer nor reference  





