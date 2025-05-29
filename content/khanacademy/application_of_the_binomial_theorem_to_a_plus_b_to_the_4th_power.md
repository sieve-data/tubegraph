---
title: Application of the binomial theorem to a plus b to the 4th power
videoId: iPwrDWQ7hPc
---

From: [[khanacademy]] <br/> 

[[expanding_binomials_using_the_binomial_theorem | Expanding binomials]] to higher powers can become computationally intensive and "painful" <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. The [[introduction_to_the_binomial_theorem | Binomial Theorem]] provides a systematic way to expand such expressions, greatly simplifying the process for higher powers <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.

## Manual Expansion: The Painful Way

To illustrate the increasing complexity, consider the manual expansion of a binomial $(a+b)$ to various powers:

*   **To the 0th power**:
    $(a+b)^0 = 1$ <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>
*   **To the 1st power**:
    $(a+b)^1 = a+b$ <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>
*   **To the 2nd power**:
    $(a+b)^2 = (a+b)(a+b)$ <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>
    This expands to:
    $a \cdot a = a^2$ <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>
    $a \cdot b = ab$ <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>
    $b \cdot a = ab$ <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>
    $b \cdot b = b^2$ <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>
    Combining terms:
    $(a+b)^2 = a^2 + 2ab + b^2$ <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>
    *Note: $(a+b)^2$ is not $a^2 + b^2$ <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.*
*   **To the 3rd power**:
    $(a+b)^3 = (a+b)^2 \cdot (a+b)$ <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>
    Substituting the expansion of $(a+b)^2$:
    $(a^2 + 2ab + b^2)(a+b)$ <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>
    Multiplying term by term:
    $b(b^2) = b^3$ <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>
    $b(2ab) = 2ab^2$ <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>
    $b(a^2) = a^2b$ <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>
    $a(b^2) = ab^2$ <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>
    $a(2ab) = 2a^2b$ <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>
    $a(a^2) = a^3$ <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>
    Adding these results:
    $a^3 + (a^2b + 2a^2b) + (2ab^2 + ab^2) + b^3$ <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>
    $(a+b)^3 = a^3 + 3a^2b + 3ab^2 + b^3$ <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>

As seen, calculating $(a+b)^3$ already takes a reasonable amount of time, suggesting that powers like $(a+b)^{10}$ or $(a+b)^{20}$ would be "incredibly painful" <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.

## The [[introduction_to_the_binomial_theorem | Binomial Theorem]] Formula

The [[introduction_to_the_binomial_theorem | Binomial Theorem]] provides a general formula for [[expanding_binomials_using_the_binomial_theorem | expanding binomials]] of the form $(a+b)^n$:

$(a+b)^n = \sum_{k=0}^{n} \text{n choose k} \cdot a^{n-k} \cdot b^k$ <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>

Where:
*   $n$ is the power to which the binomial is raised <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>.
*   $k$ is an index that ranges from $0$ to $n$ <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>.
*   $\text{n choose k}$ represents a [[binomial_coefficients_and_combinatorics | binomial coefficient]], which is calculated using the formula:
    $\text{n choose k} = \frac{n!}{k!(n-k)!}$ <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>
    (Here, $0!$ is defined as $1$ <a class="yt-timestamp" data-t="00:09:33">[00:09:33]</a>)

## Application to $(a+b)^4$

Let's apply the [[introduction_to_the_binomial_theorem | Binomial Theorem]] to find $(a+b)^4$ <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>. Here, $n=4$.

The formula becomes:
$(a+b)^4 = \sum_{k=0}^{4} \text{4 choose k} \cdot a^{4-k} \cdot b^k$ <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>

We will sum the terms for $k=0, 1, 2, 3, 4$:

*   **For $k=0$**:
    $\text{4 choose 0} \cdot a^{4-0} \cdot b^0$ <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>
    $\text{4 choose 0} = \frac{4!}{0!(4-0)!} = \frac{4!}{1 \cdot 4!} = 1$ <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a> to <a class="yt-timestamp" data-t="00:09:38">[00:09:38]</a>
    Term: $1 \cdot a^4 \cdot 1 = a^4$ <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>
*   **For $k=1$**:
    $\text{4 choose 1} \cdot a^{4-1} \cdot b^1$ <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>
    $\text{4 choose 1} = \frac{4!}{1!(4-1)!} = \frac{4!}{1 \cdot 3!} = \frac{4 \cdot 3!}{1 \cdot 3!} = 4$ <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a> to <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>
    Term: $4 \cdot a^3 \cdot b = 4a^3b$ <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>
*   **For $k=2$**:
    $\text{4 choose 2} \cdot a^{4-2} \cdot b^2$ <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>
    $\text{4 choose 2} = \frac{4!}{2!(4-2)!} = \frac{4!}{2! \cdot 2!} = \frac{4 \cdot 3 \cdot 2 \cdot 1}{(2 \cdot 1)(2 \cdot 1)} = \frac{24}{4} = 6$ <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a> to <a class="yt-timestamp" data-t="00:10:52">[00:10:52]</a>
    Term: $6 \cdot a^2 \cdot b^2 = 6a^2b^2$ <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>
*   **For $k=3$**:
    $\text{4 choose 3} \cdot a^{4-3} \cdot b^3$ <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>
    $\text{4 choose 3} = \frac{4!}{3!(4-3)!} = \frac{4!}{3! \cdot 1!} = \frac{4 \cdot 3!}{3! \cdot 1} = 4$ <a class="yt-timestamp" data-t="00:10:59">[00:10:59]</a> to <a class="yt-timestamp" data-t="00:11:23">[00:11:23]</a>
    Term: $4 \cdot a^1 \cdot b^3 = 4ab^3$ <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>
*   **For $k=4$**:
    $\text{4 choose 4} \cdot a^{4-4} \cdot b^4$ <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>
    $\text{4 choose 4} = \frac{4!}{4!(4-4)!} = \frac{4!}{4! \cdot 0!} = \frac{4!}{4! \cdot 1} = 1$ <a class="yt-timestamp" data-t="00:11:27">[00:11:27]</a> to <a class="yt-timestamp" data-t="00:11:40">[00:11:40]</a>
    Term: $1 \cdot a^0 \cdot b^4 = b^4$ <a class="yt-timestamp" data-t="00:08:55">[00:08:55]</a>

Adding all terms together:
$(a+b)^4 = a^4 + 4a^3b + 6a^2b^2 + 4ab^3 + b^4$ <a class="yt-timestamp" data-t="00:11:57">[00:11:57]</a>

### [[patterns_and_symmetry_in_binomial_expansions | Patterns and Symmetry]]

When examining the expansion of $(a+b)^4$, several [[patterns_and_symmetry_in_binomial_expansions | patterns]] emerge:
*   **Coefficients**: The coefficients follow a symmetric pattern: 1, 4, 6, 4, 1 <a class="yt-timestamp" data-t="00:12:42">[00:12:42]</a>.
*   **Exponents of 'a'**: The power of 'a' starts at $n$ (here, 4) and decreases by 1 in each subsequent term, ending at 0: $a^4, a^3, a^2, a^1, a^0$ (implied) <a class="yt-timestamp" data-t="00:12:51">[00:12:51]</a>.
*   **Exponents of 'b'**: The power of 'b' starts at 0 (implied) and increases by 1 in each subsequent term, ending at $n$ (here, 4): $b^0$ (implied), $b^1, b^2, b^3, b^4$ <a class="yt-timestamp" data-t="00:12:57">[00:12:57]</a>.
*   **Sum of Exponents**: In every term, the sum of the exponents of 'a' and 'b' always equals $n$ (here, 4) <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>. For example, in $a^3b^1$, $3+1=4$.