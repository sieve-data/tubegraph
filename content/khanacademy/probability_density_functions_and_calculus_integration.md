---
title: Probability density functions and calculus integration
videoId: Fvi9A_tEmXQ
---

From: [[khanacademy]] <br/> 

In the study of [[probability_and_distribution_modeling | probability and distribution modeling]], random variables are central. These can be categorized into two main types: discrete and continuous <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. Discrete random variables take on a finite number of values, often integers <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. Continuous random variables, however, can take on an infinite number of values within a given range <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>.

## Understanding Continuous Random Variables and PDFs

For a continuous random variable, such as the exact amount of rain tomorrow (e.g., random variable Y) <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>, its [[probability_distribution_functions | probability distribution]] is represented by a Probability Density Function (PDF) <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>. This function, often denoted as *f(x)* (where the x-axis represents the amount of rain in inches), illustrates the likelihood of different outcomes <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>, <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>.

## Probability of an Exact Value: Why it's Zero

A critical distinction for continuous random variables is that the [[calculating_probability_of_an_event | probability]] of the variable taking on an *exact* specific value is essentially zero <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.

For example, the [[calculating_probability_of_an_event | probability]] of having exactly 2 inches of rain (not 2.000001 or 1.99999 inches) is 0 <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>, <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>. This is because a continuous variable can take on an infinite number of values, making the chance of hitting any single, infinitely precise point infinitesimally small <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.

This concept can be compared to asking for the area of a single line <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>. A line, as mathematically defined, has no width, and thus no area <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>. Similarly, a single point on a continuous distribution has no "width" and therefore no probability.

## Calculating Probability for a Range of Values

For continuous random variables, [[calculating_probability_of_an_event | probability]] is determined over an *interval* or range of values <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>. To find the [[calculating_probability_of_an_event | probability]] that a continuous random variable Y falls within a certain range (e.g., between 1.9 and 2.1 inches of rain) <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>, one must calculate the [[area_under_probability_curves | area under the probability density function]] curve for that interval <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>.

This is where [[concept_of_derivatives_and_differential_calculus | calculus]] becomes essential. The [[area_under_probability_curves | area under the curve]] of a PDF is found using the definite integral <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>:

```
P(a ≤ Y ≤ b) = ∫[a to b] f(x) dx
```
Where *f(x)* is the probability density function, and *a* and *b* are the lower and upper bounds of the interval, respectively <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>. For example, to find the [[calculating_probability_of_an_event | probability]] of rain between 1.9 and 2.1 inches, one would integrate *f(x)* from 1.9 to 2.1 <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>.

This principle applies to any range:
*   To find the [[calculating_probability_of_an_event | probability]] of less than 0.1 inches of rain, one would calculate the area from 0 to 0.1 <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>, <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>.
*   To find the [[calculating_probability_of_an_event | probability]] of more than 4 inches of rain, one would integrate from 4 to infinity <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>, <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>.

## Total Probability

A fundamental rule for any [[probability_distribution_functions | probability distribution function]], whether discrete or continuous, is that the total [[calculating_probability_of_an_event | probability]] of all possible outcomes must equal 1 (or 100%) <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>, <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>.

*   For discrete [[probability_distribution_functions | probability distributions]], the sum of all individual probabilities must be 1 <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>, such as a coin flip where P(Heads) + P(Tails) = 0.5 + 0.5 = 1 <a class="yt-timestamp" data-t="00:09:13">[00:09:13]</a>, <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>.
*   For continuous [[probability_distribution_functions | probability density functions]], the total [[area_under_probability_curves | area under the curve]] across the entire range of possible values must equal 1 <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>. This means the definite integral of the PDF from its lowest possible value to its highest (often 0 to infinity, depending on the variable) must equal 1 <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>, <a class="yt-timestamp" data-t="00:09:46">[00:09:46]</a>.
    ```
    ∫[from -∞ to +∞] f(x) dx = 1
    ```