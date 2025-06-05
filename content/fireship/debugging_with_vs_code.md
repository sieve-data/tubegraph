---
title: Debugging with VS Code
videoId: u21W_tfPVrY
---

From: [[fireship]] <br/> 

Debugging is a crucial process for identifying and resolving issues in your application. Visual Studio Code (VS Code) provides a powerful integrated debugger that supports various runtimes and allows for detailed inspection of your code's execution.

## Accessing and Using the Debugger
When an application encounters issues, VS Code's debugger panel can help diagnose the problem <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.
To access the debugger, click the bug icon in the sidebar <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.

### Setting Breakpoints
You can set breakpoints in your code by simply adding a red dot next to the line numbers <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>. When the script execution hits a breakpoint, it will pause, allowing you to inspect the local state, call stack, and other relevant information <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>.

### Running the Debugger
To start the debugger, click the "play" button, which will automatically attach the debugger to the current process <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>. While debugging, VS Code displays all local and global variables <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>.

### Debugger Console
The debugger console allows you to execute commands within the context of the running script <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>. You can inspect the name and value of any variable by typing it into the command line, and its value will be printed in the console <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>.

## Debugging Specific Runtimes

### Node.js Debugging
Node.js applications can be debugged out of the box in VS Code <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>. For other runtimes, you can install specific [[using_extensions_and_snippets_in_vs_code | extensions]] to enable debugging support <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>.

### Chrome Browser Debugging
For front-end applications, such as Angular, you can debug directly within the Chrome browser context <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>.
1.  **Install the Chrome extension:** Begin by installing the Chrome debugger [[using_extensions_and_snippets_in_vs_code | extension]] <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>.
2.  **Launch configuration:** In the debugger panel, select Chrome as the debugger and set up a launch configuration. For Angular applications, this typically means configuring it to connect to `localhost:4200` <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>.
3.  **Set breakpoints:** Place breakpoints in your component files, for example, before a component is initialized or on a button click event <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>.
4.  **Start debugging:** Clicking "play" will launch Chrome, and the debugger will run, controllable directly from VS Code <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>.
5.  **Inspect state:** While debugging, you can highlight over properties in your code to see the current state of the data <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>. This feature is highly effective for managing and understanding state in web applications <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>.