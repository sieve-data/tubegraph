---
title: Calculating standard deviation and probability
videoId: 5ABpqVSx33I
---

From: [[khanacademy]] <br/> 

In inferential statistics, a primary goal is to determine the [[calculating_probability_of_an_event | probability]] of obtaining a certain sample mean from a population <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. This often involves understanding the [[sampling_distribution_and_standard_deviation | sampling distribution]] of the sample mean <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. The [[sampling_distribution_and_standard_deviation | sampling distribution]] has an assumed mean value and a [[standard_deviation_and_its_significance | standard deviation]] <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. To calculate the [[calculating_probability_of_an_event | probability]] of a sample mean being at least as extreme as an observed value, one typically determines how many [[standard_deviation_explained | standard deviations]] the sample mean is from the population mean <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. This measure is encapsulated in either a Z-statistic or a T-statistic, depending on the sample size and knowledge of the population [[standard_deviation_explained | standard deviation]] <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>.

## The Z-Statistic

The Z-statistic (or Z-score) is used when the population [[standard_deviation_explained | standard deviation]] is known, or when the sample size is sufficiently large (typically greater than 30) <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>, <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>. It quantifies how many [[standard_deviation_explained | standard deviations]] a sample mean is from the assumed population mean <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.

The formula for the Z-statistic is:
$$ Z = \frac{\bar{x} - \mu}{\sigma_{\bar{x}}} $$
where:
*   $\bar{x}$ is the sample mean <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>.
*   $\mu$ is the assumed mean of the [[sampling_distribution_and_standard_deviation | sampling distribution]] <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.
*   $\sigma_{\bar{x}}$ is the [[standard_deviation_explained | standard deviation]] of the [[sampling_distribution_and_standard_deviation | sampling distribution]] <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.

According to the Central Limit Theorem, for a sufficient sample size, the [[standard_deviation_explained | standard deviation]] of the [[sampling_distribution_and_standard_deviation | sampling distribution]] can be expressed as:
$$ \sigma_{\bar{x}} = \frac{\sigma}{\sqrt{n}} $$
where:
*   $\sigma$ is the population [[standard_deviation_explained | standard deviation]] <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.
*   $n$ is the sample size <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.

Thus, the Z-statistic formula can be rewritten as:
$$ Z = \frac{\bar{x} - \mu}{\sigma / \sqrt{n}} $$
This Z-statistic is approximately normally distributed <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>. Once the Z-statistic is calculated, a Z-table (or normal distribution table) can be used to determine the [[calculating_probability_of_an_event | probability]] of obtaining a value as extreme as or more extreme than the observed sample mean <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>.

## The T-Statistic

When the population [[standard_deviation_explained | standard deviation]] is unknown and the sample size is small (especially less than 30), using the sample [[standard_deviation_explained | standard deviation]] ($s$) as an estimate for the population [[standard_deviation_explained | standard deviation]] means the resulting statistic will not be normally distributed <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>. In such cases, a T-statistic is used <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>.

The formula for the T-statistic is:
$$ T = \frac{\bar{x} - \mu}{s / \sqrt{n}} $$
where:
*   $\bar{x}$ is the sample mean <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>.
*   $\mu$ is the assumed mean of the [[sampling_distribution_and_standard_deviation | sampling distribution]] <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>.
*   $s$ is the sample [[standard_deviation_explained | standard deviation]] (an estimate for the population [[standard_deviation_explained | standard deviation]]) <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.
*   $n$ is the sample size <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>.

This statistic follows a T-distribution, which is different from a normal distribution, particularly with smaller sample sizes <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>. Similar to the Z-statistic, once the T-value is calculated, a T-table is used to determine the [[calculating_probability_of_an_event | probability]] of obtaining a T-value at least as extreme as the calculated one <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>. The T-distribution is also normalized, typically having a mean of 0 <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.

## Summary: When to Use Z vs. T

A simple rule of thumb for calculating these statistics and their associated probabilities is:
*   **If your sample size is greater than 30 (n > 30)**: The sample [[standard_deviation_explained | standard deviation]] is a good approximation for the population [[standard_deviation_explained | standard deviation]], and the statistic will be approximately normally distributed. Use a Z-statistic and a Z-table to find the [[calculating_probability_of_an_event | probability]] <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>.
*   **If your sample size is small (n < 30)**: The statistic will have a T-distribution. Use a T-statistic and a T-table to find the [[calculating_probability_of_an_event | probability]] <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>.

Understanding which statistic to apply is crucial for accurately [[calculating_probability_of_an_event | calculating probabilities]] related to sample means in inferential statistics <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>.