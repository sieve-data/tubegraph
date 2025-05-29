---
title: Calculus and probability density functions
videoId: Fvi9A_tEmXQ
---

From: [[khanacademy]] <br/> 

Probability theory differentiates between two main types of [[Random variables and probabilities | random variables]]: discrete and continuous <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. While discrete random variables take on a finite number of values, often integers <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>, continuous random variables can assume an infinite number of values within a given range <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>. An example of a continuous [[Random variables and probabilities | random variable]] is the exact amount of rain tomorrow <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.

## Probability Density Function (PDF)

For a continuous [[Random variables and probabilities | random variable]], its [[Probability distribution and density functions | probability distribution]] is represented by a [[Probability distribution and density functions | probability density function]] (PDF) <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>. The x-axis of a PDF graph represents the values of the [[Random variables and probabilities | random variable]] (e.g., amount of rain in inches), and the height of the curve at any point indicates the density of probability around that value <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.

### Probability of an Exact Value

A critical distinction for continuous [[Random variables and probabilities | random variables]] is that the [[Probability calculation | probability]] of the variable taking on *exactly* a specific value is essentially zero <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>. For instance, the [[Probability calculation | probability]] of having exactly 2 inches of rain (not 2.01, not 1.99, but precisely 2.000... with infinite precision) is zero <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>. This is because there are an infinite number of possible values, making the chance of landing on one specific point infinitesimally small <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>. It's analogous to asking for the area of a single line, which has no width and thus no area <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>.

### Calculating Probability over an Interval

Instead of exact values, [[Probability calculation | probability]] for continuous [[Random variables and probabilities | random variables]] is calculated over an interval <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>. To find the [[Probability calculation | probability]] that a continuous [[Random variables and probabilities | random variable]] falls within a certain range (e.g., between 1.9 and 2.1 inches of rain), one must determine the area under the [[Probability distribution and density functions | probability density function]] curve for that interval <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>.

This calculation involves [[Differential Calculus and Its Applications | calculus]], specifically the definite integral <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>. If `f(x)` defines the [[Probability distribution and density functions | probability density function]], the [[Probability calculation | probability]] that the [[Random variables and probabilities | random variable]] `Y` is between `a` and `b` is given by:

> ∫<sub>a</sub><sup>b</sup> f(x) dx <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>

For example, the [[Probability calculation | probability]] of rain being between 1.9 and 2.1 inches would be the integral of the PDF from 1.9 to 2.1 <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>.

### Properties of Probability Density Functions

A key [[Properties of probability distribution functions | property of probability distribution functions]], both discrete and continuous, is that the sum of all possible [[Events and outcomes in probability | events]]' probabilities must equal 1 (or 100%) <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>, <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>.

For continuous [[Random variables and probabilities | random variables]] and their [[Probability distribution and density functions | probability density functions]], this means the total area under the entire curve must be equal to 1 <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>, <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>. If the function is defined from 0 to infinity, the integral from 0 to infinity of `f(x) dx` must equal 1 <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>. This ensures that the [[Probability calculation | probability]] of *any* outcome occurring sums to certainty <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>.

> [!info] Total Probability
> For a discrete [[Probability distribution functions | probability distribution function]], the sum of all individual probabilities must equal 1 <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>, e.g., P(Heads) + P(Tails) = 0.5 + 0.5 = 1 <a class="yt-timestamp" data-t="00:09:19">[00:09:19]</a>. For a continuous [[Probability distribution and density functions | probability density function]], the total area under the curve (its definite integral over its entire domain) must equal 1 <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>.