---
title: Running JavaScript in various environments
videoId: 9emXNzqCKyg
---

From: [[fireship]] <br/> 

Understanding where and how JavaScript code runs is fundamental to development <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. JavaScript can be executed in different environments, including on local machines (server-side) and within web browsers (client-side) <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.

## Running JavaScript on the Command Line

To run JavaScript directly on your machine, you can use [[nodejs_runtime_and_basic_operations | Node.js]] <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>.

### Steps to Run with Node.js
1.  Open a code editor, such as VS Code <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.
2.  Create a JavaScript file (e.g., `index.js`) <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.
3.  Add JavaScript code, for instance, `console.log("hello world")` <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.
4.  Assuming [[nodejs_runtime_and_basic_operations | Node.js]] is installed, execute the script from your command line by typing `node index.js` <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.

Running JavaScript this way allows you to create back-end, server-side JavaScript applications <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.

## Running JavaScript in Browsers

Most developers associate JavaScript with browsers and web applications <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.

### Developer Console
It's possible to execute JavaScript directly in the browser by opening the developer console <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>. The browser has an [[using_javascript_on_web_and_server_environments | interpreter]] (or JIT compiler) that runs the code typed into the console <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>. However, the browser console is primarily a debugging tool <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>.

### Script Tags in HTML
The standard way web applications run JavaScript is by declaring a `<script>` tag within an HTML document <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.

#### How it Works
1.  Create an `index.html` file <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>.
2.  Add a `<script>` tag and set its `src` attribute to your JavaScript file (e.g., `<script src="index.js" defer></script>`) <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>.
3.  When the browser parses the HTML file, it will load and execute the script <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.
4.  Using the `defer` attribute ensures the JavaScript executes only after the entire HTML document is fully loaded <a class="yt-timestamp" data-t="00:02:00">[00:01:58">[00:02:00]</a>. This is useful because JavaScript often references HTML elements that might not be available until the document is completely loaded <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>.

> [!NOTE] Frameworks commonly handle the setup of script tags automatically, but understanding their underlying function is important for web development <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.