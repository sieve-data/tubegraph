---
title: Static type systems and productionlevel programming languages
videoId: pEfrdAtAmqk
---

From: [[fireship]] <br/> 

As software complexity increases, developers often seek more rigid frameworks, which can be achieved through a static type system <a class="yt-timestamp" data-t="03:38:40">[03:38:40]</a>. This approach makes up the bulk of production code currently in use globally <a class="yt-timestamp" data-t="03:46:27">[03:46:27]</a>.

## Key Statically Typed Production Languages

### Java
Java revolutionized programming with its Java Virtual Machine (JVM) <a class="yt-timestamp" data-t="03:49:08">[03:49:08]</a>. It compiles to bytecode that runs on the JVM, enabling developers to target any computer architecture from a single codebase <a class="yt-timestamp" data-t="03:53:39">[03:53:39]</a>. While its syntax can be challenging for beginners <a class="yt-timestamp" data-t="04:01:06">[04:01:06]</a>, explicit types make code easier to understand and refactor <a class="yt-timestamp" data-t="04:06:23">[04:06:23]</a>. Modern Integrated Development Environments (IDEs) like IntelliJ can assist greatly in code generation <a class="yt-timestamp" data-t="04:10:48">[04:10:48]</a>.

### C#
Developed by Microsoft as a successor to Java, C# shares many similarities but is often more favored by its users <a class="yt-timestamp" data-t="04:14:48">[04:14:48]</a>. It's widely used for building games with Unity, as well as web and desktop applications with the .NET framework <a class="yt-timestamp" data-t="04:21:05">[04:21:05]</a>.

### [[Functional Programming with TypeScript | TypeScript]]
Another popular Microsoft tool, [[Functional Programming with TypeScript | TypeScript]] enhances [[JavaScript highlevel features | JavaScript]] by adding a type system <a class="yt-timestamp" data-t="04:29:41">[04:29:41]</a>. This makes [[JavaScript highlevel features | JavaScript]] much easier to manage in large, complex projects <a class="yt-timestamp" data-t="04:32:02">[04:32:02]</a>.

### Mobile Development Languages
For modern mobile application development, developers often work with:
*   Kotlin for Android <a class="yt-timestamp" data-t="04:37:37">[04:37:37]</a>
*   Swift for iOS <a class="yt-timestamp" data-t="04:39:10">[04:39:10]</a>
*   Dart with the [[Flutter programming languages and ecosystem | Flutter]] framework <a class="yt-timestamp" data-t="04:40:07">[04:40:07]</a>

These languages are all statically typed, offering a modern and concise approach with features like type inference to minimize boilerplate code <a class="yt-timestamp" data-t="04:42:07">[04:42:07]</a>.

### Go
Go is a high-performance language developed at Google for building [[Lowlevel systems programming languages | low-level systems]] <a class="yt-timestamp" data-t="04:50:41">[04:50:41]</a>. It was designed as a replacement for C, with Ken Thompson, one of C's original creators, contributing to its design <a class="yt-timestamp" data-t="04:54:19">[04:54:19]</a>. Go's syntax is concise and approachable for beginners, and it includes a garbage collector, eliminating the need for manual memory management common in C <a class="yt-timestamp" data-t="05:00:54">[05:00:54]</a>.

### Functional and Modern Languages
Developers often explore functional languages when seeking alternatives to large, object-oriented paradigms <a class="yt-timestamp" data-t="05:16:34">[05:16:34]</a>.

*   **F#** (F Sharp) is a functional sister language to C# developed by Microsoft <a class="yt-timestamp" data-t="05:55:07">[05:55:07]</a>. Unlike purely functional languages like Haskell, F# also supports imperative and object-oriented programming, making it more accessible to developers familiar with those styles <a class="yt-timestamp" data-t="06:00:03">[06:00:03]</a>.
*   **Scala** is a good alternative to Java, supporting both object-oriented and functional programming and running on the JVM <a class="yt-timestamp" data-t="06:08:31">[06:08:31]</a>. It is statically typed <a class="yt-timestamp" data-t="06:14:38">[06:14:38]</a>.
*   **Nim** is a high-performance language that is expressive like Python but is statically typed <a class="yt-timestamp" data-t="08:58:39">[08:58:39]</a>. It features a tunable garbage collector that can be turned off for manual memory management <a class="yt-timestamp" data-t="09:02:40">[09:02:40]</a>.
*   **Carbon** was announced by Google as a potential successor to C++ <a class="yt-timestamp" data-t="09:09:21">[09:09:21]</a>. Its unique feature is its full interoperability with existing C++ codebases <a class="yt-timestamp" data-t="09:13:30">[09:13:30]</a>.
*   **Solidity** is a statically typed, object-oriented language designed specifically for implementing smart contracts, particularly on the Ethereum blockchain <a class="yt-timestamp" data-t="09:18:27">[09:18:27]</a>.
*   **Hack**, developed by Facebook, is designed to interoperate with PHP <a class="yt-timestamp" data-t="09:26:10">[09:26:10]</a>. It was created to improve performance and add a type system to scale Facebook's original PHP-built website <a class="yt-timestamp" data-t="09:31:02">[09:31:02]</a>.