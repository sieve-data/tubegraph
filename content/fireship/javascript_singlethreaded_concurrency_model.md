---
title: JavaScript singlethreaded concurrency model
videoId: FSs_JYwnAdI
---

From: [[fireship]] <br/> 

[[JavaScript highlevel features | JavaScript]] is characterized as a [[javascript_singlethreaded_nature | single-threaded]], garbage-collected, interpreted or just-in-time compiled, prototype-based, multi-paradigm, dynamic language with a non-blocking event loop concurrency model <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. This article focuses on its [[javascript_singlethreaded_nature | single-threaded]] nature and the mechanisms that allow it to handle concurrency without blocking.

## [[javascript_singlethreaded_nature | Single-Threaded Nature]]
[[JavaScript highlevel features | JavaScript]] is a [[javascript_singlethreaded_nature | single-threaded]] language, meaning it can only perform one computation at a time <a class="yt-timestamp" data-t="05:10:00">[05:10:00]</a>. This characteristic is evident when a long-running synchronous task, like an infinite `while` loop, is executed in a browser tab. Such a loop will prevent the tab from responding to any other events, as the single thread is stuck in the loop <a class="yt-timestamp" data-t="05:18:00">[05:18:00]</a>.

When a [[JavaScript highlevel features | JavaScript]] program runs, it allocates memory on your RAM for the runtime, variables, and objects <a class="yt-timestamp" data-t="00:49:00">[00:49:00]</a>. It also requires a thread from the CPU to execute instructions <a class="yt-timestamp" data-t="00:56:00">[00:56:00]</a>.

## Memory Management

Two primary regions of memory are allocated when executing [[JavaScript highlevel features | JavaScript]] code: the Call Stack and the Heap <a class="yt-timestamp" data-t="05:42:00">[05:42:00]</a>.

### Call Stack
The Call Stack is a high-performance, continuous region of memory used to execute functions <a class="yt-timestamp" data-t="05:48:00">[05:48:00]</a>.
*   When a function is called, a frame is created on the call stack containing a copy of its local variables <a class="yt-timestamp" data-t="05:53:00">[05:53:00]</a>.
*   Calling a function within another function adds another frame to the stack <a class="yt-timestamp" data-t="05:59:00">[05:59:00]</a>.
*   Returning from a function pops its frame off the stack <a class="yt-timestamp" data-t="06:03:00">[06:03:00]</a>.
*   If a function, especially a recursive one, never reaches a return statement, it can lead to a "call stack size exceeded" error <a class="yt-timestamp" data-t="07:03:00">[07:03:00]</a>. Each frame in such a situation would contain a copy of its local variables <a class="yt-timestamp" data-t="07:17:00">[07:17:00]</a>.

### Heap
The Heap is a largely unstructured memory pool used to store objects or primitive values within closures <a class="yt-timestamp" data-t="07:30:00">[07:30:00]</a>.
*   The heap is [[javascript_memory_management_and_garbage_collection | garbage collected]], meaning the [[JavaScript highlevel features | JavaScript]] runtime (like V8) attempts to clear up free memory when it's no longer referenced <a class="yt-timestamp" data-t="07:52:00">[07:52:00]</a>.
*   This removes the need for manual memory allocation and deallocation, unlike languages like C <a class="yt-timestamp" data-t="08:00:00">[08:00:00]</a>.

## [[javascript_event_loop_and_asynchronous_programming | The Event Loop]]

Despite being [[javascript_singlethreaded_nature | single-threaded]], [[JavaScript highlevel features | JavaScript]] manages long-running tasks and maintains a non-blocking experience through the [[javascript_event_loop_and_asynchronous_programming | event loop]] <a class="yt-timestamp" data-t="08:16:00">[08:16:00]</a>.

The [[javascript_event_loop_and_asynchronous_programming | event loop]] operates as a `while` loop that continuously waits for messages from a queue and then processes their synchronous instructions to completion <a class="yt-timestamp" data-t="08:23:00">[08:23:00]</a>. This is what makes [[JavaScript highlevel features | JavaScript]] non-blocking; it primarily listens to events and handles callbacks, rather than waiting for function return values <a class="yt-timestamp" data-t="08:44:00">[08:44:00]</a>.

The basic flow of an [[javascript_event_loop_and_asynchronous_programming | event loop]] iteration:
1.  Handle all synchronous code in the script <a class="yt-timestamp" data-t="09:01:00">[09:01:00]</a>.
2.  Check if there are any messages or callbacks in the queue ready for execution <a class="yt-timestamp" data-t="09:06:00">[09:06:00]</a>.

For example, if a `setTimeout` for 0 seconds is placed at the top of a script, the [[javascript_event_loop_and_asynchronous_programming | event loop]] will execute all synchronous code first before getting to the timeout's callback <a class="yt-timestamp" data-t="09:11:00">[09:11:00]</a>. This mechanism allows [[asynchronous_programming_in_javascript | asynchronous operations]], like HTTP calls or file system interactions, to be offloaded to separate thread pools without blocking the main [[JavaScript highlevel features | JavaScript]] thread <a class="yt-timestamp" data-t="09:26:00">[09:26:00]</a>.

### Microtask Queue and Promises

The introduction of [[using_promises_for_asynchronous_operations | Promises]] brought a new queue, the Microtask Queue, which has priority over the main task queue (used for DOM APIs and `setTimeout`) <a class="yt-timestamp" data-t="09:58:00">[09:58:00]</a>.

The refined [[javascript_event_loop_and_asynchronous_programming | event loop]] iteration order:
1.  Handle synchronous code <a class="yt-timestamp" data-t="10:11:00">[10:11:00]</a>.
2.  Process any ready callbacks from the Microtask Queue (e.g., [[using_promises_for_asynchronous_operations | Promises]]) <a class="yt-timestamp" data-t="10:14:00">[10:14:00]</a>.
3.  Execute callbacks ready from the main task queue (e.g., `setTimeout`, DOM APIs) <a class="yt-timestamp" data-t="10:19:00">[10:19:00]</a>.

## Just-In-Time (JIT) Compilation

Modern [[JavaScript highlevel features | JavaScript]] engines, such as Mozilla's SpiderMonkey and Google's V8, implement Just-In-Time (JIT) compilation <a class="yt-timestamp" data-t="04:36:00">[04:36:00]</a>. V8, for instance, compiles [[JavaScript highlevel features | JavaScript]] code down to native machine code before running it, differing from a pure interpreter that executes bytecode line by line <a class="yt-timestamp" data-t="04:47:00">[04:47:00]</a>. While JIT compilation improves performance in browsers and Node.js, it doesn't fundamentally change how developers write [[JavaScript highlevel features | JavaScript]] code <a class="yt-timestamp" data-t="05:04:00">[05:04:00]</a>.

## Conclusion

Understanding these underlying concepts of the Call Stack, Heap, and especially the [[javascript_event_loop_and_asynchronous_programming | Event Loop]] and Microtask Queue, clarifies how [[JavaScript highlevel features | JavaScript]], despite its [[javascript_singlethreaded_nature | single-threaded nature]], achieves its [[asynchronous_programming_in_javascript | asynchronous]] and non-blocking concurrency model. While not strictly necessary for building applications, knowing these details provides a deeper insight into the language's behavior <a class="yt-timestamp" data-t="10:28:00">[10:28:00]</a>.