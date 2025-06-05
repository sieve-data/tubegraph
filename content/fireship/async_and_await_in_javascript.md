---
title: Async and await in JavaScript
videoId: Mus_vwhTCq0
---

From: [[fireship]] <br/> 

`Async` and `await` are powerful features in [[state_of_javascript_in_modern_development | modern JavaScript]] that simplify working with [[asynchronous_programming_and_event_loop | asynchronous]] code, making it more readable and easier to manage than traditional promise chains <a class="yt-timestamp" data-t="11:13:00">[11:13:00]</a>.

## The Problem with Traditional Promises

When dealing with multiple sequential [[asynchronous_programming_and_event_loop | asynchronous]] operations, promises can lead to "then() chain hell" <a class="yt-timestamp" data-t="11:00:00">[11:00:00]</a>. For instance, imagine needing to retrieve three different [[asynchronous_programming_and_event_loop | asynchronous]] numbers one after the other and then summing them <a class="yt-timestamp" data-t="10:29:00">[10:29:00]</a>. This scenario is common in real-world applications, such as retrieving data from a database and then from an API <a class="yt-timestamp" data-t="10:38:00">[10:38:00]</a>.

With traditional promises, you:
1.  Wait for an [[asynchronous_programming_and_event_loop | asynchronous]] value to resolve <a class="yt-timestamp" data-t="10:46:00">[10:46:00]</a>.
2.  Handle it with a callback function inside `.then()` <a class="yt-timestamp" data-t="10:50:00">[10:50:00]</a>.
3.  Once data is available, return another promise <a class="yt-timestamp" data-t="10:53:00">[10:53:00]</a>.
4.  Chain another `.then()` callback <a class="yt-timestamp" data-t="10:56:00">[10:56:00]</a>.

This pattern can create verbose code that repeatedly uses "and then, and then, and then" <a class="yt-timestamp" data-t="11:00:00">[11:00:00]</a>.

## Solution: Async/Await

`Async/await` provides a much cleaner solution by allowing [[asynchronous_programming_and_event_loop | async]] code to be expressed in a synchronous format <a class="yt-timestamp" data-t="11:17:00">[11:17:00]</a>.

### How it Works

1.  **`async` keyword**: Prepending `async` to a function forces it to return a promise <a class="yt-timestamp" data-t="11:23:00">[11:23:00]</a>.
2.  **`await` keyword**: Inside an `async` function, `await` can be used in front of a promise. This pauses the execution of the `async` function until the promise resolves, returning the resolved value directly to a variable <a class="yt-timestamp" data-t="11:30:00">[11:30:00]</a>.

```javascript
// Example of a function returning an async promise
function random() {
  return new Promise(resolve => {
    setTimeout(() => {
      resolve(Math.random());
    }, 100);
  });
}

// Rewriting a promise chain with async/await
async function getNumbers() {
  const first = await random();   // Await the first number
  const second = await random();  // Await the second number
  const third = await random();   // Await the third number
  console.log(first + second + third);
}
// This code is much easier to read and understand because it flows line by line.
```
<a class="yt-timestamp" data-t="10:23:00">[10:23:00]</a> <a class="yt-timestamp" data-t="10:46:00">[10:46:00]</a> <a class="yt-timestamp" data-t="11:20:00">[11:20:00]</a> <a class="yt-timestamp" data-t="11:46:00">[11:46:00]</a>

### Benefits

The main benefit of `async/await` is enhanced readability and understanding, as code can be followed line by line, clearly showing the sequence of [[asynchronous_programming_and_event_loop | asynchronous]] operations <a class="yt-timestamp" data-t="11:46:00">[11:46:00]</a>. It is considered one of the most significant advancements in JavaScript <a class="yt-timestamp" data-t="11:54:00">[11:54:00]</a>.

### Further Applications

While not detailed, `async/await` can also be utilized in conditional statements and `for` loops for more complex [[asynchronous_programming_and_event_loop | asynchronous]] flows <a class="yt-timestamp" data-t="12:00:00">[12:00:00]</a>.