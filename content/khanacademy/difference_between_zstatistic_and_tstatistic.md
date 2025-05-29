---
title: Difference between Zstatistic and Tstatistic
videoId: 5ABpqVSx33I
---

From: [[khanacademy]] <br/> 

In [[introduction_to_inferential_statistics | inferential statistics]], a common goal is to determine the probability of obtaining a certain sample mean <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. This video aims to clarify the distinction between a Z-statistic and a T-statistic, which are tools used in this process <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>.

## Calculating Probability of a Sample Mean

When assessing the probability of a sample mean, the general approach involves determining how many standard deviations away from the assumed mean the sample mean lies <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. This is typically done by calculating the difference between the sample mean and the assumed population mean, then dividing by the standard deviation of the sampling distribution <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>.

The standard deviation of the sampling distribution can be expressed as the population standard deviation divided by the square root of the sample size, as per the Central Limit Theorem for a sufficient sample size <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>, <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.

This leads to the general formula:
$$ \frac{\text{Sample Mean} - \text{Assumed Population Mean}}{\frac{\text{Population Standard Deviation}}{\sqrt{\text{Sample Size}}}} $$ <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>

This quantity represents how many standard deviations the sample mean is from the population mean <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.

## Z-statistic

The quantity derived above is known as a [[zscore_and_sampling_distribution | Z-score]], or more specifically, a Z-statistic when it's derived from a sample mean <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.

### When to Use a Z-statistic

A Z-statistic is used under specific conditions:
1.  **Known Population Standard Deviation:** If the population standard deviation is known, the Z-statistic formula can be directly applied <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.
2.  **Large Sample Size (n > 30):** More commonly, the population standard deviation is unknown <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>. In such cases, if the sample size is greater than 30 (n > 30), the sample standard deviation can be used as a good approximation for the population standard deviation <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>, <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>, <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>. When this approximation is made with a sample size of 30 or more, the resulting statistic is considered to be approximately normally distributed <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>, <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>, and thus follows a normal distribution <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>.

### Interpretation

Once the Z-statistic is calculated, a Z-table or a normal distribution table can be consulted to find the probability of obtaining a sample mean at least as extreme as the observed one <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>, <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>. All Z-values are associated with a normal distribution <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>.

## T-statistic

### When to Use a T-statistic

A T-statistic is used when the sample size is small, specifically less than 30 (n < 30) <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>, <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>. In this scenario, if the population standard deviation is unknown and must be estimated using the sample standard deviation, the resulting statistic will *not* be normally distributed <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>, <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>. Instead, it will follow a T-distribution <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>, <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>.

The formula for the T-statistic is identical to the Z-statistic when the sample standard deviation is used to approximate the population standard deviation:
$$ \frac{\text{Sample Mean} - \text{Mean of Sampling Distribution}}{\frac{\text{Sample Standard Deviation}}{\sqrt{\text{Sample Size}}}} $$ <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>

### Interpretation

For a T-statistic, a T-table must be used to find the probability of getting a T-value at least as extreme as the calculated one <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>, <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>. The T-distribution is bell-shaped like the normal distribution but has fatter tails, especially for smaller sample sizes, reflecting greater uncertainty. When normalized, a T-distribution also has a mean of 0 <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>.

## Rule of Thumb

*   **Calculate the quantity:** Always compute the value using the formula involving the sample mean, assumed population mean, and sample standard deviation divided by the square root of the sample size <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>.
*   **Sample Size (n > 30):** If the sample size is greater than 30, the statistic is approximately normally distributed. Use a Z-table for probabilities <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>, <a class="yt-timestamp" data-t="00:05:59">[00:05:59]</a>.
*   **Sample Size (n < 30):** If the sample size is small, the statistic follows a T-distribution. Use a T-table for probabilities <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>, <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>.