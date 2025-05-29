---
title: Probability density functions
videoId: Fvi9A_tEmXQ
---

From: [[khanacademy]] <br/> 

A probability density function (PDF) is a function used to describe the probability distribution of a continuous random variable <a class="yt-timestamp" data-t="01:29:49">[01:29:49]</a>. Unlike discrete random variables, which take on a finite number of values <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>, continuous random variables can take on an infinite number of values within a given range <a class="yt-timestamp" data-t="00:28:57">[00:28:57]</a>.

## Understanding Continuous Random Variables

Consider a random variable, Y, representing the exact amount of rain tomorrow <a class="yt-timestamp" data-t="00:48:15">[00:48:15]</a>. This is a continuous variable because the amount of rain could be 2 inches, 2.01 inches, 1.999 inches, and so on, infinitely precisely <a class="yt-timestamp" data-t="00:31:54">[00:31:54]</a>.

### Probability of an Exact Value

For a continuous random variable, the probability of it taking on any *exact* specific value is essentially zero <a class="yt-timestamp" data-t="03:47:00">[03:47:00]</a>. For example, the probability of getting *exactly* 2 inches of rain (not 2.000001 or 1.99999) is 0 <a class="yt-timestamp" data-t="03:13:00">[03:13:00]</a>.

This can be understood by analogy:
> "It's like asking you what's the area of a line? An area of a line, if you were to just draw a line, you'd say well, area is height times base. Well the height has some dimension, but the base, what's the width the a line? As far as the way we've defined a line, a line has no with, and therefore no area." <a class="yt-timestamp" data-t="06:40:48">[06:40:48]</a>

## [[calculating_probability | Calculating Probability]] with PDFs

Instead of asking for an exact value, [[calculating_probabilities_for_specific_outcomes | probability]] for a continuous random variable is determined over a range or interval <a class="yt-timestamp" data-t="04:29:00">[04:29:00]</a>.

The probability for a continuous random variable to fall within a specific range is represented by the **area under the curve** of its probability density function within that range <a class="yt-timestamp" data-t="05:24:00">[05:24:00]</a>.

For instance, to find the probability that the amount of rain (Y) is between 1.9 and 2.1 inches, one would calculate the area under the PDF curve from 1.9 to 2.1 <a class="yt-timestamp" data-t="05:14:00">[05:14:00]</a>.

### Using Integrals to [[calculating_probability_using_integrals | Calculate Probability]]

In calculus, the area under a curve is found using an integral <a class="yt-timestamp" data-t="03:33:00">[03:33:00]</a>. If `f(x)` defines the probability density function, the probability that a random variable `Y` is between `a` and `b` is given by the definite integral of `f(x)` from `a` to `b` <a class="yt-timestamp" data-t="05:37:00">[05:37:00]</a>:

$$ P(a \le Y \le b) = \int_{a}^{b} f(x) \,dx $$ <a class="yt-timestamp" data-t="06:06:00">[06:06:00]</a>

This concept is crucial for [[understanding_probability_concepts | understanding probability concepts]] when dealing with continuous data, such as the [[normal_distribution | normal distribution]] <a class="yt-timestamp" data-t="02:22:56">[02:22:56]</a>.

## [[properties_of_probability_distributions | Properties of Probability Distributions]]

For any valid [[probability_distribution_functions | probability distribution function]], whether discrete or continuous, the sum of all probabilities for all possible outcomes must equal 1 (or 100%) <a class="yt-timestamp" data-t="08:03:00">[08:03:00]</a>.

For a continuous random variable, this means the **total area under the entire probability density function curve must be equal to 1** <a class="yt-timestamp" data-t="08:17:00">[08:17:00]</a>. If the function `f(x)` describes the PDF from 0 to infinity (representing all possible outcomes), then:

$$ \int_{0}^{\infty} f(x) \,dx = 1 $$ <a class="yt-timestamp" data-t="08:22:00">[08:22:00]</a>

This is analogous to discrete probability distributions, where the sum of probabilities for all outcomes must also equal 1 <a class="yt-timestamp" data-t="08:41:00">[08:41:00]</a>. For example, with a coin toss, the probability of heads (0.5) plus the probability of tails (0.5) equals 1 <a class="yt-timestamp" data-t="09:13:00">[09:13:00]</a>. If the probabilities exceeded 1 (e.g., 0.6 for heads and 0.6 for tails), it would imply a 120% probability, which makes no sense <a class="yt-timestamp" data-t="09:20:00">[09:20:00]</a>. This fundamental rule is key to [[introduction_to_probability | introductory probability]] and [[probability_in_inferential_statistics | probability in inferential statistics]].