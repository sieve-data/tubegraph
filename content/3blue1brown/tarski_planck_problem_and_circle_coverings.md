---
title: Tarski Planck problem and circle coverings
videoId: piJkuavhV50
---

From: [[3blue1brown]] <br/> 

The Tarski-Planck problem is a pure [[Geometry and circles | geometry]] puzzle that asks for the minimum possible sum of widths of strips required to completely cover a unit circle <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>. A "strip" is defined as any region bounded by two parallel chords within the circle, and its width (`d`) is the distance between these two chords <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>.

## Problem Statement

Consider a circle with a radius of 1 <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>. If you have dropped down enough strips such that they completely cover the area of the circle, what is the minimum possible value for the sum of the widths of all those strips? <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>

## Initial Strategies

*   **Single Fat Strip:** A trivial way to cover the circle is to use one strip with a width of 2, equal to the circle's diameter <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>. This strip covers the entire circle, so the sum of widths is 2 <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.
*   **Parallel Subdivisions:** If the circle is subdivided into a series of parallel strips, the sum of their widths will still be the diameter of the circle, which is 2 <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>.

The core question is whether it's possible to achieve a sum of widths less than 2, and by how much <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>. Initially, it seems very difficult to find any strategy that gets even close to 2, let alone lower <a class="yt-timestamp" data-t="00:06:59">[00:06:59]</a>.

## The Higher-Dimensional Insight

The solution to this problem comes from stepping into a higher dimension <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>.

A direct approach is challenging because the area of a strip is not directly proportional to its width; it depends on where the strip sits on the circle (e.g., a strip near the center has a larger area than one near the edge for the same width) <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>.

The key insight is that this proportionality *becomes true* if you project everything up onto a hemisphere sitting above the circle <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>.
Specifically, if `d` is the width of a strip on the two-dimensional circle, the area of that strip when projected onto a three-dimensional hemisphere is `π * d` <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>. Crucially, this area *only* depends on the width `d` and not on the strip's position on the circle (whether it's over the center or closer to the edge) <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>.

### Connection to Archimedes' Proof

This concept is related to [[connection_between_sphere_and_circle_area_formulas | Archimedes' proof]] for the surface area of a sphere <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>. Archimedes' idea involves considering a cylinder that tightly "hugs" a sphere of the same radius <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>. When a small patch of area on the sphere is projected outward onto this cylinder, its area does not change <a class="yt-timestamp" data-t="00:08:51">[00:08:51]</a>. This happens because the stretching effect along lines of latitude is precisely canceled out by the squishing effect along lines of longitude due to the angle of the patch <a class="yt-timestamp" data-t="00:08:58">[00:08:58]</a>.

Applying this to a strip: if a strip on the sphere (or hemisphere) is projected onto the cylinder, its area becomes the circumference of the cylinder (2πr) multiplied by the strip's thickness (or width) <a class="yt-timestamp" data-t="00:09:39">[00:09:39]</a>. For a unit sphere (r=1), this would be 2π times the width. The area of the strip on the hemisphere itself, given its width `d` when projected down to the circle, is πd <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>.

## Proof of the Minimum Sum

1.  Consider any covering of the circle with a set of strips <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>.
2.  Each of these strips can be projected upwards to form a covering of the hemisphere with corresponding projected strips <a class="yt-timestamp" data-t="00:09:53">[00:09:53]</a>.
3.  The sum of the areas of these projected strips on the hemisphere is equal to the sum of `π * d` for each strip, which can be factored as `π * (sum of d)` <a class="yt-timestamp" data-t="00:09:58">[00:09:58]</a>.
4.  Since these projected strips cover the hemisphere, their total area must be at least the area of the hemisphere itself <a class="yt-timestamp" data-t="00:10:02">[00:10:02]</a>.
5.  The surface area of a unit sphere (radius 1) is 4πr², so 4π. A hemisphere's area is half of that, 2π <a class="yt-timestamp" data-t="00:10:06">[00:10:06]</a>.
6.  Therefore, `π * (sum of d)` must be greater than or equal to `2π` <a class="yt-timestamp" data-t="00:10:06">[00:10:06]</a>.
7.  Dividing both sides by π, we find that the `sum of d` can never be below 2 <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>.

Since a sum of 2 is achievable (e.g., with parallel strips), and no sum less than 2 is possible, the minimum possible value for the sum of the widths of the strips is 2 <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>. This problem demonstrates how insights from higher dimensions can simplify the analysis of problems that are initially framed in lower dimensions <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>.