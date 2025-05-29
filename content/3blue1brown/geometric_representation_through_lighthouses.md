---
title: Geometric representation through lighthouses
videoId: d-o3eB9sfls
---

From: [[3blue1brown]] <br/> 

The Basel problem asks for the sum of the inverses of the next square numbers, starting with 1 + 1/4 + 1/9 + 1/16 and so on, approaching a sum as more terms are added <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This challenge remained unsolved for 90 years until Euler found the answer to be pi squared divided by 6 <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>. The problem is often referred to as the Basel problem in honor of Euler's hometown <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.

## Pi and Geometry

Whenever the mathematical constant pi (π) appears, there is typically some connection to circles <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>. While some argue against insisting on connecting such equations with [[connection_between_numerical_and_geometric_understandings | geometric intuition]] <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>, pi is fundamentally tied to circles <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>. Therefore, if pi appears in a sum, there will be a path within mathematics leading back to circles and [[visualizing_mathematical_concepts | geometry]] <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>. For the Basel problem, this path is surprisingly short <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>.

## The Lighthouse Analogy

The proof for the Basel problem can be visualized using a [[visualizing_mathematical_concepts | geometric representation]] involving light <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.
Imagine standing at the origin of a positive number line with lighthouses placed on every positive integer (1, 2, 3, 4, etc.) <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>.
*   The apparent brightness of the first lighthouse is defined as "one" <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.
*   The second lighthouse appears 1/4 as bright as the first <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.
*   The third appears 1/9 as bright, the fourth 1/16, and so on <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.

This setup provides a physical representation of the Basel problem's sum, where the total brightness received from the infinite line of lighthouses is 1 + 1/4 + 1/9 + 1/16 + ... <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>. The goal is to show that this total brightness equals pi squared divided by 6 times the brightness of the first lighthouse <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>.

The key to progress is to find ways to rearrange these lighthouses without changing the total brightness for the observer, ultimately making the sum easier to compute <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.

### The Inverse Square Law

Apparent brightness refers to the proportion of light rays hitting a screen or the angle the light covers <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.
The inverse square law, a distinctly three-dimensional phenomenon, explains why brightness decreases by the inverse square of the distance <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>. If the distance from a light source doubles, the light rays cover an area with twice the width and twice the height, meaning it takes four copies of the original screen to receive the same light <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>. Thus, each individual screen receives 1/4 as much light <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>. Similarly, at three times the distance, a screen receives 1/9 as much light <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>. This law applies whenever a quantity spreads out evenly from a point source, such as sound, heat, or radio signals <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.

## The Inverse Pythagorean Theorem

A crucial building block for manipulating lighthouse setups without changing total brightness is a transformation where a single lighthouse is replaced by two <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.
*   Consider an observer at the origin of the XY plane and a lighthouse <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>.
*   Draw a line from the lighthouse to the observer <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>.
*   Draw another line perpendicular to the first, passing through the lighthouse <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.
*   Place two new lighthouses where this perpendicular line intersects the coordinate axes (Lighthouse A and Lighthouse B) <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>.

The brightness experienced from the first lighthouse is equal to the combined brightness from Lighthouses A and B <a class="yt-timestamp" data-t="00:05:45">[00:05:45]</a>. This is based on the Inverse Pythagorean theorem <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>: if `h` is the distance to the original lighthouse, and `a` and `b` are the distances to the two new lighthouses, then `1/a^2 + 1/b^2 = 1/h^2` <a class="yt-timestamp" data-t="00:06:12">[00:06:12]</a>.

### Proof Sketch via Light and Screens

The Inverse Pythagorean theorem can be proven using intuitions of light and screens <a class="yt-timestamp" data-t="00:06:59">[00:06:59]</a>:
1.  Imagine scaling down the entire right triangle, with the miniature hypotenuse acting as a screen receiving light from the first lighthouse <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>.
2.  If this screen is reshaped to be the combination of the two legs of the miniature triangle, it still receives the same amount of light <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a>.
3.  The amount of light from the first lighthouse hitting the left leg is exactly the same as the amount of light from lighthouse A hitting that leg <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>.
4.  Symmetrically, the light from the first lighthouse hitting the bottom leg is the same as the light from lighthouse B hitting that portion <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a>.
This relationship arises from similar triangles, which hold true in the limiting case for a very tiny screen <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.

## Iterative Transformations on a Circular Lake

This transformation rule (single lighthouse to two) can be used to build up the infinite array needed for the Basel problem solution <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>.

1.  **Initial Setup:** Imagine an observer at the edge of a circular lake, directly opposite a lighthouse <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>. If the distance along the lake's border between the observer and the lighthouse is one, the lake has a circumference of two <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>. The apparent brightness is 1 divided by the diameter squared <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>. Since the diameter is circumference/pi (2/π), the apparent brightness is π² / 4 <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>.

2.  **First Transformation:** Draw a new circle twice as big (circumference 4) <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>. Draw a tangent line to the top of the small circle <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>. Replace the original lighthouse with two new ones where this tangent line intersects the larger circle <a class="yt-timestamp" data-t="00:09:34">[00:09:34]</a>.
    *   A key [[geometric_interpretation_of_dot_products | geometric fact]] is that if a triangle is formed with the diameter of a circle and any point on the circle, the angle at that point will be 90 degrees <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a>.
    *   This ensures the Inverse Pythagorean theorem applies, meaning the brightness from the two new lighthouses equals the original brightness (π² / 4) <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>.

3.  **Second Transformation:** Draw another circle twice as big (circumference 8) <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>. For each lighthouse, draw a line from it through the top of the smaller circle (which is the center of the larger circle) <a class="yt-timestamp" data-t="00:10:12">[00:10:12]</a>. Consider the two points where this line intersects the larger circle; these become new lighthouses <a class="yt-timestamp" data-t="00:10:23">[00:10:23]</a>.
    *   Since this line is a diameter of the large circle, the lines from the two new points to the observer form a right angle <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>.
    *   The line from the observer to the original lighthouse is at a right angle with the newly drawn long line <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>.
    *   These two facts justify applying the Inverse Pythagorean theorem <a class="yt-timestamp" data-t="00:10:48">[00:10:48]</a>.
    *   Repeating this for all lighthouses results in four lighthouses evenly spaced around the lake <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>.

4.  **Continuing the Process:** This process is repeated: draw a circle twice as big, transforming each lighthouse into two new ones along a line through the center of the larger circle <a class="yt-timestamp" data-t="00:11:35">[00:11:35]</a>.
    *   At each step, the apparent brightness to the observer remains π² / 4 <a class="yt-timestamp" data-t="00:13:39">[00:13:39]</a>.
    *   At each step, the lighthouses remain evenly spaced on the circumference, with a distance of 2 between them <a class="yt-timestamp" data-t="00:13:45">[00:13:45]</a>.
    *   The even spacing is maintained because lines from adjacent lighthouses on the small lake to the center form a 90-degree angle <a class="yt-timestamp" data-t="00:13:31">[00:13:31]</a>. Using the inscribed angle theorem, drawing lines to a point on the circumference yields half that angle (45 degrees) <a class="yt-timestamp" data-t="00:12:48">[00:12:48]</a>. When new lighthouses are positioned using these lines, their lines to the center divide the circle evenly into 45-degree angle pieces <a class="yt-timestamp" data-t="00:13:11">[00:13:11]</a>.

### Reaching the Limit: The Infinite Number Line

In the limit, as this process continues infinitely, the ever-growing circles converge to a flat, horizontal line <a class="yt-timestamp" data-t="00:13:56">[00:13:56]</a>. This line contains an infinite number of lighthouses, evenly spaced in both positive and negative directions <a class="yt-timestamp" data-t="00:13:56">[00:13:56]</a>. Since the apparent brightness was consistently π² / 4 throughout the transformation, it remains so in this limiting case <a class="yt-timestamp" data-t="00:14:01">[00:14:01]</a>.

This yields an infinite series: the sum of the inverse squares `1/n^2` where `n` covers all odd integers (1, 3, 5, ...) and negative odd integers (-1, -3, -5, ...). The sum of these is π² / 4 <a class="yt-timestamp" data-t="00:14:12">[00:14:12]</a>.
This demonstrates a profound [[connection_between_numerical_and_geometric_understandings | connection between numerical sums and geometry]] <a class="yt-timestamp" data-t="00:14:46">[00:14:46]</a>. The number line can be seen as a limit of ever-growing circles, where summing along it is akin to adding along the boundary of an infinitely large circle <a class="yt-timestamp" data-t="00:14:51">[00:14:51]</a>.

## Solving the Basel Problem

The derived sum `∑ (1/n^2)` for all *odd* integers (positive and negative) is π² / 4 <a class="yt-timestamp" data-t="00:14:24">[00:14:24]</a>.

1.  **Positive Odd Integers:** Restricting the sum to only positive odd numbers (1, 3, 5, ...) yields π² / 8 <a class="yt-timestamp" data-t="00:15:22">[00:15:22]</a>.
2.  **Including Even Integers:** The original Basel problem requires summing over *all* positive integers (1, 2, 3, 4, ...). This sum is missing the reciprocals of even numbers (1/4, 1/16, 1/36, ...) <a class="yt-timestamp" data-t="00:15:32">[00:15:32]</a>.
3.  **Relationship between Even and Total Sums:** The sum of the reciprocals of even numbers can be thought of as a scaled copy of the total series <a class="yt-timestamp" data-t="00:15:42">[00:15:42]</a>. If every lighthouse is shifted to be twice as far from the origin (1 to 2, 2 to 4, etc.), the apparent brightness decreases by a factor of four due to the inverse square law <a class="yt-timestamp" data-t="00:15:52">[00:15:52]</a>. Therefore, the sum over even integers is 1/4 times the sum over all integers <a class="yt-timestamp" data-t="00:16:05">[00:16:05]</a>.
4.  **Deriving the Full Sum:**
    *   Let `S_all` be the sum over all positive integers.
    *   Let `S_odd` be the sum over positive odd integers.
    *   Let `S_even` be the sum over positive even integers.
    *   We know `S_all = S_odd + S_even` <a class="yt-timestamp" data-t="00:16:20">[00:16:20]</a>.
    *   We also know `S_even = (1/4) * S_all` <a class="yt-timestamp" data-t="00:16:05">[00:16:05]</a>.
    *   Substituting, `S_all = S_odd + (1/4) * S_all`.
    *   Rearranging, `(3/4) * S_all = S_odd` <a class="yt-timestamp" data-t="00:16:20">[00:16:20]</a>.
    *   Thus, `S_all = (4/3) * S_odd` <a class="yt-timestamp" data-t="00:16:25">[00:16:25]</a>.
    *   Since `S_odd = π² / 8`, then `S_all = (4/3) * (π² / 8) = π² / 6` <a class="yt-timestamp" data-t="00:16:30">[00:16:30]</a>.

This geometrically-inspired approach successfully solves the Basel problem.