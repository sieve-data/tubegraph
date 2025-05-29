---
title: Fractal dimension and its implications
videoId: gB9n2gHsHN4
---

From: [[3blue1brown]] <br/> 

## What is a Fractal?

Fractals are often perceived as a beautiful blend of simplicity and complexity, frequently featuring [[visualization_and_characteristics_of_fractal_patterns | infinitely repeating patterns]] <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. Programmers are particularly fond of them due to the small amount of code required to produce intricate images <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.

A [[misconceptions_about_selfsimilarity_in_fractals | common misconception is that fractals are shapes that are perfectly self-similar]] <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>. While shapes like the Von Koch snowflake <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a> and Sierpinski triangle <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a> are perfectly self-similar, producing identical copies when zoomed in, [[benoit_mandelbrot_and_the_pragmatic_origins_of_fractal_geometry | Benoit Mandelbrot]], the "father of [[fractal_geometry | fractal geometry]]" <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>, had a broader definition in mind <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. His motivation was a pragmatic desire to accurately model nature's roughness, rather than just beauty <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.

[[fractal_geometry | Fractal geometry]] can be seen as a rebellion against calculus, which assumes smoothness upon sufficient zooming <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>. Mandelbrot viewed this as overly idealized, neglecting finer details crucial for accurate modeling <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>. The [[popular perception that fractals only include perfectly self-similar shapes is another over-idealization]], contradicting the pragmatic origins of [[fractal_geometry | fractal geometry]] <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>.

The true definition of fractals is tied to the concept of **fractal dimension** <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>. This concept allows shapes to have a dimension that is any positive real number, not just whole numbers <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>. For example, the Sierpinski triangle is approximately 1.585-dimensional, the Von Koch curve is about 1.262-dimensional, and the coastline of Britain is around 1.21-dimensional <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>. While the idea of fractional dimension might initially seem counter-intuitive, it proves to be a useful construct for modeling the world <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.

## Self-Similarity Dimension

To understand fractal dimension, it helps to start with [[selfsimilar_shapes_versus_nonselfsimilar_fractals | self-similar shapes]] <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>. These shapes are built up from smaller, identical copies of themselves.

Consider how the "mass" of a shape changes when scaled down:
*   **Line (1D):** A line scaled down by a factor of one-half has its mass (length) scaled down by one-half. Two smaller copies make up the original <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.
*   **Square (2D):** A square scaled down by one-half has its mass (area) scaled down by one-fourth (½²). Four smaller copies make up the original <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.
*   **Cube (3D):** A cube scaled down by one-half has its mass (volume) scaled down by one-eighth (½³). Eight smaller copies make up the original <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.

In these cases, the factor by which the mass changes is the scaling factor raised to the power of the shape's dimension <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>.

### Calculating Dimension for Fractals

*   **Sierpinski Triangle:** When scaled down by one-half, its mass goes down by a factor of one-third, as it's made of three smaller copies <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>. To find its dimension (D), we solve: (1/2)^D = 1/3. This is equivalent to 2^D = 3, which means D = log₂(3) ≈ 1.585 <a class="yt-timestamp" data-t="00:06:52">[00:06:52]</a>. Thus, the Sierpinski triangle is 1.585-dimensional <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>.
*   **Von Koch Curve:** This curve is composed of four smaller copies of itself, each scaled down by one-third <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>. So, (1/3)^D = 1/4, or 3^D = 4, meaning D = log₃(4) ≈ 1.262 <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>.
*   **Right-angled Koch Curve:** This fractal is built from eight scaled-down copies, with a scaling factor of one-fourth <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>. So, (1/4)^D = 1/8, or 4^D = 8, meaning D = log₄(8) = 3/2 = 1.5 <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>.

This method, known as self-similarity dimension, makes the concept of fractional dimension reasonable, but it's not general enough for all shapes <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a>.

## Generalizing to Non-Self-Similar Shapes (Box Counting Method)

The concept of "mass" can be made more rigorous using a grid-based approach. For a disk, which is 2D, we expect its area (mass) to scale by the square of the scaling factor <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>.

### The Box-Counting Method

1.  **Grid Coverage:** Cover the shape with a grid and count the number of grid squares that touch the shape <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>.
2.  **Scaling and Counting:** Scale up the shape by a factor (S) and count how many grid squares touch the new, scaled version <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>.
3.  **Dimension Relation:** The number of boxes (N) touched by the scaled shape should be proportional to S^D, where D is the dimension <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>.

For a Sierpinski triangle, scaling it up by a factor of two should result in approximately three times the number of boxes touched, because it's built from three smaller copies <a class="yt-timestamp" data-t="00:12:19">[00:12:19]</a>. This means the data for the Sierpinski triangle would fit a curve of y = x^1.585, multiplied by a constant <a class="yt-timestamp" data-t="00:12:40">[00:12:40]</a>.

This method can be applied to non-self-similar, rough shapes like the coastline of Britain. When scaled, the number of boxes touching the coastline increases approximately proportional to the scaling factor raised to the power of 1.21 <a class="yt-timestamp" data-t="00:13:07">[00:13:07]</a>.

### Empirical Computation of Fractal Dimension

To empirically compute the dimension of a shape:
1.  **Data Collection:** Try various scaling factors (S) and count the number of boxes (N) touching the shape for each factor <a class="yt-timestamp" data-t="00:13:37">[00:13:37]</a>. The relationship is N ≈ C * S^D <a class="yt-timestamp" data-t="00:13:46">[00:13:46]</a>.
2.  **Log-Log Plot:** Take the logarithm of both sides: log(N) ≈ log(C) + D * log(S) <a class="yt-timestamp" data-t="00:14:08">[00:14:08]</a>.
3.  **Linear Regression:** Plot log(S) against log(N). This relationship should appear as a line, and the **slope of that line is the empirical measurement for the dimension** <a class="yt-timestamp" data-t="00:14:18">[00:14:18]</a>.

## Implications and Characteristics of Fractal Dimension

With this understanding, the definition of a fractal is a shape whose dimension is not an integer, but some fractional amount <a class="yt-timestamp" data-t="00:15:10">[00:15:10]</a>. This provides a quantitative way to describe shapes that are "rough" and remain rough even upon zooming in <a class="yt-timestamp" data-t="00:15:17">[00:15:17]</a>.

However, a nuance is that the measured dimension can sometimes change based on the zoom level <a class="yt-timestamp" data-t="00:15:43">[00:15:43]</a>. For example, a winding shape in 3D might appear 1D at a distance, 2D (like a tube) when scaled up, and then 1D again when zoomed in further to reveal the curves <a class="yt-timestamp" data-t="00:15:52">[00:15:52]</a>.

In pure mathematics, various definitions of dimension focus on the limit of this dimension at closer and closer zoom levels <a class="yt-timestamp" data-t="00:17:00">[00:17:00]</a>. For a purely geometric shape to be a "genuine fractal," it must continue to appear rough even at infinite zoom <a class="yt-timestamp" data-t="00:17:21">[00:17:21]</a>.

In applied settings, such as examining the coastline of Britain, one looks at a wide range of scales. A shape is typically considered a fractal if its measured dimension remains approximately constant across multiple scales <a class="yt-timestamp" data-t="00:17:52">[00:17:52]</a>. The coastline of Britain, for instance, maintains its 1.21-dimensional roughness even when zoomed in by a factor of a thousand <a class="yt-timestamp" data-t="00:18:00">[00:18:00]</a>. This persistent roughness is the sense in which many natural shapes exhibit self-similarity, though not perfectly <a class="yt-timestamp" data-t="00:18:11">[00:18:11]</a>.

[[Selfsimilar_shapes_versus_nonselfsimilar_fractals | Perfectly self-similar shapes]] are important for providing simple examples of persistent roughness <a class="yt-timestamp" data-t="00:18:19">[00:18:19]</a>, but it's crucial not to view them as the only type of fractal, as fractals in general possess much more varied characteristics <a class="yt-timestamp" data-t="00:18:39">[00:18:39]</a>.

## [[The application and computation of fractal dimensions in nature | Applications in Nature]]

Fractal dimension provides a quantitative way to describe roughness <a class="yt-timestamp" data-t="00:18:56">[00:18:56]</a>.
*   The coastline of Norway, with a fractal dimension of about 1.52, is numerically communicated as being significantly more jagged than Britain's coastline (1.21) <a class="yt-timestamp" data-t="00:19:03">[00:19:03]</a>.
*   A calm ocean surface might have a fractal dimension barely above 2, while a stormy one could be closer to 2.3 <a class="yt-timestamp" data-t="00:19:12">[00:19:12]</a>.

Fractal dimension is not only prevalent in nature but also appears to be a core differentiator between naturally occurring objects and man-made ones <a class="yt-timestamp" data-t="00:19:21">[00:19:21]</a>.