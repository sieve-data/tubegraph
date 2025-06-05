---
title: Creating a dropdown menu with CSS
videoId: rXuHGLzSmSE
---

From: [[fireship]] <br/> 

A dropdown menu can be built using only [[CSS for Styling and Layout | CSS]] without requiring [[JavaScript]] <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. This method uses CSS techniques to keep the dropdown open <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.

## HTML Structure for the Dropdown <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>

To create the dropdown in HTML, follow these steps:
*   Inside your existing navigation bar, add an additional `<li>` (list item) element <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>.
*   Give this `<li>` element a class, such as `has-drop-down` <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>.
*   Inside this `<li>`, add a link (`<a>` tag) and then an additional `<ul>` (unordered list) element. This `<ul>` will represent the dropdown menu itself <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>.
*   The dropdown `<ul>` will contain several dropdown items, each as an `<li>` <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>.
*   Each individual dropdown `<li>` will have its own link (`<a>` tag) <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.
*   For these links, provide an `id` that represents the desired action (e.g., `id="light"`, `id="dark"`, `id="solar"`) <a class="yt-timestamp" data-t="00:05:33">[00:05:33]</a>.

## Styling the Dropdown with CSS <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>

The dropdown menu requires specific [[CSS for Styling and Layout | CSS]] properties for positioning and visibility:

*   **Positioning**: Set `position: absolute;` for the dropdown menu `<ul>` <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>.
*   **Dimensions**: Assign a `fixed width` (e.g., `500px`) <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>.
*   **Initial Visibility**: Set `opacity: 0;` by default to make it invisible until focused <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>.
*   **Stacking Context**: Set `z-index: 2;` (or a value greater than its parent) to ensure it appears on top of the main navbar <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>.
*   **Appearance**: Add a `background` color and a `border` <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>. You can round out specific corners using `border-bottom-left-radius` and `border-bottom-right-radius` <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>.
*   **Item Layout**: For the actual buttons or links inside the dropdown, use [[CSS for Styling and Layout | flexbox]] by setting `display: flex;` on their container. Align items to the center (`align-items: center;`) and space them evenly (`justify-content: space-around;`) <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>.
*   **Visual Enhancements**:
    *   Add a `box-shadow` for depth <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>.
    *   Adjust horizontal positioning using `transform: translateX()` to center it under the parent link <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>.
    *   Ensure each link inside the dropdown takes up all available space <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>.

## Opening and Closing the Dropdown with CSS <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>

The key to a [[CSS for Styling and Layout | CSS-only dropdown]] is using the `:focus-within` pseudo-selector:

*   **Focus Detection**: Use `:focus-within` on the `.has-drop-down` class (the parent `<li>`) to detect when any element *inside* the dropdown (like a link) has focus <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.
*   **Visibility Change**: When an element inside the dropdown is focused, set the `opacity` of the dropdown `<ul>` to `1` <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>.
*   **Smooth Transition**: Apply a `transition` property (e.g., `transition: opacity 0.3s;`) to the dropdown `<ul>` to make the opacity fade in and out smoothly when it gains or loses focus <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>.

This setup allows the dropdown to fade in when the theme link is clicked (gaining focus) and fade out when clicked outside (losing focus) <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>.

## Adding Color Indicators (Circles) <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>

You can display a circle next to each link in the dropdown with a corresponding color for its theme:

*   **Pseudo-element**: Target the `::before` pseudo-element of each link in the dropdown <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.
*   **Content**: Set `content: '';` for the pseudo-element <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>.
*   **Shape**: Give it a `border` (e.g., `2px`), a `border-radius: 50%;`, and equal `width` and `height` to create a perfect circle <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>.
*   **Alignment**: Refine the alignment and margins as needed <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>.