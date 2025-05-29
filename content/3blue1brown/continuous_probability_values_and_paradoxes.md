---
title: Continuous probability values and paradoxes
videoId: ZA4JkHKZM50
---

From: [[3blue1brown]] <br/> 

When considering the probability of an unknown event, such as the weight of a coin, questions arise that challenge intuitive understanding, particularly when dealing with continuous values <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>.

## The Challenge of Continuous Probability

Imagine a weighted coin where the probability of flipping heads, denoted as 'h', could be any real number between 0 and 1, e.g., 20%, 90%, or 31.41592% <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. If, after 10 flips, 7 come up heads, one might ask: "What's the probability that the true probability of flipping heads is 0.7?" <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a> This question is unusual for two reasons <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>:

1.  It asks about a [[probability_of_a_probability | probability of a probability]] <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.
2.  It asks about probabilities in the context of continuous values <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>.

### The Paradox of Individual Continuous Values

When considering a specific continuous value, like 'h' being precisely 0.7 (as opposed to 0.7000001), a strong possibility for [[paradoxes_in_the_concept_of_derivatives | paradox]] emerges <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>:

> [!WARNING] The Summation Problem
> If every specific value within a continuous range (uncountably infinitely many of them) has a non-zero probability, no matter how minuscule, adding them all up would result in an infinite total probability <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>. Conversely, if all these probabilities are zero, their sum would also be zero, when the total probability of 'h' being *some* value should be 1 <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>. This creates a conundrum where probabilities cannot all be non-zero, nor can they all be zero <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.

## Resolving the Paradox: Probability Density

The key to resolving this paradox lies in shifting focus from individual values to *ranges of values* <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>. For example, instead of asking the probability of h being exactly 0.7, one might ask the probability of h being between 0.8 and 0.85 <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.

Crucially, in this context, the *area* of a bar (representing a range) is used to represent probability, not the height of the bar <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>. As these ranges become increasingly fine, approaching individual points, the smaller probability of falling into any one narrow range is accounted for by its thinner width, while the heights remain relatively consistent <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>. This process approaches a smooth curve <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>.

### Probability Density Function (PDF)

> [!NOTE] Probability Density
> The height of this curve represents a "probability per unit in the x-direction," known as **probability density** <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>. The curve itself is called a **probability density function (PDF)** <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>. For any valid probability distribution, the total area under this curve must equal one <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>.

The way to interpret a PDF is that the probability of a random variable lying between two values equals the area under the curve between those values <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>.

*   The probability of a specific number, like 0.7, is 0, because the area of an infinitely thin slice is 0 <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.
*   The probability of all possible values combined is 1, as this is the total area under the curve <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>.

This approach successfully sidesteps the initial paradox <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.

## Shifting Rules and Deeper Foundations

The resolution highlights a subtle shift in the rules for combining probabilities between finite and continuous settings <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>:

*   In finite or countably infinite settings (e.g., rolling a die), the probability of a collection of outcomes is the sum of their individual probabilities <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.
*   In continuous contexts, the probability of falling into a range is no longer the sum of individual probabilities, as individual probabilities are zero <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>. Instead, probabilities associated with ranges are the fundamental primitive objects <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>.

Mathematicians address this by using [[measure_theory_in_probability | measure theory]], a field that unifies these two settings and formalizes the idea of associating probabilities with subsets of possibilities <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>. For example, measure theory can smoothly handle situations where a single value has a non-zero probability, while other values are distributed continuously <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>.

## Integrals: The Continuous Equivalent of Sums

A common rule of thumb in [[integrals_and_probability_distributions | probability distributions]] is that if a sum is used in a discrete context, an integral is used in the continuous context to find areas under curves <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>. The theoretical underpinnings of integrals, particularly a more powerful definition than typically taught in introductory calculus, are based on [[measure_theory_in_probability | measure theory]] <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>.

Understanding that the rules for combining probabilities change between finite and continuous settings is crucial for grasping [[mathematical_intuition_and_counterintuitive_results | counterintuitive results]] in probability, such as how a collection of outcomes, each with zero probability, can collectively have a probability of one <a class="yt-timestamp" data-t="00:08:23">[00:08:23]</a>.

## Back to the Coin Problem

For the original question about the coin with an unknown weight 'h', the correct approach is to seek the probability density function (PDF) that describes 'h' after observing experimental outcomes <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>. Once this PDF is found, it can be used to answer practical questions, such as the probability that the true probability of flipping heads falls within a specific range, e.g., between 0.6 and 0.8 <a class="yt-timestamp" data-t="00:09:23">[00:09:23]</a>.