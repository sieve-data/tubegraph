---
title: Simulation of random processes and probability
videoId: zeJD6dqJ5lo
---

From: [[3blue1brown]] <br/> 

Simulation provides a powerful way to understand the behavior of random processes, especially when dealing with a large number of events where individual outcomes are chaotic and random <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. While single events may have effectively unknowable outcomes, simulations can demonstrate how the relative proportions for many different outcomes are distributed <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>.

## The Galton Board: A Core Example

The Galton board is a popular demonstration of probability distributions <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. It illustrates the normal distribution, also known as a bell curve or Gaussian distribution <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.

### Simplified Galton Board Model for Simulation

To illustrate key concepts like the Central Limit Theorem, a simplified model of the Galton board is often used <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>. In this model:
*   Each ball falls onto a central peg <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.
*   It has a 50-50 probability of bouncing to the left or to the right <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>.
*   These outcomes are thought of as adding one (+1) or subtracting one (-1) from its position <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.
*   After a bounce, it lands in the middle of an adjacent peg below, where the same 50-50 choice is repeated <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.

For a board with five rows of pegs, the ball makes five random choices between +1 and -1, and its final position is the sum of these numbers <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>. By letting many balls fall in a simulation, the number of balls in each bucket gives a loose sense of how likely each bucket is <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>. While explicit calculations can be made for simple cases (reminiscent of Pascal's triangle) <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>, simulating a large number of samples allows for an understanding of the distribution's shape <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>.

## Random Variables and Sums

A random variable is a random process where each outcome is associated with a number <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>. Examples include:
*   Each bounce off a peg on a Galton board (associated with -1 or +1) <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>.
*   Rolling a die (associated with numbers 1 through 6) <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>.

Simulations often involve taking multiple samples of a random variable and summing them together, such as letting a ball bounce off multiple pegs or rolling many dice and adding the results <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.

## The Central Limit Theorem (CLT) and Simulations

The Central Limit Theorem (CLT) is a cornerstone of probability theory <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. Its core idea is that as the size of the sum of independent, identically distributed random variables gets larger, the distribution of that sum will look more and more like a bell curve (normal distribution) <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.

### Simulating Dice Rolls

To illustrate the generality of the CLT, simulations can be run with dice <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>.
*   **Weighted Dice:** Even if starting with a weighted die that has a non-uniform or skewed distribution, the sum of multiple rolls will still tend towards a bell curve <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>.
    *   A simulation taking 10 samples from a skewed distribution and summing them, repeated many times, shows a bell curve shape emerging <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.
    *   Initially, with a sum of only two dice, the distribution may resemble the skewed starting distribution <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>.
    *   However, as more dice are added to the sum (e.g., 5, 10, 15), the resulting distribution becomes more symmetric and bell-shaped <a class="yt-timestamp" data-t="00:07:52">[00:07:52]</a>.
*   **Varying Initial Distributions:** The theorem holds regardless of the initial distribution of the individual random variable. For example, a die with most probability tied to 1 and 6, and low probability for mid-values, will still produce a bell curve for the sum of many rolls <a class="yt="yt-timestamp" data-t="00:08:07">[00:08:07]</a>.

Simulations effectively demonstrate order emerging from chaos <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>. However, they can sometimes appear "spiky" due to the randomness of the simulation, leading to questions about whether the observed shape is truly representative of the underlying distribution <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>. For precise understanding, theoretical calculations are necessary <a class="yt-timestamp" data-t="00:08:59">[00:08:59]</a>.

## Theoretical vs. Simulation Approaches

While simulations are great for illustration, theoretical calculations provide the precise shape of distributions in the long run <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>.
*   **Uniform Distribution:** For a fair die (uniform distribution, 1/6 probability for each face), the probability of different sums for a pair of dice can be found by counting distinct pairs that sum to the same value <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>. This is effectively a counting game, often visualized with diagonals on a grid <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>.
*   **Non-Uniform Distribution:** For a non-uniform distribution of a single die, calculating the sum distribution involves summing the probabilities of pairs, a process known as convolution <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>. The computer can perform these complex calculations to display the precise results <a class="yt-timestamp" data-t="00:10:25">[00:10:25]</a>.

### Quantifying Distributions: Mean and Standard Deviation

To describe the CLT quantitatively, it's essential to understand how distributions shift and spread out <a class="yt-timestamp" data-t="00:11:25">[00:11:25]</a>. This requires describing their [[understanding_mean_and_standard_deviation_in_probability | mean]] and standard deviation <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>.
*   **Mean (μ):** Represents the center of mass of a distribution, calculated as the expected value of the random variable <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>. For a sum of 'n' independent and identically distributed (IID) variables, the mean of the sum is 'n' times the mean of a single variable <a class="yt-timestamp" data-t="00:13:33">[00:13:33]</a>.
*   **Variance (σ²):** Measures how spread out a distribution is by taking the expected value of the squared difference between each possible value and the mean <a class="yt-timestamp" data-t="00:12:18">[00:12:18]</a>. For two independent random variables, the variance of their sum is the sum of their individual variances <a class="yt-timestamp" data-t="00:13:53">[00:13:53]</a>. Thus, for 'n' IID variables, the variance of the sum is 'n' times the variance of the original variable <a class="yt-timestamp" data-t="00:14:20">[00:14:20]</a>.
*   **Standard Deviation (σ):** The square root of the variance, interpretable as a distance on a diagram <a class="yt-timestamp" data-t="00:12:53">[00:12:53]</a>. For 'n' IID variables, the standard deviation of the sum is the square root of 'n' times the original standard deviation <a class="yt-timestamp" data-t="00:14:29">[00:14:29]</a>. This indicates that distributions spread out relatively slowly, proportional to the square root of the sum's size <a class="yt-timestamp" data-t="00:14:56">[00:14:56]</a>.

### The Normal Distribution Formula

The general idea of the CLT is to realign distributions so their means line up and rescale them so their standard deviations equal one <a class="yt-timestamp" data-t="00:15:08">[00:15:08]</a>. When this is done, the shape approaches a universal form described by the normal distribution function <a class="yt-timestamp" data-t="00:15:21">[00:15:21]</a>.

The formula for a normal distribution, with mean (μ) and standard deviation (σ), is:
$f(x) = \frac{1}{\sigma\sqrt{2\pi}}e^{-\frac{1}{2}\left(\frac{x-\mu}{\sigma}\right)^2}$ <a class="yt-timestamp" data-t="00:19:06">[00:19:06]</a>, <a class="yt-timestamp" data-t="00:19:40">[00:19:40]</a>

*   The term $e^{-x^2}$ provides the basic bell curve shape <a class="yt-timestamp" data-t="00:16:32">[00:16:32]</a>, <a class="yt-timestamp" data-t="00:16:36">[00:16:36]</a>.
*   The $\frac{x-\mu}{\sigma}$ part standardizes the variable, making it zero-mean and unit standard deviation <a class="yt-timestamp" data-t="00:21:02">[00:21:02]</a>, <a class="yt-timestamp" data-t="00:21:06">[00:21:06]</a>.
*   The factor $\frac{1}{\sigma\sqrt{2\pi}}$ is a normalization constant that ensures the total area under the curve is 1, a requirement for probability density functions <a class="yt-timestamp" data-t="00:17:38">[00:17:38]</a>, <a class="yt-timestamp" data-t="00:18:56">[00:18:56]</a>. The appearance of $\pi$ in this formula is a curious and deeper mathematical connection <a class="yt-timestamp" data-t="00:18:28">[00:18:28]</a>.

The special case where $\mu=0$ and $\sigma=1$ is called the **standard normal distribution** <a class="yt-timestamp" data-t="00:19:15">[00:19:15]</a>.

## Applications and Practical Use

When dealing with sums of random variables, knowing the mean (μ) and standard deviation (σ) of the underlying variable is enough to predict the mean and standard deviation of the sum, and thus, the parameters of the resulting normal distribution <a class="yt-timestamp" data-t="00:20:10">[00:20:10]</a>.

The formal statement of the Central Limit Theorem specifies that the probability of the standardized sum falling between two values (a and b) approaches an [[integrals_and_probability_distributions | integral]] of the standard normal distribution as the number of terms in the sum approaches infinity <a class="yt-timestamp" data-t="00:24:25">[00:24:25]</a>. This integral represents the area under the standard normal curve between those values <a class="yt-timestamp" data-t="00:24:40">[00:24:40]</a>. This is an example of the [[applications_of_probability_density | applications of probability density]].

### Example: Sum of 100 Die Rolls

If a fair die is rolled 100 times and the results are added together:
1.  **Mean of a single die roll (μ):** (1+2+3+4+5+6)/6 = 3.5 <a class="yt-timestamp" data-t="00:26:12">[00:26:12]</a>.
2.  **Standard deviation of a single die roll (σ):** Calculated from the variance (2.92), it is approximately 1.71 <a class="yt-timestamp" data-t="00:26:19">[00:26:19]</a>.
3.  **Mean of the sum of 100 rolls:** $100 \times \mu = 100 \times 3.5 = 350$ <a class="yt-timestamp" data-t="00:26:42">[00:26:42]</a>.
4.  **Standard deviation of the sum of 100 rolls:** $\sqrt{100} \times \sigma = 10 \times 1.71 = 17.1$ <a class="yt-timestamp" data-t="00:26:47">[00:26:47]</a>.

Using the rule of thumb that 95% of values in a normal distribution fall within two standard deviations of the mean <a class="yt-timestamp" data-t="00:25:39">[00:25:39]</a>:
*   Lower bound: $350 - (2 \times 17.1) = 315.8$ (approx. 316) <a class="yt-timestamp" data-t="00:26:57">[00:26:57]</a>.
*   Upper bound: $350 + (2 \times 17.1) = 384.2$ (approx. 384) <a class="yt-timestamp" data-t="00:27:01">[00:27:01]</a>.

Thus, one can be 95% sure that the sum of 100 fair die rolls will fall between 316 and 384 <a class="yt-timestamp" data-t="00:27:07">[00:27:07]</a>. This principle also applies to the empirical average of die rolls, where the standard deviation of the average decreases as the sample size increases <a class="yt-timestamp" data-t="00:27:18">[00:27:18]</a>.

## Assumptions of the Central Limit Theorem

The Central Limit Theorem relies on three key assumptions:
1.  **Independence:** All variables being summed must be independent of each other, meaning the outcome of one process does not influence another <a class="yt-timestamp" data-t="00:28:18">[00:28:18]</a>.
2.  **Identically Distributed:** All variables must be drawn from the same probability distribution <a class="yt-timestamp" data-t="00:28:27">[00:28:27]</a>.
    *   These first two assumptions are often lumped together as IID (Independent and Identically Distributed) <a class="yt-timestamp" data-t="00:28:42">[00:28:42]</a>.
    *   The real Galton board, for example, violates these assumptions, as bounces are not independent nor identically distributed <a class="yt-timestamp" data-t="00:28:50">[00:28:50]</a>. Despite this, it still appears to produce a normal distribution, possibly due to generalizations of the theorem <a class="yt-timestamp" data-t="00:29:41">[00:29:41]</a>.
3.  **Finite Variance:** The variance of the individual random variables must be finite <a class="yt-timestamp" data-t="00:30:06">[00:30:06]</a>.
    *   This is not an issue for discrete outcomes like dice rolls <a class="yt-timestamp" data-t="00:30:10">[00:30:10]</a>.
    *   However, for distributions with an infinite set of outcomes where the sum for variance might diverge to infinity, the sum of variables may not tend towards a normal distribution <a class="yt-timestamp" data-t="00:30:15">[00:30:15]</a>.

It is important to be cautious and avoid assuming a variable is normally distributed without justification, as the CLT's applicability depends on these assumptions <a class="yt-timestamp" data-t="00:29:54">[00:29:54]</a>.