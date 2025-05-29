---
title: Real estate metaphor in the context of coordinate systems
videoId: zwAD6dRSVyI
---

From: [[3blue1brown]] <br/> 

Mathematics often uses geometric reasoning in two and three dimensions, benefiting from a "nice back and forth" between numbers and spatial concepts that our visual cortex processes well <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. However, this intuitive understanding becomes challenging when dealing with quadruplets, quintuplets, or hundreds of numbers, as our physical space limits our geometric intuition <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>. To bridge this gap, a hybrid approach combining geometric and analytic views can make analytic reasoning more visual in arbitrarily high dimensions <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>. This approach utilizes the "real estate" metaphor for understanding [[Coordinate systems and basis vectors | coordinate systems]] and shapes in higher dimensions.

## The Real Estate Metaphor Explained

The core idea of this metaphor is to assign a "real estate" value to each coordinate. For a given number `x`, its "real estate" is `x²` <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>.
For example, in a 2D [[Coordinate systems and basis vectors | coordinate system]], a circle with radius 1 centered at the origin consists of all points `(x, y)` where `x² + y² = 1` <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>. This means that `x` and `y` share a total of one unit of "real estate" between them <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.

A key insight of this metaphor is that "real estate is cheap near zero and more expensive away from zero" <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>.
*   If `x` moves from 1 to 0.9, `x²` changes from 1 to 0.81, "giving up" 0.19 units of real estate <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>.
*   For `y²` to increase by the same 0.19 units (from 0), `y` must move 0.44 units away from zero, more than four times the amount `x` moved <a class="yt-timestamp" data-t="00:05:33">[00:05:33]</a>. This illustrates that a small change in a coordinate far from zero corresponds to a large change in a coordinate near zero, for the same amount of "real estate" <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>.

The square root of the total real estate among all coordinates represents the distance from the origin <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>.

### Visualizing with Sliders

To make this concept tangible, one can imagine vertical number lines with sliders, where each slider represents a coordinate <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>. Each configuration of these sliders represents a point in a higher-dimensional space <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.
*   **2D Circle:** Movements around a unit circle `x² + y² = 1` correspond to a constant exchange of real estate between `x` and `y` <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>. The sliders exhibit a "piston dance" motion, moving slower away from zero because real estate is "more expensive" there <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>.
*   **3D Sphere:** For a unit sphere `x² + y² + z² = 1`, a third slider for `z` is added, and these three sliders share one unit of real estate <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>. If one coordinate is fixed (e.g., `x` at 0.5, occupying 0.25 units of real estate), the remaining coordinates (`y` and `z`) trade off the remaining 0.75 units <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>. This corresponds to slicing the sphere, where a larger `x` value results in a smaller circular slice for `y` and `z` <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>. This perspective offers a "bug on the surface" feel, where one understands local movements rather than a global view <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>.

### The Problem of the Inner Sphere in Higher Dimensions

The "real estate" metaphor helps explain counterintuitive phenomena in higher dimensions, such as the increasing size of an "inner sphere" within a box.

Consider a 2x2x...x2 box centered at the origin, with corners at `(±1, ±1, ..., ±1)`. Imagine unit spheres (radius 1) centered at each of these corners. The goal is to find the radius of an inner sphere, centered at the origin, that is just large enough to be tangent to these corner spheres <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>.

1.  **Two Dimensions (2D Box):**
    *   The distance from the origin to a corner (e.g., (1,1)) is `sqrt(1² + 1²) = sqrt(2)` (approx. 1.414) <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>.
    *   Subtracting the radius of a corner circle (1), the inner circle's radius is `sqrt(2) - 1` (approx. 0.414) <a class="yt-timestamp" data-t="00:10:02">[00:10:02]</a>. This seems reasonable; the inner circle is smaller than the corner circles <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>.
    *   Using the real estate metaphor, the point of tangency for a corner circle (e.g., centered at (1, -1)) is where `x` and `y` coordinates are equal <a class="yt-timestamp" data-t="00:13:20">[00:13:20]</a>. At this point, real estate is shared evenly between `x` and `y` relative to their respective centers (1 and -1) <a class="yt-timestamp" data-t="00:13:31">[00:13:31]</a>. When measured from the origin (0,0), both `x` and `y` are less than 0.5, meaning `x² + y²` is less than `0.5² + 0.5² = 0.5` <a class="yt-timestamp" data-t="00:14:55">[00:14:55]</a>.

2.  **Three Dimensions (3D Box):**
    *   The distance from the origin to a corner (e.g., (1,1,1)) is `sqrt(1² + 1² + 1²) = sqrt(3)` (approx. 1.73) <a class="yt-timestamp" data-t="00:11:18">[00:11:18]</a>.
    *   Subtracting the corner sphere radius (1), the inner sphere's radius is `sqrt(3) - 1` (approx. 0.73) <a class="yt-timestamp" data-t="00:11:29">[00:11:29]</a>. This also seems reasonable <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>.
    *   For the corner sphere centered at (1,1,1), the point closest to the origin where real estate is shared evenly among `x, y, z` from the corner's perspective means `x, y, z` are all equal and reach down towards 0 <a class="yt-timestamp" data-t="00:15:26">[00:15:26]</a>. When viewed from the origin, this point's coordinates are less than 0.5, so the total real estate `x² + y² + z²` is less than `0.25 + 0.25 + 0.25 = 0.75` <a class="yt-timestamp" data-t="00:16:14">[00:16:14]</a>. The inner sphere is still smaller than the corner spheres <a class="yt-timestamp" data-t="00:16:26">[00:16:26]</a>.

3.  **Four Dimensions (4D Box):**
    *   There are 16 corner spheres centered at `(±1, ±1, ±1, ±1)` <a class="yt-timestamp" data-t="00:16:37">[00:16:37]</a>.
    *   The distance from the origin to a corner (e.g., (1,1,1,1)) is `sqrt(1² + 1² + 1² + 1²) = sqrt(4) = 2` <a class="yt-timestamp" data-t="00:17:55">[00:17:55]</a>.
    *   Subtracting the corner sphere radius (1), the inner sphere's radius is `2 - 1 = 1` <a class="yt-timestamp" data-t="00:18:03">[00:18:03]</a>.
    *   Using the real estate metaphor, the point on a corner sphere (e.g., centered at (1,1,1,1)) closest to the origin is where all four coordinates are equal <a class="yt-timestamp" data-t="00:17:04">[00:17:04]</a>. Each coordinate reaches exactly halfway between 1 and 0, meaning each is 0.5 <a class="yt-timestamp" data-t="00:17:09">[00:17:09]</a>. At this point, each coordinate `(0.5)` has `0.5² = 0.25` units of real estate with respect to the origin. The total real estate for the inner sphere is `0.25 * 4 = 1` <a class="yt-timestamp" data-t="00:17:39">[00:17:39]</a>. This means the inner sphere is *precisely the same size* as the corner spheres <a class="yt-timestamp" data-t="00:17:50">[00:17:50]</a>. This matches the numerical result and is a fundamentally 4D phenomenon <a class="yt-timestamp" data-t="00:18:45">[00:18:45]</a>.

4.  **Five Dimensions (5D Box):**
    *   The distance from the origin to a corner is `sqrt(1² * 5) = sqrt(5)` (approx. 2.24) <a class="yt-timestamp" data-t="00:19:50">[00:19:50]</a>.
    *   The inner sphere's radius is `sqrt(5) - 1` (approx. 1.24) <a class="yt-timestamp" data-t="00:19:50">[00:19:50]</a>. This is *larger* than 1.
    *   The real estate metaphor shows that for the inner sphere to be tangent, all five coordinates are equally splitting the one unit of real estate *from the corner's perspective* <a class="yt-timestamp" data-t="00:19:06">[00:19:06]</a>. However, when viewed from the origin, each coordinate is slightly *higher* than 0.5 <a class="yt-timestamp" data-t="00:19:14">[00:19:14]</a>. The sum of their squares (`x² + y² + z² + w² + v²`) is much greater than 1, meaning the inner sphere actually "pokes outside the box" <a class="yt-timestamp" data-t="00:19:32">[00:19:32]</a>.

5.  **Ten Dimensions (10D Box):**
    *   The distance from the origin to a corner is `sqrt(1² * 10) = sqrt(10)` (approx. 3.16).
    *   The inner sphere's radius is `sqrt(10) - 1` (approx. 2.16) <a class="yt-timestamp" data-t="00:20:58">[00:20:58]</a>.
    *   The point of tangency (where all ten coordinates equally split the real estate) results in each coordinate being far from the origin <a class="yt-timestamp" data-t="00:20:47">[00:20:47]</a>. The sum of their squares is significantly greater than 1, allowing the inner sphere to have a very large amount of real estate <a class="yt-timestamp" data-t="00:20:52">[00:20:52]</a>.
    *   This 10D inner sphere is so large that its diameter (approx. 4.32) is greater than the dimension of the outer bounding box (which is 4) <a class="yt-timestamp" data-t="00:21:36">[00:21:36]</a>. This means it "pokes outside of that outer bounding box" <a class="yt-timestamp" data-t="00:21:41">[00:21:41]</a>. As dimensions increase, this inner sphere continues to grow without bound <a class="yt-timestamp" data-t="00:22:22">[00:22:22]</a>.

### Benefits and Limitations

While this "slider method" with the "real estate" metaphor does not provide a global [[Visual understanding of linear transformations | visual understanding]] of higher-dimensional objects (feeling like a "bug on the surface" <a class="yt-timestamp" data-t="00:25:25">[00:25:25]</a>), it offers a concrete "foothold" for thinking about high-dimensional shapes <a class="yt-timestamp" data-t="00:23:57">[00:23:57]</a>. It is a direct representation of an analytic description <a class="yt-timestamp" data-t="00:24:20">[00:24:20]</a>, allowing mathematicians to probe properties of higher-dimensional spheres and other shapes without skeptically questioning their "reality" <a class="yt-timestamp" data-t="00:22:57">[00:22:57]</a>. It redesigns the "instruments of analytic reasoning" to better leverage human image processing capabilities, enabling visual thinking even when direct visualization is impossible <a class="yt-timestamp" data-t="00:24:29">[00:24:29]</a>.