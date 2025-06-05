---
title: Electron for Web Developers
videoId: 3yqDxhR2XxE
---

From: [[fireship]] <br/> 

[[building_desktop_apps_with_electron | Electron]] is a framework that enables [[building_desktop_apps_with_electron | building desktop applications]] using standard [[introduction_to_web_development | web development]] technologies such as HTML, CSS, and [[javascript_and_frontend_development | JavaScript]] <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. This approach allows [[using_javascript_on_web_and_server_environments | web]] and [[using_javascript_on_web_and_server_environments | Node.js]] developers to leverage their existing skills to create cross-platform desktop applications installable on macOS, Windows, and Linux <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>.

## Why Choose Electron?

For [[using_javascript_on_web_and_server_environments | web]] or [[using_javascript_on_web_and_server_environments | Node.js]] developers, Electron provides an exceptional developer experience <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>. It transforms the creation of desktop applications into a practical business decision for companies that might not otherwise consider them <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. Even large companies with significant resources often opt for Electron because it makes business sense <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>. The primary goal is to deliver an excellent user experience, which is entirely achievable with Electron, as users typically do not know or care about the underlying technology used to build an app <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>.

### [[criticism_and_drawbacks_of_electron | Criticism and Drawbacks of Electron]]

Electron applications bundle Chromium and Node.js, which tends to result in a large app size, even for simple applications <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>. Additionally, running Chromium can be resource-intensive, potentially leading to higher CPU and RAM usage compared to apps built with Objective-C or C# <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.

However, for most developers, these [[criticism_and_drawbacks_of_electron | drawbacks]] are often less significant in the broader context of project development <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>. As humorously put by a quote attributed to Winston Churchill, "Electron is the worst desktop architecture, except for all the others we've tried" <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>.

## Core Concepts of Electron

Electron applications integrate APIs from the [[introduction_to_web_development | web]], Node.js, and Electron itself <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>.

### Main Process

Every Electron application has exactly one main process <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>. This process is typically created by an `index.js` file <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>. It uses an event-based API to control the lifecycle of the application <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>. Key events include:

*   `app.on('ready')`: Fires once the application is ready, allowing for initialization logic <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>.
*   `window-all-closed`: Handles behavior when all windows are closed <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.

The main process can implement platform-specific code by checking the `process.platform` value, which is `Darwin` for macOS or `win32` for Windows <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>.

### Render Process

An Electron app can have multiple render processes running simultaneously <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>. Each render process is an instance of Chromium, similar to a tab or window in a web browser <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>. They are created by instantiating a `BrowserWindow` <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>. Setting `nodeIntegration` to `true` in a `BrowserWindow` allows direct access to Node.js globals within the front-end code <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>.

The render process loads HTML files (e.g., `index.html`) using `loadfile()` <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a> and runs client-side [[javascript_and_frontend_development | JavaScript]] (e.g., `render.js`) <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.

### Inter-Process Communication (IPC)

Electron uses Inter-Process Communication (IPC) to enable communication between the main and render processes <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>. For example, the `remote` module allows access to main process functionalities like native menus directly from the render process <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>.

## Building an Electron Application (Example: Screen Recorder)

A practical example of an Electron application is a screen recorder, which combines various Electron, Node.js, and [[introduction_to_web_development | web]] APIs <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>.

### Initial Setup with Electron Forge

[[building_desktop_apps_with_electron | Electron Forge]] is a tool used to generate initial boilerplate code and help build distributable packages <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>.

*   To generate boilerplate: `npx create-electron-app <app-name>` <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>.
*   To start the app: `npm start` <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>.
*   To restart the app after changes (as hot reloading is not default): Type `rs` in the terminal <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.

### Key API Usage

*   **`desktopCapturer.getSources()`**: Used in the render process to get a list of available windows or screens for recording <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>. This method returns a promise that resolves to an array of objects, each representing a recordable source <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>.
*   **Native Menus (`Menu`, `remote` module)**:
    *   The `Menu` class is designed to run on the main process <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>.
    *   The `remote` module allows accessing main process functionalities (like `Menu`) from the render process <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>.
    *   `Menu.buildFromTemplate()`: Creates a menu from an array of menu item objects <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>.
    *   `menu.popup()`: Displays the native menu <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>.
*   **Web Media APIs (`navigator.mediaDevices.getUserMedia`)**:
    *   The browser's built-in `navigator` API is used to create a streaming video from a selected source <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>.
    *   `navigator.mediaDevices.getUserMedia()`: Awaited with constraints (e.g., `chromeMediaSource: 'desktop'`, `chromeMediaSourceId`) to get a video stream <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>.
*   **Media Recording (`MediaRecorder`)**:
    *   The browser's built-in `MediaRecorder` API is used to record a video stream <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>.
    *   It has an event-based API, with important events like `onDataAvailable` (to collect video chunks) <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a> and `onstop` (to finalize the recording) <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>.
    *   Recorded chunks can be converted into a `Blob` <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>, then to a `Buffer` using `Buffer.from(blob.arrayBuffer())` for Node.js file operations <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>.
*   **Native Dialogues (`dialog`, `remote` module)**:
    *   Electron's `dialog` module (accessed via `remote`) allows creating native dialogues for tasks like saving or opening files <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>.
    *   `dialog.showSaveDialog()`: Awaited to get the user-selected file path <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>.
*   **File System (`fs` module - Node.js)**:
    *   Node.js's built-in `fs` (file system) module is used to write files to the system <a class="yt-timestamp" data-t="00:09:58">[00:09:58]</a>.
    *   `fs.writeFile()`: Used to write the recorded video `Buffer` to the chosen file path <a class="yt-timestamp" data-t="00:10:06">[00:10:06]</a>.

### Packaging the Application

[[building_desktop_apps_with_electron | Electron Forge]] can automatically package the application for different operating systems <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>.

*   To build distributables: Run `npm run make` <a class="yt-timestamp" data-t="00:10:34">[00:10:34]</a>.
*   This command detects the operating system and creates an `out` directory containing the executable application <a class="yt-timestamp" data-t="00:10:37">[00:10:37]</a>.