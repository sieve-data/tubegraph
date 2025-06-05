---
title: Introduction to computer science concepts
videoId: -uleG_Vecis
---

From: [[fireship]] <br/> 

Computer science explores the fundamental principles behind how computers work and how software is built <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. It provides the underlying "science" for understanding software engineering, even though it's possible to code without deep knowledge of these concepts <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>.

## [[Fundamentals of computing and binary systems | Core Components of a Computer]]

At its most basic, a computer is a device that can read and write to a piece of tape holding ones and zeros <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>. This theoretical model is known as a [[Fundamentals of computing and binary systems | Turing Machine]], capable of computing anything <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.

### Central Processing Unit (CPU)
The core of modern computers is the Central Processing Unit (CPU) <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>. Inside the CPU, billions of tiny transistors act as microscopic on/off switches <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.

*   **Bit**: The value at one of these switches, representing the smallest piece of information a computer can use <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.
*   **Byte**: A package of eight bits, capable of representing 256 different values, such as keyboard characters <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>.
*   **Nibble**: A four-bit group <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>.

### [[Fundamentals of computing and binary systems | Binary Systems]]
Computers use a binary system, which is a base-2 counting system with only two characters: one and zero <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>. Characters typed on a keyboard are mapped to binary values using character encodings like ASCII or UTF-8 <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>. For human readability, binary is often represented in hexadecimal (base-16) format <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.

Code written in programming languages is converted into **machine code**, a binary format that the CPU can decode and execute <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.

### Random Access Memory (RAM)
The CPU does not store application data itself <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>. For that, computers use **Random Access Memory (RAM)**, where each location has a memory address that the CPU can read and write to <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>. The CPU and RAM are considered the "brain" of the computer <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.

### Input and Output (I/O) Devices
For a computer to be useful, it needs to handle input and output <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>.
*   **Input devices** include keyboards and mice <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.
*   **Output devices** include monitors <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.

## Operating Systems

Developers generally don't need to worry about how hardware fits together because **operating system kernels** like [[Introduction to Linux and its History | Linux]], Mac, and Windows control all hardware resources via device drivers <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.

*   **Shell**: A program that acts as the user's entry point to the operating system, wrapping the kernel <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>.
*   **Command Line Interface (CLI)**: The shell takes text as input and produces output, forming a CLI <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.
*   **Secure Shell (SSH)**: A protocol that allows connecting to remote computers over a network using the shell <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>.

## Programming Languages

Programming languages are tools that use the **abstraction principle** to simplify working with computers for humans by layering different systems <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.

*   **Interpreted Languages**: A program called an interpreter executes each line of code one by one (e.g., Python) <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.
*   **Compiled Languages**: A compiler converts the entire program into machine code in advance, resulting in an executable file that can run without extra dependencies (e.g., C++) <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.

## Data Representation and Memory Management

Programming languages have built-in **data types** to represent data in a human-friendly way, such as characters and numbers, instead of raw bytes <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.

*   **Variables**: The fundamental way to use data, attaching a name to a data point for reuse <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.
    *   **Dynamically typed language**: The program automatically figures out the data type assigned to a variable (e.g., Python) <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.
    *   **Statically typed language**: The data type of a variable must be specified in the code when defined (e.g., C) <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.

### Memory Allocation
When a variable is defined, its value is stored in memory <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.
*   **Pointer**: A variable whose value is the memory address of another variable, used for low-level memory control <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.
*   **Garbage Collector**: Many languages implement a garbage collector to automatically allocate and de-allocate memory when an object is no longer referenced <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.

### Common Data Types
*   **Int**: Represents whole numbers, which can be signed (negative numbers) or unsigned <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.
*   **Floating Point (Float)**: Represents numbers with a decimal point. It has a limited memory, representing a range of numbers at a certain precision, similar to scientific notation <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>.
*   **Double**: Offers more range or precision by doubling the memory used for a number <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>.
*   **Char**: Represents a single character <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>.
*   **String**: Represents multiple characters together <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>.

### Endianness
When characters are stored in memory, their order matters:
*   **Big-endian**: The most significant byte is stored at the smallest memory address <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.
*   **Little-endian**: The least significant byte is stored at the smallest memory address <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>.

## [[Data structures and algorithms | Data Structures]]

[[Data structures and algorithms | Data structures]] are fundamental ways to organize data in software engineering <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>.

*   **Array / List**: Organizes multiple data points in order, maintaining an integer index starting at zero <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>.
*   **Linked List**: Each item has a pointer to the next item in the sequence <a class="yt-timestamp" data-t="00:05:33">[00:05:33]</a>.
*   **Stack**: Follows the **Last-In, First-Out (LIFO)** principle, where the last item added is the first one accessed <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>.
*   **Queue**: Follows the **First-In, First-Out (FIFO)** principle, where the first item added is the first one accessed <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>.
*   **Hash / Map / Dictionary**: Like an array, but uses user-defined keys to point to individual items, forming a collection of key-value pairs <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>.
*   **Trees**: Organize nodes (data points) in a hierarchy, allowing for quicker traversal <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>.
*   [[Introduction to Graphs and Types | **Graphs**]]: Connect multiple nodes (data) together in a virtually unlimited number of ways, with edges representing relationships between data points <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.

## [[Data structures and algorithms | Algorithms]]

[[Data structures and algorithms | Data structures]] don't perform actions on their own <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a>. To do something useful, an **algorithm** is needed, which is code that solves a problem <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>.

### Algorithmic Mechanisms
*   **Function**: A block of code that takes an input, performs actions, and returns an output <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>.
    *   Functions have names and can be called with different input parameters called **arguments** <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>.
*   **Operators**: Built-in mechanisms (like equality, greater than, less than) used to compare values <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>.
*   **Boolean**: A data type representing true or false values, often the result of comparisons <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a>.
*   **Expression**: Code that produces a value <a class="yt-timestamp" data-t="00:07:19">[00:07:19]</a>.
*   **Statement**: Code that simply performs an action without necessarily producing a value <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>.
    *   **If Statement**: Handles conditional logic, executing code if a condition is true, otherwise running an `else` block <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.
    *   **Loop**: A type of statement that runs a block of code repeatedly.
        *   **While Loop**: Runs code repeatedly until a condition becomes false <a class="yt-timestamp" data-t="00:07:38">[00:07:38]</a>.
        *   **For Loop**: Iterates over an iterable data type, like an array, running code for each item <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>.
*   **Void Function**: A function that does not have an output <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>.
*   **Recursion**: When a function calls itself <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>.
    *   If not terminated, recursion can lead to an **infinite loop** <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>.
    *   **Call Stack**: A short-term memory chunk where programming languages put function calls <a class="yt-timestamp" data-t="00:08:13">[00:08:13]</a>. Continuous recursive calls push frames onto the call stack, potentially causing a **stack overflow error** <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>.
    *   A **base condition** is needed to terminate recursive loops <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>.

### Algorithm Performance
*   **Big-O Notation**: A standard format for approximating the performance of an algorithm at scale <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a>.
    *   **Time Complexity**: How fast an algorithm will run <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>.
    *   **Space Complexity**: How much memory is required to run an algorithm <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>.

### Types of Algorithms
*   **Brute Force**: Involves looping over every possible combination to solve a problem <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>.
*   **Divide and Conquer**: Breaks a problem into smaller sub-problems, like binary search, which repeatedly cuts the problem in half <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>.
*   **Dynamic Programming**: Breaks a problem into smaller sub-problems and stores the results of each computation for later use <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>.
    *   **Memoization**: A technique used in dynamic programming where if a function has already been called, its existing value is used instead of recomputing it <a class="yt-timestamp" data-t="00:09:13">[00:09:13]</a>.
*   **Greedy Algorithms**: Make the most beneficial choice in the short term without considering the problem as a whole (e.g., Dijkstra's shortest path algorithm) <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>.
*   **Backtracking Algorithms**: Take an incremental approach, exploring all possible options like a rat in a maze <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.

## Programming Paradigms

Different ways to structure and organize code:
*   **Declarative Programming**: Code describes what the program does and its desired outcome, without specifying the control flow <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>. Often associated with functional languages like Haskell <a class="yt-timestamp" data-t="00:09:53">[00:09:53]</a>.
*   **Imperative Programming**: Code uses statements (like `if` and `while`) to provide explicit instructions on how to produce an outcome <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>. Associated with procedural languages like C <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>.
*   **Multi-Paradigm Languages**: Support multiple programming paradigms (e.g., Python, JavaScript, Kotlin, Swift) <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>.

### Object-Oriented Programming (OOP)
A common paradigm where **classes** are used as blueprints for data or **objects** <a class="yt-timestamp" data-t="00:10:16">[00:10:16]</a>.
*   **Encapsulation**: Classes encapsulate variables (called **properties**) and functions (called **methods**) <a class="yt-timestamp" data-t="00:10:23">[00:10:23]</a>.
*   **Inheritance**: Classes can share behaviors through inheritance, where a **subclass** extends and overrides behaviors of a **parent class** <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>.
*   OOP supports various **design patterns** <a class="yt-timestamp" data-t="00:10:39">[00:10:39]</a>.

Objects are actual chunks of data in memory, instantiated from classes <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>.
*   **Heap**: A separate area of memory from the call stack where long-lived data objects are stored, allowing them to grow and shrink <a class="yt-timestamp" data-t="00:10:55">[00:10:55]</a>.
*   **Pass by Reference**: Allows multiple variables to use the same object without increasing memory footprint, as they all point to the same chunk of memory in the heap <a class="yt-timestamp" data-t="00:11:05">[00:11:05]</a>.

## Concurrency and Parallelism

*   **Threads**: The CPU core is broken into virtual cores, allowing code to run simultaneously <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>.
*   **Parallelism**: Programming languages that support parallelism can execute code on two different threads at the same time <a class="yt-timestamp" data-t="00:11:27">[00:11:27]</a>.
*   **Concurrency**: Many single-threaded languages implement concurrency models (like event loops or co-routines) to handle multiple jobs on a single thread by pausing or delaying execution <a class="yt-timestamp" data-t="00:11:34">[00:11:34]</a>.

## Networking and the Internet

Modern computing often involves working in the cloud with **virtual machines** – software that simulates hardware, splitting large computers into smaller virtual ones <a class="yt-timestamp" data-t="00:11:49">[00:11:49]</a>. These machines are the backbone of the [[Understanding the Internet and the World Wide Web | Internet]] <a class="yt-timestamp" data-t="00:12:03">[00:12:03]</a>.

*   **[[Understanding the Internet and the World Wide Web | Internet Protocol (IP) Address]]**: Each machine has a unique IP address to identify it on the network <a class="yt-timestamp" data-t="00:12:06">[00:12:06]</a>.
*   **URL (Uniform Resource Locator)**: An alias for an IP address, registered in a global database called the **Domain Name Service (DNS)** <a class="yt-timestamp" data-t="00:12:11">[00:12:11]</a>.
*   **TCP Handshake**: Two computers establish a connection by performing a TCP handshake to exchange messages called packets <a class="yt-timestamp" data-t="00:12:18">[00:12:18]</a>.
*   **SSL (Secure Sockets Layer)**: A security layer typically used on top of TCP to encrypt and decrypt messages over the network <a class="yt-timestamp" data-t="00:12:24">[00:12:24]</a>.
*   **Hypertext Transfer Protocol (HTTP)**: Allows two computers to securely share data; a client may request a web page, and the server responds with HTML <a class="yt-timestamp" data-t="00:12:31">[00:12:31]</a>.
*   **Application Programming Interface (API)**: Modern servers provide a standardized way for clients to request data <a class="yt-timestamp" data-t="00:12:40">[00:12:40]</a>.
*   **REST Architecture**: A common API architecture where URLs are mapped to different data entities on the server <a class="yt-timestamp" data-t="00:12:46">[00:12:46]</a>.