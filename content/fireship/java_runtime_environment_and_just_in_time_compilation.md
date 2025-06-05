---
title: Java runtime environment and just in time compilation
videoId: l9AzO1FMgM8
---

From: [[fireship]] <br/> 

Java is a high-level, multi-paradigm programming language renowned for its capacity to compile to platform-independent bytecode <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. It was originally designed by James Gosling in 1990 at Sun Microsystems <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>.

## The Java Virtual Machine (JVM) and Bytecode

What made Java innovative was its approach to compilation and execution <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>. Unlike languages such as C or C++, which compile directly to machine code, Java compiles to bytecode <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. This bytecode can then run on any operating system without the need for recompilation <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. This [[java_virtual_machine_and_platform_independence | platform independence]] is achieved by executing the code using the [[java_virtual_machine_and_platform_independence | Java Virtual Machine (JVM)]] <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.

Java is unique in that it functions as both a compiled and an interpreted language simultaneously <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

## The Java Runtime Environment (JRE)

To run Java applications, a computer simply needs to have the [[java_virtual_machine_and_platform_independence | Java Runtime Environment (JRE)]] installed <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>, which is common on most systems <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. For developers, this characteristic enables the principle of "write once, run anywhere" <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.

> [!INFO] Development vs. Runtime
> While the JRE is sufficient for running Java programs, developers need the [[how_to_create_and_run_a_basic_java_program | Java Development Kit (JDK)]] to create them <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.

## Compilation and Execution Process

The process of [[compilation_and_execution_process_in_assembly_language | compiling and executing]] a Java program involves a few key steps:
1.  **Compilation to Bytecode**: Once a Java program is finished, a compiler is used to generate a `.class` file <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>. This file contains the bytecode <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.
2.  **Execution by JVM**: The `java` command is then used to instruct the [[java_virtual_machine_and_platform_independence | JVM]] to interpret and run this `.class` file <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>.

This dual nature (compiled to bytecode, then interpreted/executed by the JVM, which often includes Just-In-Time compilation) allows Java to achieve its powerful [[java_virtual_machine_and_platform_independence | platform independence]] while also offering performance benefits.