---
title: Applications of probability density function
videoId: ZA4JkHKZM50
---

From: [[3blue1brown]] <br/> 

The concept of a [[probability_density_and_distribution | probability density function]] (PDF) is crucial for working with probabilities in continuous settings, such as when dealing with measurements or unknown parameters that can take on any real value within a range <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>.

## The Challenge of Continuous Probabilities

Consider a weighted coin where the exact probability of flipping heads, let's call it `h`, is unknown <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a> <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>. This value `h` could be any real number between 0 and 1 <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. If you flip the coin 10 times and get 7 heads, a natural question arises: "What's the probability that the true probability of flipping heads is precisely 0.7?" <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a> <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.

This question presents two immediate difficulties:
1.  **[[understanding_probability_of_probabilities | Probability of a Probability]]**: It asks about the probability of a value that is itself a probability (a long-run frequency of a random event) <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.
2.  **Continuous Values**: It seeks a probability for a single, specific value (e.g., 0.7) within a continuum of possibilities <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>.

The second point leads to a paradox:
*   If every specific value within a continuous range (like 0 to 1) has a non-zero probability, no matter how minuscule, summing them all up would result in an infinite total probability, which contradicts the rule that total probability must be 1 <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a> <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.
*   Conversely, if all specific probabilities are zero, their sum would also be zero, which means the true weight `h` could not be any value, which is also incorrect as `h` must be *some* value <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.

This paradox highlights the need for a different approach when dealing with continuous variables <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a> <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.

## Resolving the Paradox with Probability Density

The key to resolving this paradox is to shift focus from individual values to *ranges of values* <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.

Instead of asking about the probability of `h` being exactly 0.7, we ask about the probability of `h` falling within a specific range, for example, between 0.8 and 0.85 <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.

### Area Represents Probability

Crucially, in the continuous context, the probability is represented by the *area* of a region, not the height of a bar <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>.

Imagine dividing the range of possible `h` values into "buckets." The probability of `h` falling into a bucket is represented by its area. As these buckets become finer and finer (thinner width), the height of the bars remains roughly the same, preserving the overall shape of the distribution <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a> <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>. In this limit, the distribution approaches a smooth curve <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>.

### Probability Density Function (PDF)

The y-axis of this smooth curve represents a *probability density* <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a> <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>. This function is known as the **Probability Density Function (PDF)** <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>.

*   The PDF does not directly give the probability of a specific value.
*   The probability of a random variable lying between two values is the **area under the PDF curve** between those values <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.
*   The total area under the entire PDF curve must always equal 1 <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a> <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>.

This framework successfully sidesteps the paradox:
*   The probability of any single, infinitely thin slice (a specific value) is 0, because the area of an infinitely thin slice is 0 <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>.
*   However, the sum of these "zero-probability" points over a range can result in a non-zero probability because it's about the area under the curve <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>.

## Connecting to Integrals

In discrete contexts (like rolling a die), the probability of a value falling into a collection of possibilities is the sum of their individual probabilities <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>. However, for continuous contexts, the rules shift: the probability of falling into a range is no longer the sum of individual probabilities, but rather the area under the PDF <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>.

This transition from sums to areas naturally leads to the use of [[application_of_integrals_in_real_world_problems | integrals]] from calculus <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a> <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>. An integral is the mathematical tool used to find the area under a curve <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>.

> [!NOTE] Mathematical Foundations
> The shift in rules between finite/countable settings and continuous settings is rigorously addressed by a field of mathematics called **measure theory** <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a> <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>. Measure theory provides a unified framework for associating numbers (like probabilities) to subsets of possibilities <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>. It even provides a more powerful definition of integrals <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>.

## Application to the Coin Problem

Returning to the original problem of the weighted coin with an unknown weight `h`:
The correct question to ask is, "What is the [[probability_density_and_distribution | probability density function]] that describes the value `h` after observing the outcomes of coin tosses?" <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a> <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>.

Once this PDF is determined, it can be used to answer practical questions, such as: "What is the probability that the true probability of flipping heads falls between 0.6 and 0.8?" <a class="yt-timestamp" data-t="00:09:23">[00:09:23]</a> <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>. This probability would be found by calculating the area under the derived PDF curve between 0.6 and 0.8.