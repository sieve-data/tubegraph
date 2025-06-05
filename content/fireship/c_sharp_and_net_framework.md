---
title: C Sharp and NET Framework
videoId: ravLFzIguCM
---

From: [[fireship]] <br/> 

C# (C Sharp) is a statically typed, general-purpose programming language widely recognized as the workhorse of the [[windows_as_an_operating_system_for_programmers | Windows .NET framework]] <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>.

## History and Evolution
C# was created in the year 2000 by Anders Hejlsberg at Microsoft <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. It was designed as a modern, C-like [[overview_of_c_sharp_language | object-oriented language]] <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a> and was initially slated to be named "Cool" <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>. Despite initial criticism for appearing as an "imitation Java," C# has evolved to become one of the most popular and well-loved programming languages today <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>. In 2014, C# became open-source software, allowing it to be used to build applications outside of the .NET Framework <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.

## Capabilities and Applications
C# can be used to build a wide range of applications <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>:
*   Desktop applications on .NET Core <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>
*   Cross-platform mobile applications with [[windows_phone_software | Xamarin]] <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>
*   [[popular_programming_languages_for_web_development | Web applications]] using [[comparison_of_web_development_frameworks | Blazer]] <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>
*   Video games with the Unity framework <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>

## Compilation and Execution
[[compiling_and_executing_c_sharp_code | C# code]] is compiled into an intermediate language <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. This intermediate language is then interpreted by the Common Language Runtime (CLR), which executes it as native machine code on any operating system without the need for recompilation <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>.

## Programming Paradigms and [[c_sharp_features_and_capabilities | Features]]
[[c_sharp_in_object_oriented_and_functional_programming | C#]] is primarily known as an [[overview_of_c_sharp_language | object-oriented language]] <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>. It supports:
*   **Object-Oriented Programming (OOP)**: Includes features like classes, inheritance, polymorphism, and constructors/destructors <a class="yt-timestamp" data-t="01:34:00">[01:34:00]</a> <a class="yt-timestamp" data-t="01:42:00">[01:42:00]</a>.
*   **Functional Programming**: Supports functional lambda expressions and other functional programming patterns <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a> <a class="yt-timestamp" data-t="01:57:00">[01:57:00]</a>.
*   **LINQ (Language Integrated Query)**: Allows declarative queries on any data structure <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.
*   **Memory Safety**: It is a memory-safe language due to garbage collection <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>. However, it's possible to create an unsafe context to manually allocate memory using [[lowlevel_systems_programming_languages | pointers]] <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.
*   **Asynchronous Programming**: Supports a task-based asynchronous pattern, enabling non-blocking code using `async`/`await` syntax <a class="yt-timestamp" data-t="02:02:00">[02:02:00]</a>.

## Getting Started with C#

### Setup
To begin, install the .NET Core SDK <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. Then, navigate to an empty directory in the terminal and run `dotnet new` to create a new application <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.

### Basic Code Structure
A new C# application typically creates a `program.cs` file <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>. This file imports the `System` namespace at the top and provides a class with a `Main` function, which is the entry point for code execution <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

### Variables
Variables are declared by specifying a type, followed by a name and a value <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>. By default, a value cannot be null, but it can be made nullable by adding a question mark to the type <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.

### Organizing Code
Code can be organized and shared across files by wrapping it in a namespace <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.

### Classes and Methods
Within a namespace, new classes can be created <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>. Classes support properties, which can be made readable with `get` or writable with `set` <a class="yt-timestamp" data-t="01:48:00">[01:48:00]</a>. C# does not have top-level functions; instead, methods are defined as members of a class <a class="yt-timestamp" data-t="01:52:00">[01:52:00]</a>.

### Executing Code
To compile and execute your C# code, use the `dotnet run` command <a class="yt-timestamp" data-t="02:11:00">[02:11:00]</a>.