---
title: Concept of Unbiased Estimator in Statistics
videoId: HvDqbzu0i0E
---

From: [[khanacademy]] <br/> 

When working with [[introduction_to_statistics | statistics]], particularly [[inferential_statistics | inferential statistics]], it's crucial to obtain estimates from samples that accurately reflect the characteristics of the larger population. An **unbiased estimator** is a statistic that, on average, correctly estimates the true value of a population parameter.

## Unbiased Sample Variance

The [[variance_and_its_calculation_for_population_and_sample | variance]] of a sample is used to estimate the population [[variance_and_its_calculation_for_population_and_sample | variance]]. To provide an unbiased estimate of the population [[variance_and_its_calculation_for_population_and_sample | variance]] when using a sample, the sum of the squared differences from the sample [[mean_or_central_tendency_in_statistics | mean]] is divided by `n-1` instead of `n` (where `n` is the number of data points in the sample) <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>. This specific denominator is used for what is referred to as the unbiased [[variance_and_its_calculation_for_population_and_sample | sample variance]] <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>.

The formula for the unbiased sample [[variance_and_its_calculation_for_population_and_sample | variance]] (s²) is:

$s^2 = \frac{\sum_{i=1}^{n} (x_i - \bar{x})^2}{n-1}$ <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>

Here, $x_i$ represents each data point in the sample, and $\bar{x}$ represents the sample [[mean_or_central_tendency_in_statistics | mean]] <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>. The use of `n-1` in the denominator helps account for the fact that the sample [[mean_or_central_tendency_in_statistics | mean]] ($\bar{x}$) is itself an estimate of the population [[mean_or_central_tendency_in_statistics | mean]] ($\mu$) <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>.

### Why n-1?

The division by `n-1` is crucial for obtaining an unbiased estimate <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>. While a full formal proof is complex, this adjustment corrects for the tendency of sample [[variance_and_its_calculation_for_population_and_sample | variance]] to slightly underestimate the true population [[variance_and_its_calculation_for_population_and_sample | variance]] when dividing by `n`.

## Sample Standard Deviation

The sample standard deviation (s) is the square root of the unbiased [[variance_and_its_calculation_for_population_and_sample | sample variance]] <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>. However, it's important to note that while the sample [[variance_and_its_calculation_for_population_and_sample | variance]] (s²) is an unbiased estimator for the population [[variance_and_its_calculation_for_population_and_sample | variance]] ($\sigma^2$), the sample standard deviation (s) is **not** an unbiased estimator for the population standard deviation ($\sigma$) <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>. Despite this, it is still considered a very good estimate <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>.

## Example Calculation

Consider a population data set: 1, 2, 3, 8, 7 <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>.
The [[mean_or_central_tendency_in_statistics | mean]] of this population ($\mu$) is 4.20 <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>.
The [[variance_and_its_calculation_for_population_and_sample | variance]] of this population ($\sigma^2$) is 7.76 <a class="yt-timestamp" data-t="00:11:14">[00:11:14]</a>.

If these numbers (1, 2, 3, 8, 7) were considered a *sample* from a larger population instead of the entire population, the calculation for the unbiased sample [[variance_and_its_calculation_for_population_and_sample | variance]] would change <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>.

Instead of dividing the sum of squared differences (38.80) by `N` (5), you would divide by `n-1` (4) <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>.

Sum of squared differences from the sample [[mean_or_central_tendency_in_statistics | mean]] = 38.80 <a class="yt-timestamp" data-t="00:10:12">[00:10:12]</a>

Unbiased sample [[variance_and_its_calculation_for_population_and_sample | variance]] (s²) = $\frac{38.80}{5-1} = \frac{38.80}{4} = 9.70$ <a class="yt-timestamp" data-t="00:11:45">[00:11:45]</a>

From this, the sample standard deviation would be the square root of 9.70, which is approximately 3.11 <a class="yt-timestamp" data-t="00:12:46">[00:12:46]</a>.