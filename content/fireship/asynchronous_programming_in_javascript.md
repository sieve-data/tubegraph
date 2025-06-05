---
title: Asynchronous programming in JavaScript
videoId: vn3tm0quoqE
---

From: [[fireship]] <br/> 

[[JavaScript singlethreaded nature | JavaScript is a single-threaded]] programming language, meaning it executes one operation at a time <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. However, many web operations are blocking or time-consuming, making [[Asynchronous programming and event loop in JavaScript | asynchronous programming]] an essential skill for JavaScript developers <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>.

This article will cover the fundamentals of [[Asynchronous programming and event loop in JavaScript | asynchronous programming]] in JavaScript, including the [[JavaScript event loop and asynchronous programming | event loop]], [[Using promises for asynchronous operations | callbacks]], [[Using promises for asynchronous operations | promises]], and the modern [[Asyncawait in JavaScript | async/await]] syntax <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>.

## The JavaScript Event Loop

To understand [[Asynchronous programming and event loop in JavaScript | asynchronous programming]], it's crucial to first grasp the concept of the [[JavaScript event loop and asynchronous programming | event loop]] <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. Both browsers and Node.js constantly run a [[JavaScript singlethreaded concurrency model | single-threaded event loop]] to execute JavaScript code <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

On its initial pass, the [[JavaScript event loop and asynchronous programming | event loop]] executes all synchronous code <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. It can also queue up [[Asynchronous programming and event loop in JavaScript | asynchronous events]] to be called back later <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>. For example, if you request data from a network, the [[JavaScript event loop and asynchronous programming | event loop]] allows that operation to happen in a separate thread pool while it continues its work <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>. Once the data retrieval finishes, it notifies the [[JavaScript event loop and asynchronous programming | event loop]] it's ready for its callback <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>.

### Macro Tasks vs. Micro Tasks

The [[JavaScript event loop and asynchronous programming | event loop]] handles queued [[Asynchronous programming and event loop in JavaScript | asynchronous events]] based on their type:

*   **Macro Tasks**: If an event is a macro task (e.g., `setTimeout`, `setInterval`), it will be executed on the *next* [[JavaScript event loop and asynchronous programming | event loop]] iteration <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.
*   **Micro Tasks**: If an event is a micro task (e.g., a fulfilled [[Using promises for asynchronous operations | promise]]), it will be called back *before* the start of the next [[JavaScript event loop and asynchronous programming | event loop]] iteration <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>. This gives micro tasks higher priority over macro tasks <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.

#### Example Event Loop Execution

Consider the following code example <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>:

```javascript
console.log("First synchronous line"); // 1
setTimeout(() => console.log("Set Timeout (Macro Task)"), 0); // 2
Promise.resolve().then(() => console.log("Promise (Micro Task)")); // 3
console.log("Second synchronous line"); // 4
```

The output order is not intuitive due to the [[JavaScript event loop and asynchronous programming | event loop]]'s priority system <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>:

1.  `First synchronous line` <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>
2.  `Second synchronous line` <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>
3.  `Promise (Micro Task)` <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>
4.  `Set Timeout (Macro Task)` <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>

Even though the `setTimeout` was queued before the [[Using promises for asynchronous operations | promise]], the [[Using promises for asynchronous operations | promise]] (a micro task) is executed first because it runs immediately after the current synchronous task completes, before the next macro task queue is processed <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>.

> For a deeper understanding of the [[JavaScript event loop and asynchronous programming | event loop]], it is highly recommended to watch Jake Archibald's talk on the subject <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. Additionally, Stephen Fluence's Demos with Angular Channel provides videos about [[Using promises for asynchronous operations | callbacks]], which are integral to the [[JavaScript event loop and asynchronous programming | event loop]] <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.

## Using Promises for Asynchronous Operations

[[Using promises for asynchronous operations | Promises]] provide a structured way to handle [[Asynchronous programming and event loop in JavaScript | asynchronous operations]] <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.

### Consuming Promises

APIs like `fetch` (available in browsers and via `node-fetch` in Node.js) return [[Using promises for asynchronous operations | promises]] <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>. When fetching data from a remote server, which is always [[Asynchronous programming and event loop in JavaScript | asynchronous]], you can queue up the [[Using promises for asynchronous operations | promise]] and provide a callback with `.then()` to process the response <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.

[[Using promises for asynchronous operations | Promises]] can be chained together <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>. If a `.then()` callback returns another [[Using promises for asynchronous operations | promise]], the next `.then()` in the chain will wait for that [[Using promises for asynchronous operations | promise]] to resolve <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.

```javascript
fetch('https://api.example.com/data')
  .then(response => response.json()) // Maps response to JSON, returns a promise
  .then(data => console.log(data))   // Receives actual user data
  .catch(error => console.error('Error fetching data:', error));
```

The synchronous `console.log` would run first, then the data would be retrieved and logged <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.

### Error Handling with Promises

A significant advantage of [[Using promises for asynchronous operations | promises]] is the ability to catch all errors in a chain with a single `.catch()` function <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>. If an error is thrown anywhere in the promise chain, it will bypass subsequent `.then()` callbacks and go straight to the nearest `.catch()` callback <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>. In a callback-based system, each [[Asynchronous programming and event loop in JavaScript | asynchronous operation]] would require a separate error handler <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>.

### Creating Promises: Avoiding Blocking Code

When creating your own [[Using promises for asynchronous operations | promises]], it's common to accidentally block the main thread <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>. For example, a CPU-intensive loop will block all other code from executing if run directly on the main thread <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>.

```javascript
console.log('Before loop'); // Logs immediately
for (let i = 0; i < 1_000_000_000; i++) { /* Arbitrary blocking loop */ }
console.log('After loop'); // Logs after ~700ms delay <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>
```

Wrapping this blocking code directly inside a new `Promise` constructor doesn't necessarily offload it from the main thread <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>:

```javascript
console.log('Before promise creation');
new Promise(resolve => {
  for (let i = 0; i < 1_000_000_000; i++) { /* Blocking loop */ }
  resolve('Done');
}).then(value => console.log(value));
console.log('After promise creation');
```

The creation of the [[Using promises for asynchronous operations | promise]] and the blocking loop *still happen on the main thread* <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>. Only the `resolve` of the value happens as a micro task <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>. This means `Before promise creation` and `After promise creation` will still be separated by the blocking loop's execution time <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.

To ensure all synchronous code runs as fast as possible and to offload blocking operations, you can place the blocking code inside a `Promise.resolve().then()` callback <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>:

```javascript
console.log('Before promise resolve');
Promise.resolve().then(() => {
  for (let i = 0; i < 1_000_000_000; i++) { /* Blocking loop */ }
  console.log('Loop finished');
});
console.log('After promise resolve');
```

In this case, `Before promise resolve` and `After promise resolve` will log immediately, and `Loop finished` will log after the blocking operation completes, as it's now executing as a micro task <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.

## Utilizing Async/Await in JavaScript

[[Asyncawait in JavaScript | Async/await]] is syntactic sugar introduced in ES7 (or TypeScript) that makes [[Asynchronous programming and event loop in JavaScript | asynchronous code]] read more like synchronous code <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>. It's a significant improvement over traditional [[Using promises for asynchronous operations | promise]] chaining, especially with long chains of [[Asynchronous programming and event loop in JavaScript | asynchronous events]] <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>.

### The `async` Keyword

Putting the `async` keyword in front of a function makes that function always return a [[Using promises for asynchronous operations | promise]] <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>. Whatever value is returned inside an `async` function will automatically be resolved as a [[Using promises for asynchronous operations | promise]] of that value <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>.

```javascript
// Function that simulates a promise-based API
async function getFruit(name) {
  const fruits = {
    'pineapple': '🍍',
    'strawberry': '🍓',
    // ...
  };
  return fruits[name]; // Automatically resolved as a promise
}
```

The `async` keyword also sets up the context for using the `await` keyword within that function <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>.

### The `await` Keyword

The `await` keyword pauses the execution of an `async` function until a [[Using promises for asynchronous operations | promise]] settles (resolves or rejects) <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>. Once the [[Using promises for asynchronous operations | promise]] resolves, its fulfilled value is returned, allowing the `async` function to resume <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>.

Consider a function to make a smoothie from multiple fruits:

```javascript
async function makeSmoothie() {
  const a = await getFruit('pineapple'); // Pauses until pineapple resolves
  const b = await getFruit('strawberry'); // Pauses until strawberry resolves
  return [a, b];
}
```

[[Asyncawait in JavaScript | Async/await]] makes it easier to share resolved values between multiple steps in an [[Asynchronous programming and event loop in JavaScript | asynchronous]] workflow, which can be difficult with traditional [[Using promises for asynchronous operations | promise]] chains <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>.

### Concurrency with `async/await` and `Promise.all()`

A common mistake when [[Utilizing async await in JavaScript | using async/await]] is failing to run independent [[Asynchronous programming and event loop in JavaScript | asynchronous operations]] concurrently <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a>. The example above for `makeSmoothie` executes sequentially: it waits for the pineapple to resolve, *then* it fetches the strawberry <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>. This is only necessary if one operation's value depends on the previous one (e.g., getting a user ID before fetching user data) <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>.

If operations are independent, `Promise.all()` should be used to run them concurrently <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>. `Promise.all()` takes an array of [[Using promises for asynchronous operations | promises]] and resolves when all of them have resolved, returning their values in an array at their respective indices <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>.

```javascript
async function makeSmoothieConcurrent() {
  // Initiates both promises at the same time
  const pineapplePromise = getFruit('pineapple');
  const strawberryPromise = getFruit('strawberry');

  // Waits for both to resolve concurrently
  const [a, b] = await Promise.all([pineapplePromise, strawberryPromise]);
  return [a, b];
}
```

This significantly improves performance by allowing independent [[Asynchronous programming and event loop in JavaScript | asynchronous operations]] to run in parallel <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>.

### Error Handling with `try-catch`

[[Asyncawait in JavaScript | Async/await]] allows for error handling using traditional `try-catch` blocks, which can offer more flexibility than chaining `.catch()` callbacks <a class="yt-timestamp" data-t="00:09:07">[00:09:07]</a>. If an error is thrown within the `try` block, execution immediately jumps to the `catch` block <a class="yt-timestamp" data-t="00:09:22">[00:09:22]</a>.

```javascript
async function makeSmoothieWithErrorHandling() {
  try {
    const a = await getFruit('pineapple');
    if (!a) throw new Error('Pineapple not found!'); // Example error
    const b = await getFruit('strawberry');
    return [a, b];
  } catch (error) {
    console.error('Smoothie failed:', error); <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>
    // Option 1: Return a default value (ignores the error for the consumer)
    // return ['🍎', '🍌']; <a class="yt-timestamp" data-t="00:09:33">[00:09:33]</a>
    // Option 2: Re-throw the error (breaks the consumer's promise chain)
    throw error; <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>
  }
}
```

### Advanced `async/await` Patterns

*   **`async/await` in `map` or `forEach` Loops**: Using `await` inside `Array.prototype.map()` or `Array.prototype.forEach()` will *not* pause the function in that context; instead, all [[Using promises for asynchronous operations | promises]] will run concurrently <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>. If sequential execution is desired, a traditional `for` loop should be used <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>.

    ```javascript
    async function processItemsSequentially(ids) {
      for (const id of ids) { // Traditional for loop
        const item = await getFruit(id); // Pauses for each iteration
        console.log(`Processed: ${item}`);
      }
    }
    ```

*   **`for await...of` Loop**: If you have a [[Using promises for asynchronous operations | promise]] that resolves to an array of items, you can use `for await...of` to iterate over them directly once the array has resolved <a class="yt-timestamp" data-t="00:10:55">[00:10:55]</a>.

    ```javascript
    async function logAllFruits() {
      const fruitPromises = Promise.all([getFruit('apple'), getFruit('banana')]);
      for await (const fruit of fruitPromises) {
        console.log(fruit);
      }
    }
    ```

*   **`await` in Conditionals**: The `await` keyword can be used directly in conditional expressions, providing a concise way to handle [[Asynchronous programming and event loop in JavaScript | asynchronous]] checks <a class="yt-timestamp" data-t="00:11:14">[00:11:14]</a>.

    ```javascript
    async function checkFruitStatus(fruitName) {
      if (await getFruit(fruitName) === '🍍') {
        console.log('It's a pineapple!');
      } else {
        console.log('Not a pineapple.');
      }
    }
    ```