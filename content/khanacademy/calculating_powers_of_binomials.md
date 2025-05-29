---
title: Calculating powers of binomials
videoId: iPwrDWQ7hPc
---

From: [[khanacademy]] <br/> 

Manually calculating higher powers of [[binomial_products | binomials]] can be a "painful" and time-consuming process <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. For instance, expanding expressions like `(a + b)^10` or `(a + b)^20` would take a significant amount of time <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>. This difficulty highlights the utility of the [[using_the_binomial_theorem_for_higher_powers | Binomial Theorem]] <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.

## Basic Binomial Expansions

Let's look at how binomials expand with increasing powers:

*   `(a + b)^0`
    Any non-zero term raised to the 0 power is equal to 1 <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.
*   `(a + b)^1`
    This simply expands to `a + b` <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>.
*   `(a + b)^2`
    A [[common_misconceptions_with_binomial_expansions | common misconception]] is to expand this as `a^2 + b^2`, which is incorrect <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.
    The correct expansion involves multiplying `(a + b)` by `(a + b)`:
    `(a + b)^2 = (a + b) * (a + b)` <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>
    `= a*a + a*b + b*a + b*b` <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>
    `= a^2 + ab + ab + b^2` <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>
    `= a^2 + 2ab + b^2` <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>
*   `(a + b)^3`
    To expand `(a + b)^3`, we multiply `(a + b)^2` by `(a + b)` <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>:
    `(a^2 + 2ab + b^2) * (a + b)`
    Multiplying by `b`:
    `b * b^2 = b^3` <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>
    `b * 2ab = 2ab^2` <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>
    `b * a^2 = a^2b` <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>
    Multiplying by `a`:
    `a * b^2 = ab^2` <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>
    `a * 2ab = 2a^2b` <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>
    `a * a^2 = a^3` <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>
    Adding the terms:
    `= a^3 + (a^2b + 2a^2b) + (2ab^2 + ab^2) + b^3` <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>
    `= a^3 + 3a^2b + 3ab^2 + b^3` <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>

## The Binomial Theorem

The [[using_the_binomial_theorem_for_higher_powers | Binomial Theorem]] provides a systematic way to expand binomials raised to any power <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.

For a binomial `(a + b)` raised to the `nth` power, the theorem states:
`(a + b)^n = Σ (k=0 to n) [n choose k * a^(n-k) * b^k]` <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>

Here, `n choose k` is a coefficient derived from [[combinatorics_and_factorials | combinatorics]] <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>.
[[understanding_n_choose_k_and_factorials_in_the_context_of_binomials | It is calculated using factorials]]:
`n choose k = n! / (k! * (n-k)!)` <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>
For this formula, `0!` is defined as 1 <a class="yt-timestamp" data-t="00:09:33">[00:09:33]</a>.

## Applying the Binomial Theorem: (a + b)^4

Let's use the Binomial Theorem to expand `(a + b)^4` <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>.
Here, `n = 4`. The sum will run from `k = 0` to `k = 4` <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>.

The expansion will be:
`(a + b)^4 = (4 choose 0)a^(4-0)b^0 + (4 choose 1)a^(4-1)b^1 + (4 choose 2)a^(4-2)b^2 + (4 choose 3)a^(4-3)b^3 + (4 choose 4)a^(4-4)b^4` <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>

Now, let's calculate each `n choose k` coefficient:
*   `4 choose 0 = 4! / (0! * 4!) = 1` (since `0! = 1`) <a class="yt-timestamp" data-t="00:09:35">[00:09:35]</a>
*   `4 choose 1 = 4! / (1! * 3!) = (4 * 3 * 2 * 1) / (1 * 3 * 2 * 1) = 4` <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>
*   `4 choose 2 = 4! / (2! * 2!) = (4 * 3 * 2 * 1) / ((2 * 1) * (2 * 1)) = 24 / 4 = 6` <a class="yt-timestamp" data-t="00:10:52">[00:10:52]</a>
*   `4 choose 3 = 4! / (3! * 1!) = (4 * 3 * 2 * 1) / ((3 * 2 * 1) * 1) = 4` <a class="yt-timestamp" data-t="00:11:23">[00:11:23]</a>
*   `4 choose 4 = 4! / (4! * 0!) = 1` <a class="yt-timestamp" data-t="00:11:40">[00:11:40]</a>

Substituting these coefficients back into the expansion:
`(a + b)^4 = 1a^4b^0 + 4a^3b^1 + 6a^2b^2 + 4a^1b^3 + 1a^0b^4` <a class="yt-timestamp" data-t="00:11:48">[00:11:48]</a>
Simplifying, noting that `x^0 = 1`:
`(a + b)^4 = a^4 + 4a^3b + 6a^2b^2 + 4ab^3 + b^4` <a class="yt-timestamp" data-t="00:12:37">[00:12:37]</a>

### Patterns in Binomial Expansions

Observing the expansion of `(a + b)^4`, we can identify several [[patterns_in_binomial_expansions | patterns]]:
*   **Coefficients**: The coefficients display [[symmetry_in_binomial_probabilities | symmetry]] (1, 4, 6, 4, 1) <a class="yt-timestamp" data-t="00:12:47">[00:12:47]</a>.
*   **Exponents of 'a'**: The power of `a` starts at `n` (here, 4) and decreases by one in each subsequent term (a^4, a^3, a^2, a^1, a^0) <a class="yt-timestamp" data-t="00:12:52">[00:12:52]</a>.
*   **Exponents of 'b'**: The power of `b` starts at 0 and increases by one in each subsequent term (b^0, b^1, b^2, b^3, b^4) <a class="yt-timestamp" data-t="00:12:57">[00:12:57]</a>.

The Binomial Theorem makes it possible to efficiently calculate expansions for very high powers, which would be impractical by direct multiplication <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>.