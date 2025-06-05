---
title: Key features of C
videoId: MNeX4EGtR5Y
---

From: [[fireship]] <br/> 

C++ is a statically typed, compiled programming language <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. It is widely used in software infrastructure <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>, though it is also known for its steep learning curve <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>.

## Origins and Design Principles

C++ was created in 1979 by Bjarne Stroustrup at AT&T Bell Labs <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. Stroustrup was inspired by the object-oriented nature of Simula but sought a language with the high performance of [[c_language_characteristics_and_usage | C]] <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. This led to the birth of "C with Classes," which evolved into C++ <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.

It is designed as a superset of [[c_language_characteristics_and_usage | C]], meaning nearly any [[c_language_characteristics_and_usage | C]] program is a valid C++ program <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>. C++ introduces zero-overhead abstractions, including object-oriented patterns <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.

## Core Features

C++ offers a combination of low-level control and high-level abstractions:
*   **Low-level Control** C++ provides direct control over memory and hardware, similar to [[c_language_characteristics_and_usage | C]] <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.
*   **High-level Abstractions** It includes features like classes and smart pointers <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>. These abstractions aim to make development safer and more efficient than in pure [[c_language_characteristics_and_usage | C]], although errors can still be severe <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.
*   **Object-Oriented Programming (OOP)** A major differentiating feature is its robust support for OOP through classes <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.
    *   **Classes** Serve as blueprints for creating objects <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>. They can define attributes and methods, which are private by default, but can be made public using the `public` specifier <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>. Methods can also be defined outside the class definition using the double colon `::` operator <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.
    *   **Polymorphism** Supported through method overloading, where methods can be defined multiple times with different parameters <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.
    *   **Encapsulation** Achieved by bundling data (attributes) and methods that operate on the data within a class, controlling access levels (e.g., public, private) <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.
    *   **Inheritance** Classes support inheritance, allowing developers to share logic more efficiently throughout a program <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.
    *   **Constructors and Destructors** These special methods run when an object is created or destroyed, respectively <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.
*   **Memory Management** While manual memory management with pointers and references is possible, tools like `unique_pointer` provide safer and easier alternatives by ensuring only one object can be allocated to memory at a time <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.

## Applications

C++ is utilized in a diverse range of systems, particularly those with constrained memory demands <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. Examples include:
*   AAA video games (e.g., Unreal Engine) <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>
*   Professional software (e.g., Adobe After Effects) <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>
*   Databases (e.g., MySQL, MongoDB) <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>
*   Embedded systems (e.g., smart toaster displays) <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>
*   Low-level infrastructure like language compilers and virtual machines <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>

## Getting Started

To begin programming in C++:
1.  **Install a Compiler** Install a C++ compiler such as GCC or Clang <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.
2.  **Create a File** Create a file ending with the `.cpp` extension <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>.
3.  **Include Libraries** Include `iostream` from the standard library to handle input and output operations <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>. For string manipulation, `string` can be included to use the `std::string` type <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.
4.  **Main Function** Code execution begins from the `main` function <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>.
5.  **Output** Use `std::cout` followed by the bitwise shift left operator (`<<`) and a string literal to print output (e.g., `std::cout << "Hello World";`) <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. The `std::` prefix can be avoided by adding `using namespace std;` at the top of the file <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>.
6.  **Compile** Compile the code using a tool like `clang++` in the terminal <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.