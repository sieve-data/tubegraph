---
title: Creating a responsive photo gallery with CSS Grid
videoId: 705XCEruZFs
---

From: [[fireship]] <br/> 

This article details how to build a responsive mosaic photo gallery using [[Basics of CSS Grid | CSS Grid]] <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>. The gallery features photos of varying sizes that gracefully reposition themselves when the viewport changes <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>.

## HTML Structure <a class="yt-timestamp" data-t="00:05:33">[00:05:33]</a>

Begin by setting up a grid container in your HTML <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>. Inside this container, include multiple `div` elements, with each `div` having a photo URL as its background <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>. These photos can be sourced from platforms like Unsplash <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>.

## Setting Row Height <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>

Initially, the rows in an implicit grid might appear very short because they are automatically sized to the text content within the children <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>. To ensure all rows are a consistent height, such as 240 pixels tall, you can set the `grid-auto-rows` property on the container <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>. This ensures each automatically created row will be fixed to that height <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>.

```css
.grid-container {
    display: grid;
    /* ... other grid properties ... */
    grid-auto-rows: 240px; /* Sets all automatically created rows to 240px tall */
}
```

## Sizing Individual Grid Items <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>

To make individual grid items span multiple rows or columns, specific classes can be created:

*   **Making an item taller:** To span an item across multiple rows vertically, use the `grid-row` property with `span 2` <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>. This tells the item to span two rows from its starting position <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>. The grid algorithm can automatically determine the ending point <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>.

    ```css
    .card-tall {
        grid-row: span 2; /* Spans the item across two rows */
    }
    ```

    > Using `grid-row: span 2` is more flexible than explicitly defining start and end lines (e.g., `grid-row: 1 / 4`) because it adapts better within an implicit grid <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>. Firefox DevTools can help visualize grid lines and tracks to understand how items are placed <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>.

*   **Making an item wider:** Similarly, to make an item wider, use the `grid-column` property with `span 2` <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>.

    ```css
    .card-wide {
        grid-column: span 2; /* Spans the item across two columns */
    }
    ```

Once these classes are defined, apply them to the specific `div` elements within your HTML to achieve the desired mosaic layout <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>.

## Ensuring Responsiveness with Media Queries <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>

A potential issue with sizing items using `span` on smaller screens is that they might become too skinny or break the layout <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>. To fix this, wrap the `card-tall` and `card-wide` classes within a [[responsive_layouts_using_css_grid_and_media_queries | media query]] <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>. This ensures these sizing rules are only applied when the viewport `min-width` is greater than a specified value, such as 600 pixels <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>.

```css
@media (min-width: 600px) {
    .card-tall {
        grid-row: span 2;
    }
    .card-wide {
        grid-column: span 2;
    }
}
```

This approach allows items to adjust gracefully on smaller devices, providing a truly responsive photo gallery <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>.