---
title: Properties of probability distribution functions
videoId: Fvi9A_tEmXQ
---

From: [[khanacademy]] <br/> 

The concept of [[random_variables_and_probabilities | random variables]] is fundamental to understanding [[introduction_to_probability | probability]]. [[random_variables_and_probabilities | Random variables]] are broadly categorized into two types: discrete and continuous <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>.

## Types of Random Variables

*   **Discrete Random Variables**: These take on a finite number of values <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. While they tend to be integers, they don't always have to be <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. The key characteristic is that you cannot have an infinite number of values for a discrete [[random_variables_and_probabilities | random variable]] <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.
*   **Continuous Random Variables**: These can take on an infinite number of values within a given range <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>. An example is the "exact amount of rain tomorrow" (represented as a [[random_variables_and_probabilities | random variable]] `Y`), which could be 2 inches, 2.01 inches, or 1.99999 inches <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>. [[random_variables_and_probabilities | Random variables]] are typically denoted by capital letters <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.

## Probability Density Functions for Continuous Variables

For continuous [[random_variables_and_probabilities | random variables]], their [[probability_distribution_functions | probability distribution]] is described by a [[probability_distribution_and_density_functions | probability density function]] (PDF) <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.

### Probability of an Exact Value
A critical property of [[probability_distribution_and_density_functions | probability density functions]] for continuous [[random_variables_and_probabilities | random variables]] is that the [[definition_of_probability | probability]] of the [[random_variables_and_probabilities | random variable]] being *exactly* equal to a specific value is essentially zero <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.

For instance, the [[definition_of_probability | probability]] of having exactly 2 inches of rain (not 2.01 or 1.99) is practically 0 <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.

> "The odds of actually anything being exactly a certain measurement to the exact infinite decimal point is actually 0." <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>

This is analogous to asking for the area of a line, which has no width and therefore no area <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>.

### Calculating Probability over an Interval
Instead, [[definition_of_probability | probability]] for continuous [[random_variables_and_probabilities | random variables]] is calculated over an interval <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>. The [[definition_of_probability | probability]] that a continuous [[random_variables_and_probabilities | random variable]] falls within a certain range is represented by the area under its [[probability_distribution_and_density_functions | probability density function]] curve between the specified points <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.

For example, to find the [[definition_of_probability | probability]] that `Y` (amount of rain) is between 1.9 and 2.1 inches, one would find the area under the curve `f(x)` from `x = 1.9` to `x = 2.1` <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>.

> The [[definition_of_probability | probability]] of this happening would be equal to the integral, for those of you who've studied [[calculus_and_probability_density_functions | calculus]], from 1.9 to 2.1 of `f(x) dx` <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>.

### Total Area Under the Curve
A fundamental property of any [[probability_distribution_and_density_functions | probability density function]] for a continuous [[random_variables_and_probabilities | random variable]] is that the total area under the entire curve must be equal to 1 <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>. This represents the certainty that one of all possible [[events_and_outcomes_in_probability | events]] will occur.

> The [[definition_of_probability | probability]] of all of the [[events_and_outcomes_in_probability | events]] that might occur can't be more than 100% <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>. So essentially, the whole area under this curve has to be equal to 1 <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>.
>
> If we took the integral of `f(x)` from 0 to infinity, this thing, at least as I've drawn it, `dx` should be equal to 1 <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>.

## Properties of Probability Distribution Functions for Discrete Variables

For discrete [[random_variables_and_probabilities | random variables]], the [[definition_of_probability | probabilities]] of all possible [[events_and_outcomes_in_probability | events]] must sum up to 1 <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>.

For example, in a coin toss, where the [[random_variables_and_probabilities | random variable]] `x` is 1 for heads and 0 for tails, if the [[definition_of_probability | probability]] of heads is 0.6, the [[definition_of_probability | probability]] of tails must be 0.4, so they add up to 1 <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a>. It's impossible to have a 60% [[definition_of_probability | probability]] of heads and a 60% [[definition_of_probability | probability]] of tails, as that would result in a total [[definition_of_probability | probability]] of 120% <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>.

This rule is consistent across both discrete and continuous [[probability_distribution_functions | probability distribution functions]]: the total [[definition_of_probability | probability]] of all possible [[events_and_outcomes_in_probability | outcomes]] must equal 1 <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>.