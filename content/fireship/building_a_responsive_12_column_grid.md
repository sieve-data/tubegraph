---
title: Building a responsive 12 column grid
videoId: 705XCEruZFs
---

From: [[fireship]] <br/> 

This article details how to build a responsive 12-column grid using CSS Grid, which can replace common grid systems like Twitter Bootstrap while requiring significantly less code and markup <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. This approach requires only three lines of code and eliminates the need for extensive HTML markup <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>.

## Benefits of CSS Grid for Layouts

The CSS Grid system works natively in the browser, meaning you don't need to add additional CSS to your bundle size, unlike third-party solutions <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>. It significantly simplifies the codebase; for example, a previous Flexbox-based system on Fireship.io that used many classes for responsive columns was replaced with a three-line CSS Grid system <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. [[css_for_styling_and_layout | CSS Grid]] also makes it easier to implement complex designs typically found in magazines because its system is inspired by print-based grids <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>.

> [!WARNING] Learning Curve
> CSS Grid can initially be "pretty weird to learn" <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>.

## Setting Up the Grid

This 12-column grid is essentially an infinite set of responsive columns <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. It's useful for displaying a feed of cards, similar to the lesson feed on Fireship.io <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>.

### HTML Structure
Start by creating an HTML file and adding boilerplate code <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>. Within the `<head>` of the document, add a `<style>` tag and import a base CSS file along with the specific CSS for the grid <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>. The base CSS file, used across examples, includes a class that defines a Flexbox to center its content, but this is not required for the grid functionality itself <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.

In the `<body>`, set up a `<section>` to serve as the main grid container <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>. All immediate children inside this container are considered grid items <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>. For demonstration, 12 children are added, assuming the content inside the grid is dynamic (e.g., 3, 50, or any number of items) <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>. The goal is to create an implicit grid that can determine the correct number of columns and rows based on content and viewport size <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.

### Core CSS Properties

1.  **`display: grid`**: The first step is to apply `display: grid` to the container <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>. Initially, items will stack in a single column <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.

2.  **`gap`**: To add spacing between children, use the `gap` property (e.g., `gap: 1rem`) <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>. This ensures consistent horizontal and vertical spacing between items without needing to set margins on individual children <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.

### Defining Columns

#### Explicit Grid with `grid-template-columns`

One way to create columns is by using the `grid-template-columns` property <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.
*   **Fractional Units (`fr`)**: `1fr` (one fractional unit) represents one part of the available space <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>. If only one column is defined as `1fr`, it takes up 100% of the available space <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>. Adding another `1fr` creates a second column, making each `1fr` equal to 50% of the space <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>. This can be repeated for as many columns as needed, such as 12 columns <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.

    ```css
    .container {
        display: grid;
        grid-template-columns: 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr; /* 12 columns */
        gap: 1rem;
    }
    ```

    This creates an explicit grid that always has 12 columns <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>, but it's not responsive and the code is "ugly" <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>.

#### Using `repeat()` for Conciseness

CSS Grid provides a `repeat()` helper function <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>. Instead of manually writing out each column, you can use `repeat(12, 1fr)` <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>. This code is identical in function but much more concise and readable <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>.

```css
.container {
    display: grid;
    grid-template-columns: repeat(12, 1fr);
    gap: 1rem;
}
```

## Creating a Responsive Implicit Grid

With `repeat(12, 1fr)`, columns might become too thin <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>. To address this and make the grid responsive, use `minmax()` and `autofit`.

### Setting Minimum Width with `minmax()`

The `minmax()` function allows you to define a minimum and maximum size for grid tracks <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.
*   `minmax(240px, 1fr)` ensures columns don't go below 240 pixels in width but allows them to expand up to `1fr` (one fractional unit of available space) <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>.
*   However, if you repeat `minmax(240px, 1fr)` 12 times (`repeat(12, minmax(240px, 1fr))`), the columns will still overflow horizontally if there isn't enough space <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.

### Automatic Column and Row Breakdown with `autofit`

To make columns break into additional rows when space is limited, create an implicit grid by using `autofit` instead of a fixed number in `repeat()` <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>.
*   `repeat(autofit, minmax(240px, 1fr))` tells Grid to calculate the number of rows and columns on the fly based on content and viewport size <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.

```css
.container {
    display: grid;
    grid-template-columns: repeat(autofit, minmax(240px, 1fr));
    gap: 1rem;
}
```

This single line (along with `display: grid;` and `gap: 1rem;`) creates a truly responsive grid <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a> without additional markup or classes in your HTML <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>.

### `autofit` vs. `autofill`

While similar, `autofit` and `autofill` have a subtle but important difference <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>:
*   **`autofill`**: Creates additional columns when extra space becomes available, even if there are no items to fill them <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.
*   **`autofit`**: Expands its children to take up all available space, rather than creating empty tracks <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>.

## Debugging with Developer Tools

If your grid is not behaving as expected, open Firefox Dev Tools, which includes an excellent grid and Flexbox inspector <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>. This tool allows you to visualize the lines and tracks on the grid, aiding in debugging <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.