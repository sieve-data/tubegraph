---
title: Population vs sample in statistics
videoId: HvDqbzu0i0E
---

From: [[khanacademy]] <br/> 

This article reviews fundamental statistical concepts, differentiating between their application to a [[sample_space_in_probability | population]] and a sample <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>.

## Core Concepts: Population vs. Sample <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>

When dealing with statistical concepts, it's crucial to distinguish between a **population** (the entire group of interest) and a **sample** (a subset of the [[sample_space_in_probability | population]]) <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.

## Mean (Central Tendency) <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>

The [[mean_in_statistics | mean]] is a measure of [[central_tendency_in_statistics | central tendency]], representing the average of a data set <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. While other measures like median and mode exist, the [[mean_in_statistics | mean]] is frequently used, especially when discussing variance and [[sampling_distribution_and_standard_deviation | standard deviation]] <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.

*   **Population Mean ($\mu$)**
    *   **Definition**: The sum of all data points ($x_i$) in the [[sample_space_in_probability | population]], divided by the total number of data points ($N$) in the [[sample_space_in_probability | population]] <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>.
    *   **Formula**: $\mu = \frac{\sum_{i=1}^{N} x_i}{N}$ <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>
*   **Sample Mean ($\bar{x}$)**
    *   **Definition**: The sum of all data points ($x_i$) in the sample, divided by the number of data points ($n$) in the sample <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.
    *   **Formula**: $\bar{x} = \frac{\sum_{i=1}^{n} x_i}{n}$ <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>
    *   *Note*: The sample size ($n$) is typically less than the [[sample_space_in_probability | population]] size ($N$) <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.

## Variance <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>

Variance measures how far data points are, on average, from the [[mean_in_statistics | mean]] <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>. It's calculated by taking the average of the squared differences between each data point and the [[mean_in_statistics | mean]] <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.

*   **Population Variance ($\sigma^2$)**
    *   **Definition**: The sum of the squared differences between each data point and the population [[mean_in_statistics | mean]], divided by the total number of data points ($N$) in the [[sample_space_in_probability | population]] <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.
    *   **Formula**: $\sigma^2 = \frac{\sum_{i=1}^{N} (x_i - \mu)^2}{N}$ <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>
*   **Sample Variance ($s^2$)**
    *   **Definition**: The sum of the squared differences between each data point in the sample and the sample [[mean_in_statistics | mean]], divided by $(n-1)$ <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>.
    *   **Formula**: $s^2 = \frac{\sum_{i=1}^{n} (x_i - \bar{x})^2}{n-1}$ <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>
    *   *Note*: The denominator $(n-1)$ is used to provide an **unbiased estimate** of the [[sample_space_in_probability | population]] variance when working with a sample <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>. This adjustment accounts for the fact that the sample [[mean_in_statistics | mean]] is an estimate, leading to a slight underestimation of variance if $n$ were used <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.

## Standard Deviation <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>

The [[sampling_distribution_and_standard_deviation | standard deviation]] is the square root of the variance <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>. It is a widely used term in [[introduction_to_statistics | statistics]] <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>.

*   **Population Standard Deviation ($\sigma$)**
    *   **Definition**: The square root of the population variance <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.
    *   **Formula**: $\sigma = \sqrt{\frac{\sum_{i=1}^{N} (x_i - \mu)^2}{N}}$ <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>
*   **Sample Standard Deviation ($s$)**
    *   **Definition**: The square root of the sample variance <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>.
    *   **Formula**: $s = \sqrt{\frac{\sum_{i=1}^{n} (x_i - \bar{x})^2}{n-1}}$ <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>
    *   *Note*: While $s^2$ is an unbiased estimator for $\sigma^2$, $s$ is *not* an unbiased estimator for $\sigma$ <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>.
*   **Why use Standard Deviation?**
    *   **Units**: If data points are measured in meters, variance is in "meter squared," which is less intuitive. [[sampling_distribution_and_standard_deviation | Standard deviation]] returns the units to the original measurement (meters), making it easier to interpret the average dispersion from the center <a class="yt-timestamp" data-t="00:06:35">[00:06:35]</a>.
    *   **Interpretability**: For data that can be modeled by a bell curve (normal distribution), [[sampling_distribution_and_standard_deviation | standard deviation]] helps in understanding the probability of finding data points within a certain range of the [[mean_in_statistics | mean]] <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>.

## Example Calculation

Let's consider a data set: {1, 2, 3, 8, 7} <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>.

### Assuming it's a Population <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>

1.  **Population Mean ($\mu$)**:
    *   Sum of data points: $1 + 2 + 3 + 8 + 7 = 21$ <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>
    *   Number of data points ($N$): 5 <a class="yt-timestamp" data-t="00:07:59">[00:07:59]</a>
    *   $\mu = 21 / 5 = 4.20$ <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>
2.  **Population Variance ($\sigma^2$)**:
    *   Squared differences from the [[mean_in_statistics | mean]] (4.20):
        *   $(1 - 4.20)^2 = (-3.2)^2 = 10.24$
        *   $(2 - 4.20)^2 = (-2.2)^2 = 4.84$
        *   $(3 - 4.20)^2 = (-1.2)^2 = 1.44$
        *   $(8 - 4.20)^2 = (3.8)^2 = 14.44$
        *   $(7 - 4.20)^2 = (2.8)^2 = 7.84$ <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>
    *   Sum of squared differences: $10.24 + 4.84 + 1.44 + 14.44 + 7.84 = 38.80$ <a class="yt-timestamp" data-t="00:10:12">[00:10:12]</a>
    *   $\sigma^2 = 38.80 / 5 = 7.76$ <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>
3.  **Population Standard Deviation ($\sigma$)**:
    *   $\sigma = \sqrt{7.76} \approx 2.785$ (rounded to 2.79) <a class="yt-timestamp" data-t="00:11:59">[00:11:59]</a>

### Assuming it's a Sample <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>

If {1, 2, 3, 8, 7} was a sample from a larger [[sample_space_in_probability | population]]:

1.  **Sample Mean ($\bar{x}$)**:
    *   The sample [[mean_in_statistics | mean]] calculation is identical to the population [[mean_in_statistics | mean]] for this specific dataset: $\bar{x} = 4.20$.
2.  **Sample Variance ($s^2$)**:
    *   The sum of squared differences from the [[mean_in_statistics | mean]] remains $38.80$.
    *   However, for a sample, we divide by $(n-1)$ <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>. Since $n=5$, we divide by $5-1=4$.
    *   $s^2 = 38.80 / 4 = 9.70$ <a class="yt-timestamp" data-t="00:11:45">[00:11:45]</a>
3.  **Sample Standard Deviation ($s$)**:
    *   $s = \sqrt{9.70} \approx 3.114$ (rounded to 3.11) <a class="yt-timestamp" data-t="00:12:46">[00:12:46]</a>

This example demonstrates how the calculations differ based on whether the data set is considered a [[sample_space_in_probability | population]] or a sample, particularly for variance and [[sampling_distribution_and_standard_deviation | standard deviation]] <a class="yt-timestamp" data-t="00:12:53">[00:12:53]</a>.