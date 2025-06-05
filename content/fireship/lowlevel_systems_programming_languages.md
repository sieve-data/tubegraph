---
title: Lowlevel systems programming languages
videoId: pEfrdAtAmqk
---

From: [[fireship]] <br/> 

Low-level systems languages are designed for manual memory management and optimization <a class="yt-timestamp" data-t="06:48:00">[06:48:00]</a>. They are commonly used to build operating system kernels and compilers, which are essential for other higher-level languages to function <a class="yt-timestamp" data-t="06:53:00">[06:53:00]</a>. These languages operate closer to the hardware, offering fine-grained control over system resources.

## Core Systems Languages

### C
C is a legendary language used to build operating system kernels such as Windows, Mac, and Linux <a class="yt-timestamp" data-t="07:00:00">[07:00:00]</a>. Its curly brace syntax has inspired many other [[programming_languages_and_their_execution_models | programming languages]] <a class="yt-timestamp" data-t="07:04:00">[07:04:00]</a>. While its keyword set is relatively small, effectively using C requires extensive knowledge of algorithms and computer architecture <a class="yt-timestamp" data-t="07:07:00">[07:07:00]</a>. For instance, C does not natively include hash maps or dictionaries, requiring developers to implement such data structures themselves <a class="yt-timestamp" data-t="07:16:00">[07:16:00]</a>. C was considered the perfect [[programming_software | programming language]] upon its release in 1969, but it only supported procedural programming <a class="yt-timestamp" data-t="07:22:00">[07:22:00]</a>.

### C++
Originally a superset of C, C++ was designed to extend C with object-oriented programming patterns like classes and inheritance <a class="yt-timestamp" data-t="07:29:00">[07:29:00]</a>. Unlike C, C++ is notoriously difficult to learn due to its complex features and manual memory management with pointers <a class="yt-timestamp" data-t="07:37:00">[07:37:00]</a>. Despite its steep learning curve, C++ is a highly prolific language, used to build highly optimized software like game engines and compilers <a class="yt-timestamp" data-t="07:51:00">[07:51:00]</a>.

### Rust
Rust is a modern choice for low-level programming that does not have a garbage collector <a class="yt-timestamp" data-t="08:00:00">[08:00:00]</a>. Instead of pointers, Rust uses a technique called "borrow checking" for memory management, which makes it easier to write memory-safe programs <a class="yt-timestamp" data-t="08:05:00">[08:05:00]</a>. Rust consistently ranks as one of the most loved languages in the world <a class="yt-timestamp" data-t="08:13:00">[08:13:00]</a>.

## Modern Low-Level Languages

### Go
Developed at Google, Go is a high-performance language designed for building low-level systems <a class="yt-timestamp" data-t="04:51:00">[04:51:00]</a>. It was created as a replacement for C, with Ken Thompson, one of C's original creators, contributing to its design <a class="yt-timestamp" data-t="04:54:00">[04:54:00]</a>. Go has a concise syntax, making it approachable for beginners, and includes a garbage collector, freeing developers from manual memory management <a class="yt-timestamp" data-t="05:00:00">[05:00:00]</a>.

### V
V is a high-performance systems language that shares similarities with Go <a class="yt-timestamp" data-t="08:24:00">[08:24:00]</a>. Unlike Go, it does not use a garbage collector, and unlike Rust, it does not perform borrow checking <a class="yt-timestamp" data-t="08:29:00">[08:29:00]</a>. V aims to create memory-safe applications through its "auto-free" innovation, where the compiler handles memory cleanup <a class="yt-timestamp" data-t="08:33:00">[08:33:00]</a>.

### Zig
Zig is a modern replacement for C, designed to simplify low-level programming by eliminating features like macros and meta-programming <a class="yt-timestamp" data-t="08:43:00">[08:43:00]</a>. It is explicit about memory management and can cross-compile C and C++ code, similar to Clang <a class="yt-timestamp" data-t="08:51:00">[08:51:00]</a>.

### Nim
Nim is a high-performance language known for being expressive like [[popular_dynamic_and_highlevel_programming_languages | Python]] while being statically typed <a class="yt-timestamp" data-t="08:57:00">[08:57:00]</a>. It features a tunable garbage collector that can be entirely disabled for manual memory management <a class="yt-timestamp" data-t="09:02:00">[09:02:00]</a>.

### Carbon
Announced by Google, Carbon is designed to be a successor to C++ <a class="yt-timestamp" data-t="09:08:00">[09:08:00]</a>. Its key feature is full interoperability with existing C++ codebases <a class="yt-timestamp" data-t="09:12:00">[09:12:00]</a>.

### Solidity
Solidity is a statically typed, object-oriented language specifically designed for implementing smart contracts, particularly on the Ethereum blockchain <a class="yt-timestamp" data-t="09:18:00">[09:18:00]</a>.

### C--
C-- is designed as a portable assembly language that borrows heavily from C but omits many of its features <a class="yt-timestamp" data-t="14:11:00">[14:11:00]</a>.

### Holy C
Holy C, created by Terry A. Davis, was used to build TempleOS, an operating system developed under the direction of God <a class="yt-timestamp" data-t="14:21:00">[14:21:00]</a>. Holy C functions like C but is just-in-time compiled on the operating system, allowing it to be used as a scripting language that can interact directly with the operating system kernel <a class="yt-timestamp" data-t="14:28:00">[14:28:00]</a>.

## Deepest Levels of Computing

### Assembly
Assembly is a low-level language with many variations corresponding directly to the architecture of the CPU <a class="yt-timestamp" data-t="14:43:00">[14:43:00]</a>. Different CPU architectures, such as x86 and ARM, require different machine code instructions <a class="yt-timestamp" data-t="14:49:00">[14:49:00]</a>. Assembly allows representation of this code with simple commands that manipulate values on the CPU's registers <a class="yt-timestamp" data-t="14:55:00">[14:55:00]</a>.

### Machine Code
Below Assembly, machine code consists of ones and zeros, or raw binary, often represented in hexadecimal format <a class="yt-timestamp" data-t="15:01:00">[15:01:00]</a>. Coding at this level requires intimate knowledge of the computer's architecture and the ability to count in binary <a class="yt-timestamp" data-t="15:09:00">[15:09:00]</a>.

### Transistors and Logic Gates
Beyond machine code lies the physical realm of billions of transistors on a CPU <a class="yt-timestamp" data-t="15:16:00">[15:16:00]</a>. A single transistor represents one bit (a one or a zero) by controlling the amount of electricity flowing through a piece of silicon <a class="yt-timestamp" data-t="15:20:00">[15:20:00]</a>. To perform useful operations, transistors are organized into logic gates (e.g., NOT, AND, OR, Exclusive OR) <a class="yt-timestamp" data-t="15:28:00">[15:28:00]</a>. These fundamental logic chunks perform the "miracle" of taking electricity as input to produce other electricity as output, billions of times per second <a class="yt-timestamp" data-t="15:35:00">[15:35:00]</a>. This forms the basis of all modern computing, allowing for activities like playing video games online <a class="yt-timestamp" data-t="15:45:00">[15:45:00]</a>.

### Quantum Electrodynamics
Even deeper, understanding the behavior of particles in the electromagnetic quantum vacuum, a field known as quantum electrodynamics, could potentially lead to building next-generation, blazingly fast quantum computers <a class="yt-timestamp" data-t="15:50:00">[15:50:00]</a>.