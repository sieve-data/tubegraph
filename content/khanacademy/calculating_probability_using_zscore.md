---
title: Calculating probability using Zscore
videoId: 5ABpqVSx33I
---

From: [[khanacademy]] <br/> 

In [[inferential_statistics | inferential statistics]], a common goal is to [[calculating_probability | calculate the probability]] of obtaining a particular sample mean or a result at least as extreme as the observed sample mean <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>. This often involves determining how many standard deviations an observed sample mean is from the assumed population mean <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. This value is known as a [[zscore_and_sampling_distribution | Z-score]], or more specifically, a [[use_of_zstatistic_in_inferential_statistics | Z-statistic]] when derived from a sample mean <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.

## The Z-statistic Formula

The [[use_of_zstatistic_in_inferential_statistics | Z-statistic]] quantifies how many standard deviations an observation (in this case, a sample mean) is away from the mean of its [[zscore_and_sampling_distribution | sampling distribution]] <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>. For a [[zscore_and_sampling_distribution | sampling distribution]] of the sample mean, which typically has an assumed mean value and standard deviation <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>, the Z-statistic is calculated as:

$Z = \frac{\text{Sample Mean} - \text{Assumed Population Mean}}{\text{Standard Deviation of Sampling Distribution}}$ <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>

Based on the Central Limit Theorem, for a sufficient sample size, the standard deviation of the [[zscore_and_sampling_distribution | sampling distribution]] (also known as the standard error of the mean) is equivalent to the population standard deviation divided by the square root of the sample size <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.

Thus, the [[use_of_zstatistic_in_inferential_statistics | Z-statistic]] formula can be rewritten as:

$Z = \frac{\bar{x} - \mu}{\sigma / \sqrt{n}}$ <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>

Where:
*   $\bar{x}$ = Sample Mean
*   $\mu$ = Assumed Population Mean (mean of the [[zscore_and_sampling_distribution | sampling distribution]] of the sample mean)
*   $\sigma$ = Population Standard Deviation
*   $n$ = Sample Size

This formula provides "our best sense of how many standard deviations away from the actual mean we are" <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>.

## Approximating with Sample Standard Deviation

Often, the population standard deviation ($\sigma$) is unknown <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>. In such cases, it can be estimated using the sample standard deviation ($s$) <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>. The approximate [[use_of_zstatistic_in_inferential_statistics | Z-statistic]] becomes:

$Z \approx \frac{\bar{x} - \mu}{s / \sqrt{n}}$ <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>

This approximation is considered acceptable if the sample size is greater than 30, as the statistic will still be approximately normally distributed <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>. If the sample size is less than 30, this expression will not be normally distributed and would instead follow a T-distribution <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.

## Calculating Probability Using the Z-table

Once the [[use_of_zstatistic_in_inferential_statistics | Z-statistic]] is calculated, it can be used to [[calculating_probabilities_for_specific_outcomes | calculate probabilities for specific outcomes]]. For instance, to find the probability of getting a result at least as extreme as the observed sample mean <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>:

1.  Calculate the Z-statistic using the appropriate formula <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>.
2.  Look up this Z-value in a Z-table (standard normal distribution table) or use a normal distribution calculator <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>.
3.  The table or calculator will provide the [[calculating_probability_using_integrals | area under the curve]] corresponding to that Z-value, which represents the [[probability in inferential statistics | probability]] <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>. For example, to find the probability of getting a value of Z or greater, one would find the area in the tail beyond that Z-score <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>.

This process helps determine the likelihood of observing a specific sample mean under a given set of assumptions <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.