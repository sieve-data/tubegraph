---
title: Probability distribution and density functions
videoId: Fvi9A_tEmXQ
---

From: [[khanacademy]] <br/> 

This article explores [[probability_distribution_functions | probability distribution functions]], distinguishing between discrete and continuous [[random_variables_and_probabilities | random variables]] and how their probabilities are represented and calculated.

## Types of Random Variables <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>

There are two main types of [[random_variables_and_probabilities | random variables]]:

*   **Discrete Random Variables** <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>
    *   Take on a finite number of values. <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>
    *   These values tend to be integers, though not always. <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>
    *   An infinite number of values cannot exist for a discrete [[random_variables_and_probabilities | random variable]]. <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>
*   **Continuous Random Variables** <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>
    *   Can take on an infinite number of values within a range. <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>
    *   Often represented by capital letters, such as Y. <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>

## Probability for Discrete Random Variables <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>

For discrete [[probability_distribution_functions | probability distributions]], the sum of all individual probabilities must equal 1. <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>

### Example: Coin Toss <a class="yt-timestamp" data-t="00:08:56">[00:08:56]</a>
Consider a coin toss where X=1 for heads and X=0 for tails. <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>
*   If the [[probability calculation | probability]] of heads is 0.5, then the [[probability calculation | probability]] of tails must also be 0.5, so they add up to 1. <a class="yt-timestamp" data-t="00:09:13">[00:09:13]</a>
*   If the [[probability calculation | probability]] of heads was 0.6, the [[probability calculation | probability]] of tails would have to be 0.4 to sum to 1. <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a>
*   Having a 60% [[probability calculation | probability]] of heads and a 60% [[probability calculation | probability]] of tails makes no sense, as it would total 120%. <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>

The sum of all probabilities for a discrete [[random_variables_in_probability | random variable]] must add up to 1. <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>

## Probability for Continuous Random Variables: Probability Density Functions <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>

Unlike discrete variables, continuous [[random_variables_and_probabilities | random variables]] use a [[calculus_and_probability_density_functions | probability density function]] (PDF) to describe probabilities. <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>

### Probability of an Exact Value <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>
The [[probability calculation | probability]] that a continuous [[random_variables_and_probabilities | random variable]] takes on an *exact* value is essentially zero. <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>

*   **Example: Exact Amount of Rain** <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>
    *   Consider the [[random_variables_in_probability | random variable]] Y representing the exact amount of rain tomorrow. <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>
    *   The [[probability calculation | probability]] of getting *exactly* 2 inches of rain (not 2.01, not 1.99, but precisely 2.000... inches) is 0. <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a> This is because continuous measurements involve infinite decimal points, making any single, exact value infinitely improbable. <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>
    *   No measurement tool can verify an exact value to an infinite decimal point. <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>

*   **Analogy: Area of a Line** <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>
    *   Asking for the [[probability calculation | probability]] of an exact value for a continuous variable is like asking for the area of a line. <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a> A line has height (the PDF value) but no width, thus no area. <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>

### Probability as Area Under the Curve <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>
For continuous [[random_variables_and_probabilities | random variables]], [[probability calculation | probability]] is calculated as the area under the [[calculus_and_probability_density_functions | probability density function]] curve over a specific interval. <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>

*   **Example: Rain within a Range** <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>
    *   Instead of asking for exactly 2 inches, it's meaningful to ask for the [[probability calculation | probability]] that Y is *almost* 2 inches, e.g., between 1.9 and 2.1 inches of rain. <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>
    *   To find this [[probability calculation | probability]], one would calculate the area under the [[calculus_and_probability_density_functions | probability density function]] curve between 1.9 and 2.1 inches. <a class="yt-timestamp" data-t="00:05:33">[00:05:33]</a>

*   **Using Calculus: The Definite Integral** <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>
    *   For those familiar with [[calculus_and_probability_density_functions | calculus]], this area is found using the definite integral of the [[calculus_and_probability_density_functions | probability density function]] (f(x)) over the desired interval. <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>
    *   For example, the [[probability calculation | probability]] of rain between 1.9 and 2.1 inches is given by:
        $$\int_{1.9}^{2.1} f(x) \,dx$$ <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>

### Total Area Under the Curve <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>
A fundamental property of [[probability_distribution_functions | probability density functions]] is that the total area under the entire curve must equal 1. <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a> This represents the 100% [[probability calculation | probability]] that *some* event will occur. <a class="yt-timestamp" data-t="00:08:07">[00:08:07]</a>

*   Using [[calculus_and_probability_density_functions | calculus]], if the function is defined from 0 to infinity (as might be for rain amount), the integral from 0 to infinity of f(x) dx must equal 1. <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>

> [!NOTE]
> An integral is essentially the area under a curve. <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>

This rule applies to both discrete ([[properties_of_probability_distribution_functions | sum of probabilities = 1]]) and continuous ([[properties_of_probability_distribution_functions | area under PDF = 1]]) [[probability_distribution_functions | probability distributions]]. <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>