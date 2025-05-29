---
title: Understanding mean and standard deviation in probability
videoId: zeJD6dqJ5lo
---

From: [[3blue1brown]] <br/> 

In probability, the mean and standard deviation are crucial quantitative measures used to describe the characteristics of a distribution, particularly its center and its spread <a class="yt-timestamp" data-t="00:27:27">[00:27:27]</a>. They are essential for understanding and applying concepts like the Central Limit Theorem <a class="yt-timestamp" data-t="00:27:51">[00:27:51]</a>.

## Mean (μ)
The mean of a distribution, denoted by the Greek letter mu (μ), serves as a way to capture the "center of mass" for that distribution <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a> <a class="yt-timestamp" data-t="00:11:47">[00:11:47]</a>.

### Calculation
It is calculated as the expected value of a random variable <a class="yt-timestamp" data-t="00:11:51">[00:11:51]</a>. This means going through all possible outcomes, multiplying the probability of each outcome by the variable's value, and summing these products <a class="yt-timestamp" data-t="00:11:54">[00:11:54]</a>. If higher values are more probable, the weighted sum (mean) will be larger; if lower values are more probable, it will be smaller <a class="yt-timestamp" data-t="00:12:03">[00:12:03]</a>.

### Mean of a Sum of Variables
When summing multiple random variables, the mean of the sum is simply the sum of the means of the individual variables <a class="yt-timestamp" data-t="00:13:25">[00:13:25]</a>. For example, if you roll a pair of dice, the expected value of their sum is two times the expected value for a single die <a class="yt-timestamp" data-t="00:13:27">[00:13:27]</a>. Generally, if a random variable has a mean μ, the mean for a sum of `n` such variables will be `n * μ` <a class="yt-timestamp" data-t="00:13:33">[00:13:33]</a> <a class="yt-timestamp" data-t="00:20:10">[00:20:10]</a> <a class="yt-timestamp" data-t="00:20:21">[00:20:21]</a>. This causes the distribution to drift to the right as `n` increases <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a> <a class="yt-timestamp" data-t="00:13:41">[00:13:41]</a>.

## Measuring Spread: Variance (σ²) and Standard Deviation (σ)
To understand how spread out a distribution is, variance and standard deviation are used <a class="yt-timestamp" data-t="00:12:10">[00:12:10]</a>.

### Variance (σ²)
Variance is a measure of spread, often denoted by sigma squared (σ²) <a class="yt-timestamp" data-t="00:12:18">[00:12:18]</a> <a class="yt-timestamp" data-t="00:12:20">[00:12:20]</a>. It is calculated by looking at the difference between each possible value and the mean, squaring that difference, and then finding the expected value of these squared differences <a class="yt-timestamp" data-t="00:12:20">[00:12:20]</a>. Squaring the difference ensures the result is always positive and makes the mathematical calculations more tractable <a class="yt-timestamp" data-t="00:12:31">[00:12:31]</a> <a class="yt-timestamp" data-t="00:12:37">[00:12:37]</a>. However, because of the squaring, the units of variance are "square units," making it less intuitive to interpret as a direct distance on a diagram <a class="yt-timestamp" data-t="00:12:45">[00:12:45]</a>.

### Variance of a Sum of Variables
For two different random variables, the variance for the sum of those variables is the sum of their individual variances <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a>. If `n` different independent realizations of the same random variable are summed, the variance of the sum is `n` times the variance of the original variable <a class="yt-timestamp" data-t="00:14:20">[00:14:20]</a> <a class="yt-timestamp" data-t="00:14:24">[00:14:24]</a>.

### Standard Deviation (σ)
The standard deviation, denoted by the Greek letter sigma (σ), is the square root of the variance <a class="yt-timestamp" data-t="00:12:53">[00:12:53]</a> <a class="yt-timestamp" data-t="00:12:57">[00:12:57]</a>. It can be more reasonably interpreted as a distance on a probability distribution diagram <a class="yt-timestamp" data-t="00:12:59">[00:12:59]</a> <a class="yt-timestamp" data-t="00:13:03">[00:13:03]</a>.

### Standard Deviation of a Sum of Variables
Since variance adds, the standard deviation for a sum of `n` independent variables is `√n` times the original standard deviation <a class="yt-timestamp" data-t="00:14:29">[00:14:29]</a> <a class="yt-timestamp" data-t="00:14:33">[00:14:33]</a> <a class="yt-timestamp" data-t="00:20:24">[00:20:24]</a>. This means distributions spread out, but only in proportion to the square root of the sum's size, not linearly with `n` <a class="yt-timestamp" data-t="00:14:59">[00:14:59]</a>.

## Mean and Standard Deviation in the [[normal_distribution_and_its_characteristics|Normal Distribution]]
The [[normal_distribution_and_its_characteristics|Normal Distribution]] (also known as a bell curve or Gaussian distribution) is a specific type of probability distribution <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a> <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. It is defined by a function that uses both the mean (μ) and standard deviation (σ) as parameters <a class="yt-timestamp" data-t="00:19:40">[00:19:40]</a> <a class="yt-timestamp" data-t="00:19:43">[00:19:43]</a>.

The formula for a [[normal_distribution_and_its_characteristics|Normal Distribution]] is:
`f(x) = (1 / (σ * √(2π))) * e^(-(x - μ)² / (2σ²))` <a class="yt-timestamp" data-t="00:19:59">[00:19:59]</a>.
*   `μ` slides the graph left and right, prescribing the mean of the distribution <a class="yt-timestamp" data-t="00:19:33">[00:19:33]</a>.
*   `σ` stretches and squishes the graph horizontally, controlling the width of the bell curve and serving as its standard deviation <a class="yt-timestamp" data-t="00:16:41">[00:16:41]</a> <a class="yt-timestamp" data-t="00:17:24">[00:17:24]</a> <a class="yt-timestamp" data-t="00:17:31">[00:17:31]</a>.
*   The `(1 / (σ * √(2π)))` factor ensures that the total area under the curve is equal to 1, which is required for a probability density function <a class="yt-timestamp" data-t="00:18:09">[00:18:09]</a> <a class="yt-timestamp" data-t="00:18:43">[00:18:43]</a> <a class="yt-timestamp" data-t="00:19:02">[00:19:02]</a>. In a continuous distribution, probability is found by calculating the area under the curve between two values, a concept related to [[integrals_and_probability_distributions|integrals and probability distributions]] <a class="yt-timestamp" data-t="00:17:47">[00:17:47]</a> <a class="yt-timestamp" data-t="00:17:58">[00:17:58]</a>.

### The 68-95-99.7 Rule
A common rule of thumb for [[normal_distribution_and_its_characteristics|normal distributions]] describes the proportion of values that fall within certain standard deviations of the mean <a class="yt-timestamp" data-t="00:25:27">[00:25:27]</a> <a class="yt-timestamp" data-t="00:25:31">[00:25:31]</a>:
*   Approximately 68% of values fall within one standard deviation of the mean (μ ± 1σ) <a class="yt-timestamp" data-t="00:25:31">[00:25:31]</a>.
*   Approximately 95% of values fall within two standard deviations of the mean (μ ± 2σ) <a class="yt-timestamp" data-t="00:25:35">[00:25:35]</a>.
*   Approximately 99.7% of values fall within three standard deviations of the mean (μ ± 3σ) <a class="yt-timestamp" data-t="00:25:42">[00:25:42]</a>.

## Role in the Central Limit Theorem
The Central Limit Theorem (CLT) states that when you sum a large number of independent and identically distributed (IID) random variables, the distribution of that sum will tend towards a [[normal_distribution_and_its_characteristics|normal distribution]], regardless of the original distribution of the individual variables <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a> <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a> <a class="yt-timestamp" data-t="00:08:07">[00:08:07]</a> <a class="yt-timestamp" data-t="00:23:47">[00:23:47]</a>.

To demonstrate this convergence, distributions are often "realigned" and "rescaled" using their mean and standard deviation <a class="yt-timestamp" data-t="00:15:08">[00:15:08]</a>:
1.  **Realigning**: Subtracting the mean of the sum from the sum itself, so the new expression has a mean of zero <a class="yt-timestamp" data-t="00:21:02">[00:21:02]</a>.
2.  **Rescaling**: Dividing by the standard deviation of the sum, which rescales the units so that the standard deviation of the new expression equals one <a class="yt-timestamp" data-t="00:21:06">[00:21:06]</a>.

This transformation expresses the sum in terms of "how many standard deviations away from the mean" it is <a class="yt-timestamp" data-t="00:21:24">[00:21:24]</a>. When this process is applied to sums of increasing size, the resulting shape approaches the standard [[normal_distribution_and_its_characteristics|normal distribution]] (where μ=0 and σ=1) <a class="yt-timestamp" data-t="00:15:21">[00:15:21]</a> <a class="yt-timestamp" data-t="00:19:15">[00:19:15]</a> <a class="yt-timestamp" data-t="00:21:10">[00:21:10]</a>.

Despite starting with vastly different underlying distributions, the information about the original distribution's shape gets "washed away" as the sum size increases, converging to this universal [[normal_distribution_and_its_characteristics|normal distribution]] shape <a class="yt-timestamp" data-t="00:15:30">[00:15:30]</a> <a class="yt-timestamp" data-t="00:23:31">[00:23:31]</a>.