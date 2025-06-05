---
title: C Sharp in Object Oriented and Functional Programming
videoId: ravLFzIguCM
---

From: [[fireship]] <br/> 

[[overview_of_c_sharp_language|C#]] is a statically typed, general-purpose programming language <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. It is widely recognized as the workhorse of the Windows [[c_sharp_and_net_framework|.NET framework]] <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>.

Created in 2000 by Anders Hejlsberg at Microsoft, [[overview_of_c_sharp_language|C#]] was initially designed as a modern C-like [[objectoriented_programming_in_c|object-oriented language]] <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. Although it faced initial criticism as an imitation of [[objectoriented_programming_in_java|Java]] <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>, it has since evolved into one of the most popular and well-loved programming languages <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. In 2014, [[overview_of_c_sharp_language|C#]] became open-source software, enabling its use for applications outside of the [[c_sharp_and_net_framework|.NET Framework]] <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.

## [[overview_of_c_sharp_language|Overview of C#]] and Execution
[[compiling_and_executing_c_sharp_code|C# code]] is compiled into an intermediate language <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. This intermediate language is then interpreted by the Common Language Runtime (CLR), allowing it to be executed as native machine code on any operating system without the need for recompilation <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.

[[overview_of_c_sharp_language|C#]] is considered a memory-safe language due to its use of garbage collection <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>. However, it does provide the option to create an "unsafe context" for developers who wish to manually allocate memory using pointers <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.

## [[objectoriented_programming_in_c|Object-Oriented Programming]] in [[overview_of_c_sharp_language|C#]]
[[overview_of_c_sharp_language|C#]] is primarily known as an [[objectoriented_programming_in_c|object-oriented language]] <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>. It fully supports the core principles of [[objectoriented_programming_in_c|object-oriented programming]]:

*   **Classes**: [[overview_of_c_sharp_language|C#]] organizes code within classes, which can include a `main` function as the entry point for execution <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. Classes can have constructors, which are called when a class is instantiated, and destructors, which are called when the class goes out of scope <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.
*   **Encapsulation**: Properties can be defined on a class, with controlled access through `get` (readable) and `set` (writable) accessors <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>. Variables are declared with a type, name, and value <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>. By default, values cannot be null, but they can be made nullable by adding a question mark to the type <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.
*   **Inheritance**: Classes support inheritance, allowing new classes to inherit properties and methods from existing classes <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.
*   **Polymorphism**: [[overview_of_c_sharp_language|C#]] supports polymorphism, enabling objects of different classes to be treated as objects of a common type <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.
*   **Methods**: The language does not have top-level functions; instead, methods are defined as members of a class <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.
*   **Namespaces**: Code can be organized and shared across multiple files by wrapping it in a namespace <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.

## [[functional_programming_languages_and_their_features|Functional Programming]] Support in [[overview_of_c_sharp_language|C#]]
While primarily [[objectoriented_programming_in_c|object-oriented]], [[overview_of_c_sharp_language|C#]] also incorporates features that support [[functional_programming_languages_and_their_features|functional programming]] paradigms <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>:

*   **Lambda Expressions**: [[overview_of_c_sharp_language|C#]] supports functional lambda expressions and anonymous functions <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a> <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.
*   **LINQ (Language Integrated Query)**: A key [[c_sharp_features_and_capabilities|feature]] called LINQ allows for writing declarative queries on any data structure <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.
*   **Asynchronous Programming**: [[overview_of_c_sharp_language|C#]] provides a task-based asynchronous pattern, enabling developers to write non-blocking code using the `async` and `await` syntax <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.