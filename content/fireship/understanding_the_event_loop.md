---
title: Understanding the event loop
videoId: vn3tm0quoqE
---

From: [[fireship]] <br/> 

[[javascript_singlethreaded_nature | JavaScript]] is a single-threaded programming language, despite many web operations being blocking or time-consuming <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. This makes [[asynchronous_programming_in_javascript | asynchronous programming]] an essential skill for any JavaScript developer <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. Before diving into advanced features like `async` and `await`, it's crucial to understand foundational concepts such as the browser or Node.js [[javascript_event_loop_and_asynchronous_programming | event loop]], callbacks, and Promises <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>.

## What is the Event Loop?

To comprehend [[asynchronous_programming_and_event_loop_in_javascript | asynchronous operations]], one must first understand the [[javascript_event_loop_and_asynchronous_programming | event loop]] <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. Both browsers and Node.js continuously operate a [[javascript_singlethreaded_concurrency_model | single-threaded event loop]] to execute your code <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

On its initial pass, the [[javascript_event_loop_and_asynchronous_programming | event loop]] executes all synchronous code <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. Concurrently, it can queue up asynchronous events to be invoked later <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>. For instance, if a function needs to fetch data from a network, the [[javascript_event_loop_and_asynchronous_programming | event loop]] will continue its operations while the data retrieval occurs in a separate thread pool <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>. Once the data fetching is complete, it signals the [[javascript_event_loop_and_asynchronous_programming | event loop]] that it's ready for its callback <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>.

### Macro Tasks vs. Micro Tasks

The timing of these callbacks depends on whether they are macro tasks or micro tasks <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>:

*   **Macro Tasks**: Tasks like `setTimeout` or `setInterval` are executed on the *next* [[javascript_event_loop_and_asynchronous_programming | event loop]] cycle <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>.
*   **Micro Tasks**: Tasks such as a fulfilled Promise are called back *before* the start of the next [[javascript_event_loop_and_asynchronous_programming | event loop]] <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>.

### Execution Order Example

Consider the following sequence of operations, none of which have an actual time delay <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>:
1.  A `console.log` (synchronous)
2.  A `setTimeout` with a zero-millisecond delay
3.  A Promise that resolves immediately
4.  Another `console.log` (synchronous)

When executed, the output order is not sequential as one might intuitively expect <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>:

1.  The first `console.log` executes immediately on the main thread <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>.
2.  The `setTimeout` is queued for a future macro task <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.
3.  The Promise is queued to run in the micro task queue *immediately after* the current synchronous task <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>.
4.  The last `console.log` executes immediately <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>.

Due to the priority of the micro task queue, the Promise will execute before the `setTimeout`, even if the `setTimeout` was queued first <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>.

### Recommended Resources
*   A highly recommended talk on the [[javascript_event_loop_and_asynchronous_programming | event loop]] is by Jake Archibald <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.
*   Stephen Fluence's demos with Angular channel also has a video on callbacks, which are part of the [[javascript_event_loop_and_asynchronous_programming | event loop]] <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.

## Promises and Async/Await

Understanding the [[javascript_event_loop_and_asynchronous_programming | event loop]] is critical before delving into Promises and the `async`/`await` syntax <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>. `async`/`await` primarily offers syntactic sugar to make [[asynchronous_programming_in_javascript | asynchronous code]] read more like synchronous code <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>.

### Async Keyword

When the `async` keyword is used in front of a function, that function will always return a Promise <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>. Whatever value is returned inside an `async` function will automatically be wrapped and resolved as a Promise <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>. Additionally, the `async` keyword sets up a context for using the `await` keyword <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>.

### Await Keyword

The `await` keyword, when used within an `async` function, pauses the execution of that function until the Promise it's "awaiting" resolves to a value <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>. This allows [[javascript_fundamentals_and_practical_concepts | asynchronous operations]] to be handled sequentially and readably, making it easier to share resolved values between multiple asynchronous steps, a common difficulty with traditional Promise chaining <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>.

### Concurrency with Async/Await

A common mistake with `async`/`await` is failing to run code concurrently <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a>. If subsequent asynchronous operations are not dependent on the result of the previous one, `await`ing them one after another will block execution unnecessarily <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>.

To run Promises concurrently, use `Promise.all()` <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>. `Promise.all()` takes an array of Promises and resolves them all concurrently, returning their resolved values in an array at the corresponding indices <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>. This can significantly improve performance by preventing unnecessary pauses in function execution <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>.

### Error Handling

`async`/`await` simplifies error handling compared to chaining `.catch()` callbacks to Promises <a class="yt-timestamp" data-t="00:09:07">[00:09:07]</a>. You can wrap your `async` code in a `try-catch` block, which offers greater flexibility for handling errors across multiple Promises <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>. If an error is thrown within the `try` block, it will bypass any subsequent code and be caught by the `catch` block <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>.

### Advanced Usage

*   **`async`/`await` in Loops**:
    *   Using `await` directly within `Array.prototype.map()` or `forEach()` will not pause the function; the Promises will run concurrently <a class="yt-timestamp" data-t="00:10:16">[00:10:16]</a>.
    *   To pause execution and await a Promise in each iteration of a loop, use a traditional `for` loop within an `async` function <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a>.
    *   For iterating over a Promise that resolves to an array, you can use `for await...of` to await the array and then loop over its items immediately <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>.
*   **`await` in Conditionals**: You can use the `await` keyword directly on the left side of a conditional expression to await a Promise's result value before evaluating the condition <a class="yt-timestamp" data-t="00:11:14">[00:11:14]</a>. This provides a concise way to write conditional logic with Promises <a class="yt-timestamp" data-t="00:11:25">[00:11:25]</a>.