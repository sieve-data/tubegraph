---
title: Memory safety and ownership concepts in Rust
videoId: 5C_HPTJg5ek
---

From: [[fireship]] <br/> 

Rust is a memory-safe, compiled programming language that combines high-level simplicity with low-level performance <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. It is a popular choice for building systems where [[rusts_performance_benefits_for_systems_programming | performance]] is critical, such as game engines, databases, or operating systems <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. Rust also serves as an excellent choice when targeting web assembly <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>.

Traditional high-level languages often use a garbage collector, which limits direct control over [[memory_management_in_c | memory management]] <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. In contrast, lower-level languages, like [[c_language_characteristics_and_usage | C]], provide explicit functions such as `free` and `allocate`, which can be prone to errors <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. Rust takes a unique approach: it operates without a garbage collector but achieves memory safety through the concepts of ownership and borrowing <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.

## Immutability by Default

By default, every variable in Rust is immutable <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. This design choice allows values to be stored in stack memory, which incurs minimal performance overhead <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. However, mutable values or objects whose size is unknown at compile time are stored in heap memory <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>. To declare a mutable variable, the `mut` keyword must be added <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.

## Ownership

In a Rust program, every value is assigned to a single variable, which is known as its *owner* <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. When that owner variable goes out of scope, the memory allocated to it is automatically dropped <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>. This automatic memory management, without a garbage collector, is a core aspect of Rust's memory safety <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.

## Borrowing

While ownership ensures memory safety, there are cases where different parts of a program may need to access a value without taking ownership. This is where *borrowing* comes in <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>. Borrowing allows access to a reference in memory without acquiring ownership of it <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>. A reference to a variable's memory location can be borrowed by prefixing it with an ampersand (`&`) <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.

## The Borrow Checker

Rust implements a sophisticated system with numerous rules to govern ownership and borrowing <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. These rules are validated at [[rust_standard_library_and_compile_process | compile]] time by the Rust *Borrow Checker* <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>. The Borrow Checker ensures code safety while providing absolute control over performance <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.

### Practical Application

To get started with Rust, one can install Rust and then use the [[cargo_package_manager_and_rust_project_setup | Cargo package manager]] by running `cargo new` from the command line <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>. Within the `main.rs` file, the program execution begins in the `main` function <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>. Variables are declared using `let`, followed by their name and type <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>. For example, to print a value, a macro like `println!` can be used to log it to the standard output <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>. After writing code, it can be compiled into an executable using the [[rust_standard_library_and_compile_process | Rust compiler]] <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.

Rust's approach allows for the creation of memory-safe executables capable of handling the most performance-intensive system requirements <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.