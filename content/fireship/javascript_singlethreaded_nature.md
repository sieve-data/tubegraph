---
title: JavaScript singlethreaded nature
videoId: vn3tm0quoqE
---

From: [[fireship]] <br/> 

[[JavaScript singlethreaded concurrency model | JavaScript]] is fundamentally a single-threaded programming language <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. This means that at any given moment, it can only execute one piece of code at a time <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

Despite this, web development frequently involves operations that are blocking or time-consuming, such as fetching data from a network <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. To handle these operations without freezing the entire application, [[asynchronous_programming_in_javascript | asynchronous programming]] is a crucial skill for any [[JavaScript highlevel features | JavaScript]] developer <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.

## The Event Loop

The core mechanism that allows [[JavaScript singlethreaded concurrency model | JavaScript]] to handle [[asynchronous_programming_and_event_loop_in_javascript | asynchronous operations]] despite being single-threaded is the [[javascript_event_loop_and_asynchronous_programming | Event Loop]] <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. Both browser environments and Node.js implement a single-threaded [[javascript_event_loop_and_asynchronous_programming | Event Loop]] to manage code execution <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

Here's how it works:
*   **Synchronous Code Execution** The [[javascript_event_loop_and_asynchronous_programming | Event Loop]] first runs all synchronous code <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.
*   **Asynchronous Event Queuing** During the synchronous execution, if an [[asynchronous_programming_in_javascript | asynchronous event]] (like a network request) is encountered, it's queued up to be called back later <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>. The [[javascript_event_loop_and_asynchronous_programming | Event Loop]] offloads these time-consuming tasks to a separate thread pool, allowing the main thread to continue its work <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.
*   **Notification and Callback** When an [[asynchronous_programming_in_javascript | asynchronous task]] completes, it notifies the [[javascript_event_loop_and_asynchronous_programming | Event Loop]] that it's ready to be called back <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.

### Task Queues: Macro vs. Micro

The [[javascript_event_loop_and_asynchronous_programming | Event Loop]] differentiates between two types of tasks, each with different priorities <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>:
*   **Macro Tasks**: These include operations like `setTimeout` or `setInterval` <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>. They are executed on the *next* turn of the [[javascript_event_loop_and_asynchronous_programming | Event Loop]] <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.
*   **Micro Tasks**: These include operations like fulfilled [[asynchronous_programming_in_javascript | Promises]] <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>. They are called back *before* the start of the *next* [[javascript_event_loop_and_asynchronous_programming | Event Loop]] cycle <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>. This means micro tasks have a higher priority and will run before any queued macro tasks, even if the macro task was queued earlier <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>.

#### Example of Task Priority

Consider the following order of operations <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>:
1.  Synchronous `console.log` <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>
2.  `setTimeout` with 0ms delay (Macro Task) <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>
3.  Immediately resolving Promise (Micro Task) <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>
4.  Another synchronous `console.log` <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>

The execution order will be <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>:
1.  First synchronous `console.log` <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>
2.  Second synchronous `console.log` <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>
3.  Promise resolution (Micro Task) <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>
4.  `setTimeout` callback (Macro Task) <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>

This demonstrates that micro tasks are prioritized to run immediately after the current synchronous task is completed, before the next full cycle of the [[javascript_event_loop_and_asynchronous_programming | Event Loop]] begins <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.

## Implications of Single-Threading

### Blocking the Main Thread

Running CPU-intensive synchronous code directly on the main thread will block all other code from executing until it completes <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>. For example, a `while` loop running a billion times can freeze the script for hundreds of milliseconds <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.

Even wrapping such code within a `new Promise()` constructor does not automatically move the blocking operation off the main thread <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>. The *creation* of the promise and the synchronous blocking code inside it still execute on the main thread. Only the *resolution* of the promise happens as a micro task <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.

To prevent blocking, CPU-intensive synchronous code should be placed inside a `Promise.resolve().then()` callback. This ensures it executes as a micro task, guaranteeing that all current synchronous code runs as fast as possible before the micro task begins <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.

### Concurrency and [[asyncawait_in_JavaScript | Async/Await]]

While [[asyncawait_in_JavaScript | async/await]] makes [[asynchronous_programming_in_javascript | asynchronous code]] read like synchronous code, it's crucial to understand how it affects concurrency on a single thread <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>.
*   **`async` Keyword**: An `async` function always returns a [[asynchronous_programming_in_javascript | Promise]] <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>. Whatever value is returned inside an `async` function is automatically resolved as a [[asynchronous_programming_in_javascript | Promise]] <a class="yt-timestamp" data-t="00:06:38">[00:06:38]</a>. It also provides the context for using the `await` keyword <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>.
*   **`await` Keyword**: `await` pauses the execution of the `async` function until the [[asynchronous_programming_in_javascript | Promise]] it's waiting on resolves to a value <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>.

A common mistake with [[asyncawait_in_JavaScript | async/await]] is *failing to run code concurrently* <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>. If an `async` function uses multiple `await` calls sequentially for independent operations, it will wait for each one to complete before starting the next, effectively running them in series <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>. This means if two operations each take one second, the total time will be two seconds <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>.

To achieve concurrency and avoid blocking, independent [[asynchronous_programming_in_javascript | Promises]] should be run simultaneously using `Promise.all()` <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>. `Promise.all()` allows all [[asynchronous_programming_in_javascript | Promises]] in an array to run concurrently, and then the `await` keyword can be used on `Promise.all()` to wait for all of them to resolve <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>. This can double the speed of an `async` function if its internal operations are not dependent on each other <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>.

### `async/await` in Loops and Conditionals

*   **`await` in `map` or `forEach`**: Using `await` directly inside `Array.prototype.map()` or `Array.prototype.forEach()` loops will *not* pause the function in that context <a class="yt-timestamp" data-t="00:10:16">[00:10:16]</a>. Instead, it will run all the [[asynchronous_programming_in_javascript | Promises]] concurrently <a class="yt-timestamp" data-t="00:10:26">[00:10:26]</a>.
*   **Pausing with Traditional `for` loops**: To pause execution for each iteration of a loop, a traditional `for` loop (e.g., `for (let i = 0; i < n; i++)`) must be used with `await` inside it <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a>. This will pause each step of the loop until the [[asynchronous_programming_in_javascript | Promise]] resolves <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>.
*   **`for await...of`**: For promises that resolve to an array, the `for await...of` syntax can be used to await the array of items and then loop over them immediately <a class="yt-timestamp" data-t="00:10:55">[00:10:55]</a>.
*   **`await` in Conditionals**: The `await` keyword can also be used directly on the left side of a conditional expression to await a [[asynchronous_programming_in_javascript | Promise]]'s result before evaluating the condition <a class="yt-timestamp" data-t="00:11:14">[00:11:14]</a>.

[[asyncawait_in_JavaScript | Async/await]] is considered one of the most beneficial additions to [[JavaScript highlevel features | JavaScript]] (ES7 or TypeScript) for managing [[asynchronous_programming_in_javascript | asynchronous code]] <a class="yt-timestamp" data-t="00:11:33">[00:11:33]</a>.