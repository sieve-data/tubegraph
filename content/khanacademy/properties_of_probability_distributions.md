---
title: Properties of probability distributions
videoId: Fvi9A_tEmXQ
---

From: [[khanacademy]] <br/> 

This article explores the key properties of [[probability_distribution_functions | probability distribution functions]] and [[probability_density_functions | probability density functions]], focusing on how they relate to discrete and continuous [[random_variables_overview | random variables]].

## Overview of Random Variables
Previously, we were introduced to the notion of the [[random_variables_overview | random variable]] and its two main types:
*   **Discrete Random Variables**: These take on a finite number of values <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. While they often tend to be integers, they don't always have to be <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. A key characteristic is that they cannot have an infinite number of values <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>.
*   **Continuous Random Variables**: These can take on an infinite number of values <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. An example is the exact amount of rain tomorrow, denoted as a capital letter, e.g., Y <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.

## Probability Density Functions for Continuous Random Variables
For continuous [[random_variables_overview | random variables]], we use a [[probability_density_functions | probability density function]] to interpret probabilities <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.

### Probability of an Exact Value
The probability that a continuous [[random_variables_overview | random variable]] is *exactly* equal to a specific value is essentially zero <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.

> [!EXAMPLE] Exact Rain
> Consider the probability that the exact amount of rain tomorrow (Y) is precisely 2 inches <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>. This means not 2.01 inches, not 1.99 inches, but *exactly* 2 inches, to an infinite decimal point <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>. Such a measurement is theoretically impossible to achieve or even measure <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.
>
> The odds of anything being exactly a certain measurement to the exact infinite decimal point is actually 0 <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>. This is analogous to asking for the area of a single line on a graph; a line has no width, and therefore no area <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>.

### Probability Over an Interval
For continuous [[random_variables_overview | random variables]], probability is determined by the area under the [[probability_density_functions | probability density function]] curve over a given interval <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>.

> [!EXAMPLE] Rain within a Range
> Instead of asking for *exactly* 2 inches of rain, a meaningful question would be: What is the probability that Y is between 1.9 and 2.1 inches of rain <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>?
>
> To find this [[calculating_probability | probability]], you would calculate the area under the curve of the [[probability_density_functions | probability density function]] from 1.9 to 2.1 <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>. In calculus, this corresponds to the definite integral of the [[probability_density_functions | probability density function]] `f(x)` from the lower bound (1.9) to the upper bound (2.1) <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>.
>
> This concept applies to any interval. For instance, to find the probability of less than 0.1 inches of rain, you'd calculate the area from 0 to 0.1 <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>. For more than 4 inches, you'd calculate the area from 4 to infinity <a class="yt-timestamp" data-t="00:07:38">[00:07:38]</a>.

### Total Area Under the Curve
A fundamental property of any [[probability_density_functions | probability density function]] for a continuous [[random_variables_overview | random variable]] is that the total area under its curve must equal 1 (or 100%) <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>. This signifies that the probability of *all possible outcomes* occurring is 1 <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>. For those familiar with calculus, this means the integral of `f(x)` from negative infinity to positive infinity (or 0 to infinity in the rain example) must be 1 <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>.

## Probability Distributions for Discrete Random Variables
Similar to continuous variables, [[probability_distribution_functions | probability distribution functions]] for discrete [[random_variables_overview | random variables]] also have a crucial property:

### Sum of Probabilities
The sum of all probabilities for all possible outcomes in a discrete [[probability_distribution_functions | probability distribution function]] must equal 1 <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>.

> [!EXAMPLE] Coin Toss
> For a simple coin toss where X=1 for heads and X=0 for tails <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>, if the probability of heads is 0.5, then the probability of tails must also be 0.5 <a class="yt-timestamp" data-t="00:09:13">[00:09:13]</a>. If one probability were 0.6, the other would have to be 0.4, ensuring they add up to 1 <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>. Having a 60% chance of heads and a 60% chance of tails would result in a 120% probability, which makes no sense <a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a>.

In summary, whether dealing with continuous or discrete [[random_variables_overview | random variables]], the total probability across all possible outcomes must always equal 1 <a class="yt-timestamp" data-t="00:09:46">[00:09:46]</a>.