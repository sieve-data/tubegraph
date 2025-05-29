---
title: Difference between Zstatistics and Tstatistics
videoId: 5ABpqVSx33I
---

From: [[khanacademy]] <br/> 

In [[inferential_statistics_and_probability_of_sample_means | inferential statistics]], both Z-statistics and T-statistics are used to determine the probability of obtaining a certain sample [[mean_or_central_tendency_in_statistics | mean]] <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. The core difference lies in the conditions under which each is applied, primarily based on sample size and knowledge of the population [[standard_deviation_and_sampling_distribution | standard deviation]] <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.

## Z-statistic

The Z-statistic, or Z-score, quantifies how many [[standard_deviation_and_sampling_distribution | standard deviations]] a sample [[mean_or_central_tendency_in_statistics | mean]] is from the assumed population [[mean_or_central_tendency_in_statistics | mean]] within a [[sampling_distribution_and_standard_deviation | sampling distribution]] <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.

### Formula
The general formula for a Z-statistic is:
$$ Z = \frac{\bar{x} - \mu}{\sigma_{\bar{x}}} $$
Where:
*   $ \bar{x} $ is the sample [[mean_or_central_tendency_in_statistics | mean]] <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>
*   $ \mu $ is the assumed [[mean_or_central_tendency_in_statistics | mean]] of the [[sampling_distribution_and_standard_deviation | sampling distribution]] (or population [[mean_or_central_tendency_in_statistics | mean]]) <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>
*   $ \sigma_{\bar{x}} $ is the [[standard_deviation_and_sampling_distribution | standard deviation]] of the [[sampling_distribution_and_standard_deviation | sampling distribution]] (also known as the standard error) <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>

The standard error ($ \sigma_{\bar{x}} $) can be expressed as $ \frac{\sigma}{\sqrt{n}} $, where $ \sigma $ is the population [[standard_deviation_and_sampling_distribution | standard deviation]] and $ n $ is the sample size <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.

So, the Z-statistic formula can also be written as:
$$ Z = \frac{\bar{x} - \mu}{\sigma / \sqrt{n}} $$ <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>

### Conditions for Use
A Z-statistic is typically used when:
*   The population [[standard_deviation_and_sampling_distribution | standard deviation]] ($ \sigma $) is known <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.
*   The sample size ($ n $) is large, generally $ n > 30 $ <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>. In this scenario, even if the population [[standard_deviation_and_sampling_distribution | standard deviation]] is unknown and approximated by the sample [[descriptive_statistics_basics | standard deviation]], the statistic is considered [[conditions_for_using_normal_distribution_vs_tdistribution | normally distributed]] due to the Central Limit Theorem <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.

### Distribution
The Z-statistic follows a [[conditions_for_using_normal_distribution_vs_tdistribution | normal distribution]] (specifically, a standard normal distribution with a [[mean_or_central_tendency_in_statistics | mean]] of 0 and a [[standard_deviation_and_sampling_distribution | standard deviation]] of 1) <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>. Probabilities associated with Z-values are found using a Z-table or normal distribution table <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>.

## T-statistic

The T-statistic is used in situations similar to the Z-statistic, but specifically when the population [[standard_deviation_and_sampling_distribution | standard deviation]] is unknown and the sample size is small <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.

### Formula
The formula for a T-statistic is similar to the approximated Z-statistic:
$$ T = \frac{\bar{x} - \mu}{s / \sqrt{n}} $$ <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>
Where:
*   $ \bar{x} $ is the sample [[mean_or_central_tendency_in_statistics | mean]]
*   $ \mu $ is the assumed [[mean_or_central_tendency_in_statistics | mean]] of the [[sampling_distribution_and_standard_deviation | sampling distribution]]
*   $ s $ is the **sample** [[descriptive_statistics_basics | standard deviation]], used as an estimate for the unknown population [[standard_deviation_and_sampling_distribution | standard deviation]] <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>
*   $ n $ is the sample size

### Conditions for Use
A T-statistic is used when:
*   The population [[standard_deviation_and_sampling_distribution | standard deviation]] ($ \sigma $) is **unknown** <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>.
*   The sample size ($ n $) is **small**, typically $ n < 30 $ <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.

### Distribution
When the sample size is small ($ n < 30 $) and the population [[standard_deviation_and_sampling_distribution | standard deviation]] is unknown, the statistic calculated using the sample [[descriptive_statistics_basics | standard deviation]] will have a [[conditions_for_using_normal_distribution_vs_tdistribution | T-distribution]] rather than a normal distribution <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>. The [[conditions_for_using_normal_distribution_vs_tdistribution | T-distribution]] has fatter tails than the normal distribution, accounting for the increased uncertainty when using a sample [[descriptive_statistics_basics | standard deviation]] to estimate the population's <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>. Probabilities are found using a T-table, which requires considering the degrees of freedom (typically $ n-1 $) <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>.

## Summary of Differences
| Feature               | Z-statistic                                      | T-statistic                                                                |
| :-------------------- | :----------------------------------------------- | :------------------------------------------------------------------------- |
| **Purpose**           | Calculate probability of sample [[mean_or_central_tendency_in_statistics | mean]] | Calculate probability of sample [[mean_or_central_tendency_in_statistics | mean]] |
| **Population SD**     | Known OR Sample size ($ n > 30 $)              | Unknown (estimated by sample SD) <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a> |
| **Sample Size**       | Large ($ n > 30 $) <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a> | Small ($ n < 30 $) <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a> |
| **Distribution**      | [[conditions_for_using_normal_distribution_vs_tdistribution | Normal distribution]] <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a> | [[conditions_for_using_normal_distribution_vs_tdistribution | T-distribution]] <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a> |
| **Probability Table** | Z-table / Normal distribution table <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a> | T-table <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>                                                              |