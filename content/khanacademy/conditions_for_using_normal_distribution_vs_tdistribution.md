---
title: Conditions for using normal distribution vs Tdistribution
videoId: 5ABpqVSx33I
---

From: [[khanacademy]] <br/> 

When performing inferential statistics, especially when trying to determine the [[probability_distribution_and_density_functions | probability]] of obtaining a certain sample mean, statisticians often calculate a test statistic to measure how many [[standard_deviation_and_sampling_distribution | standard deviations]] a sample mean is from an assumed population mean <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. This calculation leads to either a Z-statistic or a T-statistic, each used under specific conditions <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>.

## Z-statistic and Normal Distribution

A Z-statistic (or Z-score) is used when the test statistic is approximately [[normal_distribution | normally distributed]] <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>. It quantifies how many [[standard_deviation_and_sampling_distribution | standard deviations]] a particular sample mean is away from the assumed population mean <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.

The formula for a Z-statistic is:
$$ Z = \frac{\bar{x} - \mu_{\bar{x}}}{\sigma_{\bar{x}}} $$
where:
*   $\bar{x}$ is the sample mean <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>
*   $\mu_{\bar{x}}$ is the mean of the [[sampling_distribution_and_standard_deviation | sampling distribution]] of the sample mean (assumed population mean) <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>
*   $\sigma_{\bar{x}}$ is the [[standard_deviation_and_sampling_distribution | standard deviation]] of the [[sampling_distribution_and_standard_deviation | sampling distribution]] of the sample mean <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.

According to the [[application_of_central_limit_theorem_in_real_life | Central Limit Theorem]], $\sigma_{\bar{x}}$ can be approximated as $\frac{\sigma}{\sqrt{n}}$, where $\sigma$ is the population [[standard_deviation_and_sampling_distribution | standard deviation]] and $n$ is the sample size <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>.

### Conditions for using Z-statistic:

1.  **Population Standard Deviation is Known**: If the true population [[standard_deviation_and_sampling_distribution | standard deviation]] ($\sigma$) is known, the Z-statistic can be used directly <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.
2.  **Large Sample Size (n > 30)**: Even if the population [[standard_deviation_and_sampling_distribution | standard deviation]] is unknown, but the sample size ($n$) is greater than 30, the sample [[standard_deviation_and_sampling_distribution | standard deviation]] ($s$) is considered a good approximation for the population [[standard_deviation_and_sampling_distribution | standard deviation]] <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>. In this case, the resulting statistic is approximately [[normal_distribution | normally distributed]] <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.

Once a Z-statistic is calculated, its [[probability_distribution_and_density_functions | probability]] can be determined by looking it up in a Z-table or a [[normal_distribution | normal distribution]] table <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>.

## T-statistic and T-distribution

A T-statistic is used when the population [[standard_deviation_and_sampling_distribution | standard deviation]] is unknown and the sample size is small <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>. In this scenario, the sample [[standard_deviation_and_sampling_distribution | standard deviation]] ($s$) is used to estimate the population [[standard_deviation_and_sampling_distribution | standard deviation]] <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>.

The formula for a T-statistic is:
$$ T = \frac{\bar{x} - \mu_{\bar{x}}}{s / \sqrt{n}} $$
where:
*   $\bar{x}$ is the sample mean <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>
*   $\mu_{\bar{x}}$ is the mean of the [[sampling_distribution_and_standard_deviation | sampling distribution]] of the sample mean (assumed population mean) <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>
*   $s$ is the sample [[standard_deviation_and_sampling_distribution | standard deviation]] <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>
*   $n$ is the sample size <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>

### Conditions for using T-statistic:

1.  **Population Standard Deviation is Unknown**: This is the primary condition where the sample [[standard_deviation_and_sampling_distribution | standard deviation]] ($s$) must be used as an estimate <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>.
2.  **Small Sample Size (n < 30)**: When the sample size is less than 30, especially significantly less than 30, the statistic derived using the sample [[standard_deviation_and_sampling_distribution | standard deviation]] will not be [[normal_distribution | normally distributed]] <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>. Instead, it follows a T-distribution <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>.

To find the [[probability_distribution_and_density_functions | probability]] associated with a T-statistic, a T-table must be used, which requires considering the degrees of freedom (typically $n-1$) <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>.

## Rule of Thumb: When to Use Which

A simple rule of thumb for deciding between a Z-statistic and a T-statistic when the population [[standard_deviation_and_sampling_distribution | standard deviation]] is unknown is based on the sample size:

*   **Sample Size ($n$) > 30**: The calculated statistic is approximately [[normal_distribution | normally distributed]], so use a **Z-table** for probabilities <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>.
*   **Sample Size ($n$) < 30**: The calculated statistic follows a T-distribution, so use a **T-table** for probabilities <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>.

Understanding this distinction is crucial for accurate inferential statistics <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>.