---
title: Basics of CSS Grid
videoId: 705XCEruZFs
---

From: [[fireship]] <br/> 

[[CSS for Styling and Layout | CSS Grid]] is a powerful layout system that enables developers to build complex, responsive web designs with minimal code <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. It simplifies code, removes the need for excessive HTML markup, and works natively in the browser without adding to bundle size <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>. Its design principles are inspired by print-based grids, making it easier to implement magazine-like layouts <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.

## Core Concepts

### Setting up a Grid Container
To begin using [[CSS for Styling and Layout | CSS Grid]], the `display` property of the container element must be set to `grid` <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>. All immediate children inside this container become "grid items" <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.

### Spacing with `gap`
The `gap` property can be used on the grid container to provide consistent spacing between grid items, both horizontally and vertically, without needing to set margins on individual children <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.

### Defining Columns with `grid-template-columns`
The `grid-template-columns` property defines the structure of columns in the grid <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.

*   **Fractional Units (`fr`)**: `1fr` represents one part of the available space <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>. For example, two `1fr` columns would each take up 50% of the available space <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.
*   **`repeat()` Function**: Instead of writing out each column manually, the `repeat()` function allows for concise repetition of column definitions, e.g., `repeat(12, 1fr)` for twelve equal columns <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
*   **`minmax()` Function**: This function allows setting a minimum and maximum size for grid tracks. For instance, `minmax(240px, 1fr)` ensures columns are at least 240 pixels wide but can expand up to one fractional unit <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.

### Implicit Grids and Responsiveness (`autofit` vs. `autofill`)
To create a truly [[responsive_layouts_using_css_grid_and_media_queries | responsive grid]] that breaks into additional rows when space is limited, an implicit grid can be created using `autofit` or `autofill` with the `repeat()` function <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>.
*   **`autofit`**: Calculates the number of rows and columns on the fly and expands its children to take up all available space <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.
*   **`autofill`**: Creates additional columns when there is extra space, but the items don't expand to fill the entire width <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.

### Sizing Rows with `grid-auto-rows`
For implicit grids where content might not dictate row height, `grid-auto-rows` can be used to set a fixed height for all automatically created rows <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>.

### Spanning Grid Items
Individual grid items can span across multiple rows or columns:
*   **`grid-row`**: Controls an item's vertical span <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>. `span 2` makes an item span two rows from its starting position <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>. It can also be explicitly defined by line numbers, e.g., `grid-row: 1 / 4` <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.
*   **`grid-column`**: Controls an item's horizontal span <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>. Similarly, `span 2` makes an item span two columns <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a>.

### Defining Areas with `grid-template-areas`
`grid-template-areas` is a property that allows defining an explicit grid layout by assigning names to different areas <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>. These names can then be assigned to individual grid items using the `grid-area` property, allowing them to occupy the defined area regardless of their order in the HTML <a class="yt-timestamp" data-t="00:09:13">[00:09:13]</a>.

## Practical Examples

### [[building_a_responsive_12_column_grid | Building a Responsive 12-Column Grid]]
[[CSS for Styling and Layout | CSS Grid]] can replace grid systems like Twitter Bootstrap by creating a responsive 12-column layout with only three lines of code and reducing complex HTML markup <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. This type of grid is useful for layouts with a feed of cards <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>.

```css
.container {
  display: grid;
  gap: 1rem;
  grid-template-columns: repeat(autofit, minmax(240px, 1fr));
}
```

### [[creating_a_responsive_photo_gallery_with_css_grid | Creating a Responsive Photo Gallery]]
[[CSS for Styling and Layout | CSS Grid]] allows for the creation of responsive mosaic photo galleries where items of different sizes (taller, wider) reposition gracefully when the viewport changes <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>. This is achieved by combining `grid-auto-rows` with `grid-row` and `grid-column` to span items <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>.
[[CSS and HTML tips for responsive design | Media queries]] can be used to apply spanning classes only above a certain minimum width (e.g., 600 pixels) to ensure better appearance on smaller screens <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>.

### [[implementing_a_staggered_intro_animation_in_css_grid | Implementing a Staggered Intro Animation]]
An explicit grid defined with `grid-template-areas` can be combined with [[CSS for Styling and Layout | CSS]] keyframe animations to create unique effects like staggered intro animations, without JavaScript or external frameworks <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>.
*   **Keyframe Animations**: Define `from` (starting) and `to` (ending) states for properties like `opacity`, `scale`, and `hue-rotate` <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>.
*   **`animation-fill-mode: backwards`**: Ensures elements start at their first keyframe value (e.g., invisible) before the animation begins <a class="yt-timestamp" data-t="00:10:26">[00:10:26]</a>.
*   **Staggering**: Achieved by setting an `animation-delay` on individual elements using the `calc()` function and a CSS variable for the delay <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>. For example, `animation-delay: calc(1 * var(--stagger-delay))` <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>. Preprocessors like Sass can make this more efficient with programmatic loops <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a>.

## Development Tips

*   **Firefox DevTools**: Firefox provides a robust grid and flexbox inspector that visualizes grid lines and tracks, which is invaluable for debugging <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.
*   **Code Along**: It's recommended to code along with examples by creating HTML and [[CSS for Styling and Layout | CSS]] files or cloning a project from GitHub <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.