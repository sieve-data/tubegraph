---
title: Difference between Zstatistic and Tstatistic
videoId: 5ABpqVSx33I
---

From: [[khanacademy]] <br/> 

In [[basic_concepts_in_probability_and_statistics | inferential statistics]], a common goal is to determine the probability of obtaining a certain [[mean_in_statistics | sample mean]] from a given [[population_vs_sample_in_statistics | population]] <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>. This often involves calculating how many standard deviations a [[mean_in_statistics | sample mean]] is from the assumed [[mean_in_statistics | population mean]] <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. The choice between using a Z-statistic or a T-statistic depends primarily on whether the [[population_vs_sample_in_statistics | population standard deviation]] is known and the size of the [[population_vs_sample_in_statistics | sample]] <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>.

## Z-statistic

A Z-statistic, also known as a [[calculating_zscores_and_pvalues | Z-score]] when derived from a statistic, quantifies how many standard deviations a [[mean_in_statistics | sample mean]] is from the [[mean_in_statistics | population mean]] <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.

The formula for a Z-statistic is:
$$ Z = \frac{\bar{x} - \mu}{\sigma / \sqrt{n}} $$
Where:
*   $\bar{x}$ = [[mean_in_statistics | sample mean]] <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>
*   $\mu$ = [[mean_in_statistics | mean]] of the sampling distribution of the [[mean_in_statistics | sample mean]] (which is assumed to be the [[mean_in_statistics | population mean]]) <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>
*   $\sigma$ = [[population_vs_sample_in_statistics | population standard deviation]] <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>
*   $n$ = [[population_vs_sample_in_statistics | sample]] size <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>

### When to use a Z-statistic

A Z-statistic is typically used under the following conditions:
*   **Population Standard Deviation is Known:** When the true [[population_vs_sample_in_statistics | population standard deviation]] ($\sigma$) is known <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.
*   **Large Sample Size (n > 30):** Even if the [[population_vs_sample_in_statistics | population standard deviation]] is unknown, if the [[population_vs_sample_in_statistics | sample]] size is greater than 30, the [[population_vs_sample_in_statistics | sample standard deviation]] (s) can be a good approximation for the [[population_vs_sample_in_statistics | population standard deviation]] <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>. The Central Limit Theorem states that with a sufficient [[population_vs_sample_in_statistics | sample]] size, the sampling distribution of the [[mean_in_statistics | sample mean]] will be approximately normally distributed <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>.

### Distribution and Interpretation
[[calculating_zscores_and_pvalues | Z-scores]] are normally distributed <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>. After calculating the Z-statistic, one can use a [[using_ztables_and_ttables_for_statistical_analysis | Z-table]] (or normal distribution table) to determine the probability of getting a result at least as extreme as the observed [[mean_in_statistics | sample mean]] <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>.

## T-statistic

A T-statistic is used when the [[population_vs_sample_in_statistics | population standard deviation]] is unknown and must be estimated from the [[population_vs_sample_in_statistics | sample]] <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.

The formula for a T-statistic is:
$$ T = \frac{\bar{x} - \mu}{s / \sqrt{n}} $$
Where:
*   $\bar{x}$ = [[mean_in_statistics | sample mean]] <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>
*   $\mu$ = [[mean_in_statistics | mean]] of the sampling distribution of the [[mean_in_statistics | sample mean]] <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>
*   $s$ = [[population_vs_sample_in_statistics | sample standard deviation]] (an estimate of $\sigma$) <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>
*   $n$ = [[population_vs_sample_in_statistics | sample]] size <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>

### When to use a T-statistic
A T-statistic is typically used under the following conditions:
*   **Population Standard Deviation is Unknown:** When the true [[population_vs_sample_in_statistics | population standard deviation]] is not known, and the [[population_vs_sample_in_statistics | sample standard deviation]] (s) is used as an estimate <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>.
*   **Small Sample Size (n < 30):** If the [[population_vs_sample_in_statistics | sample]] size is less than 30, especially significantly less than 30, the distribution of the calculated statistic will not be normally distributed <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.

### Distribution and Interpretation
If the [[population_vs_sample_in_statistics | sample]] size is small and the [[population_vs_sample_in_statistics | population standard deviation]] is estimated, the statistic follows a T-distribution <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>. The T-distribution is similar to a normal distribution but has fatter tails, accounting for the increased uncertainty due to estimating the [[population_vs_sample_in_statistics | population standard deviation]] from a small [[population_vs_sample_in_statistics | sample]]. A [[using_ztables_and_ttables_for_statistical_analysis | T-table]] is then used to find the probability of a T-value at least as extreme as the calculated statistic <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>.

## Key Differences and Rule of Thumb

The fundamental difference lies in the assumption about the [[population_vs_sample_in_statistics | population standard deviation]] and its impact on the sampling distribution:

*   **Z-statistic:** Assumes the [[population_vs_sample_in_statistics | population standard deviation]] ($\sigma$) is known, or that the [[population_vs_sample_in_statistics | sample]] size is large enough (n > 30) for the [[population_vs_sample_in_statistics | sample standard deviation]] (s) to serve as a reliable estimate, resulting in a normal distribution <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.
*   **T-statistic:** Used when the [[population_vs_sample_in_statistics | population standard deviation]] ($\sigma$) is unknown and the [[population_vs_sample_in_statistics | sample]] size is small (n < 30), leading to a T-distribution <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>.

In summary, calculate the quantity:
$$ \frac{\text{sample mean} - \text{assumed population mean}}{\text{standard error of the mean}} $$
If your [[population_vs_sample_in_statistics | sample]] size is more than 30, use a [[using_ztables_and_ttables_for_statistical_analysis | Z-table]]. If your [[population_vs_sample_in_statistics | sample]] size is small, use a [[using_ztables_and_ttables_for_statistical_analysis | T-table]] <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>.