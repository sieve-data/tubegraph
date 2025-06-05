---
title: Packaging Electron Apps for Multiple Operating Systems
videoId: 3yqDxhR2XxE
---

From: [[fireship]] <br/> 

[[building_desktop_apps_with_electron | Electron]] enables developers to create desktop applications that are installable on macOS, Windows, and [[integrating_linux_tools_in_windows_for_web_development | Linux]] using standard web technologies like HTML, CSS, and [[running_javascript_in_various_environments | JavaScript]] <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>.

## Simplifying Distribution with Electron Forge

One of the significant advantages of [[building_desktop_apps_with_electron | Electron]] is its ability to package applications for various operating systems with relative ease <a class="yt-timestamp" data-t="00:10:23">[00:10:23]</a>. The tool primarily responsible for this capability is **Electron Forge** <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>.

Electron Forge simplifies the process of building distributables that users can install on their systems <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>. It handles the complexities of packaging automatically <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>.

### How to Package an Electron App

To package an [[building_desktop_apps_with_electron | Electron]] application using Electron Forge, follow these steps:

1.  **Open the Terminal**: Navigate to your project directory in the command line <a class="yt-timestamp" data-t="00:10:34">[00:10:34]</a>.
2.  **Run the Build Command**: Execute `npm run make` <a class="yt-timestamp" data-t="00:10:36">[00:10:36]</a>.
3.  **Automatic Detection**: Electron Forge automatically detects your operating system <a class="yt-timestamp" data-t="00:10:37">[00:10:37]</a>.
4.  **Build Distributable**: It then builds the distributable file specifically for that OS <a class="yt-timestamp" data-t="00:10:39">[00:10:39]</a>.

### Output Location

After the command completes, Electron Forge creates an `out` directory in your project <a class="yt-timestamp" data-t="00:10:44">[00:10:44]</a>. Within this directory, you will find the executable file that allows users to run your application natively on their system <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>. For example, if building on Windows, the executable will be found there <a class="yt-timestamp" data-t="00:10:42">[00:10:42]</a>.

This straightforward process means that if you possess [[running_javascript_in_various_environments | JavaScript]] knowledge, you can begin [[building_desktop_apps_with_electron | building desktop apps]] and preparing them for distribution today <a class="yt-timestamp" data-t="00:10:52">[00:10:52]</a>.