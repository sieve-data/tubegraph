---
title: Central Limit Theorem and sample size implications
videoId: 5ABpqVSx33I
---

From: [[khanacademy]] <br/> 
In inferential statistics, a common goal is to determine the probability of obtaining a specific [[sampling_distribution_and_sample_mean | sample mean]] <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. This involves understanding the distinction between a Z-statistic and a T-statistic <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>.

### Z-Statistic

To calculate the probability of a [[sampling_distribution_and_sample_mean | sample mean]], we typically determine how many [[sampling_distribution_and_standard_deviation | standard deviations]] the sample result is from the assumed [[central_tendency_in_statistics | mean]] <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. This calculation is derived from the [[sampling_distribution_and_sample_mean | sampling distribution]] of the [[sampling_distribution_and_sample_mean | sample mean]] <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.

The formula for the Z-statistic is:
$$Z = \frac{\text{Sample Mean} - \text{Assumed Population Mean}}{\text{Standard Deviation of Sampling Distribution}}$$ <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>

Often, the [[sampling_distribution_and_standard_deviation | standard deviation]] of the [[sampling_distribution_and_sample_mean | sampling distribution]] is unknown <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>. The Central Limit Theorem states that with a sufficient sample size, the [[sampling_distribution_and_standard_deviation | standard deviation]] of the [[sampling_distribution_and_sample_mean | sampling distribution]] of the [[sampling_distribution_and_sample_mean | sample mean]] is equivalent to the [[sampling_distribution_and_standard_deviation | standard deviation]] of the [[population_vs_sample_in_statistics | population]] divided by the square root of the sample size <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>.

So, the Z-statistic can be written as:
$$Z = \frac{\text{Sample Mean} - \text{Assumed Population Mean}}{\frac{\text{Population Standard Deviation}}{\sqrt{\text{Sample Size}}}}$$ <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>

This Z-statistic, when derived from the [[sampling_distribution_and_sample_mean | sample mean]] statistic, is a Z-score <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>. We can then use a Z-table or normal distribution table to find the probability of obtaining a Z-value of that magnitude or greater <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>.

### T-Statistic and Sample Size Implications

In many real-world scenarios, the [[sampling_distribution_and_standard_deviation | standard deviation]] of the [[population_vs_sample_in_statistics | population]] is also unknown <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>. To approximate this, we use the [[sampling_distribution_and_standard_deviation | sample standard deviation]] <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.

The approximate Z-statistic formula then becomes:
$$Z \approx \frac{\text{Sample Mean} - \text{Assumed Population Mean}}{\frac{\text{Sample Standard Deviation}}{\sqrt{\text{Sample Size}}}}$$ <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>

#### Role of Sample Size

*   **Large Sample Size (n > 30)**: If the sample size is greater than 30, this approximation will be approximately normally distributed <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>. In this case, the [[sampling_distribution_and_standard_deviation | sample standard deviation]] is a good approximation for the [[sampling_distribution_and_standard_deviation | population standard deviation]] <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>, and a Z-table can be used to determine probabilities <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>.

*   **Small Sample Size (n < 30)**: If the sample size is less than 30, this expression will *not* be normally distributed <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>. Instead, this quantity follows a **T-distribution** <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>, and the value is called a T-statistic.
    The T-statistic is calculated using the same formula:
    $$T = \frac{\text{Sample Mean} - \text{Assumed Population Mean}}{\frac{\text{Sample Standard Deviation}}{\sqrt{\text{Sample Size}}}}$$ <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>
    For a small sample size, one must use a T-table to find the probability of obtaining a T-value at least as extreme as the calculated one <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>. A normalized T-distribution also has a [[central_tendency_in_statistics | mean]] of 0 <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>.

In essence, the critical distinction between using a Z-statistic and a T-statistic hinges on the sample size: a sample size greater than 30 allows for the use of Z-statistics and normal distribution tables, while a smaller sample size necessitates the use of T-statistics and T-distribution tables <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>.