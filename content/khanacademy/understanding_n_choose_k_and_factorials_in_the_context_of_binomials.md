---
title: Understanding n choose k and factorials in the context of binomials
videoId: iPwrDWQ7hPc
---

From: [[khanacademy]] <br/> 

Calculating higher and higher [[calculating_powers_of_binomials | powers of binomials]] can become a challenging and "painful" task manually <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>.

Consider these simple expansions:
*   Any non-zero term to the 0 power equals 1 <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>.
    *   `(a + b)^0 = 1` <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>
*   `(a + b)^1 = a + b` <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>
*   `(a + b)^2` is *not* `a^2 + b^2` <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. This is a [[common_misconceptions_with_binomial_expansions | common misconception]] <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.
    *   `(a + b)^2 = (a + b) * (a + b)` <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>
    *   This expands to `a*a + a*b + b*a + b*b = a^2 + ab + ab + b^2 = a^2 + 2ab + b^2` <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.
*   `(a + b)^3` can be found by multiplying `(a^2 + 2ab + b^2)` by `(a + b)` <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.
    *   This results in `a^3 + 3a^2b + 3ab^2 + b^3` <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.

As the power increases, manually expanding [[binomial products | binomial products]] becomes very time-consuming <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>. This is where the [[using_the_binomial_theorem_for_higher_powers | binomial theorem]] proves useful <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.

## The Binomial Theorem

The [[using_the_binomial_theorem_for_higher_powers | binomial theorem]] provides a formula for expanding a binomial `(a + b)` raised to the `n`th power <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>:

`(a + b)^n = Σ (from k=0 to n) of (n choose k) * a^(n-k) * b^k` <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>

## Understanding "n choose k" (Binomial Coefficient)

The term "n choose k" (written as `(n k)` or `nCk`) represents a binomial coefficient <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>. It originates from [[combinatorics_and_factorials | combinatorics]] <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a> and is calculated using [[combinatorics_and_factorials | factorials]]:

`n choose k = n! / (k! * (n - k)!)` <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>

### Factorial Definition

*   `n!` (n factorial) is the product of all positive integers less than or equal to `n`.
*   By convention, `0!` (zero factorial) is defined as 1 for these calculations <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.

## Applying the Binomial Theorem: Example with (a + b)^4

Let's use the [[using_the_binomial_theorem_for_higher_powers | binomial theorem]] to expand `(a + b)^4` <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>. Here, `n = 4`.

The expansion will be the sum from `k=0` to `k=4` of `(4 choose k) * a^(4-k) * b^k` <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>:

1.  **For k = 0**:
    *   Coefficient: `4 choose 0 = 4! / (0! * (4-0)!) = 4! / (1 * 4!) = 1` <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a>
    *   Term: `1 * a^(4-0) * b^0 = 1 * a^4 * 1 = a^4` <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>

2.  **For k = 1**:
    *   Coefficient: `4 choose 1 = 4! / (1! * (4-1)!) = 4! / (1 * 3!) = (4 * 3 * 2 * 1) / (3 * 2 * 1) = 4` <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>
    *   Term: `4 * a^(4-1) * b^1 = 4a^3b` <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>

3.  **For k = 2**:
    *   Coefficient: `4 choose 2 = 4! / (2! * (4-2)!) = 4! / (2! * 2!) = (4 * 3 * 2 * 1) / ((2 * 1) * (2 * 1)) = 24 / 4 = 6` <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>
    *   Term: `6 * a^(4-2) * b^2 = 6a^2b^2` <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>

4.  **For k = 3**:
    *   Coefficient: `4 choose 3 = 4! / (3! * (4-3)!) = 4! / (3! * 1!) = (4 * 3 * 2 * 1) / (3 * 2 * 1) = 4` <a class="yt-timestamp" data-t="00:10:59">[00:10:59]</a>
    *   Term: `4 * a^(4-3) * b^3 = 4ab^3` <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>

5.  **For k = 4**:
    *   Coefficient: `4 choose 4 = 4! / (4! * (4-4)!) = 4! / (4! * 0!) = 4! / (4! * 1) = 1` <a class="yt-timestamp" data-t="00:11:27">[00:11:27]</a>
    *   Term: `1 * a^(4-4) * b^4 = 1 * a^0 * b^4 = b^4` <a class="yt-timestamp" data-t="00:08:55">[00:08:55]</a>

Adding these terms together, we get the full expansion:
`(a + b)^4 = a^4 + 4a^3b + 6a^2b^2 + 4ab^3 + b^4` <a class="yt-timestamp" data-t="00:12:00">[00:12:00]</a>

### [[patterns_in_binomial_expansions | Patterns in Binomial Expansions]]

Observing the expansion of `(a + b)^4`, several [[patterns_in_binomial_expansions | patterns]] emerge <a class="yt-timestamp" data-t="00:12:41">[00:12:41]</a>:
*   **Symmetry in Coefficients**: The coefficients are symmetrical: 1, 4, 6, 4, 1 <a class="yt-timestamp" data-t="00:12:42">[00:12:42]</a>.
*   **Exponents of 'a'**: The power of 'a' decreases from `n` to 0 (e.g., `a^4, a^3, a^2, a^1, a^0`) <a class="yt-timestamp" data-t="00:12:51">[00:12:51]</a>.
*   **Exponents of 'b'**: The power of 'b' increases from 0 to `n` (e.g., `b^0, b^1, b^2, b^3, b^4`) <a class="yt-timestamp" data-t="00:12:57">[00:12:57]</a>.

These [[patterns_in_binomial_expansions | patterns]] are consistent across all binomial expansions and are directly derived from the structure of the [[using_the_binomial_theorem_for_higher_powers | binomial theorem]].