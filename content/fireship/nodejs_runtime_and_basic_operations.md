---
title: Nodejs runtime and basic operations
videoId: ENrzD9HAZK4
---

From: [[fireship]] <br/> 

## What is Node.js?
[[introduction_to_nodejs | Node.js]] is not a programming language, but rather a runtime environment that allows you to run [[basics_of_javascript_and_its_history | JavaScript]] on a server <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>. Historically, [[basics_of_javascript_and_its_history | JavaScript]] was designed in the 1990s as a simple scripting language to run only in the browser <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>. Before the initial release of [[introduction_to_nodejs | Node.js]] in 2009, it was impossible to write [[basics_of_javascript_and_its_history | JavaScript]] code on the server, where languages like Java or PHP were typically used <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.

[[introduction_to_nodejs | Node.js]] revolutionized web development by enabling developers to write a full-stack application in a single language <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>. This allows [[basics_of_javascript_and_its_history | JavaScript]] to be used on the server, where it could previously only be written in a web browser <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>.

### Use Cases
[[introduction_to_nodejs | Node.js]] is well-suited for applications that require high throughput, such as real-time applications and web servers <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>.

## Installing and Running Node.js
To check if [[introduction_to_nodejs | Node.js]] is installed on your system, you can run `node -v` from the command line <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>. It is recommended to use a package called Node Version Manager (NVM) to manage different [[introduction_to_nodejs | Node.js]] versions <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>.

### Basic Operations
#### REPL Mode
One way to interact with [[introduction_to_nodejs | Node.js]] is through its REPL (Read-Eval-Print Loop) mode <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>. By typing `node` into the command line, you can run [[basics_of_javascript_and_its_history | JavaScript]] code directly and see the results <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>.
```bash
$ node
> console.log("hello world")
hello world
undefined
>
```
To exit the REPL, press `Ctrl + C` twice <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.

#### Executing Files
In most cases, you will execute [[basics_of_javascript_and_its_history | JavaScript]] code from a file <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>. The default entry point into a [[introduction_to_nodejs | Node.js]] application is typically an `index.js` file <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.

To run a [[basics_of_javascript_and_its_history | JavaScript]] file:
1.  Create a file, e.g., `index.js`, and add your code:
    ```javascript
    // index.js
    console.log("hello world");
    ```
2.  Execute it from the command line:
    ```bash
    $ node index.js
    # or if it's index.js in the current directory:
    $ node .
    ```
This will output `hello world` <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>.

## Understanding the Node.js Runtime
While [[basics_of_javascript_and_its_history | JavaScript]] works similarly in the browser and [[introduction_to_nodejs | Node.js]], there are important differences <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>.

### Built-in Globals
[[introduction_to_nodejs | Node.js]] provides a handful of built-in global identifiers <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>:
*   `console`: Used for logging values to the terminal <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.
*   `global`: An object that serves as a namespace available throughout the entire [[introduction_to_nodejs | Node.js]] process <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>. It is comparable to the `window` object in a browser <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>.
*   `process`: Gives access to the currently running [[introduction_to_nodejs | Node.js]] process. It can be used to check the current platform/operating system or retrieve environment variables <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>.

### [[asynchronous_programming_in_javascript | Asynchronous Programming]] and Event Loop
[[introduction_to_nodejs | Node.js]] is described as an [[asynchronous_programming_in_javascript | asynchronous]], event-driven [[basics_of_javascript_and_its_history | JavaScript]] runtime <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>. It implements an event loop, similar to a web browser, which allows [[introduction_to_nodejs | Node.js]] to offload intensive operations to separate threads <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>. Only very fast, non-blocking operations occur on the main thread, making [[introduction_to_nodejs | Node.js]] "non-blocking" <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.

#### Events and Callbacks
In [[introduction_to_nodejs | Node.js]], you often listen to events and respond with callback functions <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.
*   **Built-in Events**: The `process` global emits an `exit` event before a [[introduction_to_nodejs | Node.js]] process finishes. You can listen to this event using `process.on('exit', callbackFunction)` <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>. The callback function is not called immediately but only after the event occurs <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>.
*   **Custom Events**: You can create your own custom events using the `EventEmitter` from the built-in `events` [[understanding_nodejs_modules_and_packages | module]] <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>.
    ```javascript
    const EventEmitter = require('events'); // Import EventEmitter
    const myEmitter = new EventEmitter(); // Instantiate a custom event emitter

    myEmitter.on('lunch', () => { // Register a callback for the 'lunch' event
      console.log('Time for lunch!');
    });

    myEmitter.emit('lunch'); // Trigger the 'lunch' event, running the callback
    myEmitter.emit('lunch'); // Trigger again
    ```
    This event-driven style is especially useful for CPU-intensive tasks <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.

#### File System Operations (`fs` module)
[[introduction_to_nodejs | Node.js]] has a built-in file system [[understanding_nodejs_modules_and_packages | module]] called `fs` that can read, write, and delete files <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>. It offers both blocking (synchronous) and non-blocking (asynchronous) methods.

*   **Blocking (Synchronous)**: Functions ending in `Sync` will complete all their work before any other code can run, potentially blocking the main thread <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>.
    ```javascript
    const fs = require('fs');

    console.log('Reading file synchronously...');
    const data = fs.readFileSync('hello.txt', 'utf8'); // Blocks execution
    console.log('File content:', data);
    console.log('Finished reading file synchronously.');
    ```
    In this example, the second `console.log` will not run until the file has been fully read <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>.

*   **Non-blocking (Asynchronous) with Callbacks**: This approach uses callbacks to prevent blocking, allowing other code to execute while the file operation is in progress <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>.
    ```javascript
    const fs = require('fs');

    console.log('Reading file asynchronously...');
    fs.readFile('hello.txt', 'utf8', (err, data) => { // Non-blocking
      if (err) {
        console.error('Error reading file:', err);
        return;
      }
      console.log('File content (from callback):', data);
    });
    console.log('Finished reading file asynchronously (this runs first).');
    ```
    When run, "Finished reading file asynchronously" will log *before* "File content (from callback)" <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>.

*   **Non-blocking (Asynchronous) with Promises/Async-Await**: Promises and the `async`/`await` syntax provide a cleaner way to handle [[asynchronous_programming_in_javascript | asynchronous]] operations compared to nested callbacks, avoiding "callback hell" <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>.
    ```javascript
    const fsPromises = require('fs').promises; // Import promises-based functions

    async function readFileWithPromises() {
      try {
        console.log('Reading file with promises...');
        const data = await fsPromises.readFile('hello.txt', 'utf8'); // Await resolves the promise
        console.log('File content (from async/await):', data);
      } catch (err) {
        console.error('Error reading file:', err);
      }
      console.log('Finished reading file with promises.');
    }

    readFileWithPromises();
    console.log('This line might run before the file content is logged.');
    ```
    This syntax makes [[asynchronous_programming_in_javascript | asynchronous]] code much more readable, especially with multiple asynchronous calls <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>.

## Modules and Packages
[[understanding_nodejs_modules_and_packages | Modules]] are [[basics_of_javascript_and_its_history | JavaScript]] files that export their code <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>. [[introduction_to_nodejs | Node.js]] has many built-in [[understanding_nodejs_modules_and_packages | modules]] like `fs` and `events` <a class="yt-timestamp" data-t="00:09:07">[00:09:07]</a>.

### CommonJS Modules (`require`/`module.exports`)
The traditional way to import a [[understanding_nodejs_modules_and_packages | module]] in [[introduction_to_nodejs | Node.js]] is using the `require` function <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>.
*   **Exporting**: In a [[understanding_nodejs_modules_and_packages | module]] file, you can add properties to the `module.exports` object or redefine it to export values <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>.
    ```javascript
    // myModule.js
    module.exports.greeting = 'Hello from my module!';
    module.exports.add = (a, b) => a + b;

    // Or redefine module.exports
    // module.exports = {
    //   greeting: 'Hello from my module!',
    //   add: (a, b) => a + b
    // };
    ```
*   **Importing**: In another file, use `require` to import the [[understanding_nodejs_modules_and_packages | module]] <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>.
    ```javascript
    // index.js
    const myModule = require('./myModule');
    console.log(myModule.greeting); // Output: Hello from my module!
    console.log(myModule.add(2, 3)); // Output: 5
    ```
While [[introduction_to_nodejs | Node.js]] now supports ES [[understanding_nodejs_modules_and_packages | Modules]] (`import`/`export` syntax), most existing [[introduction_to_nodejs | Node.js]] code still uses `require`, making it essential to understand <a class="yt-timestamp" data-t="00:09:19">[00:09:19]</a>.

### Node Package Manager (NPM)
NPM is a tool used to install and manage remote packages (third-party [[understanding_nodejs_modules_and_packages | modules]]) for use in your own code <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>. It comes installed with [[introduction_to_nodejs | Node.js]] <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>.

#### Initializing a Project
To manage project dependencies, initialize a `package.json` file in your project's root directory:
```bash
$ npm init -y
```
This creates a `package.json` file that contains metadata about your project and tracks its dependencies <a class="yt-timestamp" data-t="00:10:36">[00:10:36]</a>.

#### Installing Packages
Use `npm install <package-name>` to install a package. For example, to install [[setting_up_a_nodejs_and_express_environment | Express]], a popular web application framework:
```bash
$ npm install express
```
This command will:
1.  Add `express` to the `dependencies` object in `package.json`, along with its version <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>.
2.  Download the package's source code into a `node_modules` directory in your project <a class="yt-timestamp" data-t="00:11:14">[00:11:14]</a>. You should never modify files directly in `node_modules` <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>.

Once installed, you can import the package by name in your [[basics_of_javascript_and_its_history | JavaScript]] code using `require` <a class="yt-timestamp" data-t="00:11:33">[00:11:33]</a>:
```javascript
const express = require('express');
const app = express();
// ... use the express app
```