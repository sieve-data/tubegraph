---
title: Building and deploying a Nodejs full stack application
videoId: ENrzD9HAZK4
---

From: [[fireship]] <br/> 

[[introduction_to_nodejs | Node.js]] is considered one of the most valuable skills for a full-stack web developer and is expected to remain relevant for the foreseeable future <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. Despite discussions about newer runtimes like Deno, [[introduction_to_nodejs | Node.js]] remains the go-to choice for building products or securing jobs due to its established nature <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. If you learn [[introduction_to_nodejs | Node.js]] today, those skills will largely transfer to Deno in the future <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.

This guide covers the basics of [[introduction_to_nodejs | Node.js]] in seven steps and then combines them to build and deploy a full-stack web application to the cloud <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a> <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>.

## What is Node.js?

[[introduction_to_nodejs | Node.js]] is not a programming language itself, but rather a runtime that enables you to execute JavaScript on a server <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>. Originally, JavaScript was designed in the 1990s as a simple scripting language for browsers <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>. The initial release of [[introduction_to_nodejs | Node.js]] in 2009 revolutionized web development by making it possible to write server-side JavaScript code, allowing developers to create full-stack applications in a single language, unlike previous server languages such as Java or PHP <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a> <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.

A typical use case involves a client sending a request to a server, which uses [[introduction_to_nodejs | Node.js]] to handle the request, read files from the file system, and respond back to the client with HTML <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.

## Installing Node.js

[[installing_and_setting_up_nodejs | Node.js]] can be installed on Windows, Mac, or Linux <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>. You can check if it's installed by running `node -v` in your command line <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>. It's recommended to use a package called Node Version Manager (NVM) to manage different [[installing_and_setting_up_nodejs | Node.js]] versions on your system, which is available for Mac/Linux and as a separate package for Windows <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>. For example, you can install a specific version with `nvm install 12.16.3` and then use it with `nvm use 12.16.3` <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.

## Hello World

To run basic JavaScript code in [[introduction_to_nodejs | Node.js]], you can use REPL (Read-Eval-Print Loop) mode by typing `node` into the command line <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>. For example, `console.log('hello world')` will print the output <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.

For executing code from a file, the default entry point for a [[introduction_to_nodejs | Node.js]] application is `index.js` <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.
1.  Create an `index.js` file <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>.
2.  Add `console.log('hello world')` inside the file <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>.
3.  Run the code from your command line using `node index.js` or simply `node .` if `index.js` is in the current directory <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>.

## Understanding the Node.js Runtime

While JavaScript functions similarly in [[introduction_to_nodejs | Node.js]] as it does in a browser, there are crucial differences <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>. [[introduction_to_nodejs | Node.js]] provides built-in global identifiers:
*   `console`: Used for logging values to the terminal <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.
*   `global`: An object available throughout the entire [[introduction_to_nodejs | Node.js]] process, comparable to the `window` object in a browser <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.
*   `process`: Provides access to the currently running [[introduction_to_nodejs | Node.js]] process, allowing checks for the operating system or environment variables <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>.

## How Events Work in Node.js

[[introduction_to_nodejs | Node.js]] is often described as an asynchronous, event-driven JavaScript runtime <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>. It implements an event loop, similar to web browsers, which allows it to offload intensive operations to separate threads <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>. This design means only fast, non-blocking operations occur on the main thread, making [[introduction_to_nodejs | Node.js]] highly suitable for high-throughput applications like real-time systems and web servers <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.

You'll primarily interact with this by listening to events and using callbacks <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>. For example, the `process` global emits an `exit` event before a [[introduction_to_nodejs | Node.js]] process finishes <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>. You can register a callback function to run when this event occurs using `process.on('exit', callbackFunction)` <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>.

You can also create custom events using the built-in `EventEmitter` module <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>:
1.  Import `EventEmitter` from the `events` module: `const EventEmitter = require('events');` <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>.
2.  Create an instance: `const eventEmitter = new EventEmitter();` <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a>.
3.  Register a callback for a custom event (e.g., `lunch`): `eventEmitter.on('lunch', () => console.log('Lunch time!'));` <a class="yt-timestamp" data-t="00:06:35">[00:06:35]</a>.
4.  Emit the event to trigger the callback: `eventEmitter.emit('lunch');` <a class="yt-timestamp" data-t="00:06:38">[00:06:38]</a>.

## The File System Module (`fs`)

[[introduction_to_nodejs | Node.js]] includes a built-in file system module (`fs`) that allows you to read, write, and delete files <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>. Operations can be blocking (synchronous) or non-blocking (asynchronous) <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>.

*   **Blocking (Synchronous) Read**: `fs.readFileSync(path, encoding)` <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>. This function will block the execution of subsequent code until the file read operation is complete <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.
*   **Non-Blocking (Asynchronous) Read with Callbacks**: `fs.readFile(path, encoding, callback)` <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>. The callback function receives an error object (if any) and the file's text <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>. [[introduction_to_nodejs | Node.js]] registers the callback, continues executing the rest of the script, and then runs the callback once the file is read <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>.
*   **Non-Blocking (Asynchronous) Read with Promises**: `fs.promises.readFile(path, encoding)` <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>. This returns a Promise, allowing for cleaner code using `async/await` syntax, especially with multiple asynchronous calls <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a> <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>.

## Modules and npm

A module in [[introduction_to_nodejs | Node.js]] is a JavaScript file that exports its code for use in other files <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>. [[introduction_to_nodejs | Node.js]] has many built-in modules like `fs` and `events` <a class="yt-timestamp" data-t="00:09:07">[00:09:07]</a>.

The traditional way to import a module in [[introduction_to_nodejs | Node.js]] is using the `require` function <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>. While [[introduction_to_nodejs | Node.js]] now supports ES Modules (import/export syntax), much existing vanilla JavaScript code still uses `require` <a class="yt-timestamp" data-t="00:09:19">[00:09:19]</a>.

To create your own module:
1.  Create a separate JavaScript file (e.g., `myModule.js`).
2.  In `myModule.js`, use `module.exports` to export properties or redefine the export as a new object <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>.
3.  In your `index.js` file, import it using `const myModule = require('./myModule.js');` <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>.

### Node Package Manager (npm)

npm is a tool installed with [[introduction_to_nodejs | Node.js]] that allows you to install and manage remote packages (third-party modules) <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>.

1.  **Initialize a project**: Run `npm init -y` in your command line <a class="yt-timestamp" data-t="00:10:30">[00:10:30]</a>. This creates a `package.json` file in your application's root, which tracks project metadata and dependencies <a class="yt-timestamp" data-t="00:10:36">[00:10:36]</a>.
2.  **Install a package**: Use `npm install [package-name]`, for example, `npm install express` <a class="yt-timestamp" data-t="00:10:51">[00:10:51]</a>. Express is a popular minimal web application framework <a class="yt-timestamp" data-t="00:10:53">[00:10:53]</a>.
    *   This command adds the package and its version to the `dependencies` object in `package.json` <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>.
    *   The actual source code for the dependency is saved in the `node_modules` directory <a class="yt-timestamp" data-t="00:11:14">[00:11:14]</a>. You should never directly modify files in `node_modules` <a class="yt-timestamp" data-t="00:11:18">[00:11:18]</a>.
3.  **Import in code**: Once installed, you can import the package by name: `const express = require('express');` <a class="yt-timestamp" data-t="00:11:33">[00:11:33]</a>.

## Building a Full Stack Application with Express

[[setting_up_a_nodejs_and_express_environment | Building a Node.js and Express environment]] allows you to create a typical full-stack web application where the server responds to client requests with HTML <a class="yt-timestamp" data-t="00:11:45">[00:11:45]</a>.

1.  **Create an Express app instance**: `const app = express();` <a class="yt-timestamp" data-t="00:11:58">[00:11:58]</a>.
2.  **Define a route for GET requests**: Use `app.get(url, callbackFunction)` <a class="yt-timestamp" data-t="00:12:21">[00:12:21]</a>.
    *   The first argument is the URL (e.g., `/` for the root) <a class="yt-timestamp" data-t="00:12:25">[00:12:25]</a>.
    *   The second argument is a callback function that handles the request, receiving `req` (request) and `res` (response) objects <a class="yt-timestamp" data-t="00:12:35">[00:12:35]</a>.
3.  **Read and send HTML**:
    *   Create an `home.html` file with your desired HTML markup <a class="yt-timestamp" data-t="00:13:09">[00:13:09]</a>.
    *   Inside the route's callback, import `readFile` from `fs.promises` (for promise-based asynchronous reading) <a class="yt-timestamp" data-t="00:13:16">[00:13:16]</a>.
    *   Read the HTML file using `await fs.promises.readFile('home.html', 'utf8')` <a class="yt-timestamp" data-t="00:14:41">[00:14:41]</a>.
    *   Send the HTML as a response: `res.send(htmlContent);` <a class="yt-timestamp" data-t="00:13:30">[00:13:30]</a>.
    *   Handle errors by sending a `500` status code: `res.status(500).send('Server Error');` <a class="yt-timestamp" data-t="00:13:34">[00:13:34]</a>.
4.  **Listen for incoming requests**:
    *   Define a port, usually from a [[introduction_to_nodejs | Node.js]] environment variable <a class="yt-timestamp" data-t="00:13:53">[00:13:53]</a>.
    *   Call `app.listen(port, callback)` to start the server <a class="yt-timestamp" data-t="00:13:58">[00:13:58]</a>.
    *   Log a message when the server starts, e.g., `console.log('App available on localhost:3000');` <a class="yt-timestamp" data-t="00:14:00">[00:14:00]</a>.
5.  **Run the application**: Execute `node .` from your command line <a class="yt-timestamp" data-t="00:14:06">[00:14:06]</a>. You can then access the application in your browser at `localhost:3000` <a class="yt-timestamp" data-t="00:14:10">[00:14:10]</a>.

Promises and `async/await` are highly recommended over callbacks for handling asynchronous operations, as they make complex code much more readable and help avoid "callback hell" <a class="yt-timestamp" data-t="00:14:17">[00:14:17]</a>.

## Deploying to the Cloud

To make your [[introduction_to_nodejs | Node.js]] application publicly accessible, you can deploy it to the cloud <a class="yt-timestamp" data-t="00:14:55">[00:14:55]</a>. Google App Engine offers an easy and free way to do this with a standard environment for [[introduction_to_nodejs | Node.js]] up to version 12 <a class="yt-timestamp" data-t="00:14:58">[00:14:58]</a>. It provides a server that scales automatically based on incoming traffic <a class="yt-timestamp" data-t="00:15:09">[00:15:09]</a>.

**Prerequisites**:
*   A Google Cloud Platform account <a class="yt-timestamp" data-t="00:15:16">[00:15:16]</a>.
*   Google Cloud command-line tools installed locally <a class="yt-timestamp" data-t="00:15:18">[00:15:18]</a>.

**Deployment Steps**:
1.  **Create `app.yaml`**: In your project's root directory, create an `app.yaml` file to configure your cloud server <a class="yt-timestamp" data-t="00:15:24">[00:15:24]</a>. Specify the runtime, e.g., `runtime: nodejs12` <a class="yt-timestamp" data-t="00:15:31">[00:15:31]</a>.
2.  **Define a `start` script**: In your `package.json` file, add a `start` script under the `scripts` section that runs your [[introduction_to_nodejs | Node.js]] application, e.g., `"start": "node ."` <a class="yt-timestamp" data-t="00:15:37">[00:15:37]</a>. App Engine will use this script to start your code <a class="yt-timestamp" data-t="00:15:35">[00:15:35]</a>.
3.  **Deploy**: Open your command line and run `gcloud app deploy` <a class="yt-timestamp" data-t="00:15:47">[00:15:47]</a>. After a short time, it will provide a URL where your application is publicly accessible <a class="yt-timestamp" data-t="00:15:51">[00:15:51]</a>.

For more advanced [[introduction_to_nodejs | Node.js]] and Express use cases, consider exploring further resources <a class="yt-timestamp" data-t="00:16:03">[00:16:03]</a>.