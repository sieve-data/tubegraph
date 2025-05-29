---
title: Measure theory in probability
videoId: ZA4JkHKZM50
---

From: [[3blue1brown]] <br/> 

Understanding probability when dealing with continuous values, such as the true underlying weight of a biased coin, introduces unique challenges compared to discrete probabilities like coin flips or dice rolls <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>. When considering a continuous variable, like the probability `h` of flipping heads (which could be any real number between 0 and 1) <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>, asking for the probability of `h` being *precisely* 0.7 leads to a paradox if not carefully handled <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.

## The Paradox of Individual Probabilities in Continuous Settings

If every specific value within an uncountably infinite range has a non-zero probability, even minuscule, their sum would blow up to infinity <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>. Conversely, if all individual probabilities are zero, their sum would also be zero, which contradicts the fact that the total probability of `h` being *some* value must be 1 <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>. This means that individual values cannot all have non-zero or all zero probabilities <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.

## Probability Density Functions (PDFs)

The key to resolving this apparent paradox is to shift focus from individual values to *ranges of values* <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.

Instead of the height of a bar representing probability, the *area* of each bar represents probability for a given range <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>. As these ranges become infinitesimally small (finer and finer "buckets"), the smaller probability of falling into any one bucket is accounted for by the thinner width of the bars, while their heights remain roughly the same <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>. This process approaches a smooth curve <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>.

This smooth curve defines a **probability density function (PDF)** <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>. The y-axis in a PDF represents "probability density," which is a probability per unit in the x-direction <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>. The total area under the entire curve of a valid probability distribution must always equal one <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>.

### Interpreting a PDF

Anytime a PDF is encountered, it should be interpreted as follows: the probability of a random variable lying between two values equals the area under the curve between those values <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>.
*   The probability of getting one very specific number (e.g., 0.7) is 0, because the area of an infinitely thin slice under the curve is 0 <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.
*   The probability of the variable being any value within its entire range is 1, as this corresponds to the total area under the full curve <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>.

This approach successfully sidesteps the initial paradox <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.

## The Role of [[measure_theory_and_open_intervals | Measure Theory]]

The resolution of the paradox reveals a subtle shift in the rules for probability in continuous settings <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>. In finite settings, like rolling a die, the probability of a random value falling into a collection of possibilities is simply the sum of individual probabilities. However, for continuous values, the probability of falling into a range is no longer the sum of individual probabilities <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>. Instead, probabilities associated with ranges become the fundamental objects <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>. An individual value is then considered a range of width zero <a class="yt-timestamp" data-t="00:06:38">[00:06:38]</a>.

This change in fundamental rules is rigorously addressed by a field of mathematics called [[measure_theory_and_open_intervals | measure theory]] <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>. [[measure_theory_and_open_intervals | Measure theory]] helps to unite discrete and continuous probability settings by providing a formal framework for associating numbers (like probabilities) to various subsets of all possibilities in a way that allows them to combine and distribute consistently <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>.

For instance, [[measure_theory_and_open_intervals | measure theory]] can smoothly handle scenarios where a single value has a non-zero probability (like a 50% chance of a random number being 0), while the remaining probability is distributed continuously (like half a bell curve for positive numbers) <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>.

### Integrals as Continuous Sums

A common rule of thumb in probability is that if a sum is used in a discrete context, an integral is used in a continuous context <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>. Integrals are the calculus tool used to find areas under curves <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>. Beyond their typical definition in introductory calculus, integrals have a more powerful definition rooted in [[measure_theory_and_open_intervals | measure theory]], which serves as the formal foundation of probability <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>.

Understanding that the "rules for combining probabilities of different sets" are fundamentally different in continuous settings, based on a different axiom system, is crucial for comprehending how continuous probabilities work without paradox <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>.

The practical implication of this understanding is that for questions involving unknown continuous probabilities, such as the weight `h` of a coin after observing flips, the appropriate approach is to determine the probability density function that describes the value <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>. This PDF can then be used to calculate the probability of `h` falling within specific ranges <a class="yt-timestamp" data-t="00:09:23">[00:09:23]</a>.