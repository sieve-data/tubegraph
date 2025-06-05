---
title: Introduction to Assembly Language
videoId: 4gwYkEK0gOk
---

From: [[fireship]] <br/> 

[[Lowlevel systems programming languages | Assembly Language]] is a [[lowlevel_systems_programming_languages | low-level programming language]] designed to simplify the instructions fed into a computer's CPU <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. It serves as a human-readable abstraction layer on top of machine code, eliminating the need for programmers to manually count ones and zeros <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>.

## [[History and Evolution of Assembly Language | History and Evolution]]

The first [[History and Evolution of Assembly Language | Assembly Language]] was created in 1947 by Kathleen Booth for the All-purpose Electronic Computer (APE(X)C) <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. Over the subsequent decade, it evolved into various formats to power the supercomputers of that era, such as the IBM 790, which had an approximate price tag of $20 million in today's currency <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. Writing code in assembly remained the standard practice until the emergence of [[C language characteristics and usage | high-level languages]] like Fortran a few years later <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.

## [[Uses and Applications of Assembly Language Today | Current Uses]]

Despite the rise of [[C language characteristics and usage | high-level languages]], assembly is still utilized today for:
*   Direct access to bare-metal hardware <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.
*   Addressing [[lowlevel_systems_programming_languages | low-level]] performance issues <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.
*   Development of device drivers and embedded systems <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.
*   Running native software in a web browser via WebAssembly <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.

A key characteristic of [[Assembly Language]] is its dependency on specific CPU architectures; for instance, ARM is used for Apple Silicon and Raspberry Pi, while x86 is for Intel chips <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.

To begin, you will need an assembler, such as the Netwide Assembler (NASM) for x86 chips <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.

## [[Assembly Language Structure and Syntax | Structure and Syntax]]

An [[Assembly Language]] program is typically divided into three main sections <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>:

*   **Text Section**: Contains the actual logic of the program <a class="yt-timestamp" data-t="01:01:00">[01:01:00]</a>. By convention, it includes an entry point labeled `start`, where code execution begins <a class="yt-timestamp" data-t="01:01:04">[01:01:04]</a>.
*   **Block Starting Symbol Section (BSS)**: Holds variables that may change throughout the application's lifecycle <a class="yt-timestamp" data-t="01:10:00">[01:10:00]</a>.
*   **Data Section**: Used to initialize constants or data that do not change <a class="yt-timestamp" data-t="01:14:00">[01:14:00]</a>.

### Declaring Constants

To declare a constant, such as a string, you start with a label and use `DB` (Define Byte) to place the string into memory <a class="yt-timestamp" data-t="01:18:00">[01:18:00]</a>. For example, `hello: DB 'Hello World'` places the "Hello World" string into memory <a class="yt-timestamp" data-t="01:21:00">[01:21:00]</a>. To print it to standard output, its length is also needed. The `equate` directive can convert a symbol into a constant <a class="yt-timestamp" data-t="01:31:00">[01:31:00]</a>. Using a dollar sign (`$`) to subtract the current position from the label provides the string's length, e.g., `helloLen EQU $ - hello` <a class="yt-timestamp" data-t="01:33:00">[01:33:00]</a>. These constants can then be referenced from the `start` label in the main program <a class="yt-timestamp" data-t="01:38:00">[01:38:00]</a>.

### Instructions and Registers

Each line of code in [[Assembly Language]] consists of an instruction along with one or more operands <a class="yt-timestamp" data-t="01:40:00">[01:40:00]</a>. There are hundreds of built-in instructions <a class="yt-timestamp" data-t="01:44:00">[01:44:00]</a>.

To perform operations quickly, the CPU uses a limited number of registers, which are 64-bit chunks of memory built directly into the CPU, as opposed to RAM <a class="yt-timestamp" data-t="01:47:00">[01:47:00]</a>. Data can be inserted into a register using the `move` instruction, specifying the register name and the data to store <a class="yt-timestamp" data-t="01:56:00">[01:56:00]</a>. For instance, on [[Introduction to Linux | Linux]], `move RAX, 1` is used for the "system write" operation <a class="yt-timestamp" data-t="02:03:00">[02:03:00]</a>. To specify where to write, `move RDI, 1` directs output to the standard output in the terminal <a class="yt-timestamp" data-t="02:06:00">[02:06:00]</a>. Other registers store the message to write and its length <a class="yt-timestamp" data-t="02:14:00">[02:14:00]</a>. To execute the code, the operating system kernel is called <a class="yt-timestamp" data-t="02:17:00">[02:17:00]</a>. Before exiting, the `RAX` register should be updated with `60` for "system exit", and an error code of `0` should be provided for a successful exit <a class="yt-timestamp" data-t="02:21:00">[02:21:00]</a>.

## [[Compilation and Execution Process in Assembly Language | Compilation and Execution]]

After writing the code, use an assembler to compile or assemble it into an object file <a class="yt-timestamp" data-t="02:28:00">[02:28:00]</a>. Then, use a linker to convert the object file into the final executable program <a class="yt-timestamp" data-t="02:32:00">[02:32:00]</a>.