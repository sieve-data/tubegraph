---
title: Central Limit Theorem fundamentals
videoId: zeJD6dqJ5lo
---

From: [[3blue1brown]] <br/> 

The Central Limit Theorem (CLT) is considered one of the "crown jewels" in probability theory <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. It explains why the normal distribution, also known as a bell curve or Gaussian distribution, appears so commonly in various, seemingly unrelated contexts <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.

## Introduction

A Galton board serves as a popular demonstration of how, even with chaotic and random single events, it is possible to make precise statements about a large number of events <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. Specifically, it illustrates how the relative proportions for many different outcomes are distributed <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>.

The normal distribution is, as its name suggests, very common <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. For example, if you plot the heights of a large number of people from a similar demographic, their heights tend to follow a normal distribution <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>. Similarly, the number of distinct prime factors for a large swath of very big natural numbers closely tracks a certain normal distribution <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>. The CLT is a key fact that explains this widespread occurrence <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>.

This lesson aims to provide the fundamental understanding of what the Central Limit Theorem is saying and what normal distributions are, assuming minimal background <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.

## Simplified Galton Board Model

To illustrate the CLT, consider a simplified model of a Galton board <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>:
*   Each ball falls onto a central peg <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.
*   It has a 50-50 probability of bouncing left or right <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>.
*   These outcomes are thought of as adding one (+1) or subtracting one (-1) from its position <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.
*   The ball lands in the middle of an adjacent peg below, facing the same 50-50 choice <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.

For a board with five rows of pegs, the ball makes five random choices between +1 and -1 <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>. Its final position is the sum of these five random numbers <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>. The goal of this idealized model is to give a simple example illustrating the Central Limit Theorem, not to accurately model physics <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.

If many different balls fall (assuming they don't influence each other), the number of balls in each bucket gives a loose sense of how likely each bucket is <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>. Calculating these probabilities for simple cases is reminiscent of Pascal's triangle <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.

The basic idea of the Central Limit Theorem is that if you increase the size of that sum (e.g., increasing the number of rows of pegs), the distribution describing where that sum will fall looks more and more like a bell curve <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.

## The General Idea of the Central Limit Theorem

A **random variable** is a random process where each outcome is associated with some number <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>. Examples include:
*   A bounce off a peg, associated with numbers -1 and +1 <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>.
*   Rolling a die, with six outcomes each associated with a number <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>.

The core claim of the Central Limit Theorem is that if you take multiple samples of a random variable and add them together, as the size of that sum gets bigger, the distribution of that sum (how likely it is to fall into different values) will look more and more like a bell curve <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.

For instance, if you rolled a die 100 times and added the results, the CLT allows you to find a range of values within which you are 95% sure the sum will fall <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>. This holds true whether the die is fair or weighted <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>. The theorem relies on three [[assumptions_and_limitations_of_the_central_limit_theorem|assumptions]] which will be discussed later <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>.

### Simulations with Dice

Simulations with dice demonstrate the CLT's generality <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>. Even if you start with a weighted die, where outcomes are not equally probable, the core idea still holds <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a>.
*   When summing a small number of dice (e.g., two), the resulting distribution may still resemble the skewed initial distribution <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>.
*   However, as more dice are added to the sum, the resulting shape becomes more symmetric, with a lump in the middle and fade towards the tails, characteristic of a bell curve <a class="yt-timestamp" data-t="00:07:52">[00:07:52]</a>.
*   This emergence of a bell curve occurs regardless of the initial distribution of a single die roll <a class="yt-timestamp" data-t="00:08:07">[00:08:07]</a>.

While simulations are illustrative, they can feel imprecise <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>. For a precise understanding, it's necessary to look at the theoretical shape these distributions take in the long run <a class="yt-timestamp" data-t="00:08:59">[00:08:59]</a>.

## Mean and Standard Deviation

When summing random variables, two key observations can be made about the resulting distributions <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>:
1.  They wander to the right (their center shifts) <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>.
2.  They become more spread out and flatter <a class="yt-timestamp" data-t="00:11:20">[00:11:20]</a>.

Quantitatively describing the CLT requires understanding the mean and standard deviation of these distributions <a class="yt-timestamp" data-t="00:11:25">[00:11:25]</a>.

### Mean (μ)
The mean of a distribution, denoted by the Greek letter mu (μ), captures the center of mass <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>. It is calculated as the expected value of the random variable: for each possible outcome, multiply its probability by its value, and sum these products <a class="yt-timestamp" data-t="00:11:51">[00:11:51]</a>.

If the mean of an initial distribution is μ, then the mean of a sum of *n* such independent variables is *n* times μ <a class="yt-timestamp" data-t="00:13:16">[00:13:16]</a>. This explains why the distributions "drift" to the right <a class="yt-timestamp" data-t="00:13:39">[00:13:39]</a>.

### Standard Deviation (σ) and Variance (σ²)
To measure how spread out a distribution is, variance and standard deviation are used <a class="yt-timestamp" data-t="00:12:10">[00:12:10]</a>.
*   **Variance (σ²)**: The expected value of the squared difference between each possible value and the mean <a class="yt-timestamp" data-t="00:12:18">[00:12:18]</a>. Squaring ensures positive numbers and simplifies the math <a class="yt-timestamp" data-t="00:12:31">[00:12:31]</a>.
*   **Standard Deviation (σ)**: The square root of the variance <a class="yt-timestamp" data-t="00:12:53">[00:12:53]</a>. It can be interpreted more reasonably as a distance on the distribution diagram <a class="yt-timestamp" data-t="00:12:59">[00:12:59]</a>.

A key fact is that the variance for the sum of two independent random variables is the sum of their individual variances <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a>. Therefore, if you take *n* different realizations of the same random variable, the variance of their sum is *n* times the variance of the original variable <a class="yt-timestamp" data-t="00:14:20">[00:14:20]</a>.

This implies that the standard deviation of the sum is the square root of *n* times the original standard deviation (σ√*n*) <a class="yt-timestamp" data-t="00:14:29">[00:14:29]</a>. This means distributions spread out, but not very quickly, only in proportion to the square root of the sum's size <a class="yt-timestamp" data-t="00:14:56">[00:14:56]</a>.

## The Normal Distribution Formula

To make the CLT quantitatively precise, we can realign all sum distributions so their means line up (at zero) and rescale them so their standard deviations equal one <a class="yt-timestamp" data-t="00:15:08">[00:15:08]</a>. When this is done, the resulting shape approaches a universal, elegant form <a class="yt-timestamp" data-t="00:15:21">[00:15:21]</a>.

The formula for a normal distribution's probability density function is <a class="yt-timestamp" data-t="00:15:57">[00:15:57]</a>:

$$f(x) = \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{1}{2}\left(\frac{x-\mu}{\sigma}\right)^2}$$

Let's break down its components <a class="yt-timestamp" data-t="00:16:01">[00:16:01]</a>:
*   $e^{-x^2}$: This provides the basic bell curve shape, decaying smoothly in both directions from a peak at zero <a class="yt-timestamp" data-t="00:16:29">[00:16:29]</a>.
*   $\left(\frac{x-\mu}{\sigma}\right)^2$:
    *   Subtracting $\mu$ (mean) from $x$ shifts the graph horizontally, allowing the peak to be at any desired mean <a class="yt-timestamp" data-t="00:19:29">[00:19:29]</a>.
    *   Dividing by $\sigma$ and squaring controls the horizontal stretch/squish of the curve. The constant $\sigma$ ultimately represents the standard deviation of the distribution <a class="yt-timestamp" data-t="00:16:38">[00:16:38]</a>.
*   $\frac{1}{\sigma\sqrt{2\pi}}$: This constant factor is a normalization constant that ensures the total area under the curve is 1 <a class="yt-timestamp" data-t="00:18:38">[00:18:38]</a>. The area under a probability density function represents the probability of a value falling within a range <a class="yt-timestamp" data-t="00:17:47">[00:17:47]</a>. The $\pi$ term appears because the integral of $e^{-x^2}$ from negative to positive infinity is $\sqrt{\pi}$ <a class="yt-timestamp" data-t="00:18:21">[00:18:21]</a>.

The special case where $\mu = 0$ and $\sigma = 1$ is called the **standard normal distribution** <a class="yt-timestamp" data-t="00:19:15">[00:19:15]</a>.

The magic of the CLT is that no matter how you start with any distribution for a single random variable, if you consider the distributions for the sums of many such variables, and then realign them by their means and rescale them by their standard deviations, they all approach this same universal bell curve shape <a class="yt-timestamp" data-t="00:15:30">[00:15:30]</a>. Even subtle changes to the initial distribution become "washed away" when summing a large number of instances <a class="yt-timestamp" data-t="00:23:31">[00:23:31]</a>.

### Formal Statement of the Central Limit Theorem

A formal statement of the CLT involves considering a sum of *n* instantiations of a variable, tweaked so its mean is zero and standard deviation is one (i.e., asking how many standard deviations away from the mean the sum is) <a class="yt-timestamp" data-t="00:21:02">[00:21:02]</a>:

The rigorous statement is that if you consider the probability that this standardized value falls between two given real numbers, *a* and *b*, and you consider the [[introduction_to_limits_in_calculus|limit]] of that probability as the size of your sum ($n$) goes to infinity, then that [[applications_and_interpretations_of_limits_in_calculus|limit]] is equal to a certain [[evaluating_integrals_and_the_role_of_the_convergence_point|integral]] <a class="yt-timestamp" data-t="00:24:25">[00:24:25]</a>. This [[evaluating_integrals_and_the_role_of_the_convergence_point|integral]] describes the area under a standard normal distribution between those two values <a class="yt-timestamp" data-t="00:24:40">[00:24:40]</a>.

## Applying the Central Limit Theorem: Die Roll Example

Let's revisit the problem: rolling a fair die 100 times and summing the results. Find the range within which you're 95% sure the sum will fall <a class="yt-timestamp" data-t="00:25:07">[00:25:07]</a>.

A handy rule of thumb for normal distributions states <a class="yt-timestamp" data-t="00:25:31">[00:25:31]</a>:
*   ~68% of values fall within one standard deviation ($\mu \pm 1\sigma$) of the mean.
*   ~95% of values fall within two standard deviations ($\mu \pm 2\sigma$) of the mean.
*   ~99.7% of values fall within three standard deviations ($\mu \pm 3\sigma$) of the mean.

**Steps to solve:**
1.  **Find the mean (μ) of a single die roll:** For a fair die, this is $(1/6 \times 1) + (1/6 \times 2) + \dots + (1/6 \times 6) = 3.5$ <a class="yt-timestamp" data-t="00:26:07">[00:26:07]</a>.
2.  **Find the standard deviation (σ) of a single die roll:** Calculate the variance by summing the squared differences between values and the mean. The variance is 2.92, so the standard deviation $\sigma = \sqrt{2.92} \approx 1.71$ <a class="yt-timestamp" data-t="00:26:19">[00:26:19]</a>.
3.  **Calculate the mean of the sum of 100 die rolls:** Since we're summing 100 independent rolls, the mean of the sum is $100 \times \mu = 100 \times 3.5 = 350$ <a class="yt-timestamp" data-t="00:26:42">[00:26:42]</a>.
4.  **Calculate the standard deviation of the sum of 100 die rolls:** The standard deviation of the sum is $\sqrt{100} \times \sigma = 10 \times 1.71 = 17.1$ <a class="yt-timestamp" data-t="00:26:47">[00:26:47]</a>.
5.  **Apply the 95% rule:** The range is $\mu_{sum} \pm 2 \times \sigma_{sum}$.
    *   Lower bound: $350 - (2 \times 17.1) = 350 - 34.2 = 315.8 \approx 316$ <a class="yt-timestamp" data-t="00:26:53">[00:26:53]</a>.
    *   Upper bound: $350 + (2 \times 17.1) = 350 + 34.2 = 384.2 \approx 384$ <a class="yt-timestamp" data-t="00:27:01">[00:27:01]</a>.

Thus, you are 95% sure the sum of 100 die rolls will fall within the range of 316 to 384 <a class="yt-timestamp" data-t="00:27:07">[00:27:07]</a>.

### Empirical Average

If you instead divide the sum of 100 die rolls by 100 (effectively calculating the empirical average), the range found for the sum can be interpreted as the expected range for that average <a class="yt-timestamp" data-t="00:27:18">[00:27:18]</a>. While the expected value for a single die roll is 3.5, the CLT allows you to compute how close to that expected value the empirical average will reasonably be <a class="yt-timestamp" data-t="00:27:44">[00:27:44]</a>.

## [[assumptions_and_limitations_of_the_central_limit_theorem|Assumptions and Limitations of the Central Limit Theorem]]

The Central Limit Theorem relies on three key [[assumptions_and_limitations_of_the_central_limit_theorem|assumptions]] <a class="yt-timestamp" data-t="00:28:12">[00:28:12]</a>:

1.  **Independence**: All variables being added up must be independent from each other; the outcome of one process does not influence another <a class="yt-timestamp" data-t="00:28:18">[00:28:18]</a>.
2.  **Identically Distributed**: All variables must be drawn from the same distribution <a class="yt-timestamp" data-t="00:28:27">[00:28:27]</a>.
    *   These two [[assumptions_and_limitations_of_the_central_limit_theorem|assumptions]] are often lumped together as IID (Independent and Identically Distributed) <a class="yt-timestamp" data-t="00:28:42">[00:28:42]</a>.
    *   The real Galton board violates these [[assumptions_and_limitations_of_the_central_limit_theorem|assumptions]] because bounces are not independent nor identically distributed <a class="yt-timestamp" data-t="00:28:50">[00:28:50]</a>. Despite this, a normal distribution often *does* emerge, potentially due to generalizations of the theorem that relax these conditions <a class="yt-timestamp" data-t="00:29:38">[00:29:38]</a>.
    *   It's important to caution against assuming a variable is normally distributed without justification <a class="yt-timestamp" data-t="00:29:54">[00:29:54]</a>.
3.  **Finite Variance**: The variance computed for these variables must be finite <a class="yt-timestamp" data-t="00:30:04">[00:30:04]</a>.
    *   This is not an issue for discrete outcomes like dice rolls <a class="yt-timestamp" data-t="00:30:10">[00:30:10]</a>.
    *   However, for some distributions with an infinite set of outcomes, the sum for variance can diverge to infinity <a class="yt-timestamp" data-t="00:30:15">[00:30:15]</a>. In such cases, even if the first two [[assumptions_and_limitations_of_the_central_limit_theorem|assumptions]] hold, the sum may not tend towards a normal distribution <a class="yt-timestamp" data-t="00:30:34">[00:30:34]</a>.