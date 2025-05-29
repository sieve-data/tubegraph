---
title: Introduction to binomial coefficients and combinatorics
videoId: WWv0RUxDfbs
---

From: [[khanacademy]] <br/> 

This article explores the use of binomial coefficients and combinatorics to calculate probabilities in scenarios involving repeated independent trials, such as coin flips. This understanding serves as a foundational step toward comprehending [[understanding_binomial_distribution_and_symmetry_in_probability | binomial distribution]].

## Defining the Random Variable and Total Outcomes

To illustrate, we define a [[introduction_to_variables | random variable]] `x` as the number of heads obtained from flipping a fair coin five times <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This [[introduction_to_variables | random variable]] can take on integer values from zero (no heads) to five (all heads) <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

To determine the probability of each outcome, we first need to calculate the total number of possible outcomes from flipping a coin five times <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. Since each flip has two possibilities (heads or tails), and there are five flips, the total number of equally likely outcomes is 2 raised to the power of 5:
`2 x 2 x 2 x 2 x 2 = 2^5 = 32` <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.

Examples of possible outcomes include "tails, heads, tails, heads, tails" or "heads, heads, heads, tails, tails" <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.

## Calculating Probabilities Using Combinatorics

We calculate the probability for each possible value of `x` by finding the number of ways to achieve that specific outcome and dividing by the total number of outcomes (32). Combinatorics, specifically the "n choose k" formula (often written as C(n, k) or (n k)), is used to determine the number of ways to select `k` items from a set of `n` items without regard to the order of selection.

The formula for "n choose k" is:
`C(n, k) = n! / (k! * (n-k)!)`

In our case, `n` is the total number of flips (5), and `k` is the number of heads we are choosing to obtain.

### Probability of `x = 0` (Zero Heads)

This outcome means all five flips are tails (TTTTT) <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.
*   **Combinations:** ⁵C₀ (5 choose 0) <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>
    `⁵C₀ = 5! / (0! * (5-0)!) = 5! / (1 * 5!) = 1` <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>
*   **Probability:** `1/32` <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>

### Probability of `x = 1` (One Head)

There are five possible positions for the single head (e.g., HTTTT, THTTT, etc.) <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
*   **Combinations:** ⁵C₁ (5 choose 1) <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>
    `⁵C₁ = 5! / (1! * (5-1)!) = 5! / (1 * 4!) = 5` <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>
*   **Probability:** `5/32` <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>

### Probability of `x = 2` (Two Heads)

*   **Combinations:** ⁵C₂ (5 choose 2) <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>
    `⁵C₂ = 5! / (2! * (5-2)!) = 5! / (2! * 3!) = (5 * 4 * 3 * 2 * 1) / ((2 * 1) * (3 * 2 * 1)) = 10` <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>
*   **Probability:** `10/32` <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>

### Probability of `x = 3` (Three Heads)

*   **Combinations:** ⁵C₃ (5 choose 3) <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>
    `⁵C₃ = 5! / (3! * (5-3)!) = 5! / (3! * 2!) = 10` <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>
*   **Probability:** `10/32` <a class="yt-timestamp" data-t="00:08:59">[00:08:59]</a>

### Probability of `x = 4` (Four Heads)

*   **Combinations:** ⁵C₄ (5 choose 4) <a class="yt-timestamp" data-t="00:09:22">[00:09:22]</a>
    `⁵C₄ = 5! / (4! * (5-4)!) = 5! / (4! * 1!) = 5` <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a>
*   **Probability:** `5/32` <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>

### Probability of `x = 5` (Five Heads)

This outcome means all five flips are heads (HHHHH) <a class="yt-timestamp" data-t="00:10:48">[00:10:48]</a>.
*   **Combinations:** ⁵C₅ (5 choose 5) <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>
    `⁵C₅ = 5! / (5! * (5-5)!) = 5! / (5! * 0!) = 1` <a class="yt-timestamp" data-t="00:11:05">[00:11:05]</a>
*   **Probability:** `1/32` <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>

## Symmetry in Probabilities

Observing the calculated probabilities reveals a symmetry:
*   P(x=0) = 1/32
*   P(x=1) = 5/32
*   P(x=2) = 10/32
*   P(x=3) = 10/32
*   P(x=4) = 5/32
*   P(x=5) = 1/32

This symmetry occurs because the probability of getting `k` heads is the same as the probability of getting `k` tails. For example, getting five heads (P(x=5)) is equivalent to getting zero tails, and getting zero heads (P(x=0)) is equivalent to getting five tails <a class="yt-timestamp" data-t="00:11:31">[00:11:31]</a>. Similarly, getting four heads means getting one tail, which has the same probability as getting one head (four tails) <a class="yt-timestamp" data-t="00:10:13">[00:10:13]</a>.

The sum of all probabilities should equal 1:
`1/32 + 5/32 + 10/32 + 10/32 + 5/32 + 1/32 = 32/32 = 1`

This approach lays the groundwork for [[understanding_binomial_distribution_and_symmetry_in_probability | understanding binomial distribution]] and its characteristic symmetrical probability distribution, particularly in cases with a 50% success rate (like a fair coin flip).