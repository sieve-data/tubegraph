---
title: Continuous values and probability paradox
videoId: ZA4JkHKZM50
---

From: [[3blue1brown]] <br/> 

Imagine a weighted coin where the probability of flipping heads, denoted as 'h', is unknown <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. This probability could be any real number between 0 and 1 <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. If you flip this coin 10 times and get 7 heads, it might lead one to believe the underlying weight is 70% <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.

## The Paradox of Probabilities of Probabilities

A peculiar question arises: "What's the probability that the true probability of flipping heads is 0.7?" <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>. This is a [[understanding_probability_of_probabilities | probability of a probability]] question, making it difficult to conceptualize, as the unknown value is itself a long-run frequency for a random event <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

The more pressing challenge, and a source of [[paradoxical_and_nonintuitive_mathematical_truths | paradox]], comes from asking about probabilities in the setting of continuous values <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>. If one asks for the probability that 'h' is precisely 0.7, as opposed to a very slightly different value like 0.7000001, there is a strong possibility for [[paradoxical_and_nonintuitive_mathematical_truths | paradox]] <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.

Consider the uncountably infinite specific values 'h' could take between 0 and 1 <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>:
*   If every specific value within this range has a non-zero probability, then adding them all up would result in an infinite total probability, which is illogical <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>.
*   Conversely, if all these probabilities are 0, the total sum would be 0, when it should be 1, because the coin's weight 'h' must be *something* <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.

## Resolving the Paradox with Ranges and Density

The key to resolving this [[paradoxical_and_nonintuitive_mathematical_truths | apparent paradox]] is to shift focus from individual values to ranges of values <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>. Instead of representing probability by the height of a bar, it is represented by the **area** of the bar <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>.

As one considers finer and finer ranges, the probability for each individual bucket approaches zero, but the overall shape of the distribution is preserved <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>. This process approaches a smooth curve <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>.

### Probability Density Function (PDF)
When area represents probability (width × height), the height of the curve represents a "probability per unit in the x-direction" <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>. This is known as [[probability_density_and_distribution | probability density]] <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>. The function describing this density is called a **Probability Density Function (PDF)** <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.

Key characteristics of a PDF:
*   The total area under the curve must equal one, reflecting that the probability of the variable taking *any* possible value within its range is 100% <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>.
*   The probability of a random variable lying between two values is given by the area under the curve between those values <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>.
*   The probability of any one specific number, like 0.7, is 0, because the area of an infinitely thin slice is 0 <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.
*   The [[paradoxical_and_nonintuitive_mathematical_truths | paradox]] is sidestepped because the rules for combining probabilities change in a continuous context <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>. Probabilities for ranges are fundamental, and an individual value is thought of as a range with width 0 <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>.

## Theoretical Underpinnings: Measure Theory

The shift in rules between finite and continuous settings can feel unsettling <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>. Mathematicians address this with [[measure_theory_in_probability | measure theory]] <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>. This field of mathematics provides a rigorous framework for associating probabilities (or "measures") to various subsets of possibilities, ensuring they combine and distribute consistently <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>.

For example, [[measure_theory_in_probability | measure theory]] can smoothly handle situations where a single value has a non-zero probability while other values follow a continuous distribution, like a random number that is 0 with 50% probability and otherwise follows a bell curve <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>.

A common rule of thumb is to replace sums in discrete contexts with integrals in continuous contexts <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>. Integrals are the calculus tool for finding areas under curves <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>. The theoretical definition of integrals, especially more powerful ones, is based on [[measure_theory_in_probability | measure theory]], which forms the formal foundation of probability <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>.

## Application to the Coin Problem

With this understanding, the correct approach to the original coin problem is to find the [[probability_density_and_distribution | probability density]] function that describes the unknown value 'h' after observing coin toss outcomes <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>. Once this PDF is established, one can answer meaningful questions, such as "What's the probability that the true probability of flipping heads falls between 0.6 and 0.8?" <a class="yt-timestamp" data-t="00:09:23">[00:09:23]</a>.