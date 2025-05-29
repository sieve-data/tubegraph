---
title: Patterns in binomial expansions
videoId: iPwrDWQ7hPc
---

From: [[khanacademy]] <br/> 

Expanding [[binomial products | binomial products]] to higher powers can become computationally "painful" very quickly without a systematic approach <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. While direct multiplication works for lower powers, observing the resulting patterns leads to the powerful [[binomial_theorem | Binomial Theorem]] for [[calculating_powers_of_binomials | calculating powers of binomials]] more efficiently <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.

## Basic Binomial Expansions

Let's look at the first few powers of the binomial `(a + b)`:

*   **`(a + b)^0`**: Any non-zero term raised to the 0 power equals 1 <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>.
    `(a + b)^0 = 1` <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>
*   **`(a + b)^1`**:
    `(a + b)^1 = a + b` <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>
*   **`(a + b)^2`**: A [[common_misconceptions_with_binomial_expansions | common misconception]] is to assume this is `a^2 + b^2` <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>. However, `(a + b)^2` means `(a + b) * (a + b)` <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.
    Applying distribution (FOIL):
    `a * a = a^2` <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>
    `a * b = ab` <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>
    `b * a = ab` <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>
    `b * b = b^2` <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>
    Combining terms:
    `(a + b)^2 = a^2 + 2ab + b^2` <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>
*   **`(a + b)^3`**: This can be found by multiplying `(a + b)^2` by `(a + b)` <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.
    `(a^2 + 2ab + b^2) * (a + b)` <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>
    Multiplying `b` by each term in the first polynomial:
    `b * b^2 = b^3` <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>
    `b * 2ab = 2ab^2` <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>
    `b * a^2 = a^2b` <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>
    Multiplying `a` by each term in the first polynomial:
    `a * b^2 = ab^2` <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>
    `a * 2ab = 2a^2b` <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>
    `a * a^2 = a^3` <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>
    Adding these results:
    `(a + b)^3 = a^3 + 3a^2b + 3ab^2 + b^3` <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>

Directly calculating [[using_the_binomial_theorem_for_higher_powers | higher powers]], such as `(a + b)^10` or `(a + b)^20`, would be "incredibly painful" <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.

## The Binomial Theorem

The [[binomial_theorem | Binomial Theorem]] provides a general formula for expanding `(a + b)^n` <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.
The theorem states:
`(a + b)^n = Σ (from k=0 to n) of (n choose k) * a^(n-k) * b^k` <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>

Here, `n choose k` is a term from [[combinatorics_and_factorials | combinatorics]], also written as `(n k)` or `nCk` <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>. It represents the number of ways to choose `k` items from a set of `n` items.
The formula for [[understanding_n_choose_k_and_factorials_in_the_context_of_binomials | n choose k]] is:
`n choose k = n! / (k! * (n - k)!)` <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>
(Note: 0! is defined as 1 for these purposes <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>).

## Applying the Theorem: `(a + b)^4`

Let's use the [[binomial_theorem | Binomial Theorem]] to expand `(a + b)^4` <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>. Here, `n = 4`.
`(a + b)^4 = Σ (from k=0 to 4) of (4 choose k) * a^(4-k) * b^k` <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>

Expanding the sum term by term for `k = 0, 1, 2, 3, 4`:

*   **For `k = 0`**:
    `4 choose 0 = 4! / (0! * 4!) = 1` <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a>
    Term: `1 * a^(4-0) * b^0 = 1 * a^4 * 1 = a^4` <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>
*   **For `k = 1`**:
    `4 choose 1 = 4! / (1! * 3!) = (4*3*2*1) / (1 * 3*2*1) = 4` <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>
    Term: `4 * a^(4-1) * b^1 = 4a^3b` <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>
*   **For `k = 2`**:
    `4 choose 2 = 4! / (2! * 2!) = (4*3*2*1) / ((2*1) * (2*1)) = 24 / 4 = 6` <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>
    Term: `6 * a^(4-2) * b^2 = 6a^2b^2` <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>
*   **For `k = 3`**:
    `4 choose 3 = 4! / (3! * 1!) = (4*3*2*1) / ((3*2*1) * 1) = 4` <a class="yt-timestamp" data-t="00:10:59">[00:10:59]</a>
    Term: `4 * a^(4-3) * b^3 = 4ab^3` <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>
*   **For `k = 4`**:
    `4 choose 4 = 4! / (4! * 0!) = 1` <a class="yt-timestamp" data-t="00:11:27">[00:11:27]</a>
    Term: `1 * a^(4-4) * b^4 = 1 * a^0 * b^4 = b^4` <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>

Adding all these terms together:
`(a + b)^4 = a^4 + 4a^3b + 6a^2b^2 + 4ab^3 + b^4` <a class="yt-timestamp" data-t="00:11:48">[00:11:48]</a>

## Observed Patterns in Expansions

Several important patterns emerge from these expansions:

1.  **Powers of `a`**: The power of the first term (`a`) decreases by 1 in each subsequent term, starting from `n` down to `0` <a class="yt-timestamp" data-t="00:12:51">[00:12:51]</a>. (e.g., `a^4, a^3, a^2, a^1, a^0`)
2.  **Powers of `b`**: The power of the second term (`b`) increases by 1 in each subsequent term, starting from `0` up to `n` <a class="yt-timestamp" data-t="00:12:57">[00:12:57]</a>. (e.g., `b^0, b^1, b^2, b^3, b^4`)
3.  **Sum of Powers**: In every term of the expansion, the sum of the exponents of `a` and `b` always equals `n` (the power to which the binomial is raised) <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.
4.  **Coefficients**: The coefficients (`n choose k` values) form a symmetrical pattern <a class="yt-timestamp" data-t="00:12:41">[00:12:41]</a>. For `(a+b)^4`, the coefficients are `1, 4, 6, 4, 1` <a class="yt-timestamp" data-t="00:12:45">[00:12:45]</a>. This [[symmetry_in_binomial_probabilities | symmetry]] is a characteristic of [[binomial_distribution | binomial theorem]] expansions. These coefficients correspond to rows in Pascal's Triangle.