---
title: Screen Recording with Electron
videoId: 3yqDxhR2XxE
---

From: [[fireship]] <br/> 

This article provides a practical beginner's guide to [[building_desktop_apps_with_electron | building desktop apps with Electron]] using HTML, CSS, and JavaScript <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. By the end, you'll understand how to create a desktop screen capture application that's installable on macOS, Windows, and Linux <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. The application combines APIs from the web, [[building_and_deploying_a_nodejs_full_stack_application | Node.js]], and [[electron_for_web_developers | Electron]] to create native menus, capture a video stream, and write the raw video file to your filesystem <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>.

## Understanding Electron

[[electron_for_web_developers | Electron]] applications bundle Chromium and [[building_and_deploying_a_nodejs_full_stack_application | Node.js]], which can lead to large app sizes and higher CPU/RAM usage compared to native apps like those built with Objective-C or C-Sharp <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>. However, for web or [[building_and_deploying_a_nodejs_full_stack_application | Node.js]] developers, [[electron_for_web_developers | Electron]] offers an excellent developer experience and makes desktop apps a practical business decision <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>. The ultimate goal is to build an awesome user experience, which is absolutely achievable with [[electron_for_web_developers | Electron]] <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>.

> [!QUOTE] "Electron is the worst desktop architecture, except for all the others we've tried." <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>
> — *Winston Churchill (paraphrased)*

## The Screen Recorder Project

The desktop app being built is a simple screen recorder <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>. It selects one of the open windows on your desktop, turns it into a video stream, and previews it in the [[electron_for_web_developers | Electron]] app <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>. When the record button is clicked, the stream is converted into a raw video file <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>. Clicking stop opens a native menu to select where to save the file, and then the raw file is written to the system <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>. This project uses [[building_and_deploying_a_nodejs_full_stack_application | Node.js]], web technologies, and [[electron_for_web_developers | Electron]] APIs <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.

## Setting Up the Project

To get started, generate boilerplate code using **Electron Forge** <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.
1.  Open the command line <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.
2.  Run `npx create-electron-app` with your desired app name <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>.
    *   This provides a starter project with an `index.html` (front-end UI entry point/renderer process) and `index.js` (main process entry point) <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.
3.  To run the app, use `npm start` <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.
    *   Note that hot reloading is not supported; restart the app by typing `rs` in the terminal <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>.

## Electron's Main and Renderer Processes

Every [[electron_for_web_developers | Electron]] app has exactly one **main process**, created by `index.js` <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.
*   The `app` module controls the lifecycle of the application, using an event-based API <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.
*   The `ready` event is essential for app initialization <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.
*   Platform-specific code can be run by checking `process.platform` (e.g., 'Darwin' for Mac, 'win32' for Windows) <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>.

An [[electron_for_web_developers | Electron]] app can have multiple **renderer processes**, each an instance of Chromium, akin to a browser tab or window <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>.
*   A renderer process is created by instantiating a `BrowserWindow` <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>.
*   Set `nodeIntegration` to `true` to access [[building_and_deploying_a_nodejs_full_stack_application | Node.js]] globals directly in front-end code <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>.
*   Use `loadFile` to load your `index.html` into the window <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.

## Building the Screen Recorder UI and Logic

### Frontend Setup

1.  Create a `render.js` file for your front-end code and link it in `index.html` with a `<script defer src="render.js"></script>` tag <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.
2.  Add Bulma CSS for styling <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>.
3.  Include a `<video>` element for previewing the output and three buttons: Start, Stop, and Select Source <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.
4.  In `render.js`, reference these HTML elements using `document.querySelector` and `document.getElementById` <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.

### Getting Video Sources

*   Use [[electron_for_web_developers | Electron]]'s `desktopCapturer` module in the renderer process to access available screens <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>. Import it using `require('electron').desktopCapturer` <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>.
*   Create an `async` function, `getVideoSources`, and assign it as the event handler for the video select button <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>.
*   Call `desktopCapturer.getSources()` with options for type (e.g., `['window', 'screen']`) to get an array of available windows/screens <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.

### Creating Native Menus

*   [[electron_for_web_developers | Electron]]'s `Menu` class runs on the main process <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>. To access it from the renderer process, use the `remote` module: `require('electron').remote` <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>. This is a form of Inter-Process Communication (IPC) <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>.
*   Use `Menu.buildFromTemplate()` which expects an array of menu item objects <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>.
*   Map the `sources` array into menu items, setting the `label` as `source.name` and registering a `click` event handler for `selectSource` function <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>.
*   Call `menu.popup()` to display the native menu <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>.

### Streaming Video

*   Implement the `async` `selectSource` function <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>.
*   Set options for `getUserMedia`: `audio` to `false`, `chromeMediaSource` to `'desktop'`, and `chromeMediaSourceId` to the selected `source.id` <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>.
*   Use the browser's built-in `navigator.mediaDevices.getUserMedia(options)` to get a stream <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>.
*   Set the `srcObject` of the HTML video element to this stream and call `videoElement.play()` to show a real-time preview <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>.

### Recording and Saving the Video

*   Use the browser's built-in **Media Recorder API** <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>.
*   Initialize a `MediaRecorder` instance with the stream and a `mimeType` option <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>.
*   Listen for `dataavailable` events to push recorded chunks into an array <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>.
*   Listen for the `stop` event:
    *   Convert the `recordedChunks` into a `Blob` <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.
    *   Convert the `Blob` into a `Buffer` using `Buffer.from(await blob.arrayBuffer())` <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>.
*   To save the file, use [[electron_for_web_developers | Electron]]'s `dialog` module (also imported from `remote`) <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>.
    *   Call `dialog.showSaveDialog()` to let the user choose a save location, providing options like a default path <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>. This returns the selected file path <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>.
*   Write the file to the system using [[building_and_deploying_a_nodejs_full_stack_application | Node.js]]'s built-in **File System (FS) module** (`fs`) <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>.
    *   Import `fs` using `require('fs')` <a class="yt-timestamp" data-t="00:10:02">[00:10:02]</a>.
    *   Use `fs.writeFile(filePath, buffer, callback)` to save the buffer data to the chosen path <a class="yt-timestamp" data-t="00:10:06">[00:10:06]</a>.

## Packaging the Application

[[packaging_electron_apps_for_multiple_operating_systems | Electron Forge]] automates the process of creating distributable files for different operating systems <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>.
1.  Open the terminal <a class="yt-timestamp" data-t="00:10:34">[00:10:34]</a>.
2.  Run `npm run make` <a class="yt-timestamp" data-t="00:10:36">[00:10:36]</a>.
    *   This command will automatically detect your operating system and build the distributable for that OS, creating an `out` directory containing the executable <a class="yt-timestamp" data-t="00:10:37">[00:10:37]</a>.

## Conclusion

The key takeaway is that if you know JavaScript, you can begin [[building_desktop_apps_with_electron | building desktop apps with Electron]] today <a class="yt-timestamp" data-t="00:10:53">[00:10:53]</a>.