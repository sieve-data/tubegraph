---
title: Variance and its calculation
videoId: HvDqbzu0i0E
---

From: [[khanacademy]] <br/> 

Variance is a statistical concept used to measure the dispersion or spread of data points in a dataset from its [[Understanding Variables | mean]] <a class="yt-timestamp" data-t="02:21:00">[02:21:00]</a>, specifically "on average, how far are the data points from this [[Understanding Variables | mean]]" <a class="yt-timestamp" data-t="02:21:00">[02:21:00]</a>. It quantifies how much the numbers in a dataset vary from the average value <a class="yt-timestamp" data-t="02:25:00">[02:25:00]</a>.

The [[Understanding Variables | mean]] is a measure of central tendency <a class="yt-timestamp" data-t="00:38:00">[00:38:00]</a>, but variance (and [[Standard deviation and its significance | standard deviation]]) provides insight into the spread of the data around that [[Understanding Variables | mean]] <a class="yt-timestamp" data-t="02:17:00">[02:17:00]</a>.

## Variance of a Population

When calculating the variance for an entire population, the notation used is sigma squared ($\sigma^2$) <a class="yt-timestamp" data-t="02:40:00">[02:40:00]</a>.

The formula for population variance is:
$\sigma^2 = \frac{\sum_{i=1}^{N} (x_i - \mu)^2}{N}$ <a class="yt-timestamp" data-t="03:02:00">[03:02:00]</a>

Where:
*   $\mu$ (mu) represents the [[Understanding Variables | mean]] of the population <a class="yt-timestamp" data-t="00:58:00">[00:58:00]</a>.
*   $x_i$ represents each individual data point in the population <a class="yt-timestamp" data-t="02:44:00">[02:44:00]</a>.
*   $N$ represents the total number of data points in the population <a class="yt-timestamp" data-t="01:17:00">[01:17:00]</a>.
*   The term $(x_i - \mu)^2$ represents the squared difference between each data point and the population [[Understanding Variables | mean]] <a class="yt-timestamp" data-t="02:56:00">[02:56:00]</a>.
*   The summation ($\sum$) means that all these squared differences are added together <a class="yt-timestamp" data-t="03:00:00">[03:00:00]</a>.
*   The sum is then divided by the total number of data points ($N$) <a class="yt-timestamp" data-t="03:08:00">[03:08:00]</a>. This is essentially taking the average of the squared distances <a class="yt-timestamp" data-t="03:00:00">[03:00:00]</a>.

### Population Variance Calculation Example

Consider the dataset: `1, 2, 3, 8, 7` as a population <a class="yt-timestamp" data-t="07:37:00">[07:37:00]</a>.

1.  **Calculate the [[Understanding Variables | mean]] ($\mu$)**:
    *   Sum of data points: $1 + 2 + 3 + 8 + 7 = 21$ <a class="yt-timestamp" data-t="07:51:00">[07:51:00]</a>
    *   Number of data points ($N$): $5$ <a class="yt-timestamp" data-t="08:01:00">[08:01:00]</a>
    *   $\mu = \frac{21}{5} = 4.20$ <a class="yt-timestamp" data-t="08:01:00">[08:01:00]</a>

2.  **Calculate the squared differences for each data point**:
    *   $(1 - 4.20)^2 = (-3.2)^2 = 10.24$
    *   $(2 - 4.20)^2 = (-2.2)^2 = 4.84$
    *   $(3 - 4.20)^2 = (-1.2)^2 = 1.44$
    *   $(8 - 4.20)^2 = (3.8)^2 = 14.44$
    *   $(7 - 4.20)^2 = (2.8)^2 = 7.84$ <a class="yt-timestamp" data-t="08:22:00">[08:22:00]</a>

3.  **Sum the squared differences**:
    *   $10.24 + 4.84 + 1.44 + 14.44 + 7.84 = 38.80$ <a class="yt-timestamp" data-t="10:12:00">[10:12:00]</a>

4.  **Divide by $N$**:
    *   $\sigma^2 = \frac{38.80}{5} = 7.76$ <a class="yt-timestamp" data-t="10:14:00">[10:14:00]</a>, <a class="yt-timestamp" data-t="10:58:00">[10:58:00]</a>
    *   So, the population variance is $7.76$ <a class="yt-timestamp" data-t="11:14:00">[11:14:00]</a>.

## Variance of a Sample

When dealing with a sample from a larger population, the calculation for variance is slightly different to provide an "unbiased estimate" of the population variance <a class="yt-timestamp" data-t="03:21:00">[03:21:00]</a>, <a class="yt-timestamp" data-t="03:25:00">[03:25:00]</a>. The notation used for sample variance is $s^2$ <a class="yt-timestamp" data-t="03:43:00">[03:43:00]</a>.

The formula for sample variance (unbiased estimator) is:
$s^2 = \frac{\sum_{i=1}^{n} (x_i - \bar{x})^2}{n-1}$ <a class="yt-timestamp" data-t="04:15:00">[04:15:00]</a>, <a class="yt-timestamp" data-t="04:22:00">[04:22:00]</a>

Where:
*   $\bar{x}$ (x-bar) represents the [[Understanding Variables | mean]] of the sample <a class="yt-timestamp" data-t="01:39:00">[01:39:00]</a>, <a class="yt-timestamp" data-t="03:48:00">[03:48:00]</a>.
*   $x_i$ represents each individual data point in the sample <a class="yt-timestamp" data-t="03:46:00">[03:46:00]</a>.
*   $n$ represents the total number of data points in the sample <a class="yt-timestamp" data-t="01:57:00">[01:57:00]</a>.
*   The denominator is $n-1$ instead of $n$ <a class="yt-timestamp" data-t="03:30:00">[03:30:00]</a>, to ensure the sample variance is an unbiased estimator of the population variance <a class="yt-timestamp" data-t="04:22:00">[04:22:00]</a>, <a class="yt-timestamp" data-t="04:28:00">[04:28:00]</a>.

### Sample Variance Calculation Example

Using the same dataset: `1, 2, 3, 8, 7` but treating it as a sample <a class="yt-timestamp" data-t="11:19:00">[11:19:00]</a>.

1.  **Calculate the sample [[Understanding Variables | mean]] ($\bar{x}$)**: (Same calculation as population [[Understanding Variables | mean]] for this example)
    *   $\bar{x} = 4.20$ <a class="yt-timestamp" data-t="08:01:00">[08:01:00]</a>

2.  **Calculate the sum of squared differences**: (Same calculation as population variance for this example)
    *   Sum of squared differences $= 38.80$ <a class="yt-timestamp" data-t="10:12:00">[10:12:00]</a>

3.  **Divide by $n-1$**:
    *   $n = 5$, so $n-1 = 4$ <a class="yt-timestamp" data-t="11:30:00">[11:30:00]</a>.
    *   $s^2 = \frac{38.80}{4} = 9.70$ <a class="yt-timestamp" data-t="11:38:00">[11:38:00]</a>, <a class="yt-timestamp" data-t="12:38:00">[12:38:00]</a>
    *   So, the sample variance is $9.70$ <a class="yt-timestamp" data-t="11:45:00">[11:45:00]</a>.

## Relationship to [[Standard deviation and its significance | Standard Deviation]]

[[Standard deviation and its significance | Standard deviation]] is closely related to variance; it is simply the square root of the variance <a class="yt-timestamp" data-t="05:23:00">[05:23:00]</a>.

*   For a population, [[Standard deviation and its significance | standard deviation]] ($\sigma$) = $\sqrt{\sigma^2}$ <a class="yt-timestamp" data-t="05:30:00">[05:30:00]</a>, <a class="yt-timestamp" data-t="05:33:00">[05:33:00]</a>.
    *   Using the example above, $\sigma = \sqrt{7.76} \approx 2.79$ <a class="yt-timestamp" data-t="11:59:00">[11:59:00]</a>, <a class="yt-timestamp" data-t="12:09:00">[12:09:00]</a>.
*   For a sample, [[Standard deviation and its significance | standard deviation]] ($s$) = $\sqrt{s^2}$ <a class="yt-timestamp" data-t="06:06:00">[06:06:00]</a>, <a class="yt-timestamp" data-t="06:08:00">[06:08:00]</a>.
    *   Using the example above, $s = \sqrt{9.70} \approx 3.11$ <a class="yt-timestamp" data-t="12:46:00">[12:46:00]</a>, <a class="yt-timestamp" data-t="12:53:00">[12:53:00]</a>.

One reason [[Standard deviation and its significance | standard deviation]] is often preferred over variance is that its units are the same as the original data measurements <a class="yt-timestamp" data-t="06:35:00">[06:35:00]</a>. For example, if data points are in meters, variance would be in "meter squared," which is a "strange concept" for dispersion <a class="yt-timestamp" data-t="06:44:00">[06:44:00]</a>. Taking the square root to get [[Standard deviation and its significance | standard deviation]] brings the units back to meters, making it more intuitive to interpret as "how far the numbers are away from the [[Understanding Variables | mean]]" <a class="yt-timestamp" data-t="06:59:00">[06:59:00]</a>, <a class="yt-timestamp" data-t="07:04:00">[07:04:00]</a>, <a class="yt-timestamp" data-t="12:13:00">[12:13:00]</a>.