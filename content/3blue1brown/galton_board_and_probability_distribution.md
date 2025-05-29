---
title: Galton board and probability distribution
videoId: zeJD6dqJ5lo
---

From: [[3blue1brown]] <br/> 

The Galton board, also known as a bean machine, is a popular demonstration illustrating how, despite individual events being chaotic and random, it's possible to make precise statements about a large number of such events <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. Specifically, it shows how the relative proportions for many different outcomes are distributed <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>.

## Connection to the Normal Distribution

The Galton board demonstrates one of the most prominent distributions in probability: the normal distribution <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. This is also known as a bell curve or a [[connection_between_gaussian_distribution_and_probability | Gaussian distribution]] <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. The normal distribution is exceptionally common and appears in many seemingly unrelated contexts, such as the heights of people within a similar demographic or the number of distinct prime factors in large natural numbers <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.

The underlying principle explaining the prevalence of the normal distribution is the Central Limit Theorem <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.

## Simplified Model of the Galton Board

To illustrate the Central Limit Theorem, a simplified model of the Galton board is often used <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>. In this model:
*   Each ball falls directly onto a central peg <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.
*   It has a 50-50 [[probability_density_and_distribution | probability]] of bouncing to the left or to the right <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>.
*   Bouncing left is considered subtracting one from its position, and bouncing right is adding one <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.
*   An unrealistic assumption is made that the ball lands precisely in the middle of the adjacent peg below it after each bounce <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.

For a Galton board with five rows of pegs, a ball makes five different random choices (+1 or -1) <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>. Its final position is essentially the sum of these five numbers <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>. By repeating this process with many balls, the number of balls in each bucket gives a sense of the likelihood for each final position <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>. The explicit calculation of these probabilities can be reminiscent of Pascal's triangle <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.

While this is an idealized model and does not accurately reflect physics, its goal is to provide a simple example to illustrate the Central Limit Theorem <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>. [[simulation_examples_of_probability_distribution | Simulations]] can be run to observe the emerging distribution <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>.

### Galton Board and the Central Limit Theorem

The core idea of the Central Limit Theorem, as illustrated by the Galton board, is that if the "size of the sum" (e.g., the number of rows of pegs a ball bounces off) increases, the distribution describing where that sum will fall looks increasingly like a bell curve <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>. This applies even if the initial random variable (like the 50-50 bounce) is very simple.

A random variable is a random process where each outcome is associated with a number <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>. In the Galton board, each bounce is a random variable with outcomes -1 or +1 <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>. The final position of the ball is the sum of multiple samples of this variable <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>. The theorem states that as the number of samples in the sum grows, the distribution of that sum converges to a bell curve <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.

## Assumptions of the Central Limit Theorem vs. the Real Galton Board

The Central Limit Theorem relies on three key assumptions:
1.  **Independence**: All the variables being added are independent of each other. The outcome of one process does not influence others <a class="yt-timestamp" data-t="00:28:18">[00:28:18]</a>.
2.  **Identically Distributed**: All variables are drawn from the same distribution <a class="yt-timestamp" data-t="00:28:27">[00:28:27]</a>. These first two assumptions are often grouped as "IID" (independent and identically distributed) <a class="yt-timestamp" data-t="00:28:42">[00:28:42]</a>.
3.  **Finite Variance**: The variance of the variables must be finite <a class="yt-timestamp" data-t="00:30:06">[00:30:06]</a>.

However, the real Galton board violates the first two assumptions <a class="yt-timestamp" data-t="00:28:50">[00:28:50]</a>.
*   The way a ball bounces off one peg *is not independent* from how it bounces off the next, as its trajectory changes <a class="yt-timestamp" data-t="00:28:56">[00:28:56]</a>.
*   The distribution of possible outcomes off each peg is *not necessarily the same* for each peg, as a glancing hit might skew probabilities <a class="yt-timestamp" data-t="00:29:08">[00:29:08]</a>.

Despite these violations, a normal distribution often *does* appear on a real Galton board <a class="yt-timestamp" data-t="00:29:38">[00:29:38]</a>. This might be partly due to generalizations of the theorem that relax these assumptions <a class="yt-timestamp" data-t="00:29:46">[00:29:46]</a>. However, it serves as a caution that one should not simply assume a variable is normally distributed without justification <a class="yt-timestamp" data-t="00:29:54">[00:29:54]</a>.