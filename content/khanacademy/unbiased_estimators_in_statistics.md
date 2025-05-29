---
title: unbiased estimators in statistics
videoId: HvDqbzu0i0E
---

From: [[khanacademy]] <br/> 

When working with data, statisticians often distinguish between a [[sampling_and_sample_means | population]] and a [[sampling_and_sample_means | sample]]. An **unbiased estimator** is a statistic used to estimate a population parameter, where the expected value of the estimator is equal to the true value of the parameter being estimated. This concept is particularly relevant when calculating variance.

## Review of Basic Statistical Concepts

To understand unbiased estimators, it's helpful to first review the definitions of [[mean_and_central_tendency | mean]], variance, and standard deviation for both populations and samples.

### Mean (Central Tendency)

The [[mean_and_central_tendency | mean]] is a measure of the average or [[mean_and_central_tendency | central tendency]] of a data set <a class="yt-timestamp" data-t="00:38:00">[00:38:00]</a>. Other measures include the median and the mode, but the [[mean_and_central_tendency | mean]] is frequently used, especially when discussing variance and [[mean_and_standard_deviation_in_hypothesis_testing | standard deviation]] <a class="yt-timestamp" data-t="00:50:00">[00:50:00]</a>.

*   **Population Mean ($\mu$)**:
    The [[mean_and_central_tendency | mean]] of a population ($\mu$) is calculated by summing all data points ($x_i$) in the population and dividing by the total number of data points ($N$) <a class="yt-timestamp" data-t="00:56:00">[00:56:00]</a>.
    $$ \mu = \frac{\sum_{i=1}^{N} x_i}{N} $$
*   **Sample Mean ($\bar{x}$)**:
    The [[mean_and_central_tendency | mean]] of a [[sampling_and_sample_means | sample]] ($\bar{x}$) is calculated similarly, by summing all data points ($x_i$) in the [[sampling_and_sample_means | sample]] and dividing by the number of data points in the [[sampling_and_sample_means | sample]] ($n$) <a class="yt-timestamp" data-t="01:30:00">[01:30:00]</a>.
    $$ \bar{x} = \frac{\sum_{i=1}^{n} x_i}{n} $$

### Variance

Variance measures how far, on average, data points are from the [[mean_and_central_tendency | mean]] <a class="yt-timestamp" data-t="02:21:00">[02:21:00]</a>, <a class="yt-timestamp" data-t="02:25:00">[02:25:00]</a>.

*   **Population Variance ($\sigma^2$)**:
    The variance of a population ($\sigma^2$) is the average of the squared differences between each data point ($x_i$) and the population [[mean_and_central_tendency | mean]] ($\mu$) <a class="yt-timestamp" data-t="02:35:00">[02:35:00]</a>.
    $$ \sigma^2 = \frac{\sum_{i=1}^{N} (x_i - \mu)^2}{N} $$
*   **Sample Variance ($s^2$) - The Unbiased Estimator**:
    When calculating the variance from a [[sampling_and_sample_means | sample]] to estimate the population variance, a slightly different formula is used to provide an **unbiased estimate** <a class="yt-timestamp" data-t="03:21:00">[03:21:00]</a>, <a class="yt-timestamp" data-t="03:25:00">[03:25:00]</a>, <a class="yt-timestamp" data-t="03:41:00">[03:41:00]</a>. Instead of dividing by $n$, the sum of the squared differences is divided by $n-1$:
    $$ s^2 = \frac{\sum_{i=1}^{n} (x_i - \bar{x})^2}{n-1} $$
    The division by $n-1$ (known as Bessel's correction) helps correct for the fact that a [[sampling_and_sample_means | sample]] [[mean_and_central_tendency | mean]] ($\bar{x}$) is used instead of the true population [[mean_and_central_tendency | mean]] ($\mu$) <a class="yt-timestamp" data-t="03:53:00">[03:53:00]</a>, <a class="yt-timestamp" data-t="03:56:00">[03:56:00]</a>. If the population [[mean_and_central_tendency | mean]] were known, division by $n$ would be appropriate even for a [[sampling_and_sample_means | sample]] <a class="yt-timestamp" data-t="03:56:00">[03:56:00]</a>. The use of $n-1$ ensures that, on average, the sample variance equals the population variance <a class="yt-timestamp" data-t="04:22:00">[04:22:00]</a>. The formal proof of why $n-1$ yields an unbiased estimator can be explored in more advanced statistical topics <a class="yt-timestamp" data-t="04:30:00">[04:30:00]</a>, <a class="yt-timestamp" data-t="04:40:00">[04:40:00]</a>.

### Standard Deviation

The [[mean_and_standard_deviation_in_hypothesis_testing | standard deviation]] is the square root of the variance <a class="yt-timestamp" data-t="05:23:00">[05:23:00]</a>. It is one of the most frequently used terms in statistics <a class="yt-timestamp" data-t="04:53:00">[04:53:00]</a>. Unlike variance, the [[mean_and_standard_deviation_in_hypothesis_testing | standard deviation]] is expressed in the same units as the original data, making it easier to interpret the spread of the data <a class="yt-timestamp" data-t="06:35:00">[06:35:00]</a>, <a class="yt-timestamp" data-t="06:59:00">[06:59:00]</a>.

*   **Population Standard Deviation ($\sigma$)**:
    $$ \sigma = \sqrt{\sigma^2} = \sqrt{\frac{\sum_{i=1}^{N} (x_i - \mu)^2}{N}} $$
*   **Sample Standard Deviation ($s$)**:
    $$ s = \sqrt{s^2} = \sqrt{\frac{\sum_{i=1}^{n} (x_i - \bar{x})^2}{n-1}} $$
    It is important to note that while $s^2$ (sample variance) is an unbiased estimator for $\sigma^2$ (population variance), $s$ (sample standard deviation) is **not** an unbiased estimator for $\sigma$ (population standard deviation) <a class="yt-timestamp" data-t="06:09:00">[06:09:00]</a>, <a class="yt-timestamp" data-t="06:11:00">[06:11:00]</a>. However, it is still considered a very good estimate <a class="yt-timestamp" data-t="06:15:00">[06:15:00]</a>.

## Example Calculation

Let's consider a population dataset: `1, 2, 3, 8, 7` <a class="yt-timestamp" data-t="07:28:00">[07:28:00]</a>.

1.  **Calculate the Population Mean ($\mu$)**:
    Sum of data points = $1+2+3+8+7 = 21$ <a class="yt-timestamp" data-t="07:51:00">[07:51:00]</a>.
    Number of data points ($N$) = $5$ <a class="yt-timestamp" data-t="07:59:00">[07:59:00]</a>.
    $\mu = \frac{21}{5} = 4.20$ <a class="yt-timestamp" data-t="08:01:00">[08:01:00]</a>.

2.  **Calculate the Population Variance ($\sigma^2$)**:
    The variance is the sum of squared differences from the mean, divided by $N$ <a class="yt-timestamp" data-t="08:09:00">[08:09:00]</a>:
    $(1-4.2)^2 = (-3.2)^2 = 10.24$
    $(2-4.2)^2 = (-2.2)^2 = 4.84$
    $(3-4.2)^2 = (-1.2)^2 = 1.44$
    $(8-4.2)^2 = (3.8)^2 = 14.44$
    $(7-4.2)^2 = (2.8)^2 = 7.84$
    Sum of squared differences = $10.24 + 4.84 + 1.44 + 14.44 + 7.84 = 38.80$ <a class="yt-timestamp" data-t="10:12:00">[10:12:00]</a>.
    $\sigma^2 = \frac{38.80}{5} = 7.76$ <a class="yt-timestamp" data-t="10:51:00">[10:51:00]</a>, <a class="yt-timestamp" data-t="11:14:00">[11:14:00]</a>.

3.  **Calculate the Population Standard Deviation ($\sigma$)**:
    $\sigma = \sqrt{7.76} \approx 2.79$ <a class="yt-timestamp" data-t="11:58:00">[11:58:00]</a>, <a class="yt-timestamp" data-t="12:09:00">[12:09:00]</a>.

### Sample Variance and Standard Deviation (Using Unbiased Estimator)

If the dataset `1, 2, 3, 8, 7` were considered a [[sampling_and_sample_means | sample]] from a larger population ($n=5$) <a class="yt-timestamp" data-t="11:19:00">[11:19:00]</a>:

1.  **Calculate the Sample Mean ($\bar{x}$)**:
    This would be the same as the population [[mean_and_central_tendency | mean]] calculated above, $\bar{x} = 4.20$.

2.  **Calculate the Sample Variance ($s^2$) (Unbiased Estimator)**:
    Using the sum of squared differences ($38.80$) and dividing by $n-1 = 5-1=4$:
    $s^2 = \frac{38.80}{4} = 9.70$ <a class="yt-timestamp" data-t="11:38:00">[11:38:00]</a>, <a class="yt-timestamp" data-t="12:38:00">[12:38:00]</a>.

3.  **Calculate the Sample Standard Deviation ($s$)**:
    $s = \sqrt{9.70} \approx 3.11$ <a class="yt-timestamp" data-t="12:40:00">[12:40:00]</a>, <a class="yt-timestamp" data-t="12:46:00">[12:46:00]</a>.

The difference in the denominator ($N$ vs. $n-1$) is crucial for providing an unbiased estimate of the population variance when working with a sample <a class="yt-timestamp" data-t="11:27:00">[11:27:00]</a>.