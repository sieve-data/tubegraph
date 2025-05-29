---
title: Variance and its Calculation for Population and Sample
videoId: HvDqbzu0i0E
---

From: [[khanacademy]] <br/> 

[[variance_and_standard_deviation | Variance]] is a statistical concept used to measure the average dispersion or how far the data points are from the mean in a dataset <a class="yt-timestamp" data-t="02:21:00">[02:21:00]</a> <a class="yt-timestamp" data-t="02:25:00">[02:25:00]</a>. It is one way to quantify the spread of data, complementing measures of central tendency like the mean, median, and mode <a class="yt-timestamp" data-t="00:38:00">[00:38:00]</a> <a class="yt-timestamp" data-t="00:47:00">[00:47:00]</a>. The mean is frequently used when discussing [[variance_and_standard_deviation | variances]] and [[Standard Deviation and its Relation to Variance | standard deviation]] <a class="yt-timestamp" data-t="00:50:00">[00:50:00]</a>.

Before calculating [[variance_and_standard_deviation | variance]], the mean of the dataset must be determined.

## Mean

The mean is a measure of the central tendency or average of a data set <a class="yt-timestamp" data-t="00:38:00">[00:38:00]</a>.

### Mean of a [[population_versus_sample | Population]] (μ)

The mean of a [[population_versus_sample | population]] (mu, μ) is calculated by summing each data point in the population (xᵢ) and dividing by the total number of data points (N) in the population <a class="yt-timestamp" data-t="00:56:00">[00:56:00]</a> <a class="yt-timestamp" data-t="01:17:00">[01:17:00]</a> <a class="yt-timestamp" data-t="01:20:00">[01:20:00]</a>.

$$
\mu = \frac{\sum_{i=1}^{N} x_i}{N}
$$ <a class="yt-timestamp" data-t="00:58:00">[00:58:00]</a>

### Mean of a [[population_versus_sample | Sample]] (x̄)

The mean of a [[population_versus_sample | sample]] (x-bar, x̄) is calculated similarly, by summing each data point in the sample (xᵢ) and dividing by the total number of data points (n) in the sample <a class="yt-timestamp" data-t="01:30:00">[01:30:00]</a> <a class="yt-timestamp" data-t="01:39:00">[01:39:00]</a> <a class="yt-timestamp" data-t="01:55:00">[01:55:00]</a>. Lowercase 'n' is used to denote that the sample size is typically less than the population size (N) <a class="yt-timestamp" data-t="01:57:00">[01:57:00]</a>.

$$
\bar{x} = \frac{\sum_{i=1}^{n} x_i}{n}
$$ <a class="yt-timestamp" data-t="01:42:00">[01:42:00]</a>

## [[variance_and_standard_deviation | Variance]]

[[variance_and_standard_deviation | Variance]] measures the average of the squared differences from the mean <a class="yt-timestamp" data-t="02:57:00">[02:57:00]</a> <a class="yt-timestamp" data-t="03:00:00">[03:00:00]</a>.

### [[variance_and_standard_deviation | Population Variance]] (σ²)

The [[variance_and_standard_deviation | variance]] of a [[population_versus_sample | population]] is denoted by sigma squared (σ²) <a class="yt-timestamp" data-t="02:35:00">[02:35:00]</a> <a class="yt-timestamp" data-t="02:40:00">[02:40:00]</a>. It is calculated by:
1.  Finding the difference between each data point (xᵢ) and the [[population_versus_sample | population]] mean (μ) <a class="yt-timestamp" data-t="02:44:00">[02:44:00]</a> <a class="yt-timestamp" data-t="02:50:00">[02:50:00]</a>.
2.  Squaring these differences <a class="yt-timestamp" data-t="02:55:00">[02:55:00]</a>.
3.  Summing all the squared differences <a class="yt-timestamp" data-t="03:02:00">[03:02:00]</a>.
4.  Dividing the sum by the total number of data points in the population (N) <a class="yt-timestamp" data-t="03:08:00">[03:08:00]</a>.

$$
\sigma^2 = \frac{\sum_{i=1}^{N} (x_i - \mu)^2}{N}
$$ <a class="yt-timestamp" data-t="02:44:00">[02:44:00]</a>

#### [[RealLife Calculations and Examples of Statistical Measures | Calculation Example for Population Variance]]

Consider the dataset {1, 2, 3, 8, 7} as a [[population_versus_sample | population]] <a class="yt-timestamp" data-t="07:37:00">[07:37:00]</a>.

1.  **Calculate the mean (μ):**
    μ = (1 + 2 + 3 + 8 + 7) / 5 = 21 / 5 = 4.20 <a class="yt-timestamp" data-t="07:40:00">[07:40:00]</a> <a class="yt-timestamp" data-t="07:51:00">[07:51:00]</a> <a class="yt-timestamp" data-t="08:01:00">[08:01:00]</a> <a class="yt-timestamp" data-t="08:07:00">[08:07:00]</a>

2.  **Calculate squared differences from the mean:**
    *   (1 - 4.20)² = (-3.20)² = 10.24
    *   (2 - 4.20)² = (-2.20)² = 4.84
    *   (3 - 4.20)² = (-1.20)² = 1.44
    *   (8 - 4.20)² = (3.80)² = 14.44
    *   (7 - 4.20)² = (2.80)² = 7.84 <a class="yt-timestamp" data-t="08:22:00">[08:22:00]</a> <a class="yt-timestamp" data-t="08:27:00">[08:27:00]</a> <a class="yt-timestamp" data-t="08:37:00">[08:37:00]</a>

3.  **Sum the squared differences:**
    10.24 + 4.84 + 1.44 + 14.44 + 7.84 = 38.80 <a class="yt-timestamp" data-t="10:12:00">[10:12:00]</a> <a class="yt-timestamp" data-t="10:14:00">[10:14:00]</a>

4.  **Divide by N (5):**
    σ² = 38.80 / 5 = 7.76 <a class="yt-timestamp" data-t="10:18:00">[10:18:00]</a> <a class="yt-timestamp" data-t="10:51:00">[10:51:00]</a> <a class="yt-timestamp" data-t="10:53:00">[10:53:00]</a> <a class="yt-timestamp" data-t="11:14:00">[11:14:00]</a>

The [[variance_and_standard_deviation | population variance]] (σ²) for this dataset is 7.76 <a class="yt-timestamp" data-t="11:19:00">[11:19:00]</a>.

### [[variance_and_standard_deviation | Sample Variance]] (s²)

The [[variance_and_standard_deviation | variance]] of a [[population_versus_sample | sample]] is denoted by s-squared (s²) <a class="yt-timestamp" data-t="03:36:00">[03:36:00]</a> <a class="yt-timestamp" data-t="03:43:00">[03:43:00]</a>. To provide an unbiased estimate of the [[population_versus_sample | population variance]] from a [[population_versus_sample | sample]], the sum of the squared differences is divided by (n - 1) instead of n, where n is the [[Sample Size and Sampling | sample size]] <a class="yt-timestamp" data-t="03:25:00">[03:25:00]</a> <a class="yt-timestamp" data-t="03:30:00">[03:30:00]</a> <a class="yt-timestamp" data-t="04:22:00">[04:22:00]</a>.

$$
s^2 = \frac{\sum_{i=1}^{n} (x_i - \bar{x})^2}{n-1}
$$ <a class="yt-timestamp" data-t="03:46:00">[03:46:00]</a>

#### [[RealLife Calculations and Examples of Statistical Measures | Calculation Example for Sample Variance]]

Consider the dataset {1, 2, 3, 8, 7} as a [[population_versus_sample | sample]] from a larger distribution <a class="yt-timestamp" data-t="11:24:00">[11:24:00]</a> <a class="yt-timestamp" data-t="11:27:00">[11:27:00]</a>.

1.  **Calculate the sample mean (x̄):**
    x̄ = (1 + 2 + 3 + 8 + 7) / 5 = 21 / 5 = 4.20 (Note: The mean calculation is the same, but it's conceptualized as a sample mean) <a class="yt-timestamp" data-t="07:40:00">[07:40:00]</a> <a class="yt-timestamp" data-t="07:51:00">[07:51:00]</a> <a class="yt-timestamp" data-t="08:01:00">[08:01:00]</a> <a class="yt-timestamp" data-t="08:07:00">[08:07:00]</a>

2.  **Sum the squared differences from the mean:**
    This sum remains 38.80, as calculated for the population variance example <a class="yt-timestamp" data-t="10:12:00">[10:12:00]</a>.

3.  **Divide by (n - 1) (5 - 1 = 4):**
    s² = 38.80 / 4 = 9.70 <a class="yt-timestamp" data-t="11:30:00">[11:30:00]</a> <a class="yt-timestamp" data-t="11:38:00">[11:38:00]</a> <a class="yt-timestamp" data-t="11:45:00">[11:45:00]</a>

The [[variance_and_standard_deviation | sample variance]] (s²) for this dataset is 9.70 <a class="yt-timestamp" data-t="11:45:00">[11:45:00]</a>.

### Relation to [[Standard Deviation and its Relation to Variance | Standard Deviation]]

The [[Standard Deviation and its Relation to Variance | standard deviation]] is simply the square root of the [[variance_and_standard_deviation | variance]] <a class="yt-timestamp" data-t="05:19:00">[05:19:00]</a> <a class="yt-timestamp" data-t="05:23:00">[05:23:00]</a> <a class="yt-timestamp" data-t="05:30:00">[05:30:00]</a>.
*   **[[Standard Deviation and its Relation to Variance | Population Standard Deviation]] (σ):** $\sigma = \sqrt{\sigma^2}$ <a class="yt-timestamp" data-t="05:30:00">[05:30:00]</a>
*   **[[Standard Deviation and its Relation to Variance | Sample Standard Deviation]] (s):** $s = \sqrt{s^2}$ <a class="yt-timestamp" data-t="06:03:00">[06:03:00]</a>

The [[Standard Deviation and its Relation to Variance | standard deviation]] is often preferred because its units are the same as the original data points, unlike [[variance_and_standard_deviation | variance]] which has squared units <a class="yt-timestamp" data-t="06:35:00">[06:35:00]</a> <a class="yt-timestamp" data-t="06:57:00">[06:57:00]</a>. For example, if measurements are in meters, [[variance_and_standard_deviation | variance]] would be in meters squared, while [[Standard Deviation and its Relation to Variance | standard deviation]] would be in meters <a class="yt-timestamp" data-t="06:39:00">[06:39:00]</a>.