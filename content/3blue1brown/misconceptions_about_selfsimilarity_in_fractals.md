---
title: Misconceptions about selfsimilarity in fractals
videoId: gB9n2gHsHN4
---

From: [[3blue1brown]] <br/> 

## Defining Fractals Beyond Perfect Self-Similarity

Many people mistakenly believe that [[fractal_geometry | fractals]] are exclusively shapes that are perfectly self-similar, meaning they contain infinitely repeating patterns where zooming in reveals perfectly identical copies of the original shape <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. This is a common misconception about the definition of a fractal, especially when compared to the broader view held by [[benoit_mandelbrot_and_the_pragmatic_origins_of_fractal_geometry | Benoit Mandelbrot]], the "father of [[fractal_geometry | fractal geometry]]" <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.

### Examples of Perfectly Self-Similar Shapes

Shapes often cited as examples of fractals include:
*   **Von Koch Snowflake:** This shape consists of three segments, each of which is perfectly self-similar, revealing an identical copy of the original when zoomed in <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>.
*   **Sierpinski Triangle:** Composed of three smaller, identical copies of itself <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.

While these [[selfsimilar_shapes_versus_nonselfsimilar_fractals | self-similar shapes]] are visually appealing and serve as good "toy models" for understanding [[visualization_and_characteristics_of_fractal_patterns | fractal patterns]], they represent an over-idealization that goes against the pragmatic origins of [[fractal_geometry | fractal geometry]] <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.

## Mandelbrot's Broader Conception of Fractals

Mandelbrot's vision for fractals was not primarily driven by beauty, but by a pragmatic desire to model the inherent "roughness" found in nature <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. [[fractal_geometry | Fractal geometry]] can be seen as a challenge to calculus, which assumes that objects appear smooth when zoomed in far enough <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>. Mandelbrot viewed this as an overly idealized approach that neglects crucial finer details in natural phenomena <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.

Perfectly [[selfsimilar_shapes_versus_nonselfsimilar_fractals | self-similar shapes]] offer a basis for modeling regularity in some forms of roughness <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>. However, the popular belief that fractals are *only* these perfectly self-similar shapes is a misconception that ironically contradicts the practical spirit behind [[benoit_mandelbrot_and_the_pragmatic_origins_of_fractal_geometry | fractal geometry's origins]] <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>.

## The True Definition: Fractal Dimension

The actual definition of fractals is rooted in the concept of [[fractal_dimension_and_its_implications | fractal dimension]] <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>. This concept allows for shapes to have dimensions that are not whole numbers but "fractional amounts" <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>, such as:
*   The Sierpinski triangle is approximately 1.585-dimensional <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.
*   The Von Koch curve is approximately 1.262-dimensional <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>.
*   The coastline of Britain is around 1.21-dimensional <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.

This [[fractal_dimension_and_its_implications | non-integer dimension]] provides a quantitative way to describe a shape's roughness and its persistence even when magnified <a class="yt-timestamp" data-t="00:15:17">[00:15:17]</a>.

### Understanding Fractal Dimension through Scaling

The concept of [[fractal_dimension_and_its_implications | fractal dimension]] can be understood by examining how a shape's "mass" changes when it is scaled <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>. For perfectly [[selfsimilar_shapes_versus_nonselfsimilar_fractals | self-similar shapes]], the dimension can be derived from the scaling factor and the number of copies needed to reconstruct the original <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>.

For example:
*   A line (1D) scaled by 1/2 has its "mass" (length) reduced by 1/2 <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>.
*   A square (2D) scaled by 1/2 has its "mass" (area) reduced by (1/2)^2 = 1/4 <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
*   A cube (3D) scaled by 1/2 has its "mass" (volume) reduced by (1/2)^3 = 1/8 <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>.
*   The Sierpinski triangle scaled by 1/2 has its "mass" reduced by 1/3, as it takes three smaller copies to form the original <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>. This means its dimension (D) is found by solving (1/2)^D = 1/3, which is D = log base 2 of 3, or approximately 1.585 <a class="yt-timestamp" data-t="00:06:52">[00:06:52]</a>.

This concept extends to non-self-similar shapes using methods like "box-counting," where the number of grid squares touching a shape is counted at different scales <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>. The relationship between the scaling factor and the number of boxes touched reveals the [[fractal_dimension_and_its_implications | fractal dimension]] <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a>. This is how the dimension of natural objects like the coastline of Britain (approx. 1.21) can be determined <a class="yt-timestamp" data-t="00:13:04">[00:13:04]</a>.

### Nuance in Defining Dimension

The measured [[fractal_dimension_and_its_implications | dimension]] can sometimes vary depending on the zoom level, especially for non-idealized shapes <a class="yt-timestamp" data-t="00:15:43">[00:15:43]</a>. In pure mathematics, definitions of [[fractal_dimension_and_its_implications | dimension]] often focus on the limit as one zooms in infinitely close <a class="yt-timestamp" data-t="00:17:00">[00:17:00]</a>, implying a shape must remain rough at arbitrary scales to be a "genuine fractal" <a class="yt-timestamp" data-t="00:17:21">[00:17:21]</a>.

In applied settings, such as measuring a coastline, the dimension is considered fractal if it remains approximately constant across a wide range of scales, even if not perfectly self-similar <a class="yt-timestamp" data-t="00:17:52">[00:17:52]</a>. For example, the coastline of Britain maintains its 1.21-dimensional roughness even when zoomed in by a factor of a thousand <a class="yt-timestamp" data-t="00:18:00">[00:18:00]</a>. This demonstrates that many natural shapes exhibit a form of [[selfsimilar_shapes_versus_nonselfsimilar_fractals | self-similarity]], albeit not perfect <a class="yt-timestamp" data-t="00:18:11">[00:18:11]</a>.

## The Role of Perfectly Self-Similar Shapes

[[selfsimilar_shapes_versus_nonselfsimilar_fractals | Perfectly self-similar shapes]] are valuable in [[fractal_geometry | fractal geometry]] because they offer simple, "low-information" examples of the phenomenon of roughness that persists across multiple scales <a class="yt-timestamp" data-t="00:18:19">[00:18:19]</a>. They provide fundamental tools for modeling [[visualization_and_characteristics_of_fractal_patterns | fractal phenomena]] <a class="yt-timestamp" data-t="00:18:34">[00:18:34]</a>. However, it's crucial not to consider them the sole or "prototypical" examples of fractals, as fractals in general possess a much wider range of characteristics <a class="yt-timestamp" data-t="00:18:39">[00:18:39]</a>.

The ability to quantitatively describe roughness using [[fractal_dimension_and_its_implications | fractional dimension]] allows for differentiation between natural objects, such as the more jagged coastline of Norway (about 1.52 dimensional) compared to Britain's (about 1.21 dimensional), or a calm ocean surface (barely above 2) versus a stormy one (closer to 2.3) <a class="yt-timestamp" data-t="00:19:03">[00:19:03]</a>. This concept often distinguishes naturally occurring objects from man-made ones <a class="yt-timestamp" data-t="00:19:21">[00:19:21]</a>.