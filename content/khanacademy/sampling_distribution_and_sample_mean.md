---
title: Sampling distribution and sample mean
videoId: 5ABpqVSx33I
---

From: [[khanacademy]] <br/> 

In inferential statistics, a key objective is to determine the [[probability_and_distribution_modeling | probability]] of obtaining a specific [[mean_in_statistics | sample mean]] <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. This is typically approached by analyzing the [[sampling_distribution_and_standard_deviation | sampling distribution]] of the [[mean_in_statistics | sample mean]] <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

## Characteristics

A [[sampling_distribution_and_standard_deviation | sampling distribution]] of the [[mean_in_statistics | sample mean]] possesses an assumed [[mean_and_central_tendency | mean value]] and a specific [[sampling_distribution_and_standard_deviation | standard deviation]] <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. The goal is to determine the [[probability_and_distribution_modeling | probability]] of observing a [[mean_in_statistics | sample mean]] that is at least as extreme as a particular value <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>. This is done by calculating how many [[sampling_distribution_and_standard_deviation | standard deviations]] the [[mean_in_statistics | sample mean]] is away from the assumed [[mean_and_central_tendency | mean]] <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.

## Z-Statistic and the Sampling Distribution

The formula for calculating how many [[sampling_distribution_and_standard_deviation | standard deviations]] a [[mean_in_statistics | sample mean]] is from the [[mean_and_central_tendency | mean]] of its [[sampling_distribution_and_standard_deviation | sampling distribution]] is:
$$ \frac{\text{Sample Mean} - \text{Assumed Mean}}{\text{Standard Deviation of the Sampling Distribution}} $$
<a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>

The [[sampling_distribution_and_standard_deviation | standard deviation]] of the [[sampling_distribution_and_standard_deviation | sampling distribution]] (also known as the standard error) is often unknown <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>. However, the [[Central Limit Theorem and sample size implications | Central Limit Theorem]] states that for a sufficient [[Central Limit Theorem and sample size implications | sample size]], this standard error can be approximated by dividing the [[population_vs_sample_in_statistics | population]] [[sampling_distribution_and_standard_deviation | standard deviation]] by the square root of the [[Central Limit Theorem and sample size implications | sample size]] <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>.

This leads to the **Z-statistic** formula:
$$ Z = \frac{\text{Sample Mean} - \mu}{\sigma / \sqrt{n}} $$
Where:
*   $\text{Sample Mean}$ is the observed sample mean.
*   $\mu$ is the [[mean_and_central tendency | mean]] of the [[sampling_distribution_and_standard_deviation | sampling distribution]] of the [[mean_in_statistics | sample mean]] (often the hypothesized [[population_vs_sample_in_statistics | population]] [[mean_and_central_tendency | mean]]) <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.
*   $\sigma$ is the [[population_vs_sample_in_statistics | population]] [[sampling_distribution_and_standard_deviation | standard deviation]] <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>.
*   $n$ is the [[Central Limit Theorem and sample size implications | sample size]] <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.

This Z-statistic represents how many [[sampling_distribution_and_standard_deviation | standard deviations]] the [[mean_in_statistics | sample mean]] is from the actual [[mean_and_central_tendency | mean]] <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>. Once calculated, a Z-score can be looked up in a Z-table or normal distribution table to find the [[probability_and_distribution_modeling | probability]] of getting a value of Z or greater <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>.

## Approximations and the T-Statistic

In many real-world scenarios, the [[population_vs_sample_in_statistics | population]] [[sampling_distribution_and_standard_deviation | standard deviation]] ($\sigma$) is also unknown <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>. In such cases, the Z-statistic can be approximated by using the [[population_vs_sample_in_statistics | sample]] [[sampling_distribution_and_standard_deviation | standard deviation]] ($s$) as an estimate for $\sigma$ <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>:
$$ Z \approx \frac{\text{Sample Mean} - \mu}{s / \sqrt{n}} $$
This approximation is generally acceptable if the [[Central Limit Theorem and sample size implications | sample size]] is greater than 30 <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>, meaning the resulting statistic will be approximately normally distributed <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.

However, if the [[Central Limit Theorem and sample size implications | sample size]] is less than 30 (especially significantly less), this expression will not be normally distributed <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>. In such situations, the statistic follows a **T-distribution** <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>. The formula for the T-statistic is the same as the approximation for Z:
$$ T = \frac{\text{Sample Mean} - \mu}{s / \sqrt{n}} $$
<a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>

When using a T-statistic, one must refer to a T-table to find the [[probability_and_distribution_modeling | probability]] of obtaining a T-value at least as extreme as the calculated one <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>.

### Rule of Thumb for Z vs. T

*   **If your [[Central Limit Theorem and sample size implications | sample size]] is greater than 30**: Use the Z-statistic. Your [[population_vs_sample_in_statistics | sample]] [[sampling_distribution_and_standard_deviation | standard deviation]] is a good approximation for the [[population_vs_sample_in_statistics | population]] [[sampling_distribution_and_standard_deviation | standard deviation]], and the statistic will be approximately normally distributed <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>.
*   **If your [[Central Limit Theorem and sample size implications | sample size]] is small (less than 30)**: Use the T-statistic. The statistic will have a T-distribution <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>.