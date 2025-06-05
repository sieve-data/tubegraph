---
title: Assembly Language Structure and Syntax
videoId: 4gwYkEK0gOk
---

From: [[fireship]] <br/> 

[[introduction_to_assembly_language | Assembly language]] is a low-level programming language designed to simplify the instructions fed into a computer CPU, serving as a human-readable abstraction on top of machine code so programmers don't have to manually count ones and zeros <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>.

## History
The first [[history_and_evolution_of_assembly_language | Assembly Language]] was created by Kathleen Booth in 1947 for the All-Purpose Electronic Computer <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. Over the subsequent decade, it evolved into various formats to power early supercomputers like the IBM 790, which cost $20 million in today's dollars <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. Writing code in [[introduction_to_assembly_language | Assembly]] was standard practice until the emergence of high-level languages like Fortran a few years later <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.

## Modern Uses
Despite the rise of higher-level languages, [[introduction_to_assembly_language | Assembly]] is still used today for several specific purposes <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>:
*   Direct access to bare-metal hardware <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.
*   Addressing low-level performance issues, particularly in device drivers and embedded systems <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.
*   Running native software in a web browser via WebAssembly <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.

## Architecture Specificity
A key characteristic of [[introduction_to_assembly_language | Assembly Language]] is that each language typically works only on a specific CPU [[differences_between_arm_and_x86_architectures | architecture]] <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>. Examples include:
*   [[differences_between_arm_and_x86_architectures | ARM]] for Apple silicon and Raspberry Pi <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.
*   [[differences_between_arm_and_x86_architectures | x86]] for Intel chips <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.

To begin programming in [[introduction_to_assembly_language | Assembly]], an assembler, such as the Netwide Assembler for [[differences_between_arm_and_x86_architectures | x86]] chips, is required <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.

## Program Structure
An [[introduction_to_assembly_language | assembly]] program is typically divided into three main sections <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>:

### Text Section
This section contains the actual logic for the program <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. By convention, it includes an entry point called `start`, which is where the code execution begins <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.

### Block Starting Symbol (BSS) Section
The BSS section holds variables that may change throughout the application's lifecycle <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.

### Data Section
This section is used to initialize constants or data that will not change during the program's execution <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.

## Basic Syntax and Features

### Declaring Constants
To declare a constant, such as a string, one starts with a label <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>. The `DB` (Define Byte) directive is then used to place the string into memory <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.

For example, to declare a "hello world" string and its length:
```assembly
hello: DB 'hello world'
hello_len: EQU $ - hello
```
The `EQU` directive converts a symbol into a constant <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>. The `$` symbol subtracts the current position from the `hello` label, thereby providing the length of the string <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>. These defined constants can then be referenced from the `start` label in the main program <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.

### Instructions and Operands
Each line of code in [[introduction_to_assembly_language | assembly]] contains an instruction along with one or more operands <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. There are hundreds of built-in instructions <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>.

### Registers
To perform operations quickly, the CPU has a limited number of registers <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. These are like 64-bit chunks of memory built directly into the CPU, as opposed to RAM <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.

Data can be inserted into a register using the `move` instruction, providing operands for the register name and the data to store <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>.

**Example of using registers for system calls (Linux):**
*   **System Write:** To perform a system write on Linux, the number `1` is used, which corresponds to this operation <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>. This value is moved into the `RAX` register.
*   **Standard Output:** To specify where to write, `1` is moved into the `RDI` register, which corresponds to the standard output in the terminal <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.
*   **Message and Length:** Another register stores the message to write along with its length <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>.
*   **Calling Kernel:** To execute the code, the operating system kernel is called <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.
*   **System Exit:** Before the program finishes, the `RAX` register is updated with `60` for `system exit`, and an error code of `0` is provided for a successful execution <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.

### Compilation and Execution
After writing the code, an assembler is used to compile or assemble it into an object file <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>. Subsequently, a linker is used to convert the object file into the final executable <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.