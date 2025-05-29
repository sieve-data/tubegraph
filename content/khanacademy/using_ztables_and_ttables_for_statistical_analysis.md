---
title: Using Ztables and Ttables for statistical analysis
videoId: 5ABpqVSx33I
---

From: [[khanacademy]] <br/> 

In [[inferential_statistics | inferential statistics]], a common goal is to determine the probability of obtaining a certain sample mean, or a result at least as extreme as an observed sample mean <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>, <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>. This is typically achieved by calculating how many standard deviations the sample mean is from the assumed population mean <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. The choice between using a Z-statistic or a T-statistic depends primarily on the sample size and whether the population standard deviation is known.

## Z-statistic

The Z-statistic, also known as a [[calculating_zscores_and_pvalues | Z-score]], measures how many standard deviations a sample mean is from the population mean <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.

The formula for the Z-statistic is:

> $$ Z = \frac{\bar{x} - \mu_{\bar{x}}}{\sigma_{\bar{x}}} $$
> Where:
> *   $\bar{x}$ is the sample mean <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>.
> *   $\mu_{\bar{x}}$ is the assumed mean of the sampling distribution of the sample means <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>.
> *   $\sigma_{\bar{x}}$ is the standard deviation of the sampling distribution <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.

According to the Central Limit Theorem, if the sample size is sufficient, the standard deviation of the sampling distribution ($\sigma_{\bar{x}}$) can be calculated as the population standard deviation ($\sigma$) divided by the square root of the sample size ($n$) <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>, <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>:

> $$ \sigma_{\bar{x}} = \frac{\sigma}{\sqrt{n}} $$

So, the Z-statistic formula can be rewritten as:

> $$ Z = \frac{\bar{x} - \mu_{\bar{x}}}{\sigma / \sqrt{n}} $$
> This provides the best estimate of how many standard deviations the sample mean is from the actual mean <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>.

Once the Z-statistic is calculated, a Z-table (or normal distribution table) is used to find the probability of obtaining a value at least as extreme as the calculated Z-score <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>, <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>.

### When to Use Z-statistic (Approximation)

In many real-world scenarios, the population standard deviation ($\sigma$) is unknown <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>, <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>. In such cases, it can be approximated using the sample standard deviation ($s$) <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>, <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>. The Z-statistic formula then becomes:

> $$ Z \approx \frac{\bar{x} - \mu_{\bar{x}}}{s / \sqrt{n}} $$

This approximation is considered acceptable if the sample size ($n$) is greater than 30 <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>. With a sample size of 30 or more, this approximated statistic will be approximately normally distributed <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>, <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>.

## T-statistic

The T-statistic is used when the population standard deviation is unknown and the sample size is small, typically less than 30 <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>. The calculation for the T-statistic is the same as the approximated Z-statistic:

> $$ T = \frac{\bar{x} - \mu_{\bar{x}}}{s / \sqrt{n}} $$
> Where:
> *   $\bar{x}$ is the sample mean <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>.
> *   $\mu_{\bar{x}}$ is the assumed mean of the sampling distribution <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>.
> *   $s$ is the sample standard deviation <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>.
> *   $n$ is the sample size <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>.

The critical distinction is that when the sample size is small (less than 30), this expression will *not* be normally distributed <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>, <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>. Instead, it follows a T-distribution <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>.

Like the Z-distribution, a normalized T-distribution has a mean of 0 <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>, <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>. To find the probability of a T-value at least as extreme as the calculated one, a T-table is used <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>, <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>, <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>.

## The Key Difference: Sample Size

The primary difference between a Z-statistic and a T-statistic lies in the sample size ($n$) when the population standard deviation is unknown <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>, <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>.

> [!Rule of Thumb]
> *   **If $n > 30$**: Use the sample standard deviation as a good approximation for the population standard deviation. The statistic is approximately normally distributed, so use a Z-table to find probabilities <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>, <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>, <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>, <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>.
> *   **If $n < 30$**: The statistic will have a T-distribution. Use a T-table to find probabilities <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>, <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>, <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>.

Understanding this distinction helps in selecting the appropriate statistical distribution and table for accurate probability calculations <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>.