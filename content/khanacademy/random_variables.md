---
title: Random variables
videoId: Fvi9A_tEmXQ
---

From: [[khanacademy]] <br/> 

A [[random_variables_overview | random variable]] is a concept introduced to represent numerical outcomes of random phenomena <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. [[definition_of_a_random_variable | Random variables]] are typically denoted by capital letters, such as `Y` <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.

## Types of Random Variables

There are two main types of [[random_variables_overview | random variables]]: [[discrete_random_variables | discrete]] and [[continuous_random_variables | continuous]] <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>.

### [[discrete_random_variables | Discrete Random Variables]]

A [[discrete_random_variables | discrete random variable]] takes on a finite number of values <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. While they often tend to be integers, they do not always have to be <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. Crucially, a [[discrete_random_variables | discrete random variable]] cannot have an infinite number of values <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>.

For a [[discrete_random_variables | discrete random variable]], the sum of all possible probabilities must equal 1 <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>. For example, in a coin flip, the probability of getting heads plus the probability of getting tails must add up to 1 (e.g., 0.5 + 0.5 = 1, or 0.6 + 0.4 = 1) <a class="yt-timestamp" data-t="00:09:13">[00:09:13]</a>.

### [[continuous_random_variables | Continuous Random Variables]]

A [[continuous_random_variables | continuous random variable]] can take on an infinite number of values <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>.

#### Example: Exact Amount of Rain

Consider the [[continuous_random_variables | random variable]] `Y` representing the exact amount of rain tomorrow <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. If we consider a probability density function (PDF) for `Y`, where the x-axis represents inches of rain (e.g., 0, 1, 2, 3, 4 inches) <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>:

*   The probability that `Y` is *exactly* equal to 2 inches is essentially 0 <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>. This is because "exactly 2 inches" means not 2.01, not 1.99, not even 2.000001, but precisely 2 to an infinite decimal point <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.
*   Logically, it's virtually impossible for any physical measurement to be *exactly* a certain value due to the infinite possibilities between any two points <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.
*   Visually, on a probability density function, the probability of an exact value corresponds to the area of a line, which is zero, as a line has no width <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>.

#### Calculating Probability for [[continuous_random_variables | Continuous Random Variables]]

To calculate the probability for a [[continuous_random_variables | continuous random variable]], you must consider an interval rather than an exact point <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>.

For example, to find the probability that `Y` is "almost 2," meaning `Y` is between 1.9 and 2.1 inches (`1.9 < Y < 2.1`) <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>:
*   This probability is represented by the *area* under the probability density curve between these two points <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>.
*   In calculus terms, this area is the definite integral of the probability density function (`f(x)`) from 1.9 to 2.1 <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>:

> $$ \int_{1.9}^{2.1} f(x) \, dx $$ <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>

The concept of using area to represent probability is crucial for [[continuous_random_variables | continuous random variables]] <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>. The probability of any event is the area under the curve within the specified range <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>.

#### Total Probability

For any probability distribution, the total probability of all possible events occurring must be 1 (or 100%) <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>. For [[continuous_random_variables | continuous random variables]], this means the entire area under the probability density function curve, from its minimum to maximum possible value (often from negative infinity to positive infinity, or 0 to infinity for rain), must be equal to 1 <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>:

> $$ \int_{0}^{\infty} f(x) \, dx = 1 $$ <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>

This property ensures that the distribution is valid and covers all possible outcomes <a class="yt-timestamp" data-t="00:08:07">[00:08:07]</a>.