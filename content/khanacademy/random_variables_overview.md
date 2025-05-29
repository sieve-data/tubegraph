---
title: Random variables overview
videoId: Fvi9A_tEmXQ
---

From: [[khanacademy]] <br/> 

This article provides an overview of [[concept_of_random_variables | random variables]], focusing on the distinctions between discrete and [[discrete_vs_continuous_random_variables | continuous random variables]] and how [[introduction_to_probability | probability]] is calculated for each type.

## What is a Random Variable?

A [[concept_of_random_variables | random variable]] is a variable whose possible values are numerical outcomes of a random phenomenon <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. [[concept_of_random_variables | Random variables]] are typically represented by capital letters, such as Y <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.

## Types of Random Variables

There are two main types of [[concept_of_random_variables | random variables]]:

### Discrete Random Variables
[[discrete_vs_continuous_random_variables | Discrete random variables]] take on a finite number of values <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. While they often tend to be integers, they don't always have to be <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. A [[discrete_vs_continuous_random_variables | discrete random variable]] cannot have an infinite number of values <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.

For a [[discrete_vs_continuous_random_variables | discrete random variable]], the sum of all possible probabilities must equal 1 <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>. For [[examples_of_random_variables | example]], in a coin flip where X = 1 for heads and X = 0 for tails, if the probability of heads is 0.6, the probability of tails must be 0.4, as their sum is 1 <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a>. It makes no sense to have probabilities that sum to more than 100% for all possible [[events_and_outcomes_in_probability | outcomes]] <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.

### Continuous Random Variables
[[discrete_vs_continuous_random_variables | Continuous random variables]] can take on an infinite number of values <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.

#### [[examples_of_random_variables | Example]]: Amount of Rain
Consider a [[concept_of_random_variables | random variable]] Y representing the exact amount of rain tomorrow <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. The amount of rain could be 0 inches, 1 inch, 2 inches, 3 inches, 4 inches, or any value in between <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.

A probability distribution for a [[discrete_vs_continuous_random_variables | continuous random variable]] is called its **probability density function** <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>. The x-axis represents the amount of rain, and the y-axis represents some height of the function <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>.

#### Probability of an Exact Value
For a [[discrete_vs_continuous_random_variables | continuous random variable]], the [[introduction_to_probability | probability]] of it equaling an *exact* value is essentially zero <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.

For [[examples_of_random_variables | example]], the [[introduction_to_probability | probability]] that exactly 2 inches of rain falls (not 2.01, not 1.99, but *exactly* 2 inches) is 0 <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>. This is because a continuous variable can take on an infinite number of values within any interval, no matter how small <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>. It's like asking for the area of a single line, which has no width and therefore no area <a class="yt-timestamp" data-t="00:06:59">[00:06:59]</a>.

> "The odds of actually anything being exactly a certain measurement to the exact infinite decimal point is actually 0." <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>

#### Probability of an Interval (Area Under the Curve)
To find the [[introduction_to_probability | probability]] for a [[discrete_vs_continuous_random_variables | continuous random variable]], you need to consider an *interval* of values <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>. For [[examples_of_random_variables | example]], what is the [[introduction_to_probability | probability]] that the amount of rain Y is between 1.9 and 2.1 inches? <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>

This [[introduction_to_probability | probability]] corresponds to the **area under the curve** of the probability density function between those two points <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>. In calculus terms, this area is found by taking the **definite integral** of the probability density function over the specified interval <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.

For a function `f(x)` representing the probability density, the [[introduction_to_probability | probability]] that `Y` is between `a` and `b` is:
`P(a <= Y <= b) = ∫[from a to b] f(x) dx` <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>.

The total area under the entire probability density function (from 0 to infinity for rain) must equal 1 (or 100%) <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>. This means the integral of `f(x)` from 0 to infinity must be equal to 1 <a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a>. This concept also applies to [[discrete_vs_continuous_random_variables | discrete probability distributions]], where the sum of all probabilities must equal 1 <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>.