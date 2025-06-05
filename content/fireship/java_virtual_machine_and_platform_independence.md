---
title: Java virtual machine and platform independence
videoId: l9AzO1FMgM8
---

From: [[fireship]] <br/> 

Java is a high-level, multi-paradigm programming language renowned for its ability to compile to platform-independent bytecode <a class="yt-timestamp" data-t="00:00:00"></a>. This innovation means that unlike languages like [[c_influences_on_other_programming_languages | C]] or C++, Java compiles to bytecode that can execute on any operating system without the need for recompilation <a class="yt-timestamp" data-t="00:00:30"></a>.

## How Platform Independence is Achieved

The platform independence of Java is primarily made possible by the **Java Virtual Machine (JVM)** <a class="yt-timestamp" data-t="00:00:39"></a>.

*   **Bytecode Generation**: When a Java program is finished, a compiler is used to generate a class file, which contains the bytecode <a class="yt-timestamp" data-t="02:00:00"></a>.
*   **JVM's Role**: The JVM is responsible for interpreting and running this bytecode <a class="yt-timestamp" data-t="02:05:00"></a>. It acts as an abstraction layer between the compiled bytecode and the underlying hardware or operating system.
*   **Compiled and Interpreted**: Java is considered both a compiled and an interpreted language simultaneously <a class="yt-timestamp" data-t="00:00:44"></a>.

## Java Runtime Environment (JRE)

For a computer to run Java bytecode, it only needs to have the [[java_runtime_environment_and_just_in_time_compilation | Java Runtime Environment]] (JRE) installed <a class="yt-timestamp" data-t="00:00:48"></a>. Most computers already have the JRE <a class="yt-timestamp" data-t="00:00:50"></a>.

## Write Once, Run Anywhere

For developers, this architecture embodies the principle of "write once, run anywhere" <a class="yt-timestamp" data-t="00:00:52"></a>. This means a single compiled Java program can be executed on diverse platforms (e.g., Windows, macOS, Linux) without modifications, as long as a compatible JVM is available on that platform.