---
title: Highdimensional spheres
videoId: zwAD6dRSVyI
---

From: [[3blue1brown]] <br/> 

Mathematics can be engaging when reasoning geometrically in two and three dimensions, as it allows for a fluid interaction between numerical pairs or triplets and spatial concepts that are easily processed by the visual cortex <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. This connection between sums of squares and circles or spheres is fundamental to many mathematical ideas <a class="yt-timestamp" data-t="01:02:00">[01:02:00]</a>. However, when exploring concepts involving quadruplets, quintuplets, or hundreds of numbers, the ability to visualize things geometrically becomes challenging <a class="yt-timestamp" data-t="01:31:00">[01:31:00]</a>. This limitation stems from the constraints of our physical space and our intuitive understanding of [[Geometry in higher dimensions | higher dimensions]] <a class="yt-timestamp" data-t="01:40:00">[01:40:00]</a>.

## Defining highdimensional spheres

A sphere in [[Geometry in higher dimensions | higher dimensions]] is defined as the set of points where the sum of the squares of its coordinates equals a constant (the radius squared) <a class="yt-timestamp" data-t="04:08:00">[04:08:00]</a>.
For example:
*   A circle with radius 1 centered at the origin represents all pairs of numbers `x` and `y` such that `x² + y² = 1` <a class="yt-timestamp" data-t="00:19:00">[00:19:00]</a>.
*   A unit sphere in three dimensions is the set of all triplets `x, y, z` where `x² + y² + z² = 1` <a class="yt-timestamp" data-t="06:50:00">[06:50:00]</a>.
*   A four-dimensional sphere with radius one centered at the origin is the set of all quadruplets of numbers `x, y, z, w` where `x² + y² + z² + w² = 1` <a class="yt-timestamp" data-t="03:06:00">[03:06:00]</a>.

Visualizing these concepts through projections can be confusing <a class="yt-timestamp" data-t="03:20:00">[03:20:00]</a>. The standard approach for mathematicians and computer scientists when dealing with lists of more than three numbers is to use two and three dimensions for analogy, but to fundamentally reason analytically <a class="yt-timestamp" data-t="02:10:00">[02:10:00]</a>.

## The "Sliders" Metaphor for Visualization

A hybrid method, employing "sliders," helps to make analytical reasoning more visual and generalize to arbitrarily [[Higher dimensions and their relevance | high dimensions]] <a class="yt-timestamp" data-t="02:28:00">[02:28:00]</a>.

### The "Real Estate" Concept
This method involves picturing multiple vertical number lines, each with a slider representing a coordinate <a class="yt-timestamp" data-t="03:55:00">[03:55:00]</a>. Each configuration of these sliders represents a point in N-dimensional space (e.g., a quadruplet of numbers) <a class="yt-timestamp" data-t="04:00:00">[04:00:00]</a>. For a unit sphere, the sum of the squares of these values must be one <a class="yt-timestamp" data-t="04:04:00">[04:04:00]</a>.

The "real estate" metaphor helps understand how values change:
*   The value of `x²` is considered the "real estate" belonging to `x` <a class="yt-timestamp" data-t="04:38:00">[04:38:00]</a>.
*   For a unit sphere, the total shared "real estate" among all coordinates is one <a class="yt-timestamp" data-t="04:46:00">[04:46:00]</a>.
*   Moving along the sphere corresponds to a constant exchange of "real estate" between variables <a class="yt-timestamp" data-t="04:51:00">[04:51:00]</a>.
*   "Real estate" is cheaper near zero and more expensive farther away from zero <a class="yt-timestamp" data-t="05:03:00">[05:03:00]</a>. For example, moving `x` from `1` to `0.9` gives up `0.19` units of real estate, which `y` gains by moving `0.44` units from `0` <a class="yt-timestamp" data-t="05:08:00">[05:08:00]</a>. This highlights the steep slope in the traditional geometric picture <a class="yt-timestamp" data-t="05:52:00">[05:52:00]</a>.

### Slicing highdimensional spheres
Visualizing a sphere using sliders allows for an understanding of its "slices":
*   In three dimensions, holding `x` constant (e.g., at `0.5`) means `y` and `z` trade off the remaining `0.75` units of real estate, akin to a two-dimensional circle formed by slicing a sphere <a class="yt-timestamp" data-t="07:05:00">[07:05:00]</a>.
*   In four dimensions, fixing one slider corresponds to taking a slice of the 4D sphere to get a small 3D sphere <a class="yt-timestamp" data-t="08:25:00">[08:25:00]</a>.

This "bug on the surface" perspective, where one experiences local movements rather than a global view, provides intuition for [[Higher dimensions and their relevance | higher dimensions]] <a class="yt-timestamp" data-t="08:07:00">[08:07:00]</a>.

## Counterintuitive phenomena in highdimensional spheres

A classic problem involves finding the radius of an inner sphere tangent to unit spheres centered at the corners of a hypercube <a class="yt-timestamp" data-t="09:00:00">[09:00:00]</a>.

### Two dimensions
For a 2x2 box centered at the origin, with unit circles at its four corners, the inner circle's radius is found by calculating the distance from the origin to a corner (`sqrt(2)`) and subtracting the corner circle's radius (`1`). The result is `sqrt(2) - 1` (approx. `0.414`) <a class="yt-timestamp" data-t="09:10:00">[09:10:00]</a>.

The point of tangency between an outer circle (e.g., centered at `(1, -1)`) and the inner circle (centered at the origin) occurs when the `x` and `y` coordinates are equal, and the "real estate" (distance from the origin squared) is shared evenly between `x` and `y` <a class="yt-timestamp" data-t="13:20:00">[13:20:00]</a>. Any slight perturbation from this point results in an increasing distance from the origin <a class="yt-timestamp" data-t="14:20:00">[14:20:00]</a>.

### Three dimensions
For a 2x2x2 cube with eight unit spheres at its corners, the inner sphere's radius is `sqrt(3) - 1` (approx. `0.73`) <a class="yt-timestamp" data-t="10:15:00">[10:15:00]</a>. The distance from the origin to a corner (e.g., `(1,1,1)`) is calculated as `sqrt(1² + 1² + 1²) = sqrt(3)` <a class="yt-timestamp" data-t="11:18:00">[11:18:00]</a>.

At the tangent point of a corner sphere (e.g., centered at `(1,1,1)`), the `x, y, z` coordinates are equal and reach down towards `0`, each contributing a third of the unit of real estate. This point is also on the inner sphere <a class="yt-timestamp" data-t="15:22:00">[15:22:00]</a>. The inner sphere is smaller than the corner spheres <a class="yt-timestamp" data-t="16:26:00">[16:26:00]</a>.

### Four dimensions
A 2x2x2x2 hypercube has 16 vertices <a class="yt-timestamp" data-t="16:37:00">[16:37:00]</a>. With 16 unit spheres centered at these corners, each tangent to four neighbors <a class="yt-timestamp" data-t="16:52:00">[16:52:00]</a>, a surprising result emerges:
*   The point on a corner sphere (e.g., centered at `(1,1,1,1)`) closest to the origin is where all four coordinates are `0.5` <a class="yt-timestamp" data-t="17:04:00">[17:04:00]</a>.
*   When viewed from the origin, each of these `0.5` coordinates contributes `0.25` units of "real estate" (`0.5² = 0.25`) <a class="yt-timestamp" data-t="17:34:00">[17:34:00]</a>.
*   The total "real estate" is `0.25 * 4 = 1` <a class="yt-timestamp" data-t="17:39:00">[17:39:00]</a>.
*   This means the inner sphere has a radius of `1`, exactly the same size as the corner spheres <a class="yt-timestamp" data-t="17:50:00">[17:50:00]</a>. Numerically, the distance from the origin to the corner `(1,1,1,1)` is `sqrt(4) = 2`, and `2 - 1 = 1` <a class="yt-timestamp" data-t="17:58:00">[17:58:00]</a>.

This implies that the inner sphere touches the faces of the hypercube <a class="yt-timestamp" data-t="18:27:00">[18:27:00]</a>, a phenomenon specific to [[Exploring fourdimensional geometry and its implications | higher dimensions]] that cannot be crammed into smaller dimensions <a class="yt-timestamp" data-t="18:45:00">[18:45:00]</a>.

### Five dimensions and beyond
In five dimensions, with 32 corner spheres, the point on a corner sphere closest to the origin has all five coordinates slightly greater than `0.5` <a class="yt-timestamp" data-t="19:14:00">[19:14:00]</a>. If they were `0.5`, the total real estate would be `1.25`, which is too much <a class="yt-timestamp" data-t="19:18:00">[19:18:00]</a>. When viewed as a point on the inner sphere relative to the origin, this configuration has more than one unit of real estate <a class="yt-timestamp" data-t="19:27:00">[19:27:00]</a>. The radius of the inner sphere is approximately `1.24` <a class="yt-timestamp" data-t="19:50:00">[19:50:00]</a>. This means the five-dimensional inner sphere actually pokes outside the hypercube <a class="yt-timestamp" data-t="20:12:00">[20:12:00]</a>.

In ten dimensions, the inner sphere's radius is approximately `2.16` <a class="yt-timestamp" data-t="21:04:00">[21:04:00]</a>. This is larger than the outer bounding box for the corner spheres (which has a diameter of 4 in 2D/3D) <a class="yt-timestamp" data-t="21:22:00">[21:22:00]</a>. The face of the hypercube remains two units from the origin regardless of dimension, as it only involves movement along a single axis <a class="yt-timestamp" data-t="21:50:00">[21:50:00]</a>. However, the point `(1,1,1,1,1,1,1,1,1,1)`, which defines the inner sphere's radius, is very far from the center in ten dimensions because all ten dimensions add a full unit of real estate for that point <a class="yt-timestamp" data-t="22:05:00">[22:05:00]</a>. As dimensions increase, the inner sphere grows without bound, and the proportion of the inner sphere inside the box decreases exponentially towards zero <a class="yt-timestamp" data-t="22:22:00">[22:22:00]</a>.

## Benefits of the slider method

The slider method helps conceptualize [[Higher dimensions and their relevance | higher dimensions]] less metaphysically, encouraging exploration of other properties of highdimensional spheres and shapes <a class="yt-timestamp" data-t="22:41:00">[22:41:00]</a>. While it's limited in providing a "bug on the surface" view rather than a global one, and it's coordinate-dependent, it offers a concrete way to think about [[Geometry in higher dimensions | high-dimensional shapes]] <a class="yt-timestamp" data-t="23:25:00">[23:25:00]</a>. This direct representation of analytic descriptions faithfully reflects what doing math in [[Higher dimensions and their relevance | higher dimensions]] entails <a class="yt-timestamp" data-t="24:17:00">[24:17:00]</a>, allowing for visual thinking even when direct visualization is impossible <a class="yt-timestamp" data-t="24:42:00">[24:42:00]</a>.