---
title: Implementing a CSS theme switcher using CSS variables and JavaScript
videoId: rXuHGLzSmSE
---

From: [[fireship]] <br/> 

This article explores how to build a dynamic theme switcher, inspired by development sites like Alligator.io, which offer options for light, dark, and even solarized themes <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. The technique relies on [[css_for_styling_and_layout | CSS variables]] and JavaScript to allow users to switch themes from scratch <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>.

## Core Concepts

The main components for this feature include:
*   [[css_for_styling_and_layout | CSS Variables]]: Used to define and manage theme colors dynamically <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>.
*   JavaScript: To swap [[css_for_styling_and_layout | CSS classes]] on the document body and interact with the browser's local storage <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.
*   Local Storage: To cache the user's selected theme, ensuring it persists even after page refreshes <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.

## Initial Setup and Basic Structure

The project begins with empty HTML, CSS, and JavaScript files <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.

### HTML Structure
The basic HTML boilerplate is created, including a custom Google font, a stylesheet linked via `<link :CSS>`, and a JavaScript file linked with `<script :source>` and the `defer` attribute <a class="yt-timestamp" data-t="00:01:41">[00:02:01]</a>. Emmet abbreviations can greatly speed up this process <a class="yt-timestamp" data-t="00:02:03">[00:02:08]</a>.

The `body` element is given a `light` class as its default theme <a class="yt-timestamp" data-t="00:02:11">[00:02:15]</a>. The page structure includes:
*   A `navbar` (using Flexbox) <a class="yt-timestamp" data-t="00:02:26">[00:02:38]</a>.
*   A `header` element for the logo and headline <a class="yt-timestamp" data-t="00:02:29">[00:02:30]</a>.
*   A `main` content area for text <a class="yt-timestamp" data-t="00:02:32">[00:02:36]</a>.

### Basic CSS Styling
Initial CSS setup includes:
*   Resetting margin and padding to zero on the body <a class="yt-timestamp" data-t="00:03:19">[00:03:22]</a>.
*   Removing default list styles for the navbar <a class="yt-timestamp" data-t="00:03:23">[00:03:26]</a>.
*   Setting `a` elements (links) to inherit the `currentcolor` from their parent, which is useful with [[css_for_styling_and_layout | CSS variables]] <a class="yt-timestamp" data-t="00:03:26">[00:03:41]</a>.
*   Styling the navbar with a fixed height and width, and setting up its unordered list as a Flex container to align and space items <a class="yt-timestamp" data-t="00:03:43">[00:04:06]</a>.

## Designing Unique UI Elements

### Header with Triangle Shape
To create a unique triangle shape at the bottom of the header, the `clip-path` property is used <a class="yt-timestamp" data-t="00:04:16">[00:04:32]</a>. The `polygon()` function allows defining points along the X and Y axes to shape the element <a class="yt-timestamp" data-t="00:04:37">[00:04:48]</a>. Firefox's developer tools can be particularly helpful for visually adjusting `clip-path` points <a class="yt-timestamp" data-t="00:04:57">[00:05:10]</a>.

### [[creating_a_dropdown_menu_with_css | Dropdown Menu]] (CSS Only)
A dropdown menu is built entirely with CSS, without JavaScript <a class="yt-timestamp" data-t="00:05:13">[00:05:15]</a>.
*   An additional list item with a `has-dropdown` class is added to the navbar, containing a link and an unordered list for the dropdown <a class="yt-timestamp" data-t="00:05:16">[00:05:27]</a>.
*   Each dropdown item has a link with a unique ID (e.g., `light`, `dark`, `solar`) for JavaScript interaction <a class="yt-timestamp" data-t="00:05:27">[00:05:43]</a>.
*   The dropdown menu is positioned `absolute`, given a fixed width, and set to `opacity: 0` by default <a class="yt-timestamp" data-t="00:05:45">[00:05:53]</a>. Its `z-index` is set higher than its parent to ensure visibility <a class="yt-timestamp" data-t="00:05:54">[00:06:01]</a>.
*   Dropdown buttons are aligned horizontally using `display: flex` <a class="yt-timestamp" data-t="00:06:07">[00:06:17]</a>.
*   The `::before` pseudo-element is used to create small colored circles next to each link, by setting a border, `border-radius: 50%`, and equal width and height <a class="yt-timestamp" data-t="00:07:23">[00:07:41]</a>.

#### Opening and Closing the Dropdown
The `:focus-within` pseudo-selector is used on the `has-dropdown` class to detect when a link inside the dropdown has focus <a class="yt-timestamp" data-t="00:06:48">[00:06:57]</a>. When focused, the dropdown's `opacity` is set to `1` <a class="yt-timestamp" data-t="00:06:58">[00:07:01]</a>. A `transition` property on the parent element makes the dropdown fade in and out <a class="yt-timestamp" data-t="00:06:42">[00:06:46]</a>.

## Dynamic Theme Switching with CSS Variables and JavaScript

### Defining Themes in CSS
Themes are defined by targeting the `:root` element and creating classes like `light`, `dark`, and `solar` <a class="yt-timestamp" data-t="00:07:53">[00:07:59]</a>.
*   Static values like a palette of gray colors, blue, purple, and yellow are defined as [[css_for_styling_and_layout | CSS variables]] on the `:root` <a class="yt-timestamp" data-t="00:08:00">[00:08:14]</a>.
*   These base colors are then used to define UI-specific variables (e.g., `--base-background`, `--nav-background`, `--text-color`, `--border-color`) <a class="yt-timestamp" data-t="00:08:23">[00:08:57]</a>. This allows for creating variables based on other variables, or even complex values like linear gradients <a class="yt-timestamp" data-t="00:08:31">[00:08:48]</a>.

```css
/* Example in :root for light theme */
:root {
  --gray-0: #f0f0f0;
  /* ...other gray colors... */
  --base-background: var(--gray-0);
  --nav-background: linear-gradient(to right, var(--gray-1), var(--gray-3));
  /* ...other variables... */
}
```

For different themes like `dark`, the same variable names are used but with different values, often swapping light grays for dark ones to provide contrast <a class="yt-timestamp" data-t="00:08:59">[00:09:11]</a>. The `solar` theme demonstrates overriding base gray colors directly to introduce a yellow-green shade, allowing it to be applied on top of existing light or dark themes <a class="yt-timestamp" data-t="00:09:21">[00:09:31]</a>.

### Applying Variables to Styles
Existing static color values in the CSS are replaced with the newly defined [[css_for_styling_and_layout | CSS variables]] using the `var()` function <a class="yt-timestamp" data-t="00:09:40">[00:09:44]</a>.
A transition is added to the `background` and `color` properties on the body to animate theme changes, with the background changing slightly faster for a cool offset effect <a class="yt-timestamp" data-t="00:09:50">[00:09:59]</a>.

```css
/* Example in body or specific element */
body {
  background: var(--base-background);
  color: var(--text-color);
  transition: background 0.2s ease-in-out, color 0.3s ease-in-out; /* Animating theme change */
}
```

### JavaScript for Theme Switching
In JavaScript, all theme buttons and the `body` element are first selected from the DOM <a class="yt-timestamp" data-t="00:10:18">[00:10:26]</a>. Click event listeners are then added to each button <a class="yt-timestamp" data-t="00:10:27">[00:10:31]</a>.

*   **Light/Dark Mode**: For mutually exclusive themes like light and dark, the `classList.replace()` method is used on the `body` element to swap themes (e.g., `body.classList.replace('light', 'dark')`) <a class="yt-timestamp" data-t="00:10:33">[00:10:57]</a>.

*   **Solar Theme**: The solar theme is applied conditionally. JavaScript checks if the `body` already contains the `solar` class. If it does, the class is removed; otherwise, it's added <a class="yt-timestamp" data-t="00:11:02">[00:11:13]</a>. The inner text of the solarize button is also updated based on its state <a class="yt-timestamp" data-t="00:11:28">[00:11:32]</a>.

    > You can also directly change [[css_for_styling_and_layout | CSS variables]] by modifying `CSS text` in JavaScript, which is useful for calculating colors dynamically <a class="yt-timestamp" data-t="00:11:14">[00:11:26]</a>.

### Persisting Theme Selection with Local Storage
To prevent theme loss on page refresh, the user's selection is cached in the browser's `localStorage` <a class="yt-timestamp" data-t="00:11:43">[00:11:47]</a>. `localStorage` is a simple key-value store <a class="yt-timestamp" data-t="00:11:47">[00:11:51]</a>.

*   When the script runs (on page load/refresh), it retrieves the saved theme and solar status from `localStorage` <a class="yt-timestamp" data-t="00:11:55">[00:12:01]</a>. If values exist, the corresponding classes are added to the `body` <a class="yt-timestamp" data-t="00:12:01">[00:12:10]</a>.
*   When a theme button is clicked, `localStorage.setItem(key, value)` is called to save the new theme (e.g., `localStorage.setItem('theme', 'dark')`) <a class="yt-timestamp" data-t="00:12:17">[00:12:26]</a>.
*   For the solar theme, `localStorage.removeItem()` is used if it's deactivated, and `localStorage.setItem('isSolar', true)` if it's activated <a class="yt-timestamp" data-t="00:12:31">[00:12:39]</a>.

The browser console can be used to inspect saved `localStorage` values and clear them using `localStorage.clear()` <a class="yt-timestamp" data-t="00:12:47">[00:12:53]</a>.

## Bonus: Rainbow Logo Hover Animation
A final touch is a rainbow animation on logo hover <a class="yt-timestamp" data-t="00:12:56">[00:13:02]</a>.
*   A [[creating_css_animations_based_on_react_state | CSS keyframes]] animation named `color-rotate` is defined <a class="yt-timestamp" data-t="00:13:04">[00:13:07]</a>.
*   This animation transitions the `filter` property's `hue-rotate` from `0deg` to `360deg`, cycling through all colors of the color wheel <a class="yt-timestamp" data-t="00:13:07">[00:13:16]</a>.
*   The animation is applied to the logo on hover using the `animation` property, setting duration, infinite loop, and direction to `alternate` (or `rotate` based on transcript) <a class="yt-timestamp" data-t="00:13:17">[00:13:30]</a>.