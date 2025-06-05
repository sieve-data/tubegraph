---
title: Using Flexbox and CSS Grid for Layout
videoId: Qhaz36TZG5Y
---

From: [[fireship]] <br/> 

Layout, or the positioning of elements relative to each other, has historically been one of the most challenging aspects of [[css_for_styling_and_layout | CSS]] <a class="yt-timestamp" data-t="02:27:13">[02:27:13]</a>. Modern [[css_for_styling_and_layout | CSS]] offers powerful tools like Flexbox and Grid to address these challenges, making layout much more intuitive <a class="yt-timestamp" data-t="02:50:42">[02:50:42]</a>.

## Flexbox

Flexbox is a modern [[css_for_styling_and_layout | CSS]] feature that allows you to create a flexible column or row anywhere in the UI <a class="yt-timestamp" data-t="02:53:23">[02:53:23]</a>. When an element has `display: flex`, it gains an X and Y axis for aligning its children <a class="yt-timestamp" data-t="02:57:04">[02:57:04]</a>.

*   **Main Axis**: Children flow along the main axis <a class="yt-timestamp" data-t="03:03:04">[03:03:04]</a>. They can be centered using the `justify-content` property <a class="yt-timestamp" data-t="03:06:08">[03:06:08]</a>.
*   **Cross Axis**: Perpendicular to the main axis <a class="yt-timestamp" data-t="03:09:05">[03:09:05]</a>. Elements can be moved to the center using the `align-items` property <a class="yt-timestamp" data-t="03:11:09">[03:11:09]</a>.

Flexbox is often the first tool to reach for when it comes to layout <a class="yt-timestamp" data-t="03:14:04">[03:14:04]</a>. However, for complex UIs with many intersecting rows and columns, it can lead to an accumulation of non-semantic container or wrapper elements in the HTML, which are only there for [[css_for_styling_and_layout | CSS]] to attach to <a class="yt-timestamp" data-t="03:18:14">[03:18:14]</a>.

## CSS Grid

[[css_for_styling_and_layout | CSS]] Grid is a modern [[css_for_styling_and_layout | CSS]] feature that can significantly reduce code compared to Flexbox for complex layouts <a class="yt-timestamp" data-t="03:32:02">[03:32:02]</a>. Unlike Flexbox, which focuses on individual columns and rows, Grid allows you to think about the big-picture layout <a class="yt-timestamp" data-t="03:37:04">[03:37:04]</a>. It's similar to the old table layout but is much more developer-friendly <a class="yt-timestamp" data-t="03:44:03">[03:44:03]</a>.

When an element is set to `display: grid`, its children can be defined as a collection of columns and rows <a class="yt-timestamp" data-t="03:51:04">[03:51:04]</a>.

*   **Columns**: Their width can be defined using the `grid-template-columns` property <a class="yt-timestamp" data-t="03:55:03">[03:55:03]</a>.
    *   The `fr` (fractional unit) value allows columns to proportionally share the available space in the grid <a class="yt-timestamp" data-t="04:04:02">[04:04:02]</a>.
*   **Rows**: Can be defined in a similar manner <a class="yt-timestamp" data-t="04:10:07">[04:10:07]</a>.

With Grid, elements inside the grid are positioned automatically <a class="yt-timestamp" data-t="04:12:04">[04:12:04]</a>, which can eliminate a significant amount of HTML and [[css_for_styling_and_layout | CSS]] code compared to Flexbox or traditional table layouts <a class="yt-timestamp" data-t="04:15:06">[04:15:06]</a>.

## Debugging Layouts

Firefox Dev Tools are generally superior for debugging [[css_for_styling_and_layout | CSS]], especially when it comes to layout <a class="yt-timestamp" data-t="02:02:00">[02:02:00]</a>. They provide nice graphics for visualizing both Flex and Grid layouts <a class="yt-timestamp" data-t="02:23:08">[02:23:08]</a>.