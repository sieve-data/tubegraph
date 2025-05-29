---
title: concept of variance
videoId: HvDqbzu0i0E
---

From: [[khanacademy]] <br/> 

[[variance | Variance]] is a statistical concept used to measure the average dispersion or spread of data points from the [[understanding_mean | mean]] of a data set <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>. It provides insight into how good an indicator the [[understanding_mean | mean]] is for the entire population or sample <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.

While the [[understanding_mean | mean]], median, and mode are measures of central tendency, the [[understanding_mean | mean]] is particularly important when discussing [[variance]] and [[standard_deviation | standard deviation]] <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.

## Population Variance

For a population, [[variance]] is denoted by the Greek letter sigma squared ($\sigma^2$) <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.

The formula for the [[variance]] of a population is:
$\sigma^2 = \frac{\sum_{i=1}^{N} (x_i - \mu)^2}{N}$ <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>

Where:
*   $x_i$ represents each individual data point in the population <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
*   $\mu$ (mu) is the [[understanding_mean | mean]] of the population <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.
*   $N$ is the total number of data points in the population <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.

This formula calculates the average of all the squared differences between each data point and the population [[understanding_mean | mean]] <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.

## Sample Variance

When dealing with a sample from a larger population, the objective is often to estimate the [[variance]] of the population based on the sample data <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.

To provide an unbiased estimate of the population [[variance]] using a sample, a slightly different formula is used for sample [[variance]], denoted by $s^2$ <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>:

$s^2 = \frac{\sum_{i=1}^{n} (x_i - \bar{x})^2}{n-1}$ <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>

Where:
*   $x_i$ represents each individual data point in the sample <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.
*   $\bar{x}$ (x-bar) is the [[understanding_mean | mean]] of the sample <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>. (It is assumed the population [[understanding_mean | mean]] is unknown, and the sample [[understanding_mean | mean]] is used as an estimate <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.)
*   $n$ is the total number of data points in the sample <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>.

The denominator is $n-1$ instead of $n$ to ensure an unbiased estimator <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>.

## Relationship to Standard Deviation

[[standard_deviation | Standard deviation]] is closely related to [[variance]] and is one of the most frequently used terms in statistics <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>.

*   **Population [[standard_deviation | Standard Deviation]] ($\sigma$):** This is the square root of the population [[variance]] <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>.
    $\sigma = \sqrt{\sigma^2}$ <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>
*   **Sample [[standard_deviation | Standard Deviation]] ($s$):** This is the square root of the sample [[variance]] <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>.
    $s = \sqrt{s^2}$ <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>

One key reason for using [[standard_deviation | standard deviation]] is that its units are the same as the original data points, unlike [[variance]]. For example, if measurements are in meters, [[variance]] units would be "meter squared," while [[standard_deviation | standard deviation]] units would remain "meters," making it a more intuitive measure of dispersion <a class="yt-timestamp" data-t="00:06:35">[00:06:35]</a>.

## Example Calculation (Population Variance)

Let's calculate the [[variance]] for a population with the following data points: 1, 2, 3, 8, 7 <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>.

1.  **Calculate the [[understanding_mean | mean]] ($\mu$):**
    Sum = 1 + 2 + 3 + 8 + 7 = 21 <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>
    Number of data points ($N$) = 5 <a class="yt-timestamp" data-t="00:07:59">[00:07:59]</a>
    $\mu = \frac{21}{5} = 4.20$ <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>

2.  **Calculate the sum of squared differences from the [[understanding_mean | mean]]:**
    $(1 - 4.20)^2 = (-3.2)^2 = 10.24$ <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>
    $(2 - 4.20)^2 = (-2.2)^2 = 4.84$ <a class="yt-timestamp" data-t="00:09:35">[00:09:35]</a>
    $(3 - 4.20)^2 = (-1.2)^2 = 1.44$ <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>
    $(8 - 4.20)^2 = (3.8)^2 = 14.44$ <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>
    $(7 - 4.20)^2 = (2.8)^2 = 7.84$ <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>

    Sum of squared differences = $10.24 + 4.84 + 1.44 + 14.44 + 7.84 = 38.80$ <a class="yt-timestamp" data-t="00:10:12">[00:10:12]</a>

3.  **Calculate the Population [[variance]] ($\sigma^2$):**
    $\sigma^2 = \frac{38.80}{5} = 7.76$ <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>

### Sample Variance (using the same data as a hypothetical sample)

If these numbers were treated as a sample instead of a population, the [[variance]] would be calculated by dividing by $n-1$:
$s^2 = \frac{38.80}{5-1} = \frac{38.80}{4} = 9.70$ <a class="yt-timestamp" data-t="00:11:45">[00:11:45]</a>

Once the [[variance]] is known, the [[standard_deviation | standard deviation]] is simply its square root <a class="yt-timestamp" data-t="00:11:58">[00:11:58]</a>.
*   Population [[standard_deviation | Standard Deviation]]: $\sqrt{7.76} \approx 2.79$ <a class="yt-timestamp" data-t="00:12:09">[00:12:09]</a>
*   Sample [[standard_deviation | Standard Deviation]]: $\sqrt{9.70} \approx 3.11$ <a class="yt-timestamp" data-t="00:12:53">[00:12:53]</a>