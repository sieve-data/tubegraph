---
title: Mosers circle problem
videoId: YtkIWDE36qU
---

From: [[3blue1brown]] <br/> 

Moser's circle problem is a famous cautionary tale in mathematics <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. It illustrates the danger of extrapolating patterns from small numbers without rigorous proof <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. The mathematician Richard Guy called this phenomenon "the strong law of small numbers," which states that "there aren't enough small numbers to meet the many demands made of them" <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>.

## The Deceptive Pattern

The problem begins by placing points on the circumference of a [[geometry_and_circles | circle]] and connecting them with chords <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. The goal is to count how many regions the [[geometry_and_circles | circle]] is divided into by these chords <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>.

*   **2 points**: Connecting two points with a chord divides the [[geometry_and_circles | circle]] into 2 regions <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.
*   **3 points**: Adding a third point and connecting it to the previous two with chords divides the [[geometry_and_circles | circle]] into 4 regions <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.
*   **4 points**: A fourth point connected to the previous three results in 8 regions <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.
*   **5 points**: A fifth point connected to the previous four yields 16 regions <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.

This sequence (2, 4, 8, 16) strongly suggests a pattern of powers of two <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. However, adding a sixth point and carefully counting the regions reveals 31, not the expected 32 <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.

### Important Condition
The pattern assumes the "generic case" where no three lines intersect at a single point within the [[geometry_and_circles | circle]] <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>. Placing points symmetrically, for example, can cause lines to coincide and change the number of regions <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.

## Solving the Problem: Finding the Real Pattern

Working out the real pattern is a good exercise in [[problemsolving_strategies_in_mathematical_puzzles | problemsolving strategies in mathematical puzzles]] <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>. The initial powers of two and later reappearance of a power of two (at the tenth iteration) are not coincidences <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.

### Warm-up Questions

To find a function describing the number of regions for `n` points, it helps to solve related, easier questions <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>:

1.  **Total Number of Chords**:
    Every chord corresponds uniquely to a pair of points on the [[geometry_and_circles | circle]] <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>. The number of distinct pairs of points is given by the "n choose two" function, written as `nC2` or `(n 2)` <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.
    *   Formula: `nC2 = n * (n - 1) / 2` <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.
    *   Example: 7 choose 2 is `7 * 6 / 2 = 21` <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>.

2.  **Number of Intersection Points within the Circle**:
    Every intersection point within the [[geometry_and_circles | circle]] is uniquely associated with a quadruplet of points on the [[geometry_and_circles | circle]]'s exterior <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>. The two diagonal chords connecting these four points will intersect <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>. The number of distinct quadruplets is given by the "n choose four" function, `nC4` or `(n 4)` <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>.
    *   Formula: `nC4 = n * (n - 1) * (n - 2) * (n - 3) / (4 * 3 * 2 * 1)` (or `n! / (4! * (n-4)!)`) <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>.
    *   Example: 6 choose 4 is 15 <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>.

### Euler's Characteristic Formula

The key to finding the number of regions is Euler's characteristic formula for planar graphs <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>. For a planar graph (diagram with nodes/vertices and lines/edges that don't intersect), the formula is:
`Vertices (v) - Edges (e) + Faces/Regions (f) = 2` <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.
This formula describes the relationship between vertices, edges, and faces of a graph, and it holds true regardless of how the graph is drawn, as long as it's planar <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.

To apply this to Moser's circle problem, which has intersecting lines, the intersection points themselves are treated as new vertices <a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a>.
*   **Total Vertices (v)**: The initial `n` points on the [[geometry_and_circles | circle]]'s boundary plus the `nC4` intersection points within the [[geometry_and_circles | circle]] <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>.
    `v = n + nC4` <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>.
*   **Total Edges (e)**: Each intersection point effectively takes two initial chords and turns them into four smaller segments, adding two new edges <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a>. So, the original `nC2` chords become `nC2 + 2 * nC4` segments <a class="yt-timestamp" data-t="00:10:17">[00:10:17]</a>. Additionally, the `n` arcs on the outside of the [[geometry_and_circles | circle]] must be counted as edges <a class="yt-timestamp" data-t="00:10:30">[00:10:30]</a>.
    `e = nC2 + 2 * nC4 + n` <a class="yt-timestamp" data-t="00:10:26">[00:10:26]</a>.

Rearranging Euler's formula to find the number of regions (`f`), and excluding the infinite outer region (which means `f - 1` regions within the [[geometry_and_circles | circle]]), the formula for the number of regions is `e - v + 1` <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.

Plugging in the expressions for `e` and `v`:
`f = (nC2 + 2 * nC4 + n) - (n + nC4) + 1` <a class="yt-timestamp" data-t="00:10:48">[00:10:48]</a>
`f = nC2 + 2 * nC4 + n - n - nC4 + 1` <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>
`f = 1 + nC2 + nC4` <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>

This formula precisely gives the number of regions for `n` points <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>.

## Connecting to Pascal's Triangle

The reason for the initial power-of-two pattern and its subsequent break lies in Pascal's triangle <a class="yt-timestamp" data-t="00:11:36">[00:11:36]</a>.

*   **n choose k and Pascal's Triangle**: Each term in Pascal's triangle corresponds to `n choose k` <a class="yt-timestamp" data-t="00:11:50">[00:11:50]</a>. Rows are indexed by `n` (starting from 0) and terms within a row by `k` (starting from 0) <a class="yt-timestamp" data-t="00:12:06">[00:12:06]</a>.
*   **Row Sums**: The sum of the terms in any row of Pascal's triangle is a power of two <a class="yt-timestamp" data-t="00:13:31">[00:13:31]</a>. This is because each number in a row donates two copies of itself to the next row, causing the total sum to double with each iteration <a class="yt-timestamp" data-t="00:13:16">[00:13:16]</a>.

The formula for the number of regions is `1 + nC2 + nC4` <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>. This can be written as `nC0 + nC2 + nC4` because `nC0` (n choose 0) is always 1 <a class="yt-timestamp" data-t="00:13:37">[00:13:37]</a>. This means the formula sums the 0th, 2nd, and 4th terms in the `n`-th row of Pascal's triangle <a class="yt-timestamp" data-t="00:13:41">[00:13:41]</a>.

*   **Why it looks like powers of 2 (n <= 5)**: For `n` values up to 5, adding `nC0 + nC2 + nC4` is equivalent to adding all the elements up to a certain point in the *previous* row of Pascal's triangle, which for these small `n` values, effectively sums the entire previous row, resulting in a power of two <a class="yt-timestamp" data-t="00:13:55">[00:13:55]</a>. For example, for `n=5`, the formula `1 + 5C2 + 5C4 = 1 + 10 + 5 = 16` <a class="yt-timestamp" data-t="00:13:46">[00:13:46]</a>. This is the sum of the 0th, 2nd, and 4th terms of row 5, which corresponds to the sum of the entire 4th row (1+4+6+4+1 = 16).

*   **Why it breaks (n = 6)**: For `n=6`, the formula `1 + 6C2 + 6C4 = 1 + 15 + 15 = 31` <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>.
    In Pascal's triangle, `6C0 + 6C2 + 6C4` sums terms from row 6 <a class="yt-timestamp" data-t="00:14:17">[00:14:17]</a>. When related to row 5 (the previous row), this sum `1+15+15` does not cover all terms of row 5 <a class="yt-timestamp" data-t="00:14:21">[00:14:21]</a>. Specifically, it misses `6C6` (the 6th term of row 6, which is 1) and other even-indexed terms that would complete the sum to `2^5 = 32`. Because it "falls short specifically by just 1," the result is `31` instead of `32` <a class="yt-timestamp" data-t="00:14:27">[00:14:27]</a>.

*   **Reappearance of a Power of Two (n = 10)**: At `n=10`, the sum `10C0 + 10C2 + 10C4` corresponds to adding the first 5 elements of row 9 of Pascal's triangle <a class="yt-timestamp" data-t="00:14:38">[00:14:38]</a>. Due to the symmetry of Pascal's triangle, this sum represents exactly half of the total sum of row 9 (`2^9`), which itself is a power of two (`2^8`) <a class="yt-timestamp" data-t="00:14:42">[00:14:42]</a>.

## Conclusion

Moser's circle problem serves as a powerful reminder to be cautious of patterns without proof <a class="yt-timestamp" data-t="00:15:37">[00:15:37]</a>. However, it also demonstrates that what appears to be a mere coincidence can often lead to a deeper and satisfying mathematical understanding <a class="yt-timestamp" data-t="00:15:41">[00:15:41]</a>. By breaking down the problem into smaller parts and leveraging tools like combinatorics (n choose k) and Euler's formula, the true mathematical structure behind the apparent pattern is revealed and connected to fundamental concepts like Pascal's triangle <a class="yt-timestamp" data-t="00:15:13">[00:15:13]</a>.