---
title: Data structures and algorithms
videoId: -uleG_Vecis
---

From: [[fireship]] <br/> 

In software engineering, understanding [[introduction_to_computer_science_concepts | computer science concepts]] like data structures and algorithms is crucial for organizing data and solving problems efficiently <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. While it's possible to learn to code and secure a high-paying job without knowing how everything works, deeper knowledge of these fundamentals enhances a developer's capabilities <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>.

## Data Structures

Data structures are fundamental ways to organize data in programming <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>. They allow for efficient storage and retrieval of information.

### Common Data Structures

*   **Array (or List)**: Similar to a shopping list, an array organizes multiple data points in order <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>. It maintains an index of integers, typically starting at zero, for each item <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>.
*   **Linked List**: Unlike an array, a linked list does not require an index <a class="yt-timestamp" data-t="00:05:33">[00:05:33]</a>. Each item in a linked list has a pointer to the next item <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>.
*   **Stack**: A stack follows the "last in, first out" (LIFO) principle <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>. Data is "popped" off the top, similar to removing the top plate from a stack <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>. The call stack, used for executing function calls, is an example of a stack <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>.
*   **Queue**: The inverse of a stack, a queue adheres to the "first in, first out" (FIFO) principle <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>. The first item in is the first to be processed <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>.
*   **Hash (Map or Dictionary)**: This structure is like an array but uses user-defined keys instead of integer indexes to point to individual items <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>. It results in a collection of key-value pairs <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>.
*   **Tree**: Trees organize nodes hierarchically, allowing for quicker traversal than linear structures <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>.
*   **Graph**: A graph is a more flexible structure than a tree, connecting multiple nodes (data points) via edges (relationships) in a virtually unlimited number of ways <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.

## Algorithms

Algorithms are blocks of code designed to solve specific problems <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>.

### Core Algorithmic Mechanisms

*   **Function**: A fundamental mechanism for implementing algorithms <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>. A function is a block of code that takes an input, performs an action, and returns an output <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>. It has a name and can be called from other parts of the code with different input parameters, known as arguments <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>. A function without an output is often called a *void function* <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>.
*   **Operators**: Built-in programming language elements used to compare values, such as equality, greater than, or less than <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>.
*   **Expression**: Any code that produces a value, such as a boolean (true/false) from a comparison <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>.
*   **Statement**: Code that performs an action but does not necessarily produce a value <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>.
    *   **If Statement**: Handles conditional logic, executing a block of code if a condition is true, or an `else` block if false <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>.
    *   **Loop**: A type of statement that runs a block of code repeatedly.
        *   **While Loop**: Executes code repeatedly until a specified condition becomes false <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>.
        *   **For Loop**: Commonly used to iterate over iterable data types like arrays, running code for each object <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>.
*   **Recursion**: Occurs when a function calls itself <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>. Without a *base condition*, recursion can lead to an infinite loop and a *stack overflow error* as the call stack fills up with function frames <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>.

### Algorithm Performance

*   **Big-O Notation**: A standard format for approximating the performance of an algorithm, especially as the input scale increases <a class="yt-timestamp" data-t="00:08:34">[00:08:34]</a>.
    *   **Time Complexity**: Measures how fast an algorithm will run <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>.
    *   **Space Complexity**: Deals with the amount of memory required by an algorithm <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>.

### Types of Algorithms

*   **Brute Force**: A basic approach where every possible combination is explored to solve a problem <a class="yt-timestamp" data-t="00:08:51">[00:08:51]</a>.
*   **Divide and Conquer**: Breaks a problem into smaller, similar sub-problems, solving each one and combining the results <a class="yt-timestamp" data-t="00:08:58">[00:08:58]</a>. Binary search, which repeatedly cuts the problem in half, is an example <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.
*   **Dynamic Programming**: A problem is broken into multiple smaller sub-problems, and the result of each computation is stored using *memoization* <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>. This means if a function has already been called with specific inputs, its result is reused rather than recomputed <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>.
*   **Greedy Algorithms**: Make the locally optimal choice at each step without considering the overall problem <a class="yt-timestamp" data-t="00:09:23">[00:09:23]</a>. Dijkstra's shortest path algorithm is an example <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>.
*   **Backtracking Algorithms**: Take an incremental approach, exploring all possible options like a rat in a maze <a class="yt-timestamp" data-t="00:09:33">[00:09:33]</a>.

### Programming Paradigms

Different ways to structure and implement code:

*   **Declarative Programming**: Describes *what* the program does and its desired outcome, without specifying *how* (e.g., control flow) <a class="yt-timestamp" data-t="00:09:46">[00:09:46]</a>. Often associated with functional languages <a class="yt-timestamp" data-t="00:09:53">[00:09:53]</a>.
*   **Imperative Programming**: Uses explicit instructions (statements like `if` and `while`) to define *how* to produce an outcome <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>. Associated with procedural languages <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>.
*   **Multi-Paradigm Languages**: Modern general-purpose languages like Python, JavaScript, and Kotlin support multiple paradigms, including [[overview_of_software_design_patterns | object-oriented programming]] <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>.

#### Object-Oriented Programming (OOP)

OOP utilizes classes as blueprints for data (objects) <a class="yt-timestamp" data-t="00:10:16">[00:10:16]</a>.
*   **Classes**: Encapsulate variables (called *properties*) and functions (called *methods*) <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>. Classes organize and reuse code, supporting *inheritance* where a subclass can extend or override parent class behaviors <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>. This concept leads to [[overview_of_software_design_patterns | design patterns]] <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>.
*   **Objects**: Actual instances of data created from classes, residing in the computer's memory <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>. Long-lived objects are stored in the *heap* memory, which can grow and shrink dynamically <a class="yt-timestamp" data-t="00:10:56">[00:10:56]</a>. Objects can be passed *by reference*, allowing multiple variables to point to the same object without increasing memory footprint <a class="yt-timestamp" data-t="00:11:05">[00:11:05]</a>.

### Concurrency and Parallelism

*   **Threads**: A CPU core can be broken into virtual cores, allowing code to run simultaneously <a class="yt-timestamp" data-t="00:11:20">[00:11:20]</a>.
*   **Parallelism**: Some programming languages support parallelism, where code literally executes on two different threads at the same time <a class="yt-timestamp" data-t="00:11:28">[00:11:28]</a>.
*   **Concurrency**: Many single-threaded languages implement concurrency models (like an *event loop* or *co-routines*) to handle multiple jobs by pausing or delaying execution on a single thread <a class="yt-timestamp" data-t="00:11:35">[00:11:35]</a>.