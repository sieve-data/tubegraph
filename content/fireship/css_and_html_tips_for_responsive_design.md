---
title: CSS and HTML tips for responsive design
videoId: lPJVi797Uy0
---

From: [[fireship]] <br/> 

This article provides a beginner-friendly tutorial on transforming flat website designs into dynamic, curvaceous ones using various [[css_for_styling_and_layout | CSS]], [[svg_and_css_integration | SVG]], and JavaScript techniques <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. The approach includes adding curves with [[css_for_styling_and_layout | CSS]] `border-radius`, [[svg_and_css_integration | SVG]] backgrounds, and even animated morphing blobs with JavaScript <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>.

## Basic HTML Setup

To begin, create a plain HTML file in a code editor like VS Code <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.
*   **Emmet Snippet for Boilerplate** Typing `!` followed by `Tab` generates initial HTML boilerplate using an Emmet snippet <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.
*   **Generating Multiple Sections** Emmet can also generate multiple content sections. For example, `section * 8` creates eight `<section>` elements <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. To add a child element like an `<h1>` with text "nice curves" and a subsequent `<p>` with dummy text, the syntax would be `section * 8 > (h1{nice curves} + p{lorem})` <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.

## Serving the HTML Locally

You can serve your HTML application locally using a couple of methods:
*   **Node.js `npx serve`** If Node.js is installed, open the command line and run `npx serve` to link your app to `localhost:5000` <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.
*   **Direct File Path** Alternatively, copy the path to your HTML file and paste it directly into your browser <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.

## Basic CSS Styling

To improve the visual appearance, [[css_for_styling_and_layout | CSS]] styles are defined within a `<style>` tag in the document's head <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.
*   **Google Fonts Integration** Select a custom font from Google Fonts and paste the provided HTML snippet into the `<head>` of your document <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>.
*   **Body Styling** Set the `body` margin to `0`, define `font-family` from Google Fonts, and apply text and background colors <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.
*   **Section Styling**
    *   Set `position: relative` on section elements to allow children to be absolutely positioned within them later <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.
    *   Use [[css_for_styling_and_layout | CSS flexbox]] to make sections flexible containers, allowing for easy content centering <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>.
        *   **Tip:** Use browser Dev Tools (right-click, inspect element) to experiment with flexbox properties directly <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.
    *   Apply a `min-height` of `400px` and padding (`100px` top/bottom, `20vw` left/right) for [[responsive_layouts_using_css_grid_and_media_queries | responsiveness]] <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>.
*   **Utility Classes** Create utility classes (e.g., `.blue`, `.red`, `.dark`, `.pink`) to easily distinguish and apply different background colors to sections <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>.

## Adding Curves with CSS

[[css_for_styling_and_layout | CSS]] can implement complex curves, though it can be challenging for intricate designs <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.
*   **Empty `div` for Curves** Add an empty `div` with a class like `curve` below content sections <a class="yt-timestamp" data-t="00:03:29">[00:03:29]</a>.
*   **Positioning** Set the curve `div` to `position: absolute` at the bottom of its parent section (which has `position: relative`) <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>.
*   **Pseudo-Elements (`::before` and `::after`)** Use `::before` and `::after` pseudo-elements (acting like invisible HTML elements) to create the curve <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>.
    *   Set `content: ''`, `position: absolute`, and apply `border-radius` with two values to create an ellipse (vertical radius, horizontal radius) <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>.
    *   Define `width` and `height` for these elements <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.
    *   Use `transform: translate(x, y)` to move these "circles" into proper alignment, which often requires trial and error <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.
    *   Use `z-index: -1` on one pseudo-element to ensure it sits underneath another, creating depth <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>.
*   **Overflow Fix** To prevent horizontal content overflow caused by curves, set `overflow-x: hidden` on the parent element <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.
*   **Simple Ellipse Curve** For simpler curves, use only the `::after` pseudo-element with an elliptical `border-radius` on specific corners (e.g., `top-left`, `top-right`) and `absolute` positioning <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.

## Adding Curves with SVG

[[svg_and_css_integration | Scalable Vector Graphics (SVG)]] simplify the creation of complex curves <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>.
*   **Shape Divider Tool** Use online tools like Shape Divider to automatically draw SVG curves and generate the necessary [[css_for_styling_and_layout | CSS]] <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.
    *   Experiment with settings, download the HTML snippet (containing the SVG graphic), and paste it into a section <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>.
    *   Copy the generated [[css_for_styling_and_layout | CSS]] code and apply it to the SVG container (e.g., a `div` with class `wave`) <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>.

### Advanced SVG Backgrounds (Separators)

For more sophisticated [[svg_and_css_integration | SVG]] backgrounds used as section separators:
*   **High App** Use web apps like High to generate beautiful [[svg_and_css_integration | SVG]] backgrounds, such as layered waves <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>.
    *   Choose colors that complement your [[css_for_styling_and_layout | CSS]] design <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>.
    *   Crucially, set the aspect ratio for the SVG to be long and skinny, like a border or separator <a class="yt-timestamp" data-t="00:07:38">[00:07:38]</a>.
    *   Download the SVG file into your project <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>.
*   **CSS `aspect-ratio` and Background Properties**
    *   Create a [[css_for_styling_and_layout | CSS]] class (e.g., `spacer`) <a class="yt-timestamp" data-t="00:07:57">[00:07:57]</a>.
    *   Use the `aspect-ratio` [[css_for_styling_and_layout | CSS]] property to manage the element's width and height based on the SVG's aspect ratio <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>.
    *   Apply the SVG as a `background-image` <a class="yt-timestamp" data-t="00:08:13">[00:08:13]</a>.
    *   Set `background-repeat: no-repeat`, `background-position: center`, and `background-size: cover` to ensure the image covers the entire element <a class="yt-timestamp" data-t="00:08:19">[00:08:19]</a>.
    *   Create a second class (e.g., `wave-bg`) to define the specific SVG graphic <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>.
    *   Add an empty `div` with these classes to apply the SVG as a transition between sections <a class="yt-timestamp" data-t="00:08:34">[00:08:34]</a>.
*   **Flipping Spacers** A `flip` utility class can be used with `transform: rotateY(180deg)` to orient [[svg_and_css_integration | SVG]] spacers in the desired direction (e.g., for top or bottom placement) <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>.

## Animated Morphing SVG with JavaScript

For dynamic, animated curves, JavaScript can be used to morph [[svg_and_css_integration | SVG]] shapes <a class="yt-timestamp" data-t="00:08:58">[00:08:58]</a>.
*   **Generating Blob SVGs** Use tools like High app to generate two different random blob shapes <a class="yt-timestamp" data-t="00:09:22">[00:09:22]</a>.
    *   Download the SVGs and extract the raw `path` source code from within the `g` (group) elements <a class="yt-timestamp" data-t="00:09:28">[00:09:28]</a>.
    *   Paste these `g` elements (each containing a `path`) into a single SVG in your HTML, giving each `path` a unique ID (e.g., `blob-one`, `blob-two`) <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a>.
    *   Delete any `rect` elements within the SVG <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>.
*   **Kute.js Library** A library like Kute.js simplifies SVG morphing animations <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>.
    *   Include the Kute.js CDN script tag in the document's `<head>` <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>.
    *   Add a script block at the bottom of the section:
        ```javascript
        KUTE.from('#blob-one', { path: '#blob-two' }).start();
        ```
        This animates `blob-one` to the shape of `blob-two` <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>.
    *   Add options like `duration` (e.g., `3000` milliseconds) and `yoyo: true` to make the animation go back and forth <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>.
    *   Call `.start()` to begin the animation <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>.
*   **Visibility and Positioning**
    *   Set the `visibility` of the second blob (`blob-two`) to `hidden` so it's not visible when the animation starts <a class="yt-timestamp" data-t="00:11:15">[00:11:15]</a>.
    *   Apply basic [[css_for_styling_and_layout | CSS]] positioning to place the blob appropriately underneath the main content <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a>.