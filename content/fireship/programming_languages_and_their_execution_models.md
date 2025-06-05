---
title: Programming languages and their execution models
videoId: -uleG_Vecis
---

From: [[fireship]] <br/> 

A programming language is a tool that uses the abstraction principle to simplify working with computers for humans, simplifying different systems layer by layer <a class="yt-timestamp" data-t="02:44:00">[02:44:00]</a>. It allows developers to write code that will eventually be converted into machine code, a binary format that the CPU can decode and execute <a class="yt-timestamp" data-t="01:37:00">[01:37:00]</a>.

## Execution Models

Programming languages utilize different execution models to run code:

### Interpreted Languages
An interpreted language has a program called an interpreter that executes each line of code one by one <a class="yt-timestamp" data-t="02:54:00">[02:54:00]</a>.
*   **Example**: [[popular_dynamic_and_highlevel_programming_languages | Python]] <a class="yt-timestamp" data-t="02:54:00">[02:54:00]</a>.

### Compiled Languages
Compiled languages use a compiler to convert the entire program into machine code in advance, before the CPU attempts to execute it <a class="yt-timestamp" data-t="03:01:00">[03:01:00]</a>. This process results in an executable file that can be run by the operating system without any extra dependencies <a class="yt-timestamp" data-t="03:08:00">[03:08:00]</a>.
*   **Example**: [[lowlevel_systems_programming_languages | C++]] <a class="yt-timestamp" data-t="03:01:00">[03:01:00]</a>.

## Language Characteristics

### Data Types and Variables
Every programming language has a variety of built-in data types to represent data <a class="yt-timestamp" data-t="03:14:00">[03:14:00]</a>. Instead of raw bytes, languages work with human-friendly concepts like characters and numbers <a class="yt-timestamp" data-t="03:20:00">[03:20:00]</a>.

Common data types include:
*   **Int**: Represents whole numbers, which can be signed (to include negative numbers) or unsigned <a class="yt-timestamp" data-t="04:22:00">[04:22:00]</a>.
*   **Floating Point (Float/Double)**: Used for numbers requiring a decimal point <a class="yt-timestamp" data-t="04:30:00">[04:30:00]</a>. It uses a form of scientific notation to represent a certain range of numbers at a specific precision due to memory limitations <a class="yt-timestamp" data-t="04:34:00">[04:34:00]</a>. A "double" type doubles the memory used for the number, providing more range or precision <a class="yt-timestamp" data-t="04:43:00">[04:43:00]</a>.
*   **Char**: Represents a single character <a class="yt-timestamp" data-t="04:48:00">[04:48:00]</a>.
*   **String**: Represents multiple characters together <a class="yt-timestamp" data-t="04:53:00">[04:53:00]</a>. Characters are mapped to binary values using character encodings like ASCII or UTF-8 <a class="yt-timestamp" data-t="01:11:00">[01:11:00]</a>.
*   **Boolean**: Represents `true` or `false` values, typically resulting from comparisons <a class="yt-timestamp" data-t="07:15:00">[07:15:00]</a>.

Variables are the most fundamental way to use data, attaching a name to a data point, allowing it to be reused in code <a class="yt-timestamp" data-t="03:25:00">[03:25:00]</a>.
*   **Dynamically Typed Languages**: Do not require explicitly telling the program which data type is assigned to a variable; it figures it out automatically <a class="yt-timestamp" data-t="03:34:00">[03:34:00]</a>. [[popular_dynamic_and_highlevel_programming_languages | Python]] is an example <a class="yt-timestamp" data-t="03:34:00">[03:34:00]</a>.
*   **Statically Typed Languages**: Require specifying the data type of a variable in the code when it's defined <a class="yt-timestamp" data-t="03:42:00">[03:42:00]</a>. [[lowlevel_systems_programming_languages | C]] is an example <a class="yt-timestamp" data-t="03:42:00">[03:42:00]</a>.

### Memory Management
When a variable is defined, its value is stored somewhere in memory on the hardware <a class="yt-timestamp" data-t="03:48:00">[03:48:00]</a>.

*   **Pointers**: A variable whose value is the memory address of another variable, used for low-level memory control <a class="yt-timestamp" data-t="03:55:00">[03:55:00]</a>.
*   **Garbage Collector**: Many languages implement a garbage collector to automatically allocate and de-allocate memory when an object is no longer referenced in the program, avoiding manual low-level memory management <a class="yt-timestamp" data-t="04:02:00">[04:02:00]</a>.
*   **Call Stack**: A short-term chunk of memory where the programming language puts functions when they are called <a class="yt-timestamp" data-t="08:13:00">[08:13:00]</a>.
*   **Heap**: A separate area of memory, unlike the call stack, that can grow and shrink based on how the application is used <a class="yt-timestamp" data-t="10:57:00">[10:57:00]</a>. It allows passing objects by reference, where multiple variables can point to the same object without increasing memory footprint <a class="yt-timestamp" data-t="11:05:00">[11:05:00]</a>.

### Concurrency and Parallelism
Modern CPUs contain multiple threads, which break physical CPU cores into virtual cores to run code simultaneously <a class="yt-timestamp" data-t="11:15:00">[11:15:00]</a>.
*   **Parallelism**: Some programming languages support parallelism, allowing code to literally execute on two different threads at the same time <a class="yt-timestamp" data-t="11:27:00">[11:27:00]</a>.
*   **Concurrency**: Many languages are single-threaded but implement concurrency models like an event loop or co-routines <a class="yt-timestamp" data-t="11:34:00">[11:34:00]</a>. These models can pause or delay normal code execution to handle multiple jobs on a single thread simultaneously <a class="yt-timestamp" data-t="11:44:00">[11:44:00]</a>.

## Programming Paradigms

When implementing code, there are always multiple ways to get the job done <a class="yt-timestamp" data-t="09:41:00">[09:41:00]</a>.

### Declarative Programming
In declarative programming, code describes *what* the program does and the desired outcome, without focusing on control flow <a class="yt-timestamp" data-t="09:44:00">[09:44:00]</a>.
*   This style is often associated with [[specialized_languages_and_scripting_languages | functional languages]] like Haskell <a class="yt-timestamp" data-t="09:52:00">[09:52:00]</a>.

### Imperative Programming
Imperative programming uses statements like `if` and `while` to provide explicit instructions about *how* to produce an outcome <a class="yt-timestamp" data-t="09:56:00">[09:56:00]</a>.
*   It is associated with procedural languages like [[lowlevel_systems_programming_languages | C]] <a class="yt-timestamp" data-t="10:02:00">[10:02:00]</a>.

### Multi-Paradigm Languages
Today, most general-purpose languages are multi-paradigm, supporting various programming options simultaneously <a class="yt-timestamp" data-t="10:06:00">[10:06:00]</a>.
*   **Examples**: [[popular_dynamic_and_highlevel_programming_languages | Python]], [[popular_dynamic_and_highlevel_programming_languages | JavaScript]], [[popular_dynamic_and_highlevel_programming_languages | Kotlin]], and [[popular_dynamic_and_highlevel_programming_languages | Swift]] <a class="yt-timestamp" data-t="10:08:00">[10:08:00]</a>.

### Object-Oriented Programming (OOP)
OOP is a paradigm where classes are used to write a blueprint for data or objects in the code <a class="yt-timestamp" data-t="10:16:00">[10:16:00]</a>.
*   A class can encapsulate variables (commonly called **properties**) and functions (usually called **methods**) <a class="yt-timestamp" data-t="10:22:00">[10:22:00]</a>.
*   It's a common way to organize and reuse code <a class="yt-timestamp" data-t="10:29:00">[10:29:00]</a>.
*   Classes can share behaviors through **inheritance**, where a subclass extends and overrides the parent class's behaviors <a class="yt-timestamp" data-t="10:31:00">[10:31:00]</a>. This concept opens the door to various [[behavioral_patterns_in_programming | design patterns]] <a class="yt-timestamp" data-t="10:41:00">[10:41:00]</a>.
*   A class itself does not perform actions; it is used to **instantiate objects**, which are actual chunks of data living in the computer's memory <a class="yt-timestamp" data-t="10:43:00">[10:43:00]</a>.