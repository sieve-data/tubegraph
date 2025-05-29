---
title: Use of Zstatistic in inferential statistics
videoId: 5ABpqVSx33I
---

From: [[khanacademy]] <br/> 

In [[introduction_to_inferential_statistics | inferential statistics]], a primary goal is to determine the [[probability_in_inferential_statistics | probability]] of obtaining a specific sample mean <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. The Z-statistic is a key tool used for this purpose, particularly when dealing with large sample sizes <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

## What is a Z-Statistic?

A Z-statistic measures how many standard deviations a sample mean is away from the assumed mean of its [[zscore_and_sampling_distribution | sampling distribution]] <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a> <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>. It is essentially a [[calculating_probability_using_zscore | Z-score]] when derived from a sample mean statistic <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.

The formula for calculating a Z-statistic is:

```
Z = (Sample Mean - Mean of Sampling Distribution) / (Standard Deviation of Sampling Distribution)
```
<a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a> <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>

According to the Central Limit Theorem, for a sufficient sample size, the standard deviation of the [[zscore_and_sampling_distribution | sampling distribution]] of the sample mean can be approximated by the population standard deviation divided by the square root of the sample size <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a> <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a> <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.

Thus, the formula for the Z-statistic can be rewritten as:

```
Z = (Sample Mean - Mean of Sampling Distribution) / (Population Standard Deviation / sqrt(Sample Size))
```
<a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a> <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>

## Conditions for Using a Z-Statistic

The Z-statistic is typically used under specific conditions related to sample size and knowledge of the population standard deviation:

*   **Known Population Standard Deviation**: If the population standard deviation is known, the Z-statistic can be directly calculated as shown above <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.
*   **Large Sample Size (n > 30)**: Even if the population standard deviation is unknown, it can be approximated by the sample standard deviation if the sample size is greater than 30 <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a> <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a> <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>. In this case, the statistic obtained is still considered to be approximately normally distributed, allowing the use of Z-tables <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a> <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a> <a class="yt-timestamp" data-t="00:05:59">[00:05:59]</a>.

When these conditions are met, the calculated Z-statistic can be looked up in a Z-table (or normal distribution table) to determine the [[probability_in_inferential_statistics | probability]] of obtaining a result at least as extreme as the observed sample mean <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a> <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a> <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a> <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>.

## Z-statistic vs. T-statistic

The distinction between using a Z-statistic and a [[difference_between_zstatistic_and_tstatistic | T-statistic]] hinges primarily on sample size:

*   **Z-statistic**: Used when the sample size is large (typically > 30), allowing the assumption of a normal distribution for the statistic, even if the population standard deviation is estimated from the sample <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a> <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>.
*   **T-statistic**: Used when the sample size is small (less than 30), and the population standard deviation is unknown. In this scenario, the statistic follows a T-distribution instead of a normal distribution <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a> <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a> <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>.