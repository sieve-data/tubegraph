---
title: Fractal Dimension and Its Application in Nature
videoId: gB9n2gHsHN4
---

From: [[3blue1brown]] <br/> 

[[understanding_fractals_and_their_definitions | Fractals]] are often admired for their blend of simplicity and complexity, frequently featuring infinitely repeating patterns <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. Programmers, in particular, appreciate how a small amount of code can generate images far more intricate than any human could draw <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.

A common misconception is that [[understanding_fractals_and_their_definitions | fractals]] are shapes that are perfectly self-similar <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>. Examples like the Von Koch snowflake and the Sierpinski triangle exhibit perfect self-similarity, meaning when you zoom in, you see an identical copy of the original <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>. While these shapes are beautiful and serve as good introductory models, Benoit Mandelbrot, the "father of fractal geometry," had a much broader conception in mind <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>, <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.

## Beyond Perfect Self-Similarity

Mandelbrot's view was driven by a pragmatic desire to model nature, specifically to capture its inherent roughness <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. This perspective can be seen as a rebellion against traditional calculus, which assumes objects become smooth when sufficiently zoomed in <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>. Mandelbrot found this assumption overly idealized, leading to models that neglected important fine details <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.

While self-similar shapes provide a basis for understanding regularity in some forms of roughness, the popular belief that [[understanding_fractals_and_their_definitions | fractals]] *only* include perfectly self-similar shapes is an over-idealization that goes against the pragmatic spirit of fractal geometry's origins <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>, <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.

The true definition of [[understanding_fractals_and_their_definitions | fractals]] is tied to the concept of [[exploring_fractal_dimension_in_mathematical_shapes | fractal dimension]] <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>. In this sense, the Sierpinski triangle has a dimension of approximately 1.585, the Von Koch curve around 1.262, and even the coastline of Britain is about 1.21D <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>. This concept allows shapes to have any positive real number as their dimension, not just whole numbers <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.

Initially, the idea of a fractional dimension might seem nonsensical, as dimension is typically understood in terms of natural numbers (e.g., a line is 1D, a plane is 2D) <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>, <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>. However, the utility of [[exploring_fractal_dimension_in_mathematical_shapes | fractal dimension]] lies in its ability to model the world <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.

## Defining Fractal Dimension

The concept of dimension can be understood by examining how a shape's "mass" (or measure) changes when it's scaled <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.

### Self-Similarity Dimension

Consider common geometric shapes:
*   **Line:** If a line is scaled down by a factor of 1/2, its mass (length) is also scaled down by 1/2. Two smaller copies combine to form the original <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>.
*   **Square:** Scaling a square down by 1/2 reduces its mass (area) by a factor of (1/2)², or 1/4. Four smaller copies form the original <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
*   **Cube:** Scaling a cube down by 1/2 reduces its mass (volume) by a factor of (1/2)³, or 1/8. Eight smaller copies form the original <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>.

In these cases, the change in mass is related to the scaling factor raised to the power of the shape's dimension <a class="yt-timestamp" data-t="00:05:45">[00:05:45]</a>. For a d-dimensional shape scaled by a factor of 's', its mass changes by s^d <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>.

Now, consider the Sierpinski triangle:
*   **Sierpinski Triangle:** When scaled down by a factor of 1/2, its mass (measure) reduces by 1/3, because three smaller copies are needed to form the original <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>, <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>. To find its dimension (d), we solve (1/2)^d = 1/3, which is equivalent to 2^d = 3 <a class="yt-timestamp" data-t="00:06:38">[00:06:38]</a>, <a class="yt-timestamp" data-t="00:06:59">[00:06:59]</a>. Using logarithms (log base 2 of 3), the dimension is approximately 1.585 <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>, <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>.
    *   This implies that neither length (1D) nor area (2D) are fitting notions to describe its measure, as its length would be infinite and its area zero <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>. Instead, it requires a 1.585-dimensional analog of length <a class="yt-timestamp" data-t="00:07:38">[00:07:38]</a>.

Other self-similar [[understanding_fractals_and_their_definitions | fractals]] include:
*   **Von Koch Curve:** Composed of four smaller copies scaled down by 1/3 <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>. Its dimension is log base 3 of 4, approximately 1.262 <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>, <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>.
*   **Right-angled Koch Curve variant:** Made of eight copies scaled down by 1/4 <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>. Its dimension is log base 4 of 8, which is exactly 1.5 <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>, <a class="yt-timestamp" data-t="00:08:56">[00:08:56]</a>.

This "self-similarity dimension" method makes the concept of fractional dimension tangible, but it's not a general notion because most shapes are not perfectly self-similar <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a>.

### Box-Counting Dimension (More General Method)

For non-self-similar shapes, a more rigorous mathematical approach is needed to define "mass" or measure. One common method is the "box-counting" method <a class="yt-timestamp" data-t="00:10:25">[00:10:25]</a>.

1.  **Grid Coverage:** Cover the shape with a grid and count the number of grid squares that touch the shape <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>.
2.  **Scaling and Counting:** Scale the shape by a factor (S) and recount the number of touching grid squares <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>.
3.  **Proportionality:** For a shape of dimension 'D', the number of boxes touched should be proportional to S^D <a class="yt-timestamp" data-t="00:11:42">[00:11:42]</a>, <a class="yt-timestamp" data-t="00:13:42">[00:13:42]</a>.
4.  **Log-Log Plot:** To find 'D', take the logarithm of both sides of the relationship. Plotting the log of the scaling factor against the log of the number of boxes should yield a linear relationship, where the slope of the line is the dimension 'D' <a class="yt-timestamp" data-t="00:14:08">[00:14:08]</a>, <a class="yt-timestamp" data-t="00:14:21">[00:14:21]</a>.

This method allows us to measure the dimension of shapes with inherent roughness, like the coastline of Britain <a class="yt-timestamp" data-t="00:13:00">[00:13:00]</a>. Its dimension of approximately 1.21 means that when scaled, the number of boxes touching it increases roughly in proportion to the scaling factor raised to the power of 1.21 <a class="yt-timestamp" data-t="00:13:07">[00:13:07]</a>, <a class="yt-timestamp" data-t="00:13:16">[00:13:16]</a>.

## What Defines a Fractal?

Essentially, [[understanding_fractals_and_their_definitions | fractals]] are shapes whose [[exploring_fractal_dimension_in_mathematical_shapes | dimension]] is not an integer, but a fractional amount <a class="yt-timestamp" data-t="00:15:10">[00:15:10]</a>. This provides a quantitative way to describe shapes that are "rough" and remain rough even when magnified <a class="yt-timestamp" data-t="00:15:17">[00:15:17]</a>, <a class="yt-timestamp" data-t="00:15:20">[00:15:20]</a>.

In pure mathematics, the dimension is often defined as the limit of this value at infinitely close zoom levels <a class="yt-timestamp" data-t="00:17:00">[00:17:00]</a>. This means a geometric fractal must continue to look rough no matter how much you zoom in <a class="yt-timestamp" data-t="00:17:21">[00:17:21]</a>.

In applied settings, such as analyzing the coastline of Britain, it's not feasible to zoom infinitely <a class="yt-timestamp" data-t="00:17:33">[00:17:33]</a>. Instead, a shape is typically considered a [[understanding_fractals_and_their_definitions | fractal]] if its measured dimension remains approximately constant across a wide range of scales <a class="yt-timestamp" data-t="00:17:52">[00:17:52]</a>. For example, the coastline of Britain retains its ~1.21 dimension even when zoomed in by a factor of a thousand <a class="yt-timestamp" data-t="00:18:00">[00:18:00]</a>, <a class="yt-timestamp" data-t="00:18:05">[00:18:05]</a>. This persistent roughness across scales is the true sense in which many natural shapes exhibit self-similarity, though not perfect self-similarity <a class="yt-timestamp" data-t="00:18:11">[00:18:11]</a>.

## Applications in Nature

[[the_realworld_implications_of_fractal_geometry | Fractal dimension]] offers a quantitative way to describe roughness, making it a powerful tool for analyzing natural phenomena <a class="yt-timestamp" data-t="00:18:56">[00:18:56]</a>, <a class="yt-timestamp" data-t="00:18:59">[00:18:59]</a>.

Examples:
*   The coastline of Norway, with a [[exploring_fractal_dimension_in_mathematical_shapes | fractal dimension]] of approximately 1.52, is numerically communicated as being significantly more jagged than Britain's coastline (1.21D) <a class="yt-timestamp" data-t="00:19:03">[00:19:03]</a>.
*   A calm ocean surface might have a [[exploring_fractal_dimension_in_mathematical_shapes | fractal dimension]] just above 2, while a stormy ocean might approach 2.3 <a class="yt-timestamp" data-t="00:19:12">[00:19:12]</a>, <a class="yt-timestamp" data-t="00:19:17">[00:19:17]</a>.

[[exploring_fractal_dimension_in_mathematical_shapes | Fractal dimension]] frequently appears in nature and seems to be a key differentiator between naturally occurring objects and man-made ones <a class="yt-timestamp" data-t="00:19:21">[00:19:21]</a>, <a class="yt-timestamp" data-t="00:19:24">[00:19:24]</a>.