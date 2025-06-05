---
title: Asynchronous programming and event loop
videoId: lkIFF4maKMU
---

From: [[fireship]] <br/> 

One of JavaScript's most notable features is its non-blocking event loop <a class="yt-timestamp" data-t="00:07:25">[00:07:25]</a>. This mechanism allows JavaScript to handle multiple operations concurrently, crucial for modern web applications <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>.

## Synchronous vs. Asynchronous Execution

Normally, code written in a script is executed synchronously, meaning each line must finish before the next one starts <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>. However, with an event loop, JavaScript can run asynchronous code in a separate thread pool, allowing the rest of the application to continue executing <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>.

Modern websites often have multiple tasks running simultaneously but only access a single thread for computation, known as the main thread <a class="yt-timestamp" data-t="00:07:46">[00:07:46]</a>. Without asynchronous code, multitasking would be impossible <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>.

## How the Event Loop Works

### Callbacks and `setTimeout`

A simple way to demonstrate asynchronous behavior is with `setTimeout` <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>. This function takes another function as an argument (a "callback function") and delays its execution until a specified number of milliseconds have passed <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>. The callback function is queued in the event loop and is only called back later when it's ready to execute on the main thread <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>.

### Callback Hell

While callback functions are common, their overuse, especially when deeply nested, can lead to a situation known as "callback hell" <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>.

## Improved Asynchronous Patterns

Fortunately, there are better ways to write asynchronous code <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>.

### Promises

A promise is a wrapper for a value that is initially unknown but will resolve to a value in the future <a class="yt-timestamp" data-t="00:08:19">[00:08:19]</a>. This is useful for operations like calls to a third-party API that fetch data <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>. If an error occurs, the promise can reject, raising an error <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>. Consumers of a promise can use `.then()` and `.catch()` methods to handle these two possible outcomes <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a>.

### [[async_and_await_in_javascript | Async and Await]]

An even better approach is to define an [[async_and_await_in_javascript | async function]], which automatically returns a promise <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>. Within the body of an [[async_and_await_in_javascript | async function]], the [[async_and_await_in_javascript | `await` keyword]] can pause execution until other promises resolve, resulting in more readable code <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>. For error handling with [[async_and_await_in_javascript | `async/await]]`, the code should be wrapped in a `try...catch` block <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>.