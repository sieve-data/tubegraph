---
title: TarskiPlanck problem solving
videoId: piJkuavhV50
---

From: [[3blue1brown]] <br/> 

The [[problemsolving_strategies_in_math | Tarski-Planck problem]] is a [[puzzles_and_geometric_problemsolving | geometric puzzle]] that involves covering a unit circle with a collection of strips and determining the minimum possible sum of their widths <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.

## The Problem Defined

Consider a circle with a radius of 1 <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>. A "strip" is defined as any region bounded by two parallel chords within the circle <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>. The key quantity is the width of the strip, denoted as `d`, which is the distance between these two parallel chords <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.

The puzzle asks: If you place enough of these strips to completely cover the area of the circle, what is the minimum possible value for the sum of the widths of all those strips? <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>

### Initial Approaches

A trivial way to cover the circle is to use one "fat" strip with a width of 2, which is the diameter of the circle <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>. This single strip covers the entire circle, so the sum of the widths would be 2 <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>. Similarly, subdividing the circle into many parallel strips also results in a sum of widths equal to the diameter, which is 2 <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>. The core of the question is whether it's possible to achieve a sum less than 2 <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.

Finding a covering that yields a sum much less than 2 is very challenging, leading to the suspicion that 2 might indeed be the minimum possible value <a class="yt-timestamp" data-t="00:06:59">[00:06:59]</a>.

## Solution Strategy: Stepping into Higher Dimensions

This problem is a prime example of how [[approaches_to_mathematical_problem_solving | insights from higher dimensions]] can simplify seemingly complex lower-dimensional problems <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a> <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>.

### The Hemisphere Projection

The crucial insight involves projecting the 2D circle and its strips onto a 3D hemisphere sitting above the circle <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>. While in two dimensions, the area of a strip is not directly proportional to its width (it depends on its position within the circle) <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>, this proportionality *becomes true* when the strips are projected onto the hemisphere <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>.

Specifically, the area of a projected strip on the hemisphere is found to be `pi` times its width (`d`), regardless of its position <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>.

### Connection to Archimedes' Proof

This property is related to Archimedes' famous proof for the surface area of a sphere <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>. Archimedes demonstrated that if a sphere is tightly hugged by a cylinder of the same radius, projecting a patch of area from the sphere outward onto the cylinder preserves its area <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>. This is because stretching along lines of latitude is precisely canceled by squishing along lines of longitude due to the angle <a class="yt-timestamp" data-t="00:08:58">[00:08:58]</a>.

Applying this, if a strip on the sphere is projected onto the cylinder, its area on the cylinder is simply its circumference (`2 * pi * r`) times its thickness (width `d`) <a class="yt-timestamp" data-t="00:09:39">[00:09:39]</a>. For a hemisphere (half the sphere) and a radius of 1, the area of the projected strip becomes `pi * d` <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>.

### Proving the Minimum

1.  **Project:** Any covering of the 2D circle with strips can be projected upwards to become a covering of the hemisphere with projected strips <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>.
2.  **Sum of Areas:** The sum of the areas of these projected strips on the hemisphere is `sum(pi * d)`, which can be factored to `pi * sum(d)` <a class="yt-timestamp" data-t="00:09:58">[00:09:58]</a>.
3.  **Hemisphere Area:** For the strips to cover the hemisphere, their total area must be at least the area of the hemisphere itself <a class="yt-timestamp" data-t="00:10:02">[00:10:02]</a>. A unit sphere has a surface area of `4 * pi * r^2 = 4 * pi` (since radius is 1), so a hemisphere has an area of `2 * pi` <a class="yt-timestamp" data-t="00:10:06">[00:10:06]</a>.
4.  **Inequality:** Therefore, `pi * sum(d) >= 2 * pi` <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>.
5.  **Conclusion:** Dividing by `pi`, it follows that `sum(d) >= 2` <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>.

This proves that the minimum possible value for the sum of the widths is 2, confirming that the simple parallel strip covering is indeed optimal <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>. The problem, while difficult to analyze directly in 2D, becomes elegantly solvable by leveraging intuitions from 3D space <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>.