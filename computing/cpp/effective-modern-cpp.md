# Notes for S. Meyers' Effective Modern C++  

# Content Declaration

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
```c++
bool func(const Widget& w); // Declaration

bool func(const Widget& w) // Definition
{ return w.size() < 10; }
```

## Signature in the book is just parameters and return
> The official definition of signature sometimes omits return types.
```c++
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

* 