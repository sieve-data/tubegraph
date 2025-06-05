---
title: Introduction to Nodejs
videoId: ENrzD9HAZK4
---

From: [[fireship]] <br/> 

[[javascript_serverside_with_nodejs | Node.js]] is considered one of the most valuable skills for a full stack web developer and is expected to remain so <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. While other technologies like Deno might emerge, an established tool like Node.js doesn't get replaced easily <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. Learning Node.js is recommended, especially for job opportunities or building products, as the skills are largely transferable to newer runtimes like Deno <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.

The best way to learn to code is by building something meaningful from scratch <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. This article covers the basics of Node.js through seven steps, culminating in building and deploying a full stack web application <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.

## What is Node.js?
[[javascript_serverside_with_nodejs | Node.js]] is not a programming language itself, but rather a runtime environment that enables you to [[javascript_serverside_with_nodejs | run JavaScript on a server]] <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>. Originally, JavaScript was designed in the 1990s as a simple scripting language exclusively for web browsers <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>. However, as the web evolved, JavaScript's capabilities expanded <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.

In 2009, the initial release of Node.js revolutionized [[introduction_to_web_development | web development]] by making it possible to write JavaScript code on the server, a domain previously dominated by languages like Java or PHP <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>. This allowed web developers to build entire full stack applications using a single language <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.

Node.js allows a server to handle client requests, read files from its file system, and respond back to the client, for instance, by serving HTML to be viewed in a browser <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.

## [[installing_and_managing_nodejs_versions | Installing Node.js]]
[[installing_and_managing_nodejs_versions | Node.js]] can be installed on Windows, Mac, or Linux <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>. To check if Node.js is installed on your system, run `node -v` from the command line <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.

It is highly recommended to use a package called [[installing_and_managing_nodejs_versions | Node Version Manager]] (NVM) to [[installing_and_managing_nodejs_versions | manage different Node.js versions]] on your system <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>. NVM has packages for Mac and Linux, and a separate package for Windows <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>. NVM allows you to install and switch between any desired version of Node.js, for example, `nvm install 12.16.3` and then `nvm use 12.16.3` <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.

## [[running_and_understanding_javascript_with_nodejs | Running JavaScript with Node.js]]
One way to experiment with [[running_and_understanding_javascript_with_nodejs | Node.js]] is by using its REPL (Read-Eval-Print Loop) mode <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>. By typing `node` into the command line, you can execute JavaScript code directly and see the results <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>.

However, in most scenarios, you'll want to execute JavaScript code from a file <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>. The default entry point for a Node.js application is typically an `index.js` file <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>. You can run the code within this file by using the `node` command followed by the file's path, or simply by pointing to the parent directory if it's named `index.js` <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>.

## Understanding the Node.js Runtime
While JavaScript largely functions the same way in [[javascript_serverside_with_nodejs | Node.js]] as it does in a browser, there are crucial differences <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>.

### Built-in Globals
Node.js includes several built-in global identifiers:
*   **`console`**: Used for logging values to the terminal <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>.
*   **`global`**: An object serving as a namespace available throughout the entire Node.js process. It's comparable to the `window` object in a browser <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.
*   **`process`**: Provides access to the currently running Node.js process. It can be used to check the operating system or retrieve environment variables <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>.

### [[eventdriven_architecture_in_nodejs | Event-Driven Architecture]]
[[eventdriven_architecture_in_nodejs | Node.js]] is described as an asynchronous, [[eventdriven_architecture_in_nodejs | event-driven JavaScript runtime]] <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>. The runtime implements an "Event Loop" similar to web browsers, which allows Node.js to offload intensive operations to separate threads <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>. This means that only very fast, non-blocking operations occur on the main thread, making Node.js non-blocking and highly suitable for high-throughput applications like real-time systems and web servers <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.

As a developer, you primarily need to understand how events and callbacks function <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>. You often listen to events, which can take various forms. For example, the `process` global emits an `exit` event before a Node.js process finishes. You can listen to this event using the `on` method and register a callback function that will execute when the event occurs <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>.

You can also create custom events using the `EventEmitter` class from Node.js's built-in `events` module. By instantiating `EventEmitter`, you can register callbacks for custom event names and then `emit` those events to trigger the associated callbacks <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>. This [[eventdriven_architecture_in_nodejs | event-driven]] style is especially useful for CPU-intensive tasks <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.

### File System (FS) Module
[[javascript_serverside_with_nodejs | Node.js]] includes a built-in file system module, `fs`, which allows you to read, write, and delete files <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>. Operations can be performed in either a blocking (synchronous) or non-blocking (asynchronous) manner <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>.

*   **Synchronous operations**: Functions ending in `sync` (e.g., `readFileSync`) will block the execution of other code until they complete <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>.
*   **Asynchronous operations (Callbacks)**: Functions like `readFile` take a callback function as an argument. The callback will execute only after the file operation is complete, allowing other code to run concurrently <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>.
*   **Asynchronous operations (Promises/Async-Await)**: A more modern and often cleaner approach involves using promises, typically accessed through the `fs.promises` namespace <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>. Promises are asynchronous and non-blocking <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>. When combined with `async`/`await` syntax, they make asynchronous code much more readable and manageable, especially when dealing with multiple asynchronous calls <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>.

## Modules
A module in Node.js is essentially a JavaScript file that exports its code <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>. Node.js comes with many built-in modules, such as `fs` and `events` <a class="yt-timestamp" data-t="00:09:07">[00:09:07]</a>.

### CommonJS Modules (`require`/`module.exports`)
The traditional way to import a module in Node.js is using the `require` function <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>. To export code from a custom module, you can add properties to the `module.exports` object, or redefine `module.exports` entirely <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>.

### ES Modules (`import`/`export`)
Node.js has added support for ES Modules, which use the `import` and `export` syntax <a class="yt-timestamp" data-t="00:09:19">[00:09:19]</a>. However, much of the existing Node.js code still uses `require` <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>.

### Node Package Manager (NPM)
To use third-party code, Node.js developers primarily use the Node Package Manager (NPM) <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>. NPM is installed automatically when you install Node.js <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>.

To manage dependencies in your project:
1.  Run `npm init -y` in your command line. This creates a `package.json` file, which stores metadata about your project and tracks its dependencies <a class="yt-timestamp" data-t="00:10:28">[00:10:28]</a>.
2.  Use `npm install [package_name]` to install a remote package, such as `npm install express`. This adds the package to your `dependencies` in `package.json` and places its source code in a `node_modules` directory <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>. The `node_modules` directory should not be manually modified <a class="yt-timestamp" data-t="00:11:16">[00:11:16]</a>.
3.  Once installed, you can import the package by name using `require` in your JavaScript code <a class="yt-timestamp" data-t="00:11:33">[00:11:33]</a>.

## [[building_and_deploying_a_full_stack_application_with_nodejs_and_express | Building and Deploying a Full Stack Application with Node.js and Express]]
This section demonstrates how to build a basic web application using Node.js and the Express framework.

### Setting up the Server with Express
1.  **Initialize Express**: Create an instance of an Express application <a class="yt-timestamp" data-t="00:11:57">[00:11:57]</a>.
2.  **Define Endpoints**: Use `app.get()` to set up different URLs (endpoints) that a user can navigate to. The first argument is the URL path (e.g., `/` for the root), and the second is a callback function that handles requests to that URL <a class="yt-timestamp" data-t="00:12:19">[00:12:19]</a>.
    *   The callback function receives `request` and `response` objects as parameters. `request` contains incoming data from the user (like headers or body), and `response` is used to send data back to the client <a class="yt-timestamp" data-t="00:12:43">[00:12:43]</a>.
3.  **Handle Requests**: Inside the callback, read HTML content from your server's file system (e.g., `home.html`) using Node's `fs` module <a class="yt-timestamp" data-t="00:13:02">[00:13:02]</a>.
    *   Use `fs.promises.readFile` with `async`/`await` for cleaner asynchronous code, to avoid "callback hell" <a class="yt-timestamp" data-t="00:14:26">[00:14:26]</a>.
    *   Send the HTML back to the client using `response.send()` <a class="yt-timestamp" data-t="00:13:28">[00:13:28]</a>. Handle errors by sending a 500 status code <a class="yt-timestamp" data-t="00:13:34">[00:13:34]</a>.
4.  **Listen for Requests**: Tell the Express app to start listening for incoming requests on a specific port (e.g., 3000), typically defined by a Node environment variable <a class="yt-timestamp" data-t="00:13:48">[00:13:48]</a>. Call `app.listen()` to start the server <a class="yt-timestamp" data-t="00:13:51">[00:13:51]</a>.
5.  **Run the App**: Start the application by running `node .` from your command line in the project's root directory <a class="yt-timestamp" data-t="00:14:04">[00:14:04]</a>.

### Deploying to the Cloud
[[building_and_deploying_a_full_stack_application_with_nodejs_and_express | Node.js]] applications can be deployed to cloud platforms <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>. A simple and free option is Google App Engine <a class="yt-timestamp" data-t="00:14:58">[00:14:58]</a>. App Engine provides a standard environment for Node.js (up to version 12) that automatically scales based on traffic <a class="yt-timestamp" data-t="00:15:02">[00:15:02]</a>.

To deploy with Google App Engine:
1.  Ensure you have a Google Cloud Platform account and the Google Cloud command-line tools installed <a class="yt-timestamp" data-t="00:15:15">[00:15:15]</a>.
2.  Create an `app.yaml` file in your source code directory. Configure it to specify the runtime, e.g., `runtime: nodejs12` <a class="yt-timestamp" data-t="00:15:25">[00:15:25]</a>.
3.  In your `package.json`, define a `start` script that runs your Node.js application (e.g., `"start": "node ."`) <a class="yt-timestamp" data-t="00:15:37">[00:15:37]</a>.
4.  Open your command line and run `gcloud app deploy` <a class="yt-timestamp" data-t="00:15:46">[00:15:46]</a>. After deployment, you will receive a public URL to access your application <a class="yt-timestamp" data-t="00:15:50">[00:15:50]</a>.