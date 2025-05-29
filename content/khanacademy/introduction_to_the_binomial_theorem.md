---
title: Introduction to the binomial theorem
videoId: iPwrDWQ7hPc
---

From: [[khanacademy]] <br/> 

Expanding higher powers of [[understanding_binomials_and_their_products | binomials]] can become quite tedious and painful <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. The [[expanding_binomials_using_the_binomial_theorem | Binomial Theorem]] provides a systematic way to expand expressions of the form ` (a + b)^n ` <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.

## Manual Expansion of Binomials

Before introducing the theorem, let's examine how quickly manual expansion becomes complex. A binomial is an algebraic expression with two terms, such as ` a + b ` <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>.

*   ` (a + b)^0 `
    *   Any non-zero term raised to the power of 0 equals 1 <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.
    *   Therefore, ` (a + b)^0 = 1 ` <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

*   ` (a + b)^1 `
    *   Anything raised to the power of 1 is itself <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>.
    *   Therefore, ` (a + b)^1 = a + b ` <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>.

*   ` (a + b)^2 `
    *   It is a common mistake to assume ` (a + b)^2 ` equals ` a^2 + b^2 ` <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.
    *   Instead, ` (a + b)^2 ` means ` (a + b) * (a + b) ` <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.
    *   Expanding this: ` a*a + a*b + b*a + b*b ` <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>
    *   This simplifies to ` a^2 + ab + ab + b^2 ` <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>
    *   Result: ` a^2 + 2ab + b^2 ` <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.

*   ` (a + b)^3 `
    *   This can be found by multiplying ` (a + b)^2 ` by ` (a + b) ` <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.
    *   ` (a^2 + 2ab + b^2) * (a + b) ` <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>
    *   Multiplying each term:
        *   ` b * b^2 = b^3 ` <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>
        *   ` b * 2ab = 2ab^2 ` <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>
        *   ` b * a^2 = a^2b ` <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>
        *   ` a * b^2 = ab^2 ` <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>
        *   ` a * 2ab = 2a^2b ` <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>
        *   ` a * a^2 = a^3 ` <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>
    *   Combining like terms: ` a^3 + 3a^2b + 3ab^2 + b^3 ` <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.

As seen, calculating ` (a + b)^3 ` takes a reasonable amount of time, implying that higher powers like ` (a + b)^4 ` or ` (a + b)^10 ` would be incredibly painful and time-consuming <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.

## The Binomial Theorem Formula

The [[expanding_binomials_using_the_binomial_theorem | Binomial Theorem]] provides a general formula for expanding ` (a + b)^n ` <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>:

` (a + b)^n = Σ (from k=0 to n) [ (n choose k) * a^(n-k) * b^k ] ` <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>

Where:
*   ` n ` is the power to which the binomial is raised <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>.
*   ` k ` is an index that ranges from 0 to ` n ` <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>.
*   ` (n choose k) ` represents a [[binomial_coefficients_and_combinatorics | binomial coefficient]], which comes from [[binomial_coefficients_and_combinatorics | combinatorics]] <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>. It is calculated as:
    ` (n choose k) = n! / (k! * (n - k)!) ` <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>
    *   Note: ` 0! ` is defined as 1 <a class="yt-timestamp" data-t="00:09:33">[00:09:33]</a>.

## Application: (a + b)^4

Let's use the [[expanding_binomials_using_the_binomial_theorem | Binomial Theorem]] to expand ` (a + b)^4 ` <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>. Here, ` n = 4 `.

According to the theorem, ` (a + b)^4 = Σ (from k=0 to 4) [ (4 choose k) * a^(4-k) * b^k ] ` <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>.

We will sum the terms for each value of ` k `:

1.  **For k = 0**:
    *   Coefficient: ` (4 choose 0) = 4! / (0! * (4-0)!) = 4! / (1 * 4!) = 1 ` <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a>
    *   Term: ` 1 * a^(4-0) * b^0 = a^4 * 1 = a^4 ` <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>

2.  **For k = 1**:
    *   Coefficient: ` (4 choose 1) = 4! / (1! * (4-1)!) = 4! / (1 * 3!) = (4*3*2*1) / (3*2*1) = 4 ` <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>
    *   Term: ` 4 * a^(4-1) * b^1 = 4a^3b ` <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>

3.  **For k = 2**:
    *   Coefficient: ` (4 choose 2) = 4! / (2! * (4-2)!) = 4! / (2! * 2!) = (4*3*2*1) / ((2*1)*(2*1)) = 24 / 4 = 6 ` <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>
    *   Term: ` 6 * a^(4-2) * b^2 = 6a^2b^2 ` <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>

4.  **For k = 3**:
    *   Coefficient: ` (4 choose 3) = 4! / (3! * (4-3)!) = 4! / (3! * 1!) = (4*3*2*1) / ((3*2*1)*1) = 4 ` <a class="yt-timestamp" data-t="00:10:59">[00:10:59]</a>
    *   Term: ` 4 * a^(4-3) * b^3 = 4ab^3 ` <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>

5.  **For k = 4**:
    *   Coefficient: ` (4 choose 4) = 4! / (4! * (4-4)!) = 4! / (4! * 0!) = 1 ` <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>
    *   Term: ` 1 * a^(4-4) * b^4 = a^0 * b^4 = 1 * b^4 = b^4 ` <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>

Summing these terms gives the full expansion of ` (a + b)^4 `:
` (a + b)^4 = a^4 + 4a^3b + 6a^2b^2 + 4ab^3 + b^4 ` <a class="yt-timestamp" data-t="00:11:58">[00:11:58]</a>.

## Patterns and Symmetry

Observing the expansion of ` (a + b)^4 `, we can see clear [[patterns_and_symmetry_in_binomial_expansions | patterns and symmetry]] <a class="yt-timestamp" data-t="00:12:41">[00:12:41]</a>:

*   **Coefficients**: The coefficients follow a symmetrical pattern: 1, 4, 6, 4, 1 <a class="yt-timestamp" data-t="00:12:45">[00:12:45]</a>.
*   **Exponents of 'a'**: The power of ` a ` decreases from ` n ` down to 0 ( ` a^4, a^3, a^2, a^1, a^0 `) <a class="yt-timestamp" data-t="00:12:51">[00:12:51]</a>.
*   **Exponents of 'b'**: The power of ` b ` increases from 0 up to ` n ` ( ` b^0, b^1, b^2, b^3, b^4 `) <a class="yt-timestamp" data-t="00:12:57">[00:12:57]</a>.
*   **Sum of Exponents**: In each term, the sum of the exponents of ` a ` and ` b ` always equals ` n ` (e.g., for ` 6a^2b^2 `, ` 2 + 2 = 4 `).

These [[patterns_and_symmetry_in_binomial_expansions | patterns and symmetry]] are consistent for all binomial expansions and highlight the elegance and efficiency of the [[expanding_binomials_using_the_binomial_theorem | Binomial Theorem]] compared to manual multiplication.