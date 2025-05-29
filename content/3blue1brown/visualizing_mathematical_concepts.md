---
title: Visualizing mathematical concepts
videoId: zwAD6dRSVyI
---

From: [[3blue1brown]] <br/> 

Mathematics often seduces us with the beauty of geometric reasoning in two and three dimensions, where there is a strong connection between numbers (pairs or triplets) and spatial concepts that our visual cortex is adept at processing <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. This connection makes many facts that appear opaque in a purely analytic context quite clear geometrically, and vice versa <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. For example, a circle with radius 1 centered at the origin can be conceptualized as every pair of numbers x and y satisfying x² + y² = 1 <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>. This ability to frame analytic facts geometrically is highly useful for math <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.

## Challenges of Higher Dimensions

However, this visual approach becomes challenging when dealing with quadruplets, quintuplets, or even 100-tuples of numbers <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>. Our intuitions about geometry are constrained by physical space, causing us to lose this beneficial back-and-forth between numbers and spatial reasoning <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. Problems involving lists of more than three numbers are a regular part of the job for mathematicians, computer scientists, and physicists <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.

The standard approach to doing math in higher dimensions is to use two and three dimensions for analogy, but fundamentally reason about things analytically <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>. This is analogous to a pilot relying primarily on instruments rather than sight when flying through clouds <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.

## The "Slider Method" for [[visual_approach_to_math_concepts | Visualizing Mathematical Concepts]] in Higher Dimensions

A hybrid approach combines geometric and analytic views, making analytic reasoning more visual in a way that generalizes to arbitrarily high dimensions <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>. This method helps to make counterintuitive higher-dimensional phenomena more intuitive <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.

### Conceptualizing Points as Sliders

The core idea is to represent each number in a tuple as a vertical number line with a slider <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>. Each configuration of these sliders represents a point in an n-dimensional space (e.g., a quadruplet of numbers for 4D space) <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.

### The "Real Estate" Analogy

To understand movement and relationships between coordinates, the concept of "real estate" is introduced <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>.
*   The value of x-squared (or y-squared, etc.) is considered the "real estate" belonging to that variable <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>.
*   For a unit sphere (radius 1), variables share a total of one unit of real estate <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.
*   Moving around on a sphere corresponds to a constant exchange of real estate between the variables <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.
*   "Real estate" is "cheap" near zero and "more expensive" away from it <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>. This means a small change in a variable far from zero results in a large change in its squared value (expensive real estate), while a large change in a variable near zero results in a small change in its squared value (cheap real estate) <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>. This concept aligns with the fact that real estate comes in units of distance squared <a class="yt-timestamp" data-t="00:06:35">[00:06:35]</a>.

### Visualizing Higher-Dimensional Spheres

For a 4-dimensional sphere with radius one centered at the origin, it is the set of all quadruplets (x,y,z,w) where x² + y² + z² + w² = 1 <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>. Using sliders, this means the sum of the squares of the four slider values is one <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>. Understanding which slider movements correspond to movements on the sphere is the goal <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>. Fixing one slider in place (e.g., x at 0.5) for a 3D sphere means the remaining sliders (y and z) trade off the remaining real estate, forming a circular slice <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>. This concept extends to higher dimensions: fixing one slider in a 4D sphere yields a 3D spherical slice <a class="yt-timestamp" data-t="00:08:25">[00:08:25]</a>.

## A Counter-Intuitive Phenomenon: The Inner Sphere Problem

A classic example of a phenomenon that seems reasonable in two and three dimensions but becomes counter-intuitive in higher dimensions is the radius of an inner sphere tangent to corner spheres of a hypercube <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.

### Two Dimensions (2D)

Consider a 2x2 box centered at the origin with corners at (±1, ±1). Four circles, each with radius 1, are centered at these four vertices, tangent to their neighbors <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>. The distance from the origin to a corner (e.g., (1,1)) is √2 ≈ 1.414 <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>. The radius of the inner circle, centered at the origin and tangent to these corner circles, is √2 - 1 ≈ 0.414 <a class="yt-timestamp" data-t="00:10:02">[00:10:02]</a>. The inner circle is smaller than the corner circles.

Using the slider method, for a corner circle centered at (1,-1), the real estate of x is its squared distance from 1, and y's real estate is its squared distance from -1 <a class="yt-timestamp" data-t="00:12:43">[00:12:43]</a>. The point of tangency between the inner circle and a corner circle occurs when the x and y coordinates are the same <a class="yt-timestamp" data-t="00:13:20">[00:13:20]</a>. At this point, real estate is shared evenly between x and y relative to the corner's center <a class="yt-timestamp" data-t="00:13:31">[00:13:31]</a>. From the origin's perspective, the total real estate (x² + y²) for this tangent point is less than 0.5² + 0.5² (i.e., less than 0.5) <a class="yt-timestamp" data-t="00:14:55">[00:14:55]</a>.

### Three Dimensions (3D)

Similarly, for a 2x2x2 cube, eight spheres of radius 1 are centered at its vertices <a class="yt-timestamp" data-t="00:15:17">[00:15:17]</a>. The distance from the origin to a corner (e.g., (1,1,1)) is √3 ≈ 1.73 <a class="yt-timestamp" data-t="00:11:18">[00:11:18]</a>. The radius of the inner sphere, tangent to these corner spheres, is √3 - 1 ≈ 0.73 <a class="yt-timestamp" data-t="00:11:29">[00:11:29]</a>. The inner sphere is still smaller than the corner spheres <a class="yt-timestamp" data-t="00:16:26">[00:16:26]</a>.

The tangent point on a corner sphere (e.g., centered at (1,1,1)) closest to the origin corresponds to a configuration where x, y, and z are equal and close to 0 <a class="yt-timestamp" data-t="00:15:22">[00:15:22]</a>. For the inner sphere, the total real estate (x² + y² + z²) at this tangent point is less than 0.75, as each coordinate is less than 0.5 <a class="yt-timestamp" data-t="00:16:14">[00:16:14]</a>.

### Four Dimensions (4D)

In four dimensions, a 2x2x2x2 hypercube has 16 vertices <a class="yt-timestamp" data-t="00:16:37">[00:16:37]</a>. The distance from the origin to a corner (e.g., (1,1,1,1)) is √4 = 2 <a class="yt-timestamp" data-t="00:17:55">[00:17:55]</a>. The radius of the inner sphere, tangent to these corner spheres, is 2 - 1 = 1 <a class="yt-timestamp" data-t="00:18:03">[00:18:03]</a>. This means the inner sphere is *precisely the same size* as the corner spheres <a class="yt-timestamp" data-t="00:17:50">[00:17:50]</a>.

Using sliders, the point on a corner sphere (e.g., centered at (1,1,1,1)) closest to the origin is where all four coordinates are exactly halfway between 1 and 0, i.e., at 0.5 <a class="yt-timestamp" data-t="00:17:04">[00:17:04]</a>. At this point, each coordinate has 0.25 units of real estate (0.5² = 0.25) <a class="yt-timestamp" data-t="00:17:15">[00:17:15]</a>. With four such coordinates, the total real estate with respect to the origin is 4 * 0.25 = 1 <a class="yt-timestamp" data-t="00:17:34">[00:17:34]</a>. This explains why the inner sphere has a radius of 1 <a class="yt-timestamp" data-t="00:17:50">[00:17:50]</a>. An interesting consequence is that this inner sphere touches the 2x2x2x2 box <a class="yt-timestamp" data-t="00:18:27">[00:18:27]</a>.

### Beyond Four Dimensions (5D and 10D)

As dimensions increase further, the inner sphere becomes even larger:
*   **Five Dimensions (5D):** There are 32 corner spheres <a class="yt-timestamp" data-t="00:18:57">[00:18:57]</a>. The radius of the inner sphere is √5 - 1 ≈ 1.24 <a class="yt-timestamp" data-t="00:19:50">[00:19:50]</a>. This means the inner sphere *pokes outside* the 2x2x2x2x2 box <a class="yt-timestamp" data-t="00:20:12">[00:20:12]</a>. In terms of sliders, the tangent point where all five coordinates split real estate evenly (relative to the corner sphere) means each coordinate is a little higher than 0.5 when measured from the origin, resulting in a sum of squares greater than 1 <a class="yt-timestamp" data-t="00:19:14">[00:19:14]</a>.
*   **Ten Dimensions (10D):** The radius of the inner sphere is √10 - 1 ≈ 2.16 <a class="yt-timestamp" data-t="00:20:58">[00:20:58]</a>. This sphere is large enough to poke outside even an *outer* bounding box of size 4x4x...x4 <a class="yt-timestamp" data-t="00:21:36">[00:21:36]</a>. From the slider perspective, the point where all ten coordinates evenly split the real estate (relative to the corner sphere) means each coordinate is still far from the origin, leading to a very large total real estate from the origin's perspective <a class="yt-timestamp" data-t="00:20:47">[00:20:47]</a>. The proportion of the inner sphere inside the box decreases exponentially towards zero as the dimension increases <a class="yt-timestamp" data-t="00:22:27">[00:22:27]</a>.

## The Value of the Slider Method

This [[visual_approach_to_math_concepts | visual approach to math concepts]], particularly the slider method, makes discussions about higher dimensions less abstract and more concrete <a class="yt-timestamp" data-t="00:22:41">[00:22:41]</a>. It helps people understand what high-dimensional properties feel like in terms of sliders and encourages exploration of other shapes <a class="yt-timestamp" data-t="00:23:04">[00:23:04]</a>. While it's limited to understanding one point and local movements, and is coordinate-dependent, it provides a crucial foothold for thinking about high-dimensional shapes <a class="yt-timestamp" data-t="00:23:25">[00:23:25]</a>.

Even though representing each coordinate literally with a slider might seem purely analytic, this small step enables a more intuitive "play" with the thought of a high-dimensional point <a class="yt-timestamp" data-t="00:23:46">[00:23:46]</a>. Concepts like "real estate" shed light on seemingly strange aspects of high dimensions, such as the distance of a box corner from its center <a class="yt-timestamp" data-t="00:24:03">[00:24:03]</a>. This method essentially redesigns the "instruments" of analytic reasoning to better leverage our brain's image processing capabilities <a class="yt-timestamp" data-t="00:24:29">[00:24:29]</a>, demonstrating that one can think visually about something even if direct visualization is impossible <a class="yt-timestamp" data-t="00:24:42">[00:24:42]</a>.