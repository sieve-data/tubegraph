---
title: Using CSS border radius for curves
videoId: lPJVi797Uy0
---

From: [[fireship]] <br/> 

CSS `border-radius` is a technique used to add curves, waves, or ripples to website content sections, transforming flat designs into dynamic, curvaceous ones <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. While powerful, implementing complex curves solely with CSS can be challenging <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>.

## Basic Implementation with `border-radius`

To begin adding curves with CSS, you can start with a basic HTML homepage structured with a hero section, content sections, and a footer <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.

### Initial Setup

1.  Create a plain HTML file <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.
2.  Use an Emmet snippet (`section * 8 > h1{Nice Curves} + p{lorem}`) to generate multiple content sections <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.
3.  Serve the HTML file locally using `npx serve` (if Node.js is installed) or by directly opening the file path in your browser <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.
4.  Link a custom font from Google Fonts by pasting the provided HTML snippet into the `<head>` of your document <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>.
5.  Add a `<style>` tag below the font link to define CSS styles <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.

### Styling the Page Elements

*   **Body**: Set `margin: 0`, define a `font-family` from Google Fonts, and choose light text color on a dark background <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.
*   **Sections**:
    *   Set `position: relative` to allow absolute positioning of child elements, crucial for background curves <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.
    *   Use [[basics_of_css_grid | CSS flexbox]] (`display: flex`, `justify-content: center`, `align-items: center`, `flex-direction: column`) to easily center content <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>. Browser developer tools can assist in experimenting with flexbox properties <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.
    *   Set `min-height` to `400px` <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>.
    *   Add `padding` with `100px` top/bottom and `20vw` left/right for responsiveness <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>.
*   **Utility Classes**: Create classes (e.g., `.blue`, `.red`, `.dark`) to apply different background colors to sections <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>.

## Creating Complex Curves with Pseudo-Elements

For more intricate curves, you can use `border-radius` on `::before` and `::after` pseudo-elements.

### Step-by-Step for Complex Curves

1.  Add an empty `div` with a class like `curve` below the content within a section <a class="yt-timestamp" data-t="00:03:29">[00:03:29]</a>. While generally not ideal, this approach is acceptable for creating curves and can even contain content if desired <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.
2.  Target the `.curve` element in CSS:
    *   Set `position: absolute` and `bottom: 0` to place it at the bottom of its relative parent section <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>.
    *   Set `left: 0`, `width: 100%`, and `height: 200px` (or desired height).
3.  Target the `::before` and `::after` pseudo-elements of `.curve`:
    *   Set `content: ''` (empty string) <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>.
    *   Set `position: absolute` <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.
    *   Apply `border-radius`. A single value creates a perfect circle, while two values create an ellipse. The first value determines the vertical radius, and the second the horizontal radius <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>.
    *   Define `width` and `height` <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.
4.  Position the pseudo-elements using the `transform` property with `translate()`. This moves the "circles" (ellipses) to specific X and Y coordinates to create the illusion of a curve <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
5.  Use `z-index: -1` on one of the pseudo-elements (e.g., `::after`) to ensure it sits below the other, creating the desired layering effect <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>.
6.  Adjust values in browser developer tools to perfectly align the elements, as precise alignment often requires trial and error <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.
7.  If horizontal overflow occurs, set `overflow-x: hidden` on the parent element to fix the issue <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.

While possible, this method for complex curves can be quite difficult <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>.

## Creating Simpler Curves with `border-radius`

CSS is generally better suited for curves that involve a single ellipse or circle <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>.

### Step-by-Step for Simple Curves (e.g., Bubble)

1.  Add a class like `bubble` to a section in your HTML <a class="yt-timestamp" data-t="00:05:59">[00:05:59]</a>.
2.  In CSS, target the `::after` pseudo-element of the `.bubble` class.
3.  Apply an elliptical `border-radius` specifically to the top-left and top-right corners (e.g., `border-top-left-radius: 50% 100%`, `border-top-right-radius: 50% 100%`) <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>.
4.  Use `position: absolute` and other positioning properties (`bottom: 0`, `left: 0`, `width: 100%`, `height: 50px`, `background: var(--dark)`) to place it appropriately <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>.

This approach is much simpler than using two intersecting circles for complex curves and is recommended for more straightforward designs <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>. For more complex, dynamic curves, [[creating_wavy_backgrounds_with_svg_and_css | SVG backgrounds]] and [[animated_morphing_svg_with_javascript | animated morphing SVG with JavaScript]] often simplify the process <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a>.