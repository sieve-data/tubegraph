---
title: How to create and run a basic Java program
videoId: l9AzO1FMgM8
---

From: [[fireship]] <br/> 

[[History of Java programming language | Java]] is a high-level, multi-paradigm programming language notable for its capability to compile to platform-independent bytecode <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. It was designed by James Gosling in 1990 at Sun Microsystems <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. One of its initial demonstrations was the Star 7 PDA, which led to the creation of the Java mascot, Duke <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>. Today, [[History of Java programming language | Java]] is one of the world's most widely used programming languages, powering enterprise web applications with Spring Framework, Big Data pipelines with Hadoop, mobile apps on Android, and even controllers for NASA's Maestro Mars Rover <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.

What made [[History of Java programming language | Java]] innovative is its compilation process: instead of compiling to machine code like [[Getting started with C programming | C]] or C++, it compiles to bytecode that can run on any operating system without recompilation <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>. This is achieved by executing the code with the [[Java virtual machine and platform independence | Java virtual machine]] (JVM) <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>. [[History of Java programming language | Java]] functions as both a compiled and interpreted language simultaneously <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. A computer only needs to have the [[Java runtime environment and just in time compilation | Java runtime environment]] (JRE) installed, which is common on most systems <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>. For developers, this translates to the "write once, run anywhere" principle <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.

[[History of Java programming language | Java]] is a strongly typed language with a curly brace syntax similar to the [[Getting started with C programming | C]] family of languages <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. It provides more high-level features such as garbage collection, runtime type checking, and reflection <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.

## Getting Started

To begin, you need to install the [[Beginner programming languages and learning tools | Java Development Kit]] (JDK) <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.

## Program Structure

1.  **Create a File**: Create a file with a `.java` extension <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.
2.  **Class Definition**: Every [[Objectoriented programming in Java | Java]] program begins with a class name, which must also match the file name <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.
3.  **Main Method**: The class is required to have a `main` method, as this is where your code execution will begin <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.

## Defining Variables and Output

Inside the `main` method:
*   **Define a Variable**: Declare a variable by specifying its type, followed by a name and a value <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.
*   **Print to Output**: You can print the variable's value to the standard output using the built-in `System` class <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>.

## Defining Methods

Since your code is within a class, you define functions as methods on this class <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.
*   The `public` keyword signifies that the method can be used outside of its defining class <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>.
*   The `static` keyword means it's a member of the class itself, rather than an instance of the class <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>.
*   You then provide a type and name for the method and return a value from it <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.

## Custom Classes and Objects

You can define your own custom classes, which serve as blueprints for objects <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>.
*   Add attributes and methods to these classes <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.
*   Use the `new` keyword to instantiate an object from the class <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.

[[Objectoriented programming in Java | Java]] is inherently [[Objectoriented programming in Java | object-oriented]], but it has evolved to support [[Objectoriented and functional programming in Java | functional patterns]] like anonymous Lambda methods <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.

## Compiling and Running

1.  **Compile**: Once your program is complete, use the compiler to generate a `.class` file, which contains the bytecode <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>.
2.  **Run**: Then, use the `java` command to instruct the [[Java virtual machine and platform independence | JVM]] to interpret and run that file <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>.