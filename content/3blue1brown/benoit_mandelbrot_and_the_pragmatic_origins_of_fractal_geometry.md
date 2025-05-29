---
title: Benoit Mandelbrot and the pragmatic origins of fractal geometry
videoId: gB9n2gHsHN4
---

From: [[3blue1brown]] <br/> 

[[fractal geometry | Fractals]] are often admired for their beautiful blend of simplicity and complexity, frequently featuring infinitely repeating patterns <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. Programmers, in particular, appreciate them for requiring a surprisingly small amount of code to generate intricate images beyond human hand capability <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. However, many people are unaware of the precise definition of a fractal, especially the one conceived by Benoit Mandelbrot, the "father of [[fractal geometry | fractal geometry]]" <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

## Challenging Misconceptions about Fractals

A common [[misconceptions_about_selfsimilarity_in_fractals | misconception]] is that fractals are shapes that are perfectly self-similar <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>. Examples often cited include the Von Koch snowflake, which consists of three perfectly self-similar segments, meaning zooming in reveals an identical copy of the original <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>. Similarly, the famous Sierpinski triangle is composed of three smaller, identical copies of itself <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>. While perfectly self-similar shapes are aesthetically pleasing and serve as useful "toy models" for understanding fractals, Mandelbrot held a much broader view <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.

## Mandelbrot's Pragmatic Vision

Mandelbrot's concept of fractals was not primarily driven by beauty, but by a pragmatic desire to model nature in a way that accurately captures its inherent roughness <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. In a significant sense, [[fractal geometry | fractal geometry]] emerged as a rebellion against calculus, which fundamentally assumes that objects appear smooth when sufficiently magnified <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>. Mandelbrot considered this assumption overly idealized, leading to models that neglected crucial finer details of the phenomena they sought to represent <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.

He observed that self-similar shapes could provide a foundation for modeling regularity within some forms of roughness <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>. However, the popular notion that fractals *only* include perfectly self-similar shapes is itself an over-idealization, contradicting the pragmatic spirit underlying [[fractal geometry | fractal geometry]]'s origins <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>.

## The True Definition: Fractal Dimension

The genuine definition of fractals is intrinsically linked to the idea of [[Fractal dimension and its implications | fractal dimension]] <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>. In this context, "dimension" can be defined such that shapes possess non-integer dimensions <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>. For example:
*   The Sierpinski triangle is approximately 1.585-dimensional <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.
*   The Von Koch curve is approximately 1.262-dimensional <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>.
*   The coastline of Britain measures around 1.21-dimensional <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.

This concept challenges the traditional understanding of dimension as solely whole numbers (e.g., a 1D line, a 2D plane, a 3D space) <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>. While the idea of fractional dimension might initially seem counter-intuitive or "made up," its utility lies in its effectiveness for modeling the real world <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.

### Understanding Dimension Through Scaling

To grasp [[Fractal dimension and its implications | fractal dimension]], it's helpful to first examine perfectly self-similar shapes <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>. Consider how the "mass" (a generalization of length, area, or volume) of a shape changes when it's scaled:
*   **Line (1D)**: A line scaled down by half results in its mass being scaled down by half. Two smaller copies form the original <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>.
*   **Square (2D)**: A square scaled down by half results in its mass being scaled down by one-fourth (1/2 squared). Four smaller copies form the original <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
*   **Cube (3D)**: A cube scaled down by half results in its mass being scaled down by one-eighth (1/2 cubed). Eight smaller copies form the original <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>.

This pattern reveals that for an integer-dimensional shape, when scaled by a factor `s`, its mass changes by `s` raised to the power of its dimension <a class="yt-timestamp" data-t="00:05:59">[00:05:59]</a>.

For a Sierpinski triangle, when scaled down by a factor of one half, its mass is observed to go down by a factor of one third, because three smaller copies form the original <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>. To find its dimension (D), we ask: (1/2)^D = 1/3, which is equivalent to 2^D = 3 <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>. Using logarithms, D = log base 2 of 3, which is approximately 1.585 <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>. This means the Sierpinski triangle is neither strictly 1D nor 2D, but 1.585-dimensional <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>. Its "mass" requires a 1.585-dimensional analog of length or area <a class="yt-timestamp" data-t="00:07:38">[00:07:38]</a>.

Other self-similar examples include:
*   The Von Koch curve: Composed of four smaller copies, each scaled down by one third. Dimension D = log base 3 of 4 ≈ 1.262 <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>.
*   A right-angled Koch curve variant: Built from eight scaled-down copies, each scaled by one fourth. Dimension D = log base 4 of 8 = 3/2 = 1.5 <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>.

### Generalizing Dimension with Box Counting

While useful, "self-similarity dimension" is restrictive <a class="yt-timestamp" data-t="00:09:26">[00:09:26]</a>. Most 2D shapes, like a disk, are not self-similar <a class="yt-timestamp" data-t="00:09:40">[00:09:40]</a>. To generalize, we use the "box-counting" method <a class="yt-timestamp" data-t="00:10:25">[00:10:25]</a>. This involves covering a shape with a grid and counting the number of grid squares it touches <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>. If you scale the shape by a factor `S`, the number of boxes it touches (`N`) should be proportional to `S` raised to the power of its dimension (D): `N = C * S^D` <a class="yt-timestamp" data-t="00:11:04">[00:11:04]</a>.

This method extends to non-self-similar, rough shapes like the coastline of Britain <a class="yt-timestamp" data-t="00:13:00">[00:13:00]</a>. If you scale the coastline, the number of boxes it touches increases approximately in proportion to the scaling factor raised to the power of 1.21 <a class="yt-timestamp" data-t="00:13:07">[00:13:07]</a>.

## Calculating Fractal Dimension Empirically

[[the_application_and_computation_of_fractal_dimensions_in_nature | Computing fractal dimension]] empirically using the box-counting method involves a clever mathematical trick <a class="yt-timestamp" data-t="00:13:29">[00:13:29]</a>. Starting with the relationship `N = C * S^D`, taking the logarithm of both sides gives: `log(N) = log(C) + D * log(S)` <a class="yt-timestamp" data-t="00:14:08">[00:14:08]</a>. This transforms the power relationship into a linear one.

Therefore, if you plot `log(S)` (log of the scaling factor) against `log(N)` (log of the number of boxes touched), the data points should form a line <a class="yt-timestamp" data-t="00:14:18">[00:14:18]</a>. The slope of this line directly gives the empirical measurement of the dimension <a class="yt-timestamp" data-t="00:14:25">[00:14:25]</a>. This makes the concept of [[Fractal dimension and its implications | fractal dimension]] much more tangible and less abstract <a class="yt-timestamp" data-t="00:14:54">[00:14:54]</a>.

## Definition of a Fractal

Essentially, fractals are shapes whose dimension is not an integer, but some fractional amount <a class="yt-timestamp" data-t="00:15:10">[00:15:10]</a>. This provides a quantitative way to describe shapes that are "rough" and remain rough even when zoomed in <a class="yt-timestamp" data-t="00:15:17">[00:15:17]</a>.

### Nuances and Applications

One nuance is that this dimension can sometimes change depending on the zoom level <a class="yt-timestamp" data-t="00:15:38">[00:15:38]</a>. For a purely geometric shape to be a "genuine fractal" in a mathematical sense, it must continue to appear rough even at infinitely close zoom levels <a class="yt-timestamp" data-t="00:17:21">[00:17:21]</a>. This is often defined by the limit of the dimension as the scale becomes finer <a class="yt-timestamp" data-t="00:17:00">[00:17:00]</a>.

In applied settings, such as examining the coastline of Britain, it's not practical to consider infinite zoom levels <a class="yt-timestamp" data-t="00:17:33">[00:17:33]</a>. Instead, a shape is considered a fractal when its measured dimension remains approximately constant across a wide range of scales <a class="yt-timestamp" data-t="00:17:52">[00:17:52]</a>. For instance, the coastline of Britain maintains its roughly 1.21-dimensional roughness even when zoomed in by a factor of a thousand <a class="yt-timestamp" data-t="00:18:00">[00:18:00]</a>. This persistent roughness across scales is the sense in which many natural shapes exhibit a form of self-similarity, though not perfect <a class="yt-timestamp" data-t="00:18:11">[00:18:11]</a>.

Perfectly self-similar shapes are vital in [[fractal geometry | fractal geometry]] as they offer simple, clear examples of this phenomenon of persistent roughness <a class="yt-timestamp" data-t="00:18:19">[00:18:19]</a>. They provide the fundamental tools for modeling fractal phenomena <a class="yt-timestamp" data-t="00:18:34">[00:18:34]</a>.

## Conclusion

Understanding [[Fractal dimension and its implications | fractal dimension]] allows for a quantitative description of roughness <a class="yt-timestamp" data-t="00:18:56">[00:18:56]</a>. For example, the coastline of Norway, with a dimension of about 1.52, is numerically described as more jagged than Britain's coastline <a class="yt-timestamp" data-t="00:19:03">[00:19:03]</a>. A calm ocean surface might have a dimension just above 2, while a stormy one could be closer to 2.3 <a class="yt-timestamp" data-t="00:19:12">[00:19:12]</a>. [[Fractal dimension and its implications | Fractal dimension]] is frequently observed in nature and serves as a key differentiator between naturally occurring objects and man-made ones <a class="yt-timestamp" data-t="00:19:21">[00:19:21]</a>.