---
title: Probability of a probability
videoId: ZA4JkHKZM50
---

From: [[3blue1brown]] <br/> 

When discussing the probability of a probability, such as the true underlying weight of a coin, two initial complexities arise:

*   It involves a probability of a probability, where the unknown value itself represents a long-run frequency for a random event <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.
*   It requires working with continuous values. If the true probability of flipping heads, denoted as 'h', can be any real number between 0 and 1, asking for the probability that 'h' is *precisely* a specific value (e.g., 0.7) can lead to paradoxes <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.

## The Paradox of Continuous Probabilities

Consider the range of possible values for 'h' between 0 and 1 <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.

*   If every specific value within this uncountably infinite range were to have a non-zero probability, summing them would result in an infinite total probability, which is illogical <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>.
*   Conversely, if all these specific probabilities were zero, the total sum would be zero, despite the coin's weight 'h' definitely being *some* value within the range (the total probability should be 1) <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.

## Resolving the Paradox: Probability Density

The solution lies in shifting focus from individual values to ranges of values <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.

Instead of assigning probability to a single point, we consider the probability that 'h' falls within a given range (e.g., between 0.8 and 0.85) <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.

### Area as Probability

Crucially, the *area* of a bar representing a range, rather than its height, should represent the probability <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>. As we consider finer and finer buckets (smaller ranges):
*   The width of each bar decreases <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>.
*   The heights of the bars remain roughly consistent, leading to a smooth curve when taken to the limit <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>.
*   This approach preserves the overall shape of the distribution, even as the probability of falling into any single infinitesimally small bucket approaches zero <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>. If heights represented probabilities, everything would tend towards zero, yielding no information about the distribution <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.

### Probability Density Function (PDF)

The height of this curve is known as [[probability_density_function_pdf | probability density]]—a probability per unit in the x-direction <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>. The total area under the entire curve must always equal one, as this is a fundamental requirement for any valid probability distribution <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>.

By associating a [[probability_density_function_pdf | probability density]] to each possible value of 'h', the paradox is circumvented <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>.

*   The probability of a random variable lying between two values is found by calculating the area under the [[probability_density_function_pdf | Probability Density Function]] curve between those values <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>.
*   The area of an infinitely thin slice (representing a single, specific number like 0.7) is zero, so the probability of any one specific number occurring is zero <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.
*   However, the total area under the full curve remains 1, representing the certainty that the value 'h' falls somewhere within its possible range <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>.

### Shifting Rules

The resolution to this paradox hinges on a subtle change in the rules of [[Probability in geometry and tetrahedrons | probability]] from discrete to continuous settings <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>.

*   In discrete contexts (e.g., rolling a die), the probability of a value falling into a collection of possibilities is the sum of individual probabilities <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.
*   In continuous contexts, the probability of falling into a range is no longer a sum of individual probabilities <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>. Instead, probabilities associated with ranges are the fundamental objects, and an individual value is considered a range of width zero <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>.

### Measure Theory and Integrals

Mathematicians address this fundamental shift through a field called [[measure_theory_in_probability | Measure Theory]], which provides a rigorous foundation for associating numbers like probabilities to various subsets of possibilities <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>.

Generally, if a sum is used in a discrete context, an [[integrals_and_probability_distributions | integral]] is used in a continuous context to find areas under curves <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>. The theoretical underpinnings of integrals are also rooted in [[measure_theory_in_probability | Measure Theory]] <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>.

By understanding the concept of [[probability_density_function_pdf | probability density]] and applying the principles of [[integrals_and_probability_distributions | integration]], we can appropriately answer questions about the [[applications_of_probability_density | probability]] of a probability, such as "what's the probability that the true probability of flipping heads falls between 0.6 and 0.8?" <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>. The next step is to determine the specific [[probability_density_function_pdf | PDF]] that describes 'h' after observing experimental outcomes <a class="yt-timestamp" data-t="00:09:23">[00:09:23]</a>.