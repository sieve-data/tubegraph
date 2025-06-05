---
title: Installing and setting up Nodejs
videoId: ENrzD9HAZK4
---

From: [[fireship]] <br/> 

[[introduction_to_nodejs | Node.js]] is considered one of the most valuable skills for a full stack web developer <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. Despite discussions about newer runtimes like Deno, Node.js remains the recommended choice for job seekers and product builders due to its established nature <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>. Learning [[introduction_to_nodejs | Node.js]] also provides skills that largely transfer to Deno <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.

## What is Node.js?

[[introduction_to_nodejs | Node.js]] is not a programming language itself, but a runtime that enables JavaScript to run on a server <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>. Originally, JavaScript was designed in the 1990s as a simple scripting language for web browsers <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>. The initial release of [[introduction_to_nodejs | Node.js]] in 2009 revolutionized web development by making it possible to write JavaScript code on the server, allowing developers to build full-stack applications using a single language <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.

[[introduction_to_nodejs | Node.js]] is highly suitable for high-throughput applications like real-time systems and web servers due to its non-blocking, event-driven design <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>.

## How to Install Node.js

[[introduction_to_nodejs | Node.js]] can be installed on Windows, Mac, or Linux <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>. You can check if it's already installed by running `node -v` in your command line <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.

It is highly recommended to use a package called Node Version Manager (NVM) to manage different [[introduction_to_nodejs | Node.js]] versions on your system <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>. There's an NVM package for Mac and Linux, and a separate one for Windows <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>. NVM allows you to install and switch between any desired [[introduction_to_nodejs | Node.js]] version, for example: `nvm install 12.16.3` followed by `nvm use 12.16.3` <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.

## Hello World in Node.js

One way to experiment with [[introduction_to_nodejs | Node.js]] is through its REPL (Read-Eval-Print Loop) mode. Typing `node` in the command line allows you to execute JavaScript code and see the results immediately <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>. For example: `console.log('hello world')` <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>. To exit REPL mode, press `Ctrl + C` twice <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.

For executing JavaScript code from a file, the default entry point for a [[introduction_to_nodejs | Node.js]] application is `index.js` <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.
1.  Create an `index.js` file.
2.  Add `console.log('hello world')` inside it <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.
3.  Run the file from the command line using `node index.js` or simply `node .` (if `index.js` is in the current directory) <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>.

## Understanding the Node.js Runtime

While JavaScript in [[introduction_to_nodejs | Node.js]] largely behaves like JavaScript in a browser, there are key differences in its [[nodejs_runtime_and_basic_operations | runtime]]:
*   **Built-in Identifiers**: [[nodejs_runtime_and_basic_operations | Node.js]] provides global identifiers like `console` (for logging) <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>.
*   **`global` Object**: This object serves as a namespace accessible throughout the entire [[nodejs_runtime_and_basic_operations | Node.js]] process, similar to the `window` object in a browser <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.
*   **`process` Object**: This crucial global object provides access to the currently running [[introduction_to_nodejs | Node.js]] process, allowing you to check the operating system or access environment variables <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>.

### Events and Callbacks

[[introduction_to_nodejs | Node.js]] is an asynchronous, event-driven JavaScript runtime <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>. It implements an event loop, similar to web browsers, which allows intensive operations to be pushed to separate threads, ensuring fast, non-blocking operations on the main thread <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>.

You typically interact with this by listening to events and registering callback functions:
*   The `process` object emits an `exit` event before a [[introduction_to_nodejs | Node.js]] process finishes <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>. You can listen to this using `process.on('exit', callbackFunction)` <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>. The callback function executes *after* the event occurs <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>.
*   You can create custom events by importing `EventEmitter` from the built-in `events` module <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>. Instantiate `EventEmitter`, register a callback with `emitter.on('eventName', callback)`, and then trigger it with `emitter.emit('eventName')` <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a>.

## File System (FS) Module

[[introduction_to_nodejs | Node.js]] includes a built-in file system module (`fs`) for reading, writing, and deleting files <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>. It supports both blocking (synchronous) and non-blocking (asynchronous) operations:

*   **Synchronous (Blocking)**: Functions ending in `Sync` (e.g., `fs.readFileSync`) will complete their work before any other code can run <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>.
    ```javascript
    const { readFileSync } = require('fs');
    const data = readFileSync('hello.txt', 'utf8');
    console.log(data);
    console.log('This runs after the file is read'); // This will wait
    ```
*   **Asynchronous (Non-Blocking) with Callbacks**: Functions like `fs.readFile` take a callback as a third argument, which executes when the operation is complete. This allows other code to run concurrently <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>.
    ```javascript
    const { readFile } = require('fs');
    readFile('hello.txt', 'utf8', (err, data) => {
        if (err) console.error(err);
        else console.log(data);
    });
    console.log('This runs immediately'); // This will likely run first
    ```
*   **Asynchronous (Non-Blocking) with Promises**: Promises offer a cleaner way to handle asynchronous operations compared to callbacks, especially when chaining multiple operations <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>. The `fs.promises` namespace provides promise-based versions of file system functions <a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a>.
    ```javascript
    const { readFile } = require('fs').promises; // Import from fs.promises
    async function readMyFile() {
        try {
            const data = await readFile('hello.txt', 'utf8');
            console.log(data);
        } catch (err) {
            console.error(err);
        }
    }
    readMyFile();
    console.log('This runs immediately');
    ```
    This `async/await` syntax makes asynchronous code much easier to read and manage <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>.

## [[understanding_nodejs_modules_and_packages | Modules and Packages]]

A [[understanding_nodejs_modules_and_packages | module]] in [[introduction_to_nodejs | Node.js]] is essentially a JavaScript file that exports its code <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>. [[introduction_to_nodejs | Node.js]] has many built-in [[understanding_nodejs_modules_and_packages | modules]] like `fs` and `events` <a class="yt-timestamp" data-t="00:09:07">[00:09:07]</a>.

*   **Exporting Custom Modules**: In a module file, you use `module.exports` to define what your [[understanding_nodejs_modules_and_packages | module]] provides <a class="yt-timestamp" data-t="00:09:54">[00:09:54]</a>.
    ```javascript
    // myModule.js
    module.exports.myFunction = () => console.log('Hello from module');
    module.exports.myVariable = 123;
    ```
*   **Importing Custom Modules**: The traditional way to import a [[understanding_nodejs_modules_and_packages | module]] in [[introduction_to_nodejs | Node.js]] is using the `require` function <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>.
    ```javascript
    // index.js
    const myModule = require('./myModule'); // Path to your module
    myModule.myFunction(); // Outputs: Hello from module
    console.log(myModule.myVariable); // Outputs: 123
    ```
    While [[introduction_to_nodejs | Node.js]] recently added support for ES [[understanding_nodejs_modules_and_packages | modules]] (import/export syntax), much existing [[introduction_to_nodejs | Node.js]] code still uses `require` <a class="yt-timestamp" data-t="00:09:19">[00:09:19]</a>.

### Node Package Manager (NPM)

NPM is a tool installed alongside [[introduction_to_nodejs | Node.js]] that allows you to install and manage remote [[understanding_nodejs_modules_and_packages | packages]] for use in your code <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>.

1.  **Initialize Project**: Run `npm init -y` in your command line <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>. This creates a `package.json` file in your project's root, which tracks metadata and dependencies <a class="yt-timestamp" data-t="00:10:36">[00:10:36]</a>.
2.  **Install Packages**: Use `npm install <package-name>` to install a third-party [[understanding_nodejs_modules_and_packages | module]]. For example, `npm install Express` <a class="yt-timestamp" data-t="00:10:48">[00:10:48]</a>.
    *   Installing a package adds it to the `dependencies` object in `package.json` and creates a `node_modules` directory where the package's source code resides <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>.
    *   You should never manually modify files within `node_modules` <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>.
3.  **Import Installed Packages**: You can import installed packages by their name using `require` <a class="yt-timestamp" data-t="00:11:33">[00:11:33]</a>.
    ```javascript
    const express = require('express');
    const app = express();
    // ... use express app
    ```

## Building a Full Stack Web Application with Express

This section outlines how to set up a basic full-stack web application using [[setting_up_a_nodejs_and_express_environment | Express]], a popular third-party [[understanding_nodejs_modules_and_packages | Node.js module]] <a class="yt-timestamp" data-t="00:11:41">[00:11:41]</a>.

1.  **Create an Express App**:
    ```javascript
    const express = require('express');
    const app = express();
    ```
2.  **Define Endpoints**: Use `app.get()` to set up a URL endpoint for HTTP GET requests. The first argument is the URL path (e.g., `/` for the root), and the second is a callback function with `request` (req) and `response` (res) parameters <a class="yt-timestamp" data-t="00:12:21">[00:12:21]</a>.
    ```javascript
    const { readFile } = require('fs').promises; // Using promises for cleaner code

    app.get('/', async (req, res) => {
        try {
            const html = await readFile('./home.html', 'utf8');
            res.send(html);
        } catch (err) {
            res.status(500).send('Server Error');
        }
    });
    ```
    This example reads an `home.html` file and sends its content back to the client <a class="yt-timestamp" data-t="00:13:00">[00:13:00]</a>.

3.  **Start the Server**:
    ```javascript
    const PORT = process.env.PORT || 3000; // Use environment variable or default to 3000
    app.listen(PORT, () => console.log(`App available on http://localhost:${PORT}`));
    ```
    To start the app, run `node .` from the command line in your project directory <a class="yt-timestamp" data-t="00:14:06">[00:14:06]</a>. You can then access it in your browser, typically at `http://localhost:3000` <a class="yt-timestamp" data-t="00:14:09">[00:14:09]</a>.

## [[building_and_deploying_a_nodejs_full_stack_application | Deploying a Node.js Application]]

A simple and free way to [[building_and_deploying_a_nodejs_full_stack_application | deploy]] your [[introduction_to_nodejs | Node.js]] application to the cloud is using Google App Engine's standard environment for Node.js (up to version 12) <a class="yt-timestamp" data-t="00:14:59">[00:14:59]</a>. This service provides a scalable server in the cloud <a class="yt-timestamp" data-t="00:15:09">[00:15:09]</a>.

**Prerequisites**:
*   A Google Cloud Platform account <a class="yt-timestamp" data-t="00:15:16">[00:15:16]</a>.
*   Google Cloud command-line tools installed locally <a class="yt-timestamp" data-t="00:15:18">[00:15:18]</a>.

**Deployment Steps**:
1.  **Create `app.yaml`**: In your source code root, create `app.yaml` to configure your cloud server <a class="yt-timestamp" data-t="00:15:26">[00:15:26]</a>. Specify the runtime:
    ```yaml
    runtime: nodejs12
    ```
2.  **Define a Start Script in `package.json`**: App Engine looks for a `start` script in your `package.json` to run your application <a class="yt-timestamp" data-t="00:15:37">[00:15:37]</a>.
    ```json
    "scripts": {
        "start": "node ."
    }
    ```
3.  **Deploy**: Open your command line and run `gcloud app deploy` <a class="yt-timestamp" data-t="00:15:47">[00:15:47]</a>. After deployment, you will receive a public URL to access your application <a class="yt-timestamp" data-t="00:15:51">[00:15:51]</a>.