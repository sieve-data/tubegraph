---
title: Objectoriented programming and inheritance
videoId: uTxRF5ag27A
---

From: [[lexfridman]] <br/> 

Object-oriented programming (OOP) is a foundational concept in the field of computer science that organizes software design around data, or objects, rather than functions and logic. OOP allows for the creation of software that models real-world entities using objects, which are instances of classes. A class defines the properties and behaviors of its objects, encapsulating data and functions into a single entity.

## Origins and Concepts

The origins of OOP can be traced back to the programming language Simula, which was primarily designed for simulation. Simula stands out for inventing object-oriented programming and introducing key features such as inheritance and runtime polymorphism <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>. These features allowed for a modular approach to programming, where the complexity of a program can grow linearly with the size of the program rather than exponentially <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.

## Inheritance in OOP

Inheritance is a core principle of OOP and is essential for establishing a hierarchical relationship between classes. Inheritance allows one class (the subclass or derived class) to inherit the properties and methods from another class (the superclass or base class). This feature supports code reuse and can simplify the maintenance and modification of code.

For example, in a class hierarchy of vehicles, a `vehicle` class may have general methods such as `turn()` or `accelerate()` <a class="yt-timestamp" data-t="00:12:11">[00:12:11]</a>. Subclasses such as `bicycle`, `car`, and `fire engine` can inherit these general functionalities while implementing their device-specific behavior <a class="yt-timestamp" data-t="00:12:12">[00:12:12]</a>.

## Key Features of Inheritance

### Reusability

Inheritance promotes code reusability by allowing new classes to use the properties and behaviors of existing classes. Developers do not have to write code from scratch for every class. Instead, they can build upon existing, tested classes, improving efficiency and consistency <a class="yt-timestamp" data-t="01:01:12">[01:01:12]</a>.

### Extensibility

Classes derived from a base class can extend or override existing methods to provide specific implementations. This extensibility supports the development of specialized classes that maintain the foundational behavior of the superclass while allowing for unique functionalities.

### Hierarchical Classification

With inheritance, a hierarchical classification of classes is established, better organizing complex systems and reflecting real-world relationships. Classes can be structured to form a commonly understood hierarchy that makes the system more intuitive for stakeholders to understand.

## Implementation in C++

C++, created by [[Programming languages and their evolution | Bjarne Stroustrup]], borrows heavily from Simula to implement OOP with classes. C++ supports and expands on OOP principles like inheritance, allowing for virtual functions and other mechanisms to maintain efficient and robust code execution <a class="yt-timestamp" data-t="01:01:06">[01:01:06]</a>. 

The design philosophy of C++ is centered around abstraction and efficiency. When designing C++, Stroustrup emphasized the zero-overhead principle, ensuring that abstractions such as inheritance do not incur performance penalties <a class="yt-timestamp" data-t="00:45:01">[00:45:01]</a>.

### Compiler Optimizations

C++ compilers, such as those from the [[Programming languages and coding philosophies | GCC or Clang]], are designed to optimize the machine code generated from C++ source code. These optimizations enable features like inheritance and runtime polymorphism to perform efficiently without sacrificing the abstractions' usability, thus adhering to the zero-overhead principle <a class="yt-timestamp" data-t="01:02:00">[01:02:00]</a>.

## Conclusion

Object-oriented programming and inheritance are essential for modern software development, allowing developers to create complex, modular, and maintainable systems. In languages like C++, these features are implemented with a focus on performance and abstraction, enabling the development of efficient and dependable applications that drive the technology of today's world.