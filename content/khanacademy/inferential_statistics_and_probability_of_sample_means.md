---
title: Inferential statistics and probability of sample means
videoId: 5ABpqVSx33I
---

From: [[khanacademy]] <br/> 

In [[inferential_statistics | inferential statistics]], a primary goal is to determine the probability of obtaining a certain [[mean_or_central_tendency_in_statistics | sample mean]] <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. This involves understanding the position of a particular [[mean_or_central_tendency_in_statistics | sample mean]] within its [[sampling_distribution_and_standard_deviation | sampling distribution]] and calculating the likelihood of observing a result at least as extreme <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.

## Understanding the Sampling Distribution of the Sample Mean

When considering the [[sampling_distribution_and_standard_deviation | sampling distribution]] of the [[mean_or_central_tendency_in_statistics | sample mean]], it has an assumed [[mean_or_central_tendency_in_statistics | mean]] value and a [[standard_deviation_and_sampling_distribution | standard deviation]] <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. To assess the probability of a specific [[mean_or_central_tendency_in_statistics | sample mean]], one must determine how many [[standard_deviation_and_sampling_distribution | standard deviations]] it is above or below the assumed population [[mean_or_central_tendency_in_statistics | mean]] of the [[sampling_distribution_and_standard_deviation | sampling distribution]] <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.

## The Z-Statistic

The Z-statistic, also known as a Z-score, is a measure of how many [[standard_deviation_and_sampling_distribution | standard deviations]] an element is from the [[mean_or_central_tendency_in_statistics | mean]] <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>. When derived from the [[mean_or_central_tendency_in_statistics | sample mean]] statistic, it is specifically called a Z-statistic <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.

The Z-statistic can be used to look up probabilities in a Z-table or normal distribution table <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>.

### When Population Standard Deviation is Known

If the population [[standard_deviation_and_sampling_distribution | standard deviation]] ($\sigma$) is known, the Z-statistic is calculated as:

$$Z = \frac{\bar{x} - \mu}{\sigma / \sqrt{n}}$$
where:
*   $\bar{x}$ is the [[mean_or_central_tendency_in_statistics | sample mean]] <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>
*   $\mu$ is the assumed [[mean_or_central_tendency_in_statistics | mean]] of the [[sampling_distribution_and_standard_deviation | sampling distribution]] <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>
*   $\sigma$ is the population [[standard_deviation_and_sampling_distribution | standard deviation]] <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>
*   $n$ is the sample size <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>

The [[central_limit_theorem_and_sample_size_considerations | Central Limit Theorem]] states that with a sufficient sample size, the [[standard_deviation_and_sampling_distribution | standard deviation]] of the [[sampling_distribution_and_standard_deviation | sampling distribution]] (also known as the [[standard_deviation_and_sampling_distribution | standard error]]) is equal to the population [[standard_deviation_and_sampling_distribution | standard deviation]] divided by the square root of the sample size ($\sigma / \sqrt{n}$) <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>.

### When Population Standard Deviation is Unknown (and Large Sample Size)

Often, the population [[standard_deviation_and_sampling_distribution | standard deviation]] is unknown <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>. In such cases, the Z-statistic can be approximated by using the sample [[standard_deviation_and_sampling_distribution | standard deviation]] ($s$) as an estimate for the population [[standard_deviation_and_sampling_distribution | standard deviation]] <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>:

$$Z \approx \frac{\bar{x} - \mu}{s / \sqrt{n}}$$

This approximation is considered acceptable, and the resulting statistic will be approximately normally distributed, if the sample size ($n$) is greater than 30 <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>.

## The T-Statistic

### When to Use the T-Statistic (Small Sample Size)

If the sample size ($n$) is small (especially if it is less than 30), the statistic calculated using the sample [[standard_deviation_and_sampling_distribution | standard deviation]] will **not** be normally distributed <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>. In this scenario, the quantity has a T-distribution, and the calculated value is referred to as a T-statistic <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>:

$$T = \frac{\bar{x} - \mu}{s / \sqrt{n}}$$

### T-distribution vs. Normal Distribution

Unlike the Z-statistic which assumes a normal distribution, the T-statistic follows a T-distribution <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>. While both are bell-shaped and symmetric with a [[mean_or_central_tendency_in_statistics | mean]] of 0 (for normalized distributions), the T-distribution has fatter tails than the normal distribution, reflecting greater uncertainty due to the use of sample [[standard_deviation_and_sampling_distribution | standard deviation]] with small sample sizes <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>. To find probabilities for a T-statistic, a T-table must be used <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>.

## Rule of Thumb: Z-statistic vs. T-statistic

```ad-note
**Calculate the quantity:**
$$ \frac{\bar{x} - \mu}{s / \sqrt{n}} $$

**If your sample size ($n$) is greater than 30:**
*   Your sample [[standard_deviation_and_sampling_distribution | standard deviation]] ($s$) is a good approximation for the population [[standard_deviation_and_sampling_distribution | standard deviation]] ($\sigma$) <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.
*   The calculated value is approximately normally distributed <a class="yt-timestamp" data-t="00:05:59">[00:05:59]</a>.
*   Use it as a **Z-statistic** and consult a Z-table (or normal distribution table) to determine probabilities <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>.

**If your sample size ($n$) is small (less than 30):**
*   This statistic will have a **T-distribution** <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>.
*   Use it as a **T-statistic** and consult a T-table to determine probabilities <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>.
```