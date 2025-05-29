---
title: Using the binomial theorem for higher powers
videoId: iPwrDWQ7hPc
---

From: [[khanacademy]] <br/> 

[[calculating_powers_of_binomials | Calculating higher and higher powers of binomials]] can become challenging and time-consuming <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. The binomial theorem offers a systematic way to expand these expressions efficiently <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.

## Manual Expansion Examples

To illustrate the difficulty of manual expansion, consider a few simple cases:

*   **(a + b)⁰**: Any non-zero base raised to the power of 0 equals 1 <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>.
    `(a + b)⁰ = 1` <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>

*   **(a + b)¹**: Raising a binomial to the power of 1 results in the binomial itself <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.
    `(a + b)¹ = a + b` <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>

*   **(a + b)²**: A [[common_misconceptions_with_binomial_expansions | common misconception]] is to assume `(a + b)²` equals `a² + b²` <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>. This is incorrect <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. The correct expansion requires multiplying the binomial by itself <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>:
    `(a + b)² = (a + b) * (a + b)` <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>
    Applying [[binomial_products | binomial products]] (FOIL method):
    `= a*a + a*b + b*a + b*b` <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>
    `= a² + ab + ab + b²` <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>
    `= a² + 2ab + b²` <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>

*   **(a + b)³**: To expand this, one can multiply `(a + b)²` by `(a + b)` <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>.
    Using `(a² + 2ab + b²) * (a + b)`:
    `= b * b² + b * 2ab + b * a²` <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>
    `= b³ + 2ab² + a²b` <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>
    `+ a * b² + a * 2ab + a * a²` <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>
    `+ ab² + 2a²b + a³` <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>
    Combining like terms:
    `= a³ + (a²b + 2a²b) + (2ab² + ab²) + b³` <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>
    `= a³ + 3a²b + 3ab² + b³` <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>

As the power increases (e.g., to the 4th, 10th, or 20th power), manual expansion becomes incredibly painful and time-consuming <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.

## The Binomial Theorem

The [[binomial_distribution | binomial theorem]] provides a formula for expanding `(a + b)` to the `nth` power <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>:

`(a + b)ⁿ = Σ (from k=0 to n) [ (n choose k) * a^(n-k) * b^k ]` <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>

Where:
*   `n` is the power to which the binomial is raised <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.
*   `k` is an index that ranges from 0 to `n` <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>.
*   `(n choose k)` represents the binomial coefficient, which is calculated using [[combinatorics_and_factorials | factorials]] <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>.

### Understanding "n choose k"

The "n choose k" notation, also written as `(n k)`, comes from [[combinatorics_and_factorials | combinatorics]] <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>. It is defined as:

`(n choose k) = n! / (k! * (n - k)!)` <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>

For this formula, 0 factorial (`0!`) is defined as 1 <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.

## Applying the Binomial Theorem: (a + b)⁴

Let's apply the binomial theorem to expand `(a + b)⁴` <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>:

`(a + b)⁴ = Σ (from k=0 to 4) [ (4 choose k) * a^(4-k) * b^k ]` <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>

We expand the sum by evaluating each term for k = 0, 1, 2, 3, and 4.

### Calculating Coefficients

1.  **k = 0**: `(4 choose 0)`
    `= 4! / (0! * (4-0)!) = 4! / (1 * 4!) = 1` <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a>
    Term: `1 * a^(4-0) * b^0 = a⁴` <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>

2.  **k = 1**: `(4 choose 1)`
    `= 4! / (1! * (4-1)!) = 4! / (1 * 3!) = (4 * 3 * 2 * 1) / (3 * 2 * 1) = 4` <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>
    Term: `4 * a^(4-1) * b^1 = 4a³b` <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>

3.  **k = 2**: `(4 choose 2)`
    `= 4! / (2! * (4-2)!) = 4! / (2! * 2!) = (4 * 3 * 2 * 1) / ((2 * 1) * (2 * 1)) = 24 / 4 = 6` <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>
    Term: `6 * a^(4-2) * b^2 = 6a²b²` <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>

4.  **k = 3**: `(4 choose 3)`
    `= 4! / (3! * (4-3)!) = 4! / (3! * 1!) = (4 * 3 * 2 * 1) / ((3 * 2 * 1) * 1) = 4` <a class="yt-timestamp" data-t="00:10:59">[00:10:59]</a>
    Term: `4 * a^(4-3) * b^3 = 4ab³` <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>

5.  **k = 4**: `(4 choose 4)`
    `= 4! / (4! * (4-4)!) = 4! / (4! * 0!) = 4! / (4! * 1) = 1` <a class="yt-timestamp" data-t="00:11:27">[00:11:27]</a>
    Term: `1 * a^(4-4) * b^4 = b⁴` <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>

### Final Expansion

Adding all the terms together gives the full expansion:

`(a + b)⁴ = a⁴ + 4a³b + 6a²b² + 4ab³ + b⁴` <a class="yt-timestamp" data-t="00:11:58">[00:11:58]</a>

## [[patterns_in_binomial_expansions | Patterns in Binomial Expansions]]

Observing the expansion `a⁴ + 4a³b + 6a²b² + 4ab³ + b⁴`, several [[patterns_in_binomial_expansions | patterns]] emerge:

*   **Coefficients**: The coefficients (`1, 4, 6, 4, 1`) exhibit [[symmetry_in_binomial_probabilities | symmetry]] <a class="yt-timestamp" data-t="00:12:42">[00:12:42]</a>. This pattern forms [[Pascal's triangle]] and is directly derived from `(n choose k)`.
*   **Exponents of 'a'**: The power of 'a' starts at `n` (4 in this case) and decreases by 1 in each subsequent term (`a⁴, a³, a², a¹, a⁰`) <a class="yt-timestamp" data-t="00:12:51">[00:12:51]</a>.
*   **Exponents of 'b'**: The power of 'b' starts at 0 and increases by 1 in each subsequent term (`b⁰, b¹, b², b³, b⁴`) <a class="yt-timestamp" data-t="00:12:57">[00:12:57]</a>.
*   **Sum of Exponents**: In each term, the sum of the exponents of `a` and `b` always equals `n` (e.g., `4+0=4`, `3+1=4`, `2+2=4`, `1+3=4`, `0+4=4`).

The binomial theorem simplifies the process of [[understanding_exponents | understanding exponents]] in binomial expansions, making it feasible to calculate even very high powers efficiently <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.