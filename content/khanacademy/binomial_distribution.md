---
title: Binomial distribution
videoId: WWv0RUxDfbs
---

From: [[khanacademy]] <br/> 

The binomial distribution models the number of successes in a fixed number of independent Bernoulli trials. The example provided uses coin flips to illustrate its principles <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.

## Defining the Random Variable

A random variable, denoted as `x`, can be defined as the number of heads obtained from flipping a fair coin five times <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>.
*   Since the coin is flipped five times, the possible values for `x` (number of heads) are 0, 1, 2, 3, 4, or 5 <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

## Total Possible Outcomes

When flipping a fair coin five times, each flip has two possible outcomes (heads or tails) <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. Therefore, the total number of equally likely outcomes is calculated as 2 multiplied by itself five times (2 x 2 x 2 x 2 x 2), which is 2<sup>5</sup> = 32 <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.

For example, possible outcomes include:
*   Tails, Heads, Tails, Heads, Tails <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>
*   Heads, Heads, Heads, Tails, Tails <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>

## Calculating Probabilities

The [[Probability calculation | probability]] for each value of the random variable `x` is determined by dividing the number of ways to achieve that outcome by the total number of equally likely outcomes (32) <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>. This involves using [[Binomial coefficients and combinatorics | binomial coefficients]], which count the number of ways to choose a certain number of successes (heads) from a set number of trials (flips) <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.

### P(X=0): Probability of Zero Heads

There is only one way to get zero heads (all tails) <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.
*   Using [[Binomial coefficients and combinatorics | combinatorics]]: 5 choose 0 (C(5,0)) = 1 <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>.
*   Probability: P(x=0) = 1/32 <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.

### P(X=1): Probability of One Head

There are five possible positions for a single head to occur among the five flips <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
*   Using [[Binomial coefficients and combinatorics | combinatorics]]: 5 choose 1 (C(5,1)) = 5 <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.
*   Probability: P(x=1) = 5/32 <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>.

### P(X=2): Probability of Two Heads

The number of ways to get two heads from five flips is calculated using [[Binomial coefficients and combinatorics | combinatorics]]:
*   5 choose 2 (C(5,2)) = 5! / (2! * (5-2)!) = (5 * 4 * 3 * 2 * 1) / ((2 * 1) * (3 * 2 * 1)) = 120 / (2 * 6) = 10 <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>.
*   Probability: P(x=2) = 10/32 <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>.

### P(X=3): Probability of Three Heads

The number of ways to get three heads from five flips is calculated using [[Binomial coefficients and combinatorics | combinatorics]]:
*   5 choose 3 (C(5,3)) = 5! / (3! * (5-3)!) = (5 * 4 * 3 * 2 * 1) / ((3 * 2 * 1) * (2 * 1)) = 120 / (6 * 2) = 10 <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>.
*   Probability: P(x=3) = 10/32 <a class="yt-timestamp" data-t="00:08:59">[00:08:59]</a>.

### P(X=4): Probability of Four Heads

The number of ways to get four heads from five flips is calculated using [[Binomial coefficients and combinatorics | combinatorics]]:
*   5 choose 4 (C(5,4)) = 5! / (4! * (5-4)!) = (5 * 4 * 3 * 2 * 1) / ((4 * 3 * 2 * 1) * (1)) = 5 <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a>.
*   Probability: P(x=4) = 5/32 <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>. This is intuitively similar to getting one tail, as there are five positions for that single tail <a class="yt-timestamp" data-t="00:10:19">[00:10:19]</a>.

### P(X=5): Probability of Five Heads

There is only one way to get five heads (all heads) <a class="yt-timestamp" data-t="00:10:30">[00:10:30]</a>.
*   Using [[Binomial coefficients and combinatorics | combinatorics]]: 5 choose 5 (C(5,5)) = 5! / (5! * (5-5)!) = 1 <a class="yt-timestamp" data-t="00:11:05">[00:11:05]</a>.
*   Probability: P(x=5) = 1/32 <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>.

## Symmetry in Probabilities

The probabilities calculated demonstrate a [[Symmetry in probability distributions | symmetry]]:
*   P(x=0) = 1/32
*   P(x=1) = 5/32
*   P(x=2) = 10/32
*   P(x=3) = 10/32
*   P(x=4) = 5/32
*   P(x=5) = 1/32

This [[Symmetry in probability distributions | symmetry]] occurs because the [[Probability calculation | probability]] of getting a certain number of heads is the same as the [[Probability calculation | probability]] of getting the corresponding number of tails (e.g., 0 heads is 5 tails, 5 heads is 0 tails) <a class="yt-timestamp" data-t="00:11:22">[00:11:22]</a>. The sum of these probabilities is 1 + 5 + 10 + 10 + 5 + 1 = 32, so 32/32 = 1.

The organization of these probabilities for a random variable forms a [[Probability Distribution Functions | probability distribution function]], often visualized as a histogram or bar chart, which for a binomial distribution will show this characteristic [[Symmetry in probability distributions | symmetry]] <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>.