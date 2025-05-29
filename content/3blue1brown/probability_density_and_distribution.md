---
title: Probability density and distribution
videoId: ZA4JkHKZM50
---

From: [[3blue1brown]] <br/> 

Imagine a weighted coin where the probability of flipping heads (let's call it 'h') is unknown <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. This probability could be any real number between 0 and 1, such as 20%, 90%, or even 31.41592% <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. If you flip this coin 10 times and get 7 heads, it might seem intuitive that the true probability of heads is 70% <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.

However, asking for the probability that the true probability `h` is *precisely* 0.7 presents a paradox <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>. This question is challenging for two main reasons:
1.  It's asking about a [[understanding_probability_of_probabilities | probability of a probability]] <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.
2.  It deals with probabilities in the setting of continuous values <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>.

## The Paradox of Continuous Probabilities

If every specific value within a continuous range (an uncountably infinite number of them) had a non-zero probability, no matter how minuscule, adding them all up would result in an infinite total probability <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>. Conversely, if all individual probabilities were 0, their sum would also be 0, when it should be 1, as the coin's weight 'h' must be *some* value <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>. This creates a situation where values can't all be non-zero, nor can they all be zero <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.

## Resolving the Paradox: Focusing on Ranges

The key to understanding probabilities over continuous values is to focus not on individual values, but on **ranges of values** <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.

Imagine representing the probability of `h` falling into specific ranges (e.g., between 0.8 and 0.85) using bars <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>. Crucially, the **area** of each bar, not its height, represents the probability <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>.

As you consider finer and finer "buckets" (smaller ranges), the probability of falling into any one of them decreases, but this is accounted for by the thinner width of the bars <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>. The heights of the bars remain roughly the same, meaning that as this process is taken to the limit, it approaches a smooth curve <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>. This allows the overall shape of the distribution to be preserved and refined, even though the individual probabilities for infinitely thin buckets approach zero <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.

## Probability Density Function (PDF)

Since probability is represented by the area (width times height) of these bars, the height of the curve represents a "probability per unit in the x-direction" <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>. This is known as **probability density** <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.

The smooth curve formed in this limit is called a **Probability Density Function (PDF)** <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>.

Key characteristics of a PDF:
*   The total area under the entire curve must equal one, as the variable must take *some* value <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>.
*   The probability of a random variable lying between two values is given by the **area under the curve** between those values <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>.
*   The probability of any single, specific number (e.g., `h` being exactly 0.7) is 0, because the area of an infinitely thin slice under the curve is 0 <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.

### Shifting Rules for Continuous Contexts

In discrete settings (like rolling a die), the probability of a value falling into a collection of possibilities is simply the sum of the probabilities of each individual possibility <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>. However, for a continuum, the rules shift: probabilities associated with ranges are the fundamental objects <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>. An individual value is conceptualized as a range of width zero <a class="yt-timestamp" data-t="00:06:38">[00:06:38]</a>.

This change in rules is formally addressed by **measure theory**, a field of mathematics that rigorously associates numbers (like probabilities) to various subsets of possibilities in a consistent way <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>. It unites finite and continuous probability settings <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>.

In practice, a common rule of thumb is that if you use a sum in a discrete context, you use an **integral** in a continuous context, as integrals are the calculus tool for finding areas under curves <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>. This shift is not just a blind substitution; it reflects a deeper change in the underlying axiomatic system for combining probabilities of different sets <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>.

## [[applications_of_probability_density_function | Application of Probability Density]]

Returning to the coin with unknown weight `h`, the correct question to ask is: What is the [[applications_of_probability_density_function | probability density function]] that describes `h` after observing the outcomes of coin tosses <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>? Once this PDF is determined, it can be used to answer questions like: "What's the probability that the true probability of flipping heads falls between 0.6 and 0.8?" <a class="yt-timestamp" data-t="00:09:23">[00:09:23]</a>.