---
title: Patterns and powers of two in mathematics
videoId: YtkIWDE36qU
---

From: [[3blue1brown]] <br/> 

Moser's Circle Problem is a famous cautionary tale in mathematics that illustrates how patterns can appear convincingly before breaking down <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. It's a prime example of what mathematician Richard Guy called the "strong law of small numbers," which states that "there aren't enough small numbers to meet the many demands made of them" <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>.

## The Problem Defined

The problem begins by placing points on the circumference of a circle and connecting them with chords <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. The objective is to count the number of regions these chords divide the circle into <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>. For the purpose of this problem, it's assumed that no three lines intersect at the same point within the circle <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.

### Initial Observations and the Apparent Pattern

*   **2 points:** Connecting two points with a chord divides the circle into 2 regions <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.
*   **3 points:** Connecting three points with chords divides the circle into 4 regions <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.
*   **4 points:** Connecting four points with chords divides the circle into 8 regions <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.
*   **5 points:** Connecting five points with chords divides the circle into 16 regions <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.

These initial results strongly suggest a pattern of powers of two (2^n-1), where `n` is the number of points <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.

### The Pattern Breaks

*   **6 points:** Adding a sixth point and connecting it to all previous ones results in 31 regions, not the expected 32 (2^5) <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>. This slight deviation makes the problem a "tease" <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.

> [!NOTE]
> The placement of points on the circle *does* matter. This problem specifically considers the "generic case" where no three lines intersect at a single point inside the circle, avoiding symmetrical arrangements that might reduce the number of regions <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.

## Solving the Problem: Finding the Real Pattern

To uncover the true pattern, it's helpful to break down the problem into simpler, related questions <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.

### 1. Total Number of Chords

Every chord corresponds uniquely to a pair of points on the circle <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>. To count the number of chords, one needs to count how many distinct pairs of points there are from `n` points <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>. This is given by the combination function [[mathematical_notation_and_conventions | n choose two]] (`nC2`), which is calculated as `n * (n - 1) / 2` <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.

*   **Example:** For 7 points, the number of chords is 7 * 6 / 2 = 21 <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>.

### 2. Number of Intersection Points

Every intersection point within the circle is uniquely associated with a quadruplet of points on the circle's circumference <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>. For any four points on the circle, their two diagonal chords will intersect inside the circle <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>. Thus, counting intersection points is equivalent to counting the number of distinct ways to choose four items from a set of `n` items, where order doesn't matter <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>. This is given by [[mathematical_notation_and_conventions | n choose four]] (`nC4`) <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.

*   [[mathematical_notation_and_conventions | n choose four]] is calculated as `n * (n - 1) * (n - 2) * (n - 3) / (4 * 3 * 2 * 1)`, or `n * (n - 1) * (n - 2) * (n - 3) / 4!` <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>.
*   **Example:** For 4 points, [[mathematical_notation_and_conventions | 4 choose four]] is 1, indicating one intersection point <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>. For 6 points, [[mathematical_notation_and_conventions | 6 choose four]] is 15 <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>.

### Applying Euler's Characteristic Formula

The key to solving the problem is Euler's characteristic formula for planar graphs <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>. For any planar graph, the relationship between vertices (V), edges (E), and faces/regions (F) is given by `V - E + F = 2` <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>.

*   In this context, the regions are the divisions of the plane, including the infinite outer region <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>.
*   Rearranging to find the number of regions (F): `F = E - V + 2` <a class="yt-timestamp" data-t="00:08:51">[00:08:51]</a>.
*   Since we are interested in the regions *inside* the circle, we adjust the formula to `Regions = E - V + 1` (subtracting the outer infinite region) <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.

To apply this to Moser's Circle Problem, the intersection points themselves must be treated as new vertices <a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a>.

*   **Total Vertices (V):** The initial `n` points on the circle + the `n choose four` intersection points <a class="yt-timestamp" data-t="00:09:28">[00:09:28]</a>. So, `V = n + (n choose 4)`.
*   **Total Edges (E):** Each intersection point takes two lines and turns them into four, effectively adding two new edges <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a>.
    *   The initial `n choose two` chords <a class="yt-timestamp" data-t="00:10:17">[00:10:17]</a>.
    *   Plus `2 * (n choose four)` edges created by intersections <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>.
    *   Plus the `n` arcs on the outside of the circle <a class="yt-timestamp" data-t="00:10:30">[00:10:30]</a>.
    *   So, `E = (n choose 2) + 2 * (n choose 4) + n`.

Plugging these into the adjusted Euler's formula (`Regions = E - V + 1`):
`Regions = [(n choose 2) + 2 * (n choose 4) + n] - [n + (n choose 4)] + 1` <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>
Simplifying the expression:
`Regions = (n choose 2) + 2 * (n choose 4) + n - n - (n choose 4) + 1`
`Regions = 1 + (n choose 2) + (n choose 4)` <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>

This formula precisely describes the number of regions for any `n` points <a class="yt-timestamp" data-t="00:11:16">[00:11:16]</a>.

## The Connection to Pascal's Triangle

The true pattern and the reason for the initial appearance of powers of two lies in [[mathematical_notation_and_conventions | Pascal's triangle]] <a class="yt-timestamp" data-t="00:11:36">[00:11:36]</a>.

*   Each term in [[mathematical_notation_and_conventions | Pascal's triangle]] represents [[mathematical_notation_and_conventions | n choose k]] <a class="yt-timestamp" data-t="00:11:50">[00:11:50]</a>. The `n` represents the row number (starting from 0) and `k` represents the element position in that row (starting from 0) <a class="yt-timestamp" data-t="00:12:06">[00:12:06]</a>.
*   The sum of all terms in any given row of [[mathematical_notation_and_conventions | Pascal's triangle]] is always a power of two <a class="yt-timestamp" data-t="00:12:31">[00:12:31]</a>. This is because each number in a row "donates" two copies of itself to the next row, effectively doubling the sum <a class="yt-timestamp" data-t="00:13:16">[00:13:16]</a>.

The formula for the number of regions is `1 + (n choose 2) + (n choose 4)`. This can be rewritten using [[mathematical_notation_and_conventions | Pascal's triangle]] notation as `(n choose 0) + (n choose 2) + (n choose 4)` <a class="yt-timestamp" data-t="00:13:37">[00:13:37]</a>.

*   For `n` values up to 5, the terms `(n choose 0)`, `(n choose 2)`, and `(n choose 4)` comprise *all* the non-zero terms in those rows of [[mathematical_notation_and_conventions | Pascal's triangle]]. Therefore, their sum *is* the total sum of that row, which is a power of two <a class="yt-timestamp" data-t="00:14:05">[00:14:05]</a>.
*   For `n = 6`, the row of [[mathematical_notation_and_conventions | Pascal's triangle]] contains terms `(6 choose 0)`, `(6 choose 1)`, `(6 choose 2)`, `(6 choose 3)`, `(6 choose 4)`, `(6 choose 5)`, `(6 choose 6)`.
    *   Our formula `(6 choose 0) + (6 choose 2) + (6 choose 4)` is `1 + 15 + 15 = 31`.
    *   The full sum of the 6th row is `1 + 6 + 15 + 20 + 15 + 6 + 1 = 64` (which is 2^6).
    *   The formula `1 + (n choose 2) + (n choose 4)` for `n=6` only sums up some of the even-indexed terms in the row. It specifically misses `(6 choose 1)` and `(6 choose 3)` and `(6 choose 5)` and `(6 choose 6)`.
    *   The reason it falls short by exactly 1 for `n=6` is that the terms `(6 choose 0)` through `(6 choose 4)` do *not* cover the whole previous row when related as `(n choose k) = (n-1 choose k-1) + (n-1 choose k)`. More precisely, by applying a known identity, the sum `(n choose 0) + (n choose 2) + (n choose 4) + ...` (sum of even terms) is `2^(n-1)`, and the sum `(n choose 1) + (n choose 3) + (n choose 5) + ...` (sum of odd terms) is also `2^(n-1)`.
    *   The formula `1 + (n choose 2) + (n choose 4)` for `n=6` is `(6 choose 0) + (6 choose 2) + (6 choose 4)`. This is `1 + 15 + 15 = 31`. The sum of all even-indexed terms in the 6th row of Pascal's triangle is `(6 choose 0) + (6 choose 2) + (6 choose 4) + (6 choose 6) = 1 + 15 + 15 + 1 = 32`. So, the pattern misses `(6 choose 6)` which is 1 <a class="yt-timestamp" data-t="00:14:27">[00:14:27]</a>.

> [!INFO]
> The pattern `1 + n choose 2 + n choose 4` is a sum of the 0th, 2nd, and 4th terms in the `n`th row of [[mathematical_notation_and_conventions | Pascal's triangle]] <a class="yt-timestamp" data-t="00:13:37">[00:13:37]</a>. For `n <= 5`, these terms account for all terms in the row, so their sum equals `2^(n-1)` (which is `2^n` for the problem's sequence if `n` starts at 1, or `2^n` if thinking about the row sum `2^n` starting with `n=0` for the first row). At `n=6`, the formula `(6 choose 0) + (6 choose 2) + (6 choose 4)` omits `(6 choose 6)` from the sum of *all even-indexed terms* in the 6th row, which would normally sum to `2^(6-1) = 32`. This missing `(6 choose 6)` term, which equals 1, is why the sum is `31` instead of `32` <a class="yt-timestamp" data-t="00:14:27">[00:14:27]</a>.

Interestingly, when `n = 10`, the terms summed `(10 choose 0) + (10 choose 2) + (10 choose 4)` constitute exactly half of the sum of all terms in the 9th row of [[mathematical_notation_and_conventions | Pascal's triangle]] (due to its symmetry), resulting in another power of two <a class="yt-timestamp" data-t="00:14:38">[00:14:38]</a>.

## Conclusion

Moser's Circle Problem serves as a powerful reminder to be cautious of patterns observed without rigorous proof <a class="yt-timestamp" data-t="00:15:37">[00:15:37]</a>. However, it also demonstrates that even apparent "coincidences" can lead to deeper, satisfying mathematical understandings through careful analysis and connection to fundamental principles like [[mathematical_notation_and_conventions | Euler's characteristic formula]] and [[mathematical_notation_and_conventions | Pascal's triangle]] <a class="yt-timestamp" data-t="00:15:41">[00:15:41]</a>.