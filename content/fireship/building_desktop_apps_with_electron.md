---
title: Building Desktop Apps with Electron
videoId: 3yqDxhR2XxE
---

From: [[fireship]] <br/> 

This guide provides a practical beginner's approach to [[Screen Recording with Electron | building desktop apps with Electron]] <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. By the end of this tutorial, you will have built a desktop application installable on macOS, Windows, and Linux using only HTML, CSS, and JavaScript <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. The project demonstrates combining APIs from the web, Node.js, and Electron to create a [[Screen Recording with Electron | desktop screen capture]] tool <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>.

## Why Electron?

Electron applications bundle Chromium and Node.js, which can lead to large app sizes and high resource consumption (CPU and RAM) compared to apps built with Objective-C or C# <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.

However, these drawbacks often don't matter for most developers <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>. For web or Node.js developers, Electron offers an excellent developer experience and makes desktop app development a practical business decision <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>. Even large companies choose Electron because it makes more business sense, as the ultimate goal is to build an awesome user experience, which is achievable with Electron <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. As Winston Churchill famously put it, "Electron is the worst desktop architecture except for all the others we've tried" <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.

## The Project: A Screen Recorder

The desktop app built in this guide is a simple [[Screen Recording with Electron | screen recorder]] <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>. It can:
*   Select one of the open windows on your desktop <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>.
*   Turn it into a video stream <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.
*   Preview the video stream within the Electron app <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.
*   Record the stream into a raw video file <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.
*   Open a native menu to select a save location <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.
*   Write the raw video file to your filesystem <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>.

This project requires using Node.js for certain tasks, web technologies for others, and Electron APIs <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.

## Getting Started

### Boilerplate Code Generation
To generate initial boilerplate code, use `electron Forge` <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.
1.  Open your command line.
2.  Run `npx create-electron-app` followed by your desired app name <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.
    ```bash
    npx create-electron-app my-screen-recorder
    ```
3.  Electron Forge sets up a starter project, which will later be used to [[packaging_electron_apps_for_multiple_operating_systems | build distributable installers]] <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.

### Project Structure
*   `src/index.html`: The entry point for the front-end UI (the render process) <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.
*   `src/index.js`: The entry point for the main process <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.

### Running the App
To start the application, run `npm start` from the command line <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>.
```bash
npm start
```
Note that Electron apps do not have hot reloading by default like many web frameworks <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>. To see changes reflected, type `rs` in the terminal and press Enter to restart the app <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>.

## Electron Architecture: Main Process vs. Render Process

### Main Process (`index.js`)
*   Every Electron app has exactly one main process <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.
*   It is created by `index.js` <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>.
*   Key modules imported are `app` and `BrowserWindow` from `electron` <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.
*   `app` controls the lifecycle of the application using an event-based API <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>. The primary event to listen to is `ready` <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.
*   Platform-specific code can be run by checking `process.platform` (e.g., `'darwin'` for macOS, `'win32'` for Windows) <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.

### Render Process (Browser Window)
*   An Electron app can have multiple render processes running simultaneously <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>.
*   Each render process is an instance of Chromium, similar to a browser tab or window <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>.
*   A render process is created by instantiating a `BrowserWindow` <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>.
*   Setting `nodeIntegration` to `true` allows access to Node.js globals directly in the front-end code <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.
*   The `index.html` file is loaded into the `BrowserWindow` using `loadURL` or `loadFile` <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>.

## Building the Screen Recorder App

### 1. UI Setup
*   Create `render.js` and link it in `index.html` with `<script defer src="./render.js"></script>` <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.
*   Add Bulma CSS to the `head` of `index.html` for styling <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>.
*   Add a `<video>` element to preview the recording output <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>.
*   Add three buttons: "Start Recording", "Stop Recording", and "Select Source" <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.
*   In `render.js`, get references to these HTML elements using `document.querySelector` and `document.getElementById` <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.

### 2. Accessing Available Screens
*   Electron's `desktopCapture` module allows access to available screens <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.
*   Import it using `const { desktopCapture } = require('electron');` <a class="yt-timestamp" data-t="00:05:45">[00:05:45]</a>.
*   Define an `async` function `getVideoSources()` and assign it as the event handler for the "Select Source" button <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>.
*   Call `desktopCapture.getSources()` to retrieve an array of available windows/screens <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>.

### 3. Native Menus for Source Selection (Inter-Process Communication - IPC)
*   The `Menu` class is designed to run on the main process <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>. To access it from the render process, use the `remote` module: `const { Menu } = require('@electron/remote');` <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>.
*   Create a menu template from the `sources` array using `map` <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>:
    ```javascript
    const videoOptionsMenu = Menu.buildFromTemplate(
        sources.map(source => {
            return {
                label: source.name,
                click: () => selectSource(source)
            };
        })
    );
    ```
*   Display the menu by calling `videoOptionsMenu.popup()` <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>.

### 4. Selecting a Source and Streaming Video
*   Implement `async function selectSource(source)` <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>.
*   Set the text of the "Select Source" button to the chosen `source.name` <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>.
*   Define `constraints` for `getUserMedia`:
    ```javascript
    const constraints = {
        audio: false,
        video: {
            mandatory: {
                chromeMediaSource: 'desktop',
                chromeMediaSourceId: source.id
            }
        }
    };
    ```
*   Get the video stream using the browser's built-in `navigator.mediaDevices.getUserMedia(constraints)` <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>.
*   Set the `srcObject` of the HTML video element to the obtained stream and call `videoElement.play()` to preview <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>.

### 5. Recording and Saving Video
*   Initialize `mediaRecorder` as a global variable and `recordedChunks` as an empty array <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>.
*   In `selectSource()`, instantiate `MediaRecorder`:
    ```javascript
    mediaRecorder = new MediaRecorder(stream, { mimeType: 'video/webm; codecs=vp9' });
    ```
*   Handle `mediaRecorder` events:
    *   `mediaRecorder.ondataavailable`: Push `event.data` to `recordedChunks` <a class="yt-timestamp" data-t="00:08:55">[00:08:55]</a>.
    *   `mediaRecorder.onstop`: Convert recorded chunks to a video file <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>.
        *   Create a `Blob` from `recordedChunks` <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>.
        *   Convert the `Blob` to a Node.js `Buffer` using `Buffer.from(await blob.arrayBuffer())` <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>.
*   Use Electron's `dialog` module (from `remote`) to prompt the user to save the file: `const { filePath } = await dialog.showSaveDialog({ ... });` <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>. Set a default filename with a timestamp <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>.
*   Write the file to the system using Node.js's built-in `fs` module: `const fs = require('fs');` <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>.
    ```javascript
    fs.writeFile(filePath, buffer, () => console.log('video saved successfully'));
    ```

## Packaging the App for Distribution

Electron Forge simplifies [[packaging_electron_apps_for_multiple_operating_systems | packaging Electron apps for different operating systems]] <a class="yt-timestamp" data-t="00:10:26">[00:10:26]</a>.
*   Open your terminal.
*   Run `npm run make` <a class="yt-timestamp" data-t="00:10:37">[00:10:37]</a>.
*   Electron Forge will automatically detect your operating system and build the distributable for that OS <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>. The executable will be found in the `out` directory <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>.

If you know JavaScript, you can start [[electron_for_web_developers | building desktop apps]] today <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>.