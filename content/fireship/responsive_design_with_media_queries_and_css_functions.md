---
title: Responsive Design with Media Queries and CSS Functions
videoId: Qhaz36TZG5Y
---

From: [[fireship]] <br/> 

When [[css_for_styling_and_layout | CSS]] was initially released, the concept of a responsive layout was still over a decade away from being realized <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>. Today, responsive design is crucial, primarily focusing on adjusting the width of elements based on the available space on a device or within the viewport <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>.

## Media Queries

Historically, [[css_for_styling_and_layout | CSS]] developers have used media queries to achieve responsive layouts <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>. Media queries allow you to apply [[css_for_styling_and_layout | CSS]] rules conditionally, based on characteristics of the viewport, such as its width <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.

For example, one might define an article to have a preferred width of 50%, but then use media queries to set it to a fixed 200 pixels on small screens or 800 pixels on large screens <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>. While effective, media queries can become cumbersome and difficult to manage as a project grows <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.

## Modern CSS Functions (`min()`, `max()`, `clamp()`)

A more modern and efficient approach for handling responsive widths is to use [[css_for_styling_and_layout | CSS]] functions like `min()`, `max()`, and `clamp()` <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>. These functions allow for more concise and maintainable code compared to traditional media queries for certain use cases.

The `clamp()` function, in particular, is powerful. It allows you to define a minimum value, a preferred value, and a maximum value for a property. For instance, an article's width can be set using `clamp()` to have a minimum of 200 pixels, a maximum of 600 pixels, and a preferred value of 50% <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>. This single line of code can replace multiple lines of media query definitions, resulting in a significant code reduction (e.g., 13 lines reduced to 1 for a 92% code reduction in one example) <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.

## Responsive Aspect Ratios

Another aspect of responsive design is maintaining the aspect ratio of elements like images or videos <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>. Traditionally, this required a "padding hack" where a percentage of padding-top (e.g., 56.25% for a 16x9 ratio) was applied to a parent element, and the child content was then absolutely positioned <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>.

Modern [[css_for_styling_and_layout | CSS]] provides the `aspect-ratio` property, which simplifies this process significantly. By defining `aspect-ratio` directly on the element (e.g., `aspect-ratio: 16 / 9;`), the desired aspect ratio is maintained, eliminating the need for the older padding-based hack <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>. While not universally supported everywhere yet, this property is a cleaner and more direct solution <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>.