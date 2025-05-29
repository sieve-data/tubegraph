---
title: Introduction to the binomial theorem
videoId: iPwrDWQ7hPc
---

From: [[khanacademy]] <br/> 

Expanding [[introduction_to_binomials_and_calculating_powers | powers of binomials]] can quickly become a "painful" and time-consuming process as the power increases <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>.

## Expanding Binomials Manually

Let's look at a few examples of expanding the binomial `a + b`:

*   **(a + b)⁰**: Any non-zero term raised to the 0 power equals 1 <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>.
    *   `(a + b)⁰ = 1` <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>
*   **(a + b)¹**: This simply equals `a + b` <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>.
*   **(a + b)²**: It is a common [[misconceptions_about_expanding_binomials | misconception]] that `(a + b)²` is equal to `a² + b²` <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>. However, this is incorrect <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.
    *   `(a + b)² = (a + b) * (a + b)` <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>
    *   Expanding this multiplication yields: `a*a + a*b + b*a + b*b` <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.
    *   Combining like terms (`ab` and `ba` are both `ab`) results in: `a² + 2ab + b²` <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>.
*   **(a + b)³**: This can be found by multiplying `(a + b)²` by `(a + b)` <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>.
    *   `(a² + 2ab + b²) * (a + b)` <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>
    *   The [[stepbystep_process_of_expanding_binomials | step-by-step process]] of multiplication yields:
        *   `b * (b²)` = `b³` <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>
        *   `b * (2ab)` = `2ab²` <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>
        *   `b * (a²)` = `a²b` <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>
        *   `a * (b²)` = `ab²` <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>
        *   `a * (2ab)` = `2a²b` <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>
        *   `a * (a²)` = `a³` <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>
    *   Adding these terms together: `a³ + 3a²b + 3ab² + b³` <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.
    *   Even for the third power, this manual process takes a "reasonable amount of time" <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>. Expanding to higher powers like the 10th or 20th power would be "incredibly painful" <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.

## The Binomial Theorem

The [[introduction_to_binomial_coefficients_and_combinatorics | binomial theorem]] provides a formula to expand binomials raised to any power `n` <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.

### Formula
The binomial theorem states that for a binomial `(a + b)` raised to the `nth` power:

`(a + b)ⁿ = Σ (from k=0 to n) [ (n choose k) * a^(n-k) * b^k ]` <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>

Where:
*   `n` is the power to which the binomial is raised <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.
*   `k` is an index that goes from 0 to `n` <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>.
*   `(n choose k)` is a binomial coefficient, which comes from [[introduction_to_binomial_coefficients_and_combinatorics | combinatorics]] <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>.

### Understanding `n choose k`
The term `(n choose k)` is calculated as:

`(n choose k) = n! / (k! * (n - k)!)` <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>

Where `!` denotes factorial (e.g., `4! = 4 * 3 * 2 * 1`) <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>. By definition, `0! = 1` <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.

## Example: Expanding (a + b)⁴

Let's use the binomial theorem to expand `(a + b)⁴` <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>. Here, `n = 4` <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>.

The expansion will be the sum of terms for `k` from 0 to 4:
`Σ (from k=0 to 4) [ (4 choose k) * a^(4-k) * b^k ]` <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>

1.  **k = 0**:
    *   Coefficient: `(4 choose 0) = 4! / (0! * 4!) = 1` <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a>.
    *   Term: `1 * a^(4-0) * b^0 = 1 * a⁴ * 1 = a⁴` <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.

2.  **k = 1**:
    *   Coefficient: `(4 choose 1) = 4! / (1! * 3!) = (4 * 3 * 2 * 1) / (1 * 3 * 2 * 1) = 4` <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>.
    *   Term: `4 * a^(4-1) * b^1 = 4a³b` <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>.

3.  **k = 2**:
    *   Coefficient: `(4 choose 2) = 4! / (2! * 2!) = (4 * 3 * 2 * 1) / (2 * 1 * 2 * 1) = 6` <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>.
    *   Term: `6 * a^(4-2) * b^2 = 6a²b²` <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>.

4.  **k = 3**:
    *   Coefficient: `(4 choose 3) = 4! / (3! * 1!) = 4` <a class="yt-timestamp" data-t="00:10:59">[00:10:59]</a>. (This is symmetric to `(4 choose 1)`) <a class="yt-timestamp" data-t="00:11:15">[00:11:15]</a>.
    *   Term: `4 * a^(4-3) * b^3 = 4ab³` <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>.

5.  **k = 4**:
    *   Coefficient: `(4 choose 4) = 4! / (4! * 0!) = 1` <a class="yt-timestamp" data-t="00:11:27">[00:11:27]</a>. (This is symmetric to `(4 choose 0)`) <a class="yt-timestamp" data-t="00:11:39">[00:11:39]</a>.
    *   Term: `1 * a^(4-4) * b^4 = 1 * a⁰ * b⁴ = b⁴` <a class="yt-timestamp" data-t="00:08:55">[00:08:55]</a>.

### Final Expansion of (a + b)⁴

Adding all the terms together:

`(a + b)⁴ = a⁴ + 4a³b + 6a²b² + 4ab³ + b⁴` <a class="yt-timestamp" data-t="00:12:00">[00:12:00]</a>

## Observed Patterns and [[understanding_binomial_distribution_and_symmetry_in_probability | Symmetry]]

When expanding binomials using the theorem, several patterns become apparent:

*   **Coefficients**: The coefficients display [[understanding_binomial_distribution_and_symmetry_in_probability | symmetry]]. For `(a + b)⁴`, they are 1, 4, 6, 4, 1 <a class="yt-timestamp" data-t="00:12:41">[00:12:41]</a>.
*   **Powers of `a`**: The power of the first term (`a`) starts at `n` and decreases by one in each subsequent term, ending at 0 (e.g., `a⁴, a³, a², a¹, a⁰`) <a class="yt-timestamp" data-t="00:12:51">[00:12:51]</a>.
*   **Powers of `b`**: The power of the second term (`b`) starts at 0 and increases by one in each subsequent term, ending at `n` (e.g., `b⁰, b¹, b², b³, b⁴`) <a class="yt-timestamp" data-t="00:12:57">[00:12:57]</a>.
*   **Sum of Powers**: In each term, the sum of the exponents of `a` and `b` always equals `n` (e.g., for `a³b¹`, `3+1=4`) <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.

The binomial theorem significantly simplifies the process of expanding binomials to higher powers, leveraging principles from [[introduction_to_binomial_coefficients_and_combinatorics | combinatorics]] for its coefficients.