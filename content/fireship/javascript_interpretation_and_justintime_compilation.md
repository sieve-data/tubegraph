---
title: JavaScript interpretation and justintime compilation
videoId: FSs_JYwnAdI
---

From: [[fireship]] <br/> 
[[JavaScript interpretation and justintime compilation | JavaScript]] is known for being an interpreted or just-in-time compiled language <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. Understanding these characteristics is key to grasping how [[JavaScript highlevel features | JavaScript]] works within a computer system <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.

### Interpreted vs. Compiled Languages

There are two primary methods to translate code written in a programming language into instructions that a CPU can execute: interpretation and compilation <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>.

*   **Interpreted Languages**: [[JavaScript interpretation and justintime compilation | JavaScript]] is fundamentally an interpreted language <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>. This means it requires an interpreter within its environment to read and execute the source code directly <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>. The interpreter translates and executes instructions one by one, immediately <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>. This can be demonstrated by running [[JavaScript fundamentals and practical concepts | JavaScript]] code directly in a browser's console <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>.
*   **Compiled Languages**: In contrast, a compiled language like Java or C statically analyzes all code in advance <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>. It then compiles the entire code down to a binary file that can be executed directly on the machine <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>. Once compiled, the binary can run without the compiler present <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.

While [[JavaScript interpretation and justintime compilation | JavaScript]] was not initially designed as a compiled language <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>, modern [[JavaScript frameworks and their updates | JavaScript engines]] utilize features of a compiler to enhance performance <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.

### Just-In-Time (JIT) Compilation

Modern [[JavaScript trends and frameworks | JavaScript engines]] like Mozilla's SpiderMonkey and Google's V8 incorporate a technique called just-in-time (JIT) compilation <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>.

*   **How JIT Works**: In the case of V8, it compiles [[JavaScript fundamentals and practical concepts | JavaScript]] code down to native machine code *before* running it <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>. This differs from a traditional interpreter that would interpret bytecode line by line <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.
*   **Performance Improvement**: The JIT compiler in these [[JavaScript frameworks and their updates | JavaScript engines]] significantly improves performance in browsers and environments like Node.js <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>. This compilation process does not fundamentally change how developers write their [[JavaScript fundamentals and practical concepts | JavaScript]] code <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.

The characteristics of [[JavaScript interpretation and justintime compilation | JavaScript]], such as being a high-level, interpreted, dynamically typed, multi-paradigm, prototype-based, [[JavaScript singlethreaded nature | single-threaded]], garbage-collected, and non-blocking language with an event loop, contribute to its flexibility and how it's implemented by browser vendors <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>. While the ECMAScript specification outlines how [[JavaScript interpretation and justintime compilation | JavaScript]] is laid out, it doesn't specify memory management or the event loop, leaving these details to engine implementations like V8 and SpiderMonkey <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.