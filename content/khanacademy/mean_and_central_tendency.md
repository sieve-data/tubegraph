---
title: Mean and central tendency
videoId: HvDqbzu0i0E
---

From: [[khanacademy]] <br/> 

In [[descriptive_statistics|statistics]], the concept of the [[mean_median_and_mode|mean]] is a fundamental way to understand the [[central_tendency_in_statistics|central tendency]] or [[measures_of_central_tendency|average]] of a dataset <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>. While other [[central_tendency_measures|measures of central tendency]] include the [[median|median]] and the mode, the [[mean_in_statistics|mean]] is frequently used, particularly when discussing concepts like variance and standard deviation <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.

## The Mean

The [[mean_in_statistics|mean]] represents the [[arithmetic_mean|average]] value of a dataset. It is calculated differently depending on whether the data represents an entire population or a sample from a larger population <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.

### Population Mean
The [[mean_in_statistics|mean]] of a population is denoted by the Greek letter mu (μ) <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>. It is calculated by summing all data points in the population and dividing by the total number of data points <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>.

$$
\mu = \frac{\sum_{i=1}^{N} x_i}{N}
$$

Where:
*   $x_i$ represents each individual data point in the population <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>
*   $N$ represents the total number of data points in the population <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>
*   $\sum$ denotes the sum of all data points from the first ($i=1$) to the Nth ($N$) <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>

This is the traditional way to calculate an [[arithmetic_mean|average]] <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.

### Sample Mean
The [[sampling_distribution_and_sample_mean|mean of a sample]] is denoted by x-bar ($\bar{x}$) <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>. It is calculated similarly to the population [[mean_in_statistics|mean]], but applies to a subset of the population <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>.

$$
\bar{x} = \frac{\sum_{i=1}^{n} x_i}{n}
$$

Where:
*   $x_i$ represents each individual data point in the sample <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>
*   $n$ represents the total number of data points in the sample <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a> (where $n < N$, as a sample is less than a population <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>)
*   $\sum$ denotes the sum of all data points from the first ($i=1$) to the nth ($n$) <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>

## Variance

While the [[mean_in_statistics|mean]] gives a [[central_tendency_in_statistics|central tendency]], variance provides a measure of how good an indicator the [[mean_in_statistics|mean]] is for the entire dataset <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>. It quantifies, on average, how far data points are from the [[mean_in_statistics|mean]] <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>.

### Population Variance
The variance of a population is denoted by sigma-squared ($\sigma^2$) <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>. It is the average of the squared differences between each data point and the population [[mean_in_statistics|mean]] <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.

$$
\sigma^2 = \frac{\sum_{i=1}^{N} (x_i - \mu)^2}{N}
$$

Where:
*   $x_i$ is each data point <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>
*   $\mu$ is the population [[mean_in_statistics|mean]] <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>
*   $N$ is the total number of data points in the population <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>

### Sample Variance
The variance of a sample is typically denoted by s-squared ($s^2$) <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>. When calculating sample variance to estimate the population variance, an "unbiased estimate" is achieved by dividing by $n-1$ instead of $n$ <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.

$$
s^2 = \frac{\sum_{i=1}^{n} (x_i - \bar{x})^2}{n-1}
$$

Where:
*   $x_i$ is each data point in the sample <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>
*   $\bar{x}$ is the sample [[mean_in_statistics|mean]] <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>
*   $n$ is the total number of data points in the sample <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>
*   The division by $n-1$ provides an unbiased estimator for the population variance <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.

## Standard Deviation

Standard deviation is arguably one of the most frequently used terms in [[descriptive_statistics|statistics]] <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>. Once variance is known, standard deviation is straightforward to calculate <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>.

Standard deviation is the square root of the variance <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>.

The primary reason for using standard deviation over variance is that its units are the same as the original data points, making it more intuitive to interpret <a class="yt-timestamp" data-t="00:06:35">[00:06:35]</a>. For example, if data is measured in meters, variance would be in "meters squared," while standard deviation would be in "meters" <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>.

### Population Standard Deviation
The standard deviation of a population is denoted by sigma ($\sigma$) <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>.

$$
\sigma = \sqrt{\sigma^2} = \sqrt{\frac{\sum_{i=1}^{N} (x_i - \mu)^2}{N}}
$$

### Sample Standard Deviation
The standard deviation of a sample is denoted by s ($s$) <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.

$$
s = \sqrt{s^2} = \sqrt{\frac{\sum_{i=1}^{n} (x_i - \bar{x})^2}{n-1}}
$$

While $s$ is the square root of the unbiased sample variance, it is important to note that $s$ itself is not an unbiased estimator for $\sigma$ <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>. However, it serves as a very good estimate <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>.

## Calculation Example

Let's calculate the [[mean_in_statistics|mean]], variance, and standard deviation for the dataset: 1, 2, 3, 8, and 7 <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>.

### Assuming the dataset is a Population

1.  **Calculate the Mean ($\mu$)**:
    Sum of data points: $1 + 2 + 3 + 8 + 7 = 21$ <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>
    Number of data points ($N$): 5 <a class="yt-timestamp" data-t="00:07:59">[00:07:59]</a>
    $\mu = \frac{21}{5} = 4.20$ <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>

2.  **Calculate the Variance ($\sigma^2$)**:
    First, find the squared differences from the mean for each data point:
    *   $(1 - 4.20)^2 = (-3.20)^2 = 10.24$ <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>
    *   $(2 - 4.20)^2 = (-2.20)^2 = 4.84$ <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>
    *   $(3 - 4.20)^2 = (-1.20)^2 = 1.44$ <a class="yt-timestamp" data-t="00:08:34">[00:08:34]</a>
    *   $(8 - 4.20)^2 = (3.80)^2 = 14.44$ <a class="yt-timestamp" data-t="00:08:38">[00:08:38]</a>
    *   $(7 - 4.20)^2 = (2.80)^2 = 7.84$ <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>

    Sum of squared differences: $10.24 + 4.84 + 1.44 + 14.44 + 7.84 = 38.80$ <a class="yt-timestamp" data-t="00:10:12">[00:10:12]</a>
    $\sigma^2 = \frac{38.80}{5} = 7.76$ <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>

3.  **Calculate the Standard Deviation ($\sigma$)**:
    $\sigma = \sqrt{7.76} \approx 2.7856$ (rounded to 2.79) <a class="yt-timestamp" data-t="00:11:59">[00:11:59]</a>

    This indicates that, on average, the numbers are about 2.79 units away from the [[mean_in_statistics|mean]] of 4.20 <a class="yt-timestamp" data-t="00:12:13">[00:12:13]</a>.

### Assuming the dataset is a Sample

If the dataset (1, 2, 3, 8, 7) was a sample from a larger population instead of the entire population <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>:

1.  **Calculate the Sample Mean ($\bar{x}$)**:
    The sample [[mean_in_statistics|mean]] would be the same as the population [[mean_in_statistics|mean]] in this case, calculated as $\bar{x} = 4.20$.

2.  **Calculate the Sample Variance ($s^2$)**:
    The sum of squared differences remains $38.80$. However, for an unbiased estimate, we divide by $n-1$:
    $s^2 = \frac{38.80}{5-1} = \frac{38.80}{4} = 9.70$ <a class="yt-timestamp" data-t="00:11:45">[00:11:45]</a>

3.  **Calculate the Sample Standard Deviation ($s$)**:
    $s = \sqrt{9.70} \approx 3.1144$ (rounded to 3.11) <a class="yt-timestamp" data-t="00:12:46">[00:12:46]</a>