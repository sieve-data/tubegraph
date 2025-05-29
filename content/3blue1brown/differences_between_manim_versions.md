---
title: Differences between Manim versions
videoId: rbu7Zu5X1zI
---

From: [[3blue1brown]] <br/> 

There are two primary versions of [[introduction_to_manim_for_animations | Manim]], the custom Python library used to animate 3Blue1Brown videos <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>, <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.

## Original Manim (3Blue1Brown's Version)

The first version of [[introduction_to_manim_for_animations | Manim]] has a history "very intertwined with the history of the channel" <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.
It originated as a "super scrappy bit of Python code" <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a> the creator wrote during undergraduate studies to illustrate mathematical functions as transformations <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. The tool improved iteratively as more videos were made <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>. Over time, it has become "more interactive, more performant" <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.

### Workflow and Features
*   **Programmatic and Bespoke:** It is entirely programmatic and highly customized <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>.
*   **Scene Structure:** All scenes are defined as Python classes with a `construct` method where rendering code resides <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>, <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.
*   **Interactive Shell:** A significant workflow improvement allows for an interactive Python terminal that communicates directly with the scene <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>. This enables:
    *   Running individual lines of code immediately to test effects <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>, <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>.
    *   Highlighting and executing sections of code <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.
    *   A "checkpoint paste" feature that reverts the scene to a cached state before running a copied code section, similar to a Jupyter notebook, for efficient iteration within long scenes <a class="yt-timestamp" data-t="00:06:12">[00:06:12]</a>, <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>.
*   **Animation Philosophy:** A core principle is that "anything can transform into anything" <a class="yt-timestamp" data-t="00:07:52">[00:07:52]</a>, with built-in functions like `write` and `transform` <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>, <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>.
*   **Smoothing Functions:** It provides "rate functions" (e.g., `smooth`, `linear`) to control animation easing, ensuring aesthetically pleasing motion <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>, <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>.
*   **3D Capabilities:** While most scenes are 2D for pedagogical reasons, it supports 3D rendering when needed <a class="yt-timestamp" data-t="00:12:02">[00:12:02]</a>, <a class="yt-timestamp" data-t="00:12:17">[00:12:17]</a>.
*   **LaTeX Integration:** Allows rendering LaTeX equations, with the ability to control and color individual mathematical symbols within the expression <a class="yt-timestamp" data-t="00:44:41">[00:44:41]</a>, <a class="yt-timestamp" data-t="00:45:56">[00:45:56]</a>, <a class="yt-timestamp" data-t="00:46:25">[00:46:25]</a>.
*   **Source Code:** All video code is openly visible on GitHub, serving as examples of functionality <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>, <a class="yt-timestamp" data-t="00:50:35">[00:50:35]</a>.

## Manim Community Version

The creator of [[introduction_to_manim_for_animations | Manim]] open-sourced the underlying tool <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>. However, due to the demands of video production, managing an open-source project was challenging <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.
Consequently, a community of people "forked the repo and created a version that is attentive to issues and pull requests and has better testing and better documentation" <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>. This version is known as the "Manim community version" <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.

### Key Differences and Recommendations
*   **Documentation:** The community version has "much better documentation" <a class="yt-timestamp" data-t="00:50:22">[00:50:22]</a>.
*   **Maintenance:** It is actively maintained with attention to issues and pull requests <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.
*   **Testing:** It features "better testing" <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.

> [!NOTE]
> It is "generally recommended people start with" the Manim community version due to its improved documentation and testing <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>, <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.

### Workflow in Manim Community
Historically, and still a common practice, users of the Manim Community version run animations "from the command line" by passing a Python file containing the scene <a class="yt-timestamp" data-t="00:43:05">[00:43:05]</a>, <a class="yt-timestamp" data-t="00:43:13">[00:43:13]</a>. This means rendering an MP4 file to see changes, which can lead to a longer iteration cycle <a class="yt-timestamp" data-t="00:43:24">[00:43:24]</a>, <a class="yt-timestamp" data-t="00:43:28">[00:43:28]</a>.

> [!INFO] Comparison with Original Manim Workflow
> The original Manim's interactive shell and OpenGL implementation were developed later to provide a more responsive "highlight the code and see what the code does" workflow, which is a "fundamental change to the workflow" compared to constant command-line rendering <a class="yt-timestamp" data-t="00:43:38">[00:43:38]</a>, <a class="yt-timestamp" data-t="00:43:47">[00:43:47]</a>.