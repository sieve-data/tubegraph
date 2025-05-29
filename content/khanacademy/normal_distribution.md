---
title: Normal distribution
videoId: JNm3M9cqWyc
---

From: [[khanacademy]] <br/> 

The normal distribution is considered one of the most fundamental and profound concepts in statistics and mathematics <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. It frequently appears in statistical analysis because of its relationship with the [[central_limit_theorem | Central limit theorem]] <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>.

## Emergence via the Central Limit Theorem

The [[central_limit_theorem | Central limit theorem]] demonstrates a powerful property related to the normal distribution: if you take sample means (or sums) from *any* [[probability_distribution_functions | probability distribution function]]—whether it's [[continuous_random_variables | continuous]] or discrete, as long as it has a well-defined mean and variance (and thus a [[standard_deviation | standard deviation]])—the distribution of these sample means will approximate a normal distribution <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>, <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>.

### The Sampling Process
To illustrate this, consider a "crazy" discrete [[probability_distribution_functions | probability distribution function]] that is not normal, such as one where specific outcomes (e.g., 2 or 5) are impossible, and others (e.g., 1 or 6) are very likely <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>, <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>, <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.

The process involves:
1.  **Defining a Sample Size (n)**: For example, `n = 4` <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.
2.  **Taking Multiple Samples**: From the original distribution, individual samples of the specified size are drawn <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>. For instance, a first sample might be (1, 1, 3, 6) <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>.
3.  **Calculating the Sample Mean**: The mean of each sample is calculated (e.g., for (1, 1, 3, 6), the mean is 2.75) <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>, <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>.
4.  **Plotting the Sample Means**: Each calculated sample mean is plotted on a frequency distribution <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>.

### Approximating the Normal Distribution
As many, many samples are taken (e.g., 10,000 times) and their means plotted, the frequency distribution of these sample means will begin to approximate a normal distribution <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>, <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>, <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>.

### Impact of Sample Size (n)
The approximation improves with larger sample sizes <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>:
*   **Larger n**: A larger sample size (e.g., `n = 20` instead of `n = 4`) will result in a distribution of sample means that more closely approximates a normal distribution <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>, <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>.
*   **Theoretical Limit**: If the sample size approaches infinity, the distribution of sample means would be a perfect normal distribution <a class="yt-timestamp" data-t="00:07:53">[00:07:53]</a>, <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>.
*   **Practicality**: Even with relatively small sample sizes like 10 or 20, the approximation to a normal distribution can be very close, serving as a good practical approximation <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>.

## Significance in Statistics
The [[central_limit_theorem | Central limit theorem]] explains why the normal distribution is so prevalent in statistics <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>. Even when the underlying [[probability_distribution_functions | probability distribution functions]] of individual [[understanding_random_variables | random variables]] are unknown or "crazy," the sums or means of many independent actions or processes tend to follow a normal distribution <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>, <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>. This makes the normal distribution a very useful approximation for the sum or means of many real-world processes <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a>.

> [!NOTE] Sample Mean vs. Sample Sum
> The [[central_limit_theorem | Central limit theorem]] applies not only to the sample mean but also to the sample sum <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>.