---
title: Stepbystep process of expanding binomials
videoId: iPwrDWQ7hPc
---

From: [[khanacademy]] <br/> 

Expanding binomials to higher powers can become computationally intensive <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. While simple cases are straightforward, the process quickly becomes cumbersome for larger exponents <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>.

## Basic Binomial Expansions

To understand the challenge, consider some basic expansions of a binomial, such as `a + b` <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.

*   **To the 0 power**: Any non-zero expression to the 0 power equals 1 <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>.
    `(a + b)^0 = 1` <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>

*   **To the 1st power**:
    `(a + b)^1 = a + b` <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>

*   **To the 2nd power (Squaring a Binomial)**:
    A common [[misconceptions_about_expanding_binomials | misconception about expanding binomials]] is to assume `(a + b)^2` is `a^2 + b^2`, which is incorrect <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>. Instead, `(a + b)^2` means `(a + b) * (a + b)` <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.

    To expand `(a + b) * (a + b)`:
    *   `a * a = a^2` <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>
    *   `a * b = ab` <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>
    *   `b * a = ab` <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>
    *   `b * b = b^2` <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>
    Combining like terms: `a^2 + ab + ab + b^2 = a^2 + 2ab + b^2` <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>

*   **To the 3rd power (Cubing a Binomial)**:
    `(a + b)^3` can be found by multiplying `(a + b)^2` by another `(a + b)` <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>. Using the result from the previous step:
    `(a^2 + 2ab + b^2) * (a + b)` <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>

    Multiplying term by term:
    *   Multiply by `b`:
        *   `b * b^2 = b^3` <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>
        *   `b * 2ab = 2ab^2` <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>
        *   `b * a^2 = a^2b` <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>
    *   Multiply by `a`:
        *   `a * b^2 = ab^2` <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>
        *   `a * 2ab = 2a^2b` <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>
        *   `a * a^2 = a^3` <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>

    Adding all terms together:
    `a^3 + (2a^2b + a^2b) + (2ab^2 + ab^2) + b^3` <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>
    `a^3 + 3a^2b + 3ab^2 + b^3` <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>

## The Challenge of Higher Powers

Manually expanding binomials to the 4th, 10th, or even 20th power would be extremely time-consuming and prone to errors <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>. This is where the [[introduction_to_the_binomial_theorem | binomial theorem]] becomes an essential tool <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.

## The Binomial Theorem

The [[introduction_to_the_binomial_theorem | binomial theorem]] provides a general formula for expanding `(a + b)^n` <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.

The formula is:
`(a + b)^n = Σ (from k=0 to n) [ (n choose k) * a^(n-k) * b^k ]` <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>

Here, `(n choose k)` represents a binomial coefficient, which comes from [[introduction_to_binomial_coefficients_and_combinatorics | combinatorics]] <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>. It is calculated as:
`(n choose k) = n! / (k! * (n - k)!)` <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>
Where `!` denotes the factorial (e.g., `4! = 4 * 3 * 2 * 1`), and `0!` is defined as 1 <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.

## Applying the Binomial Theorem: (a + b)^4

Let's use the [[introduction_to_the_binomial_theorem | binomial theorem]] to expand `(a + b)^4` <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.
Here, `n = 4`. The sum will run from `k = 0` to `k = 4` <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>.

`(a + b)^4 = (4 choose 0)a^(4-0)b^0 + (4 choose 1)a^(4-1)b^1 + (4 choose 2)a^(4-2)b^2 + (4 choose 3)a^(4-3)b^3 + (4 choose 4)a^(4-4)b^4` <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>

Now, let's calculate each `(n choose k)` coefficient:

*   **For k = 0**: `(4 choose 0)`
    `4! / (0! * (4 - 0)!) = 4! / (1 * 4!) = 1` <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a>
    Term: `1 * a^4 * b^0 = a^4` <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>

*   **For k = 1**: `(4 choose 1)`
    `4! / (1! * (4 - 1)!) = 4! / (1 * 3!) = (4 * 3 * 2 * 1) / (1 * 3 * 2 * 1) = 4` <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>
    Term: `4 * a^3 * b^1 = 4a^3b` <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>

*   **For k = 2**: `(4 choose 2)`
    `4! / (2! * (4 - 2)!) = 4! / (2! * 2!) = (4 * 3 * 2 * 1) / ((2 * 1) * (2 * 1)) = 24 / 4 = 6` <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>
    Term: `6 * a^2 * b^2 = 6a^2b^2` <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>

*   **For k = 3**: `(4 choose 3)`
    `4! / (3! * (4 - 3)!) = 4! / (3! * 1!) = (4 * 3 * 2 * 1) / ((3 * 2 * 1) * 1) = 4` <a class="yt-timestamp" data-t="00:10:59">[00:10:59]</a>
    Term: `4 * a^1 * b^3 = 4ab^3` <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>

*   **For k = 4**: `(4 choose 4)`
    `4! / (4! * (4 - 4)!) = 4! / (4! * 0!) = 4! / (4! * 1) = 1` <a class="yt-timestamp" data-t="00:11:27">[00:11:27]</a>
    Term: `1 * a^0 * b^4 = b^4` <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>

Combining all terms, the full expansion is:
`(a + b)^4 = a^4 + 4a^3b + 6a^2b^2 + 4ab^3 + b^4` <a class="yt-timestamp" data-t="00:11:48">[00:11:48]</a>

## Observed Patterns in Binomial Expansions

When examining the expanded form of `(a + b)^n`, several patterns become evident:

*   **Coefficients**: The coefficients display symmetry. For `(a + b)^4`, they are `1, 4, 6, 4, 1` <a class="yt-timestamp" data-t="00:12:42">[00:12:42]</a>.
*   **Exponent of 'a'**: The power of the first term (`a`) starts at `n` and decreases by 1 in each subsequent term until it reaches 0 <a class="yt-timestamp" data-t="00:12:51">[00:12:51]</a>.
*   **Exponent of 'b'**: The power of the second term (`b`) starts at 0 and increases by 1 in each subsequent term until it reaches `n` <a class="yt-timestamp" data-t="00:12:57">[00:12:57]</a>.