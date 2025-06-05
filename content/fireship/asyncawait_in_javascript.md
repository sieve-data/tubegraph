---
title: Asyncawait in JavaScript
videoId: Mus_vwhTCq0
---

From: [[fireship]] <br/> 

[[utilizing_async_await_in_javascript | Async/await]] is considered one of the most significant advancements in [[new_javascript_features_in_2020 | modern JavaScript]] for handling [[asynchronous_programming_in_javascript | asynchronous operations]] <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>, <a class="yt-timestamp" data-t="00:11:52">[00:11:52]</a>. It provides a more readable and understandable way to write [[asynchronous_programming_in_javascript | asynchronous code]] by allowing it to be expressed in a synchronous format <a class="yt-timestamp" data-t="00:11:14">[00:11:14]</a>, <a class="yt-timestamp" data-t="00:11:46">[00:11:46]</a>.

## The Problem with Promises and Callbacks

Before [[utilizing_async_await_in_javascript | async/await]], [[using_promises_for_asynchronous_operations | asynchronous operations]] were typically handled using promises <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>. When using promises, you wait for an [[asynchronous_programming_in_javascript | asynchronous]] value to resolve and then handle it with a callback function inside `.then()` <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>. After data is received, you can return another promise and chain more `.then()` callbacks <a class="yt-timestamp" data-t="00:10:51">[00:10:51]</a>.

While functional, this approach often leads to code that is difficult to read and manage, frequently referred to as "promise chains" or "callback hell," characterized by repetitive "and then" calls <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>.

> For example, in a real-world scenario, you might need to retrieve one item from a database, then use that data to retrieve another item from an API, and so on <a class="yt-timestamp" data-t="00:10:39">[00:10:39]</a>, <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>, <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>.

## How Async/await Works

[[utilizing_async_await_in_javascript | Async/await]] provides a clean solution by allowing you to write [[asynchronous_programming_in_javascript | asynchronous code]] in a more sequential, synchronous-like style <a class="yt-timestamp" data-t="00:11:14">[00:11:14]</a>, <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>.

### `async` Keyword
To use [[utilizing_async_await_in_javascript | async/await]], you add the `async` keyword in front of a function declaration <a class="yt-timestamp" data-t="00:11:22">[00:11:22]</a>. An `async` function implicitly returns a promise <a class="yt-timestamp" data-t="00:11:25">[00:11:25]</a>.

### `await` Keyword
Within an `async` function, you can use the `await` keyword in front of any promise <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>. When `await` is used, the function pauses its execution until the promise resolves, and then returns the resolved value directly into a variable <a class="yt-timestamp" data-t="00:11:32">[00:11:32]</a>.

```javascript
async function getRandomNumbers() { <a class="yt-timestamp" data-t="00:11:22">[00:11:22]</a>
  const first = await random();   // Waits for 'random' promise to resolve <a class="yt-timestamp" data-t="00:11:37">[00:11:37]</a>, <a class="yt-timestamp" data-t="00:11:39">[00:11:39]</a>
  const second = await random();  // Continues only after 'first' is resolved <a class="yt-timestamp" data-t="00:11:42">[00:11:42]</a>
  const third = await random();   // Continues only after 'second' is resolved <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>

  return first + second + third;
}
```

This structure makes the code significantly easier to read and understand, as you can follow the execution line by line, much like synchronous code <a class="yt-timestamp" data-t="00:11:46">[00:11:46]</a>, <a class="yt-timestamp" data-t="00:11:48">[00:11:48]</a>.

While not detailed in the transcript, `async/await` can also be used in conditional statements or for loops <a class="yt-timestamp" data-t="00:12:01">[00:12:01]</a>.