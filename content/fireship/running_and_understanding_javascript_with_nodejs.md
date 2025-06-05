---
title: Running and understanding JavaScript with Nodejs
videoId: ENrzD9HAZK4
---

From: [[fireship]] <br/> 

[[Introduction to Node.js | Node.js]] is considered one of the most valuable skills for a full stack web developer <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. Despite common predictions that new technologies like Deno or GraphQL will replace it, Node.js remains a highly established and relevant technology, especially for getting a job or building a product <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. Skills learned in Node.js are also largely transferable to newer runtimes like Deno <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.

The best way to learn Node.js is by building something meaningful from scratch <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.

## What is Node.js?

[[Introduction to Node.js | Node.js]] is not a programming language itself, but rather a runtime that enables you to run [[JavaScript serverside with Node.js | JavaScript on a server]] <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>. Initially, [[javascript_basics_and_history | JavaScript]] was designed as a simple scripting language exclusively for web browsers in the 1990s <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>. The initial release of Node.js in 2009 revolutionized web development by making it possible to write [[JavaScript serverside with Node.js | JavaScript code on the server]] <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>. This allowed web developers to build full-stack applications using a single language <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.

Node.js is ideal for applications requiring high throughput, such as real-time applications and web servers <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>.

## Installing and Running Node.js

Node.js can be installed on Windows, Mac, or Linux <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>. You can check if it's installed by running `node -v` in your command line <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.

> [!INFO] Managing Node.js Versions
> It's highly recommended to use a package called Node Version Manager (NVM) to manage different [[installing_and_managing_nodejs_versions | Node.js versions]] on your system <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>. NVM allows you to install and switch between any desired Node.js version <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.

### Hello World

There are two primary ways to run [[JavaScript]] with Node.js:

1.  **REPL Mode**: Type `node` in the command line to enter Read-Eval-Print Loop (REPL) mode, allowing you to run [[JavaScript]] code interactively and see immediate results <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>.
    ```
    node
    > console.log("Hello World")
    ```
2.  **Executing a File**: Create a `.js` file (e.g., `index.js`) containing your [[JavaScript]] code <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.
    ```javascript
    // index.js
    console.log("Hello World");
    ```
    You can then execute this file from the command line: `node index.js` or simply `node .` if it's named `index.js` in the current directory <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>.

## Understanding the Node.js Runtime

While [[JavaScript]] generally behaves similarly in Node.js as it does in a browser, there are crucial differences <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>.

### Built-in Identifiers (Globals)

Node.js provides several built-in global identifiers:
*   `console`: Used for logging values to the terminal <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>.
*   `global`: An object serving as a namespace available throughout the entire Node.js process. It's comparable to the `window` object in a browser <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.
*   `process`: Provides access to the currently running Node.js process, allowing you to check the operating system or access environment variables <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>.

### [[Event-driven architecture in Node.js | Event-Driven Architecture]]

Node.js is described as an asynchronous, [[eventdriven_architecture_in_nodejs | event-driven JavaScript runtime]] <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>. It implements an [[eventdriven_architecture_in_nodejs | event loop]], similar to web browsers, which allows it to offload intensive operations to separate threads <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>. This ensures that only fast, non-blocking operations occur on the main thread, making Node.js "non-blocking" <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.

> [!INFO] Callbacks
> In Node.js, you often interact with events using [[functions_and_closures_in_javascript | callbacks]] <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>. For example, the `process` global emits an `exit` event before a Node.js process finishes <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>. You can listen to this event using `process.on('exit', callbackFunction)` <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>. The [[functions_and_closures_in_javascript | callback function]] is executed only *after* the event occurs <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>.

### Custom Events

You can create your own custom events using the `EventEmitter` class from Node's built-in `events` module <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>.
```javascript
const EventEmitter = require('events');
const myEmitter = new EventEmitter();

myEmitter.on('lunch', () => {
    console.log('Time for lunch!');
});

myEmitter.emit('lunch'); // Triggers the 'lunch' event
myEmitter.emit('lunch'); // Can be emitted multiple times
```

## File System Module (`fs`)

Node.js includes a built-in `fs` module for interacting with the file system (reading, writing, deleting files) <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>. Operations can be performed in either a blocking (synchronous) or non-blocking (asynchronous) way <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>.

### Blocking vs. Non-blocking

*   **Blocking (Synchronous)**: Functions ending in `Sync` (e.g., `readFileSync`) will complete their work before any other code can run <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>.
    ```javascript
    const fs = require('fs');
    console.log('Before reading file');
    const data = fs.readFileSync('hello.txt', 'utf8');
    console.log('File content (blocking):', data);
    console.log('After reading file'); // This runs after file is read
    ```
*   **Non-blocking (Asynchronous with Callbacks)**: Functions like `readFile` take a [[functions_and_closures_in_javascript | callback function]] as an argument <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>. Node.js registers the [[functions_and_closures_in_javascript | callback]], continues executing the rest of the script, and then runs the [[functions_and_closures_in_javascript | callback]] when the file operation is complete <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>.
    ```javascript
    const fs = require('fs');
    console.log('Before reading file');
    fs.readFile('hello.txt', 'utf8', (err, data) => {
        if (err) throw err;
        console.log('File content (non-blocking):', data);
    });
    console.log('After reading file'); // This runs before the callback
    ```

### Asynchronous with Promises

Promises provide a cleaner way to handle asynchronous operations compared to nested callbacks, especially when dealing with multiple asynchronous calls <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>.
```javascript
const fsPromises = require('fs').promises; // Access the promises namespace

async function readFileWithPromises() {
    console.log('Before reading file');
    try {
        const data = await fsPromises.readFile('hello.txt', 'utf8');
        console.log('File content (promises):', data);
    } catch (err) {
        console.error('Error reading file:', err);
    }
    console.log('After reading file');
}

readFileWithPromises();
```

## Modules

A module in Node.js is essentially a [[JavaScript]] file that exports its code for use elsewhere <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>.

### Built-in Modules

Node.js comes with several built-in modules, such as `fs` and `events` <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>. These are imported using the `require` function <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>.

> [!WARNING] CommonJS vs. ES Modules
> Node.js historically used the CommonJS `require`/`module.exports` syntax <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>. While newer Node.js versions support ES Modules (`import`/`export`), the `require` syntax is still prevalent in much of the existing Node.js codebase <a class="yt-timestamp" data-t="00:09:19">[00:09:19]</a>.

### Custom Modules

You can create your own modules by defining properties on `module.exports` within a `.js` file <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>.
```javascript
// myModule.js
module.exports.greet = (name) => `Hello, ${name}!`;
module.exports.PI = 3.14159;

// index.js
const myModule = require('./myModule');
console.log(myModule.greet('World')); // Output: Hello, World!
console.log(myModule.PI); // Output: 3.14159
```

### Node Package Manager (NPM)

NPM is the primary tool for installing and managing third-party packages (libraries) in Node.js projects <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>. It's installed automatically with Node.js <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>.

1.  **Initialize Project**: Run `npm init -y` in your project directory to create a `package.json` file <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>. This file tracks project metadata and dependencies <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>.
2.  **Install Packages**: Use `npm install <package-name>` (e.g., `npm install express`) to download and add packages to your project <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>.
    *   Installed packages appear in the `dependencies` section of `package.json` <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>.
    *   Their source code resides in the `node_modules` directory <a class="yt-timestamp" data-t="00:11:14">[00:11:14]</a>.

Once installed, packages can be imported by name:
```javascript
const express = require('express'); // 'express' is a popular third-party module
```

## Building a Full Stack Application with Node.js and Express

You can build a typical full-stack web application with Node.js, where a server responds to user requests with HTML <a class="yt-timestamp" data-t="00:11:45">[00:11:45]</a>.

### Using Express.js

[[Building and deploying a full stack application with Node.js and Express | Express.js]] is a minimal web application framework that simplifies creating URLs and handling HTTP requests <a class="yt-timestamp" data-t="00:11:53">[00:11:53]</a>.

```javascript
const express = require('express');
const fsPromises = require('fs').promises; // For promise-based file reading
const app = express();
const PORT = process.env.PORT || 3000; // Define a port for the server

// Define a GET endpoint for the root URL
app.get('/', async (req, res) => {
    try {
        const htmlContent = await fsPromises.readFile('home.html', 'utf8');
        res.send(htmlContent); // Send HTML back to the client
    } catch (err) {
        console.error('Error reading file:', err);
        res.status(500).send('Server Error'); // Handle errors
    }
});

// Start the server and listen for incoming requests
app.listen(PORT, () => {
    console.log(`App available on http://localhost:${PORT}`);
});
```
To run this application, create a `home.html` file (e.g., `<h1>Hello from Node.js!</h1>`) and then run `node index.js` (assuming the above code is in `index.js`) <a class="yt-timestamp" data-t="00:13:09">[00:13:09]</a>.

## Deploying to the Cloud

Once your Node.js application is built, you can deploy it to the cloud <a class="yt-timestamp" data-t="00:15:02">[00:15:02]</a>. Google App Engine offers a standard environment for Node.js that provides an automatically scaling server <a class="yt-timestamp" data-t="00:15:02">[00:15:02]</a>.

### Deployment Steps (Google App Engine Example)

1.  **Google Cloud Platform Account**: Ensure you have a GCP account and the Google Cloud command-line tools installed <a class="yt-timestamp" data-t="00:15:16">[00:15:16]</a>.
2.  **`app.yaml`**: Create an `app.yaml` file in your project root to configure the cloud server.
    ```yaml
    runtime: nodejs12 # Specify Node.js runtime version
    ```
    <a class="yt-timestamp" data-t="00:15:26">[00:15:26]</a>
3.  **`package.json` Start Script**: Add a `start` script to your `package.json` file that tells App Engine how to run your application.
    ```json
    {
      "name": "my-node-app",
      "version": "1.0.0",
      "description": "",
      "main": "index.js",
      "scripts": {
        "start": "node ." // This runs the index.js file
      },
      "keywords": [],
      "author": "",
      "license": "ISC",
      "dependencies": {
        "express": "^4.17.1"
      }
    }
    ```
    <a class="yt-timestamp" data-t="00:15:37">[00:15:37]</a>
4.  **Deploy**: Run `gcloud app deploy` from your command line. This will deploy your application and provide a public URL <a class="yt-timestamp" data-t="00:15:47">[00:15:47]</a>.