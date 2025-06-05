---
title: Data Structures and Algorithms
videoId: -uleG_Vecis
---

From: [[fireship]] <br/> 

When code throws an error, changing nothing and re-running it a few times is a common initial reaction before needing a computer science degree <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. Software engineering allows individuals to learn to code and secure high-paying jobs without fully understanding how everything functions <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. This article explains the underlying science behind programming concepts, particularly [[Data Structures and Algorithms | data structures]] and [[Data Structures and Algorithms | algorithms]] <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.

## Core Computer Concepts

A computer is fundamentally a piece of tape holding ones and zeros, along with a device to read and write to it <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>. This concept is known as a Turing Machine, which theoretically can compute anything <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.

At the core of modern computers is the [[Computer Architecture and Components | Central Processing Unit (CPU)]] <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>. Inside the CPU, silicon contains billions of tiny transistors, acting as microscopic on/off switches <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.
*   **Bit**: The value at one of these switches, representing the smallest piece of information a computer can use <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.
*   **Byte**: A package of eight bits, capable of representing 256 different values, such as characters typed on a keyboard <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>. Characters are mapped to binary values using character encodings like ASCII or UTF-8 <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.
*   **Binary**: A base-2 counting system using only two characters: one and zero <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>.
*   **Hexadecimal**: A base-16 format (ten numbers and six letters) often used to represent binary more readably, where a four-bit group is called a nibble <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.

When developers write code in a [[Programming Concepts and Paradigms | programming language]], it's converted into machine code, a binary format executable by the CPU <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.
*   **Random Access Memory (RAM)**: Stores data for applications, functioning like a neighborhood where each house holds a byte at a specific memory address <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>. The CPU can read and write to these addresses <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.
*   **Input/Output Devices**: Essential for computer utility; examples include keyboards and mice for input, and monitors for output <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>.
*   **Operating System Kernels**: Control hardware resources via device drivers, abstracting away the complexities of hardware integration for developers <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>.
*   **Shell**: A program wrapping the kernel, exposing the operating system to the user through a command line interface (CLI) <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>. It can connect to local or remote computers via protocols like Secure Shell (SSH) <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>.

## Programming Languages and Memory Management

[[Programming Concepts and Paradigms | Programming languages]] use the abstraction principle to simplify computer interaction for humans <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.
*   **Interpreted Languages**: Like Python, use an interpreter to execute code line by line <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.
*   **Compiled Languages**: Like C++, use a compiler to convert the entire program into machine code in advance, resulting in an executable file <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.

### Data Types and Variables
Programming languages have built-in data types to represent data, such as characters and numbers, which are more human-friendly than bytes <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.
*   **Variable**: Attaches a name to a data point, allowing its reuse in code <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.
*   **Dynamically Typed Language**: Like Python, infers the data type assigned to a variable automatically <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.
*   **Statically Typed Language**: Like C, requires explicit specification of a variable's data type when defined <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>.

### Memory Allocation
Variables are stored in memory, and developers may need to allocate and free up memory <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.
*   **Pointer**: A variable whose value is the memory address of another variable, used for low-level memory control <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.
*   **Garbage Collector**: Implemented in many languages to automatically allocate and de-allocate memory when an object is no longer referenced <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.

Common data types include:
*   **Int**: For whole numbers, which can be signed (for negative numbers) or unsigned <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.
*   **Floating Point (Float/Double)**: For numbers with decimal points, representing a range of numbers with certain precision. Double types use twice the memory for greater range/precision <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>.
*   **Char**: For a single character <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>.
*   **String**: For multiple characters together <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>.

Characters stored in memory addresses adhere to specific byte orders:
*   **Big Endian**: The most significant byte is stored at the smallest memory address <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.
*   **Little Endian**: The least significant byte is stored at the smallest memory address <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.

## Data Structures

> [!definition] Data Structure
> A way to organize data into a structured format for efficient use <a class="yt-timestamp" data-t="05:13:00">[05:13:00]</a>.

Some fundamental [[Data Structures and Algorithms | data structures]] include:
*   **Array (or List)**: Organizes multiple data points in order and maintains an integer index starting at zero <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>.
*   **Linked List**: Each item has a pointer to the next item in the sequence <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.
*   **Stack**: Follows the Last-In, First-Out (LIFO) principle, where data is popped off the top <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.
*   **Queue**: Follows the First-In, First-Out (FIFO) principle, where the first item in is the first to be processed <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>.
*   **Hash (or Map/Dictionary)**: Similar to an array but uses user-defined keys (instead of integer indices) to point to individual items, forming a collection of key-value pairs <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>. [[Lua tables and data structures]] are a good example of this concept.
*   **Trees**: Organize nodes hierarchically, allowing for faster traversal than linear structures <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>. [[Combinatorics and graph theory in algorithm design | Trees]] are a specific type of [[Combinatorics and graph theory in algorithm design | graph]].
*   **Graph**: Connects multiple nodes in an unlimited number of ways, with a node for data and an edge for the relationship between data points <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a>. [[Combinatorics and graph theory in algorithm design | Graphs]] are a fundamental concept in [[Combinatorics and graph theory in algorithm design | combinatorics and graph theory]].

## Algorithms

> [!definition] Algorithm
> Code that solves a problem <a class="yt-timestamp" data-t="06:36:00">[06:36:00]</a>.

Mechanisms for implementing [[Data Structures and Algorithms | algorithms]]:
*   **Function**: A block of code that takes an input, performs an action, and returns an output <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>. Functions have a name and can be called from other parts of the code with input parameters called arguments <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>. Some functions may not have an output and are called void functions <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>.
*   **Operators**: Built-in elements in languages (e.g., equality, greater than, less than) used to compare values <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>.
*   **Boolean**: A data type representing true or false values, often the result of comparisons <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a>.
*   **Expression**: Code that produces a value <a class="yt-timestamp" data-t="00:07:19">[00:07:19]</a>.
*   **Statement**: Code that performs an action without necessarily producing a value <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>.
    *   **If Statement**: Handles conditional logic; executes a block of code if a condition is true, otherwise it may execute an `else` block <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.
    *   **Loop**: A type of statement that runs a block of code repeatedly.
        *   **While Loop**: Runs code repeatedly until a condition becomes false <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>.
        *   **For Loop**: Runs code for every object in an iterable [[Data Structures and Algorithms | data type]] like an array <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>.
*   **Recursion**: When a function calls itself <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>. If not designed with a base condition, it can lead to an infinite loop and a stack overflow error, as each call pushes a new frame onto the call stack (a short-term memory chunk for executing code) <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>. [[Problemsolving and coding practice | Solving problems]] with recursion requires careful thought about termination.

### Algorithm Performance
To determine the efficiency of an algorithm, [[Problemsolving and coding practice | developers]] use **Big-O Notation** <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>.
> [!definition] Big-O Notation
> A standard format for approximating the performance of an algorithm at scale <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>.
It references:
*   **Time Complexity**: How fast an algorithm will run <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>.
*   **Space Complexity**: How much memory is required to run the algorithm <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>.

### Types of Algorithms
*   **Brute Force**: Involves looping over every possible combination to solve a problem <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>.
*   **Divide and Conquer**: Breaks a problem into smaller sub-problems, often by cutting the problem in half multiple times, like in [[Logarithms and logarithmic functions in algorithms | binary search]] <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>.
*   **Dynamic Programming**: Breaks a problem into smaller sub-problems, storing the result of each computation for later use using a technique called **memoization** <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>. Memoization prevents recomputing values if a function has already been called <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>.
*   **Greedy Algorithms**: Make the most beneficial choice in the short term without considering the problem as a whole <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>. Dijkstra's shortest path algorithm is an example <a class="yt-timestamp" data-t="00:09:28">[00:09:28]</a>.
*   **Backtracking Algorithms**: Take an incremental approach, exploring all possible options like a rat in a maze <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.

## Programming Paradigms

Multiple ways exist to implement code and [[Data Structures and Algorithms | algorithms]] <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>. These approaches are known as [[Programming Concepts and Paradigms | programming paradigms]]:
*   **Declarative Programming**: Code describes what the program does and its outcome, without specifying control flow <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>. This is associated with functional languages like Haskell <a class="yt-timestamp" data-t="00:09:53">[00:09:53]</a>.
*   **Imperative Programming**: Code uses statements (like `if` and `while`) to provide explicit instructions on how to produce an outcome <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>. It is associated with procedural languages like C <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>.
*   **Multi-Paradigm Languages**: Most general-purpose languages today (e.g., Python, JavaScript, Kotlin, Swift) support multiple paradigms simultaneously <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>.

### Object-Oriented Programming (OOP)
> [!definition] Object-Oriented Programming (OOP)
> A paradigm where classes are used to write blueprints for data or objects <a class="yt-timestamp" data-t="10:16:00">[10:16:00]</a>.
*   **Class**: Encapsulates variables (called properties) and functions (called methods) <a class="yt-timestamp" data-t="00:10:22">[00:10:22]</a>.
*   **Encapsulation**: Bundling data (properties) and methods that operate on the data into a single unit (class).
*   **Inheritance**: Allows classes to share behaviors, where a subclass can extend and override the behaviors of a parent class <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a>.
*   [[Software design patterns | Design Patterns]]: OOP opens the door to various [[Software design patterns | design patterns]] for organizing and reusing code <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>.
*   **Object**: An actual chunk of data instantiated from a class that lives in a computer's memory <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>.

### Memory for Objects
*   **Call Stack**: A short-term chunk of memory for executing code, where function calls are put <a class="yt-timestamp" data-t="00:10:56">[00:10:56]</a>. Data in the call stack is not long-lived.
*   **Heap**: A separate area of memory where long-lived data (objects) can reside <a class="yt-timestamp" data-t="00:10:58">[00:10:58]</a>. Unlike the call stack, the heap can grow and shrink based on application usage <a class="yt-timestamp" data-t="00:11:01">[00:11:01]</a>. Objects can be passed by reference, meaning multiple variables can point to the same object in the heap without increasing memory footprint <a class="yt-timestamp" data-t="00:11:05">[00:11:05]</a>.

## Concurrency and Parallelism
*   **Thread**: The CPU core is broken into virtual cores, allowing simultaneous code execution <a class="yt-timestamp" data-t="00:11:18">[00:11:18]</a>.
*   **Parallelism**: Some programming languages support parallelism, where code executes on two different threads at the same time <a class="yt-timestamp" data-t="00:11:27">[00:11:27]</a>.
*   **Concurrency**: Many single-threaded languages implement concurrency models (like an event loop or co-routines) to handle multiple jobs on a single thread by pausing or delaying normal execution <a class="yt-timestamp" data-t="00:11:35">[00:11:35]</a>.

## Cloud Computing and Networking
Modern computing often involves working with virtual machines in the cloud, which are software simulations of hardware that split large computers into smaller virtual ones <a class="yt-timestamp" data-t="00:11:49">[00:11:49]</a>.
*   **Internet Protocol (IP)**: Virtual machines, forming the backbone of the internet, are connected via IP <a class="yt-timestamp" data-t="00:12:04">[00:12:04]</a>. Each machine has a unique IP address <a class="yt-timestamp" data-t="00:12:08">[00:12:08]</a>.
*   **URL (Uniform Resource Locator)**: An IP address is typically aliased to a URL registered in the Domain Name Service (DNS) <a class="yt-timestamp" data-t="00:12:11">[00:12:11]</a>.
*   **TCP Handshake**: Establishes a connection between two computers, allowing them to exchange messages called packets <a class="yt-timestamp" data-t="00:12:18">[00:12:18]</a>.
*   **SSL (Secure Sockets Layer)**: A security layer typically used on top of TCP to encrypt and decrypt messages over the network <a class="yt-timestamp" data-t="00:12:25">[00:12:25]</a>.
*   **HTTP (Hypertext Transfer Protocol)**: Allows computers to securely share data; a client may request a web page, and the server responds with [[HTML structure and syntax | HTML]] <a class="yt-timestamp" data-t="00:12:31">[00:12:31]</a>.
*   **API (Application Programming Interface)**: Modern servers provide standardized ways for clients to request data <a class="yt-timestamp" data-t="00:12:40">[00:12:40]</a>.
*   **REST (Representational State Transfer)**: A common API architecture where URLs are mapped to different data entities on the server <a class="yt-timestamp" data-t="00:12:46">[00:12:46]</a>.