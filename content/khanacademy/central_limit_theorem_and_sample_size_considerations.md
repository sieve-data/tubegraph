---
title: Central limit theorem and sample size considerations
videoId: 5ABpqVSx33I
---

From: [[khanacademy]] <br/> 

In [[Inferential statistics and probability of sample means | inferential statistics]], a common goal is to determine the probability of obtaining a particular [[mean_or_central_tendency_in_statistics | sample mean]] from a [[sampling_distribution_and_standard_deviation | sampling distribution]] <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. This involves understanding how many [[standard_deviation_and_sampling_distribution | standard deviations]] a given [[mean_or_central_tendency_in_statistics | sample mean]] is from the assumed population [[mean_or_central_tendency_in_statistics | mean]] <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. The choice between using a Z-statistic or a T-statistic largely depends on whether the [[population_versus_sample | population]] [[standard_deviation_and_sampling_distribution | standard deviation]] is known or estimated, and critically, the [[sample_size_and_sampling | sample size]] <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>.

## The Z-Statistic

When working with a [[sampling_distribution_and_standard_deviation | sampling distribution]] of the [[mean_or_central_tendency_in_statistics | sample mean]], the number of [[standard_deviation_and_sampling_distribution | standard deviations]] a [[mean_or_central_tendency_in_statistics | sample mean]] is from the true [[mean_or_central_tendency_in_statistics | mean]] can be calculated as:

$\frac{(\text{Sample Mean} - \text{Assumed Mean})}{\text{Standard Deviation of the Sampling Distribution}}$ <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>

The [[Central Limit Theorem | Central Limit Theorem]] states that, with a sufficient [[sample_size_and_sampling | sample size]], the [[standard_deviation_and_sampling_distribution | standard deviation]] of the [[sampling_distribution_and_standard_deviation | sampling distribution]] of the [[mean_or_central_tendency_in_statistics | sample mean]] (also known as the standard error) can be approximated as the [[population_versus_sample | population]] [[standard_deviation_and_sampling_distribution | standard deviation]] divided by the square root of the [[sample_size_and_sampling | sample size]] <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>.

This leads to the Z-statistic formula:

$Z = \frac{(\bar{x} - \mu)}{\sigma / \sqrt{n}}$

Where:
*   $\bar{x}$ is the [[mean_or_central_tendency_in_statistics | sample mean]]
*   $\mu$ is the [[mean_or_central_tendency_in_statistics | mean]] of the [[sampling_distribution_and_standard_deviation | sampling distribution]] (often the assumed [[population_versus_sample | population]] [[mean_or_central_tendency_in_statistics | mean]])
*   $\sigma$ is the [[population_versus_sample | population]] [[standard_deviation_and_sampling_distribution | standard deviation]]
*   $n$ is the [[sample_size_and_sampling | sample size]]

This value is a Z-score, or more specifically, a Z-statistic when derived from a [[mean_or_central_tendency_in_statistics | sample mean]] statistic <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>. Once calculated, a Z-table or normal distribution table can be used to find the probability of obtaining a result at least as extreme as the observed Z-value <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>.

## The T-Statistic

A common issue in real-world scenarios is that the [[population_versus_sample | population]] [[standard_deviation_and_sampling_distribution | standard deviation]] ($\sigma$) is unknown <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>. In such cases, the [[sample_size_and_sampling | sample standard deviation]] ($s$) is used as an estimate <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>. The statistic then becomes:

$\frac{(\bar{x} - \mu)}{s / \sqrt{n}}$ <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>

The critical distinction arises with the [[sample_size_and_sampling | sample size]]:

*   **Large [[Sample_size_and_sampling | Sample Size]] (n > 30)**: If the [[sample_size_and_sampling | sample size]] is sufficiently large (typically greater than 30), the [[sample_size_and_sampling | sample standard deviation]] ($s$) is considered a good approximation for the [[population_versus_sample | population]] [[standard_deviation_and_sampling_distribution | standard deviation]] ($\sigma$) <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>. In this scenario, the statistic is still approximately normally distributed, and it can be treated as a Z-statistic <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.
*   **Small [[Sample_size_and_sampling | Sample Size]] (n < 30)**: If the [[sample_size_and_sampling | sample size]] is small (especially less than 30), substituting the [[sample_size_and_sampling | sample standard deviation]] for the [[population_versus_sample | population]] [[standard_deviation_and_links | standard deviation]] means that the resulting expression will *not* be normally distributed <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>. Instead, this statistic follows a T-distribution <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>.

The T-distribution is similar to the normal distribution but has "fatter tails," meaning it accounts for the increased uncertainty when estimating the [[population_versus_sample | population]] [[standard_deviation_and_sampling_distribution | standard deviation]] from a small [[sample_size_and_sampling | sample]] <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>. When using a T-statistic, a T-table is consulted to find the probability, also taking into account the degrees of freedom (which is related to the [[sample_size_and_sampling | sample size]]) <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>.

## Rule of Thumb for Z vs. T

<a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>
> [!info]
> Calculate the quantity $\frac{(\bar{x} - \mu)}{s / \sqrt{n}}$:
> *   If your [[sample_size_and_sampling | sample size]] ($n$) is **greater than 30**, the [[sample_size_and_sampling | sample standard deviation]] is a good approximation for the [[population_versus_sample | population]] [[standard_deviation_and_sampling_distribution | standard deviation]], and the statistic is approximately normally distributed. Use a **Z-table**.
> *   If your [[sample_size_and_sampling | sample size]] ($n$) is **small (less than 30)**, the statistic will have a T-distribution. Use a **T-table**.

This distinction is crucial for accurately determining probabilities and making inferences about [[population_versus_sample | populations]] based on [[sample_size_and_sampling | sample]] data.