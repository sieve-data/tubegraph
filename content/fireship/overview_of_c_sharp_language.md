---
title: Overview of C Sharp Language
videoId: ravLFzIguCM
---

From: [[fireship]] <br/> 

[[C Sharp Features and Capabilities | C#]] is a statically typed, general-purpose programming language <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. It is notable as the "workhorse" of the [[c_sharp_and_net_framework | Windows .NET framework]] <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>.

## History and Origins
C# was created in 2000 by Anders Hejlsberg at Microsoft <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. It was designed as a modern C-like [[c_sharp_in_object_oriented_and_functional_programming | object-oriented language]] <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a> and was initially going to be called "Cool" <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>. Although initially criticized as an "imitation Java," it has evolved into one of the most popular and well-loved programming languages <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>. In 2014, C# became open-source software <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>, allowing it to build applications outside of the [[c_sharp_and_net_framework | .NET Framework]] <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>.

## Applications and Usage
C# can be used to build a wide range of applications <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>:
*   Desktop applications on .NET Core <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>
*   Cross-platform mobile applications with Xamarin <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>
*   Web applications with Blazor <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>
*   Video games with the Unity framework <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>

## [[c_sharp_features_and_capabilities | Key Features]]
C# is primarily known as an [[c_sharp_in_object_oriented_and_functional_programming | object-oriented language]] <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>, but it also supports [[c_sharp_in_object_oriented_and_functional_programming | functional Lambda expressions]] <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a> and other functional programming patterns <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>. It includes a feature called LINQ (Language Integrated Query) that allows writing declarative queries on any data structure <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.

It is a memory-safe language due to garbage collection <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>. However, it is possible to create an unsafe context to allocate memory with pointers <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. For asynchronous programming, C# supports a task-based asynchronous pattern, enabling non-blocking code using the `async` and `await` syntax <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.

## [[compiling_and_executing_c_sharp_code | Compiling and Execution]]
C# code is compiled into an intermediate language <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. This intermediate language can then be interpreted by the Common Language Runtime (CLR), where it is executed as native machine code on any operating system without requiring recompilation <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>.

## Getting Started
To begin with C#, install the .NET Core SDK <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. In an empty directory, use the terminal command `dotnet new` to create a new application <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. This command generates a `Program.cs` file <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.

### Code Structure
*   **Namespaces**: The `Program.cs` file imports the `System` namespace at the top <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>. Code can be wrapped in a namespace to organize it and share it across other files <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.
*   **Classes**: The file provides a class with a `Main` function, which is the entry point for code execution <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. New classes can be created within a namespace, which can have a Constructor (instantiated when the class is created) and a Destructor (called when the class goes out of scope) <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>. Classes support inheritance, polymorphism, and other typical object-oriented features <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.
*   **Variables**: Variables are declared by specifying a type, followed by a name and a value <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>. By default, a variable cannot be null, but adding a question mark to the type makes it nullable <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.
*   **Properties**: Properties can be defined on a class and made readable with `get` or writable with `set` <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.
*   **Methods**: The language does not have top-level functions; instead, functions are defined as methods that are members of a class <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.

### Executing Code
To [[compiling_and_executing_c_sharp_code | compile and execute]] C# code, use the `dotnet run` command <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.