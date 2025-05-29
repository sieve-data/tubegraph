---
title: Probability density function PDF
videoId: ZA4JkHKZM50
---

From: [[3blue1brown]] <br/> 

Imagine you have a weighted coin where the probability of flipping heads is unknown. It could be any real number between 0% and 100% <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. If you flip this coin 10 times and get 7 heads, you might wonder if the true probability of heads is 70% <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. This leads to a complex question: what's the [[probability_of_a_probability | probability that the true probability of flipping heads]] is exactly 0.7? <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a> This type of inquiry is unusual for two reasons:
1.  It asks about a [[probability_of_a_probability | probability of a probability]] <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.
2.  It deals with probabilities in the context of continuous values <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>.

Let's call this unknown probability of flipping heads 'h'. The value 'h' can be any real number from 0 to 1 <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.

## The Paradox of Continuous Values

A significant challenge arises when trying to assign a probability to a specific continuous value, like h being exactly 0.7 <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>. If every specific value within a continuous range (an uncountably infinite number of values) has a non-zero probability, no matter how minuscule, summing them all up would result in an infinite total probability <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>. Conversely, if all individual probabilities are zero, their sum would also be zero, even though the true probability 'h' must be *some* value within the range 0 to 1, meaning the total probability should be 1 <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>. This creates an apparent paradox <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.

## Resolving the Paradox: Ranges and Area

The key to resolving this paradox is to shift focus from individual values to *ranges* of values <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>. Instead of asking for the probability of h being exactly 0.7, we ask for the probability that h falls within a range, such as between 0.8 and 0.85 <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.

Crucially, when visualizing these probabilities, it's not the height of a bar that represents probability, but its *area* <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>. By taking finer and finer buckets (smaller ranges), the width of each bar decreases, while the heights remain roughly the same, leading to a smooth curve as a limit <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>. This smooth curve preserves the overall shape of the distribution, even as the probability of falling into any single infinitesimally small bucket approaches zero <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>.

## What is Probability Density?

If the area represents probability (width × height), then the height must represent a "probability per unit in the x-direction" <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>. This concept is known as **probability density** <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>. When applied to all possible values of a continuous variable, it forms a **probability density function (PDF)** <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>.

### Key Properties of a PDF
*   **Area as Probability:** The probability that a random variable lies between two values is given by the area under the PDF curve between those values <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.
*   **Individual Probability is Zero:** The probability of getting any one very specific number (e.g., 0.7) is 0, because the area of an infinitely thin slice is 0 <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.
*   **Total Area is One:** The total area under the entire PDF curve must always equal 1 <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>. This represents the certainty that the variable will take *some* value within its possible range <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.

This framework successfully sidesteps the initial paradox <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.

## Discrete vs. Continuous Rules

In discrete settings (like rolling a die), the probability of a collection of outcomes is simply the sum of individual probabilities <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>. However, for continuous contexts, the rules shift: probabilities associated with ranges are the fundamental objects, and an individual value is considered a range of width zero <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>.

This change in rules from summing in discrete contexts to using [[integrals_and_probability_distributions | integrals]] in continuous contexts (to find areas under curves) is a common rule of thumb in calculus <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>. The formal foundation for this lies in a field of mathematics called measure theory, which provides a rigorous way to associate probabilities to subsets of possibilities <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>.

Understanding probability density is crucial for dealing with random variables that can take any real number value <a class="yt-timestamp" data-t="00:08:23">[00:08:23]</a>. It allows us to ask meaningful questions, such as: "What's the probability that the true probability of flipping heads falls between 0.6 and 0.8?" by finding the area under the appropriate PDF <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.