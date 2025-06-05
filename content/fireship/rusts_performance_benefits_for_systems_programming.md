---
title: Rusts performance benefits for systems programming
videoId: 5C_HPTJg5ek
---

From: [[fireship]] <br/> 

Rust is a compiled programming language that aims to provide high-level simplicity alongside low-level performance <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. It is a popular choice for building systems where performance is absolutely critical <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>.

## Applications in Performance-Critical Systems

Rust is well-suited for developing applications requiring high performance, such as:
*   [[lowlevel_systems_programming_languages | Game engines]] <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>
*   Databases <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>
*   [[lowlevel_systems_programming_languages | Operating systems]] <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>
It is also an excellent choice when targeting WebAssembly <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>.

## Memory Management for Performance

Traditional high-level languages often use a garbage collector, which can reduce control over memory management <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. In contrast, Rust has no garbage collector <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>. Instead, it achieves [[memory_safety_and_ownership_concepts_in_rust | memory safety]] and performance through the concepts of [[memory_safety_and_ownership_concepts_in_rust | ownership and borrowing]] <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>:

*   **Immutability and Stack Memory**
    By default, every variable in Rust is immutable <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. This design allows values to be stored in stack memory, which has minimal performance overhead <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.
*   **Heap Memory for Dynamic Data**
    Mutable values or objects with an unknown size at compile time are stored in heap memory <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.
*   **Ownership**
    Every value in a Rust program is assigned to a single variable, known as its owner <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. When the owner variable goes out of scope, the memory allocated to it is automatically deallocated <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.
*   **Borrowing**
    [[memory_safety_and_ownership_concepts_in_rust | Borrowing]] allows different parts of the program to access a reference in memory without taking [[memory_safety_and_ownership_concepts_in_rust | ownership]] of it <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.
*   **Borrow Checker**
    A set of rules governs the [[memory_safety_and_ownership_concepts_in_rust | ownership and borrowing]] system, which are validated by the Rust borrow checker at compile time <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>. These rules ensure code safety while maintaining absolute control over performance <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.

## Development and Compilation

Rust includes [[cargo_package_manager_and_rust_project_setup | Cargo]], its package manager, where each package is referred to as a crate <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>. The [[rust standard library and compile process | Rust standard library]] contains modules for IO, the file system, concurrency, and other functionalities <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>. Code is compiled into an executable using the Rust compiler <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>, resulting in a memory-safe executable capable of handling the most performance-intensive system requirements <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.