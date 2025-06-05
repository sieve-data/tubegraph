---
title: Objectoriented programming in C
videoId: MNeX4EGtR5Y
---

From: [[fireship]] <br/> 

C++ is a statically typed, compiled programming language known for its widespread use in software infrastructure, though it is also infamous for its steep learning curve <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>.

## History and Design
C++ was created in 1979 by Bjarne Stroustrup at AT&T Bell Labs <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. Stroustrup was inspired by the [[Objectoriented programming in Java | object-oriented]] nature of Simula but needed a language with the high performance characteristics of [[C language characteristics and usage | C]] <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. This led to the birth of "C with classes" <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>.

C++ is designed as a superset of [[C language characteristics and usage | C]], meaning that virtually any [[C language characteristics and usage | C]] program is also a valid C++ program <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>. It adds zero-overhead abstractions, including [[Objectoriented programming in Java | object-oriented patterns]] like polymorphism, encapsulation, and inheritance <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.

### Key Characteristics
C++ is popular because it provides low-level [[Memory management in C | memory]] and hardware control, similar to [[C language characteristics and usage | C]], but also offers high-level abstractions such as classes and smart pointers <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.

> "C++ makes it harder to shoot yourself in the foot but when you do it'll blow your whole leg off." <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>

## Applications and Usage
Today, C++ is utilized in a wide variety of systems with constrained [[Memory management in C | memory]] demands <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. Examples include:
*   Unreal Engine for AAA video games <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>
*   Programs like Adobe After Effects <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>
*   Databases such as MySQL and MongoDB <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>
*   Embedded systems, like the display on a smart toaster <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>
*   Implementation of low-level infrastructure, including language compilers and virtual machines <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>

## Getting Started with C++
To begin programming in C++, you need to install a C++ compiler like GCC or Clang++ <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.
*   **File Extension**: C++ source files typically end in `.cpp` <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>.
*   **Input/Output**: Include `iostream` from the standard library to handle input and output operations <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.
*   **Execution**: Code execution starts from the `main` function <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>.
*   **Hello World**: To print "Hello World", use `std::cout` followed by the bit-wise shift-left operator (`<<`) and a string literal <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. The `std::` prefix can be omitted by adding `using namespace std;` at the top of the file <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>.
*   **Strings**: String variables can be defined as an array of characters, or by including the `<string>` header from the standard library, you can use the `std::string` type <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.

## Object-Oriented Programming (OOP) in C++
The significant advantage of C++ is its support for [[Objectoriented programming in Java | object-oriented programming]] with classes <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.

### Classes and Objects
*   **Classes**: A class serves as a blueprint for an object <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.
*   **Attributes and Methods**: Inside a class, you can define attributes (data members) and methods (member functions) <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>.
    *   By default, members are private. They can be made public by adding them under the `public:` specifier <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.
    *   Methods can also be defined outside the class definition using a double colon (`::`) <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.
*   **Overloading**: Methods can be defined multiple times with different parameters, a concept known as overloading, which is a form of polymorphism <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.
*   **Constructors and Destructors**: These special methods run code when an object is created (constructor) or destroyed (destructor) <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.
*   **Inheritance**: Classes support inheritance, allowing developers to efficiently share logic throughout a program <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.
*   **Instantiation**: To create an object, type the class name followed by the object's name and, optionally, any parameters for the constructor <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.

### Memory Management
While C++ allows manual [[Memory management in C | memory]] management with pointers and references, tools like `std::unique_ptr` can simplify and secure the process by ensuring that only one object can be allocated to [[Memory management in C | memory]] at a time <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.

## Compiling and Running
To run your C++ code, open a terminal and use a tool like Clang++ to compile it <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.