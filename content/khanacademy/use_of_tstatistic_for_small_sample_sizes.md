---
title: Use of Tstatistic for small sample sizes
videoId: 5ABpqVSx33I
---

From: [[khanacademy]] <br/> 

When performing [[introduction_to_statistics | inferential statistics]] and trying to determine the probability of obtaining a certain [[mean_and_standard_deviation_in_hypothesis_testing | sample mean]], statisticians often use a standardized value to understand how many standard deviations a result is from the mean <a class="yt-timestamp" data-t="00:22:00">[00:22:00]</a>, <a class="yt-timestamp" data-t="01:08:00">[01:08:00]</a>. This value is typically calculated as:

` (Sample Mean - Assumed Mean of Sampling Distribution) / Standard Deviation of Sampling Distribution ` <a class="yt-timestamp" data-t="01:15:00">[01:15:00]</a>

The [[importance_of_central_limit_theorem_in_statistics | Central Limit Theorem]] states that, with a sufficient [[implications_of_sample_size_on_statistical_distribution | sample size]], the standard deviation of the sampling distribution can be approximated by the [[population_versus_sample_in_statistics | population standard deviation]] divided by the square root of the [[implications_of_sample_size_on_statistical_distribution | sample size]] <a class="yt-timestamp" data-t="01:54:00">[01:54:00]</a>. This leads to the calculation of a [[Zscore and sampling distribution | Z-score]], or more specifically, a [[use_of_zstatistic_in_inferential_statistics | Z-statistic]] when derived from a sample mean statistic <a class="yt-timestamp" data-t="02:45:00">[02:45:00]</a>. This [[use_of_zstatistic_in_inferential_statistics | Z-statistic]] is then used with a Z-table (or normal distribution table) to find probabilities <a class="yt-timestamp" data-t="02:58:00">[02:58:00]</a>.

## Distinguishing Z-statistic and T-statistic

Often, the [[population_versus_sample_in_statistics | population standard deviation]] is unknown <a class="yt-timestamp" data-t="03:18:00">[03:18:00]</a>. In such cases, the [[population_versus_sample_in_statistics | population standard deviation]] is estimated using the [[descriptive_statistics | sample standard deviation]] <a class="yt-timestamp" data-t="03:38:00">[03:38:00]</a>.

### When to Use a Z-statistic

If the [[implications_of_sample_size_on_statistical_distribution | sample size]] is large (generally considered greater than 30) <a class="yt-timestamp" data-t="03:53:00">[03:53:00]</a>, <a class="yt-timestamp" data-t="04:02:00">[04:02:00]</a>, the [[descriptive_statistics | sample standard deviation]] is a good approximation for the [[population_versus_sample_in_statistics | population standard deviation]] <a class="yt-timestamp" data-t="05:51:00">[05:51:00]</a>. In this scenario, the calculated statistic (even with the approximation) will be approximately normally distributed <a class="yt-timestamp" data-t="04:14:00">[04:14:00]</a>, <a class="yt-timestamp" data-t="04:44:00">[04:44:00]</a>, allowing the continued use of a [[use_of_zstatistic_in_inferential_statistics | Z-table]] for probability calculations <a class="yt-timestamp" data-t="06:01:00">[06:01:00]</a>.

### When to Use a T-statistic (Small Sample Sizes)

The [[difference_between_zstatistic_and_tstatistic | distinction between the Z-statistic and T-statistic]] becomes crucial when the [[implications_of_sample_size_on_statistical_distribution | sample size]] is small <a class="yt-timestamp" data-t="06:08:00">[06:08:00]</a>. If the [[implications_of_sample_size_on_statistical_distribution | sample size]] is less than 30 (especially if significantly less) <a class="yt-timestamp" data-t="04:17:00">[04:17:00]</a>, the expression:

` (Sample Mean - Mean of Sampling Distribution of Sample Mean) / (Sample Standard Deviation / sqrt(Sample Size)) ` <a class="yt-timestamp" data-t="04:28:00">[04:28:00]</a>

will **not** be normally distributed <a class="yt-timestamp" data-t="04:23:00">[04:23:00]</a>. Instead, this quantity will follow a **T-distribution** <a class="yt-timestamp" data-t="04:49:00">[04:49:00]</a>.

When using a T-distribution, the process is similar to using a Z-distribution:
1.  Calculate the T-value using the formula above <a class="yt-timestamp" data-t="05:26:00">[05:26:00]</a>.
2.  Use a T-table (instead of a Z-table) to determine the probability of getting a T-value at least as extreme as the calculated one <a class="yt-timestamp" data-t="06:19:00">[06:19:00]</a>.

While all Z-values are normally distributed <a class="yt-timestamp" data-t="05:09:00">[05:09:00]</a>, a T-distribution accounts for the increased uncertainty when the [[population_versus_sample_in_statistics | population standard deviation]] is unknown and the [[implications_of_sample_size_on_statistical_distribution | sample size]] is small. A normalized T-distribution also has a mean of 0 <a class="yt-timestamp" data-t="05:18:00">[05:18:00]</a>.