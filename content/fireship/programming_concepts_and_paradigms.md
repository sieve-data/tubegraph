---
title: Programming Concepts and Paradigms
videoId: -uleG_Vecis
---

From: [[fireship]] <br/> 

## Introduction to Programming

Software engineering offers high-paying jobs even with limited understanding of underlying computer mechanics <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. A programming language serves as a tool that employs the abstraction principle to make computers practical for humans to work with <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>, simplifying systems layer by layer <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.

### Language Execution Models

Programming languages primarily fall into two categories based on how their code is executed:

*   **Interpreted Languages**: Some languages, like Python, are interpreted <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>. An interpreter program executes each line of code one by one <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.
*   **Compiled Languages**: Other languages, such as C++, are compiled <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>. They use a compiler to convert the entire program into machine code in advance <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>. This process results in an executable file that can be run by the operating system without additional dependencies <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.

## Core Programming Concepts

### Data Types and Variables

Every programming language includes various built-in [[Data Structures and Algorithms | data types]] to represent information in human-friendly formats, such as characters and numbers, instead of raw bytes <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>.

The most fundamental way to use data in an application is by declaring a variable <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>. This associates a name with a data point, enabling its reuse within the code <a class="yt-timestamp" data-t="00:03:29">[00:03:29]</a>.

*   **Dynamically Typed Languages**: Languages like Python are dynamically typed <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>, meaning the program automatically infers the data type assigned to a variable <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>.
*   **Statically Typed Languages**: Languages like C are statically typed <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>, requiring the developer to explicitly specify the data type of a variable when defining it <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>.

Common data types found in most programming languages include:
*   **`int`**: Represents whole numbers, which can be signed (allowing negative numbers) or unsigned <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.
*   **`float` / `double`**: Used for numbers requiring a decimal point <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>. `float` uses a limited memory space to represent a range of numbers with certain precision, similar to scientific notation <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>. `double` doubles the memory used for the number, providing greater range or precision <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.
*   **`char`**: Represents a single character <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>.
*   **`string`**: Represents multiple characters together <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>.
*   **`boolean`**: Represents true or false values <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a>.

### Memory Management

When a variable is defined, its value is stored in hardware memory <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>. Developers may need to allocate and free up memory during program execution <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.

*   **Pointers**: A pointer is a variable whose value is the memory address of another variable <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>, used for low-level memory control <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>.
*   **Garbage Collector**: Many languages avoid low-level memory management by implementing a garbage collector <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>. This system automatically allocates and de-allocates memory when an object is no longer referenced in the program <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.
*   **Call Stack**: When a function is called, the programming language places it into memory on the call stack <a class="yt-timestamp" data-t="00:08:13">[00:08:13]</a>, a short-term memory chunk for executing code <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>. If a function recursively calls itself indefinitely, it can lead to a stack overflow error <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>.
*   **Heap**: For long-lived data, most languages use a separate memory area called the heap <a class="yt-timestamp" data-t="00:10:55">[00:10:55]</a>. Unlike the call stack, the heap can grow and shrink dynamically <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>. It allows objects to be passed by reference, meaning multiple variables can point to the same object in the heap without increasing memory footprint <a class="yt-timestamp" data-t="00:11:05">[00:11:05]</a>.

### Control Flow

*   **Expressions**: When code produces a value, it's known as an expression <a class="yt-timestamp" data-t="00:07:19">[00:07:19]</a>.
*   **Statements**: Code that simply performs an action without producing a value is a statement <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>.
    *   **If Statement**: Handles conditional logic; if a condition is true, specific code executes, otherwise an `else` block may run <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.
    *   **Loop**: A common type of statement that repeatedly executes a block of code <a class="yt-timestamp" data-t="00:07:38">[00:07:38]</a>.
        *   **While Loop**: Runs repeatedly until a condition becomes false <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>.
        *   **For Loop**: Iterates over an iterable [[Data Structures and Algorithms | data type]], such as an array, executing code for each item <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>.

### Functions

A function is a block of code that takes an input, performs an action, and returns an output <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>. Like variables, functions have a name and can be called from other parts of the code with different input parameters, known as arguments <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>. Some functions may not have an output, often called void functions <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>.

*   **Recursion**: An interesting property of functions is that they can call themselves, a concept known as recursion <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>. Without a base condition, recursive functions can lead to infinite loops and stack overflow errors <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>.

## Algorithms and Performance

An [[problemsolving_and_coding_practice | algorithm]] is code designed to solve a specific problem <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>.

*   **Big-O Notation**: Used to evaluate the efficiency of an [[problemsolving_and_coding_practice | algorithm]] <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a>. It's a standard format for approximating the performance of an [[problemsolving_and_coding_practice | algorithm]] at scale <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>.
    *   **Time Complexity**: Refers to how fast an [[problemsolving_and_coding_practice | algorithm]] will run <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>.
    *   **Space Complexity**: Deals with the amount of memory required to run an [[problemsolving_and_coding_practice | algorithm]] <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>.

Common types of [[problemsolving_and_coding_practice | algorithms]] include:
*   **Brute Force**: Involves looping over every possible combination to find a solution <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>.
*   **Divide and Conquer**: Breaks a problem into smaller sub-problems, often by halving it repeatedly, such as in binary search <a class="yt-timestamp" data-t="00:08:58">[00:08:58]</a>.
*   **Dynamic Programming**: Deconstructs a problem into multiple smaller sub-problems, storing the result of each computation for later use via memoization <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>. Memoization reuses existing computed values instead of recomputing them from scratch <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>.
*   **Greedy Algorithms**: Make the most beneficial choice in the short term without considering the overall problem <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>. Dijkstra's shortest path algorithm is an example <a class="yt-timestamp" data-t="00:09:28">[00:09:28]</a>.
*   **Backtracking Algorithms**: Adopt an incremental approach by exploring all possible options, similar to navigating a maze <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a>.

## [[phps_programming_paradigms_and_features | Programming Paradigms]]

When implementing code, there are multiple approaches to achieving a solution <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>.

*   **Declarative Programming**: Code describes *what* the program does and its desired outcome, without specifying control flow <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>. This style is often associated with functional languages like Haskell <a class="yt-timestamp" data-t="00:09:53">[00:09:53]</a>.
*   **Imperative Programming**: Code uses statements (like `if` and `while`) to provide explicit instructions on *how* to produce an outcome <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>. This is associated with procedural languages like C <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>.
*   **Multi-Paradigm Languages**: Most modern general-purpose languages, including Python, JavaScript, Kotlin, and Swift, are multi-paradigm <a class="yt-timestamp" data-t="00:10:06">[00:10:06]</a>, supporting various programming styles simultaneously <a class="yt-timestamp" data-t="00:10:13">[00:10:13]</a>.

### [[objectoriented_programming_in_c | Object-Oriented Programming]] (OOP)

[[objectoriented_programming_in_c | Object-Oriented Programming]] (OOP) is a paradigm centered around the concept of classes, which serve as blueprints for data or objects <a class="yt-timestamp" data-t="00:10:16">[00:10:16]</a>.

*   **Classes**: A class can encapsulate variables (commonly called properties) and functions (usually called methods) <a class="yt-timestamp" data-t="00:10:22">[00:10:22]</a>. OOP provides a common way to organize and reuse code <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>.
*   **Inheritance**: Classes can share behaviors through inheritance, where a subclass can extend and override the behaviors of a parent class <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a>. This concept opens the door to various [[software_design_patterns | design patterns]] <a class="yt-timestamp" data-t="00:10:39">[00:10:39]</a>.
*   **Objects**: A class itself doesn't perform actions; instead, it is used to instantiate objects <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>, which are actual chunks of data residing in the computer's memory <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>.

## Advanced Concepts

### Concurrency and Parallelism

The CPU contains multiple threads, which break a physical CPU core into virtual cores to run code simultaneously <a class="yt-timestamp" data-t="00:11:15">[00:11:15]</a>.

*   **Parallelism**: Some programming languages support parallelism, allowing code to literally execute on two different threads at the same time <a class="yt-timestamp" data-t="00:11:27">[00:11:27]</a>.
*   **Concurrency**: Many languages are single-threaded but can still handle multiple jobs by implementing concurrency models <a class="yt-timestamp" data-t="00:11:34">[00:11:34]</a>. These models, such as event loops or co-routines, can pause or delay normal code execution to manage multiple tasks on a single thread simultaneously <a class="yt-timestamp" data-t="00:11:40">[00:11:40]</a>.