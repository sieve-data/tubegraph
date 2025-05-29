---
title: Understanding binomial distribution and symmetry in probability
videoId: WWv0RUxDfbs
---

From: [[khanacademy]] <br/> 

This article explores the fundamental concepts behind binomial distribution by examining the probabilities of obtaining a certain number of heads when flipping a fair coin multiple times. This process serves as a buildup to understanding the [[Normal distribution | normal distribution]] and [[Properties of probability distributions | probability distribution functions]] <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a> <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>.

## Defining the Random Variable

A random variable, denoted as `x`, converts particular outcomes of an experiment into numbers <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a> <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. In this context, `x` is defined as the number of heads obtained from flipping a fair coin five times <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a> <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. The possible values for `x` are 0, 1, 2, 3, 4, or 5 <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

## Calculating Total Possible Outcomes

To determine the probability of each value of `x`, it's first necessary to identify the total number of unique outcomes from five coin flips <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. For each flip, there are two possibilities: heads (H) or tails (T) <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.
Therefore, for five flips, the total number of equally likely outcomes is calculated as 2 multiplied by itself five times, or 2^5 <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.

This results in:
2 x 2 x 2 x 2 x 2 = 32 total equally likely outcomes <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a> <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.

Examples of outcomes include:
*   Tails, Heads, Tails, Heads, Tails <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>
*   Heads, Heads, Heads, Tails, Tails <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>

## Probabilities for Each Value of `x`

The probability for each value of `x` (number of heads) is determined by finding how many of the 32 total equally likely outcomes result in that specific number of heads, divided by the total number of outcomes. This involves concepts related to [[Introduction to binomial coefficients and combinatorics | binomial coefficients and combinatorics]] <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.

### Probability of x = 0 (No Heads)

This outcome means all five flips are tails (TTTTT). There is only one way to achieve this <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a> <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.
The number of ways to choose 0 heads from 5 flips can be represented using combinations as "5 choose 0" (C(5, 0) or ⁵C₀) <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>.

*   ⁵C₀ = 5! / (0! * (5-0)!) = 5! / (1 * 5!) = 1 <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>
*   P(x=0) = 1/32 <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>

### Probability of x = 1 (One Head)

To get one head, the head can appear in any of the five positions (e.g., HTTTT, THTTT, TTHTT, TTTHT, TTTTH) <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>. There are five such possibilities <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>. This is represented as "5 choose 1" <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.

*   ⁵C₁ = 5! / (1! * (5-1)!) = 5! / (1 * 4!) = 5 <a class="yt-timestamp" data-t="00:06:12">[00:06:12]</a>
*   P(x=1) = 5/32 <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>

### Probability of x = 2 (Two Heads)

This involves choosing 2 positions out of 5 for the heads. This is "5 choose 2" <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>.

*   ⁵C₂ = 5! / (2! * (5-2)!) = 5! / (2! * 3!) = (5 * 4 * 3 * 2 * 1) / ((2 * 1) * (3 * 2 * 1)) = 10 <a class="yt-timestamp" data-t="00:07:46">[00:07:46]</a>
*   P(x=2) = 10/32 <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>

### Probability of x = 3 (Three Heads)

This involves choosing 3 positions out of 5 for the heads. This is "5 choose 3" <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>.

*   ⁵C₃ = 5! / (3! * (5-3)!) = 5! / (3! * 2!) = (5 * 4 * 3 * 2 * 1) / ((3 * 2 * 1) * (2 * 1)) = 10 <a class="yt-timestamp" data-t="00:08:56">[00:08:56]</a>
*   P(x=3) = 10/32 <a class="yt-timestamp" data-t="00:08:59">[00:08:59]</a>

### Probability of x = 4 (Four Heads)

This involves choosing 4 positions out of 5 for the heads. This is "5 choose 4" <a class="yt-timestamp" data-t="00:09:22">[00:09:22]</a>.

*   ⁵C₄ = 5! / (4! * (5-4)!) = 5! / (4! * 1!) = (5 * 4 * 3 * 2 * 1) / ((4 * 3 * 2 * 1) * 1) = 5 <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>
*   P(x=4) = 5/32 <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>

### Probability of x = 5 (Five Heads)

This outcome means all five flips are heads (HHHHH). There is only one way to achieve this <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a> <a class="yt-timestamp" data-t="00:10:36">[00:10:36]</a>. This is represented as "5 choose 5" <a class="yt-timestamp" data-t="00:10:51">[00:10:51]</a>.

*   ⁵C₅ = 5! / (5! * (5-5)!) = 5! / (5! * 0!) = 1 <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>
*   P(x=5) = 1/32 <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>

## Summary of Probabilities and Observed Symmetry

The probabilities for the number of heads (x) from 0 to 5 are:

*   P(x=0) = 1/32
*   P(x=1) = 5/32
*   P(x=2) = 10/32
*   P(x=3) = 10/32
*   P(x=4) = 5/32
*   P(x=5) = 1/32

Notice the clear symmetry in these probabilities: 1, 5, 10, 10, 5, 1 <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a> <a class="yt-timestamp" data-t="00:11:22">[00:11:22]</a>. This symmetry is inherent in binomial distributions for fair coin flips or situations where the probability of success (e.g., getting a head) is 0.5 <a class="yt-timestamp" data-t="00:11:28">[00:11:28]</a>. The probability of getting `k` heads is the same as getting `k` tails. For instance, the probability of getting five heads (zero tails) is the same as getting zero heads (five tails) <a class="yt-timestamp" data-t="00:11:31">[00:11:31]</a> <a class="yt-timestamp" data-t="00:11:35">[00:11:35]</a>. This concept relates to [[Analyzing symmetry in parabolic graphs | analyzing symmetry in parabolic graphs]] which often arise when [[Probability distribution functions | probability distribution functions]] are graphed.

This exercise provides a foundational [[Introduction to binomials and calculating powers | introduction to binomials and calculating powers]] and how [[Calculation of combinations for binomial expansion | calculation of combinations for binomial expansion]] is applied in probability <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>. This distribution can be further visualized graphically to represent the probability distribution for this random variable <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>.