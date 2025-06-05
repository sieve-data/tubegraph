---
title: Compilation and Execution Process in Assembly Language
videoId: 4gwYkEK0gOk
---

From: [[fireship]] <br/> 

[[introduction_to_assembly_language | Assembly language]] is a low-level programming language designed to simplify the instructions fed into a computer's CPU, acting as a human-readable abstraction over machine code <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This means programmers do not have to manually count ones and zeros <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>.

## Prerequisites for Compilation

A crucial aspect of [[introduction_to_assembly_language | Assembly Language]] is its architecture-specific nature: each [[introduction_to_assembly_language | Assembly Language]] only functions on a particular CPU architecture <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>. Examples include ARM for Apple silicon and Raspberry Pi, or x86 for Intel chips <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. To begin the process, an assembler is required, such as the Netwide Assembler (NASM) for x86 chips <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.

## [[assembly_language_structure_and_syntax | Structure of an Assembly Program]]

An [[introduction_to_assembly_language | Assembly Language]] program is typically organized into three distinct sections <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>:

*   **Text Section**: This section holds the actual logic of the program <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. By convention, it includes an entry point named `start`, which marks where the code execution begins <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.
*   **Block Starting Symbol Section (BSS)**: This section contains variables that may change throughout the application's lifecycle <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.
*   **Data Section**: Here, constants or data that do not change during the program's execution are initialized <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.

### Declaring Constants

To declare a constant, such as a string, a label is used, followed by `DB` (Define Byte) to place the data into memory <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>. For example, to print "hello world" to standard output, its length is also needed <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>. The `equate` directive can convert a symbol into a constant <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>. Using a dollar sign (`$`) can subtract the current position from a label, effectively providing the string's length <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>. These constants can then be referenced from the `start` label in the main program <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.

## Program Logic and System Interaction

Each line of [[introduction_to_assembly_language | Assembly Language]] code consists of an instruction accompanied by one or more operands <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. The language includes hundreds of built-in instructions <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>.

To perform operations quickly, the CPU utilizes a limited number of registers, which are 64-bit chunks of memory built directly into the CPU itself, distinct from RAM <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. Data can be inserted into a register using the `move` instruction, by specifying the register name and the data to store <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>. For instance, `number one` corresponds to `system write` on Linux <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>. To specify where to write, `one` is moved into the `RDI` register, which corresponds to the standard output in the terminal <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>. Other registers store the message to write and its length <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>.

To execute the code, the program calls the operating system kernel <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>. Before exiting, the `RX` register must be updated with `60` for a system exit, and an error code of `zero` provided for a successful termination <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>. Failing to do so can result in a segmentation fault <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.

## The Compilation and Execution Process

The final steps involve transforming the assembly code into an executable file:

1.  **Assembly**: The assembler is used to *compile* or *assemble* the code into an object file <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>.
2.  **Linking**: A linker then converts this object file into the final executable program <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.

This process transforms the human-readable assembly instructions into the machine code that the CPU can directly execute.