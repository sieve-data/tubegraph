---
title: Calculating probability using integrals
videoId: Fvi9A_tEmXQ
---

From: [[khanacademy]] <br/> 

In [[introduction_to_probability|probability]] and statistics, [[random_variable|random variables]] are quantities whose values are subject to variations due to chance. There are two main types of [[random_variable|random variables]] <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>:

*   **Discrete Random Variables**: These take on a finite number of values, often integers, but not exclusively <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. For example, the outcome of a coin flip (heads or tails) is a discrete variable.
*   **Continuous Random Variables**: These can take on an infinite number of values within a given range <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>. An example is the exact amount of rain tomorrow, which could be 2 inches, 2.01 inches, 2.0001 inches, and so on <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.

[[quantifying_outcomes_for_probability|Quantifying outcomes for probability]] for continuous variables differs significantly from discrete ones.

## The Challenge of Exact Probabilities

For a continuous random variable, such as the amount of rain (Y), the [[calculating_probabilities_for_specific_outcomes|probability of any exact value]] is essentially zero <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.

Imagine trying to determine the probability that it will rain *exactly* 2 inches tomorrow (not 2.01, not 1.99, but precisely 2.000... with infinite precision) <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>. Since there's an infinite number of possible values around 2 inches, the chance of hitting that *exact* point is negligible <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>.

This concept can be compared to the "area of a line." A line has no width, and therefore no area <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>. Similarly, a single point on a continuous scale has no "width" and thus no associated probability mass.

## Using Intervals and Area Under the Curve

Instead of asking for the probability of an exact value, for continuous random variables, we typically ask for the [[calculating_probability|probability]] that the variable falls within a certain interval <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>.

For example, instead of asking for the probability of exactly 2 inches of rain, we might ask for the probability that the amount of rain (Y) is between 1.9 inches and 2.1 inches <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>. This represents an interval rather than a single point.

### Probability Density Functions (PDFs)

For continuous random variables, their [[probability_density_functions|probability distribution functions]] are referred to as **probability density functions (PDFs)** <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>. When plotted, the x-axis represents the possible values of the variable (e.g., amount of rain), and the curve's height at any point indicates the probability density at that point <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.

To find the [[calculating_probability|probability]] that a continuous random variable falls within a specific interval, you need to calculate the **area under the curve** of its [[probability_density_functions|probability density function]] over that interval <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.

### The Role of Integrals

For those familiar with calculus, the area under a curve is calculated using a definite integral <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.

If the [[probability_density_functions|probability density function]] is defined as `f(x)`, the [[calculating_probability|probability]] that a random variable `Y` falls between `a` and `b` is given by the integral:

$$ P(a \le Y \le b) = \int_{a}^{b} f(x) \,dx $$ <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>

For instance, to find the probability of rain between 1.9 and 2.1 inches, you would integrate the rain's PDF from 1.9 to 2.1 <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>.

Similarly, if you want the probability of less than 0.1 inches of rain, you would integrate from 0 to 0.1 <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>. For more than 4 inches, you would integrate from 4 to infinity <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>.

## Total Probability

A fundamental principle in [[understanding_probability_concepts|probability]] is that the sum of all possible probabilities must equal 1 (or 100%) <a class="yt-timestamp" data-t="00:08:07">[00:08:07]</a>.

*   For discrete random variables, this means that if you sum the probabilities of all possible outcomes, the total must be 1 <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>, <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>. For example, for a coin flip, P(Heads) + P(Tails) must equal 1 <a class="yt-timestamp" data-t="00:09:19">[00:09:19]</a>.

*   For continuous random variables, this translates to the **total area under the [[probability_density_functions|probability density function]] equalling 1** <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>, <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>. This means if you integrate the PDF over all possible values (from negative infinity to positive infinity, or from 0 to infinity for non-negative quantities like rain), the result must be 1:

$$ \int_{-\infty}^{\infty} f(x) \,dx = 1 $$ <a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a>

This concept is crucial for [[probability_in_inferential_statistics|probability in inferential statistics]] and [[calculating_probability_using_zscore|calculating probability using Z-score]], where the area under the curve (often a normal distribution) represents the probability of an event occurring within a range.