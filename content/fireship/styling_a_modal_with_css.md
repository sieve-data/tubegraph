---
title: Styling a modal with CSS
videoId: SuqU904ZHA4
---

From: [[fireship]] <br/> 

Animation, a satisfying aspect for developers, can transform a standard feature into something remarkable <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This guide focuses on styling a modal window in React using [[CSS for Styling and Layout | CSS]] <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>.

## Initial Setup for [[CSS for Styling and Layout | CSS]]
To begin, after generating a React project with Create React App, delete all boilerplate code from `index.css` <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>. Then, import `normalize.css`, which provides a blank slate for [[CSS for Styling and Layout | CSS]] styling <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>. The project's main [[CSS for Styling and Layout | CSS]] styles are then pasted into this file <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.

## Styling the Backdrop Component
The backdrop is an overlay that darkens the entire screen behind the modal window <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>. Its styling involves several key [[CSS for Styling and Layout | CSS]] properties:
*   **Positioning** Set `position` to `absolute` and place it in the top-left corner <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>.
*   **Dimensions** Give it a `height` and `width` of `100%` to cover the entire screen <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>.
*   **Background and Opacity** Use a black background with an added two characters to the hex color for opacity (e.g., `#00000080`) <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>. This allows elements underneath to remain visible <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.
*   **Centering Children** To center any content (children components) within the backdrop horizontally and vertically, use `display: flex` <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.

## Styling the Modal Window Component
The modal window sits on top of the backdrop, focusing user attention <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>. A key styling aspect for the modal window is making its width and height responsive <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>.

*   **Responsive Width with `clamp()` and `min()`**: The `clamp()` function in [[CSS for Styling and Layout | CSS]] is used to define the modal's width <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>.
    *   It attempts to set the width to `700px` <a class="yt-timestamp" data-t="00:06:38">[00:06:38]</a>.
    *   If the screen is too small, it will expand up to `90%` of the viewport width <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>.
    *   If the screen is too large, it will cap at a maximum of `50%` of the screen width <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>.
    *   This approach is effective for [[CSS and HTML tips for responsive design | responsive design]], avoiding the need for media queries which would require significantly more code <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>.