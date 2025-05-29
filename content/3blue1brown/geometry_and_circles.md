---
title: Geometry and circles
videoId: WUvTyaaNkzM
---

From: [[3blue1brown]] <br/> 

The study of [[Geometry of ellipses | geometry]] can serve as an intuitive starting point for understanding fundamental calculus concepts <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>. One particular problem, the area of a circle, provides a visual path to grasp ideas like integrals, derivatives, and their inverse relationship <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.

## The Area of a Circle

The well-known formula for the area of a circle is π times its radius squared (πr²) <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>. To understand why this formula holds, one can consider a circle, for example, with a radius of 3 <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>.

### Slicing a Circle into Concentric Rings

A promising approach to finding the area of a circle is to slice it into many concentric rings <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>. This method respects the circle's symmetry, which often simplifies mathematical problems <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.

Consider one such ring with an inner radius `r` (between 0 and the circle's full radius) <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>. If we can find a way to express the area of each individual ring and then sum them up, it could lead to the total area of the circle <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>.

### Approximating Ring Area

A ring can be imagined as being straightened out and approximated as a thin rectangle <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.
*   The width of this approximate rectangle is the circumference of the original ring, which is 2πr <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>. This comes from the definition of [[Pis relationship to circles and geometry | pi]] <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>.
*   The thickness of the rectangle depends on how finely the circle was sliced. In calculus notation, this tiny difference in radius from one ring to the next is denoted as `dr` (e.g., 0.1) <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.

Therefore, the approximate area of an unwrapped ring is `2πr * dr` <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>. This approximation becomes more accurate as `dr` becomes smaller, because the inner and outer circumferences of the ring get closer to being the same length <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>.

### Summing the Rings and the Area Under a Graph

The total area of the circle can be approximated by summing the areas of all these thin rectangular rings, with `r` ranging from 0 up to just under the full radius (e.g., 3) <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>.

This sum can be visualized by arranging all these approximate rectangles upright side by side along an axis representing `r` <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>. Each rectangle has a thickness of `dr`, and its height is `2πr`, representing the circumference of the corresponding ring <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>.

This setup forms a shape that closely resembles the area under the graph of the function `y = 2πr` <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>. The graph of `2πr` is a straight line with a slope of `2π` <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>. As `dr` becomes infinitesimally small, the sum of the rectangular areas becomes an increasingly accurate approximation of the area under this graph <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>.

For a circle with radius `R`, the area under the graph of `2πr` from `r=0` to `r=R` forms a triangle <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>.
*   The base of this triangle is `R` (the radius of the circle) <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>.
*   The height of the triangle is `2πR` (the circumference at the full radius) <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>.

Using the formula for the area of a triangle (1/2 * base * height), the area is:
`1/2 * R * (2πR) = πR²` <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>.

This derivation demonstrates how the formula for the area of a circle naturally emerges from considering the sum of infinitesimally thin concentric rings <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>.

## Connection to Calculus

This process of approximating a problem with a sum of many small quantities (like `2πr * dr`) and then finding the exact answer by considering the limit as these quantities become infinitesimally small, is a core concept in calculus <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>.

*   The summation of these infinitesimally small areas (`2πr * dr`) to find the total area is an example of an **integral** <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a> <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>. Integrals are used to find the area under a graph <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>.
*   The relationship between the area function `a(x)` and the original function `f(x)` (e.g., `x²` or `2πr`) is captured by the **derivative** <a class="yt-timestamp" data-t="00:14:11">[00:14:11]</a>. The derivative `da/dx` (the ratio of a tiny change in area to a tiny change in input `x`) is approximately equal to the height of the graph at that point (`x²` in the example, or `2πr` for the circle) <a class="yt-timestamp" data-t="00:12:34">[00:12:34]</a>.
*   The fact that the derivative of an area function gives back the original function defining the graph illustrates the **Fundamental Theorem of Calculus**, which states that integrals and derivatives are inverse operations <a class="yt-timestamp" data-t="00:15:20">[00:15:20]</a>.

This visual exploration of the area of a circle provides a foundational glimpse into these major calculus ideas <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a> <a class="yt-timestamp" data-t="00:15:44">[00:15:44]</a>.