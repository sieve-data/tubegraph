---
title: Computer Architecture and Components
videoId: -uleG_Vecis
---

From: [[fireship]] <br/> 

Understanding the fundamental concepts of computer science provides insight into how software interacts with hardware. Many software engineers learn to code and secure high-paying jobs without fully grasping how computers function internally <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. This knowledge, however, is crucial for truly comprehending the "magic" behind the code <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>.

## What is a Computer?

At its core, a computer can be understood as a "Turing machine," a theoretical device consisting of a piece of tape that holds ones and zeros, and a mechanism to read and write to it <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>. In theory, a Turing machine can compute anything, from video graphics to complex algorithms <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.

## Fundamental Hardware Components

Modern computers are built around key hardware components that process and store information.

### [[How a CPU Works | Central Processing Unit (CPU)]]

The [[How a CPU Works | CPU]] is at the core of modern computers <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>. When opened, a [[How a CPU Works | CPU]] reveals a piece of silicon containing billions of tiny [[Transistors and Logic Gates in a CPU | transistors]] <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. These [[Transistors and Logic Gates in a CPU | transistors]] act like microscopic on/off switches <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.

*   **Bit**: The value of one of these switches is called a "bit," the smallest piece of information a computer can use <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.
*   **Byte**: A single bit isn't very useful on its own, so bits are packaged in groups of eight, called a "byte" <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. One byte can represent 256 different values, such as all the characters typed on a keyboard <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. When typing, characters are mapped to binary values using character encodings like ASCII or UTF-8 <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.

### Data Representation: Binary and Hexadecimal

*   **Binary**: This is a system for counting that uses only two characters: 1 and 0 <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>.
*   **Hexadecimal**: Because binary is difficult for humans to read, it's often represented in hexadecimal, a base-16 format <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>. In hexadecimal, ten numbers and six letters represent a four-bit group called a "nibble" <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.

When developers write code, it's eventually converted into "machine code," a binary format the [[How a CPU Works | CPU]] can decode and execute <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.

### Random Access Memory (RAM)

The [[How a CPU Works | CPU]] doesn't store application data itself; for that, computers use "Random Access Memory" or RAM <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. RAM can be thought of as a neighborhood where each house holds a byte, and every location has a unique "memory address" that the [[How a CPU Works | CPU]] can read from and write to <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>. The [[How a CPU Works | CPU]] and RAM are considered the brain of the computer <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.

### Input/Output Devices

For a computer to be useful, it needs to handle input and output. Examples include keyboards and mice as input devices, and monitors as output devices <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>.

## Software Layer: Operating Systems and Shells

Most developers don't need to directly manage hardware interactions because "operating system kernels" like [[Linux system architecture and components | Linux]], Mac, and Windows control all hardware resources through "device drivers" <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.

The "shell" is a program that provides an entry point to interact with the operating system, exposing it to the user <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>. It's called a shell because it "wraps" the kernel <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>. Shells typically take a line of text as input and produce output, forming a "command line interface" (CLI) <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>. Command line interfaces can connect to both local and remote computers over a network using protocols like Secure Shell (SSH) <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>.

## Programming Languages and Abstraction

Programming languages are tools that use the "abstraction principle" to simplify working with computers for humans, by building systems layer by layer <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.

*   **Interpreted Languages**: Languages like Python are "interpreted," meaning a program called an "interpreter" executes each line of code one by one <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.
*   **Compiled Languages**: Languages like C++ are "compiled" <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>. They use a "compiler" to convert the entire program into machine code in advance, resulting in an "executable file" that the operating system can run without extra dependencies <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>.

## Data Types and Memory Management

Programming languages offer built-in "data types" to represent data in a more human-friendly way than raw bytes, such as characters and numbers <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.

### Variables and Memory Allocation

The most fundamental way to use data is to declare a "variable," which attaches a name to a data point for reuse <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.

*   **Dynamically Typed Languages**: In languages like Python, you don't need to explicitly tell the program the data type of a variable; it figures it out automatically <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.
*   **Statically Typed Languages**: In contrast, languages like C require you to specify the data type of a variable when you define it <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.

When a variable is defined, its value is stored in memory on the hardware <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.

*   **Pointers**: A "pointer" is a variable whose value is the memory address of another variable, used for low-level memory control <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.
*   **Garbage Collector**: Many languages avoid low-level memory management by implementing a "garbage collector," which automatically allocates and de-allocates memory when an object is no longer referenced <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.

### Common Data Types

*   **Integer (int)**: Represents whole numbers, which can be signed (allowing negative numbers) or unsigned <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.
*   **Floating Point (float)**: Used for numbers with a decimal point <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>. It's called "float" because there's limited memory, representing a range of numbers at a certain precision, similar to scientific notation <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.
*   **Double**: Many languages offer a "double" for more range or precision, which doubles the memory used for the number <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>.
*   **Character (char)**: Represents a single character <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>.
*   **String**: Represents multiple characters together <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>.

### Endianness

When characters are stored in memory, their order matters.
*   **Big Endian**: The most significant byte is stored at the smallest memory address <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.
*   **Little Endian**: The least significant byte is stored at the smallest memory address <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>.

## Data Structures

"Data structures" are fundamental for organizing data in software engineering <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>.

*   **Array / List**: Organizes multiple data points in order and maintains an index of integers starting at zero <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>.
*   **Linked List**: Each item has a pointer to the next item, useful when an index isn't needed <a class="yt-timestamp" data-t="00:05:33">[00:05:33]</a>.
*   **Stack**: Follows the "last in, first out" (LIFO) principle, like a stack of plates where the last one added is the first one removed <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.
*   **Queue**: The inverse of a stack, following a "first in, first out" (FIFO) principle <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>.
*   **Hash / Map / Dictionary**: Similar to an array, but instead of an integer index, you define "keys" that point to individual items, creating a collection of key-value pairs <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>.
*   **Trees**: Organize nodes in a hierarchy, allowing for quicker traversal than linear structures <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>.
*   **Graphs**: Connect multiple nodes (data points) together in virtually unlimited ways, with "edges" representing the relationships between data points <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a>.

## Algorithms and Control Flow

"Algorithms" are blocks of code that solve a problem <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.

### Functions

A "function" is a fundamental mechanism for implementing algorithms, taking an input, performing an action, and returning an output <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>. Functions have a name and can be called from other parts of the code with different input parameters, known as "arguments" <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>.

*   **Operators**: Languages provide built-in operators (e.g., equality, greater than, less than) to compare values <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>.
*   **Boolean**: Comparisons result in a "Boolean" data type, which is either true or false <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>.
*   **Expression vs. Statement**: Code that produces a value is an "expression" <a class="yt-timestamp" data-t="00:07:19">[00:07:19]</a>. Code that simply performs an action is a "statement" <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>.

### Control Flow

*   **If Statement**: Handles "conditional logic," executing code if a condition is true, or running code in an "else block" if false <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.
*   **Loops**:
    *   **While Loop**: Runs a block of code repeatedly until a condition becomes false <a class="yt-timestamp" data-t="00:07:38">[00:07:38]</a>.
    *   **For Loop**: Iterates over iterable data types, such as arrays, executing code for each item <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>.
*   **Void Function**: A function that doesn't have an output <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>.
*   **Recursion**: Occurs when a function calls itself <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>. Without a "base condition" to terminate the loop, it can lead to an "infinite loop" <a class="yt-timestamp" data-t="00:08:07">[00:08:07]</a>. When a function is called, the programming language places it into memory on the "call stack," a short-term memory chunk for executing code <a class="yt-timestamp" data-t="00:08:13">[00:08:13]</a>. Continuous recursion can cause a "stack overflow error" <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>.

### Algorithm Performance

*   **Big-O Notation**: A standard format for approximating the performance of an algorithm at scale <a class="yt-timestamp" data-t="00:08:34">[00:08:34]</a>.
    *   **Time Complexity**: How fast an algorithm will run <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>.
    *   **Space Complexity**: How much memory is required <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>.

### Types of Algorithms

*   **Brute Force**: Involves looping over every possible combination to solve a problem <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>.
*   **Divide and Conquer**: Breaks a problem into smaller sub-problems, like "binary search" which repeatedly cuts the problem in half <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>.
*   **Dynamic Programming**: Breaks a problem into smaller sub-problems and stores the result of each computation for later use, a technique called "memoization" <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>. Memoization prevents recomputing values if a function has already been called <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>.
*   **Greedy Algorithms**: Make the most beneficial choice in the short term without considering the problem as a whole, for example, Dijkstra's shortest path algorithm <a class="yt-timestamp" data-t="00:09:22">[00:09:22]</a>.
*   **Backtracking Algorithms**: Take an incremental approach, exploring all possible options, like a rat navigating a maze <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.

## Programming Paradigms

Different "programming paradigms" offer multiple ways to structure code.

*   **Declarative Programming**: Describes *what* the program does and its outcome, without detailing control flow <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>. Often associated with "functional languages" like Haskell <a class="yt-timestamp" data-t="00:09:53">[00:09:53]</a>.
*   **Imperative Programming**: Uses statements (like `if` and `while`) to provide explicit instructions on *how* to produce an outcome <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>. Associated with "procedural languages" like C <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>.
*   **Multi-Paradigm Languages**: Most modern general-purpose languages (Python, JavaScript, Kotlin, Swift) support multiple paradigms simultaneously <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>.

### Object-Oriented Programming (OOP)

A common paradigm is "Object-Oriented Programming" (OOP) <a class="yt-timestamp" data-t="00:10:16">[00:10:16]</a>.

*   **Classes**: Used to write a blueprint for data or "objects" <a class="yt-timestamp" data-t="00:10:18">[00:10:18]</a>.
*   **Properties**: Variables encapsulated within a class <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>.
*   **Methods**: Functions encapsulated within a class <a class="yt-timestamp" data-t="00:10:26">[00:10:26]</a>.
*   **Inheritance**: Classes can share behaviors through "inheritance," where a "subclass" can extend and override behaviors of a "parent class" <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>. This also opens the door to "design patterns" <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>.
*   **Objects**: Classes are used to "instantiate objects," which are actual chunks of data living in memory <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>.

### Heap vs. Call Stack

*   **Heap**: When data is long-lived and needs to be referenced repeatedly, it's stored in a separate memory area called the "heap" <a class="yt-timestamp" data-t="00:10:55">[00:10:55]</a>. Unlike the call stack, the heap can grow and shrink based on application usage <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>.
*   **Pass by Reference**: The heap allows "passing objects by reference," meaning multiple variables can use the same object without increasing memory footprint, as they all point to the same memory location <a class="yt-timestamp" data-t="00:11:05">[00:11:05]</a>.

## Concurrency and Parallelism

The [[How a CPU Works | CPU]] contains multiple "threads" <a class="yt-timestamp" data-t="00:11:15">[00:11:15]</a>. A thread virtually breaks a physical [[How a CPU Works | CPU]] core into smaller cores, allowing it to run code simultaneously <a class="yt-timestamp" data-t="00:11:20">[00:11:20]</a>.

*   **Parallelism**: Some programming languages support "parallelism," where code literally executes on two different threads at the same time <a class="yt-timestamp" data-t="00:11:27">[00:11:27]</a>.
*   **Concurrency**: Many languages are "single-threaded" but achieve concurrency by implementing models like "event loops" or "co-routines" <a class="yt-timestamp" data-t="00:11:35">[00:11:35]</a>. These models can pause or delay code execution to handle multiple jobs on a single thread simultaneously <a class="yt-timestamp" data-t="00:11:40">[00:11:40]</a>.

## Modern Cloud Computing

In modern computing, developers rarely work directly with the bare metal [[How a CPU Works | CPU]] and RAM <a class="yt-timestamp" data-t="00:11:49">[00:11:49]</a>. Instead, they work in the "cloud" with "virtual machines" <a class="yt-timestamp" data-t="00:11:53">[00:11:53]</a>. A virtual machine is software that simulates hardware, allowing large computers to be split into many smaller virtual ones <a class="yt-timestamp" data-t="00:11:55">[00:11:55]</a>.

### Internet Communication

These virtual machines form the backbone of the internet and are connected via the "Internet Protocol" (IP) <a class="yt-timestamp" data-t="00:12:03">[00:12:03]</a>. Each machine has a unique "IP address" for identification <a class="yt-timestamp" data-t="00:12:07">[00:12:07]</a>, often aliased to a "URL" registered in the "Domain Name Service" (DNS) <a class="yt-timestamp" data-t="00:12:11">[00:12:11]</a>.

*   **TCP Handshake**: To establish a connection, two computers perform a "TCP handshake" to exchange "packets" (messages) <a class="yt-timestamp" data-t="00:12:17">[00:12:17]</a>.
*   **SSL**: A "security layer" like SSL (Secure Sockets Layer) typically encrypts and decrypts messages over the network <a class="yt-timestamp" data-t="00:12:25">[00:12:25]</a>.
*   **HTTP**: The "Hypertext Transfer Protocol" (HTTP) allows secure data sharing <a class="yt-timestamp" data-t="00:12:31">[00:12:31]</a>. A client might request a web page, and the server responds with HTML <a class="yt-timestamp" data-t="00:12:35">[00:12:35]</a>.
*   **API**: Modern servers provide a standardized way for clients to request data through an "Application Programming Interface" (API) <a class="yt-timestamp" data-t="00:12:40">[00:12:40]</a>.
*   **REST**: A common API architecture is "REST," where URLs are mapped to different data entities available on the server <a class="yt-timestamp" data-t="00:12:47">[00:12:47]</a>.