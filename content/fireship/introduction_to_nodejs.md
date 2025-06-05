---
title: Introduction to Nodejs
videoId: ENrzD9HAZK4
---

From: [[fireship]] <br/> 

Node.js is considered one of the most valuable skills for a full-stack web developer <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. It is an established technology <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a> and its skills are largely transferable to other runtimes like Deno <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. The best way to learn Node.js is by building something meaningful from scratch <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.

## What is Node.js?

Node.js is not a programming language <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>; instead, it is a runtime that allows JavaScript to run on a server <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>. Historically, JavaScript was designed in the 1990s to run solely in the browser as a simple scripting language <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>. The initial release of Node.js in 2009 revolutionized web development by enabling JavaScript code to run on the server, a capability previously limited to languages like Java or PHP <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>. This innovation allowed web developers to build full-stack applications using a single language <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.

Node.js is well-suited for high-throughput applications such as real-time systems and web servers <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>.

## [[installing_and_setting_up_nodejs | Installing and Setting up Node.js]]

Node.js can be [[installing_and_setting_up_nodejs | installed on Windows, Mac, or Linux]] <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>. You can check if Node.js is installed by running `node -v` in the command line <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.

It is recommended to use Node Version Manager (NVM) for managing different Node.js versions on your system <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>. NVM has packages for Mac and Linux, and a separate package for Windows <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>. With NVM, you can install specific Node.js versions, for example, `nvm install 12.16.3`, and then use that version as your runtime with `nvm use` <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.

## Basic Operations

### Hello World

You can interact with Node.js in REPL (Read-Eval-Print Loop) mode by typing `node` into the command line <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>. For example, `console.log('hello world')` will print the value <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>. To exit REPL mode, press Ctrl+C twice <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.

To execute JavaScript code from a file, the default entry point for a Node.js application is `index.js` <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.
You can create an `index.js` file with `console.log('hello world')` inside <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>. This code can be run using the `node` command followed by the path to the file, or simply the parent directory if it's `index.js` <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>.

### Understanding the [[nodejs_runtime_and_basic_operations | Node.js Runtime]]

While JavaScript largely behaves the same in Node.js as in the browser, there are key differences <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>.

Node.js has built-in global identifiers:
*   **`console`**: Used for logging values to the terminal <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>.
*   **`global`**: An object acting as a namespace available throughout the entire Node.js process <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>. It can be compared to the `window` object in a browser <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>.
*   **`process`**: Provides access to the currently running Node.js process <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>. It can be used to check the operating system or retrieve environment variables <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.

### Events in Node.js

Node.js is described as an asynchronous, event-driven JavaScript runtime <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>. It implements an event loop, similar to web browsers, which allows intensive operations to be pushed to separate threads <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>. This design ensures that only fast, non-blocking operations occur on the main thread, making Node.js a "non-blocking" runtime <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.

In Node.js, you often listen to events using callbacks <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.
*   **Built-in Events**: The `process` global emits an `exit` event before a Node.js process finishes <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>. You can listen to this event using `process.on('exit', callbackFunction)` <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>. The callback function runs only after the event occurs <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>.
*   **Custom Events**: You can create custom events using the `EventEmitter` class from the built-in `events` module <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>. After instantiating `EventEmitter` and registering a callback with `emitter.on('eventName', callback)`, you can trigger the event with `emitter.emit('eventName')` <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a>. This event-driven programming style is particularly useful for CPU-intensive tasks <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.

### File System

Node.js includes a built-in file system module called `fs` <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>. It can read, write, and delete files in both blocking (synchronous) and non-blocking (asynchronous) ways <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>.

*   **Blocking (Synchronous) Operations**: Functions ending in `Sync` (e.g., `readFileSync`) will complete all their work before any other code can run <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>. For example, using `readFileSync` will prevent subsequent console logs from executing until the file has been fully read <a class="yt-timestamp" data-t="00:07:38">[00:07:38]</a>.
*   **Non-blocking (Asynchronous) Operations with Callbacks**: To make code non-blocking, you can use functions like `readFile` <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>. A callback function is passed as a third argument, which receives an error object or the file content upon completion <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>. Node.js registers the callback, executes the rest of the script, and then runs the callback when the file is read <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>.
*   **Non-blocking (Asynchronous) Operations with Promises**: Promises offer a cleaner, non-blocking alternative to callbacks <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>. You can import file system functions from `fs.promises` (e.g., `readFile` from `fs.promises`) <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>. With `async/await` syntax, you can write more readable asynchronous code, particularly when handling multiple asynchronous calls <a class="yt-timestamp" data-t="00:08:45">[00:08:45]</a>.

### [[understanding_nodejs_modules_and_packages | Modules and Packages]]

A module is a JavaScript file that exports its code <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>. Node.js includes many built-in [[understanding_nodejs_modules_and_packages | modules]], such as `fs` and `events` <a class="yt-timestamp" data-t="00:09:07">[00:09:07]</a>.

*   **CommonJS Modules (`require`/`module.exports`)**: The traditional way to import a module in Node.js is using the `require` function <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>. To make a module useful, you export code from it using `module.exports` <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a>. You can add properties to `module.exports` or redefine it as a new object <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>.
*   **ES Modules (`import`/`export`)**: Node.js also supports ES Modules with `import`/`export` syntax, but much of the existing vanilla JavaScript code still uses `require` <a class="yt-timestamp" data-t="00:09:19">[00:09:19]</a>.

*   **Node Package Manager (npm)**: The primary tool for using third-party code is npm <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>. npm is installed automatically with Node.js <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>.
    *   **`npm init`**: Running `npm init -y` in the command line creates a `package.json` file in your application's root directory <a class="yt-timestamp" data-t="00:10:28">[00:10:28]</a>. This file tracks your project's metadata and dependencies <a class="yt-timestamp" data-t="00:10:39">[00:10:39]</a>.
    *   **`npm install`**: Use `npm install [package_name]` to install remote [[understanding_nodejs_modules_and_packages | packages]] <a class="yt-timestamp" data-t="00:10:48">[00:10:48]</a>. For example, `npm install express` installs the Express framework <a class="yt-timestamp" data-t="00:10:51">[00:10:51]</a>.
    *   **`package.json` and `node_modules`**: Installing a package adds it to the `dependencies` object in `package.json`, pinning it to a specific version <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>. The raw source code for dependencies is stored in the `node_modules` directory <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>, which should generally not be modified manually <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>. Once installed, you can import a package by name using `require` <a class="yt-timestamp" data-t="00:11:32">[00:11:32]</a>.

## Building a Full Stack Web Application

You can use Node.js to [[setting_up_a_nodejs_and_express_environment | set up a Node.js and Express environment]] to [[building_and_deploying_a_nodejs_full_stack_application | build a full stack web application]] <a class="yt-timestamp" data-t="00:11:41">[00:11:41]</a>.

### Setting up Express

1.  **Create an Express App**: Begin by creating an instance of an Express application <a class="yt-timestamp" data-t="00:11:58">[00:11:58]</a>.
    ```javascript
    const express = require('express');
    const app = express();
    ```
2.  **Define Endpoints**: Express allows you to create URLs and endpoints that users can navigate to <a class="yt-timestamp" data-t="00:12:00">[00:12:00]</a>. For a GET request (when a user navigates to a URL), use `app.get()` <a class="yt-timestamp" data-t="00:12:11">[00:12:11]</a>. The first argument is the URL (e.g., `/` for the root), and the second is a callback function that handles the request <a class="yt-timestamp" data-t="00:12:21">[00:12:21]</a>. This callback function receives `request` and `response` objects <a class="yt-timestamp" data-t="00:12:42">[00:12:42]</a>.
    ```javascript
    app.get('/', (req, res) => {
        // Handle request here
    });
    ```
3.  **Read and Serve HTML**: To serve HTML, read an HTML file from your file system using Node's `fs` module (e.g., `fs.readFile` or `fs.promises.readFile`) <a class="yt-timestamp" data-t="00:13:04">[00:13:04]</a>.
    ```javascript
    const fs = require('fs').promises; // Using promises for cleaner async
    // ... inside app.get callback
    try {
        const htmlContent = await fs.readFile('home.html', 'utf8');
        res.send(htmlContent);
    } catch (err) {
        console.error(err);
        res.status(500).send('Server Error');
    }
    ```
    This example uses `fs.promises` and `async/await` syntax to avoid "callback hell" <a class="yt-timestamp" data-t="00:14:14">[00:14:14]</a>.

4.  **Start the Server**: Tell your Express application to start listening for incoming requests by defining a port (often from an environment variable) and calling `app.listen()` <a class="yt-timestamp" data-t="00:14:48">[00:14:48]</a>.
    ```javascript
    const PORT = process.env.PORT || 3000;
    app.listen(PORT, () => {
        console.log(`App available on localhost:${PORT}`);
    });
    ```
    The application can be started from the command line by running `node .` (assuming `index.js` as the entry point) <a class="yt-timestamp" data-t="00:14:06">[00:14:06]</a>.

## [[building_and_deploying_a_nodejs_full_stack_application | Building and Deploying a Node.js Full Stack Application]]

One way to [[building_and_deploying_a_nodejs_full_stack_application | deploy a Node.js application]] to the cloud for public access is using Google App Engine <a class="yt-timestamp" data-t="00:14:58">[00:14:58]</a>.

### Deploying with Google App Engine

1.  **Google Cloud Setup**: You need a Google Cloud Platform account and the Google Cloud command-line tools installed locally <a class="yt-timestamp" data-t="00:15:14">[00:15:14]</a>.
2.  **`app.yaml`**: Create an `app.yaml` file in your source code to configure the cloud server <a class="yt-timestamp" data-t="00:15:24">[00:15:24]</a>. Specify the runtime, for example, `runtime: nodejs12` <a class="yt-timestamp" data-t="00:15:31">[00:15:31]</a>.
3.  **`start` Script**: App Engine looks for a `start` script in your `package.json` to run your code <a class="yt-timestamp" data-t="00:15:35">[00:15:35]</a>. Define a start script like `"start": "node ." ` to launch your Express app <a class="yt-timestamp" data-t="00:15:39">[00:15:39]</a>.
4.  **Deploy**: Open the command line and run `gcloud app deploy` <a class="yt-timestamp" data-t="00:15:45">[00:15:45]</a>. After deployment, a URL will be provided to access your application publicly <a class="yt-timestamp" data-t="00:15:49">[00:15:49]</a>.