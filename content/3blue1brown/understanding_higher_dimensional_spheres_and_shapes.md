---
title: Understanding higher dimensional spheres and shapes
videoId: zwAD6dRSVyI
---

From: [[3blue1brown]] <br/> 

Mathematics often uses geometric representations to clarify complex analytical facts, especially in two and three dimensions <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. This approach leverages our visual cortex's ability to process spatial information, creating a valuable back-and-forth between numerical properties and visual concepts <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>. For instance, a circle with radius 1 centered at the origin visually represents all pairs of numbers (x, y) where x² + y² = 1 <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>. This connection is fundamental to various mathematical concepts, such as the relationship between pi and number theory, Pythagorean triples, and topological facts about spheres <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.

However, this intuitive connection diminishes when dealing with higher dimensions, such as quadruplets, quintuplets, or 100-tuples of numbers <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>. Our physical space constrains our geometric intuition, making it challenging to conceptualize points in spaces beyond three dimensions <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.

## The Challenge of [[Geometric reasoning in higher dimensions | Higher Dimensions]]

Problems involving lists of more than three numbers are common in mathematics, computer science, and physics <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>. The standard approach involves using two and three dimensions for [[Analogy between 2D 3D and higher dimensions | analogy]] but primarily relying on analytical reasoning <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>. This is likened to a pilot navigating solely by instruments through clouds <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.

There is a need for methods that bridge the gap between purely geometric and purely analytic views, making analytic reasoning more visual and generalizable to arbitrarily [[Higherdimensional cubes and coloring problems | high dimensions]] <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>. This approach aims to make counterintuitive phenomena in [[Higherdimensional cubes and coloring problems | higher dimensions]] more intuitive <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.

## Defining [[Geometric reasoning and sphere surface area | Higher-Dimensional Spheres]]

The focus in understanding [[Higherdimensional cubes and coloring problems | higher dimensional spheres]] is on their definition. For instance, a [[Higherdimensional cubes and coloring problems | four-dimensional sphere]] with radius one centered at the origin is the set of all quadruplets of numbers (x, y, z, w) where the sum of their squares is one (x² + y² + z² + w² = 1) <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>. Visualizing projections of a 4D sphere into 3D can be confusing and doesn't readily extend to a [[Higherdimensional cubes and coloring problems | five or six or a seven dimensional sphere]] <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.

## The Slider Analogy and "Real Estate"

To better conceptualize [[Higherdimensional cubes and coloring problems | higher dimensional points]], a literal approach involves picturing separate vertical number lines with sliders for each coordinate <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>. Each configuration of these sliders represents a point in N-dimensional space (e.g., a quadruplet for 4D space) <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>. Being on a unit sphere in this space means the sum of the squares of these slider values equals one <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>.

To understand movements on a sphere, an analogy of "real estate" can be used <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>:
*   The value of x² is the "real estate" belonging to x <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.
*   For a unit circle (x² + y² = 1), x and y share one unit of "real estate" <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.
*   Moving on the circle means a constant exchange of this real estate between variables <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.
*   "Real estate" is cheaper near zero and more expensive away from it <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>. For example, moving x from 1 to 0.9 (giving up 0.19 units of real estate) requires y to move 0.44 units from 0 to gain the same amount of cheap real estate <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>. This corresponds to the steep slope of a circle near its axes <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>.
*   In three dimensions, adding a third slider for z means x, y, and z share one unit of real estate <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>. Fixing one slider (e.g., x at 0.5, using 0.25 real estate) leaves the remaining real estate for the others (0.75 for y and z), which corresponds to a circular slice of the sphere <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>.

In [[Higherdimensional cubes and coloring problems | four dimensions and higher]], the fundamental rules of this "real estate" exchange remain, even without a global visual <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>. Fixing one slider in a 4D sphere creates a small 3D sphere as the remaining three variables trade off real estate <a class="yt-timestamp" data-t="00:08:25">[00:08:25]</a>.

## The Counterintuitive Inner Sphere Problem: A [[Threedimensional puzzles and fourdimensional insights | High-Dimensional Puzzle]]

Consider a classic problem: finding the radius of an inner sphere tangent to corner spheres within a hypercube.

### Two Dimensions

Start with a 2x2 box centered at the origin, with corners at (±1, ±1) <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>. Draw four circles, each with radius 1, centered at these four vertices, so they are tangent to their neighbors <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>. The inner circle centered at the origin, tangent to these corner circles, has a radius of √2 - 1 (approximately 0.414) <a class="yt-timestamp" data-t="00:10:02">[00:10:02]</a>. This is derived from the distance from the origin to a corner (√2) minus the radius of a corner circle (1) <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>.

### Three Dimensions

In three dimensions, imagine a [[Tiling in higher dimensions | 2x2x2 cube]] with 8 corner spheres of radius 1 <a class="yt-timestamp" data-t="00:10:17">[00:10:17]</a>. The distance from the origin to a corner (e.g., (1,1,1)) is √1² + 1² + 1² = √3 (approximately 1.73) <a class="yt-timestamp" data-t="00:11:18">[00:11:18]</a>. The radius of the inner sphere tangent to these 8 corner spheres is √3 - 1 (approximately 0.73) <a class="yt-timestamp" data-t="00:11:29">[00:11:29]</a>. This still seems reasonable, with the inner sphere smaller than the corner spheres <a class="yt-timestamp" data-t="00:16:26">[00:16:26]</a>.

### [[Higherdimensional cubes and coloring problems | Four Dimensions]] and Beyond

The surprise occurs as dimensions increase <a class="yt-timestamp" data-t="00:11:48">[00:11:48]</a>.

*   **Four Dimensions**: A 2x2x2x2 hypercube has 16 vertices <a class="yt-timestamp" data-t="00:16:37">[00:16:37]</a>. The distance from the origin to a corner (e.g., (1,1,1,1)) is √1² + 1² + 1² + 1² = √4 = 2 <a class="yt-timestamp" data-t="00:17:58">[00:17:58]</a>. Subtracting the radius of a corner sphere (1) gives an inner sphere radius of 2 - 1 = 1 <a class="yt-timestamp" data-t="00:18:03">[00:18:03]</a>. This means the inner sphere is *precisely the same size* as the corner spheres <a class="yt-timestamp" data-t="00:17:50">[00:17:50]</a>.

    Using the slider analogy, the point on a corner sphere (centered at (1,1,1,1)) closest to the origin is where all four coordinates are equal and "reach exactly halfway between 1 and 0" (i.e., at 0.5) <a class="yt-timestamp" data-t="00:17:04">[00:17:04]</a>. At this point, each coordinate is 0.5 units from 0, contributing 0.5² = 0.25 units of "real estate" with respect to the origin <a class="yt-timestamp" data-t="00:17:34">[00:17:34]</a>. With four such coordinates, the total "real estate" is 4 * 0.25 = 1 <a class="yt-timestamp" data-t="00:17:39">[00:17:39]</a>. This sum of squares (1) confirms the inner sphere's radius is 1. This sphere also touches the faces of the hypercube <a class="yt-timestamp" data-t="00:18:27">[00:18:27]</a>.

*   **Five Dimensions**: A 5D hypercube has 32 corner spheres <a class="yt-timestamp" data-t="00:19:00">[00:19:00]</a>. The distance from the origin to a corner is √5. The inner sphere's radius is √5 - 1 (approximately 1.24) <a class="yt-timestamp" data-t="00:19:50">[00:19:50]</a>. This means the inner sphere is *larger* than the corner spheres and *pokes outside the box* <a class="yt-timestamp" data-t="00:20:12">[00:20:12]</a>.
    In terms of sliders, the point on a corner sphere closest to the origin occurs when all five coordinates equally split the "real estate." This time, each coordinate is slightly *higher* than 0.5 (as 5 * 0.25 = 1.25, which is too much real estate for a unit sphere centered at the corner) <a class="yt-timestamp" data-t="00:19:14">[00:19:14]</a>. When viewed from the origin, this configuration means the sum of squares is greater than 1, implying a radius greater than 1 <a class="yt-timestamp" data-t="00:19:32">[00:19:32]</a>.

*   **Ten Dimensions**: For a 10D hypercube, the inner sphere's radius is √10 - 1 (approximately 2.16) <a class="yt-timestamp" data-t="00:20:58">[00:20:58]</a>. This inner sphere is so large it *pokes outside the outer bounding box* that encompasses all corner spheres, as its diameter (around 4.32) is larger than the outer box's dimension of 4 <a class="yt-timestamp" data-t="00:21:36">[00:21:36]</a>. This happens because the distance to a corner of the box (e.g., (1,...,1)) involves summing the squares of ten 1s, resulting in √10, which is significantly larger than the radius of the corner spheres <a class="yt-timestamp" data-t="00:22:05">[00:22:05]</a>. As dimensions increase, the inner sphere continues to grow without bound, and the proportion of it inside the box decreases exponentially <a class="yt-timestamp" data-t="00:22:24">[00:22:24]</a>.

## Conclusion

The slider analogy and the concept of "real estate" provide a concrete "foothold" for thinking about [[Higherdimensional cubes and coloring problems | high-dimensional shapes]] <a class="yt-timestamp" data-t="00:23:39">[00:23:39]</a>. While it's a coordinate-dependent view and limited to understanding one point and local movements at a time, it helps develop an intuition for counterintuitive phenomena in higher dimensions <a class="yt-timestamp" data-t="00:23:25">[00:23:25]</a>. It allows one to conceptually "play" with a [[Higherdimensional cubes and coloring problems | high-dimensional point]] and appreciate how concepts like the distance to a hypercube's corner behave <a class="yt-timestamp" data-t="00:23:59">[00:23:59]</a>. This method essentially redesigns our "analytic instruments" to better leverage our brain's image processing capabilities, enabling visual thinking even when direct visualization is impossible <a class="yt-timestamp" data-t="00:24:29">[00:24:29]</a>.