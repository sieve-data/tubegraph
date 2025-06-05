---
title: Using promises for asynchronous operations
videoId: vn3tm0quoqE
---

From: [[fireship]] <br/> 

[[JavaScript is a single-threaded concurrency model | JavaScript is a single-threaded programming language]] <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. Despite this, web operations are often blocking or time-consuming, making [[Asynchronous programming in JavaScript | asynchronous programming]] an essential skill for JavaScript developers <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. Promises are a fundamental part of [[Asynchronous programming in JavaScript | asynchronous programming]] in JavaScript, offering a cleaner way to handle asynchronous operations compared to traditional callbacks <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>.

## Promises and the Event Loop

To understand [[Asynchronous programming in JavaScript | asynchronous programming]] and Promises, it's crucial to first grasp the concept of the [[JavaScript event loop and asynchronous programming | event loop]] <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. Both the browser and Node.js continually run a [[JavaScript singlethreaded concurrency model | single-threaded event loop]] to execute your code <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

The [[JavaScript event loop and asynchronous programming | event loop]] operates by:
*   Running all synchronous code first <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.
*   Queueing up [[Asynchronous programming in JavaScript | asynchronous events]] to be called back later <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.
*   When an asynchronous operation, like fetching data from a network, finishes, it notifies the [[JavaScript event loop and asynchronous programming | event loop]] that it's ready to be called back <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.

A key distinction within the [[JavaScript event loop and asynchronous programming | event loop]] is between "macro tasks" and "micro tasks" <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>:
*   **Macro tasks** (e.g., `setTimeout`, `setInterval`) are executed on the *next* [[JavaScript event loop and asynchronous programming | event loop]] iteration <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>.
*   **Micro tasks** (e.g., a fulfilled promise) are called back *before the start of the next* [[JavaScript event loop and asynchronous programming | event loop]] <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>. This means promises have higher priority than macro tasks like `setTimeout` <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.

```javascript
console.log('Synchronous line 1'); // Executed immediately
setTimeout(() => console.log('Set timeout (macro task)'), 0); // Queued for next event loop
Promise.resolve().then(() => console.log('Promise (micro task)')); // Queued for microtask queue
console.log('Synchronous line 2'); // Executed immediately

// Expected output:
// Synchronous line 1
// Synchronous line 2
// Promise (micro task)
// Set timeout (macro task)
```
Even with a zero-millisecond delay, the `setTimeout` callback, being a macro task, is executed after the promise, which is a micro task <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.

## Consuming Promises

Promises simplify consuming asynchronous APIs.

### Basic Consumption with `.then()`
The `fetch` API is a common example of a promise-based API <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>. It returns a promise of the response when hitting an HTTP endpoint <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>.

```javascript
console.log('Starting data fetch'); // Synchronous
fetch('https://api.example.com/users/1')
    .then(response => response.json()) // Map response to JSON (also returns a promise)
    .then(data => console.log('Fetched user data:', data)); // Access actual user data
console.log('Fetch request initiated'); // Synchronous
```
In this example, `console.log('Starting data fetch')` and `console.log('Fetch request initiated')` run first, then the data is retrieved and logged <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>. Promises allow chaining multiple asynchronous operations using `.then()` callbacks, where each `.then()` returns a new promise <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.

### Error Handling with `.catch()`
A significant advantage of promises is the ability to catch all errors in a chain with a single `.catch()` function <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.

```javascript
fetch('https://api.example.com/invalid-endpoint')
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error('An error occurred:', error)); // Catches errors anywhere in the chain
```
If an error occurs anywhere in the promise chain, it will bypass subsequent `.then()` callbacks and go directly to the `.catch()` callback <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>. This prevents "callback hell" for error handling, where each callback would require a separate error handler <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>.

## Creating Promises

When creating your own promises, it's important to understand how they interact with the [[JavaScript event loop and asynchronous programming | event loop]] to avoid blocking the main thread.

### Pitfalls: Blocking the Main Thread
Wrapping synchronous, time-consuming code directly inside a new `Promise` constructor will still block the main thread during the promise's creation phase <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>. Only the resolution of the value happens as a micro task <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.

```javascript
function heavySyncOperation() {
    let i = 0;
    while (i < 1_000_000_000) { // Arbitrary billion-loop
        i++;
    }
    return 'Operation complete';
}

console.log('Before promise creation'); // First sync log
const myPromise = new Promise(resolve => {
    console.log('Inside promise constructor - still synchronous!'); // This will block
    const result = heavySyncOperation();
    resolve(result);
});
myPromise.then(value => console.log(value));
console.log('After promise creation'); // Second sync log
```
Running this code shows a delay between "Before promise creation" and "After promise creation" because `heavySyncOperation()` is still blocking the main thread during the promise's instantiation <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>.

### Correctly Ensuring Asynchronous Execution
To ensure synchronous code runs as fast as possible before an asynchronous operation, wrap the potentially blocking code inside a `Promise.resolve().then()` block. This guarantees it will be executed *after* all synchronous code in the current macro task has completed <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.

```javascript
function heavySyncOperation() {
    let i = 0;
    while (i < 1_000_000_000) {
        i++;
    }
    return 'Operation complete (async)';
}

console.log('Before promise resolve'); // First sync log
Promise.resolve().then(() => {
    console.log('Inside resolved promise - now truly asynchronous');
    return heavySyncOperation();
}).then(value => console.log(value));
console.log('After promise resolve'); // Second sync log
```
This pattern allows both synchronous `console.log` statements to execute immediately, and then the heavy operation runs asynchronously, demonstrating correct non-blocking behavior <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.

## [[Utilizing async await in JavaScript | Utilizing Async/Await in JavaScript]]

[[Utilizing async await in JavaScript | Async/await]] is syntactic sugar built on top of promises, designed to make [[Asynchronous programming in JavaScript | asynchronous code]] read more like synchronous code <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>.

### The `async` Keyword
Adding the `async` keyword in front of a function declaration makes that function always return a promise <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>. Whatever value is returned inside an `async` function will automatically be wrapped in a resolved promise <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>.

```javascript
async function getFruitEmoji(fruitName) {
    const fruits = {
        pineapple: '🍍',
        strawberry: '🍓'
    };
    return fruits[fruitName]; // Automatically wrapped in a resolved promise
}

// This is equivalent to:
function getFruitEmojiPromise(fruitName) {
    const fruits = {
        pineapple: '🍍',
        strawberry: '🍓'
    };
    return Promise.resolve(fruits[fruitName]);
}
```
The `async` keyword also sets up the context for using the `await` keyword <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>.

### The `await` Keyword
The `await` keyword, used only inside an `async` function, pauses the execution of that function until the awaited promise resolves to a value <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>.

```javascript
async function makeSmoothie() {
    const a = await getFruitEmoji('pineapple'); // Pause until pineapple emoji is retrieved
    const b = await getFruitEmoji('strawberry'); // Pause until strawberry emoji is retrieved
    return [a, b];
}
```
This pattern makes it much easier to share result values between multiple asynchronous steps, a task that can be difficult with traditional promise chaining <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>.

### Running Concurrent Promises with `Promise.all()`
A common mistake when [[Utilizing async await in JavaScript | using async/await]] is to `await` multiple independent promises sequentially, which can lead to unnecessary delays <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a>. You should only `await` one thing after another if the second value is dependent on the first <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>.

To run multiple independent promises concurrently and wait for all of them to resolve, use `Promise.all()` <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>.

```javascript
async function makeSmoothieConcurrent() {
    // Both promises are initiated immediately, then awaited together
    const pineapplePromise = getFruitEmoji('pineapple');
    const strawberryPromise = getFruitEmoji('strawberry');

    // await Promise.all waits for all promises in the array to resolve concurrently
    const [a, b] = await Promise.all([pineapplePromise, strawberryPromise]);
    return [a, b];
}
```
Using `Promise.all()` significantly improves performance by allowing asynchronous operations to happen in parallel, avoiding blocking the [[JavaScript event loop and asynchronous programming | event loop]] unnecessarily <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>.

### Error Handling with `try-catch`
[[Utilizing async await in JavaScript | Async/await]] simplifies error handling by allowing the use of traditional `try-catch` blocks around asynchronous code <a class="yt-timestamp" data-t="00:09:07">[00:09:07]</a>.

```javascript
async function riskyOperation() {
    try {
        const result1 = await getFruitEmoji('apple'); // Assume this might throw an error
        if (!result1) {
            throw new Error('Apple not found!');
        }
        const result2 = await getFruitEmoji('banana');
        return [result1, result2];
    } catch (error) {
        console.error('Caught error:', error.message);
        // Decision point:
        // 1. Re-throw the error to propagate it: throw error;
        // 2. Return a default value to handle it gracefully: return ['❌', '❌'];
    }
}
```
If an error is thrown anywhere within the `try` block, execution immediately jumps to the `catch` block <a class="yt-timestamp" data-t="00:09:22">[00:09:22]</a>.
*   **Returning a value** from the `catch` block effectively ignores the error for the consumer of the promise, providing a replacement value <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>.
*   **Throwing an error** from the `catch` block will break the consumer's promise chain and be handled by their own `catch` callback <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>.

## Advanced Promise Patterns with Async/Await

[[Utilizing async await in JavaScript | Async/await]] offers several powerful patterns for working with promises.

### Concurrency with `Array.map`
You can use `Array.map` to convert an array of IDs or items into an array of promises, which can then be resolved concurrently using `Promise.all()` <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>.

```javascript
async function getMultipleFruits(fruitNames) {
    // Array.map creates an array of promises, which can then be awaited concurrently
    const fruitPromises = fruitNames.map(name => getFruitEmoji(name));
    const fruits = await Promise.all(fruitPromises);
    return fruits;
}
```
It's important to note that `await` inside `map` or `forEach` loops won't pause the outer function's execution; instead, it will run all promises concurrently <a class="yt-timestamp" data-t="00:10:16">[00:10:16]</a>.

### Sequential Execution with Traditional `for` Loops
If you need each iteration of a loop to `await` a promise before proceeding to the next, use a traditional `for` loop within an `async` function <a class="yt-timestamp" data-t="00:10:34">[00:10:34]</a>.

```javascript
async function getFruitsSequentially(fruitNames) {
    const results = [];
    for (const name of fruitNames) {
        const fruit = await getFruitEmoji(name); // Pauses for each iteration
        results.push(fruit);
    }
    return results;
}
```

### Iterating Over Promises with `for await...of`
When you have a promise that resolves to an iterable (like an array), you can use the `for await...of` syntax to iterate over the resolved items immediately <a class="yt-timestamp" data-t="00:10:55">[00:10:55]</a>.

```javascript
async function processFruits() {
    const fruitPromises = Promise.resolve(['pineapple', 'strawberry'].map(name => getFruitEmoji(name)));
    for await (const fruit of fruitPromises) {
        console.log(`Processing ${fruit}`);
    }
}
```
This awaits the array of items to resolve first, then loops over them <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>.

### Using `await` in Conditionals
The `await` keyword can also be used directly within conditional statements, providing a concise way to evaluate promise results <a class="yt-timestamp" data-t="00:11:14">[00:11:14]</a>.

```javascript
async function checkFruit(fruitName) {
    if (await getFruitEmoji(fruitName) === '🍍') { // Awaits the result for the comparison
        console.log('It's a pineapple!');
    } else {
        console.log('Not a pineapple.');
    }
}
```
[[Utilizing async await in JavaScript | Async/await]] is considered one of the most significant improvements to [[Asynchronous programming in JavaScript | JavaScript]] for handling asynchronous operations <a class="yt-timestamp" data-t="00:11:33">[00:11:33]</a>.