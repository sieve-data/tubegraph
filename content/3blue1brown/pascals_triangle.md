---
title: Pascals triangle
videoId: YtkIWDE36qU
---

From: [[3blue1brown]] <br/> 

Pascal's triangle is a triangular array of binomial coefficients, where each term is the sum of the two terms directly above it <a class="yt-timestamp" data-t="01:41:41">[01:41:41]</a>.

## Properties and Applications

### Connection to Combinations (n choose k)
Every term within Pascal's triangle represents `n choose k` for specific values of `n` and `k` <a class="yt-timestamp" data-t="01:41:50">[01:41:50]</a>. This function calculates the number of distinct ways to choose `k` items from a set of `n` items, where the order of selection does not matter <a class="yt-timestamp" data-t="01:41:57">[01:41:57]</a>.

To locate `n choose k` in the triangle, rows and columns are typically indexed starting from 0 <a class="yt-timestamp" data-t="01:42:10">[01:42:10]</a>. For example, in the 5th row (0-indexed), the 3rd element (0-indexed) is 10, which corresponds to 5 choose 3 <a class="yt-timestamp" data-t="01:42:15">[01:42:15]</a>.

### Row Sums and Powers of Two
When the terms in each row of Pascal's triangle are summed, the result is always a power of two <a class="yt-timestamp" data-t="01:43:31">[01:43:31]</a>:
*   Row 0: 1 <a class="yt-timestamp" data-t="01:43:35">[01:43:35]</a>
*   Row 1: 1 + 1 = 2 <a class="yt-timestamp" data-t="01:43:35">[01:43:35]</a>
*   Row 2: 1 + 2 + 1 = 4 <a class="yt-timestamp" data-t="01:43:39">[01:43:39]</a>
*   Row 3: 1 + 3 + 3 + 1 = 8 <a class="yt-timestamp" data-t="01:43:39">[01:43:39]</a>

This pattern is genuine, not a trick <a class="yt-timestamp" data-t="01:44:50">[01:44:50]</a>. The reason for this pattern is that each number in a given row "donates" two copies of itself to the next row, causing the total sum of the terms in each subsequent row to double <a class="yt-timestamp" data-t="01:44:59">[01:44:59]</a>, <a class="yt-timestamp" data-t="01:45:11">[01:45:11]</a>, <a class="yt-timestamp" data-t="01:45:16">[01:45:16]</a>, <a class="yt-timestamp" data-t="01:45:21">[01:45:21]</a>, <a class="yt-timestamp" data-t="01:45:24">[01:45:24]</a>.

### Application in Moser's Circle Problem
Pascal's triangle provides insight into the pattern observed in [[mosers_circle_problem | Moser's Circle Problem]] <a class="yt-timestamp" data-t="01:36:00">[01:36:00]</a>, <a class="yt-timestamp" data-t="01:31:00">[01:31:00]</a>. The formula for the number of regions in [[mosers_circle_problem | Moser's Circle Problem]] is `1 + n choose 2 + n choose 4` <a class="yt-timestamp" data-t="01:11:11">[01:11:11]</a>. In the context of Pascal's triangle, this formula means adding the 0th, 2nd, and 4th terms in a specific row <a class="yt-timestamp" data-t="01:46:37">[01:46:37]</a>.

For `n` values of 5 or less, adding these terms corresponds to summing the entire previous row of Pascal's triangle, which results in a power of two <a class="yt-timestamp" data-t="01:47:55">[01:47:55]</a>, <a class="yt-timestamp" data-t="01:48:05">[01:48:05]</a>, <a class="yt-timestamp" data-t="01:48:08">[01:48:08]</a>.

The pattern breaks at `n = 6` because adding the first five elements of the previous row (n=5) does not cover the entire row, falling short by exactly 1 <a class="yt-timestamp" data-t="01:48:17">[01:48:17]</a>, <a class="yt-timestamp" data-t="01:48:21">[01:48:21]</a>, <a class="yt-timestamp" data-t="01:48:25">[01:48:25]</a>, <a class="yt-timestamp" data-t="01:48:27">[01:48:27]</a>, <a class="yt-timestamp" data-t="01:48:32">[01:48:32]</a>.

At `n = 10`, the result coincidentally returns to a power of two because adding the first five elements of the 9th row (n-1) covers exactly half of that symmetric row. Since the sum of an entire row is a power of two, half of that sum is also a power of two <a class="yt-timestamp" data-t="01:48:38">[01:48:38]</a>, <a class="yt-timestamp" data-t="01:49:42">[01:49:42]</a>, <a class="yt-timestamp" data-t="01:49:46">[01:49:46]</a>, <a class="yt-timestamp" data-t="01:49:51">[01:49:51]</a>. It is currently unknown if there are any further instances of the result being a power of two for `n > 10` <a class="yt-timestamp" data-t="01:49:56">[01:49:56]</a>.