---
title: Implementing SVG for scalable vector graphics
videoId: lPJVi797Uy0
---

From: [[fireship]] <br/> 

Scalable Vector Graphics (SVG) can be used to simplify the implementation of complex curves and interactive elements on a webpage <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>. SVG backgrounds and animated morphing blobs with JavaScript are examples of how SVG can be used <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a> <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

## Utilizing Online Tools for SVG Creation

A convenient aspect of SVG is the ability to use design tools or purpose-built web applications to automatically generate the SVG code and accompanying CSS <a class="yt-timestamp" data-t="00:06:32">[00:06:32]</a>.

### Shape Divider

One such tool, `shape divider`, allows users to experiment with different settings to create a desired curve design <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a> <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>. After designing, the tool provides an HTML snippet containing the SVG graphic, which can be pasted directly into a section of the HTML document <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a> <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>. It also supplies the necessary CSS code to integrate the SVG into the UI <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a> <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>.

### Haikei (High)

Another free web application, `Haikei` (referred to as `high` in the transcript), is dedicated to generating SVG backgrounds <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a> <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>. Key features include:

*   **Layered Waves Option** This allows for the creation of multi-layered wave designs <a class="yt-timestamp" data-t="00:07:25">[00:07:25]</a> <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>.
*   **Color Selection** It's important to select colors within the tool that complement the existing CSS color scheme of the webpage <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a> <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>.
*   **Aspect Ratio Adjustment** For SVG graphics intended as borders or separators between content sections, they often need to be long and skinny, requiring an adjustment to the aspect ratio within the tool <a class="yt-timestamp" data-t="00:07:38">[00:07:38]</a> <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a> <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a> <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>. The selected aspect ratio should be noted for later CSS implementation <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>.

After customization, the SVG file can be downloaded directly into the project <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a> <a class="yt-timestamp" data-t="00:07:52">[00:07:52]</a> <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>.

### Implementing Downloaded SVG Backgrounds

To implement the downloaded SVG as a background or transition, CSS can be used:

1.  **Spacer Class**: A CSS class, such as `spacer`, can be created to manage the SVG's dimensions <a class="yt-timestamp" data-t="00:07:57">[00:07:57]</a> <a class="yt-timestamp" data-t="00:07:59">[00:07:59]</a>.
2.  **Aspect Ratio Property**: The `aspect-ratio` CSS feature allows the management of an element's width and height based on a single ratio, which should match the aspect ratio noted from the SVG generation tool <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a> <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a> <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a> <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a> <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>.
3.  **Background Styling**: The SVG image can be set as a background using `background-image` <a class="yt-timestamp" data-t="00:08:13">[00:08:13]</a> <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>. To ensure it covers the element properly, `background-repeat` should be set to `no-repeat`, `background-position` to `center`, and `background-size` to `cover` <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a> <a class="yt-timestamp" data-t="00:08:19">[00:08:19]</a> <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a> <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a> <a class="yt-timestamp" data-t="00:08:23">[00:08:23]</a>.
4.  **HTML Integration**: An empty `div` element with these CSS classes can then be added to the HTML where the SVG transition is desired <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a> <a class="yt-timestamp" data-t="00:08:38">[00:08:38]</a> <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>.

## [[animated_morphing_svg_with_javascript | Animated Morphing SVG with JavaScript]]

For dynamic and interactive elements, JavaScript can be used to create [[animated_morphing_svg_with_javascript | animated morphing SVG]] shapes <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a> <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>.

### Preparing SVG for Morphing

1.  **Generate Blobs**: Use a tool like `Haikei` to create two different blob shapes and download their SVG files <a class="yt-timestamp" data-t="00:09:22">[00:09:22]</a> <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a> <a class="yt-timestamp" data-t="00:09:26">[00:09:26]</a>.
2.  **Extract SVG Paths**: Open the downloaded SVG files and extract the raw SVG source code <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a> <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>. Paste the code for the first blob into the HTML document, specifically the `<path>` element which defines the shape of the blob <a class="yt-timestamp" data-t="00:09:33">[00:09:33]</a> <a class="yt-timestamp" data-t="00:09:35">[00:09:35]</a> <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a> <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>.
3.  **Combine Paths**: For the second blob, find the `<g>` (group) element in its raw SVG code and copy it. Paste this `<g>` element as a sibling to the first blob's group within the same SVG container in the HTML <a class="yt-timestamp" data-t="00:09:54">[00:09:54]</a> <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a> <a class="yt-timestamp" data-t="00:09:58">[00:09:58]</a> <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a> <a class="yt-timestamp" data-t="00:10:02">[00:10:02]</a> <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a> <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>.
4.  **Assign IDs**: Give each `<path>` element a unique ID (e.g., `blobOne`, `blobTwo`) for JavaScript referencing <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a> <a class="yt-timestamp" data-t="00:10:22">[00:10:22]</a> <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>.
5.  **Hide Second Blob**: Initially, the second blob should have its `visibility` set to `hidden` in CSS so it's not visible before the animation begins <a class="yt-timestamp" data-t="00:11:15">[00:11:15]</a> <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a> <a class="yt-timestamp" data-t="00:11:18">[00:11:18]</a>.

### Using KUTE.js for Morphing Animation

The KUTE.js library simplifies complex morph animations <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a> <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>.

1.  **Install KUTE.js**: Include the KUTE.js CDN link via a `<script>` tag in the `<head>` of the HTML document <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a> <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a> <a class="yt-timestamp" data-t="00:10:42">[00:10:42]</a>.
2.  **Create Animation Script**: In a new `<script>` tag at the bottom of the relevant section, use KUTE.js to define the morph animation <a class="yt-timestamp" data-t="00:10:44">[00:10:44]</a> <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>.
    *   Use `KUTE.fromTo()` method, specifying the starting SVG ID (`blobOne`) and the target SVG ID (`blobTwo`) <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a> <a class="yt-timestamp" data-t="00:10:48">[00:10:48]</a> <a class="yt-timestamp" data-t="00:10:52">[00:10:52]</a> <a class="yt-timestamp" data-t="00:10:53">[00:10:53]</a> <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>.
    *   Add an options object as a third argument to control animation properties:
        *   `duration`: Set the animation duration (e.g., `3000` milliseconds) <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a> <a class="yt-timestamp" data-t="00:10:59">[00:10:59]</a> <a class="yt-timestamp" data-t="00:11:01">[00:11:01]</a>.
        *   `yoyo`: Set to `true` to make the animation loop back and forth between the two states <a class="yt-timestamp" data-t="00:11:03">[00:11:03]</a> <a class="yt-timestamp" data-t="00:11:04">[00:11:04]</a> <a class="yt-timestamp" data-t="00:11:05">[00:11:05]</a> <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>.
    *   Call `.start()` on the animation object to begin <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a> <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a>.
3.  **Positioning**: Add basic CSS positioning to place the blob appropriately underneath the main content in that section <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a> <a class="yt-timestamp" data-t="00:11:22">[00:11:22]</a> <a class="yt-timestamp" data-t="00:11:23">[00:11:23]</a> <a class="yt-timestamp" data-t="00:11:24">[00:11:24]</a> <a class="yt-timestamp" data-t="00:11:26">[00:11:26]</a>.