---
title: Asynchronous programming and event loop in JavaScript
videoId: lkIFF4maKMU
---

From: [[fireship]] <br/> 

[[Asynchronous programming in JavaScript | Asynchronous programming]] and the [[JavaScript event loop and asynchronous programming | event loop]] are key features of JavaScript that allow for non-blocking operations, essential for modern web applications <a class="yt-timestamp" data-t="07:25:00">[07:25:00]</a>.

## Understanding Synchronous vs. Asynchronous Execution

Normally, code in a JavaScript script is executed synchronously, meaning each line must finish before the next one starts <a class="yt-timestamp" data-t="07:28:00">[07:28:00]</a>. However, JavaScript, despite being inherently [[JavaScript singlethreaded nature | single-threaded]], allows for multitasking through asynchronous code <a class="yt-timestamp" data-t="07:42:00">[07:42:00]</a>. Without asynchronous capabilities, it would be impossible to handle multiple operations simultaneously, as modern websites often do <a class="yt-timestamp" data-t="07:51:00">[07:51:00]</a>.

## The [[JavaScript event loop and asynchronous programming | Event Loop]]

The [[JavaScript event loop and asynchronous programming | event loop]] enables the execution of asynchronous code in a separate thread pool, allowing the rest of the application to continue running <a class="yt-timestamp" data-t="07:35:00">[07:35:00]</a>.

### Demonstrating Asynchronicity with `setTimeout`

A simple way to illustrate this is using `setTimeout`, which takes a function as an argument and executes it after a specified number of milliseconds <a class="yt-timestamp" data-t="07:54:00">[07:54:00]</a>. The function passed to `setTimeout` is known as a callback function <a class="yt-timestamp" data-t="08:03:00">[08:03:00]</a>. It's enqueued in the [[JavaScript event loop and asynchronous programming | event loop]] and called back later when it's ready to execute on the main thread <a class="yt-timestamp" data-t="08:06:00">[08:06:00]</a>.

### Callback Functions and "Callback Hell"

Callback functions are very common in [[Asynchronous programming in JavaScript | asynchronous programming]] <a class="yt-timestamp" data-t="08:10:00">[08:10:00]</a>. However, their overuse and deep nesting can lead to a difficult-to-manage situation known as "callback hell" <a class="yt-timestamp" data-t="08:11:00">[08:11:00]</a>.

## Handling [[Asynchronous programming in JavaScript | Asynchronous Programming]] with Promises

To mitigate the issues of callback hell, Promises were introduced as a more structured way to handle [[Asynchronous programming in JavaScript | asynchronous operations]] <a class="yt-timestamp" data-t="08:15:00">[08:15:00]</a>.

A Promise acts as a wrapper for a value that is not yet known but will resolve to a value in the future, such as data from a third-party API call <a class="yt-timestamp" data-t="08:18:00">[08:18:00]</a>.
*   If the operation is successful, the Promise will "resolve" <a class="yt-timestamp" data-t="08:22:00">[08:22:00]</a>.
*   If an error occurs, the Promise will "reject" <a class="yt-timestamp" data-t="08:29:00">[08:29:00]</a>.

Consumers of a Promise can use `.then()` and `.catch()` methods to handle these two possible outcomes, allowing for chained operations and error management <a class="yt-timestamp" data-t="08:33:00">[08:33:00]</a>.

## [[Utilizing async await in JavaScript | Async/Await]] for Cleaner Asynchronous Code

A more modern and readable approach to [[Asynchronous programming in JavaScript | asynchronous programming]] is using the [[Asyncawait in JavaScript | async/await]] syntax <a class="yt-timestamp" data-t="08:37:00">[08:37:00]</a>.

### Defining [[Asyncawait in JavaScript | Async Functions]]

An `async` function automatically returns a Promise <a class="yt-timestamp" data-t="08:39:00">[08:39:00]</a>. Inside an `async` function, the `await` keyword can be used to pause the function's execution until another Promise resolves, resulting in more readable, synchronous-looking code <a class="yt-timestamp" data-t="08:43:00">[08:43:00]</a>.

### Error Handling with `try...catch`

For robust error handling within [[Asyncawait in JavaScript | async/await]] code, it's recommended to wrap the code in a `try...catch` block <a class="yt-timestamp" data-t="08:51:00">[08:51:00]</a>.