---
title: Fractals and SelfSimilarity Misconceptions and Clarifications
videoId: gB9n2gHsHN4
---

From: [[3blue1brown]] <br/> 

[[understanding_fractals_and_their_definitions | Fractals]] are often admired for their blend of simplicity and complexity, frequently featuring infinitely repeating patterns <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. Programmers particularly appreciate them because they can generate intricate images with minimal code <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. However, the true definition of a fractal, as intended by Benoit Mandelbrot, the "father of fractal geometry," is often misunderstood <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

## Common Misconception: Perfect Self-Similarity

A widespread misconception is that [[understanding_fractals_and_their_definitions | fractals]] are defined as shapes that are perfectly self-similar <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>. Examples often cited include the Von Koch snowflake, which consists of three perfectly self-similar segments <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>, and the Sierpinski triangle, composed of three smaller, identical copies of itself <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>. While these shapes are visually appealing and serve as good models, they represent an over-idealization of what [[understanding_fractals_and_their_definitions | fractals]] truly are <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.

## Mandelbrot's Broader Vision: Modeling Roughness

Benoit Mandelbrot had a much broader conception of [[understanding_fractals_and_their_definitions | fractals]], motivated not by aesthetic beauty but by a practical desire to accurately model the inherent roughness found in nature <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. [[the_realworld_implications_of_fractal_geometry | Fractal geometry]] can be seen as a "rebellion against calculus," which assumes that objects appear smooth when sufficiently zoomed in <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>. Mandelbrot viewed this as an "overly idealized" approach that neglects critical finer details in models <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.

He recognized that self-similar shapes provide a basis for modeling regularity in some forms of roughness <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>. However, the popular notion that [[understanding_fractals_and_their_definitions | fractals]] *only* include perfectly self-similar shapes goes against the pragmatic spirit of [[the_realworld_implications_of_fractal_geometry | fractal geometry]]'s origins <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.

## Defining Fractals through Fractal Dimension

The actual definition of [[understanding_fractals_and_their_definitions | fractals]] centers on the concept of [[fractal_dimension_and_its_application_in_nature | fractal dimension]] <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>. This concept allows for shapes to have dimensions that are any positive real number, not just whole numbers <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>. For instance, the Sierpinski triangle has an approximate dimension of 1.585D, the Von Koch curve is about 1.262D, and even the coastline of Britain turns out to be around 1.21D <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.

Initially, the idea of "fractional dimension" might seem nonsensical, as dimension is typically understood as a natural number (e.g., a line is 1D, a plane 2D) <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>. While the concept of [[fractal_dimension_and_its_application_in_nature | fractal dimension]] is "made up" like all mathematical constructs, its value lies in its usefulness for modeling the world <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.

### Understanding Self-Similarity Dimension

To grasp [[fractal_dimension_and_its_application_in_nature | fractal dimension]], it's helpful to start with perfectly self-similar shapes. Consider how "mass" (generalizing length, area, and volume) changes when shapes are scaled:

*   **Line (1D)**: A line scaled down by a factor of 1/2 has its mass (length) scaled down by 1/2. Two smaller copies form the original <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>.
*   **Square (2D)**: A square scaled down by 1/2 has its mass (area) scaled down by (1/2)^2 = 1/4. Four smaller copies form the original <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
*   **Cube (3D)**: A cube scaled down by 1/2 has its mass (volume) scaled down by (1/2)^3 = 1/8. Eight smaller copies form the original <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>.

This pattern reveals that the mass changes by the scaling factor raised to the power of the shape's dimension <a class="yt-timestamp" data-t="00:05:45">[00:05:45]</a>.

Applying this to self-similar [[understanding_fractals_and_their_definitions | fractals]]:

*   **Sierpinski Triangle**: When scaled down by 1/2, its "mass" goes down by a factor of 1/3, because three smaller copies form the original <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>. To find its dimension (D), we solve (1/2)^D = 1/3, which is equivalent to 2^D = 3. Using logarithms, D = log base 2 of 3, approximately 1.585 <a class="yt-timestamp" data-t="00:06:52">[00:06:52]</a>. Thus, the Sierpinski triangle is 1.585-dimensional <a class="yt-timestamp" data-t="00:07:24">[00:07:24]</a>. Its "mass" is neither length nor area, but rather a 1.585-dimensional analog <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.
*   **Von Koch Curve**: This curve is composed of four smaller copies, each scaled down by 1/3 <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>. So, (1/3)^D = 1/4, or 3^D = 4. D = log base 3 of 4, approximately 1.262 <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>.
*   **Right-angled Koch Curve**: Composed of eight scaled-down copies, with a scaling factor of 1/4 <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>. So, (1/4)^D = 1/8, or 4^D = 8. D = log base 4 of 8, which is exactly 3/2 or 1.5 <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>.

This concept, known as "self-similarity dimension," makes fractional dimension seem reasonable but is limited by its reliance on perfect self-similarity <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a>.

### Generalizing Dimension: The Box-Counting Method

To apply dimension to non-self-similar shapes, a more general method is needed. One common approach is the **box-counting method** <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>:

1.  Cover the shape with a grid of boxes.
2.  Count the number of boxes that touch the shape.
3.  Scale the shape (or equivalently, use a finer grid) and recount the boxes <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>.

For a disk, scaling it by a factor of two should result in approximately four times as many boxes touched, reflecting its 2D nature <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>. For the Sierpinski triangle, scaling by two should result in approximately three times as many boxes touched, confirming its dimension of about 1.585 (since 2^1.585 ≈ 3) <a class="yt-timestamp" data-t="00:12:10">[00:12:10]</a>.

This method is crucial because it applies to shapes that are not self-similar but still exhibit roughness, such as the coastline of Britain <a class="yt-timestamp" data-t="00:13:00">[00:13:00]</a>. If you apply the box-counting method to the coastline of Britain, you'd find that the number of boxes touched increases approximately in proportion to the scaling factor raised to the power of 1.21 <a class="yt-timestamp" data-t="00:13:07">[00:13:07]</a>.

### Empirical Calculation of Fractal Dimension

To empirically calculate the [[exploring_fractal_dimension_in_mathematical_shapes | fractal dimension]] (D) of a shape using the box-counting method, where `N` is the number of boxes touched and `S` is the scaling factor, the relationship is `N = C * S^D` (where C is a constant) <a class="yt-timestamp" data-t="00:13:42">[00:13:42]</a>.

To find D, take the logarithm of both sides: `log(N) = log(C) + D * log(S)` <a class="yt-timestamp" data-t="00:14:08">[00:14:08]</a>. This yields a linear relationship: if you plot `log(N)` against `log(S)`, the slope of the resulting line will be the dimension D <a class="yt-timestamp" data-t="00:14:18">[00:14:18]</a>. By trying various scaling factors and performing linear regression on a log-log plot, one can determine the empirical [[fractal_dimension_and_its_application_in_nature | fractal dimension]] of a shape <a class="yt-timestamp" data-t="00:14:33">[00:14:33]</a>.

## The True Definition of a Fractal

Essentially, [[understanding_fractals_and_their_definitions | fractals]] are shapes whose dimension is not an integer, but instead some fractional amount <a class="yt-timestamp" data-t="00:15:10">[00:15:10]</a>. This provides a quantitative way to describe shapes that are "rough" and remain rough even when zoomed in <a class="yt-timestamp" data-t="00:15:17">[00:15:17]</a>.

While the box-counting dimension can sometimes change based on the zoom level, in pure mathematics, the dimension is typically defined as the limit of this dimension at infinitely close zoom levels <a class="yt-timestamp" data-t="00:15:43">[00:15:43]</a>. For a purely geometric shape to be a "genuine" fractal, it must continue to appear rough even at infinite magnification <a class="yt-timestamp" data-t="00:17:21">[00:17:21]</a>.

In applied settings, such as examining the coastline of Britain, it's not practical to consider infinite zoom <a class="yt-timestamp" data-t="00:17:33">[00:17:33]</a>. Instead, a shape is considered a fractal if its measured dimension remains approximately constant across a wide range of scales, from very zoomed out to very zoomed in <a class="yt-timestamp" data-t="00:17:40">[00:17:40]</a>. The coastline of Britain, for example, maintains its 1.21-dimensional roughness even when zoomed in by a factor of a thousand <a class="yt-timestamp" data-t="00:18:00">[00:18:00]</a>. This highlights how many natural shapes exhibit a form of "imperfect" self-similarity <a class="yt-timestamp" data-t="00:18:11">[00:18:11]</a>.

## Significance of Fractal Dimension

Perfectly self-similar shapes remain important in [[the_realworld_implications_of_fractal_geometry | fractal geometry]] as simplified examples of roughness that persists across scales <a class="yt-timestamp" data-t="00:18:19">[00:18:19]</a>. However, the broader definition of [[fractal_dimension_and_its_application_in_nature | fractal dimension]] allows for a quantitative description of roughness that applies to real-world phenomena <a class="yt-timestamp" data-t="00:18:56">[00:18:56]</a>.

[[fractal_dimension_and_its_application_in_nature | Fractal dimension]] is a powerful tool for understanding the world:
*   The coastline of Norway, with a [[fractal_dimension_and_its_application_in_nature | fractal dimension]] of about 1.52, is numerically proven to be more jagged than Britain's coastline (1.21D) <a class="yt-timestamp" data-t="00:19:03">[00:19:03]</a>.
*   A calm ocean surface might have a [[fractal_dimension_and_its_application_in_nature | fractal dimension]] slightly above 2, while a stormy one could be closer to 2.3 <a class="yt-timestamp" data-t="00:19:12">[00:19:12]</a>.

[[fractal_dimension_and_its_application_in_nature | Fractal dimension]] not only arises frequently in nature but also seems to differentiate naturally occurring objects from man-made ones <a class="yt-timestamp" data-t="00:19:21">[00:19:21]</a>.