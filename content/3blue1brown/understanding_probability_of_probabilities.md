---
title: Understanding probability of probabilities
videoId: ZA4JkHKZM50
---

From: [[3blue1brown]] <br/> 
## Understanding Probability of Probabilities

The concept of a "probability of a probability" arises when we consider the uncertainty of an unknown probability itself <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. For instance, imagine a weighted coin where the true probability of flipping heads (let's call it `h`) is unknown <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a> <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>. This `h` could be any real number between 0 and 1 <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. After observing 7 heads in 10 flips, one might ask: what is the probability that the true probability of flipping heads is exactly 0.7? <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a> <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.

### The Paradox of Continuous Values

Asking about the exact probability of a specific continuous value, such as `h` being precisely 0.7, presents a significant challenge <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>. This is due to a paradox:
*   If every specific value within a continuous range (an uncountably infinite number of them) has a non-zero probability, no matter how minuscule, summing them up would cause the total probability to "blow up to infinity" <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a> <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.
*   Conversely, if all these probabilities are zero, the total sum of probabilities would be 0, when it should logically be 1, as the coin's weight `h` must be some value <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a> <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>.

This implies that these values cannot all be non-zero, nor can they all be zero <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.

### Resolving the Paradox with Probability Density

The key to working with [[probability_density_and_distribution | probabilities over continuous values]] and resolving this paradox is to focus on *ranges* of values rather than individual ones <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a> <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.

Instead of the height of a bar representing probability, the *area* of a bar represents that probability <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a> <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>. As you consider finer and finer ranges, or "buckets," the probability of falling into any one bucket becomes smaller, but this is accounted for by the thinner width of the bars <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a> <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>. The heights, however, remain relatively consistent <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>.

Taking this process to the limit, we approach a smooth curve <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a> <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>. While the individual probabilities of falling into any specific bucket will approach zero, the overall shape of the distribution is preserved and refined <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a> <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>.

#### Probability Density Function (PDF)

If the y-axis no longer represents probability, what are its units? <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a> Since probability is represented by the area (width times height), the height represents a "probability per unit in the x-direction" <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a> <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>. This is known as a **probability density** <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.

Associating a probability density to each value in a continuous range gives what is known as a [[probability_density_and_distribution | probability density function]], or PDF <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a> <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>.

Key properties of a PDF:
*   The probability of a random variable lying between two values equals the area under the curve between those values <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a> <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>. This is a fundamental concept for [[applications_of_probability_density_function | applications of probability density function]].
*   The total area under the entire curve of a valid [[probability_density_and_distribution | probability distribution]] must equal 1 <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a> <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a> <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>.
*   The probability of any one specific number in a continuous distribution is 0, because the area of an infinitely thin slice under the curve is 0 <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a> <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>.

This approach sidesteps the paradox by defining probabilities for ranges as the fundamental objects, rather than summing probabilities of individual points <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a> <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>.

### Underlying Mathematical Foundations

The rules for combining probabilities shift between finite (discrete) and continuous contexts <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a> <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>. In discrete settings, probabilities of a collection of possibilities are summed <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>. In continuous settings, sums are replaced by integrals (a calculus tool for finding areas under curves) <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a> <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>.

To provide a rigorous framework for these varying rules, mathematicians developed [[measure_theory_in_probability | measure theory]] <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a> <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a> <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>. [[measure_theory_in_probability | Measure theory]] helps to unite discrete and continuous settings by rigorously associating numbers (like probabilities) to various subsets of possibilities in a way that combines and distributes consistently <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a> <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>.

### Practical Application

Returning to the original problem of the weighted coin with an unknown weight `h`, the correct question to ask is: what is the [[probability_density_and_distribution | probability density function]] that describes the value `h` after observing the outcomes of coin tosses? <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a> <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>. If this PDF can be determined, it can be used to answer practical questions, such as the probability that the true coin weight `h` falls within a specific range, like between 0.6 and 0.8 <a class="yt-timestamp" data-t="00:09:23">[00:09:23]</a> <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>.