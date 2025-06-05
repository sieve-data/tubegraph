---
title: JavaScript memory management and garbage collection
videoId: FSs_JYwnAdI
---

From: [[fireship]] <br/> 

When a [[JavaScript fundamentals and practical concepts | JavaScript]] program runs, whether in a web browser or server-side with Node.js, it needs to allocate memory on the system's RAM to store variables and objects for the runtime <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>. It also requires a thread from the CPU to execute instructions <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>. However, as a [[JavaScript highlevel features | high-level programming language]], [[JavaScript fundamentals and practical concepts | JavaScript]] abstracts away these low-level concerns from the developer <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. [[JavaScript highlevel features | High-level languages]] like [[JavaScript fundamentals and practical concepts | JavaScript]] utilize abstractions such as garbage collectors and dynamic typing to simplify the development process <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>.

The ECMAScript 262 specification, which [[JavaScript fundamentals and practical concepts | JavaScript]] is based on, defines how the language is laid out but does not specify memory management or the [[JavaScript event loop and asynchronous programming | event loop]] <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>. These implementation details are handled by browser vendors through [[JavaScript engines]], such as Mozilla's SpiderMonkey and Google's V8 <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>.

## Memory Regions: Call Stack and Heap

When your [[JavaScript fundamentals and practical concepts | JavaScript]] code executes, two primary regions of memory are allocated on the machine: the call stack and the heap <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>.

### The Call Stack
The call stack is a high-performance, continuous region of memory used to execute [[Functions and closures in JavaScript | functions]] <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>.
*   **Function Calls**: When a [[Functions and closures in JavaScript | function]] is called, it creates a "frame" on the call stack <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>. This frame contains a copy of its local variables <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>.
*   **Nesting Functions**: If a [[Functions and closures in JavaScript | function]] calls another [[Functions and closures in JavaScript | function]], a new frame is added on top of the stack <a class="yt-timestamp" data-t="00:05:59">[00:05:59]</a>.
*   **Function Return**: When a [[Functions and closures in JavaScript | function]] returns, its frame is "popped" off the stack <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.
*   **"Call Stack Size Exceeded" Error**: If a [[Functions and closures in JavaScript | function]] never returns (e.g., an infinitely recursive [[Functions and closures in JavaScript | function]]), the call stack can grow indefinitely until the engine throws a "call stack size exceeded" error <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>. Each frame in such a recursive [[Functions and closures in JavaScript | function]] would contain a copy of its local [[Variables and scope in JavaScript | variables]] <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>.

### The Heap
The heap is a mostly unstructured memory pool where [[JavaScript objects and their properties | objects]] and primitive values inside [[Functions and closures in JavaScript | closures]] are stored <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>.
*   It's used for data that might be referenced by multiple [[Functions and closures in JavaScript | function]] calls outside of a local context <a class="yt-timestamp" data-t="00:07:25">[00:07:25]</a>.
*   You can inspect [[JavaScript objects and their properties | objects]] stored in the heap by taking a heap snapshot in Chrome DevTools <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>.

## Garbage Collection

A key feature of the heap in [[JavaScript fundamentals and practical concepts | JavaScript]] environments (like V8) is that it is "garbage collected" <a class="yt-timestamp" data-t="00:07:52">[00:07:52]</a>.
*   **Automatic Memory Management**: The [[JavaScript fundamentals and practical concepts | JavaScript]] runtime automatically attempts to clear up free memory when it's no longer referenced in your code <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>.
*   **No Manual Allocation/Deallocation**: This means developers do not need to manually allocate and free up memory as they would in languages like C <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>.
*   **Still Need to Consider Memory**: While automated, this does not mean developers can ignore memory considerations entirely <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>. Memory leaks can still occur if references are inadvertently maintained, preventing the garbage collector from reclaiming memory.