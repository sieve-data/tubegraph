---
title: Applications and usage of C
videoId: MNeX4EGtR5Y
---

From: [[fireship]] <br/> 

C++ is a statically typed, compiled programming language known for its extensive use in software infrastructure <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. While it has a reputation for a steep learning curve <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>, its design provides a unique balance of low-level control and high-level abstractions.

## History and Design Philosophy
Created in 1979 by Bjarne Stroustrup at AT&T Bell Labs, C++ (originally "C with classes") was inspired by the object-oriented nature of Simula <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. Stroustrup aimed to combine the high performance of [[c_language_characteristics_and_usage | C]] with object-oriented capabilities <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>.

C++ is designed as a superset of [[key_features_of_c | C]], meaning most [[c_language_characteristics_and_usage | C]] programs are valid C++ programs <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>. It adds "zero overhead abstractions" such as [[objectoriented_programming_in_c | object-oriented patterns]] like polymorphism, encapsulation, and inheritance <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.

## Key Characteristics and Advantages
C++'s popularity stems from its ability to provide [[key_features_of_c | low-level memory and hardware control]] similar to [[c_language_characteristics_and_usage | C]], combined with high-level abstractions like classes and smart pointers <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. This combination makes it powerful for systems requiring both performance and complex software design.

## Widespread Applications
Today, C++ is utilized in a diverse range of systems, particularly those with constrained memory demands <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>:
*   **Video Games**: Used in engines like Unreal Engine for AAA video games <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.
*   **Creative Software**: Programs such as Adobe After Effects <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.
*   **Databases**: Powers systems like MySQL and MongoDB <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.
*   **Embedded Systems**: Found in devices like smart toasters <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.
*   **Low-Level Infrastructure**: Used to implement language compilers and virtual machines <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.

## Programming Concepts and Usage
When [[getting_started_with_c_programming | programming in C++]], several fundamental concepts are central to its usage:

### Object-Oriented Programming (OOP)
A significant feature of C++ is its support for [[objectoriented_programming_in_c | object-oriented programming]] with classes <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.
*   **Classes**: A class serves as a blueprint for an object <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.
*   **Attributes and Methods**: Inside a class, you can define attributes and methods, which are private by default but can be made public using the `public` specifier <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>. Methods can also be defined outside the class using a double colon `::` <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.
*   **Overloading**: Methods can be defined multiple times with different parameters, a concept known as overloading, which is a form of polymorphism <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.
*   **Constructors and Destructors**: These are special methods that run code when an object is created or destroyed, respectively <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.
*   **Inheritance**: Classes support inheritance, allowing developers to efficiently share logic throughout a program <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.

To create an object, you type the class name followed by the object's name and any optional constructor parameters <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.

### Memory Management
While C++ allows manual memory management with pointers and references, tools like `unique_pointer` provide a safer and easier way to manage memory by ensuring only one object is allocated to memory at a time <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.

## Getting Started
To begin [[getting_started_with_c_programming | programming in C++]], you first need to install a C++ compiler such as GCC or Clang <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>. C++ source files typically end with the `.cpp` extension <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>.

Basic code structure involves:
*   Including `iostream` from the standard library for input and output operations <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.
*   Code execution starting from the `main` function <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>.
*   Using `std::cout` and the bitwise shift left operator `<<` to print output <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. The `std::` prefix can be avoided by adding a `using namespace std;` declaration <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>.
*   String variables can be declared as an array of characters, or more conveniently by including the `string` header from the standard library to use the `string` type <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.

To compile and run C++ code, you open a terminal and use a tool like `clang++` <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.