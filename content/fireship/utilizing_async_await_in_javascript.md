---
title: Utilizing async await in JavaScript
videoId: vn3tm0quoqE
---

From: [[fireship]] <br/> 

[[asynchronous_programming_in_javascript | Asynchronous programming]] is an essential skill for any JavaScript developer, as JavaScript is a single-threaded programming language, yet web operations are often blocking or time-consuming <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. The `async await` syntax provides significant syntactic sugar to make asynchronous code more readable <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>.

Before diving into `async await`, it's crucial to understand foundational concepts like the [[javascript_event_loop_and_asynchronous_programming | browser or Node.js event loop]], callbacks, and [[using_promises_for_asynchronous_operations | promises]] <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>.

## The Event Loop Explained

Both the browser and Node.js operate on a single-threaded [[javascript_event_loop_and_asynchronous_programming | event loop]] to execute JavaScript code <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

Initially, the [[javascript_event_loop_and_asynchronous_programming | event loop]] runs all synchronous code <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. It can also queue up [[asynchronous_programming_in_javascript | asynchronous]] events to be called back later <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>. When an operation like fetching data from a network is initiated, the [[javascript_event_loop_and_asynchronous_programming | event loop]] continues its tasks while the network operation happens in a separate thread pool <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>. Once the data retrieval finishes, it signals the [[javascript_event_loop_and_asynchronous_programming | event loop]] that it's ready for a callback <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>.

Key distinctions in the [[javascript_event_loop_and_asynchronous_programming | event loop]]:
*   **Macro tasks**: If an event is a macro task (e.g., `setTimeout`, `setInterval`), it will be executed on the *next* [[javascript_event_loop_and_asynchronous_programming | event loop]] iteration <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.
*   **Micro tasks**: If an event is a micro task (e.g., a fulfilled [[using_promises_for_asynchronous_operations | promise]]), it will be called back *before* the start of the next [[javascript_event_loop_and_asynchronous_programming | event loop]] <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>.

### Event Loop Example

Consider the following sequence of operations <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>:
1.  A synchronous `console.log`.
2.  A `setTimeout` with a 0ms delay.
3.  A [[using_promises_for_asynchronous_operations | promise]] that resolves immediately.
4.  Another synchronous `console.log`.

Intuitively, one might expect them to execute sequentially. However, due to the [[javascript_event_loop_and_asynchronous_programming | event loop]]'s priorities, the execution order is different <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>:
*   The first and last synchronous `console.log` statements execute immediately on the main thread <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>.
*   The `setTimeout` is queued as a macro task for a future loop <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.
*   The [[using_promises_for_asynchronous_operations | promise]] is queued as a micro task, running immediately after the current synchronous task completes but *before* the next [[javascript_event_loop_and_asynchronous_programming | event loop]] iteration <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>.

This means the [[using_promises_for_asynchronous_operations | promise]]'s callback, even if queued later, executes before the `setTimeout`'s callback because micro tasks have higher priority than macro tasks <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>.

## Working with [[using_promises_for_asynchronous_operations | Promises]]

[[using_promises_for_asynchronous_operations | Promises]] are a significant improvement over callbacks for [[asynchronous_programming_in_javascript | asynchronous operations]] <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. The `fetch` API, for instance, returns a [[using_promises_for_asynchronous_operations | promise]] of the HTTP response <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>.

### Consuming [[using_promises_for_asynchronous_operations | Promises]]
[[using_promises_for_asynchronous_operations | Promises]] can be chained together using `.then()` callbacks, allowing for sequential [[asynchronous_programming_in_javascript | asynchronous]] operations <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.
A key advantage is that errors anywhere in a [[using_promises_for_asynchronous_operations | promise]] chain can be caught with a single `.catch()` function at the end <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>. If an error is thrown, it bypasses all subsequent `.then()` callbacks and goes directly to the `.catch()` block <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.

### Creating [[using_promises_for_asynchronous_operations | Promises]]
When creating [[using_promises_for_asynchronous_operations | promises]], it's important to understand what runs on the main thread <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>. Wrapping a synchronous, blocking operation (e.g., a long `while` loop) directly within a `new Promise()` constructor will *not* move it off the main thread <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>. The promise creation itself, and the synchronous code inside its executor function, still execute on the main thread <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>. Only the resolution of the value happens as a micro task <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.

To ensure synchronous code runs as fast as possible without blocking, place the blocking operation inside a `Promise.resolve().then()` callback <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>. This guarantees the blocking code is executed as a micro task *after* all the synchronous code in the current macro task has completed <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.

## The Power of `async await`

`async await` is syntactic sugar that makes [[asynchronous_programming_in_javascript | asynchronous]] code read like synchronous code <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>.

### The `async` Keyword
Adding the `async` keyword in front of a function declaration makes that function always return a [[using_promises_for_asynchronous_operations | promise]] <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>. Whatever value is returned inside an `async` function will automatically be wrapped and resolved as a [[using_promises_for_asynchronous_operations | promise]] <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>. The `async` keyword also sets up the context for using the `await` keyword <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>.

### The `await` Keyword
The `await` keyword, used only within an `async` function, pauses the execution of that function until the [[using_promises_for_asynchronous_operations | promise]] it's waiting on resolves to a value <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>. This allows [[asynchronous_programming_in_javascript | asynchronous]] values to be assigned directly to variables, simplifying code that would otherwise require complex [[using_promises_for_asynchronous_operations | promise]] chaining <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>.

One significant benefit of `async await` is the ease of sharing resolved values between multiple [[asynchronous_programming_in_javascript | asynchronous]] steps, a task often cumbersome with raw [[using_promises_for_asynchronous_operations | promises]] <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>.

### Error Handling with `try-catch`
`async await` simplifies error handling by allowing the use of traditional `try-catch` blocks <a class="yt-timestamp" data-t="00:09:07">[00:09:07]</a>. This provides more flexibility than chaining `.catch()` callbacks to [[using_promises_for_asynchronous_operations | promise]] chains <a class="yt-timestamp" data-t="00:09:13">[00:09:13]</a>. If an error is thrown within the `try` block, execution jumps to the `catch` block <a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a>.

Within the `catch` block, you can either:
*   `return` a value: This effectively ignores the error and provides a replacement value, allowing the consumer of the [[using_promises_for_asynchronous_operations | promise]] to receive a result instead of an error <a class="yt-timestamp" data-t="00:09:33">[00:09:33]</a>.
*   `throw` another error: This propagates the error, breaking the consumer's [[using_promises_for_asynchronous_operations | promise]] chain and allowing their `catch` callback to handle it <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>.

## Best Practices and Tricks

### Concurrent Execution with `Promise.all`
A common mistake when using `async await` is failing to run independent [[asynchronous_programming_in_javascript | asynchronous]] operations concurrently <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a>. Using `await` sequentially for operations that don't depend on each other will pause execution unnecessarily, leading to slower performance <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>.

Instead, group independent [[using_promises_for_asynchronous_operations | promises]] into `Promise.all` <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>. `Promise.all` will run all [[using_promises_for_asynchronous_operations | promises]] in an array concurrently and resolve when all of them have completed, returning an array of their resolved values <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>. This significantly improves performance for non-dependent [[asynchronous_programming_in_javascript | asynchronous]] calls <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>.

### `async await` in Loops
*   **`async await` in `map` or `forEach`**: Using `await` directly inside [[modern_javascript_array_methods | Array.prototype.map()]] or [[modern_javascript_array_methods | Array.prototype.forEach()]] will *not* pause the function <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>. Instead, the [[using_promises_for_asynchronous_operations | promises]] will run concurrently <a class="yt-timestamp" data-t="00:10:26">[00:10:26]</a>. This can be useful for triggering many concurrent operations, but it won't await each one sequentially.
*   **Sequential `await` in loops**: To pause each iteration of a loop and `await` a [[using_promises_for_asynchronous_operations | promise]] before proceeding to the next, use a traditional `for` loop within an `async` function <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a>.
*   **`for await...of`**: If you have a [[using_promises_for_asynchronous_operations | promise]] that resolves to an array, you can use `for await...of` to iterate over the resolved array directly after the [[using_promises_for_asynchronous_operations | promise]] resolves <a class="yt-timestamp" data-t="00:10:55">[00:10:55]</a>.

### `await` in Conditionals
The `await` keyword can be used directly within conditional statements (e.g., `if` statements) <a class="yt-timestamp" data-t="00:11:14">[00:11:14]</a>. This allows for concise and readable conditional expressions based on the resolved value of a [[using_promises_for_asynchronous_operations | promise]] <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>.

`async await` is considered one of the most beneficial additions to JavaScript for managing [[asynchronous_programming_in_javascript | asynchronous code]] <a class="yt-timestamp" data-t="00:11:33">[00:11:33]</a>.