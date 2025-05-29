---
title: Normal distribution and its properties
videoId: zeJD6dqJ5lo
---

From: [[3blue1brown]] <br/> 

The normal distribution, also known as a bell curve or a [[connection_between_gaussian_distribution_and_probability | Gaussian distribution]], is one of the most prominent distributions in all of [[probability_density_and_distribution | probability]] <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>. Even when individual events are chaotic and random, it's possible to make precise statements about a large number of events, particularly how their outcomes are distributed <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>.

This distribution is common and appears in various seemingly unrelated contexts <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. For example, if you plot the heights of a large number of people in a similar demographic, those heights tend to follow a normal distribution <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>. Similarly, the number of distinct prime factors for a large swath of very big natural numbers closely tracks a certain normal distribution <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.

The [[central_limit_theorem | Central Limit Theorem]] (CLT) is a key concept in probability theory that explains why the normal distribution is so common <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.

## Illustrating with the Galton Board

A Galton board is a popular demonstration that illustrates the normal distribution <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>, <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.

### Simplified Model

An overly simplified model of the Galton board helps illustrate the [[central_limit_theorem | Central Limit Theorem]] <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>:
*   Each ball falls onto a central peg <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.
*   It has a 50-50 chance of bouncing to the left (-1) or to the right (+1) <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>.
*   After a choice, it lands in the middle of an adjacent peg below, where it again faces the 50-50 choice <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.
*   For a board with five rows, the ball makes five random choices between +1 and -1 <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.
*   The final position of the ball is essentially the sum of these numbers <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.
*   Repeating this process for many balls gives a sense of how likely each bucket (representing a sum) is <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>, <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.
*   The numbers are simple enough to explicitly calculate probabilities, which are reminiscent of Pascal's triangle <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>, <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.

The core idea of the [[central_limit_theorem | Central Limit Theorem]] is that as the size of the sum increases (e.g., more rows of pegs), the distribution describing where that sum will fall looks more and more like a bell curve <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>, <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.

### [[simulation_examples_of_probability_distribution | Simulations]] of Sums

A random variable is a random process where each outcome is associated with a number <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>. For instance, a peg bounce gives -1 or +1 <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>, or rolling a die gives 1-6 <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>. The [[central_limit_theorem | Central Limit Theorem]] claims that as you add together more samples of a random variable, the [[probability_density_and_distribution | distribution]] of that sum increasingly resembles a bell curve <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>, <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.

This holds true even for starting distributions that are not uniform, such as a weighted die <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a>, <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>. For example, if a die's [[probability_density_and_distribution | distribution]] is skewed towards lower values, sums of 10 samples from it will still emerge as a bell curve, albeit slightly skewed <a class="yt-timestamp" data-t="00:06:35">[00:06:35]</a>, <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>. As the number of dice in each sum increases (e.g., from 2 to 15), the resulting distribution becomes more and more symmetric and bell-shaped <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>. This phenomenon also occurs if the initial [[probability_density_and_distribution | distribution]] is bimodal (e.g., most probability on 1 and 6) <a class="yt-timestamp" data-t="00:08:07">[00:08:07]</a>.

## Mean and Standard Deviation

To describe the [[central_limit_theorem | Central Limit Theorem]] quantitatively, it's necessary to understand the concepts of mean and standard deviation <a class="yt-timestamp" data-t="00:11:25">[00:11:25]</a>.

### Mean (μ)

The mean of a [[probability_density_and_distribution | distribution]], denoted by the Greek letter mu (μ), captures its center of mass <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>. It's calculated as the expected value of a random variable, which is the sum of (probability of outcome × value of variable) for all possible outcomes <a class="yt-timestamp" data-t="00:11:51">[00:11:51]</a>.

If the mean of an initial [[probability_density_and_distribution | distribution]] is μ, then the mean of the sum of *n* such variables will be *n* times μ <a class="yt-timestamp" data-t="00:13:16">[00:13:16]</a>. This explains why distributions of sums drift to the right <a class="yt-timestamp" data-t="00:13:39">[00:13:39]</a>.

### Variance and Standard Deviation (σ)

To measure how spread out a [[probability_density_and_distribution | distribution]] is, variance and standard deviation are used <a class="yt-timestamp" data-t="00:12:10">[00:12:10]</a>.
*   **Variance:** Calculated by taking the expected value of the squared difference between each possible value and the mean <a class="yt-timestamp" data-t="00:12:20">[00:12:20]</a>. Squaring ensures positive numbers and simplifies the math <a class="yt-timestamp" data-t="00:12:31">[00:12:31]</a>.
*   **Standard Deviation (σ):** Denoted by the Greek letter sigma (σ), it's the square root of the variance <a class="yt-timestamp" data-t="00:12:53">[00:12:53]</a>. This provides a measure of spread that can be interpreted as a distance <a class="yt-timestamp" data-t="00:12:59">[00:12:59]</a>.

A key fact is that the variance for the sum of independent random variables is the sum of their individual variances <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a>. If you sum *n* independent realizations of the same random variable, the variance of the sum is *n* times the variance of the original variable <a class="yt-timestamp" data-t="00:14:20">[00:14:20]</a>. Consequently, the standard deviation of the sum is the square root of *n* times the original standard deviation (σ√*n*) <a class="yt-timestamp" data-t="00:14:29">[00:14:29]</a>. This means distributions spread out more slowly than their mean drifts <a class="yt-timestamp" data-t="00:14:56">[00:14:56]</a>.

## The Normal Distribution Formula

The general idea of the [[central_limit_theorem | Central Limit Theorem]] is that if you realign all distributions of sums so their means line up and then rescale them so their standard deviations are 1, they approach a certain universal shape <a class="yt-timestamp" data-t="00:15:08">[00:15:08]</a>, <a class="yt-timestamp" data-t="00:15:30">[00:15:30]</a>. This shape is described by the normal distribution formula <a class="yt-timestamp" data-t="00:15:54">[00:15:54]</a>.

The building blocks of the formula:
*   **Exponential Decay:** `e^(-x)` describes exponential decay <a class="yt-timestamp" data-t="00:16:06">[00:16:06]</a>.
*   **Symmetry:** Using `e^(-|x|)` creates decay in both directions with a sharp point <a class="yt-timestamp" data-t="00:16:18">[00:16:18]</a>. Using `e^(-x^2)` creates a smoother, basic bell curve shape decaying in both directions <a class="yt-timestamp" data-t="00:16:29">[00:16:29]</a>.
*   **Scaling (Standard Deviation):** Introducing a constant `c` (or equivalently, structuring as `e^(-1/2 * (x/σ)^2)`) allows stretching or squishing the curve horizontally <a class="yt-timestamp" data-t="00:16:38">[00:16:38]</a>. Here, `σ` becomes the standard deviation of the distribution <a class="yt-timestamp" data-t="00:17:20">[00:17:20]</a>, <a class="yt-timestamp" data-t="00:17:24">[00:17:24]</a>.
*   **Normalization (Area = 1):** For a valid [[probability_density_and_distribution | probability distribution]], the area under the curve must be 1 <a class="yt-timestamp" data-t="00:17:38">[00:17:38]</a>. The area under `e^(-x^2)` is √π <a class="yt-timestamp" data-t="00:18:21">[00:18:21]</a>, requiring a division by √π <a class="yt-timestamp" data-t="00:18:38">[00:18:38]</a>. Combined with the standard deviation scaling, the overall normalizing factor becomes `1 / (σ * √(2π))` <a class="yt-timestamp" data-t="00:18:43">[00:18:43]</a>, <a class="yt-timestamp" data-t="00:18:52">[00:18:52]</a>, <a class="yt-timestamp" data-t="00:18:56">[00:18:56]</a>. This ensures the total area is 1 <a class="yt-timestamp" data-t="00:19:06">[00:19:06]</a>.
*   **Shifting (Mean):** Subtracting a constant `μ` from `x` (`(x - μ)^2`) allows sliding the graph left or right to prescribe the mean of the distribution <a class="yt-timestamp" data-t="00:19:25">[00:19:25]</a>.

The complete formula for a normal distribution, parameterized by its mean (μ) and standard deviation (σ), is:

$$ f(x) = \frac{1}{\sigma \sqrt{2\pi}} e^{-\frac{1}{2}\left(\frac{x - \mu}{\sigma}\right)^2} $$ <a class="yt-timestamp" data-t="00:19:40">[00:19:40]</a>

The special case where `σ = 1` and `μ = 0` is called the **standard normal distribution** <a class="yt-timestamp" data-t="00:19:15">[00:19:15]</a>.

### [[connection_between_gaussian_distribution_and_probability | Probability Density Functions]]

Unlike discrete distributions, continuous distributions like the normal distribution are described by [[probability_density_and_distribution | probability density functions]] (PDFs) <a class="yt-timestamp" data-t="00:17:47">[00:17:47]</a>. You don't ask for the probability of a particular point, but rather the probability that a value falls between two different values, which is equal to the area under the curve between those values <a class="yt-timestamp" data-t="00:17:50">[00:17:50]</a>, <a class="yt-timestamp" data-t="00:22:05">[00:22:05]</a>.

## Quantifying the [[central_limit_theorem | Central Limit Theorem]]

If an underlying random variable has a mean μ and standard deviation σ, then for a sum of *n* such variables:
*   The mean of the sum is `n * μ` <a class="yt-timestamp" data-t="00:20:10">[00:20:10]</a>.
*   The standard deviation of the sum is `σ * √n` <a class="yt-timestamp" data-t="00:20:22">[00:20:22]</a>.

The [[central_limit_theorem | Central Limit Theorem]] states that as the sum size *n* increases, the distribution of the sum, when normalized, tends towards the standard normal distribution <a class="yt-timestamp" data-t="00:21:02">[00:21:02]</a>. Normalization involves:
1.  Subtracting the expected mean (`n * μ`) from the sum, so the new expression has a mean of zero <a class="yt-timestamp" data-t="00:21:02">[00:21:02]</a>.
2.  Dividing by the expected standard deviation (`σ * √n`), which rescales units so the standard deviation of the new expression is one <a class="yt-timestamp" data-t="00:21:06">[00:21:06]</a>.

This transformed expression tells "how many standard deviations away from the mean is this sum?" <a class="yt-timestamp" data-t="00:21:24">[00:21:24]</a>.

### The Magic of CLT

For a sufficiently large sum (e.g., 50 different values), regardless of how the initial underlying random variable's [[probability_density_and_distribution | distribution]] is changed, it has essentially no effect on the shape of the plot of the normalized sum <a class="yt-timestamp" data-t="00:23:16">[00:23:16]</a>. All the specific information and nuance of the initial distribution gets "washed away," and the sum tends towards the single universal shape of the standard normal distribution <a class="yt-timestamp" data-t="00:23:31">[00:23:31]</a>.

### Formal Statement

The rigorous statement of the [[central_limit_theorem | Central Limit Theorem]] is:
Consider the value where *n* different instantiations of a variable are summed, then tweaked so its mean and standard deviation are 1. If you consider the probability that this value falls between two given real numbers, *a* and *b*, and you consider the limit of that probability as the size of your sum goes to infinity, then that limit is equal to the integral (area) under a standard normal distribution between those two values <a class="yt-timestamp" data-t="00:24:09">[00:24:09]</a>.

## Applications and Rules of Thumb

For normal distributions, there's a handy rule of thumb:
*   About **68%** of values fall within one standard deviation of the mean <a class="yt-timestamp" data-t="00:25:31">[00:25:31]</a>.
*   About **95%** of values fall within two standard deviations of the mean <a class="yt-timestamp" data-t="00:25:35">[00:25:35]</a>.
*   About **99.7%** of values fall within three standard deviations of the mean <a class="yt-timestamp" data-t="00:25:42">[00:25:42]</a>.

### Example: Rolling 100 Dice

If you roll a fair die 100 times and add the results, you can find a range where you are 95% sure the sum will fall <a class="yt-timestamp" data-t="00:25:12">[00:25:12]</a>.
1.  **Mean of a single die roll (μ):** (1/6 * 1) + (1/6 * 2) + ... + (1/6 * 6) = 3.5 <a class="yt-timestamp" data-t="00:26:07">[00:26:07]</a>.
2.  **Standard deviation of a single die roll (σ):** Calculated from variance, it's approximately 1.71 (variance is 2.92) <a class="yt-timestamp" data-t="00:26:19">[00:26:19]</a>.
3.  **Mean of 100 rolls:** 100 * μ = 100 * 3.5 = 350 <a class="yt-timestamp" data-t="00:26:42">[00:26:42]</a>.
4.  **Standard deviation of 100 rolls:** √100 * σ = 10 * 1.71 = 17.1 <a class="yt-timestamp" data-t="00:26:47">[00:26:47]</a>.
5.  **95% range:** Two standard deviations from the mean.
    *   Lower bound: 350 - (2 * 17.1) = 350 - 34.2 = 315.8 (approx. 316) <a class="yt-timestamp" data-t="00:26:53">[00:26:53]</a>.
    *   Upper bound: 350 + (2 * 17.1) = 350 + 34.2 = 384.2 (approx. 384) <a class="yt-timestamp" data-t="00:27:01">[00:27:01]</a>.
    Therefore, you are 95% sure the sum will fall between 316 and 384 <a class="yt-timestamp" data-t="00:27:07">[00:27:07]</a>.

If you divide the sum by 100, it represents the empirical average of 100 die rolls <a class="yt-timestamp" data-t="00:27:18">[00:27:18]</a>, <a class="yt-timestamp" data-t="00:27:21">[00:27:21]</a>. The interval then tells you the range you expect for that empirical average, which should be around 3.5 <a class="yt-timestamp" data-t="00:27:37">[00:27:37]</a>. The [[central_limit_theorem | Central Limit Theorem]] allows computation of how close to the expected value the empirical average will likely be <a class="yt-timestamp" data-t="00:27:51">[00:27:51]</a>.

## [[assumptions_and_limitations_of_the_central_limit_theorem | Assumptions and Limitations of the Central Limit Theorem]]

The [[central_limit_theorem | Central Limit Theorem]] has three underlying assumptions:
1.  **Independence:** All variables being added must be independent of each other <a class="yt-timestamp" data-t="00:28:18">[00:28:18]</a>. The outcome of one process does not influence another <a class="yt-timestamp" data-t="00:28:22">[00:28:22]</a>.
2.  **Identically Distributed:** All variables must be drawn from the same [[probability_density_and_distribution | distribution]] <a class="yt-timestamp" data-t="00:28:27">[00:28:27]</a>. These two assumptions are often lumped together as IID (Independent and Identically Distributed) <a class="yt-timestamp" data-t="00:28:42">[00:28:42]</a>.
3.  **Finite Variance:** The variance computed for these variables must be finite <a class="yt-timestamp" data-t="00:30:04">[00:30:04]</a>. This is usually not an issue for discrete outcomes but can be for distributions with an infinite set of outcomes where the variance sum might diverge to infinity <a class="yt-timestamp" data-t="00:30:10">[00:30:10]</a>. If variance is infinite, the sum might not tend towards a normal distribution, even if the first two assumptions hold <a class="yt-timestamp" data-t="00:30:30">[00:30:30]</a>.

The actual Galton board violates the first two assumptions: a ball's bounce off one peg is not independent of the next, and the [[probability_density_and_distribution | distribution]] of outcomes off each peg might not be the same <a class="yt-timestamp" data-t="00:28:50">[00:28:50]</a>. The simplified model is necessary for it to be a true example of the [[central_limit_theorem | Central Limit Theorem]] <a class="yt-timestamp" data-t="00:29:29">[00:29:29]</a>. While the real Galton board appears to produce a normal distribution, this might be due to generalizations of the theorem that relax these assumptions <a class="yt-timestamp" data-t="00:29:38">[00:29:38]</a>. It's important to be cautious about assuming a variable is normally distributed without justification <a class="yt-timestamp" data-t="00:29:54">[00:29:54]</a>.

Further topics include exploring why this particular function is the one that distributions tend towards, and the role of [[explaining_pi_in_the_normal_distribution_formula | pi]] and [[role_of_circular_symmetry_in_statistical_distributions | circular symmetry]] in its formula <a class="yt-timestamp" data-t="00:30:48">[00:30:48]</a>.