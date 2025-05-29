---
title: Exploring Fractal Dimension in Mathematical Shapes
videoId: gB9n2gHsHN4
---

From: [[3blue1brown]] <br/> 

Fractals are a beautiful blend of simplicity and complexity, often featuring infinitely repeating patterns <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. While programmers appreciate how little code it takes to produce intricate fractal images <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>, the true definition of a fractal, as envisioned by Benoit Mandelbrot (the "father of fractal geometry"), is often misunderstood <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

## Beyond Perfect Self-Similarity

A common misconception is that fractals must be perfectly self-similar shapes <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>. Examples like the Von Koch snowflake <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a> and the Sierpinski triangle <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a> are perfectly self-similar, meaning that when zoomed in, they reveal identical copies of the original <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. While beautiful and useful as "toy models" for understanding fractals <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>, Mandelbrot's conception was broader, motivated by a pragmatic desire to accurately model the roughness found in nature <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.

[[Fractals and SelfSimilarity Misconceptions and Clarifications | Fractal geometry]] can be seen as a rebellion against calculus, which assumes objects appear smooth when zoomed in sufficiently <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>. Mandelbrot found this overly idealized, leading to models that neglect crucial fine details <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>. While self-similar shapes help model regularity in roughness <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>, the popular view that fractals are *only* perfectly self-similar is an over-idealization that goes against the practical spirit of their origin <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.

## [[Fractal Dimension and Its Application in Nature | Fractal Dimension]]

The true definition of fractals is tied to the idea of [[Fractal Dimension and Its Application in Nature | fractal dimension]] <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>. In this context, shapes can have dimensions that are any positive real number, not just whole numbers <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>. For example:
*   The Sierpinski triangle is approximately 1.585D <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.
*   The Von Koch curve is approximately 1.262D <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>.
*   The coastline of Britain is around 1.21D <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.

While the concept of fractional dimension might seem nonsensical at first, especially from a linear algebra perspective where dimension is typically for natural numbers <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>, [[Fractal Dimension and Its Application in Nature | fractal dimension]] proves to be a useful construct for modeling the world <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.

### Dimension from Scaling and "Mass"

To understand [[Fractal Dimension and Its Application in Nature | fractal dimension]], it helps to start with perfectly self-similar shapes, even those that aren't fractals <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>. Consider a line, a square, a cube, and a Sierpinski triangle <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>. All of these are self-similar:
*   A line scaled by half yields two smaller lines <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>.
*   A square scaled by half yields four smaller squares <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.
*   A cube scaled by half yields eight smaller cubes <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.
*   A Sierpinski triangle scaled by half yields three smaller Sierpinski triangles <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>.

Instead of length, area, or volume, a more general term for measurement is "mass" <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>. [[Fractal Dimension and Its Application in Nature | Fractal dimension]] is about how the "mass" of these shapes changes when scaled <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>:

*   **Line (1D):** Scaling by 1/2 scales mass by 1/2 (since 2 copies form the original) <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>. This is 1/2 to the power of 1.
*   **Square (2D):** Scaling by 1/2 scales mass by 1/4 (since 4 copies form the original) <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>. This is 1/2 to the power of 2.
*   **Cube (3D):** Scaling by 1/2 scales mass by 1/8 (since 8 copies form the original) <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>. This is 1/2 to the power of 3.

In these cases, the exponent of the scaling factor that determines the change in mass *is* the dimension of the shape <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>.

#### Calculating Fractional Dimensions for Self-Similar Fractals

For the Sierpinski triangle, scaling by a factor of 1/2 makes its "mass" go down by a factor of 1/3 (since 3 copies form the original) <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>. To find its dimension (d), we solve for:
(1/2)^d = 1/3 <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>
This is equivalent to 2^d = 3 <a class="yt-timestamp" data-t="00:06:59">[00:06:59]</a>.
Using logarithms, d = log base 2 of 3 ≈ 1.585 <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>.
Thus, the Sierpinski triangle is 1.585-dimensional <a class="yt-timestamp" data-t="00:07:24">[00:07:24]</a>.

Similarly for the Von Koch curve:
*   It's composed of four smaller copies <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>.
*   Each copy is scaled down by 1/3 <a class="yt-timestamp" data-t="00:07:53">[00:07:53]</a>.
*   So, (1/3)^d = 1/4 <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>.
*   This means 3^d = 4 <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>.
*   d = log base 3 of 4 ≈ 1.262 <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>.

Another example is a right-angled Koch curve variant:
*   It's built from eight scaled-down copies <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>.
*   The scaling factor is 1/4 <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>.
*   So, (1/4)^d = 1/8 <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>.
*   This means 4^d = 8 <a class="yt-timestamp" data-t="00:08:56">[00:08:56]</a>.
*   d = log base 4 of 8 = 3/2 = 1.5 <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.

This method is called [[Understanding Fractals and Their Definitions | self-similarity dimension]] <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a>.

### Generalizing Dimension: The Box-Counting Method

The [[Understanding Fractals and Their Definitions | self-similarity dimension]] concept is limited because most shapes are not self-similar <a class="yt-timestamp" data-t="00:09:26">[00:09:26]</a>. For instance, a disk is two-dimensional, but its larger version isn't pieced together from smaller copies <a class="yt-timestamp" data-t="00:09:45">[00:09:45]</a>.

To generalize "mass" for abstract geometric objects, the **box-counting method** is used <a class="yt-timestamp" data-t="00:10:12">[00:10:12]</a>.
1.  Cover the shape with a grid <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>.
2.  Count the number of grid squares (boxes) that touch the shape <a class="yt-timestamp" data-t="00:10:32">[00:10:32]</a>.
3.  Scale up the shape by some factor (S), and count the new number of boxes touched <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>.

For a 2D disk, scaling it up by a factor of 2 should approximately quadruple the number of boxes touched, as the number of boxes is proportional to its area <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>. This relationship becomes more precise with a finer grid <a class="yt-timestamp" data-t="00:11:10">[00:11:10]</a>.

Applying this to the Sierpinski triangle: If scaled by a factor of 2, the proportion of boxes touched by the larger triangle to the smaller one should be about 3 <a class="yt-timestamp" data-t="00:12:06">[00:12:06]</a>. This is because the larger version is built from three copies of the smaller version <a class="yt-timestamp" data-t="00:12:26">[00:12:26]</a>. This value of 3 is equivalent to 2 raised to the power of the Sierpinski triangle's dimension (2^1.585) <a class="yt-timestamp" data-t="00:12:32">[00:12:32]</a>. If plotting the scaling factor (x) against the number of boxes touched (y), the data would fit a curve of the form y = C * x^1.585 <a class="yt-timestamp" data-t="00:12:40">[00:12:40]</a>.

This method is crucial because it applies to non-self-similar shapes with roughness, like the coastline of Britain <a class="yt-timestamp" data-t="00:13:00">[00:13:00]</a>. When scaling the British coastline, the number of boxes touched increases approximately in proportion to the scaling factor raised to the power of 1.21 <a class="yt-timestamp" data-t="00:13:07">[00:13:07]</a>.

### Empirical Calculation

To empirically find the dimension (D) of a shape using the box-counting method, where the number of boxes (N) scales with the scaling factor (S) as N = C * S^D <a class="yt-timestamp" data-t="00:13:42">[00:13:42]</a>:
1.  Take the logarithm of both sides: log(N) = log(C) + D * log(S) <a class="yt-timestamp" data-t="00:14:08">[00:14:08]</a>.
2.  Plot log(S) against log(N) (a "log-log plot") <a class="yt-timestamp" data-t="00:14:18">[00:14:18]</a>.
3.  The relationship should be linear, and the slope of this line will be the dimension (D) <a class="yt-timestamp" data-t="00:14:25">[00:14:25]</a>.
By computing a linear regression on data from various scaling factors, the slope provides an empirical measurement of the dimension <a class="yt-timestamp" data-t="00:14:47">[00:14:47]</a>.

## Defining a Fractal

Essentially, fractals are shapes whose dimension is not an integer, but a fractional amount <a class="yt-timestamp" data-t="00:15:10">[00:15:10]</a>. This provides a quantitative way to describe shapes that are rough and remain rough even when zoomed in <a class="yt-timestamp" data-t="00:15:17">[00:15:17]</a>.

There is a nuance: the measured dimension can sometimes change based on the zoom level <a class="yt-timestamp" data-t="00:15:38">[00:15:38]</a>. For example, a shape that looks one-dimensional (like a line) at a distance might appear two-dimensional (like a tube) when zoomed in, and then one-dimensional again (like winding curves) when zoomed in even further <a class="yt-timestamp" data-t="00:15:52">[00:15:52]</a>.

In pure mathematics, the focus is on the limit of this dimension as zooming approaches infinity <a class="yt-timestamp" data-t="00:17:00">[00:17:00]</a>. A genuine fractal continues to look rough infinitely far <a class="yt-timestamp" data-t="00:17:21">[00:17:21]</a>. In applied settings, like the coastline of Britain, a shape is considered a fractal if its measured dimension remains approximately constant across a wide range of scales <a class="yt-timestamp" data-t="00:17:40">[00:17:40]</a>. This is the sense in which many natural shapes exhibit approximate self-similarity <a class="yt-timestamp" data-t="00:18:11">[00:18:11]</a>.

Perfectly self-similar shapes are important as simple examples of persistent roughness <a class="yt-timestamp" data-t="00:18:19">[00:18:19]</a>, providing tools to model [[the_realworld_implications_of_fractal_geometry | fractal phenomena]] <a class="yt-timestamp" data-t="00:18:34">[00:18:34]</a>. However, they are not the sole or even prototypical example of fractals, as fractals in general possess much more character <a class="yt-timestamp" data-t="00:18:39">[00:18:39]</a>.

[[The RealWorld Implications of Fractal Geometry | Fractal dimension]] offers a quantitative way to describe roughness <a class="yt-timestamp" data-t="00:18:56">[00:18:56]</a>. For instance, the coastline of Norway, with a [[Fractal Dimension and Its Application in Nature | fractal dimension]] of about 1.52, is numerically proven to be more jagged than Britain's coastline (1.21) <a class="yt-timestamp" data-t="00:19:03">[00:19:03]</a>. A calm ocean surface might have a [[Fractal Dimension and Its Application in Nature | fractal dimension]] barely above 2, while a stormy one could be closer to 2.3 <a class="yt-timestamp" data-t="00:19:12">[00:19:12]</a>. [[Fractal Dimension and Its Application in Nature | Fractal dimension]] is frequently observed in nature and helps distinguish naturally occurring objects from those that are man-made <a class="yt-timestamp" data-t="00:19:21">[00:19:21]</a>.