---
title: Applications of probability density
videoId: ZA4JkHKZM50
---

From: [[3blue1brown]] <br/> 

When dealing with probabilities involving continuous values, such as the true probability of a weighted coin landing heads (denoted as `h`), a unique challenge arises <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>. Unlike discrete events (like flipping a coin a finite number of times), a continuous variable `h` can take on an uncountably infinite number of values between 0 and 1 <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.

## The Paradox of Continuous Probabilities

Consider asking for the probability that `h` is *precisely* 0.7, as opposed to 0.7000001 or any other nearby value <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>. If every specific value within a continuous range had a non-zero probability, even a minuscule one, adding them all up would result in an infinite total probability, which contradicts the fundamental rule that total probability must be 1 <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>. Conversely, if all individual probabilities were 0, their sum would also be 0, again contradicting the requirement that the total probability of `h` being *some* value must be 1 <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>. This presents an apparent paradox <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.

## Resolving the Paradox with Probability Density

The solution to this paradox involves a shift in how probability is conceptualized for continuous variables <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.

### Focus on Ranges, Not Individual Values

Instead of focusing on the probability of individual values, it's more meaningful to consider the probability that a continuous variable falls within a *range* of values <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>. For example, one might ask for the probability that `h` is between 0.8 and 0.85 <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.

### Area as Probability

Crucially, in the context of continuous variables, the *area* under a curve represents probability, not the height of individual bars <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>. This is illustrated by imagining probabilities for ranges represented as buckets. As these buckets become finer and finer, approaching an infinitely thin width, they form a smooth curve <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>. If height represented probability, everything would go to zero, but if area represents probability, the overall shape of the distribution is preserved and refined <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>.

### Probability Density Function (PDF)

The y-axis in this context no longer represents probability directly <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>. Instead, it represents **probability density**—a kind of probability per unit in the x-direction <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>.

When plotting this continuous curve, it's known as a [[probability_density_function_pdf | Probability Density Function (PDF)]] <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>. The fundamental interpretation of a PDF is that the probability of a random variable lying between two values is equal to the area under its curve between those values <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>.

*   The probability of getting one very specific number (e.g., 0.7) is 0, because the area of an infinitely thin slice is 0 <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.
*   The total area under the entire PDF curve must equal 1, as this represents the total probability of the variable taking *any* possible value <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>. This resolves the initial paradox <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.

### The Shift in Rules

The core shift for continuous settings is that the probability of falling into a range of values is no longer simply the sum of the probabilities of each individual value <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>. Instead, probabilities associated with ranges are the fundamental objects, and an individual value can be conceived as a range of width 0 <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>.

### Connection to [[measure_theory_in_probability | Measure Theory]] and [[Integrals and probability distributions | Integrals]]

This conceptual framework is rigorously formalized in [[measure_theory_in_probability | measure theory]], a field of mathematics that provides a unified way to associate numbers (like probabilities) with subsets of all possibilities, whether discrete or continuous <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>.

A common rule of thumb in probability is that if a sum is used in a discrete context, an [[Integrals and probability distributions | integral]] is used in a continuous context <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>. Integrals are the calculus tool used to find areas under curves <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>. The theoretical underpinnings of [[Integrals and probability distributions | integrals]] also connect to [[measure_theory_in_probability | measure theory]] <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>.

## Practical Application

For problems like determining the unknown weight `h` of a coin after observing several flips, the appropriate question to ask is: What is the [[probability_density_function_pdf | probability density function]] that describes `h` after seeing the outcomes? <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a> Once this PDF is found, it can be used to answer questions about the probability that `h` falls within a specific range, such as between 0.6 and 0.8 <a class="yt-timestamp" data-t="00:09:23">[00:09:23]</a>.