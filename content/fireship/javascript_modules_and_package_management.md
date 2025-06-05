---
title: JavaScript modules and package management
videoId: lkIFF4maKMU
---

From: [[fireship]] <br/> 

As JavaScript applications grow in complexity, it becomes necessary to organize code into separate files. [[JavaScript modules and package management | Modules]] provide a way to share code between files, preventing all code from residing in a single, unmanageable file <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>.

## How Modules Work
By default, all code within a file or module is private to that specific file <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>. To make code, such as a function, accessible elsewhere, it can be designated as a default export <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>. This allows other files to use an `import` statement to utilize the exported function <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>. It's also possible to export multiple values from a single file and import them by name <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a>.

## Package Management
In JavaScript development, it's common to use code written by other developers <a class="yt-timestamp" data-t="00:09:23">[00:09:23]</a>. The largest [[javascript_package_management_and_libraries | JavaScript package manager]] is [[javascript_package_management_and_libraries | npm]] <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>. When a package is installed from [[javascript_package_management_and_libraries | npm]], its code is downloaded into the `node_modules` folder within your project <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>. Additionally, [[javascript_package_management_and_libraries | npm]] provides a `package.json` file that lists all the dependencies used in the project <a class="yt-timestamp" data-t="00:09:35">[00:09:35]</a>.

## Bundling and Optimization
After building a complete JavaScript application, all JavaScript files typically need to be combined into a single bundle for use by the browser <a class="yt-timestamp" data-t="00:11:05">[00:11:05]</a>. Tools known as module bundlers, such as Vite or webpack, handle this process efficiently <a class="yt="yt-timestamp" data-t="00:11:13">[00:11:13]</a>.

A potential issue is that a large JavaScript bundle can negatively impact page load performance, which can be measured by the network waterfall in browser developer tools <a class="yt-timestamp" data-t="00:11:18">[00:11:18]</a>. To mitigate this, it's possible to split the JavaScript bundle into multiple files and use dynamic imports to load JavaScript only when it's needed <a class="yt-timestamp" data-t="00:11:27">[00:11:27]</a>.