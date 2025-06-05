---
title: Understanding Nodejs modules and packages
videoId: ENrzD9HAZK4
---

From: [[fireship]] <br/> 

One of the most valuable skills for a full-stack web developer is proficiency with [[introduction_to_nodejs | Node.js]], a skill that is expected to remain relevant for the foreseeable future <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. [[introduction_to_nodejs | Node.js]] itself is not a programming language but rather a [[nodejs_runtime_and_basic_operations | runtime]] that enables JavaScript to run on a server <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.

## [[introduction_to_nodejs | Node.js]] Modules

A module is essentially a JavaScript file that exports its code <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>.

### Built-in Modules
[[introduction_to_nodejs | Node.js]] includes several built-in modules, such as:
*   `fs` (File System): This module allows reading, writing, and deleting files on the file system in both blocking and non-blocking ways <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>.
*   `events`: This module provides the `EventEmitter` class, which can be used to create and handle custom events <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>.

### Importing Modules with `require`
The traditional method for importing a module in [[introduction_to_nodejs | Node.js]] is by using the `require` function <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>. Although [[introduction_to_nodejs | Node.js]] recently added support for ES Modules with `import`/`export` syntax, much of the existing vanilla JavaScript code in [[introduction_to_nodejs | Node.js]] still utilizes `require`, making it an important concept for developers to understand <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>.

To import a module, you assign the result of `require` to a variable <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>. For built-in modules, you simply specify the module's name (e.g., `require('events')` <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>). For local modules, you provide the path to the file <a class="yt-timestamp" data-t="00:09:45">[00:09:45]</a>.

### Exporting Code with `module.exports`
To make a module useful, it must export some code from it <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>. This is done by referencing the `module.exports` object within the module's file <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>. You can add new properties to this object or redefine it as a new object, and whatever is added will be accessible when the module is imported <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>.

## [[introduction_to_nodejs | Node.js]] Packages and npm

When you need to use code written by others, the primary resource is Node Package Manager (npm) <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>. npm was acquired by GitHub, which itself was acquired by Microsoft <a class="yt-timestamp" data-t="00:10:17">[00:10:17]</a>. When you [[installing_and_setting_up_nodejs | install Node.js]], npm is also installed <a class="yt-timestamp" data-t="00:10:22">[00:10:22]</a>.

### Initializing a Project with `npm init`
To begin using npm in a project, you run `npm init` from the command line, often with the `-y` flag to use default options <a class="yt-timestamp" data-t="00:10:30">[00:10:30]</a>. This command creates a `package.json` file in the application's root directory <a class="yt-timestamp" data-t="00:10:36">[00:10:36]</a>. This file contains metadata about your project and, crucially, tracks its dependencies <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>.

### Installing Packages with `npm install`
`npm` is a tool for installing remote packages to use in your own code <a class="yt-timestamp" data-t="00:10:26">[00:10:26]</a>.
For example, to install [[setting_up_a_nodejs_and_express_environment | Express]], a popular third-party [[introduction_to_nodejs | Node.js]] module and web application framework, you would run `npm install Express` <a class="yt-timestamp" data-t="00:10:51">[00:10:51]</a>. After installation, the `package.json` file is updated to include [[setting_up_a_nodejs_and_express_environment | Express]] in its `dependencies` object, pegged to a specific version <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>. This `dependencies` object enables managing multiple project dependencies and reinstalling them all at once on different systems <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a>.

### The `node_modules` Directory
The raw source code for installed dependencies resides in the `node_modules` directory <a class="yt-timestamp" data-t="00:11:14">[00:11:14]</a>. It is generally advised never to modify code within this directory, as the `package.json` file dictates how it's built by fetching remote packages and saving their source there <a class="yt-timestamp" data-t="00:11:18">[00:11:18]</a>. This process should be repeatable on any system <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>.

Once a package is installed, you can import it by its name in your JavaScript code using `require` <a class="yt-timestamp" data-t="00:11:33">[00:11:33]</a>. For example, `require('express')` would import the [[setting_up_a_nodejs_and_express_environment | Express]] framework <a class="yt-timestamp" data-t="00:11:37">[00:11:37]</a>. These concepts are fundamental for [[building_and_deploying_a_nodejs_full_stack_application | building and deploying a full stack web application]] with [[introduction_to_nodejs | Node.js]] <a class="yt-timestamp" data-t="00:11:41">[00:11:41]</a>.