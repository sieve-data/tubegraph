---
title: The Basel Problem
videoId: d-o3eB9sfls
---

From: [[3blue1brown]] <br/> 

The [[The Basel Problem | Basel Problem]] is a challenge that involves finding the sum of the infinite series of the reciprocals of the square numbers: 1 + 1/4 + 1/9 + 1/16, and so on <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This problem remained [[unsolved_problem_in_physics_and_math | unsolved]] for 90 years after it was initially posed <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>. It was finally [[Eulers Solution to Basel Problem | Euler]] who discovered the answer to be π² / 6 <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>. The problem is named the [[The Basel Problem | Basel Problem]] in honor of [[Eulers Solution to Basel Problem | Euler's]] hometown, Basel <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.

## The Connection to Pi and Circles

The appearance of pi (π) in the solution is surprising, as the initial series seems to have no connection to circles <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. However, pi is fundamentally tied to circles <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>. If pi appears in a mathematical result, there is always a path, however convoluted, in the vast interconnected web of mathematics that leads back to circles and geometry <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>. The proof presented for the [[The Basel Problem | Basel Problem]] leverages this connection, showing a path much shorter than one might initially expect <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.

## A Physical Analogy: Lighthouses

To conceptualize the problem, imagine standing at the origin of a positive number line with lighthouses placed on every positive integer (1, 2, 3, 4, etc.) <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.
The apparent brightness of the first lighthouse is set to 1 <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>. The apparent brightness of subsequent lighthouses is 1/4th, 1/9th, 1/16th, and so on, of the first <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>. This setup provides a physical representation of the [[The Basel Problem | Basel Problem]], where the total brightness received from all lighthouses is the sum of the series <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>. The goal then becomes to show that this total brightness equals π² / 6 times the brightness of the first lighthouse <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>. The key [[problemsolving_strategies_in_math | strategy]] is to find ways to rearrange these lighthouses without changing the total brightness <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.

### Apparent Brightness and the Inverse Square Law

Apparent brightness is determined by how much light hits an observer's screen or retina <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>. This relates to the solid angle covered by the light source <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>. The phenomenon of light spreading out evenly from a point source follows the [[inverse square law]] <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.
*   If you double the distance from a light source, the rays spread out to cover an area with twice the width and twice the height, requiring four copies of the original screen to receive the same light <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>. Thus, each individual screen receives 1/4th as much light <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>.
*   Similarly, at three times the distance, each screen receives 1/9th as much light <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.
This pattern continues because the area hit by light increases by the square of the distance, meaning brightness decreases by the inverse square of that distance <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>. This [[inverse square law]] applies to any quantity spreading evenly from a point source, such as sound, heat, or radio signals <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>. The [[inverse square law]] is precisely why the infinite array of evenly spaced lighthouses physically implements the [[The Basel Problem | Basel Problem]] <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.

## The [[Inverse Pythagorean Theorem]]

A key building block for manipulating light sources without changing total brightness is the [[Inverse Pythagorean Theorem]] <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>.
*   **Statement**: If an observer is at the origin, and a lighthouse is at distance `H`, draw a line from the lighthouse perpendicular to the line connecting it to the observer. If this new line intersects the coordinate axes at points where two new lighthouses (A and B) are placed, at distances `a` and `b` from the observer, then the brightness from the first lighthouse (1/H²) is equal to the combined brightness from lighthouses A and B (1/a² + 1/b²) <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>. This means 1/a² + 1/b² = 1/H² <a class="yt-timestamp" data-t="00:06:12">[00:06:12]</a>.
*   **Proof Intuition**: The theorem can be intuitively understood using the concept of light hitting screens <a class="yt-timestamp" data-t="00:06:59">[00:06:59]</a>. Imagine scaling down the right triangle formed by the observer and the lighthouses <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>. If the miniature hypotenuse is a screen receiving light from the original lighthouse, reshaping that screen to be the combination of the two legs of the miniature triangle still results in the same amount of light received <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a>. The key [[Mathematical Insights and Elegant Solutions | insight]] is that due to similar triangles, the amount of light hitting one leg from the original lighthouse is the same as the amount of light from lighthouse A hitting that leg <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>. Symmetrically, the same applies to the other leg and lighthouse B <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a>. This holds true in the limiting case for a very tiny screen <a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a>.

## Geometric Proof: From Circles to a Line

The [[Inverse Pythagorean Theorem]] allows for transforming a single lighthouse into two, maintaining constant brightness for the observer <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>. This principle can be used to construct the infinite array needed for the [[The Basel Problem | Basel Problem]] <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>.

1.  **Initial Setup**: Imagine an observer at the edge of a circular lake directly opposite a single lighthouse <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>. Let the distance along the lake's border between observer and lighthouse be 1, implying the lake has a circumference of 2 <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>. The apparent brightness is 1 divided by the diameter squared <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>. Since diameter = circumference / π = 2/π, the apparent brightness works out to be π² / 4 <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a>.

2.  **First Transformation**: Draw a new circle twice as large (circumference 4) <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>. Draw a tangent line to the top of the small circle (which is the center of the observer's circle) <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>. Replace the original lighthouse with two new ones where this tangent line intersects the larger circle <a class="yt-timestamp" data-t="00:09:34">[00:09:34]</a>. An important geometry fact is that a triangle formed by a circle's diameter and any point on the circle always has a 90-degree angle at that point <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>. This ensures the [[Inverse Pythagorean Theorem]] applies, so the brightness from the two new lighthouses combined equals the original brightness (π² / 4) <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>.

3.  **Second Transformation**: Draw another circle twice as big (circumference 8) <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>. For each existing lighthouse, draw a line from it through the top of the smaller circle (which is the center of the larger circle) <a class="yt-timestamp" data-t="00:10:13">[00:10:13]</a>. Create two new lighthouses where this line intersects the larger circle <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>. Again, because the connecting line is a diameter of the large circle, the lines from the new lighthouses to the observer form a right angle, allowing the [[Inverse Pythagorean Theorem]] to apply <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>. This process generates four lighthouses that are evenly spaced around the lake <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>.

4.  **Iteration and Limiting Case**: This process continues iteratively <a class="yt-timestamp" data-t="00:11:34">[00:11:34]</a>:
    *   At each step, the circle's size doubles <a class="yt-timestamp" data-t="00:13:30">[00:13:30]</a>.
    *   Each lighthouse is transformed into two new ones along a line drawn through the center of the larger circle <a class="yt-timestamp" data-t="00:13:33">[00:13:33]</a>.
    *   The apparent brightness to the observer remains constant at π² / 4 <a class="yt-timestamp" data-t="00:13:42">[00:13:42]</a>.
    *   The lighthouses remain evenly spaced on the circumference <a class="yt-timestamp" data-t="00:13:47">[00:13:47]</a>.
    *   In the limit, this sequence converges to a flat horizontal line with an infinite number of lighthouses evenly spaced in both directions <a class="yt-timestamp" data-t="00:13:54">[00:13:54]</a>. The apparent brightness in this limiting case is still π² / 4 <a class="yt-timestamp" data-t="00:14:01">[00:14:01]</a>.

This limiting case results in the sum of the inverse squares of *all odd integers* (positive and negative): 1/(±1)² + 1/(±3)² + 1/(±5)² + ... = π² / 4 <a class="yt-timestamp" data-t="00:14:12">[00:14:12]</a>. Summing only the positive odd numbers yields half of this: π² / 8 <a class="yt-timestamp" data-t="00:15:21">[00:15:21]</a>.

## Deriving the Full Basel Problem Solution

The goal is to find the sum of inverse squares of *all positive integers*: 1/1² + 1/2² + 1/3² + 1/4² + ...
We already have the sum for positive odd integers: 1/1² + 1/3² + 1/5² + ... = π² / 8 <a class="yt-timestamp" data-t="00:15:22">[00:15:22]</a>.
The missing terms are the reciprocals of the even numbers: 1/2² + 1/4² + 1/6² + ... <a class="yt-timestamp" data-t="00:15:32">[00:15:32]</a>.
This series of even numbers can be thought of as a scaled copy of the total series we want <a class="yt-timestamp" data-t="00:15:42">[00:15:42]</a>. If every lighthouse's distance from the origin is doubled (1 to 2, 2 to 4, 3 to 6, etc.), the apparent brightness is decreased by a factor of four due to the [[inverse square law]] <a class="yt-timestamp" data-t="00:15:52">[00:15:52]</a>.
Therefore, the sum over even integers is 1/4th of the sum over all positive integers <a class="yt-timestamp" data-t="00:16:04">[00:16:04]</a>.
Since `(sum over all integers) = (sum over odd integers) + (sum over even integers)` <a class="yt-timestamp" data-t="00:16:15">[00:16:15]</a>,
Let `S` be the sum over all positive integers.
Then, `S = (sum over odd integers) + (1/4)S` <a class="yt-timestamp" data-t="00:16:15">[00:16:15]</a>.
This implies `(3/4)S = (sum over odd integers)` <a class="yt-timestamp" data-t="00:16:18">[00:16:18]</a>.
Since `sum over odd integers = π² / 8`, we have `(3/4)S = π² / 8` <a class="yt-timestamp" data-t="00:16:30">[00:16:30]</a>.
Solving for S: `S = (π² / 8) * (4/3) = π² / 6` <a class="yt-timestamp" data-t="00:16:30">[00:16:30]</a>.

This [[Mathematical Insights and Elegant Solutions | elegant solution]] reveals the deep geometric connection behind the [[The Basel Problem | Basel Problem]], where the number line itself can be seen as a limit of ever-growing circles <a class="yt-timestamp" data-t="00:14:46">[00:14:46]</a>.