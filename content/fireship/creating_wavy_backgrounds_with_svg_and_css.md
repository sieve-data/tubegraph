---
title: Creating wavy backgrounds with SVG and CSS
videoId: lPJVi797Uy0
---

From: [[fireship]] <br/> 

This article explores various [[techniques_for_svg_styling_with_css_and_javascript | techniques]] to transform a flat website design into a visually appealing one featuring curves, waves, blobs, and ripples between content sections <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. It covers both pure CSS approaches and more advanced methods involving SVG and JavaScript for [[creating_interactive_svg_animations | interactive animations]] <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>.

## Initial Project Setup

To begin, create a basic HTML homepage including a hero section, content sections, and a footer <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. An empty HTML file can be quickly generated in VS Code using the Emmet snippet `!` followed by `Tab` <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>. Multiple content sections (e.g., eight) can be generated with `section*8>h1{Nice curves}+p{lorem}` and `Tab` <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.

The HTML page can be served locally using `npx serve` if Node.js is installed, linking to `localhost:5000` <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>. Alternatively, the HTML file path can be directly pasted into the browser <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.

### Styling with CSS

Enhance the design by adding a custom font from Google Fonts, pasting the provided HTML snippet into the `<head>` of the document <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>. CSS styles are defined within a `<style>` tag below the font link <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>.

Basic CSS for the page body and sections:
*   Body: `margin: 0`, custom `font-family`, light `text-color`, dark `background` <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.
*   Section: `position: relative` (important for absolute positioning of children later) <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>, `display: flex` for easy content centering <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>, `min-height: 400px` <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>, `padding: 100px 20vw` for responsiveness <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>.
*   Utility classes can be added for different background colors <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>.

## [[using_css_border_radius_for_curves | Using CSS Border Radius for Curves]]

### Complex Pure CSS Curve

This method demonstrates creating complex curves using only CSS, though it is more challenging <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>.

1.  Add an empty `div` with a class of `curve` below the content in a section <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>.
2.  The `.curve` div should have `position: absolute` and be placed at the bottom (`bottom: 0`, `left: 0`, `right: 0`, `height: 100px`, `width: 100%`) within its `position: relative` parent section <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>.
3.  Target the `::before` and `::after` pseudo-elements of the `.curve` div <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>. These can be thought of as invisible HTML elements that can be styled <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>.
    *   Set `content: ''` <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>.
    *   Apply `position: absolute` <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.
    *   Use `border-radius` with two values (e.g., `50% 100%`) to create an ellipse, where the first value is the vertical radius and the second is the horizontal <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>.
    *   Set `width` and `height` <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.
4.  Position the `::before` and `::after` elements strategically using `top`, `left`, and [[css_transforms_for_complex_animations | `transform: translate()`]] (moving the circle along X and Y axes) <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>. This often requires trial and error <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.
5.  Use `z-index: -1` on the `::after` element to ensure one circle sits behind the other, creating the illusion of a curve <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>.
6.  To fix horizontal overflow caused by the curve, set `overflow-x: hidden` on the parent element <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.

### Simple CSS Curve (Single Ellipse)

For simpler curves, CSS is well-suited for single ellipses or circles <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>.
*   Add a class (e.g., `bubble`) to a section <a class="yt-timestamp" data-t="00:05:59">[00:05:59]</a>.
*   Target only the `::after` pseudo-element and apply an elliptical `border-radius` to the top-left and top-right, combined with `position: absolute` for placement <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>.

## [[svg_and_css_integration | Using SVG for Complex Curves]]

[[benefits_of_svg_for_web_designers | Scalable Vector Graphics (SVG)]] simplify the creation of more complex curves <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a>.

### Shape Divider Tool

This web application automatically generates SVG and CSS for shape dividers:
1.  Go to a tool like `shapedivider.app` <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>.
2.  Experiment with settings to achieve the desired curve design <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>.
3.  Download and copy the generated HTML snippet, which contains the SVG graphic, and paste it into the bottom of a section in your HTML <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>.
4.  Copy the accompanying CSS code and paste it into your style tags <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>.

### Haikei Tool for Layered Waves

Haikei is another tool dedicated to generating SVG backgrounds, including layered waves <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>.
1.  Select the "layered waves" option and choose to place the waves at the top or bottom <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>.
2.  Tweak the design and ensure colors complement your CSS <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>.
3.  Adjust the aspect ratio to make the graphic long and skinny, suitable for a separator <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>.
4.  Download the SVG file into your project <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>.
5.  In CSS, create a `spacer` class:
    *   Use the `aspect-ratio` CSS feature, setting it to the value noted from the Haikei tool <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>.
    *   Set `background-image` to the downloaded SVG <a class="yt-timestamp" data-t="00:08:13">[00:08:13]</a>.
    *   Add `background-repeat: no-repeat`, `background-position: center`, and `background-size: cover` <a class="yt-timestamp" data-t="00:08:19">[00:08:19]</a>.
6.  Apply this `spacer` class to an empty `div` between sections in your HTML to create the transition <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a>.

## [[animated_morphing_svg_with_javascript | Animated Morphing SVG with JavaScript]]

For dynamic, [[creating_interactive_svg_animations | animated SVG effects]], JavaScript can be employed <a class="yt-timestamp" data-t="00:08:58">[00:08:58]</a>.

1.  Add a section with a specific class (e.g., `pink`) and apply `spacer` layers on either side, using a `flip` class (`transform: rotate(180deg)`) for the top spacer if needed <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>.
2.  Generate two random blob graphics using the Haikei app <a class="yt-timestamp" data-t="00:09:22">[00:09:22]</a>.
3.  Open the downloaded SVG files and extract the raw SVG source code <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>.
4.  Inside the HTML section, paste the SVG code for the first blob. Delete any `<rect>` elements <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>.
5.  From the second blob's SVG file, copy the `<g>` (group) element and paste it as a sibling to the first blob's group within the HTML SVG <a class="yt-timestamp" data-t="00:09:56">[00:10:00]</a>.
6.  Assign unique IDs (e.g., `blob-one` and `blob-two`) to the `<path>` elements of each blob within the SVG <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>.
7.  Integrate `Kute.js` (or `Cute.js`), an animation library similar to GreenSock, by adding its CDN script tag to the `<head>` of the document <a class="yt-timestamp" data-t="00:10:28">[00:10:28]</a>.
8.  At the bottom of the section, add a `<script>` block:
    *   Call `KUTE.fromTo()` with the IDs of the two blobs (e.g., `KUTE.fromTo('#blob-one', '#blob-two', { /* options */ })`) <a class="yt-timestamp" data-t="00:10:44">[00:10:44]</a>.
    *   Include options like `duration: 3000` (milliseconds) and `yoyo: true` to make the animation loop back and forth <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>.
    *   Call `.start()` on the animation object to begin <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>.
9.  Set the `visibility` of the second blob (`#blob-two`) to `hidden` in CSS so it's not visible before the animation starts <a class="yt-timestamp" data-t="00:11:15">[00:11:15]</a>.
10. Add basic positioning CSS to place the blob appropriately within the section <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a>.

This combination of CSS and SVG, with optional JavaScript, allows for the creation of visually appealing and dynamic wavy backgrounds on a website <a class="yt-timestamp" data-t="00:11:29">[00:11:29]</a>.