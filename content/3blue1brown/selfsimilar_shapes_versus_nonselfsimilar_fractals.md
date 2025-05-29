---
title: Selfsimilar shapes versus nonselfsimilar fractals
videoId: gB9n2gHsHN4
---

From: [[3blue1brown]] <br/> 

Fractals are often perceived as a beautiful blend of simplicity and complexity, frequently displaying infinitely repeating patterns <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. Programmers, in particular, appreciate them because intricate images can be produced with surprisingly little code <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. However, a common [[misconceptions_about_selfsimilarity_in_fractals | misconception]] about fractals is that they must be perfectly self-similar <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.

## The Role of Self-Similar Shapes

Perfectly self-similar shapes are those where, when you zoom in, you find an identical copy of the original <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. Examples include:
*   The Von Koch snowflake, which consists of three perfectly self-similar segments <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>.
*   The Sierpinski triangle, composed of three smaller, identical copies of itself <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.

While beautiful, self-similar shapes serve as a useful "toy model" for understanding what fractals truly are <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>. They provide simple, low-information examples of the phenomenon of roughness that persists across many scales <a class="yt-timestamp" data-t="00:18:23">[00:18:23]</a>.

## Benoit Mandelbrot's Broader Conception of Fractals

[[Benoit Mandelbrot and the pragmatic origins of fractal geometry | Benoit Mandelbrot]], considered the father of [[fractal geometry | fractal geometry]], held a much broader view of fractals than just perfect self-similarity <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. His motivation was pragmatic: to model nature in a way that accurately captures roughness, rather than focusing solely on beauty <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.

[[fractal geometry | Fractal geometry]] can be seen as a "rebellion against calculus," which assumes that objects become smooth when zoomed in far enough <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>. Mandelbrot viewed this assumption as overly idealized, leading to models that neglected important finer details <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>. He recognized that self-similar shapes could model regularity in some forms of roughness <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>. However, the popular belief that fractals *only* include perfectly self-similar shapes is an over-idealization that goes against the pragmatic origins of [[fractal geometry | fractal geometry]] <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.

## Defining Fractals Through Fractal Dimension

The true definition of fractals is tied to the concept of [[fractal dimension and its implications | fractal dimension]], which is typically not an integer <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>. This provides a quantitative way to describe shapes that are rough and remain rough even when magnified <a class="yt-timestamp" data-t="00:15:17">[00:15:17]</a>.

For example, the Sierpinski triangle has a dimension of approximately 1.585D <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>, and the Von Koch curve is around 1.262D <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>. In general, shapes can have dimensions that are any positive real number, not just whole numbers <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.

### Self-Similarity Dimension (A Starting Point)

To understand [[fractal dimension and its implications | fractal dimension]], it's helpful to start with perfectly self-similar shapes and consider how their "mass" changes when scaled <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>. The term "mass" generalizes concepts like length, area, and volume <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>.

| Shape               | Scaling Factor (s) | Number of Copies (N) | Mass Scaled by | Dimension (D) = log(N) / log(1/s) |
| :------------------ | :----------------- | :------------------- | :------------- | :-------------------------------- |
| Line                | 1/2                | 2                    | 1/2            | 1                                 |
| Square              | 1/2                | 4                    | 1/4            | 2                                 |
| Cube                | 1/2                | 8                    | 1/8            | 3                                 |
| Sierpinski Triangle | 1/2                | 3                    | 1/3            | log₂(3) ≈ 1.585 <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>   |
| Von Koch Curve      | 1/3                | 4                    | 1/4            | log₃(4) ≈ 1.262 <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>   |
| Right-angled Koch Curve | 1/4            | 8                    | 1/8            | log₄(8) = 1.5 <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>   |

This concept of "self-similarity dimension" shows how fractional dimensions can arise <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a>. However, it's not a general notion because it relies on a shape being perfectly reconstructible from smaller copies of itself <a class="yt-timestamp" data-t="00:09:26">[00:09:26]</a>.

### Generalizing Dimension: The Box-Counting Method

For shapes that are not perfectly self-similar, a more rigorous mathematical approach is needed to define "mass" and subsequently, dimension <a class="yt-timestamp" data-t="00:10:12">[00:10:12]</a>. The box-counting method is a common technique:
1.  Cover the shape with a grid <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>.
2.  Count the number of grid squares (or cubes in 3D) that touch the shape <a class="yt-timestamp" data-t="00:10:32">[00:10:32]</a>.
3.  Scale the shape by a factor (S) and recount the number of touching boxes (N) <a class="yt-timestamp" data-t="00:10:48">[00:10:48]</a>.

For a D-dimensional shape, the number of boxes N will be proportional to S^D (N ≈ C * S^D) <a class="yt-timestamp" data-t="00:13:46">[00:13:46]</a>. To find D, one can take the logarithm of both sides: log(N) = D * log(S) + log(C) <a class="yt-timestamp" data-t="00:14:08">[00:14:08]</a>. Plotting log(S) against log(N) should yield a linear relationship, where the slope of the line is the dimension (D) <a class="yt-timestamp" data-t="00:14:18">[00:14:18]</a>. This allows for empirical measurement of dimension using linear regression <a class="yt-timestamp" data-t="00:14:47">[00:14:47]</a>.

## Non-Self-Similar Fractals in Nature

This box-counting method can be applied to complex, non-self-similar shapes found in nature, like the [[the_application_and_computation_of_fractal_dimensions_in_nature | coastline of Britain]] <a class="yt-timestamp" data-t="00:13:00">[00:13:00]</a>. The [[the_application_and_computation_of_fractal_dimensions_in_nature | coastline of Britain]] has a fractal dimension of approximately 1.21D <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>. This means that if you scale it, the number of boxes touching it increases roughly in proportion to the scaling factor raised to the power of 1.21 <a class="yt-timestamp" data-t="00:13:16">[00:13:16]</a>.

### Nuances of Fractal Dimension

The measured dimension can sometimes change depending on the zoom level <a class="yt-timestamp" data-t="00:15:43">[00:15:43]</a>. For example, a thick, winding line might appear one-dimensional at a very fine scale, two-dimensional like a tube at an intermediate scale, and one-dimensional again at a coarser scale <a class="yt-timestamp" data-t="00:16:06">[00:16:06]</a>.

In pure mathematics, the dimension is often defined by the limit of this measurement as you zoom in infinitely far <a class="yt-timestamp" data-t="00:17:00">[00:17:00]</a>. This means a genuine fractal must appear rough even at arbitrary zoom levels <a class="yt-timestamp" data-t="00:17:21">[00:17:21]</a>. In applied settings, a shape is considered fractal if its measured dimension remains *approximately constant* across a sufficiently wide range of scales <a class="yt-timestamp" data-t="00:17:52">[00:17:52]</a>. For example, the [[the_application_and_computation_of_fractal_dimensions_in_nature | coastline of Britain]] consistently exhibits a dimension of around 1.21, even when zoomed in significantly <a class="yt-timestamp" data-t="00:18:00">[00:18:00]</a>. This persistence of roughness across scales is what allows many natural shapes to be considered self-similar, even if not perfectly so <a class="yt-timestamp" data-t="00:18:11">[00:18:11]</a>.

## Conclusion

[[fractal dimension and its implications | Fractal dimension]] offers a quantitative way to describe roughness <a class="yt-timestamp" data-t="00:18:56">[00:18:56]</a>. For instance, the [[the_application_and_computation_of_fractal_dimensions_in_nature | coastline of Norway]] is about 1.52 dimensional, indicating it is more jagged than Britain's coastline (1.21D) <a class="yt-timestamp" data-t="00:19:03">[00:19:03]</a>. A calm ocean surface might have a dimension barely above 2, while a stormy one could be closer to 2.3 <a class="yt-timestamp" data-t="00:19:12">[00:19:12]</a>. This numerical description of roughness is a core differentiator between naturally occurring objects and man-made ones <a class="yt-timestamp" data-t="00:19:24">[00:19:24]</a>.