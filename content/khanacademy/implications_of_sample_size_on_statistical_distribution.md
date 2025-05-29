---
title: Implications of sample size on statistical distribution
videoId: 5ABpqVSx33I
---

From: [[khanacademy]] <br/> 

In [[probability_in_inferential_statistics | inferential statistics]], a common goal is to determine the [[probability_in_inferential_statistics | probability]] of obtaining a particular [[sampling_and_sample_means | sample mean]] <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. This often involves understanding how many standard deviations a [[sampling_and_sample_means | sample mean]] is from the assumed population mean <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>. The choice between using a Z-statistic or a T-statistic, and consequently a normal or T-distribution, is primarily influenced by the [[population_versus_sample_in_statistics | sample]] size and whether the [[population_versus_sample_in_statistics | population]] standard deviation is known <a class="yt-timestamp" data-t="00:06:32">[00:06:32]</a>.

## Z-statistic: Large Sample Sizes

When dealing with a large [[population_versus_sample_in_statistics | sample]] size, the Z-statistic is typically employed to determine the [[probability_in_inferential_statistics | probability]] of a given [[sampling_and_sample_means | sample mean]] <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.

The formula for the Z-statistic, based on the [[sampling_and_sample_means | sample mean]], is:
$$Z = \frac{\bar{x} - \mu_{\bar{x}}}{\sigma_{\bar{x}}}$$
Where:
*   $\bar{x}$ is the [[sampling_and_sample_means | sample mean]] <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>
*   $\mu_{\bar{x}}$ is the mean of the [[sampling_and_sample_means | sampling distribution]] <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>
*   $\sigma_{\bar{x}}$ is the standard deviation of the [[sampling_and_sample_means | sampling distribution]] <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>

According to the [[importance_of_central_limit_theorem_in_statistics | Central Limit Theorem]], if the [[population_versus_sample_in_statistics | sample]] size is sufficiently large, the standard deviation of the [[sampling_and_sample_means | sampling distribution]] ($\sigma_{\bar{x}}$) can be approximated by the [[population_versus_sample_in_statistics | population]] standard deviation ($\sigma$) divided by the square root of the [[population_versus_sample_in_statistics | sample]] size ($n$) <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>:
$$ \sigma_{\bar{x}} \approx \frac{\sigma}{\sqrt{n}} $$
This allows the Z-statistic formula to be written as:
$$Z = \frac{\bar{x} - \mu_{\bar{x}}}{\sigma / \sqrt{n}}$$
This Z-statistic represents how many standard deviations the [[sampling_and_sample_means | sample mean]] is away from the assumed mean <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.

### Approximation with Sample Standard Deviation

Often, the [[population_versus_sample_in_statistics | population]] standard deviation ($\sigma$) is unknown <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>. For large [[population_versus_sample_in_statistics | sample]] sizes (typically $n > 30$), the [[population_versus_sample_in_statistics | sample]] standard deviation ($s$) can be used as a good approximation for the [[population_versus_sample_in_statistics | population]] standard deviation <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>:
$$Z \approx \frac{\bar{x} - \mu_{\bar{x}}}{s / \sqrt{n}}$$
When the [[population_versus_sample_in_statistics | sample]] size is greater than 30, this statistic will be approximately normally distributed <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>. This allows for the use of a Z-table (or normal distribution table) to determine the [[probability_in_inferential_statistics | probability]] of observing a result at least as extreme as the calculated Z-value <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>.

## T-statistic: Small Sample Sizes

When the [[population_versus_sample_in_statistics | population]] standard deviation is unknown and the [[population_versus_sample_in_statistics | sample]] size is small (especially less than 30), the statistic used to determine the [[probability_in_inferential_statistics | probability]] does not follow a normal distribution <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>. In this scenario, a T-statistic is used, and it follows a T-distribution <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>.

The T-statistic uses the [[population_versus_sample_in_statistics | sample]] standard deviation ($s$) directly:
$$T = \frac{\bar{x} - \mu_{\bar{x}}}{s / \sqrt{n}}$$
For small [[population_versus_sample_in_statistics | sample]] sizes ($n < 30$), this statistic will have a T-distribution <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>. Like the normal distribution, a normalized T-distribution will have a mean of 0 <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>. To find the [[probability_in_inferential_statistics | probability]] of a T-value at least as extreme as the calculated one, a T-table must be used <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>.

## Rule of Thumb

The key differentiator for choosing between a Z-statistic and a T-statistic is the [[population_versus_sample_in_statistics | sample]] size, particularly when the [[population_versus_sample_in_statistics | population]] standard deviation is unknown <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>:

> [!summary] Z-statistic vs. T-statistic
> *   If your [[population_versus_sample_in_statistics | sample]] size is greater than 30 ($n > 30$), use the Z-statistic (which will be approximately normally distributed) and consult a Z-table for [[probability_in_inferential_statistics | probabilities]] <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>.
> *   If your [[population_versus_sample_in_statistics | sample]] size is small ($n < 30$), use the T-statistic (which will have a T-distribution) and consult a T-table for [[probability_in_inferential_statistics | probabilities]] <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>.