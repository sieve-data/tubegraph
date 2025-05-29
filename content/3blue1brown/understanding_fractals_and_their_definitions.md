---
title: Understanding Fractals and Their Definitions
videoId: gB9n2gHsHN4
---

From: [[3blue1brown]] <br/> 

Fractals are often appreciated for their beautiful blend of simplicity and complexity, frequently featuring infinitely repeating patterns <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. Programmers, in particular, favor them due to the surprisingly small amount of code required to generate intricate images far beyond human drawing capabilities <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.

## Misconceptions About Fractals

A common misconception is that fractals are shapes that are perfectly self-similar <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>. Examples include the Von Koch snowflake, which consists of three segments, each a perfectly identical, scaled-down copy of the original when zoomed in <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>. Similarly, the Sierpinski triangle is composed of three smaller identical copies of itself <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>. While perfectly self-similar shapes are visually appealing and serve as good "toy models" for fractals, they don't capture the full essence of what fractals truly are <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.

## Benoit Mandelbrot's Broader Conception

Benoit Mandelbrot, the father of [[Fractal Dimension and Its Application in Nature | fractal geometry]], held a much broader view of fractals <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>. His motivation wasn't primarily beauty but a pragmatic desire to model nature by capturing roughness <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. [[Fractal Dimension and Its Application in Nature | Fractal geometry]] can be seen as a rebellion against calculus, which assumes smoothness upon sufficient zooming <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>. Mandelbrot found this assumption overly idealized, leading to models that neglect crucial finer details <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>. He observed that while self-similar shapes help model regularity in some forms of roughness, the popular belief that fractals are *only* perfectly self-similar is an over-idealization that contradicts the pragmatic origins of [[Fractal Dimension and Its Application in Nature | fractal geometry]] <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>.

## The True Definition: [[Fractal Dimension and Its Application in Nature | Fractal Dimension]]

The real definition of fractals is tied to the concept of [[Fractal Dimension and Its Application in Nature | fractal dimension]] <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>. This concept suggests that shapes can have dimensions that are any positive real number, not just whole numbers <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>. For example:
*   The Sierpinski triangle is approximately 1.585-dimensional (1.585D) <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.
*   The Von Koch curve is approximately 1.262D <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>.
*   The coastline of Britain is around 1.21D <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.

Initially, the idea of fractional dimension might seem nonsensical, as dimension is typically understood for natural numbers (e.g., a line is 1D, a plane is 2D, space is 3D) <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>. While the idea of [[Fractal Dimension and Its Application in Nature | fractal dimension]] is a mathematical construct, its utility lies in its ability to model the world <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.

### Self-Similarity Dimension

To understand [[Fractal Dimension and Its Application in Nature | fractal dimension]], it's helpful to start with perfectly self-similar shapes, even those not considered fractals <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>. Consider:
*   **Line**: Can be broken into two smaller lines, each scaled down by half <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>. Scaling down by half reduces its "mass" (length) by half <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>.
*   **Square**: Can be broken into four smaller squares, each scaled down by half <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>. Scaling down by half reduces its "mass" (area) by a fourth <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
*   **Cube**: Can be broken into eight smaller cubes, each scaled down by half <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>. Scaling down by half reduces its "mass" (volume) by an eighth (one half cubed) <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>.
*   **Sierpinski triangle**: Made of three smaller copies, each with a side length half of the original <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>. Scaling down by half reduces its "mass" by a third, as it takes three smaller copies to form the original <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.

This concept of "mass" generalizes length, area, and volume <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>. [[Fractal Dimension and Its Application in Nature | Fractal dimension]] describes how the mass of these shapes changes when scaled <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.

For lines, squares, and cubes, the mass changes by the scaling factor raised to an integer power, which corresponds to their dimension <a class="yt-timestamp" data-t="00:05:45">[00:05:45]</a>. Generalizing, a shape is *D*-dimensional if scaling it by a factor `S` changes its mass by `S^D` <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>.

Applying this to the Sierpinski triangle:
*   Scaled down by `1/2`, its mass goes down by `1/3` <a class="yt-timestamp" data-t="00:06:38">[00:06:38]</a>.
*   We seek `D` such that `(1/2)^D = 1/3` <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>.
*   This is equivalent to `2^D = 3`, solved by `D = log_2(3)` <a class="yt-timestamp" data-t="00:06:59">[00:06:59]</a>.
*   `log_2(3)` is approximately `1.585` <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>.

For the Von Koch curve:
*   Composed of four smaller copies, each scaled down by `1/3` <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>.
*   Scaling factor `1/3`, mass reduction factor `1/4` <a class="yt-timestamp" data-t="00:07:57">[00:07:57]</a>.
*   We seek `D` such that `(1/3)^D = 1/4`, or `3^D = 4` <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.
*   `D = log_3(4)`, which is approximately `1.262` <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>.

Another example, a right-angled version of the Koch curve:
*   Built from eight scaled-down copies, with a scaling factor of `1/4` <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>.
*   We seek `D` such that `(1/4)^D = 1/8`, or `4^D = 8` <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>.
*   `D = log_4(8)`, which is exactly `3/2` or `1.5` <a class="yt-timestamp" data-t="00:08:56">[00:08:56]</a>.

This "self-similarity dimension" makes the idea of fractional dimension more intuitive, but it's not a general notion as it relies on the shape's ability to be rebuilt from smaller copies <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a>.

### Box-Counting Method

For non-self-similar shapes, like a disk or the coastline of Britain, a more rigorous method is needed to define "mass" <a class="yt-timestamp" data-t="00:10:12">[00:10:12]</a>. One common approach is the box-counting method:
1.  **Cover the shape with a grid**: Highlight and count the number of grid squares (or cubes in 3D) that touch the shape <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>.
2.  **Scale the shape**: Scale the shape by a factor `S` and recount the number of touching grid squares <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>.
3.  **Analyze the proportionality**: For a 2D disk, the number of touching squares should increase approximately in proportion to the square of the scaling factor (e.g., scale by 2, count 4 times as many boxes) <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>. This becomes more accurate with a finer grid <a class="yt-timestamp" data-t="00:11:10">[00:11:10]</a>.

For a [[Fractal Dimension and Its Application in Nature | fractal]], like the Sierpinski triangle, if scaled by a factor of two, the proportion of boxes touched by the larger version to the smaller one should be about three <a class="yt-timestamp" data-t="00:12:10">[00:12:10]</a>. This implies `2^D ≈ 3`, where `D` is the dimension, `1.585` <a class="yt-timestamp" data-t="00:12:32">[00:12:32]</a>. Plotting the scaling factor against the number of boxes touched would show data fitting a curve `y = x^(1.585)` (multiplied by a constant) <a class="yt-timestamp" data-t="00:12:40">[00:12:40]</a>.

This method can be applied to non-self-similar, rough shapes like the coastline of Britain <a class="yt-timestamp" data-t="00:13:00">[00:13:00]</a>. When scaled, the number of boxes touching the coastline increases approximately in proportion to the scaling factor raised to the power of `1.21` <a class="yt-timestamp" data-t="00:13:07">[00:13:07]</a>.

To empirically compute this dimension for any shape:
1.  The number of boxes (`N`) touching a shape scaled by `S` is `N ≈ C * S^D` (where `C` is a constant and `D` is the dimension) <a class="yt-timestamp" data-t="00:13:42">[00:13:42]</a>.
2.  Taking the logarithm of both sides gives `log(N) ≈ log(C) + D * log(S)` <a class="yt-timestamp" data-t="00:14:08">[00:14:08]</a>.
3.  Plotting `log(S)` against `log(N)` will yield a linear relationship where the slope of the line is the dimension `D` <a class="yt-timestamp" data-t="00:14:18">[00:14:18]</a>. This allows for linear regression to find the best fit line and determine the empirical dimension <a class="yt-timestamp" data-t="00:14:33">[00:14:33]</a>.

## Definition of a Fractal

Essentially, fractals are shapes whose [[Fractal Dimension and Its Application in Nature | fractal dimension]] is not an integer, but a fractional amount <a class="yt-timestamp" data-t="00:15:10">[00:15:10]</a>. This quantitatively describes shapes that are rough and remain rough even upon zooming in <a class="yt-timestamp" data-t="00:15:17">[00:15:17]</a>.

## Nuances and Applied Settings

The measured dimension can sometimes change based on how far zoomed in one is <a class="yt-timestamp" data-t="00:15:43">[00:15:43]</a>. For example, a winding 3D shape might appear 1D (like a line) when far out, then 2D (like a tube) when moderately zoomed in, and finally 1D again (like individual curves) when very zoomed in <a class="yt-timestamp" data-t="00:15:52">[00:15:52]</a>.

In pure mathematics, various definitions of dimension focus on the limit of this dimension at infinitely close zoom levels <a class="yt-timestamp" data-t="00:17:00">[00:17:00]</a>. A geometric shape is a "genuine fractal" if it continues to look rough infinitely <a class="yt-timestamp" data-t="00:17:21">[00:17:21]</a>.

In applied settings, such as examining the coastline of Britain, it's not feasible to zoom infinitely <a class="yt-timestamp" data-t="00:17:33">[00:17:33]</a>. Instead, a shape is typically considered a fractal if its measured dimension remains approximately constant across a wide range of scales <a class="yt-timestamp" data-t="00:17:40">[00:17:40]</a>. The coastline of Britain, for instance, maintains a roughness of around 1.21 dimension even when zoomed in by a factor of a thousand <a class="yt-timestamp" data-t="00:18:00">[00:18:00]</a>. This persistent roughness across scales is the sense in which many natural shapes exhibit self-similarity, though not perfectly <a class="yt-timestamp" data-t="00:18:11">[00:18:11]</a>.

Perfectly self-similar shapes are valuable in [[Fractal Dimension and Its Application in Nature | fractal geometry]] as they offer simple, low-information examples of persistent roughness, providing primitive tools for modeling [[Fractal Dimension and Its Application in Nature | fractal phenomena]] <a class="yt-timestamp" data-t="00:18:19">[00:18:19]</a>. However, they are not the sole or prototypical examples, as fractals generally possess much more character <a class="yt-timestamp" data-t="00:18:39">[00:18:39]</a>.

## [[The RealWorld Implications of Fractal Geometry | Real-World Implications of Fractal Dimension]]

[[Fractal Dimension and Its Application in Nature | Fractal dimension]] provides a quantitative way to describe roughness <a class="yt-timestamp" data-t="00:18:56">[00:18:56]</a>. For example:
*   The coastline of Norway is about 1.52-dimensional, numerically indicating it is much more jagged than Britain's coastline <a class="yt-timestamp" data-t="00:19:03">[00:19:03]</a>.
*   A calm ocean surface might have a [[Fractal Dimension and Its Application in Nature | fractal dimension]] just above 2, while a stormy one might be closer to 2.3 <a class="yt-timestamp" data-t="00:19:12">[00:19:12]</a>.

[[Fractal Dimension and Its Application in Nature | Fractal dimension]] frequently appears in nature and seems to be a core differentiator between naturally occurring objects and man-made ones <a class="yt-timestamp" data-t="00:19:21">[00:19:21]</a>.