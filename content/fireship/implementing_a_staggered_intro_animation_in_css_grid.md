---
title: Implementing a staggered intro animation in CSS Grid
videoId: 705XCEruZFs
---

From: [[fireship]] <br/> 

This article details how to create an explicit CSS Grid with a fancy staggered intro animation, where each grid item comes in clockwise until it reaches the center, with changing colors during the animation <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>. The middle columns of the grid are also responsive based on the viewport size <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>.

## Basic HTML Structure
The fundamental HTML structure involves a grid container holding multiple `div` elements, which serve as the grid items <a class="yt-timestamp" data-t="00:07:59">[00:07:59]</a>.

## CSS Grid Setup
To begin, set the `display` property of the container to `grid` and add a `gap` property for spacing between items <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>.

### Defining Explicit Grid Areas
An explicit grid can be created using the `grid-template-areas` property, which allows you to name different areas within the grid <a class="yt-timestamp" data-t="00:08:05">[00:08:05]</a>. For instance, areas can be named with letters (e.g., 'a' to 'l' clockwise) or even emojis to represent main content sections <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>. Using shapes for area names can make the UI's purpose of each grid area extremely clear <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>.

### Sizing Rows and Columns
Once `grid-template-areas` are defined, you can set the sizing for rows and columns <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>.
*   **Rows**: If the grid container has a fixed height, individual rows can take up a percentage of that height using the `repeat()` function (e.g., `repeat(4, 25%)` for four rows, each 25% tall) <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>.
*   **Columns**: Columns can be given fixed widths, while middle columns can use the `auto` property to automatically resize based on the viewport <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>.

### Placing Children in Grid Areas
To place children into their respective grid areas, use the `grid-area` property on the individual grid items <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>. For items arranged in a logical order, `nth-child` selectors can be used, but custom class names are also a viable option <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>. Applying `grid-area: [area-name]` will make the element occupy that predefined area in the grid <a class="yt-timestamp" data-t="00:09:13">[00:09:13]</a>.

## Implementing the Staggered Intro Animation

### Staggered Delay Variable
To easily manage the timing of the staggered animation, define a CSS variable for the delay (e.g., `--staggered-delay`) <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>. This allows for changing the timing without manually updating each element's delay <a class="yt-timestamp" data-t="00:09:35">[00:09:35]</a>.

### Keyframes Animation
A `@keyframes` animation defines the visual transition:
*   **`from` (Starting Point)**: Set `opacity: 0` (invisible), `transform: scale(0.3)`, and `filter: hue-rotate(180deg)` <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>. The `hue-rotate` creates a rainbow-like color change as items animate in <a class="yt-timestamp" data-t="00:09:58">[00:09:58]</a>.
*   **`to` (Ending Point)**: Set `opacity: 1`, `transform: scale(1)`, and `filter: hue-rotate(0deg)` <a class="yt-timestamp" data-t="00:10:02">[00:10:02]</a>.
CSS automatically interpolates between these starting and ending values over the specified animation duration <a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a>. This is part of [[animating_ui_elements_with_css_keyframes | Animating UI Elements with CSS Keyframes]].

### Applying the Animation
Apply the animation to all cards (grid items) using the `animation` shorthand property <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>:
*   **`animation-name`**: The name defined in your `@keyframes` rule <a class="yt-timestamp" data-t="00:10:17">[00:10:17]</a>.
*   **`animation-duration`**: The length of the animation (e.g., `700ms`) <a class="yt-timestamp" data-t="00:10:19">[00:10:19]</a>.
*   **`animation-timing-function`**: Controls the acceleration and deceleration (e.g., `ease-out`) <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>.

### Essential Property: `animation-fill-mode`
Set `animation-fill-mode` to `backwards` <a class="yt-timestamp" data-t="00:10:26">[00:10:26]</a>. This is crucial because it ensures elements start at their first keyframe value (e.g., invisible) before the animation begins, preventing them from being visible prematurely <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>. This is critical for [[implementing_fade_in_animations | implementing fade in animations]].

### Staggering the Animation Delay
To create the staggered effect, apply an `animation-delay` to each individual element <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>. The `calc()` CSS function can be used to perform basic calculations on numeric values <a class="yt-timestamp" data-t="00:10:52">[00:10:52]</a>. For example, `animation-delay: calc(1 * var(--staggered-delay))` for the first item, `calc(2 * var(--staggered-delay))` for the second, and so on for all items <a class="yt-timestamp" data-t="00:10:56">[00:10:56]</a>.

While this approach involves some code duplication, using a CSS preprocessor like Sass allows for more efficient code by running programmatic `for` loops to generate these delays automatically <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a>.

This setup results in a unique animated grid without needing JavaScript or external CSS frameworks <a class="yt-timestamp" data-t="00:11:14">[00:11:14]</a>.