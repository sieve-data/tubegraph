---
title: The application and computation of fractal dimensions in nature
videoId: gB9n2gHsHN4
---

From: [[3blue1brown]] <br/> 

[[fractal geometry | Fractals]] are often admired for their beautiful blend of simplicity and complexity, frequently featuring infinitely repeating patterns <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. While many associate fractals with perfectly self-similar shapes, this is a common misconception that does not align with the broader definition envisioned by [[Benoit Mandelbrot and the pragmatic origins of fractal geometry | Benoit Mandelbrot]], often called the father of [[fractal geometry | fractal geometry]] <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>. Mandelbrot's conception was driven by a pragmatic desire to model nature's roughness, rather than idealized smoothness <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.

## Understanding [[fractal dimension and its implications | Fractal Dimension]]

A core concept in [[fractal geometry | fractal geometry]] is [[fractal dimension and its implications | fractal dimension]], which is the main topic of this discussion <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>. In this context, shapes can have dimensions that are any positive real number, not just whole numbers <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>. For example, the [[Selfsimilar shapes versus nonselfsimilar fractals | Sierpinski triangle]] is approximately 1.585D, the Von Koch curve is around 1.262D, and the coastline of Britain is about 1.21D <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>. While the idea of fractional dimension might initially seem nonsensical, it proves to be a useful construct for modeling the world <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.

### Self-Similarity Dimension: A Foundational Concept

To understand [[fractal dimension and its implications | fractal dimension]], it's helpful to start with perfectly [[Selfsimilar shapes versus nonselfsimilar fractals | self-similar shapes]] <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>. These shapes are made up of smaller, identical copies of themselves <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.

Consider the following examples:
*   **Line**: A line can be broken into two smaller lines, each scaled down by half, and two smaller lines can form the original <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>. When scaled down by half, its "mass" (length) is also halved <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>.
*   **Square**: A square consists of four smaller squares, each scaled down by half, and four smaller squares can form the original <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>. When scaled down by half, its "mass" (area) is scaled down by one-fourth <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
*   **Cube**: A cube consists of eight smaller cubes, each scaled down by half, and eight smaller cubes can form the original <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>. When scaled down by half, its "mass" (volume) is scaled down by one-eighth <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.

In these cases, if a shape is scaled by a factor, its mass changes by that factor raised to the power of its dimension <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>.

For fractals like the [[Selfsimilar shapes versus nonselfsimilar fractals | Sierpinski triangle]]:
*   The [[Selfsimilar shapes versus nonselfsimilar fractals | Sierpinski triangle]] is composed of three smaller copies of itself, each with a side length half of the original <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.
*   When scaled down by half, its "mass" effectively goes down by a factor of one-third, as three smaller copies form the original <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.
*   To find its dimension (D), we ask: (1/2)^D = 1/3, which is equivalent to 2^D = 3 <a class="yt-timestamp" data-t="00:06:59">[00:06:59]</a>. This is solved using logarithms: D = log base 2 of 3, which is approximately 1.585 <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>.
*   Similarly, the Von Koch curve is made of four copies, each scaled down by one-third <a class="yt-timestamp" data-t="00:07:53">[00:07:53]</a>. Its dimension is log base 3 of 4, approximately 1.262 <a class="yt-timestamp" data-t="00:08:19">[00:08:19]</a>.

This "self-similarity dimension" provides a clear-cut way to understand fractional dimensions <a class="yt-timestamp" data-t="00:09:23">[00:09:23]</a>.

### Generalizing [[fractal dimension and its implications | Fractal Dimension]]: The Box-Counting Method

The self-similarity definition is restrictive, as most shapes are not perfectly self-similar <a class="yt-timestamp" data-t="00:09:40">[00:09:40]</a>. A more general method for determining dimension is the **box-counting method** <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>.

1.  **Grid Coverage**: Cover the shape with a grid of squares (or cubes in 3D).
2.  **Count Boxes**: Count the number of grid squares that touch the shape <a class="yt-timestamp" data-t="00:10:32">[00:10:32]</a>. This number is proportional to its "measure" (e.g., area for a 2D shape) <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>.
3.  **Scale and Recount**: Scale the shape by a factor (S) and recount the boxes. For a disk, if scaled by S=2, the number of boxes should increase approximately by S^2 (four times), confirming its 2D nature <a class="yt-timestamp" data-t="00:10:59">[00:10:59]</a>. For the [[Selfsimilar shapes versus nonselfsimilar fractals | Sierpinski triangle]] scaled by S=2, the number of boxes increases by approximately 3, reflecting its construction from three smaller copies <a class="yt-timestamp" data-t="00:12:26">[00:12:26]</a>. This relationship can be expressed as: `Number of Boxes = C * S^D`, where C is a constant and D is the dimension <a class="yt-timestamp" data-t="00:13:55">[00:13:55]</a>.

To empirically compute the dimension (D) using the box-counting method, especially for complex shapes:
1.  **Logarithmic Plot**: Take the logarithm of both sides of the equation `Number of Boxes = C * S^D` to get `log(Number of Boxes) = log(C) + D * log(S)` <a class="yt-timestamp" data-t="00:14:14">[00:14:14]</a>.
2.  **Linear Relationship**: Plot `log(S)` against `log(Number of Boxes)`. This plot should approximate a line <a class="yt-timestamp" data-t="00:14:25">[00:14:25]</a>.
3.  **Slope as Dimension**: The slope of this line will be equal to the dimension (D) <a class="yt-timestamp" data-t="00:14:30">[00:14:30]</a>. Programmers can use linear regression on such a log-log plot to find the empirical dimension <a class="yt-timestamp" data-t="00:14:47">[00:14:47]</a>.

## [[fractal dimension and its implications | Fractal Dimensions]] in Nature

The box-counting method makes the idea of [[fractal dimension and its implications | fractal dimension]] more tangible, especially when applied to natural phenomena.

### The Coastline of Britain Example

The classic example of a natural fractal is the coastline of Britain <a class="yt-timestamp" data-t="00:13:04">[00:13:04]</a>. If you count the boxes touching it at various scales, the number of boxes increases approximately in proportion to the scaling factor raised to the power of 1.21 <a class="yt-timestamp" data-t="00:13:21">[00:13:21]</a>. This means the coastline of Britain has a [[fractal dimension and its implications | fractal dimension]] of approximately 1.21.

### Defining a Fractal

Essentially, fractals are shapes whose dimension is not an integer <a class="yt-timestamp" data-t="00:15:14">[00:15:14]</a>. This quantitatively describes them as shapes that are "rough" and remain rough even as you zoom in <a class="yt-timestamp" data-t="00:15:20">[00:15:20]</a>.

A nuance to consider is that the measured dimension can sometimes change based on the zoom level <a class="yt-timestamp" data-t="00:15:47">[00:15:47]</a>. For example, a shape might look 1-dimensional at a distance, then 2-dimensional (like a tube) when zoomed in slightly, and then 1-dimensional again when zoomed in further to reveal intricate curves <a class="yt-timestamp" data-t="00:16:43">[00:16:43]</a>.

*   In **pure mathematics**, a genuine fractal must continue to look rough even at infinite zoom levels, with its dimension being the limit of this slope as zoom levels increase <a class="yt-timestamp" data-t="00:17:17">[00:17:17]</a>.
*   In **applied settings** (like coastlines), a shape is considered a fractal if its measured dimension remains approximately constant across a wide range of scales <a class="yt-timestamp" data-t="00:17:56">[00:17:56]</a>. This approximate self-similarity in roughness is what characterizes many natural fractals, distinguishing them from the idealized, perfectly [[Selfsimilar shapes versus nonselfsimilar fractals | self-similar shapes]] <a class="yt-timestamp" data-t="00:18:16">[00:18:16]</a>.

### Significance of Fractional Dimensions

[[fractal dimension and its implications | Fractal dimension]] provides a quantitative way to describe roughness <a class="yt-timestamp" data-t="00:18:59">[00:18:59]</a>.
*   The coastline of Norway, with a [[fractal dimension and its implications | fractal dimension]] of about 1.52, is numerically communicated as being more jagged than Britain's coastline (1.21D) <a class="yt-timestamp" data-t="00:19:06">[00:19:06]</a>.
*   A calm ocean surface might have a [[fractal dimension and its implications | fractal dimension]] barely above 2, while a stormy one could be closer to 2.3 <a class="yt-timestamp" data-t="00:19:17">[00:19:17]</a>.

This concept frequently arises in nature and appears to be a core differentiator between naturally occurring objects and man-made ones <a class="yt-timestamp" data-t="00:19:29">[00:19:29]</a>.