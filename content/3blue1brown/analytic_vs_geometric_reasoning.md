---
title: Analytic vs geometric reasoning
videoId: zwAD6dRSVyI
---

From: [[3blue1brown]] <br/> 

Mathematics often leverages the visual nature of geometry to understand abstract concepts, but this approach has inherent limitations, particularly when dealing with higher dimensions <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>.

## The Appeal of Geometric Reasoning

There is an inherent beauty in reasoning geometrically in two and three dimensions <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. This method offers a strong [[connection_between_numerical_and_geometric_understandings | back and forth]] between numerical pairs or triplets and spatial understanding, which the human visual cortex is adept at processing <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>.

For instance, visualizing a circle with radius 1 centered at the origin allows for the conceptualization of every pair of numbers (x,y) satisfying the numerical property x² + y² = 1 <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>. Many facts that appear obscure in a purely analytic context become clear geometrically, and vice versa <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. This [[connection_between_numerical_and_geometric_understandings | back and forth]] between sums of squares and circles/spheres is fundamental <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>. Examples include:
*   Connecting Pi to number theory and primes <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.
*   Visualizing all possible Pythagorean triples <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.
*   Using topological facts about spheres to solve counting puzzles, as in the Borsuk-Ulam theorem <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.

The ability to frame analytic facts geometrically is extremely useful for mathematics <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.

## Limitations: The "Tease" of Higher Dimensions

The utility of geometric intuition becomes a "tease" when mathematicians venture into higher dimensions, dealing with quadruplets, quintuplets, or even 100-tuples of numbers <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>. The constraints of our physical space limit our [[spatial_intuition_in_math | intuitions]] about geometry, causing us to lose the valuable [[connection_between_numerical_and_geometric_understandings | back and forth]] between numbers and spatial understanding <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. It is challenging to conceptualize lists of many numbers as individual points in some space <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.

For mathematicians, computer scientists, and physicists, problems involving lists of more than three numbers are common <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>. The standard approach to doing math in higher dimensions is to use two and three dimensions for analogy, but to fundamentally reason analytically <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>. This is analogous to a pilot relying primarily on instruments rather than sight when flying through clouds <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.

## A Hybrid Approach: Visualizing Analytic Reasoning

To bridge the gap between purely geometric and purely analytic views, a hybrid method can be employed to make analytic reasoning more visual, even in arbitrarily high dimensions <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>. This approach aims to make counterintuitive higher-dimensional phenomena more intuitive <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.

The focus is on higher-dimensional spheres. For example, a four-dimensional sphere with radius one centered at the origin is defined as the set of all quadruplets of numbers (x,y,z,w) where the sum of their squares is one (x² + y² + z² + w² = 1) <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>. Direct projections of 4D spheres into 3D can be confusing and don't reflect the true nature of doing math with such objects <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.

### The "Sliders" and "Real Estate" Analogy

A concrete way to think about higher dimensions is to be literal: visualize four separate numbers for 4D space <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>.
*   **Sliders:** Picture multiple vertical number lines, each with a slider representing a coordinate (x, y, z, w, etc.) <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>. Each configuration of these sliders represents a point in N-dimensional space (e.g., a quadruplet of numbers) <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.
*   **Unit Sphere Condition:** For a point to be on a unit sphere centered at the origin, the sum of the squares of these slider values must equal one <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>. Understanding movements on the sphere means understanding which slider movements satisfy this condition <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.
*   **"Real Estate" Analogy:** The term "real estate" is used to describe the value of a coordinate squared (e.g., x² is x's "real estate") <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>. The total "real estate" (sum of squares) must always be one for a unit sphere <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>. Moving around the sphere corresponds to a constant exchange of "real estate" between variables <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.
    *   **Cost of Real Estate:** "Real estate" is "cheap" near zero (a small change in the slider corresponds to a large change in square value) and "expensive" away from zero (a large change in the slider corresponds to a small change in square value) <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>. This leads to a "piston looking dance motion" where sliders move more slowly away from zero <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>.
    *   The square root of the total real estate among all coordinates gives the distance from the origin <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>.

This "bug on the surface" perspective, focusing on local movements and real estate exchange, provides a foothold for thinking about high-dimensional shapes more concretely <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a> <a class="yt-timestamp" data-t="00:23:36">[00:23:36]</a>.

## A Classic Example: The Inner Sphere Radius in N Dimensions

Consider a box of side length 2 centered at the origin (e.g., in 2D, a 2x2 square with corners at (±1, ±1)) <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>. Place unit spheres (radius 1) at each corner <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>. The problem is to find the radius of the sphere centered at the origin that is just large enough to be tangent to these corner spheres <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>.

### 2 Dimensions
*   **Setup:** A 2x2 square with unit circles at its four corners <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>.
*   **Calculation:** The distance from the origin to a corner (e.g., (1,1)) is √(1² + 1²) = √2 ≈ 1.414 <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>. Subtracting the radius of a corner circle (1), the inner circle's radius is √2 - 1 ≈ 0.414 <a class="yt-timestamp" data-t="00:10:02">[00:10:02]</a>. This seems reasonable <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>.
*   **Slider View:** For a corner circle centered at (1,-1), its "real estate" is defined by (x-1)² + (y-(-1))² = 1² <a class="yt-timestamp" data-t="00:12:43">[00:12:43]</a>. The point of tangency with the inner circle occurs when x and y coordinates are the same <a class="yt-timestamp" data-t="00:13:20">[00:13:20]</a>, specifically when the "real estate" is shared evenly <a class="yt-timestamp" data-t="00:13:31">[00:13:31]</a>. At this point, x and y are both less than 0.5, so the total x² + y² (relative to the origin) is less than 0.5² + 0.5² = 0.5 <a class="yt-timestamp" data-t="00:14:55">[00:14:55]</a>.

### 3 Dimensions
*   **Setup:** A 2x2x2 cube with eight unit spheres at its corners <a class="yt-timestamp" data-t="00:15:17">[00:15:17]</a>.
*   **Calculation:** The distance from the origin to a corner (e.g., (1,1,1)) is √(1² + 1² + 1²) = √3 ≈ 1.73 <a class="yt-timestamp" data-t="00:11:48">[00:11:48]</a> <a class="yt-timestamp" data-t="00:11:23">[00:11:23]</a>. Subtracting the radius (1), the inner sphere's radius is √3 - 1 ≈ 0.73 <a class="yt-timestamp" data-t="00:11:29">[00:11:29]</a>. This also seems reasonable <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>.
*   **Slider View:** For a corner sphere at (1,1,1), the point closest to the origin (tangent point) is where x, y, and z are equal <a class="yt-timestamp" data-t="00:15:22">[00:15:22]</a>. They must be slightly beyond 0.5 because 0.5² = 0.25, and with three coordinates, 3 * 0.25 = 0.75, which is not enough for the total unit of real estate shared among the corner sphere's dimensions <a class="yt-timestamp" data-t="00:15:43">[00:15:43]</a>. Relative to the origin, this point has x² + y² + z² less than 0.75, confirming the inner sphere is smaller than the corner spheres <a class="yt-timestamp" data-t="00:16:03">[00:16:03]</a>.

### Higher Dimensions: The Surprising Twist

Something unexpected happens to the inner radius as dimensions increase <a class="yt-timestamp" data-t="00:11:48">[00:11:48]</a>. The ability to use sliders helps to understand this <a class="yt-timestamp" data-t="00:12:04">[00:12:04]</a>.

*   **4 Dimensions:**
    *   **Setup:** A 2x2x2x2 hypercube with 16 unit spheres at its corners <a class="yt-timestamp" data-t="00:16:37">[00:16:37]</a>.
    *   **Calculation:** The distance from the origin to a corner (e.g., (1,1,1,1)) is √(1² + 1² + 1² + 1²) = √4 = 2 <a class="yt-timestamp" data-t="00:17:55">[00:17:55]</a>. Subtracting the radius (1), the inner sphere's radius is 2 - 1 = 1 <a class="yt-timestamp" data-t="00:18:03">[00:18:03]</a>.
    *   **Slider View:** The point on a corner sphere (e.g., centered at (1,1,1,1)) closest to the origin is when all four coordinates are equally splitting the corner sphere's unit of real estate <a class="yt-timestamp" data-t="00:17:04">[00:17:04]</a>. This happens precisely when each coordinate is 0.5 <a class="yt-timestamp" data-t="00:17:09">[00:17:09]</a>. When viewing this as a point on the *inner* sphere relative to the origin (0,0,0,0), each of these four coordinates still has 0.5² = 0.25 units of real estate. The total is 4 * 0.25 = 1 <a class="yt-timestamp" data-t="00:17:34">[00:17:34]</a>.
    *   **Result:** The inner sphere has precisely the same size (radius 1) as the corner spheres <a class="yt-timestamp" data-t="00:17:50">[00:17:50]</a>. This means if all real estate goes to one coordinate, that coordinate can reach 1 (e.g., point (1,0,0,0)), touching the hypercube's face <a class="yt-timestamp" data-t="00:18:20">[00:18:20]</a>. This is a purely four-dimensional phenomenon and cannot be intuitively crammed into smaller dimensions <a class="yt-timestamp" data-t="00:18:45">[00:18:45]</a>.

*   **5 Dimensions:**
    *   **Setup:** A 2x2x2x2x2 hypercube with 32 unit spheres at its corners <a class="yt-timestamp" data-t="00:18:57">[00:18:57]</a>.
    *   **Calculation:** The distance from the origin to a corner (e.g., (1,1,1,1,1)) is √5 ≈ 2.236 <a class="yt-timestamp" data-t="00:19:50">[00:19:50]</a>. The inner sphere's radius is √5 - 1 ≈ 1.24 <a class="yt-timestamp" data-t="00:19:50">[00:19:50]</a>.
    *   **Slider View:** The point on a corner sphere closest to the origin has all five coordinates equally splitting the real estate. Each coordinate will be slightly higher than 0.5 (as 5 * 0.25 = 1.25, too much for 1 unit) <a class="yt-timestamp" data-t="00:19:06">[00:19:06]</a>. When viewed from the origin, this configuration has much more than one unit of real estate <a class="yt-timestamp" data-t="00:19:27">[00:19:27]</a>.
    *   **Result:** The inner sphere is larger than the corner spheres, and its radius (1.24) means it actually "pokes outside" the 2x2x2x2x2 box <a class="yt-timestamp" data-t="00:20:12">[00:20:12]</a> <a class="yt-timestamp" data-t="00:20:05">[00:20:05]</a>.

*   **10 Dimensions:**
    *   **Calculation:** The inner sphere's radius is √10 - 1 ≈ 2.16 <a class="yt-timestamp" data-t="00:20:58">[00:20:58]</a>.
    *   **Slider View:** The point on a corner sphere closest to the origin has all ten coordinates splitting the real estate evenly <a class="yt-timestamp" data-t="00:20:39">[00:20:39]</a>. This appears very far from the origin, indicating a large amount of real estate for the inner sphere <a class="yt-timestamp" data-t="00:20:47">[00:20:47]</a>.
    *   **Result:** The inner sphere is more than twice as large as the corner spheres <a class="yt-timestamp" data-t="00:21:13">[00:21:13]</a>. It even "pokes outside" of a 4x4x...x4 outer bounding box that would enclose all corner spheres <a class="yt-timestamp" data-t="00:21:36">[00:21:36]</a>. As dimensions increase, the inner sphere continues to grow without bound, and the proportion of the inner sphere lying inside the box decreases exponentially towards zero <a class="yt-timestamp" data-t="00:22:22">[00:22:22]</a>. This happens because the face of the box is always 2 units from the origin (moving along one axis), while the corner's distance from the origin is √N (where N is the number of dimensions), which determines the inner sphere's radius <a class="yt-timestamp" data-t="00:21:50">[00:21:50]</a> <a class="yt-timestamp" data-t="00:22:05">[00:22:05]</a>.

## Conclusion

The slider method, while a direct representation of analytic descriptions, re-frames these instruments to better utilize the brain's image processing capabilities <a class="yt-timestamp" data-t="00:24:20">[00:24:20]</a>. It allows for a more concrete and less metaphysical understanding of higher dimensions, enabling mathematicians to inquire about other properties of high-dimensional shapes <a class="yt-timestamp" data-t="00:22:41">[00:22:41]</a>. Just because something cannot be fully visualized, it does not mean it cannot be thought about visually <a class="yt-timestamp" data-t="00:24:42">[00:24:42]</a>.