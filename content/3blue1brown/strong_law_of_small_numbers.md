---
title: Strong law of small numbers
videoId: YtkIWDE36qU
---

From: [[3blue1brown]] <br/> 

The strong law of small numbers is a famous cautionary tale in mathematics <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. It was coined by mathematician Richard Guy <a class="yt-timestamp" data-t="01:44:00">[01:44:00]</a>.

## Definition
The law is summed up by the phrase: "there aren't enough small numbers to meet the many demands made of them" <a class="yt-timestamp" data-t="01:47:00">[01:47:00]</a>. This highlights situations where initial small numbers in a sequence might suggest a pattern that doesn't hold true for larger numbers <a class="yt-timestamp" data-t="01:47:00">[01:47:00]</a>.

## Example: Moser's Circle Problem
Moser's circle problem is a prime example of the strong law of small numbers <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>, <a class="yt-timestamp" data-t="01:40:00">[01:40:00]</a>. This problem involves placing `n` points on a circle and connecting them with all possible chords, then counting the number of regions the circle is divided into <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>, <a class="yt-timestamp" data-t="02:26:00">[02:26:00]</a>.

The pattern observed for a small number of points is as follows:
*   **2 points:** 2 regions <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>, <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>
*   **3 points:** 4 regions <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>, <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>
*   **4 points:** 8 regions <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>, <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>
*   **5 points:** 16 regions <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>, <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>

This sequence (2, 4, 8, 16) strongly suggests that the number of regions is a power of two, specifically 2<sup>n-1</sup> or 2<sup>n</sup> depending on how `n` is defined initially <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.

However, when a sixth point is added:
*   **6 points:** The number of regions is 31, not the expected 32 (2<sup>5</sup>) <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>, <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>.

This problem serves as a "tease," appearing to follow a convincing power-of-two pattern until it "just barely breaks" <a class="yt-timestamp" data-t="01:29:00">[01:29:00]</a>.

### Conditions for the pattern
The number of regions depends on the placement of points; however, for the purpose of the problem, it's assumed that no three lines intersect at a single point within the circle <a class="yt-timestamp" data-t="01:06:00">[01:06:00]</a>, <a class="yt-timestamp" data-t="01:14:00">[01:14:00]</a>. This is considered the generic case if `n` random points are chosen <a class="yt-timestamp" data-t="01:20:00">[01:20:00]</a>.

### The Actual Formula
The actual number of regions for `n` points is given by the formula: 1 + n choose 2 + n choose 4 <a class="yt-timestamp" data-t="01:11:00">[01:11:00]</a>.
*   "n choose 2" (or C(n,2)) represents the number of chords, which is the number of distinct pairs of points on the circle <a class="yt-timestamp" data-t="03:04:00">[03:04:00]</a>, <a class="yt-timestamp" data-t="03:09:00">[03:09:00]</a>. It is calculated as `n * (n-1) / 2` <a class="yt-timestamp" data-t="03:25:00">[03:25:00]</a>, <a class="yt-timestamp" data-t="03:46:00">[03:46:00]</a>.
*   "n choose 4" (or C(n,4)) represents the number of intersection points within the circle <a class="yt-timestamp" data-t="04:50:00">[04:50:00]</a>, <a class="yt-timestamp" data-t="04:54:00">[04:54:00]</a>. Each intersection point corresponds uniquely to a quadruplet of points on the circle's exterior <a class="yt-timestamp" data-t="04:31:00">[04:31:00]</a>, <a class="yt-timestamp" data-t="04:37:00">[04:37:00]</a>. It is calculated as `n * (n-1) * (n-2) * (n-3) / 4!` <a class="yt-timestamp" data-t="05:11:00">[05:11:00]</a>, <a class="yt-timestamp" data-t="05:31:00">[05:31:00]</a>.

This formula is derived using Euler's characteristic formula (V - E + F = 2) for planar graphs <a class="yt-timestamp" data-t="06:27:00">[06:27:00]</a>, <a class="yt-timestamp" data-t="08:27:00">[08:27:00]</a>. By treating the intersection points as new vertices, the complex diagram can be viewed as a planar graph <a class="yt-timestamp" data-t="09:20:00">[09:20:00]</a>, <a class="yt-timestamp" data-t="09:24:00">[09:24:00]</a>. The formula simplifies from `E - V + 2` (for total regions including the outer infinite region) to `E - V + 1` (for regions within the circle) <a class="yt-timestamp" data-t="09:00:00">[09:00:00]</a>, <a class="yt-timestamp" data-t="09:04:00">[09:04:00]</a>.

### Connection to Pascal's Triangle
The reason the pattern initially appears as powers of two before breaking by one is explained by Pascal's triangle <a class="yt-timestamp" data-t="01:36:00">[01:36:00]</a>, <a class="yt-timestamp" data-t="01:40:00">[01:40:00]</a>.
*   Each term in Pascal's triangle is an "n choose k" value <a class="yt-timestamp" data-t="01:50:00">[01:50:00]</a>, <a class="yt-timestamp" data-t="01:53:00">[01:53:00]</a>.
*   The sum of elements in any row of Pascal's triangle equals a power of two <a class="yt-timestamp" data-t="01:31:00">[01:31:00]</a>, <a class="yt-timestamp" data-t="01:35:00">[01:35:00]</a>, <a class="yt-timestamp" data-t="01:39:00">[01:39:00]</a>. This happens because each number in the triangle "donates" two copies of itself to the next row, causing the sum of the row totals to double with each iteration <a class="yt-timestamp" data-t="01:59:00">[01:59:00]</a>, <a class="yt-timestamp" data-t="01:13:00">[01:13:00]</a>, <a class="yt-timestamp" data-t="01:16:00">[01:16:00]</a>, <a class="yt-timestamp" data-t="01:20:00">[01:20:00]</a>, <a class="yt-timestamp" data-t="01:21:00">[01:21:00]</a>.

The formula for the number of regions (1 + n choose 2 + n choose 4) corresponds to adding the 0th, 2nd, and 4th terms in the nth row of Pascal's triangle <a class="yt-timestamp" data-t="01:37:00">[01:37:00]</a>, <a class="yt-timestamp" data-t="01:42:00">[01:42:00]</a>.
*   For n <= 5, these terms sum to the entire sum of the previous row in Pascal's triangle, which is a power of two <a class="yt-timestamp" data-t="01:46:00">[01:46:00]</a>, <a class="yt-timestamp" data-t="01:51:00">[01:51:00]</a>.
*   For n = 6, adding these terms from the 6th row of Pascal's triangle corresponds to adding the first five elements of the 5th row <a class="yt-timestamp" data-t="01:41:00">[01:41:00]</a>, <a class="yt-timestamp" data-t="01:42:00">[01:42:00]</a>. This sum falls short of the total sum of the 5th row (which is 2<sup>5</sup>=32) by exactly one (the last element of the 5th row is 1), resulting in 31 regions <a class="yt-timestamp" data-t="01:42:00">[01:42:00]</a>, <a class="yt-timestamp" data-t="01:46:00">[01:46:00]</a>, <a class="yt-timestamp" data-t="01:51:00">[01:51:00]</a>.
*   It is also noted that for n = 10, the pattern seemingly randomly hits another power of two <a class="yt-timestamp" data-t="02:11:00">[02:11:00]</a>, <a class="yt-timestamp" data-t="02:14:00">[02:14:00]</a>, <a class="yt-timestamp" data-t="01:35:00">[01:35:00]</a>, <a class="yt-timestamp" data-t="01:38:00">[01:38:00]</a>. This occurs because for n=10, adding the first 5 elements of the 9th row of Pascal's triangle equals exactly half of that row's sum, which itself is a power of two due to the triangle's symmetry <a class="yt-timestamp" data-t="01:42:00">[01:42:00]</a>, <a class="yt-timestamp" data-t="01:46:00">[01:46:00]</a>, <a class="yt-timestamp" data-t="01:51:00">[01:51:00]</a>.

In summary, while the strong law of small numbers highlights the danger of generalizing patterns from limited data <a class="yt-timestamp" data-t="01:37:00">[01:37:00]</a>, <a class="yt-timestamp" data-t="01:40:00">[01:40:00]</a>, it also demonstrates that such "coincidences" can lead to deeper, satisfying mathematical understandings <a class="yt-timestamp" data-t="01:41:00">[01:41:00]</a>, <a class="yt-timestamp" data-t="01:45:00">[01:45:00]</a>.