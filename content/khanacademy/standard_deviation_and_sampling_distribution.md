---
title: Standard deviation and sampling distribution
videoId: 5ABpqVSx33I
---

From: [[khanacademy]] <br/> 

In [[inferential_statistics_and_probability_of_sample_means | inferential statistics]], a primary goal is to determine the probability of obtaining a specific [[inferential_statistics_and_probability_of_sample_means | sample mean]] <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. This involves understanding the relationship between Z-statistics and T-statistics <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>.

## Sampling Distribution of the Sample Mean

When considering a [[sampling_distribution_and_standard_deviation | sampling distribution]] of the [[inferential_statistics_and_probability_of_sample_means | sample mean]], it possesses an assumed mean value and a specific [[sampling_distribution_and_standard_deviation | standard deviation]] <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. The objective is to calculate the probability of observing a [[inferential_statistics_and_probability_of_sample_means | sample mean]] that is at least as extreme as the one obtained <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>. This is typically done by figuring out how many [[sampling_distribution_and_standard_deviation | standard deviations]] the [[inferential_statistics_and_probability_of_sample_means | sample mean]] is from the expected mean <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.

## Z-Statistic

The Z-statistic (or Z-score) quantifies how many [[sampling_distribution_and_standard_deviation | standard deviations]] a [[inferential_statistics_and_probability_of_sample_means | sample mean]] is from the assumed population mean <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.

### Calculation of Z-Statistic

The Z-statistic is calculated using the formula:
`Z = (Sample Mean - Mean of Sampling Distribution) / Standard Deviation of Sampling Distribution` <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>

However, the [[sampling_distribution_and_standard_deviation | standard deviation]] of the [[sampling_distribution_and_standard_deviation | sampling distribution]] (also known as the standard error) is often unknown <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>. The [[Central_limit_theorem_and_sample_size_considerations | Central Limit Theorem]] states that with a sufficient [[Sample_Size_and_Sampling | sample size]], the [[sampling_distribution_and_standard_deviation | standard deviation]] of the [[sampling_distribution_and_standard_deviation | sampling distribution]] can be approximated by:
`Population Standard Deviation / sqrt(Sample Size)` <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.

So, the Z-statistic formula can be rewritten as:
`Z = (Sample Mean - Mean of Sampling Distribution) / (Population Standard Deviation / sqrt(Sample Size))` <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>

This Z-statistic, when derived from the [[inferential_statistics_and_probability_of_sample_means | sample mean]], is called a Z-statistic <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>. Once calculated, its probability can be determined using a Z-table or [[Normal_Distribution | normal distribution]] table <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>. All Z-values are normally distributed <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>.

### Approximating Population Standard Deviation for Z-Statistic

Often, the [[variance_and_standard_deviation | standard deviation]] of the population is also unknown <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>. In such cases, it can be estimated using the [[variance_and_standard_deviation | sample standard deviation]] <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>.

The approximate Z-statistic becomes:
`Z ≈ (Sample Mean - Mean of Sampling Distribution) / (Sample Standard Deviation / sqrt(Sample Size))` <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>

This approximation is considered acceptable and results in an approximately [[Normal_Distribution | normally distributed]] value if the [[Sample_Size_and_Sampling | sample size]] is greater than 30 <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>.

## T-Statistic

When the [[Sample_Size_and_Sampling | sample size]] is less than 30, the approximation using the [[variance_and_standard_deviation | sample standard deviation]] for the population [[variance_and_standard_deviation | standard deviation]] no longer yields a [[Normal_Distribution | normally distributed]] expression <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>. In these instances, the calculated statistic follows a T-distribution, and it is referred to as a T-statistic <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>.

The formula for the T-statistic is the same as the approximated Z-statistic:
`T = (Sample Mean - Mean of Sampling Distribution) / (Sample Standard Deviation / sqrt(Sample Size))` <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>

The key difference is the distribution used for probability calculations: a T-distribution instead of a [[Normal_Distribution | normal distribution]] <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>. A normalized T-distribution also has a mean of 0 <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.

## Rule of Thumb: Z vs. T

The choice between using a Z-statistic and a T-statistic depends primarily on the [[Sample_Size_and_Sampling | sample size]]:

*   **Z-Statistic**: If the [[Sample_Size_and_Sampling | sample size]] is greater than 30, the [[variance_and_standard_deviation | sample standard deviation]] is a good approximation for the population [[variance_and_standard_deviation | standard deviation]]. The resulting statistic is approximately [[Normal_Distribution | normally distributed]], and a Z-table can be used to determine probabilities <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>.
*   **T-Statistic**: If the [[Sample_Size_and_Sampling | sample size]] is small (typically less than 30), this statistic will have a T-distribution. A T-table must then be used to figure out the probability of getting a T-value at least as extreme as the calculated one <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>.

This rule is crucial for applying the correct distribution when performing hypothesis tests or constructing confidence intervals, as detailed in [[conditions_for_using_normal_distribution_vs_tdistribution | Conditions for using normal distribution vs T-distribution]].