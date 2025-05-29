---
title: Pascals triangle and the powers of two
videoId: YtkIWDE36qU
---

From: [[3blue1brown]] <br/> 

Pascal's Triangle is a mathematical arrangement where each term is the sum of the two terms directly above it <a class="yt-timestamp" data-t="00:11:41">[00:11:41]</a>. It provides a "visceral connection" to the pattern observed in Moser's Circle Problem regarding powers of two <a class="yt-timestamp" data-t="00:15:29">[00:15:29]</a>.

## Relation to Combinations (n Choose k)

Every term within Pascal's Triangle represents `n choose k` for some values of `n` and `k` <a class="yt-timestamp" data-t="00:11:50">[00:11:50]</a>. This function, `n choose k`, answers the question of how many ways one can select a subset of size `k` from a set of size `n` <a class="yt-timestamp" data-t="00:11:57">[00:11:57]</a>. Rows and columns are typically indexed starting from zero <a class="yt-timestamp" data-t="00:12:06">[00:12:06]</a>. For example, `5 choose 3` is found in the 5th row, 3rd element (when starting counts from 0), and its value is 10 <a class="yt-timestamp" data-t="00:12:10">[00:12:10]</a>.

### Calculating `n choose k`

*   **`n choose 2`**: This counts the number of distinct pairs that can be chosen from a set of `n` items, where order doesn't matter <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>. It is calculated as `n * (n - 1) / 2` <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>. For example, `7 choose 2` is `(7 * 6) / 2 = 21` <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>.
*   **`n choose 4`**: This counts the number of distinct quadruplets from a set of size `n` <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>. It is calculated by multiplying `n * (n - 1) * (n - 2) * (n - 3)` and then dividing by `4!` (4 factorial), which is `4 * 3 * 2 * 1 = 24` <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>. For example, `4 choose 4` equals 1 <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>, and `6 choose 4` equals 15 <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>.

## Sum of the Rows and Powers of Two

A key property of Pascal's Triangle is that when its rows are summed, the results are always powers of two <a class="yt-timestamp" data-t="00:12:31">[00:12:31]</a>.
*   Row 0: 1 = `2^0` <a class="yt-timestamp" data-t="00:12:35">[00:12:35]</a>
*   Row 1: 1 + 1 = 2 = `2^1` <a class="yt-timestamp" data-t="00:12:35">[00:12:35]</a>
*   Row 2: 1 + 2 + 1 = 4 = `2^2` <a class="yt-timestamp" data-t="00:12:37">[00:12:37]</a>
*   Row 3: 1 + 3 + 3 + 1 = 8 = `2^3` <a class="yt-timestamp" data-t="00:12:39">[00:12:39]</a>

This is a "genuine pattern" without trickery <a class="yt-timestamp" data-t="00:12:50">[00:12:50]</a>. The reason for this is that as one goes from one row to the next, each number "donates two copies of itself" to the row below it <a class="yt-timestamp" data-t="00:13:16">[00:13:16]</a>. Consequently, the total sum of the numbers in each row doubles with every iteration <a class="yt-timestamp" data-t="00:13:21">[00:13:21]</a>.

## Moser's Circle Problem Connection

The formula for the number of regions a circle is divided into by connecting `n` points on its boundary (in the generic case where no three lines intersect at the same point inside the circle) is `1 + n choose 2 + n choose 4` <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>.

When this formula is related to Pascal's Triangle, it can be seen as adding up the 0th, 2nd, and 4th terms (`n choose 0`, `n choose 2`, `n choose 4`) in a given row <a class="yt-timestamp" data-t="00:13:37">[00:13:37]</a>.

For `n` values up to 5, adding these specific terms is equivalent to summing the *entire* previous row of Pascal's Triangle, which results in a power of two <a class="yt-timestamp" data-t="00:13:51">[00:13:51]</a>.
*   For `n = 2` points, there are 2 regions (2^1) <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>.
*   For `n = 3` points, there are 4 regions (2^2) <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>.
*   For `n = 4` points, there are 8 regions (2^3) <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.
*   For `n = 5` points, there are 16 regions (2^4) <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.

### The "Break" in the Pattern

The pattern appears to break at `n = 6` points, yielding 31 regions instead of the expected 32 (2^5) <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>. This happens because for `n = 6`, adding `n choose 0`, `n choose 2`, and `n choose 4` (i.e., `6 choose 0 + 6 choose 2 + 6 choose 4`) does not sum the *entirety* of the previous row (the 5th row) <a class="yt-timestamp" data-t="00:14:21">[00:14:21]</a>. Specifically, it falls short by 1, explaining why the result is `2^n - 1` <a class="yt-timestamp" data-t="00:14:27">[00:14:27]</a>.

### The "Reappearance" of a Power of Two

Surprisingly, another power of two appears at the tenth iteration (`n = 10`) <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>. When `n = 10`, summing `10 choose 0`, `10 choose 2`, and `10 choose 4` corresponds to adding the first five elements of the 9th row of Pascal's Triangle <a class="yt-timestamp" data-t="00:14:38">[00:14:38]</a>. Due to the symmetry of Pascal's Triangle, this sum equals exactly half of the total sum of the 9th row (which is `2^9`) <a class="yt-timestamp" data-t="00:14:46">[00:14:46]</a>. Half of a power of two is also a power of two (`2^8`), which accounts for the reappearance of a power of two at `n=10` <a class="yt-timestamp" data-t="00:14:51">[00:14:51]</a>.