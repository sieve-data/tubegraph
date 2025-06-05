---
title: JavaScript event loop and asynchronous programming
videoId: FSs_JYwnAdI
---

From: [[fireship]] <br/> 

JavaScript is characterized as a high-level, single-threaded, garbage-collected, interpreted or just-in-time compiled, prototype-based, multi-paradigm, dynamic language with a non-blocking [[understanding_the_event_loop | event loop]] concurrency model <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. While JavaScript is based on the ECMAScript (ECMA 262) specification <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>, this specification doesn't dictate how the language should be implemented or how memory should be managed, nor does it mention the [[understanding_the_event_loop | event loop]] <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>. These implementation details are handled by browser vendors, with popular examples including Mozilla's SpiderMonkey and Google's V8 engines <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.

## High-Level Programming Language
[[JavaScript singlethreaded nature | JavaScript]] is considered a high-level programming language <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a> because it provides a significant degree of abstraction and simplification over a computer's hardware <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>. Unlike low-level languages like machine code or assembly, JavaScript developers don't typically need to concern themselves with details like manual memory allocation <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. It simplifies development through abstractions such as garbage collectors and dynamic typing <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.

## Interpreted and Just-In-Time Compiled
JavaScript is an interpreted language <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>, meaning it requires an interpreter in the environment (like a web browser) to read and execute its source code directly, one instruction at a time <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>. This differs from compiled languages (e.g., Java or C), which statically analyze and compile all code into a binary executable before running <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>.

Modern JavaScript engines, like V8, employ **just-in-time (JIT) compilation** <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>. V8 compiles JavaScript code down to native machine code before execution, rather than merely interpreting bytecode line by line <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>. This JIT compilation significantly improves performance in browsers and Node.js environments <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>.

## Memory Allocation: Call Stack and Heap
When executing JavaScript code, two primary regions of memory are allocated: the **call stack** and the **heap** <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>.

### Call Stack
The call stack is a high-performance, continuous region of memory used to execute [[JavaScript function basics and anatomy | JavaScript functions]] <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>.
*   When a function is called, a "frame" is created on the call stack. This frame contains a copy of the function's local variables <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>.
*   If a function calls another function, a new frame is added on top of the current one <a class="yt-timestamp" data-t="00:05:59">[00:05:59]</a>.
*   When a function returns, its frame is "popped off" the stack <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.
*   An example of a `console.log` operation shows it's pushed onto the stack, executed, and immediately popped off <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>.
*   If a function never returns (e.g., an infinitely recursive function), it can lead to a "call stack size exceeded" error <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.

### Heap
The heap is a mostly unstructured memory pool used to store things like objects or primitive values within closures <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>. Unlike the call stack, the heap is garbage-collected <a class="yt-timestamp" data-t="00:07:52">[00:07:52]</a>. This means the JavaScript runtime (e.g., V8) automatically clears up memory when it's no longer referenced by the code, eliminating the need for manual memory allocation and deallocation like in C <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>.

## [[JavaScript singlethreaded nature | JavaScript's Single-Threaded Nature]]
[[JavaScript singlethreaded nature | JavaScript]] is a single-threaded language <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>, meaning it can only perform one computation at a time <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>. If a long-running synchronous task, such as an infinite `while` loop, is executed, it will block the single thread, preventing any other operations or event captures in that browser tab <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>. This can cause the browser tab to use close to 100% of the CPU core's resources <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>.

## The [[understanding_the_event_loop | Event Loop]] and [[asynchronous_programming_in_javascript | Asynchronous Programming]]
To handle long-running tasks without blocking the single thread, JavaScript utilizes the [[understanding_the_event_loop | event loop]] <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>.

### How the [[understanding_the_event_loop | Event Loop]] Works
At its core, the [[understanding_the_event_loop | event loop]] is a `while` loop that continuously waits for messages from a queue and then processes their synchronous instructions to completion <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>.
*   When a user interacts with a web page (e.g., clicking a button), an event listener sends a message to the queue <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a>.
*   The runtime then processes the JavaScript defined as the callback for that event <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>.
*   This mechanism makes JavaScript **non-blocking** <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a> because it's always listening for events and handling callbacks rather than waiting for a function's return value <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>. It only waits for the CPU to process synchronous code, which typically happens on a microsecond scale <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>.

### Execution Order
In each iteration, the [[understanding_the_event_loop | event loop]] first handles all synchronous code in the script <a class="yt-timestamp" data-t="00:08:59">[00:08:59]</a>. After synchronous code finishes, it checks if there are any messages or callbacks in the queue ready for execution <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>.

For instance, a `setTimeout` with a 0-second delay will not execute first, even if placed at the top of the script <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>. The [[understanding_the_event_loop | event loop]] will only get to it after it has completed the initial synchronous code execution <a class="yt-timestamp" data-t="00:09:19">[00:09:19]</a>.

This design allows for offloading long-running jobs, such as HTTP calls in a browser or file system interactions in Node.js, to separate thread pools without blocking the main JavaScript thread <a class="yt-timestamp" data-t="00:09:26">[00:09:26]</a>.

### Microtask Queue (for [[using_promises_for_asynchronous_operations | Promises]])
With the introduction of [[using_promises_for_asynchronous_operations | Promises]], JavaScript added a **microtask queue** <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a>. The microtask queue has priority over the main task queue, which is used for DOM APIs and `setTimeout` <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>.

This means that within an [[understanding_the_event_loop | event loop]] iteration:
1.  Synchronous code is handled first <a class="yt-timestamp" data-t="00:10:13">[00:10:13]</a>.
2.  Then, any ready callbacks from [[using_promises_for_asynchronous_operations | Promises]] (in the microtask queue) are handled <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>.
3.  Lastly, callbacks from `setTimeout` or DOM APIs (in the main task queue) are executed <a class="yt-timestamp" data-t="00:10:19">[00:10:19]</a>.

Understanding these underlying computer science concepts can provide a deeper insight into how [[asyncawait_in_javascript | asynchronous programming]] works in [[Asynchronous programming and event loop in JavaScript | JavaScript]] <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>.