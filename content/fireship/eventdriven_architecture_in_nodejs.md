---
title: Eventdriven architecture in Nodejs
videoId: ENrzD9HAZK4
---

From: [[fireship]] <br/> 

[[introduction_to_nodejs | Node.js]] is widely described as an asynchronous, event-driven [[javascript_serverside_with_nodejs | JavaScript]] runtime <a class="yt-timestamp" data-t="05:20:10">[05:20:10]</a>. This design choice makes [[introduction_to_nodejs | Node.js]] highly suitable for high-throughput applications like real-time systems and web servers <a class="yt-timestamp" data-t="05:39:10">[05:39:10]</a>.

## The Event Loop

The [[introduction_to_nodejs | Node.js]] runtime implements an "event loop" <a class="yt-timestamp" data-t="05:24:91">[05:24:91]</a>, similar to web browsers <a class="yt-timestamp" data-t="05:26:99">[05:26:99]</a>. This mechanism allows [[introduction_to_nodejs | Node.js]] to offload intensive operations to separate threads <a class="yt-timestamp" data-t="05:29:96">[05:29:96]</a>. As a result, only fast, non-blocking operations occur on the main thread <a class="yt-timestamp" data-t="05:31:00">[05:31:00]</a>, which is why [[introduction_to_nodejs | Node.js]] is often referred to as "non-blocking" <a class="yt-timestamp" data-t="05:36:00">[05:36:00]</a>.

## Events and Callbacks

While low-level details of the event loop aren't always necessary for developers to understand <a class="yt-timestamp" data-t="05:49:00">[05:49:00]</a>, familiarity with how events and callbacks function is crucial <a class="yt-timestamp" data-t="05:51:00">[05:51:00]</a>. In [[introduction_to_nodejs | Node.js]], developers typically listen for events <a class="yt-timestamp" data-t="05:53:00">[05:53:00]</a>.

An example of a built-in event is `exit` on the `process` global object <a class="yt-timestamp" data-t="05:57:00">[05:57:00]</a>. Before a [[introduction_to_nodejs | Node.js]] process finishes, it emits this event <a class="yt-timestamp" data-t="06:01:00">[06:01:00]</a>. You can listen to this event using the `on` method and register a callback function as the second argument <a class="yt-timestamp" data-t="06:03:00">[06:03:00]</a>. This callback function will only execute *after* the `exit` event occurs in the future <a class="yt-timestamp" data-t="06:15:00">[06:15:00]</a>.

```javascript
process.on('exit', () => {
  console.log('Node.js process is about to exit!');
});
```
<a class="yt-timestamp" data-t="06:01:00">[06:01:00]</a>

## Custom Events

Beyond built-in events, you can create your own custom events using the `EventEmitter` class from the built-in `events` module <a class="yt-timestamp" data-t="06:21:00">[06:21:00]</a>.

```javascript
import { EventEmitter } from 'events'; // This uses ES Modules syntax for clarity

// Create a custom event emitter
const myEmitter = new EventEmitter();

// Register a callback for a 'lunch' event
myEmitter.on('lunch', () => {
  console.log('Lunch event occurred!');
});

// Emit the 'lunch' event, triggering the callback
myEmitter.emit('lunch'); // Logs: Lunch event occurred!
myEmitter.emit('lunch'); // Logs: Lunch event occurred!
```
<a class="yt-timestamp" data-t="06:24:00">[06:24:00]</a>
This event-driven style is highly beneficial for handling CPU-intensive tasks <a class="yt-timestamp" data-t="06:51:00">[06:51:00]</a>.

## File System and Asynchronous Operations

The built-in `fs` (file system) module in [[introduction_to_nodejs | Node.js]] provides functions for reading, writing, and deleting files <a class="yt-timestamp" data-t="06:57:00">[06:57:00]</a>. These operations can be performed in either a *blocking* (synchronous) or *non-blocking* (asynchronous) manner <a class="yt-timestamp" data-t="07:05:00">[07:05:00]</a>.

*   **Blocking (Synchronous)**: Functions ending in `Sync`, like `readFileSync`, will complete all their work before any other code can run <a class="yt-timestamp" data-t="07:22:00">[07:22:00]</a>. If reading a large file, this can cause the application to pause <a class="yt-timestamp" data-t="07:39:00">[07:39:00]</a>.
    ```javascript
    import { readFileSync } from 'fs';
    console.log('Before reading file');
    const data = readFileSync('hello.txt', 'utf8');
    console.log(data);
    console.log('After reading file'); // This runs AFTER the file is read
    ```
    <a class="yt-timestamp" data-t="07:22:00">[07:22:00]</a>

*   **Non-Blocking (Asynchronous)**: Functions like `readFile` take a callback function as an argument <a class="yt-timestamp" data-t="07:47:00">[07:47:00]</a>. [[running_and_understanding_javascript_with_nodejs | Node.js]] registers the callback and continues executing the rest of the script, running the callback only when the file operation is complete <a class="yt-timestamp" data-t="08:09:00">[08:09:00]</a>.
    ```javascript
    import { readFile } from 'fs';
    console.log('Before reading file');
    readFile('hello.txt', 'utf8', (err, data) => {
      if (err) console.error(err);
      console.log(data); // This might run AFTER 'After reading file'
    });
    console.log('After reading file');
    ```
    <a class="yt-timestamp" data-t="07:47:00">[07:47:00]</a>

## Promises and Async/Await

While callbacks are fundamental, deeply nested callbacks can lead to "callback hell," making code difficult to manage <a class="yt-timestamp" data-t="14:17:00">[14:17:00]</a>. [[async_and_await_in_javascript | Promises]] provide a cleaner, non-blocking alternative <a class="yt-timestamp" data-t="08:20:00">[08:20:00]</a>.

The `fs.promises` namespace offers promise-based versions of file system functions <a class="yt-timestamp" data-t="08:28:00">[08:28:00]</a>. Coupled with the [[async_and_await_in_javascript | `async/await` syntax]], this makes asynchronous code much more readable and concise <a class="yt-timestamp" data-t="08:47:00">[08:47:00]</a>.

```javascript
import { readFile } from 'fs/promises'; // Import from the promises namespace

async function processFile() {
  console.log('Before reading file');
  try {
    const data = await readFile('hello.txt', 'utf8');
    console.log(data);
  } catch (err) {
    console.error('Error reading file:', err);
  }
  console.log('After reading file');
}

processFile();
```
<a class="yt-timestamp" data-t="08:28:00">[08:28:00]</a>
This approach is particularly useful when handling multiple asynchronous operations within a single function <a class="yt-timestamp" data-t="08:50:00">[08:50:00]</a>.

By embracing this event-driven, non-blocking paradigm, [[introduction_to_nodejs | Node.js]] excels at handling many concurrent connections efficiently, making it a powerful tool for modern web development.