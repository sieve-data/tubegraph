---
title: Lowlevel systems programming languages
videoId: pEfrdAtAmqk
---

From: [[fireship]] <br/> 

Low-level systems programming languages delve into the deepest layers of software engineering, providing manual control over memory and hardware optimization. These languages are essential for building foundational software components like operating system kernels and compilers <a class="yt-timestamp" data-t="06:48:42">[06:48:42]</a> <a class="yt-timestamp" data-t="06:53:07">[06:53:07]</a>.

## Foundational Languages

### C
[[Learning lowerlevel programming languages like C | C]] is a legendary low-level systems language that was used to build the kernels for Windows, Mac, and Linux operating systems <a class="yt-timestamp" data-t="07:00:23">[07:00:23]</a> <a class="yt-timestamp" data-t="07:01:23">[07:01:23]</a>. Its curly brace syntax [[C influences on other programming languages | inspired many other programming languages]] <a class="yt-timestamp" data-t="07:04:19">[07:04:19]</a>. While not overly difficult to learn due to its relatively small set of keywords, effective use of C requires extensive knowledge of algorithms and computer architecture <a class="yt-timestamp" data-t="07:07:37">[07:07:37]</a> <a class="yt-timestamp" data-t="07:08:18">[07:08:18]</a> <a class="yt-timestamp" data-t="07:11:06">[07:11:06]</a>. For instance, C does not natively support hash maps or dictionaries, requiring developers to implement such data structures independently <a class="yt-timestamp" data-t="07:16:47">[07:16:47]</a> <a class="yt-timestamp" data-t="07:21:49">[07:21:49]</a>.

### C++
C++ originated as a superset of C, designed to extend it with object-oriented programming patterns like classes and inheritance <a class="yt-timestamp" data-t="07:29:13">[07:29:13]</a> <a class="yt-timestamp" data-t="07:32:02">[07:32:02]</a> <a class="yt-timestamp" data-t="07:36:11">[07:36:11]</a>. Unlike C, it is considered extremely challenging to learn due to its complexities, especially its manual memory management using pointers <a class="yt-timestamp" data-t="07:37:37">[07:37:37]</a> <a class="yt-timestamp" data-t="07:42:04">[07:42:04]</a> <a class="yt-timestamp" data-t="07:45:00">[07:45:00]</a>. Despite its steep [[Choosing the right programming language | learning curve]], C++ remains highly prolific for building optimized software like game engines and compilers <a class="yt-timestamp" data-t="07:50:41">[07:50:41]</a> <a class="yt-timestamp" data-t="07:56:06">[07:56:06]</a>.

### Rust
Rust is a modern choice for low-level programming <a class="yt-timestamp" data-t="07:59:00">[07:59:00]</a> <a class="yt-timestamp" data-t="08:01:21">[08:01:21]</a>. It does not include a garbage collector, but unlike C and C++, it employs a technique called borrow checking instead of pointers for memory management <a class="yt-timestamp" data-t="08:03:07">[08:03:07]</a> <a class="yt-timestamp" data-t="08:11:02">[08:11:02]</a>. This feature significantly simplifies writing memory-safe programs and contributes to Rust's consistent ranking as one of the most loved languages globally <a class="yt-timestamp" data-t="08:12:06">[08:12:06]</a> <a class="yt-timestamp" data-t="08:16:11">[08:16:11]</a>.

## Modern Low-Level Languages

### Go
Go is a high-performance language developed at Google for building low-level systems <a class="yt-timestamp" data-t="04:51:00">[04:51:00]</a> <a class="yt-timestamp" data-t="04:54:19">[04:54:19]</a>. It was designed as a replacement for C, with one of C's original creators, Ken Thompson, contributing to its design <a class="yt-timestamp" data-t="04:55:08">[04:55:08]</a> <a class="yt-timestamp" data-t="05:00:13">[05:00:13]</a>. Go offers a concise syntax, making it approachable for beginners, and includes a garbage collector, freeing developers from manual memory management concerns <a class="yt-timestamp" data-t="05:01:06">[05:01:06]</a> <a class="yt-timestamp" data-t="05:08:15">[05:08:15]</a>.

### V
V is a high-performance systems language that feels very similar to Go <a class="yt-timestamp" data-t="08:24:08">[08:24:08]</a> <a class="yt-timestamp" data-t="08:28:36">[08:28:36]</a>. However, unlike Go, it does not use a garbage collector, and unlike Rust, it does not employ borrow checking <a class="yt-timestamp" data-t="08:29:41">[08:29:41]</a> <a class="yt-timestamp" data-t="08:33:14">[08:33:14]</a>. V aims to create memory-safe applications through its "auto free" innovation, where the compiler automatically manages memory cleanup <a class="yt-timestamp" data-t="08:34:39">[08:34:39]</a> <a class="yt-timestamp" data-t="08:39:56">[08:39:56]</a>.

### Zig
Zig is another modern replacement for C, designed to simplify low-level programming by eliminating features like macros and meta-programming <a class="yt-timestamp" data-t="08:43:08">[08:43:08]</a> <a class="yt-timestamp" data-t="08:49:50">[08:49:50]</a>. It is very explicit about memory management and can cross-compile C and C++ code, similar to Clang <a class="yt-timestamp" data-t="08:50:54">[08:50:54]</a> <a class="yt-timestamp" data-t="08:55:18">[08:55:18]</a>.

### Nim
Nim is a high-performance language that is highly expressive, akin to Python, but is statically typed <a class="yt-timestamp" data-t="08:57:47">[08:57:47]</a> <a class="yt-timestamp" data-t="09:02:08">[09:02:08]</a>. It features a tunable garbage collector that can be entirely disabled for manual memory management <a class="yt-timestamp" data-t="09:02:37">[09:02:37]</a> <a class="yt-timestamp" data-t="09:07:56">[09:07:56]</a>.

### Carbon
Google recently announced Carbon, a language designed to be a successor to C++ <a class="yt-timestamp" data-t="09:08:48">[09:08:48]</a> <a class="yt-timestamp" data-t="09:12:00">[09:12:00]</a>. Its key feature is its full interoperability with legacy C++ codebases <a class="yt-timestamp" data-t="09:13:09">[09:13:09]</a> <a class="yt-timestamp" data-t="09:16:03">[09:16:03]</a>.

## Specialized Low-Level Languages

### Solidity
Solidity is a statically typed, object-oriented language specifically designed for implementing smart contracts, particularly on the Ethereum blockchain <a class="yt-timestamp" data-t="09:18:29">[09:18:29]</a> <a class="yt-timestamp" data-t="09:25:21">[09:25:21]</a>.

### Hack
Developed by Facebook, Hack is designed to interoperate with PHP <a class="yt-timestamp" data-t="09:26:06">[09:26:06]</a> <a class="yt-timestamp" data-t="09:28:57">[09:28:57]</a>. Facebook's original website was built with PHP, but they required a language with better performance and a type system to scale it up <a class="yt-timestamp" data-t="09:30:19">[09:30:19]</a> <a class="yt-timestamp" data-t="09:36:20">[09:36:20]</a>.

## Even Lower Levels

### C-- (C minus minus)
C-- is designed as a portable assembly language that heavily borrows from C but omits many of its features <a class="yt-timestamp" data-t="14:10:48">[14:10:48]</a> <a class="yt-timestamp" data-t="14:19:14">[14:19:14]</a>.

### [[holy_c_programming_language | Holy C]]
[[holy_c_programming_language | Holy C]] was created by Terry A. Davis and used to build TempleOS, an operating system that was written under the direction of God <a class="yt-timestamp" data-t="14:21:40">[14:21:40]</a> <a class="yt-timestamp" data-t="14:28:02">[14:28:02]</a>. It functions like C but is just-in-time compiled on the operating system, allowing it to be used like a [[scripting_and_utility_programming_languages | scripting language]] that can interact directly with the operating system kernel <a class="yt-timestamp" data-t="14:28:44">[14:28:44]</a> <a class="yt-timestamp" data-t="14:36:47">[14:36:47]</a>.

### Assembly
Assembly is a low-level language with many variations that correspond directly to the architecture of the CPU <a class="yt-timestamp" data-t="14:43:40">[14:43:40]</a> <a class="yt-timestamp" data-t="14:48:47">[14:48:47]</a>. Different CPU architectures, such as x86 and ARM, necessitate different machine code instructions <a class="yt-timestamp" data-t="14:49:28">[14:49:28]</a> <a class="yt-timestamp" data-t="14:53:23">[14:53:23]</a>. Assembly enables representation of this code with simple commands that manipulate values on the CPU's registers <a class="yt-timestamp" data-t="14:54:11">[14:54:11]</a> <a class="yt-timestamp" data-t="14:59:43">[14:59:43]</a>.

### Machine Code
One level below Assembly is machine code, which consists of ones and zeros (raw binary), typically represented in hexadecimal format <a class="yt-timestamp" data-t="15:01:13">[15:01:13]</a> <a class="yt-timestamp" data-t="15:08:44">[15:08:44]</a>. Coding at this level requires an intimate knowledge of the computer's architecture and the ability to count in binary <a class="yt-timestamp" data-t="15:09:47">[15:09:47]</a> <a class="yt-timestamp" data-t="15:15:03">[15:15:03]</a>.

### Transistors and Logic Gates
Beyond machine code, the lowest level involves billions of transistors on a CPU <a class="yt-timestamp" data-t="15:16:04">[15:16:04]</a> <a class="yt-timestamp" data-t="15:21:49">[15:21:49]</a>. A single transistor represents one bit (a one or zero) by controlling the flow of electricity through a piece of silicon <a class="yt-timestamp" data-t="15:21:49">[15:21:49]</a> <a class="yt-timestamp" data-t="15:27:03">[15:27:03]</a>. To perform useful functions, transistors are organized into logic gates like NOT, AND, OR, and XOR <a class="yt-timestamp" data-t="15:28:16">[15:28:16]</a> <a class="yt-timestamp" data-t="15:34:36">[15:34:36]</a>. These simple logic chunks perform the "miracle" of taking electricity as input to produce other electricity as output, doing so billions of times per second globally <a class="yt-timestamp" data-t="15:36:20">[15:36:20]</a> <a class="yt-timestamp" data-t="15:45:00">[15:45:00]</a>.