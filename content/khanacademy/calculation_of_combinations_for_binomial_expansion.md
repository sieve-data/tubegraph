---
title: Calculation of combinations for binomial expansion
videoId: iPwrDWQ7hPc
---

From: [[khanacademy]] <br/> 

Expanding [[introduction_to_binomials_and_calculating_powers | binomials]] to higher powers can become very complex and time-consuming quickly <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. For example, while `(a+b)^0 = 1` <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a> and `(a+b)^1 = a+b` <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a> are straightforward, `(a+b)^2` is `a^2 + 2ab + b^2` <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>, not simply `a^2 + b^2` <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. Expanding `(a+b)^3` results in `a^3 + 3a^2b + 3ab^2 + b^3` <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>, and pursuing even higher powers like `(a+b)^10` or `(a+b)^20` would be "incredibly painful" <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.

This is where the [[introduction_to_the_binomial_theorem | binomial theorem]] proves useful <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.

## The Binomial Theorem Formula

The [[introduction_to_the_binomial_theorem | binomial theorem]] provides a formula for expanding a [[introduction_to_binomials_and_calculating_powers | binomial]] `(a + b)` raised to the `n`th power <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>:

$$
(a + b)^n = \sum_{k=0}^{n} \binom{n}{k} a^{n-k} b^k
$$ <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>

Here, `n` is the power to which the [[introduction_to_binomials_and_calculating_powers | binomial]] is raised <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>, and `k` is an index that starts at 0 and goes up to `n` <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>. The term $\binom{n}{k}$ is known as "n choose k" and is derived from [[introduction_to_binomial_coefficients_and_combinatorics | combinatorics]] <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>.

### Understanding "n choose k"

The "n choose k" coefficient, written as $\binom{n}{k}$, is calculated using factorials <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>:

$$
\binom{n}{k} = \frac{n!}{k!(n-k)!}
$$ <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>

It's important to note that 0 factorial (0!) is defined as 1 for these calculations <a class="yt-timestamp" data-t="00:09:33">[00:09:33]</a>.

## Applying the Binomial Theorem: An Example

Let's apply the [[introduction_to_the_binomial_theorem | binomial theorem]] to expand `(a + b)^4` <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.

Using the formula, `n` is 4, so the expansion will be the sum from `k=0` to `k=4` <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>:

$$
(a + b)^4 = \sum_{k=0}^{4} \binom{4}{k} a^{4-k} b^k
$$ <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>

This expands to:

*   **For k = 0**:
    $\binom{4}{0} a^{4-0} b^0 = \binom{4}{0} a^4 b^0$ <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>
    Calculation of $\binom{4}{0}$: $\frac{4!}{0!(4-0)!} = \frac{4!}{1 \cdot 4!} = 1$ <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a>
    Term: $1a^4$ <a class="yt-timestamp" data-t="00:11:48">[00:11:48]</a>

*   **For k = 1**:
    $\binom{4}{1} a^{4-1} b^1 = \binom{4}{1} a^3 b^1$ <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>
    Calculation of $\binom{4}{1}$: $\frac{4!}{1!(4-1)!} = \frac{4!}{1 \cdot 3!} = \frac{4 \times 3 \times 2 \times 1}{1 \times (3 \times 2 \times 1)} = 4$ <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>
    Term: $4a^3b$ <a class="yt-timestamp" data-t="00:11:48">[00:11:48]</a>

*   **For k = 2**:
    $\binom{4}{2} a^{4-2} b^2 = \binom{4}{2} a^2 b^2$ <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>
    Calculation of $\binom{4}{2}$: $\frac{4!}{2!(4-2)!} = \frac{4!}{2! \cdot 2!} = \frac{4 \times 3 \times 2 \times 1}{(2 \times 1)(2 \times 1)} = \frac{24}{4} = 6$ <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>
    Term: $6a^2b^2$ <a class="yt-timestamp" data-t="00:11:52">[00:11:52]</a>

*   **For k = 3**:
    $\binom{4}{3} a^{4-3} b^3 = \binom{4}{3} a^1 b^3$ <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>
    Calculation of $\binom{4}{3}$: $\frac{4!}{3!(4-3)!} = \frac{4!}{3! \cdot 1!} = \frac{4 \times 3 \times 2 \times 1}{(3 \times 2 \times 1)(1)} = 4$ <a class="yt-timestamp" data-t="00:10:59">[00:10:59]</a>
    Term: $4ab^3$ <a class="yt-timestamp" data-t="00:11:54">[00:11:54]</a>

*   **For k = 4**:
    $\binom{4}{4} a^{4-4} b^4 = \binom{4}{4} a^0 b^4$ <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>
    Calculation of $\binom{4}{4}$: $\frac{4!}{4!(4-4)!} = \frac{4!}{4! \cdot 0!} = \frac{4!}{4! \cdot 1} = 1$ <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>
    Term: $1b^4$ <a class="yt-timestamp" data-t="00:11:56">[00:11:56]</a>

Summing these terms yields the full expansion of `(a + b)^4`:

$$
(a + b)^4 = a^4 + 4a^3b + 6a^2b^2 + 4ab^3 + b^4
$$ <a class="yt-timestamp" data-t="00:12:00">[00:12:00]</a>

## Observed Patterns

When expanding [[introduction_to_binomials_and_calculating_powers | binomials]] using this method, several patterns emerge:

*   **Coefficient Symmetry**: The coefficients demonstrate a symmetrical pattern (e.g., 1, 4, 6, 4, 1 for `n=4`) <a class="yt-timestamp" data-t="00:12:42">[00:12:42]</a>.
*   **Powers of `a`**: The power of `a` decreases by one in each successive term, starting from `n` down to 0 (e.g., $a^4, a^3, a^2, a^1, a^0$) <a class="yt-timestamp" data-t="00:12:51">[00:12:51]</a>.
*   **Powers of `b`**: The power of `b` increases by one in each successive term, starting from 0 up to `n` (e.g., $b^0, b^1, b^2, b^3, b^4$) <a class="yt-timestamp" data-t="00:12:57">[00:12:57]</a>.

This method greatly simplifies the [[stepbystep_process_of_expanding_binomials | step-by-step process of expanding binomials]] for higher powers, avoiding the tedious manual multiplication <a class="yt-timestamp" data-t="00:13:08">[00:13:08]</a>.