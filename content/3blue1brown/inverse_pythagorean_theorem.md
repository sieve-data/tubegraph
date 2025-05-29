---
title: Inverse Pythagorean Theorem
videoId: d-o3eB9sfls
---

From: [[3blue1brown]] <br/> 

The [[Inverse Square Law|Inverse Pythagorean theorem]] describes a relationship between distances in a right-angled triangle, specifically when dealing with light sources and an observer. This theorem, a "cousin" of the traditional [[proof_and_demonstration_of_the_pythagorean_theorem | Pythagorean theorem]], is particularly useful in scenarios where the brightness of a light source decreases by the inverse square of its distance from an observer <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.

## Statement of the Theorem

Imagine an observer at the origin of an XY plane. A single lighthouse is positioned somewhere on this plane <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>. Draw a line from the lighthouse to the observer, and then another line perpendicular to the first one at the lighthouse's position <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>. If two new lighthouses are placed where this perpendicular line intersects the coordinate axes (e.g., lighthouse A on the left axis and lighthouse B on the upper axis), it turns out that the combined brightness from lighthouses A and B equals the brightness from the original lighthouse <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>.

If:
*   `a` is the distance from the observer to lighthouse A
*   `b` is the distance from the observer to lighthouse B
*   `h` is the distance from the observer to the original lighthouse

Then the relationship is given by:
$$ \frac{1}{a^2} + \frac{1}{b^2} = \frac{1}{h^2} $$ <a class="yt-timestamp" data-t="00:06:12">[00:06:12]</a> <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>

## Intuitive Proof Using Light and Screens

While there are straightforward algebraic proofs involving triangle area and the traditional [[proof_and_demonstration_of_the_pythagorean_theorem | Pythagorean theorem]] <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>, a more intuitive method involves "intuitions of light and screens" <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>.

1.  **Scaled Triangle and Screen**: Imagine scaling down the entire right triangle formed by the observer and the lighthouses into a miniature version <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>. Consider the miniature hypotenuse as a "screen" receiving light from the original lighthouse <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a>.
2.  **Reshaping the Screen**: If this screen is reshaped to be the combination of the two legs of the miniature triangle, it will still receive the same total amount of light <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>. The rays of light hitting the legs are precisely the same as those that would hit the hypotenuse <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>.
3.  **Equivalent Light Reception**: The key insight is that the amount of light from the first lighthouse hitting the left leg of the scaled screen is exactly the same as the amount of light coming from lighthouse A (on the left axis) that hits that same leg <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>. Symmetrically, the amount of light from the first lighthouse hitting the bottom leg of the screen is the same as the amount of light hitting that portion from lighthouse B (on the upper axis) <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a>.
4.  **Similar Triangles**: This equivalence is due to similar triangles <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>. This principle holds true in the limiting case for a very tiny screen <a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a>.
5.  **[[Inverse Square Law|Inverse Square Law]]**: This intuitive proof relies on the [[Inverse Square Law|inverse square law]], which states that the apparent brightness of a light source decreases by the inverse square of the distance <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>. This law applies whenever a quantity spreads out evenly from a point source, such as light, sound, or heat <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.

## Application in the Basel Problem

The [[Inverse Square Law|Inverse Pythagorean theorem]] serves as a fundamental "building block" for transforming a single lighthouse into two others without altering the total perceived brightness for an observer <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a> <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>. This transformation is crucial in the geometric approach to solving the Basel problem, which seeks the sum of the inverse squares of all positive integers ($1/1^2 + 1/2^2 + 1/3^2 + \dots$) <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>.

By repeatedly applying this principle in a specific geometric setup involving circles and tangent lines, an initial lighthouse's brightness can be transformed into an infinite array of evenly spaced lighthouses <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>. In the limit, as circles grow infinitely large, this setup approximates an infinite line of lighthouses, physically representing the sum of inverse squares <a class="yt-timestamp" data-t="00:13:56">[00:13:56]</a> <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>. The fact that the total brightness (and thus the sum) remains constant throughout these transformations, eventually yielding a result related to [[geometric_intuition_of_pi | pi]] squared, highlights the deep connections between geometry and seemingly abstract series <a class="yt-timestamp" data-t="00:14:46">[00:14:46]</a>.