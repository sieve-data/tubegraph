---
title: JavaScript highlevel features
videoId: FSs_JYwnAdI
---

From: [[fireship]] <br/> 

[[popular_dynamic_and_highlevel_programming_languages | JavaScript]] is a high-level, single-threaded, garbage-collected, interpreted or just-in-time compiled, prototype-based, multi-paradigm, dynamic language with a non-blocking event loop concurrency model. <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a> Understanding how [[javascript_fundamentals_and_practical_concepts | JavaScript]] works in a computer system requires examining its core characteristics. <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>

When a [[javascript_fundamentals_and_practical_concepts | JavaScript]] program runs (e.g., a web application in a browser or server-side with Node.js), it allocates memory on RAM for runtime, variables, and objects. <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a> It also utilizes a CPU thread to execute instructions. <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a> As a [[javascript_fundamentals_and_practical_concepts | JavaScript]] developer, one doesn't typically need to consider these low-level details because [[javascript_fundamentals_and_practical_concepts | JavaScript]] is a high-level programming language. <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>

## Defining "High-Level"

The term "high-level" refers to the degree of abstraction or simplification a language provides over the computer's hardware. <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>

*   **Machine Code** is the lowest level, a numeric language executed directly by the CPU, but extremely difficult for humans to use. <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>
*   **Assembly Language** adds some syntactic sugar but is specific to a particular CPU or operating system. <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>
*   **C Language** offers a modern syntax and cross-platform capabilities, but developers still manage low-level issues like memory allocation. <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>
*   **[[popular_dynamic_and_highlevel_programming_languages | JavaScript]]** and [[popular_dynamic_and_highlevel_programming_languages | Python]] represent a higher level, utilizing abstractions like garbage collectors and [[javascript_data_types_and_control_flow | dynamic typing]] to simplify application development. <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>

## Key Characteristics of JavaScript

### Interpreted and Just-In-Time Compiled

There are two fundamental ways to translate code for CPU execution: interpretation and compilation. <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>

*   **Interpreted**: [[javascript_fundamentals_and_practical_concepts | JavaScript]] is an interpreted language, meaning it requires an interpreter in the environment to read and execute source code directly, instruction by instruction. <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a> This differs from compiled languages like Java or C, which statically analyze and compile all code into a binary before execution. <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>
*   **Just-In-Time (JIT) Compilation**: Although initially not designed as a compiled language, modern [[javascript_fundamentals_and_practical_concepts | JavaScript]] engines (like Mozilla's SpiderMonkey and Google's V8) incorporate JIT compilation. <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a> <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a> V8, for example, compiles [[javascript_fundamentals_and_practical_concepts | JavaScript]] down to native machine code before running it, enhancing performance in browsers and Node.js. <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a> <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>

### Dynamically Typed

[[javascript_fundamentals_and_practical_concepts | JavaScript]] is a [[javascript_data_types_and_control_flow | dynamically typed]] language, a common feature among high-level interpreted languages. <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a> This means explicit type definitions are not used in vanilla [[javascript_fundamentals_and_practical_concepts | JavaScript]] code. <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a> Instead, the type is associated with the runtime value, not the variables or [[javascript_function_basics_and_anatomy | functions]]. <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>

### Multi-Paradigm

[[javascript_fundamentals_and_practical_concepts | JavaScript]] is a multi-paradigm language, allowing developers to combine styles from declarative/functional approaches and imperative/object-oriented approaches. <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a> Most general-purpose programming languages share this characteristic. <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>

### Prototype-Based

[[javascript_fundamentals_and_practical_concepts | JavaScript]] is based on prototypal inheritance. <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a> In [[javascript_fundamentals_and_practical_concepts | JavaScript]], everything is an [[javascript_objects_and_their_properties | object]], and each [[javascript_objects_and_their_properties | object]] maintains a link to its prototype. <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a> This forms a "prototype chain" where [[javascript_objects_and_their_properties | objects]] can inherit behaviors from other [[javascript_objects_and_their_properties | objects]]. <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a> This concept contributes to [[javascript_fundamentals_and_practical_concepts | JavaScript]]'s flexibility as a multi-paradigm language, especially when contrasted with class-based inheritance. <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>

### Single-Threaded with an Event Loop Concurrency Model

[[javascript_fundamentals_and_practical_concepts | JavaScript]] is a single-threaded language, meaning it can only perform one computation at a time. <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a> This can lead to the browser tab freezing if a long-running, synchronous task (like an infinite `while` loop) is executed directly, as the single thread becomes stuck. <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>

To manage long-running tasks without blocking, [[javascript_fundamentals_and_practical_concepts | JavaScript]] uses an **Event Loop**. <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>

*   **Mechanism**: The event loop is essentially a `while` loop that waits for messages from a queue and then processes their synchronous instructions to completion. <a class="yt-timestamp" data-t="00:08:23">[00:08:23]</a>
*   **Non-Blocking**: This model makes [[javascript_fundamentals_and_practical_concepts | JavaScript]] non-blocking because it primarily listens to events and handles callbacks. <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a> It doesn't wait for function return values but rather for the CPU to process synchronous code, typically in microseconds. <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>
*   **Asynchronous Operations**: Long-running jobs, such as HTTP calls or file system interactions, can be offloaded to separate thread pools (e.g., in the browser or Node.js) without blocking the main [[javascript_fundamentals_and_practical_concepts | JavaScript]] thread. <a class="yt-timestamp" data-t="00:09:26">[00:09:26]</a>

#### Call Stack and Heap

When [[javascript_fundamentals_and_practical_concepts | JavaScript]] code executes, two main regions of memory are allocated:

*   **Call Stack**: A high-performance, continuous region of memory used to execute [[javascript_function_basics_and_anatomy | functions]]. <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>
    *   When a [[javascript_function_basics_and_anatomy | function]] is called, it creates a "frame" on the stack containing copies of its local variables. <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>
    *   Calling a [[javascript_function_basics_and_anatomy | function]] within a [[javascript_function_basics_and_anatomy | function]] adds another frame. <a class="yt-timestamp" data-t="00:05:59">[00:05:59]</a>
    *   Returning from a [[javascript_function_basics_and_anatomy | function]] pops its frame off the stack. <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>
    *   An infinite recursive [[javascript_function_basics_and_anatomy | function]] can lead to a "call stack size exceeded" error. <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>
*   **Heap**: A largely unstructured memory pool where [[javascript_objects_and_their_properties | objects]] or primitive values within [[functions_and_closures_in_javascript | closures]] are stored. <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a> Unlike the call stack, the heap is used for data that might be referenced by multiple [[javascript_function_basics_and_anatomy | function]] calls outside of a local context. <a class="yt-timestamp" data-t="00:07:25">[00:07:25]</a>

### Garbage Collected

The heap in [[javascript_fundamentals_and_practical_concepts | JavaScript]] is garbage collected. <a class="yt-timestamp" data-t="00:07:52">[00:07:52]</a> This means the [[javascript_fundamentals_and_practical_concepts | JavaScript]] runtime (e.g., V8) automatically attempts to clear up memory when it is no longer referenced in the code. <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a> This eliminates the need for manual memory allocation and deallocation, unlike languages like C. <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>

## Microtask Queue

Modern [[javascript_fundamentals_and_practical_concepts | JavaScript]] introduces a **Microtask Queue**, primarily for Promises, which has priority over the main task queue used for DOM APIs and `setTimeout`. <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a> This means that promise handlers will be called back before `setTimeout` callbacks, even if both have a zero-second delay. <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a> During an event loop iteration, synchronous code runs first, then callbacks in the microtask queue, and finally callbacks from the main task queue. <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>

While these low-level concepts provide a deep understanding of [[javascript_fundamentals_and_practical_concepts | JavaScript]], developers do not necessarily need to know all of them to begin building applications. <a class="yt-timestamp" data-t="00:10:28">[00:10:28]</a> The practical applications of [[javascript_fundamentals_and_practical_concepts | JavaScript]] for building products are explored in subsequent videos. <a class="yt-timestamp" data-t="00:10:32">[00:10:32]</a>