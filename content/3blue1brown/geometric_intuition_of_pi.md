---
title: Geometric Intuition of Pi
videoId: d-o3eB9sfls
---

From: [[3blue1brown]] <br/> 

The number pi (π) is famously associated with circles and geometry, even when it appears in contexts that initially seem unrelated, such as an infinite sum of reciprocals of square numbers <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>. While some argue that pi is not fundamentally about circles, its presence in various mathematical formulas often indicates a connection to geometry and circles within the vast interconnected web of mathematics <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. The visual proof for the solution to the Basel Problem offers a compelling demonstration of this connection, [[visual_intuition_in_calculus | illustrating pi's geometric roots]].

## The Basel Problem

The Basel Problem asks for the sum of the series 1 + 1/4 + 1/9 + 1/16 + ... (the sum of the inverses of successive square numbers) as more and more terms are added <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This challenge remained unsolved for 90 years until Leonhard Euler discovered the surprising answer: pi squared divided by 6 (π²/6) <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>. This infinite sum is often referred to as the Basel problem, named in honor of Euler whose hometown was Basel <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.

## A Light-Based Analogy

To provide a [[converting_analytic_reasoning_to_geometric_intuition | geometric intuition]] for the Basel Problem's solution, imagine an observer standing at the origin of a positive number line <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>. A small lighthouse is placed on every positive integer: 1, 2, 3, 4, and so on <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.

The apparent brightness of the first lighthouse (at distance 1) is assigned a value of 1 <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>. The apparent brightness of the second lighthouse (at distance 2) is 1/4 as much as the first, the third (at distance 3) is 1/9 as much, and so on <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>. This setup is useful because the total brightness received from the infinite line of lighthouses becomes 1 + 1/4 + 1/9 + 1/16 + ..., which is precisely the sum asked by the Basel Problem <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>. The goal is to show that this total brightness equals pi squared divided by 6 times the brightness of the first lighthouse <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>.

### The Inverse Square Law

The decreasing brightness with distance is explained by the inverse square law <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>. This law, a distinctly three-dimensional phenomenon, states that the brightness of a light source decreases by the inverse square of the distance from the source <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>. If you double the distance from a light source, the rays will cover an area with twice the width and twice the height, meaning it would take four copies of the original screen to receive the same rays <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>. Thus, each individual screen receives 1/4 as much light <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>. This pattern continues: at three times the distance, a screen receives 1/9 as much light <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>. This law applies to any quantity spreading evenly from a point source, such as sound or heat <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.

## The Inverse Pythagorean Theorem

A key building block for manipulating light setups without changing total brightness for the observer is the Inverse Pythagorean Theorem <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.

Imagine an observer at the origin of the XY plane and a single lighthouse (H) somewhere on that plane <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>. Draw a line from the lighthouse to the observer, and then another line perpendicular to the first, passing through the lighthouse <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>. Now, place two new lighthouses, A and B, where this new perpendicular line intersects the coordinate axes <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>.

The theorem states that the brightness experienced by the observer from the original lighthouse (H) is equal to the combined brightness from lighthouses A and B <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>. If `a` is the distance to A, `b` to B, and `h` to H, the relation is `1/a² + 1/b² = 1/h²` <a class="yt-timestamp" data-t="00:06:12">[00:06:12]</a>.

This theorem can be intuitively understood using the concept of light and screens <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>. If you scale down the right triangle formed by the observer and lighthouses A, B, and H, and imagine the miniature hypotenuse as a screen receiving light from H, reshaping this screen into the two legs of the miniature triangle still receives the same amount of light <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>. The amount of light from H hitting the left leg is exactly the same as the amount of light from lighthouse A hitting that side, and similarly for the right leg and lighthouse B <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>. This relies on the concept of similar triangles and applies in the limiting case of a very tiny screen <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.

## The Circular Transformation

The Inverse Pythagorean Theorem allows a single lighthouse to be transformed into two others without changing the observer's brightness <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>. This is leveraged in a sequence of transformations:

1.  **Initial Setup:** Picture an observer at the edge of a circular lake, directly opposite a single lighthouse <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>. If the distance along the lake's border between the observer and the lighthouse is 1, the lake has a circumference of 2 <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>. The apparent brightness from the lighthouse is `1 / (diameter)²`. Since the circumference is 2, the diameter is `2/π`, so the brightness is `π² / 4` <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.

2.  **First Transformation:** Draw a new circle twice as big (circumference 4) <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>. Draw a tangent line to the top of the small circle (which is the center of the larger circle from the observer's perspective) <a class="yt-timestamp" data-t="00:09:34">[00:09:34]</a>. Replace the original lighthouse with two new ones where this tangent line intersects the larger circle <a class="yt-timestamp" data-t="00:09:34">[00:09:34]</a>. A key [[geometric_reasoning_in_higher_dimensions | geometric fact]] is that a triangle formed with a circle's diameter as one side and any point on the circle as the third vertex will always have a 90-degree angle at that point <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>. This allows the Inverse Pythagorean Theorem to apply, maintaining the brightness at `π² / 4` <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>.

3.  **Second Transformation:** Draw a new circle twice as big again (circumference 8) <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>. For *each* existing lighthouse, draw a line through the top of the smaller circle (the center of the larger circle) <a class="yt-timestamp" data-t="00:10:12">[00:10:12]</a>. Where this line intersects the larger circle, place two new lighthouses <a class="yt-timestamp" data-t="00:10:23">[00:10:23]</a>. Again, due to the right-angle property with the diameter, the Inverse Pythagorean Theorem applies <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>. This process results in four lighthouses evenly spaced around the lake <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>.

4.  **Continuing the Process:** This process continues indefinitely, doubling the size of each circle and transforming each lighthouse into two new ones <a class="yt-timestamp" data-t="00:12:31">[00:12:31]</a>. At every step, the apparent brightness to the observer remains `π² / 4`, and the lighthouses remain evenly spaced with a distance of 2 between them along the circumference <a class="yt-timestamp" data-t="00:13:28">[00:13:28]</a>. The inscribed angle theorem from geometry helps confirm that the new lighthouses divide the circle evenly into smaller angle pieces <a class="yt-timestamp" data-t="00:12:48">[00:12:48]</a>.

## The Limiting Case and Odd Integers Sum

In the limit, as the circles grow infinitely large, the circumference approaches a flat horizontal line <a class="yt-timestamp" data-t="00:13:56">[00:13:56]</a>. The lighthouses become an infinite number of evenly spaced lights along this line, extending in both positive and negative directions <a class="yt-timestamp" data-t="00:13:56">[00:13:56]</a>. Since the apparent brightness remained `π² / 4` throughout the transformations, this will also be the total brightness in this limiting case <a class="yt-timestamp" data-t="00:14:01">[00:14:01]</a>.

This results in an infinite series: the sum of the inverse squares of all odd integers (1, 3, 5, ...) and their negative counterparts (-1, -3, -5, ...). Adding all of these terms gives `π² / 4` <a class="yt-timestamp" data-t="00:14:12">[00:14:12]</a>.
`... + 1/(-5)² + 1/(-3)² + 1/(-1)² + 1/1² + 1/3² + 1/5² + ... = π²/4`
Since the squares of negative numbers are positive, this is equivalent to `2 * (1/1² + 1/3² + 1/5² + ...) = π²/4`.
Therefore, the sum of the positive odd inverse squares is `1/1² + 1/3² + 1/5² + ... = π²/8` <a class="yt-timestamp" data-t="00:15:22">[00:15:22]</a>.

## Connecting to the Basel Problem's Sum

The sum obtained (`π²/8`) is for positive odd integers, while the Basel Problem requires the sum over *all* positive integers (odd and even) <a class="yt-timestamp" data-t="00:15:27">[00:15:27]</a>.

Let `S = 1/1² + 1/2² + 1/3² + 1/4² + ...` (the Basel Problem sum).
The sum over even integers can be written as `1/2² + 1/4² + 1/6² + ...` <a class="yt-timestamp" data-t="00:15:37">[00:15:37]</a>.
This can be factored: `1/2²(1/1² + 1/2² + 1/3² + ...) = 1/4 * S` <a class="yt-timestamp" data-t="00:15:42">[00:15:42]</a>.
So, the sum of even inverse squares is 1/4 of the total sum `S` <a class="yt-timestamp" data-t="00:15:57">[00:15:57]</a>.

Since the total sum `S` is composed of the sum of odd inverse squares plus the sum of even inverse squares:
`S = (1/1² + 1/3² + 1/5² + ...) + (1/2² + 1/4² + 1/6² + ...)` <a class="yt-timestamp" data-t="00:16:15">[00:16:15]</a>
`S = (π²/8) + (1/4 * S)` <a class="yt-timestamp" data-t="00:16:15">[00:16:15]</a>

Solving for `S`:
`S - 1/4 * S = π²/8`
`3/4 * S = π²/8`
`S = (π²/8) * (4/3)`
`S = π²/6` <a class="yt-timestamp" data-t="00:16:25">[00:16:25]</a>

This visual and geometric approach, leveraging the inverse square law and the Inverse Pythagorean Theorem in a series of circular transformations, provides an intuitive and compelling explanation for why pi appears in the solution to the Basel Problem <a class="yt-timestamp" data-t="00:14:46">[00:14:46]</a>. The number line, in this context, can be seen as the limit of ever-growing circles <a class="yt-timestamp" data-t="00:14:51">[00:14:51]</a>.