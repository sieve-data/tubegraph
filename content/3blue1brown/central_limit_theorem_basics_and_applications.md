---
title: Central Limit Theorem basics and applications
videoId: zeJD6dqJ5lo
---

From: [[3blue1brown]] <br/> 

The [[central_limit_theorem | Central Limit Theorem]] (CLT) is a fundamental concept in probability theory that explains why certain distributions are so common <a class="yt-timestamp" data-t="01:05:00">[01:05:00]</a>. It demonstrates how, even with chaotic individual events, precise statements can be made about a large number of events <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>.

## Introduction: The Galton Board

A Galton board is a popular demonstration illustrating that even if a single event is random and has an unknowable outcome, the distribution of many events can be predicted <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. Specifically, it shows how the relative proportions for many different outcomes are distributed <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>. The Galton board demonstrates one of the most prominent distributions in probability: the [[connections_between_gaussian_distribution_and_the_central_limit_theorem | normal distribution]] (also known as a bell curve or a [[connections_between_gaussian_distribution_and_the_central_limit_theorem | Gaussian distribution]]) <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.

The [[connections_between_gaussian_distribution_and_the_central_limit_theorem | normal distribution]] is very common and appears in many unrelated contexts <a class="yt-timestamp" data-t="00:40:00">[00:40:00]</a>, such as:
*   The heights of a large number of people in a similar demographic <a class="yt-timestamp" data-t="00:46:00">[00:46:00]</a>.
*   The number of distinct prime factors for a large swath of very big natural numbers <a class="yt-timestamp" data-t="00:53:00">[00:53:00]</a>.

The [[central_limit_theorem | Central Limit Theorem]] is a key fact that explains the prevalence of the [[connections_between_gaussian_distribution_and_the_central_limit_theorem | normal distribution]] <a class="yt-timestamp" data-t="01:09:00">[01:09:00]</a>.

### Simplified Galton Board Model

To illustrate the CLT, a simplified model of the Galton board is used <a class="yt-timestamp" data-t="01:56:00">[01:56:00]</a>. In this model:
*   Each ball falls onto a central peg <a class="yt-timestamp" data-t="02:00:00">[02:00:00]</a>.
*   It has a 50-50 probability of bouncing left or right <a class="yt-timestamp" data-t="02:05:00">[02:05:00]</a>.
*   Each bounce is considered as adding one (+1) or subtracting one (-1) from its position <a class="yt-timestamp" data-t="02:09:00">[02:09:00]</a>.
*   The ball lands in the middle of the peg adjacent below it, repeating the 50-50 choice <a class="yt-timestamp" data-t="02:14:00">[02:14:00]</a>.
*   For a board with five rows, the final position is the sum of five random choices <a class="yt-timestamp" data-t="02:27:00">[02:27:00]</a>.

If many balls fall, the number of balls in each bucket gives a sense of its probability <a class="yt-timestamp" data-t="03:10:00">[03:10:00]</a>. For simple cases, the probabilities can be explicitly calculated, reminiscent of Pascal's triangle <a class="yt-timestamp" data-t="03:23:00">[03:23:00]</a>. However, the power of the CLT lies in its applicability beyond simple examples <a class="yt-timestamp" data-t="03:34:00">[03:34:00]</a>.

## Core Idea of the Central Limit Theorem

The basic idea of the [[central_limit_theorem | Central Limit Theorem]] is that if you increase the size of a sum of random numbers, the distribution describing where that sum will fall looks more and more like a bell curve <a class="yt-timestamp" data-t="03:56:00">[03:56:00]</a>.

### Random Variables and Their Sums

A random variable is a random process where each outcome is associated with a number <a class="yt-timestamp" data-t="04:19:00">[04:19:00]</a>.
*   **Example 1**: Each bounce off a peg on the Galton board is a random variable with outcomes -1 and +1 <a class="yt-timestamp" data-t="04:29:00">[04:29:00]</a>.
*   **Example 2**: Rolling a die is a random variable with six outcomes, each associated with a number <a class="yt-timestamp" data-t="04:38:00">[04:38:00]</a>.

The CLT deals with taking multiple samples of a random variable and adding them together <a class="yt-timestamp" data-t="04:45:00">[04:45:00]</a>. For instance, letting a ball bounce off multiple pegs or rolling many dice and summing the results <a class="yt-timestamp" data-t="04:50:00">[04:50:00]</a>. The theorem claims that as the size of this sum grows, its distribution will increasingly resemble a bell curve <a class="yt-timestamp" data-t="05:01:00">[05:01:00]</a>.

### Simulations and Observations

Simulations with dice rolls illustrate the CLT's generality <a class="yt-timestamp" data-t="06:10:00">[06:10:00]</a>. Even starting with a weighted die (a non-uniform distribution), the core idea holds <a class="yt-timestamp" data-t="06:20:00">[06:20:00]</a>.
*   With 10 distinct samples from a skewed distribution, the sum's distribution begins to look like a bell curve <a class="yt-timestamp" data-t="06:35:00">[06:35:00]</a>.
*   Comparing sums of 2, 5, 10, and 15 dice shows that as the number of dice in each sum increases, the resulting distribution becomes more symmetric and bell-shaped <a class="yt-timestamp" data-t="07:21:00">[07:21:00]</a>.
*   This emergence of symmetry from an asymmetric starting point is a key feature <a class="yt-timestamp" data-t="07:16:00">[07:16:00]</a>.
*   Even with an initial distribution where most probability is tied to extremes (e.g., 1 and 6 for a die), a bell curve shape still emerges for the sums <a class="yt-timestamp" data-t="08:07:00">[08:07:00]</a>.

To move beyond simulation artifacts, theoretical calculations are used to show the precise shape distributions take in the long run <a class="yt-timestamp" data-t="08:59:00">[08:59:00]</a>. For a uniform distribution (e.g., fair dice), calculating sums involves counting pairs that result in the same sum (similar to convolutions, but simpler) <a class="yt-timestamp" data-t="09:06:00">[09:06:00]</a>. For non-uniform distributions, a [[connections_between_gaussian_distribution_and_the_central_limit_theorem | convolution]] operation is used, which is a weighted version of the counting game <a class="yt-timestamp" data-t="09:51:00">[09:51:00]</a>.

As the size of the sum grows, the distributions:
*   Wander to the right <a class="yt-timestamp" data-t="11:17:00">[11:17:00]</a>.
*   Get more spread out and flatter <a class="yt-timestamp" data-t="11:20:00">[11:20:00]</a>.

## Quantitative Description: Mean and Standard Deviation

To describe the [[central_limit_theorem | Central Limit Theorem]] quantitatively, the concepts of mean and standard deviation are essential <a class="yt-timestamp" data-t="11:25:00">[11:25:00]</a>.

### Mean ($\mu$)

The mean, denoted by the Greek letter mu ($\mu$), captures the center of mass for a distribution <a class="yt-timestamp" data-t="11:43:00">[11:43:00]</a>. It's calculated as the expected value of a random variable, summing the product of each outcome's probability and its value <a class="yt-timestamp" data-t="11:51:00">[11:51:00]</a>.
*   If the mean of an initial distribution is $\mu$, the mean of the sum of $n$ such variables is $n \times \mu$ <a class="yt-timestamp" data-t="13:16:00">[13:16:00]</a>.

### Variance ($\sigma^2$) and Standard Deviation ($\sigma$)

Variance measures how spread out a distribution is <a class="yt-timestamp" data-t="12:10:00">[12:10:00]</a>. It is the expected value of the squared difference between each possible value and the mean <a class="yt-timestamp" data-t="12:20:00">[12:20:00]</a>. Squaring the difference ensures a positive number and simplifies mathematical operations <a class="yt-timestamp" data-t="12:31:00">[12:31:00]</a>.

Standard deviation, denoted by the Greek letter sigma ($\sigma$), is the square root of the variance <a class="yt-timestamp" data-t="12:53:00">[12:53:00]</a>. It can be interpreted more reasonably as a distance on a diagram <a class="yt-timestamp" data-t="12:59:00">[12:59:00]</a>.
*   A key fact is that the variance for the sum of independent random variables is the sum of their individual variances <a class="yt-timestamp" data-t="13:50:00">[13:50:00]</a>.
*   If you take $n$ realizations of the same random variable, the variance of their sum is $n$ times the original variance <a class="yt-timestamp" data-t="14:20:00">[14:20:00]</a>.
*   Consequently, the standard deviation of the sum is $\sqrt{n}$ times the original standard deviation <a class="yt-timestamp" data-t="14:29:00">[14:29:00]</a>. This means distributions spread out in proportion to the square root of the sum's size <a class="yt-timestamp" data-t="14:56:00">[14:56:00]</a>.

## The Normal Distribution Formula

The [[central_limit_theorem | Central Limit Theorem]] implies that distributions of sums approach a universal shape, which can be revealed by realigning distributions so their means line up and rescaling them so their standard deviations equal one <a class="yt-timestamp" data-t="15:04:00">[15:04:00]</a>. This universal shape is described by the [[connections_between_gaussian_distribution_and_the_central_limit_theorem | normal distribution]] formula.

The formula for a [[connections_between_gaussian_distribution_and_the_central_limit_theorem | normal distribution]] is built up as follows:
1.  **Exponential Decay**: `e` to the negative `x` squared (`e^(-x^2)`) creates a smooth bell-curve shape that decays in both directions <a class="yt-timestamp" data-t="16:06:00">[16:06:00]</a>.
2.  **Scaling and Squishing**: Introducing a constant `c` (e.g., `e^(-c*x^2)`) stretches or squishes the graph horizontally, allowing for narrower or wider bell curves <a class="yt-timestamp" data-t="16:38:00">[16:38:00]</a>.
3.  **Standard Deviation Parameter**: Reconfiguring the exponent to negative one-half times `x` divided by `sigma` squared (`-1/2 * (x/sigma)^2`) means that `sigma` will directly represent the standard deviation of the distribution <a class="yt-timestamp" data-t="17:20:00">[17:20:00]</a>.
4.  **Probability Density Function**: For the curve to be interpreted as a probability distribution (a probability density function), the area under the curve must equal 1 <a class="yt-timestamp" data-t="17:38:00">[17:38:00]</a>. The area under `e^(-x^2)` is $\sqrt{\pi}$ <a class="yt-timestamp" data-t="18:21:00">[18:21:00]</a>.
    *   To make the area 1, the function is divided by $\sqrt{\pi}$ <a class="yt-timestamp" data-t="18:35:00">[18:35:00]</a>.
    *   Considering the `sigma` parameter, the full constant factor required is `1 / (sigma * sqrt(2 * pi))` <a class="yt-timestamp" data-t="18:43:00">[18:43:00]</a>.
    *   The special case where `sigma = 1` is called the standard [[connections_between_gaussian_distribution_and_the_central_limit_theorem | normal distribution]] <a class="yt-timestamp" data-t="19:15:00">[19:15:00]</a>.
5.  **Mean Parameter**: Subtracting another constant `mu` from the variable `x` (`(x - mu)`) allows the graph to slide left or right, prescribing the mean of the distribution <a class="yt-timestamp" data-t="19:25:00">[19:25:00]</a>.

The complete formula for a [[connections_between_gaussian_distribution_and_the_central_limit_theorem | normal distribution]] with mean $\mu$ and standard deviation $\sigma$ is:
$f(x; \mu, \sigma) = \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{1}{2}\left(\frac{x-\mu}{\sigma}\right)^2}$ <a class="yt-timestamp" data-t="19:40:00">[19:40:00]</a>

The CLT states that the distribution of sums, when realigned to a mean of zero and rescaled to a standard deviation of one, tends towards this single universal shape, regardless of the initial distribution <a class="yt-timestamp" data-t="23:20:00">[23:20:00]</a>.

### Formal Statement of the CLT

The rigorous statement of the [[central_limit_theorem | Central Limit Theorem]] involves considering a value that represents "how many standard deviations away from the mean is the sum" <a class="yt-timestamp" data-t="24:12:00">[24:12:00]</a>.
The probability that this value falls between two real numbers, `a` and `b`, as the size of the sum (`n`) goes to infinity, is equal to a certain [[application_of_limits_in_integral_calculus | integral]] <a class="yt-timestamp" data-t="24:30:00">[24:30:00]</a>. This [[application_of_limits_in_integral_calculus | integral]] describes the area under a standard [[connections_between_gaussian_distribution_and_the_central_limit_theorem | normal distribution]] between those two values <a class="yt-timestamp" data-t="24:44:00">[24:44:00]</a>.

## Application Example: Sum of 100 Die Rolls

Consider rolling a fair die 100 times and adding the results <a class="yt-timestamp" data-t="25:07:00">[25:07:00]</a>. To find a range of values within which the sum is 95% sure to fall:

1.  **Initial Distribution Properties**:
    *   Mean ($\mu$) of a single fair die roll: (1/6 * 1) + (1/6 * 2) + ... + (1/6 * 6) = 3.5 <a class="yt-timestamp" data-t="26:07:00">[26:07:00]</a>.
    *   Standard Deviation ($\sigma$) of a single fair die roll (calculated from variance): 1.71 (variance = 2.92) <a class="yt-timestamp" data-t="26:19:00">[26:19:00]</a>.

2.  **Sum Distribution Properties (100 rolls)**:
    *   Mean of the sum: $100 \times \mu = 100 \times 3.5 = 350$ <a class="yt-timestamp" data-t="26:42:00">[26:42:00]</a>.
    *   Standard Deviation of the sum: $\sqrt{100} \times \sigma = 10 \times 1.71 = 17.1$ <a class="yt-timestamp" data-t="26:47:00">[26:47:00]</a>.

3.  **95% Range**: A common rule of thumb for [[connections_between_gaussian_distribution_and_the_central_limit_theorem | normal distributions]] is that 95% of values fall within two standard deviations of the mean <a class="yt-timestamp" data-t="25:31:00">[25:31:00]</a>.
    *   Lower bound: $350 - (2 \times 17.1) \approx 316$ <a class="yt-timestamp" data-t="26:53:00">[26:53:00]</a>.
    *   Upper bound: $350 + (2 \times 17.1) \approx 384$ <a class="yt-timestamp" data-t="26:57:00">[26:57:00]</a>.
    *   Therefore, you can be 95% sure the sum will fall between 316 and 384 <a class="yt-timestamp" data-t="27:07:00">[27:07:00]</a>.

If the sum is divided by 100, it represents the empirical average of 100 die rolls <a class="yt-timestamp" data-t="27:21:00">[27:21:00]</a>. The interval then indicates the range you expect to see for that average <a class="yt-timestamp" data-t="27:37:00">[27:37:00]</a>. The [[central_limit_theorem | Central Limit Theorem]] allows computation of how close this empirical average will be to the expected value (3.5) <a class="yt-timestamp" data-t="27:51:00">[27:51:00]</a>.

## Assumptions of the Central Limit Theorem

The [[central_limit_theorem | Central Limit Theorem]] relies on three key assumptions:

1.  **Independence**: All variables being added must be independent from each other; the outcome of one process does not influence another <a class="yt-timestamp" data-t="28:18:00">[28:18:00]</a>.
2.  **Identically Distributed**: All variables must be drawn from the same distribution <a class="yt-timestamp" data-t="28:27:00">[28:27:00]</a>.
    *   These first two assumptions are often combined as "IID" (Independent and Identically Distributed) <a class="yt-timestamp" data-t="28:42:00">[28:42:00]</a>.
    *   The real Galton board actually violates these assumptions, as a ball's trajectory after one peg influences the next <a class="yt-timestamp" data-t="28:50:00">[28:50:00]</a>. Despite this, a [[connections_between_gaussian_distribution_and_the_central_limit_theorem | normal distribution]] still emerges, possibly due to generalizations of the theorem <a class="yt-timestamp" data-t="29:38:00">[29:38:00]</a>.
3.  **Finite Variance**: The variance computed for the variables must be finite <a class="yt-timestamp" data-t="30:04:00">[30:04:00]</a>.
    *   This is not an issue for discrete outcomes like dice rolls <a class="yt-timestamp" data-t="30:10:00">[30:10:00]</a>.
    *   However, some distributions with an infinite set of outcomes can have an infinite variance <a class="yt-timestamp" data-t="30:15:00">[30:15:00]</a>. In such cases, even if the first two assumptions hold, the sum might not tend towards a [[connections_between_gaussian_distribution_and_the_central_limit_theorem | normal distribution]] <a class="yt-timestamp" data-t="30:27:00">[30:27:00]</a>.