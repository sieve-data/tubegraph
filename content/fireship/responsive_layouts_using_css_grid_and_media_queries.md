---
title: Responsive layouts using CSS Grid and media queries
videoId: 705XCEruZFs
---

From: [[fireship]] <br/> 

[[Basics of CSS Grid | CSS Grid]] is a powerful [[css_for_styling_and_layout | CSS]] layout system that simplifies the creation of complex and responsive web designs <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. It can replace many use cases previously handled by grid systems like Twitter Bootstrap, often with significantly less code and markup <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>.

## Benefits of CSS Grid

Historically, developers often relied on Flexbox-based systems or third-party [[css_for_styling_and_layout | CSS]] frameworks like Bootstrap for layouts <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. While these solutions are viable, [[Basics of CSS Grid | CSS Grid]] offers several advantages:
*   **Reduced Bundle Size** [[Basics of CSS Grid | CSS Grid]] is a native browser feature, so it doesn't add extra [[css_for_styling_and_layout | CSS]] to a project's bundle size <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.
*   **Simplified Codebase** Moving to [[Basics of CSS Grid | CSS Grid]] can drastically simplify HTML markup by removing numerous classes previously needed for responsiveness <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. A functional grid system might only require three lines of code <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.
*   **Print-Inspired Design** [[Basics of CSS Grid | CSS Grid]] is inspired by print-based grids, making it easier to implement complex and beautiful designs often found in magazines <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>.

## Building a Responsive 12-Column Grid

The first example demonstrates [[building_a_responsive_12_column_grid | building a responsive 12-column grid]] that can serve as an infinite set of responsive columns, useful for feeds of cards <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.

### Basic Setup
1.  **HTML Structure** Create a `section` element to act as the main grid container. Immediate children inside this container are known as grid items <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.
2.  **Display Grid** Set `display: grid` on the container to enable grid layout <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.
3.  **Spacing** Use the `gap` property (e.g., `gap: 1rem`) on the container to ensure consistent spacing between items horizontally and vertically, avoiding the need for margins on individual children <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.

### Creating Columns
*   **Explicit Grid** The `grid-template-columns` property defines columns. `1fr` (one fractional unit) represents one part of the available space <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>. For example, `grid-template-columns: 1fr 1fr` creates two equal columns <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.
*   **Repeat Function** To avoid verbose code for many columns (e.g., 12 columns), use the `repeat()` function: `repeat(12, 1fr)` <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>.
*   **Min/Max Sizing** To ensure columns have a minimum width but can still expand, use `minmax()`: `repeat(12, minmax(240px, 1fr))` <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>. This ensures columns don't go below 240 pixels but can grow to fill available space <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>.

### Responsiveness with Implicit Grid
*   **`autofit`** To make columns break into additional rows when space runs out, use `autofit` with `repeat()`: `repeat(autofit, minmax(240px, 1fr))` <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>. This tells [[Basics of CSS Grid | Grid]] to calculate the number of rows and columns on the fly, creating a truly responsive grid with just three lines of code <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.
*   **`autofill` vs. `autofit`**
    *   `autofill` creates additional columns when space becomes available, even if there are no items to fill them <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>.
    *   `autofit` expands existing children to take up all available space when there are fewer items than available slots <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>.

### Debugging
*   **Firefox Dev Tools** [[Basics of CSS Grid | Firefox Dev Tools]] include a robust [[Basics of CSS Grid | Grid]] and Flexbox inspector that allows visualization of grid lines and tracks <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.

## Creating a Responsive Photo Gallery

This example shows [[creating_a_responsive_photo_gallery_with_css_grid | creating a responsive photo gallery]] where items can have varying sizes (taller, wider) and gracefully reposition themselves on viewport changes <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>.

### Grid Setup
1.  **HTML** Use a grid container with multiple `div` elements, each serving as a card with a photo as its background <a class="yt-timestamp" data-t="00:05:33">[00:05:33]</a>.
2.  **Auto Rows** For implicit grids, `grid-auto-rows` can set a fixed height for automatically created rows (e.g., `grid-auto-rows: 240px`) <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>.

### Sizing Individual Grid Items
*   **`grid-row`** To make an item span multiple rows vertically, use `grid-row: span 2` (span 2 rows from its starting position) or explicitly define start and end lines (e.g., `grid-row: 1 / 4`) <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>.
*   **`grid-column`** To make an item span multiple columns horizontally, use `grid-column: span 2` <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>.

### Responsive Adjustments with Media Queries
*   **[[css_and_html_tips_for_responsive_design | Media Queries]]** To prevent oversized items on smaller screens, wrap the `grid-row` and `grid-column` classes in a [[css_and_html_tips_for_responsive_design | media query]]. For instance, `@media (min-width: 600px)` ensures these styles only apply on viewports wider than 600 pixels <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.

## Implementing a Staggered Intro Animation in CSS Grid

This example demonstrates [[implementing_a_staggered_intro_animation_in_css_grid | implementing a staggered intro animation in CSS Grid]] using an explicit grid and advanced [[css_for_styling_and_layout | CSS]] properties <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>.

### Explicit Grid with Named Areas
1.  **`grid-template-areas`** This property allows you to define an explicit grid by assigning names to different grid areas (e.g., `'a b c'`) <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>. This provides a visual representation of the layout <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>.
2.  **Sizing Rows and Columns**
    *   **Rows** Use `grid-template-rows` (e.g., `repeat(4, 25%)` for 25% height for each of 4 rows in a fixed-height container) <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>.
    *   **Columns** Use `grid-template-columns` with fixed widths and `auto` for responsive middle columns (e.g., `240px auto auto 240px`) <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>.
3.  **Placing Children** Use `grid-area` on individual grid items to place them into the named areas defined by `grid-template-areas` (e.g., `grid-area: a;`) <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>.

### Staggered Intro Animation
1.  **[[css_for_styling_and_layout | CSS]] Variable for Delay** Define a [[css_for_styling_and_layout | CSS]] variable for the staggered delay (e.g., `--stagger-delay: 50ms`) <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a>.
2.  **Keyframe Animation** Create a `@keyframes` animation to define the start (`from`) and end (`to`) states of the animation <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>.
    *   **`from` State**: `opacity: 0; transform: scale(0.3); filter: hue-rotate(180deg);` <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>. The `hue-rotate` creates a rainbow-like color change <a class="yt-timestamp" data-t="00:09:58">[00:09:58]</a>.
    *   **`to` State**: `opacity: 1; transform: scale(1); filter: hue-rotate(0deg);` <a class="yt-timestamp" data-t="00:10:02">[00:10:02]</a>.
3.  **Apply Animation to Cards**
    *   Set `animation` properties on all grid items: `animation: intro 700ms ease-out;` <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>.
    *   Use `animation-fill-mode: backwards` to ensure elements start at their first keyframe value (invisible in this case) before the animation begins <a class="yt-timestamp" data-t="00:10:26">[00:10:26]</a>.
4.  **Staggering with `animation-delay` and `calc()`**
    *   Apply `animation-delay` to each individual element.
    *   Use the [[css_for_styling_and_layout | CSS]] `calc()` function to multiply the element's order by the `--stagger-delay` variable (e.g., `animation-delay: calc(1 * var(--stagger-delay));`) <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>. This creates the staggered effect <a class="yt-timestamp" data-t="00:10:48">[00:10:48]</a>.
    *   For efficiency with many items, preprocessors like SAS can generate these delays using programmatic loops <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>.

By leveraging [[Basics of CSS Grid | CSS Grid]]'s capabilities, it's possible to create unique, responsive, and animated layouts without the need for JavaScript or external [[css_for_styling_and_layout | CSS]] frameworks <a class="yt-timestamp" data-t="00:11:14">[00:11:14]</a>.