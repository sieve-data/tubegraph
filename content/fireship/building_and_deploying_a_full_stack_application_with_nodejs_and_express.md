---
title: Building and deploying a full stack application with Nodejs and Express
videoId: ENrzD9HAZK4
---

From: [[fireship]] <br/> 

[[introduction_to_nodejs | Node.js]] is considered one of the most valuable skills for a full stack web developer and is expected to remain relevant for the foreseeable future <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. While newer runtimes like Deno exist and have a bright future, [[introduction_to_nodejs | Node.js]] is well-established and essential for building products or securing jobs in the current market <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. The skills learned in [[introduction_to_nodejs | Node.js]] are largely transferable to Deno <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.

This guide will cover the basics of [[running_and_understanding_javascript_with_nodejs | Node.js]] and demonstrate how to build and deploy a full stack web application to the cloud <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.

## Understanding Node.js
[[introduction_to_nodejs | Node.js]] is not a programming language itself, but a runtime that enables you to execute [[javascript_serverside_with_nodejs | JavaScript on a server]] <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>. Originally, JavaScript was designed in the 1990s to run solely within a web browser <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>. The release of [[introduction_to_nodejs | Node.js]] in 2009 revolutionized web development by making it possible to write [[javascript_serverside_with_nodejs | JavaScript code on the server]], allowing developers to build entire full stack applications using a single language <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.

[[introduction_to_nodejs | Node.js]] allows you to:
*   Handle requests from a URL <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.
*   Read files from the server's file system <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.
*   Respond back to the client with HTML <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.

## Installing Node.js
[[installing_and_managing_nodejs_versions | Node.js can be installed on Windows, Mac, or Linux]] <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>. You can check if it's installed by running `node -v` in the command line <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.

For managing different [[installing_and_managing_nodejs_versions | Node.js]] versions, it's highly recommended to use a package called Node Version Manager (NVM) <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>. NVM has separate packages for Mac/Linux and Windows <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>.
*   Install NVM by following its instructions <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.
*   Install a specific Node.js version, e.g., `nvm install 12.16.3` <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.
*   Use a specific version: `nvm use 12.16.3` <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>.

## Running "Hello World"
You can interact with [[running_and_understanding_javascript_with_nodejs | Node.js]] in REPL (Read-Eval-Print Loop) mode by typing `node` into the command line, which allows you to execute JavaScript code and see the results immediately <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>. For example, `console.log('hello world')` <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.

Typically, you'll execute JavaScript code from a file <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>. The default entry point for a [[running_and_understanding_javascript_with_nodejs | Node.js]] application is `index.js` <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.
1.  Create an `index.js` file <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>.
2.  Add `console.log('hello world');` inside `index.js` <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>.
3.  Run the file from the command line: `node index.js` or `node .` (if `index.js` is in the current directory) <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>.

## Understanding the Node.js Runtime
While JavaScript generally behaves the same in [[introduction_to_nodejs | Node.js]] as it does in a browser, there are key differences:

### Built-in Globals
[[introduction_to_nodejs | Node.js]] provides several built-in global identifiers <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>:
*   `console`: Used for logging values to the terminal <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.
*   `global`: An object serving as a namespace available throughout the entire Node.js process, similar to the `window` object in browsers <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.
*   `process`: Provides access to the currently running [[introduction_to_nodejs | Node.js]] process, useful for checking the operating system (e.g., `process.platform`) or environment variables <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>.

### Event-Driven and Asynchronous Nature
[[introduction_to_nodejs | Node.js]] is an asynchronous, event-driven JavaScript runtime <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>. It uses an event loop, similar to web browsers, to push intensive operations to separate threads <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>. This design ensures that only fast, non-blocking operations occur on the main thread, making [[introduction_to_nodejs | Node.js]] highly suitable for high-throughput applications like real-time systems and web servers <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.

As a developer, understanding events and callbacks is crucial <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>. You typically "listen" to events, which can be built-in (like the `exit` event on the `process` object) or custom <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>. A callback function is registered to run only after a specific event occurs <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>.

You can create custom events using the `EventEmitter` from Node.js's built-in `events` module <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>:
```javascript
const EventEmitter = require('events');
const eventEmitter = new EventEmitter();

eventEmitter.on('lunch', () => {
    console.log('yum');
});

eventEmitter.emit('lunch'); // Triggers the callback
eventEmitter.emit('lunch'); // Triggers again
```
This event-driven style is very effective for CPU-intensive tasks <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.

## File System Module (FS)
[[introduction_to_nodejs | Node.js]] includes a built-in `fs` module for interacting with the file system (reading, writing, deleting files) <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>. Operations can be blocking (synchronous) or non-blocking (asynchronous):

*   **Blocking (Synchronous):** Functions ending in `Sync` (e.g., `fs.readFileSync`) will complete their work before any other code can run <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>.
*   **Non-blocking (Asynchronous with Callbacks):** Functions like `fs.readFile` take a callback function as an argument, which executes once the operation is complete <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>. Node.js registers the callback, continues executing the rest of the script, and then runs the callback when the file is read <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>.

*   **Non-blocking (Asynchronous with Promises):** The `fs.promises` namespace provides promise-based versions of file system functions, which are often cleaner than callbacks, especially for multiple asynchronous operations <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>. These can be used with `async/await` syntax for more readable code <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>.

## Modules and npm
A module in [[introduction_to_nodejs | Node.js]] is a JavaScript file that exports its code <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>.
*   **Built-in Modules:** [[introduction_to_nodejs | Node.js]] has many built-in modules like `fs` and `events` <a class="yt-timestamp" data-t="00:09:07">[00:09:07]</a>.
*   **Importing Modules:** The traditional way to import a module is using the `require` function <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>. While [[introduction_to_nodejs | Node.js]] now supports ES Modules (import/export syntax), `require` is still widely used in existing [[building_applications_with_vanilla_javascript | vanilla JavaScript]] Node.js code <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>.
*   **Exporting Custom Modules:** In your module file, you use `module.exports` to add properties or redefine the exported object <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>.

### Node Package Manager (npm)
npm is a tool for installing and managing remote packages (third-party modules) to use in your code <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>. It's automatically installed with [[introduction_to_nodejs | Node.js]] <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>.

**Steps to use npm:**
1.  **Initialize Project:** Open your command line in an empty directory and run `npm init -y` <a class="yt-timestamp" data-t="00:10:30">[00:10:30]</a>. This creates a `package.json` file, which tracks your project's metadata and dependencies <a class="yt-timestamp" data-t="00:10:36">[00:10:36]</a>.
2.  **Install a Package:** To install a package, for example, Express (a popular web application framework), run `npm install express` <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>.
    *   This adds "express" to the `dependencies` object in `package.json`, pinning it to a specific version <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>.
    *   It also creates a `node_modules` directory, where the raw source code for the dependency resides <a class="yt-timestamp" data-t="00:11:14">[00:11:14]</a>. This directory should generally not be modified manually <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>.
3.  **Import Installed Package:** You can now import the installed package by its name in your JavaScript code, e.g., `require('express')` <a class="yt-timestamp" data-t="00:11:33">[00:11:33]</a>.

## Building a Full Stack Application with Express
Express is a minimal web application framework that helps in [[backend_development_and_serverside_concepts | backend development and serverside concepts]] <a class="yt-timestamp" data-t="00:11:53">[00:11:53]</a>.

1.  **Create an Express App Instance:**
    ```javascript
    const express = require('express');
    const app = express();
    ```
    An Express app allows you to create different URLs and endpoints <a class="yt-timestamp" data-t="00:12:00">[00:12:00]</a>.

2.  **Define a Route (GET Request):**
    For a typical full stack web application, the server responds with HTML when a user makes a GET request to a URL <a class="yt-timestamp" data-t="00:11:46">[00:11:46]</a>.
    ```javascript
    const { readFile } = require('fs').promises; // Using promises for cleaner async code

    app.get('/', async (request, response) => {
        try {
            const html = await readFile('./home.html', 'utf8');
            response.send(html);
        } catch (error) {
            response.status(500).send('Server Error');
        }
    });
    ```
    *   `app.get('/', ...)` defines an endpoint for the root URL (`/`) <a class="yt-timestamp" data-t="00:12:21">[00:12:21]</a>.
    *   The second argument is a callback function that handles the request, receiving `request` (incoming data) and `response` (for sending data back) parameters <a class="yt-timestamp" data-t="00:12:35">[00:12:35]</a>.
    *   This example reads an `home.html` file from the file system and sends its content back to the client using `response.send()` <a class="yt-timestamp" data-t="00:13:02">[00:13:02]</a>.
    *   Using `fs.promises` and `async/await` helps avoid "callback hell" and makes the code more readable for asynchronous operations <a class="yt-timestamp" data-t="00:14:14">[00:14:14]</a>.

3.  **Start Listening for Requests:**
    ```javascript
    const port = process.env.PORT || 3000; // Use environment variable or default to 3000

    app.listen(port, () => {
        console.log(`App available on http://localhost:${port}`);
    });
    ```
    *   `app.listen()` tells the Express app to start listening for incoming requests on a specified port <a class="yt-timestamp" data-t="00:14:49">[00:14:49]</a>.

4.  **Run the Application:**
    Open the command line and run `node .` (assuming `index.js` is the entry point) <a class="yt-timestamp" data-t="00:14:06">[00:14:06]</a>. Then navigate to `http://localhost:3000` in your browser to see the HTML rendered <a class="yt-timestamp" data-t="00:14:09">[00:14:09]</a>.

## Deploying to the Cloud (Google App Engine)
One easy and free way to deploy your Node.js application is using Google App Engine <a class="yt-timestamp" data-t="00:15:01">[00:15:01]</a>. Google App Engine's standard environment for Node.js (up to version 12) provides a server that scales automatically based on traffic <a class="yt-timestamp" data-t="00:15:03">[00:15:03]</a>.

**Prerequisites:**
*   A Google Cloud Platform account <a class="yt-timestamp" data-t="00:15:16">[00:15:16]</a>.
*   Google Cloud command-line tools installed locally <a class="yt-timestamp" data-t="00:15:18">[00:15:18]</a>.

**Deployment Steps:**
1.  **Create `app.yaml`:** In your project's source code, create an `app.yaml` file to configure your cloud server <a class="yt-timestamp" data-t="00:15:26">[00:15:26]</a>.
    ```yaml
    runtime: nodejs12
    ```
    This specifies the [[introduction_to_nodejs | Node.js]] version 12 runtime <a class="yt-timestamp" data-t="00:15:31">[00:15:31]</a>.

2.  **Define a Start Script in `package.json`:** App Engine looks for a `start` script in `package.json` to run your code <a class="yt-timestamp" data-t="00:15:37">[00:15:37]</a>.
    ```json
    {
      "name": "my-express-app",
      "version": "1.0.0",
      "main": "index.js",
      "scripts": {
        "start": "node ."
      },
      "dependencies": {
        "express": "^4.17.1"
      }
    }
    ```
    Ensure `main` points to your app's entry file (`index.js` in this case) <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.

3.  **Deploy:** Open your command line and run `gcloud app deploy` <a class="yt-timestamp" data-t="00:15:47">[00:15:47]</a>.
    After deployment, you'll receive a public URL to access your application on the web <a class="yt-timestamp" data-t="00:15:51">[00:15:51]</a>.