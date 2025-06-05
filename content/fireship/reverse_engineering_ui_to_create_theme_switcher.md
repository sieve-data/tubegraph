---
title: Reverse engineering UI to create theme switcher
videoId: rXuHGLzSmSE
---

From: [[fireship]] <br/> 

This article explores how to reverse engineer a user interface, specifically focusing on creating a dynamic theme switcher with light, dark, and solarized modes. It also covers other common UI design techniques such as creating custom shapes, CSS-only dropdown menus, and hover animations.

## Core Feature: Dynamic Theme Switching
The main goal is to build a feature similar to Alligator.io, allowing users to switch between light, dark, and solarized themes <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This is achieved using CSS variables and JavaScript <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>. The implementation involves a total of four different color schemes <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.

### Key Components for Theme Switching
*   **CSS Variables**: Defined on the root element (`:root`) and specific theme classes (e.g., `.light`, `.dark`, `.solar`). These variables hold static values like base colors (e.g., various shades of gray, blue, purple, yellow) <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>. They can be used to build more complex values like linear gradients for backgrounds <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>.
*   **JavaScript**: Handles user interaction (button clicks) to change the theme by manipulating the CSS classes on the `body` element <a class="yt-timestamp" data-t="00:10:13">[00:10:13]</a>. The `classList.replace()` method is used for mutually exclusive themes like light and dark <a class="yt-timestamp" data-t="00:10:45">[00:10:45]</a>. The solarized theme is applied conditionally on top of existing light or dark modes <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>. JavaScript can also directly modify CSS variables <a class="yt-timestamp" data-t="00:11:15">[00:11:15]</a>.
*   **Local Storage**: Caches the user's theme selection in the browser, ensuring the chosen theme persists even after page refreshes <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>, <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>. This is done using `localStorage.setItem()` and `localStorage.getItem()` <a class="yt-timestamp" data-t="00:11:51">[00:11:51]</a>.

For more information on [[implementing_a_css_theme_switcher_using_css_variables_and_javascript | implementing a CSS theme switcher using CSS variables and JavaScript]], check out the related content.

## User Interface Design Techniques

Beyond the theme switcher, several other [[design_techniques_in_app_development | design techniques]] are demonstrated:

### CSS Triangle Shape
A triangle shape at the bottom of a header element is created using the `clip-path` CSS property <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>, <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>. The `polygon()` function within `clip-path` allows defining custom shapes by specifying coordinates (X and Y percentages) <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>. Firefox Developer Tools provide a visual `clip-path` editor to easily adjust points <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.

### CSS-Only Dropdown Menu
A dropdown menu is built without JavaScript <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>, <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.
*   The dropdown element is initially set to `opacity: 0` and `position: absolute` with a `z-index` greater than its parent <a class="yt-timestamp" data-t="00:05:45">[00:05:45]</a>.
*   The `focus-within` pseudo-selector on the parent list item (`.has-dropdown`) is used to detect when any element inside the dropdown receives focus <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>.
*   When focused, the dropdown's `opacity` is set to `1`, causing it to fade in <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>. A `transition` property on the dropdown element makes the fade effect smooth <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>.
*   Circular indicators next to each theme link within the dropdown are created using the `::before` pseudo-element with `border-radius: 50%` <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>.

### Rainbow Logo Animation
A rainbow color transition effect is applied to the logo on hover <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>. This is achieved using CSS keyframes and the `filter` property <a class="yt-timestamp" data-t="00:12:57">[00:12:57]</a>.
*   A `@keyframes` rule named `color-rotate` animates the `filter: hue-rotate()` property from `0deg` to `360deg` <a class="yt-timestamp" data-t="00:13:05">[00:13:05]</a>.
*   On hover, the `animation` property is applied to the logo, setting the `color-rotate` animation to run infinitely with a duration of one second, and the `animation-direction` set to `alternate` (or `rotate` in the transcript, which seems to be a typo for `alternate` or just a conceptual description of the direction) <a class="yt-timestamp" data-t="00:13:17">[00:13:17]</a>. This creates a continuous cycle through the color spectrum <a class="yt-timestamp" data-t="00:13:34">[00:13:34]</a>.
For more examples, refer to [[animating_ui_elements_with_css_keyframes | Animating UI elements with CSS keyframes]].

## Project Setup and Structure
The project uses standard HTML, CSS, and JavaScript files <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.
*   **HTML Structure**: A basic boilerplate is generated using Emmet in VS Code <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>, including links to a custom Google Font, a stylesheet (`style.css`), and a deferred JavaScript file (`app.js`) <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>. The `body` element starts with a default `light` class <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.
*   **Navbar**: A flexbox-based navigation bar is used, containing an unordered list (`ul`) as a flex container with list items (`li`) as flex items <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.
*   **CSS Reset**: Initial styles clear default margins, padding, and list styles, and set links to inherit the current text color (`color: currentcolor`) <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>.
*   **Font**: A custom font from Google Fonts is used <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.
*   **CSS Color Scheme Generation**: Tools like Colors.co can assist in generating color palettes <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>.