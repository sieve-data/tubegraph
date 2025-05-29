---
title: Mosers circle problem
videoId: YtkIWDE36qU
---

From: [[3blue1brown]] <br/> 

Moser's circle problem is a famous cautionary tale in mathematics that demonstrates how initial patterns can be deceptive <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. It begins by placing points on a circle and connecting them with chords, then counting the number of regions these chords divide the circle into <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>.

## The Deceptive Pattern

When starting with a circle and adding points:
*   **Two points** connected by a chord divide the circle into two regions <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.
*   **Three points** connected by chords divide the circle into four regions <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.
*   **Four points** connected by chords result in eight regions <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.
*   **Five points** connected by chords yield sixteen regions <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.

This progression (2, 4, 8, 16) strongly suggests a pattern of powers of two (2^n-1 or 2^n depending on how n is defined) <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. However, when a **sixth point** is added and connected, the number of regions is not 32 (the expected power of two), but 31 <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.

This problem assumes a "generic case" where no three lines intersect at a single point <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>. The problem is considered a "tease" because it looks convincingly like powers of two until it just barely breaks <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.

## The Strong Law of Small Numbers

This phenomenon is an example of what mathematician Richard Guy called "the strong law of small numbers" <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. This law suggests that "there aren't enough small numbers to meet the many demands made of them" <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. Despite this, the initial pattern being powers of two and other occurrences of powers of two later on (like at the tenth iteration) are not mere coincidences <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.

## Solving the Problem: A Path to Understanding

To understand the true pattern, it's helpful to break down the problem into easier, related questions <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>. This is a common strategy in [[problemsolving_strategies_in_math | problem solving]] <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.

### Warm-up Questions

1.  **How many total chords are there?**
    *   Each chord connects a unique pair of points on the circle <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.
    *   This is a combination problem: "n choose 2" (or "n C 2"), which counts the number of distinct pairs that can be chosen from a set of 'n' items where order doesn't matter <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.
    *   The formula is n * (n-1) / 2 <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.
    *   For example, with 7 points, there are 7 * 6 / 2 = 21 chords <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>.

2.  **How many intersection points are there within the circle?**
    *   Every intersection point is uniquely associated with a quadruplet (set of four) points on the circle's exterior <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>. For any four points on the circle, the two diagonal chords connecting them will intersect inside the circle <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>.
    *   This is also a combination problem: "n choose 4" (or "n C 4") <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>.
    *   The formula is n * (n-1) * (n-2) * (n-3) / (4 * 3 * 2 * 1) or n! / (4! * (n-4)!) <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
    *   For example, with 4 points, there is 1 intersection point (4 choose 4 = 1) <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>. With 6 points, there are 15 intersection points (6 choose 4 = 15) <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>.

### Euler's Characteristic Formula for Planar Graphs

The key to solving Moser's circle problem is applying Euler's characteristic formula, which states that for any planar graph (a graph that can be drawn without edges intersecting), the number of vertices (V) minus the number of edges (E) plus the number of faces/regions (F) always equals two (V - E + F = 2) <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>. This formula originally described the vertices, edges, and faces of 3D polyhedra <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.

This formula can be rearranged to find the number of regions: F = E - V + 2 <a class="yt-timestamp" data-t="00:08:51">[00:08:51]</a>. If only counting the regions *inside* the circle (excluding the infinite outer region), the formula becomes F = E - V + 1 <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.

Although the chords in Moser's problem intersect, the diagram can be treated as a new planar graph by considering each intersection point as a new vertex <a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a>.

*   **Total Vertices (V)**: The original 'n' points on the circle plus the 'n choose 4' intersection points <a class="yt-timestamp" data-t="00:09:28">[00:09:28]</a>. So, V = n + (n choose 4) <a class="yt-timestamp" data-t="00:10:48">[00:10:48]</a>.
*   **Total Edges (E)**: Each intersection point essentially takes two original lines and turns them into four smaller lines, adding two new edges <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a>. So, the original 'n choose 2' chords are now broken into 'n choose 2 + 2 * (n choose 4)' smaller segments <a class="yt-timestamp" data-t="00:10:17">[00:10:17]</a>. Additionally, the 'n' arcs on the outside of the circle must be counted as edges <a class="yt-timestamp" data-t="00:10:30">[00:10:30]</a>.
    *   Therefore, E = (n choose 2) + 2 * (n choose 4) + n <a class="yt-timestamp" data-t="00:10:52">[00:10:52]</a>.

Plugging these into the modified Euler's formula (F = E - V + 1):
F = [(n choose 2) + 2 * (n choose 4) + n] - [n + (n choose 4)] + 1 <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>
F = (n choose 2) + 2 * (n choose 4) + n - n - (n choose 4) + 1
F = 1 + (n choose 2) + (n choose 4) <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>

This formula precisely describes the number of regions for 'n' points.

## Connecting to Pascal's Triangle

The derived formula, 1 + (n choose 2) + (n choose 4), can be understood by examining Pascal's Triangle <a class="yt-timestamp" data-t="00:11:36">[00:11:36]</a>.

*   **Pascal's Triangle Structure**: Each term in Pascal's triangle represents "n choose k" <a class="yt-timestamp" data-t="00:11:50">[00:11:50]</a>. For example, the 3rd element (k=3, zero-indexed) in the 5th row (n=5, zero-indexed) is 10, which is 5 choose 3 <a class="yt-timestamp" data-t="00:12:10">[00:12:10]</a>.
*   **Sums of Rows**: When summing the numbers in each row of Pascal's triangle, the result is always a power of two <a class="yt-timestamp" data-t="00:13:31">[00:13:31]</a>. This is because each number in a row donates two copies of itself to the next row, effectively doubling the sum <a class="yt-timestamp" data-t="00:13:08">[00:13:08]</a>.

The formula for Moser's circle problem (1 + n choose 2 + n choose 4) can be written as (n choose 0) + (n choose 2) + (n choose 4), since (n choose 0) is always 1 <a class="yt-timestamp" data-t="00:13:37">[00:13:37]</a>. This means the number of regions is the sum of the 0th, 2nd, and 4th terms in the 'n' row of Pascal's triangle <a class="yt-timestamp" data-t="00:13:37">[00:13:37]</a>.

For n values up to 5, summing these terms actually corresponds to summing *all* the terms in the (n-1)th row of Pascal's triangle <a class="yt-timestamp" data-t="00:14:05">[00:14:05]</a>. Since the sum of any full row of Pascal's triangle is a power of two, the results for n=1 through n=5 are powers of two <a class="yt-timestamp" data-t="00:14:05">[00:14:05]</a>.

The pattern breaks at n = 6 because (6 choose 0) + (6 choose 2) + (6 choose 4) does not include all the terms in the 5th row (it misses 6 choose 6, which is 1) <a class="yt-timestamp" data-t="00:14:17">[00:14:17]</a>. This is why the result is exactly one less than the expected power of two (31 instead of 32) <a class="yt-timestamp" data-t="00:14:27">[00:14:27]</a>.

Interestingly, when n = 10, the sum of (10 choose 0) + (10 choose 2) + (10 choose 4) is exactly half the sum of the 9th row of Pascal's Triangle (due to the triangle's symmetry), which results in another power of two <a class="yt-timestamp" data-t="00:14:38">[00:14:38]</a>. Determining if this is the last time a power of two appears as a result is an open challenge <a class="yt-timestamp" data-t="00:14:56">[00:14:56]</a>.

In summary, Moser's circle problem serves as a cautionary tale against assuming patterns without proof <a class="yt-timestamp" data-t="00:15:37">[00:15:37]</a>. However, it also demonstrates that even apparent coincidences can lead to satisfying mathematical understandings through methods like combinatorial counting and [[geometric_reasoning_and_sphere_surface_area | Euler's formula]] <a class="yt-timestamp" data-t="00:15:41">[00:15:41]</a>.