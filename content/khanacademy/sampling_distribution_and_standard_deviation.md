---
title: Sampling distribution and standard deviation
videoId: -FtlH4svqx4
---

From: [[khanacademy]] <br/> 

When conducting scientific research, such as testing the effect of a drug, statistical hypothesis testing is a crucial method to determine if observed results are significant or merely due to chance <a class="yt-timestamp" data-t="02:22:00">[02:22:00]</a>. This process involves setting up opposing hypotheses and assessing the probability of the collected data under a specific assumption <a class="yt-timestamp" data-t="02:27:00">[02:27:00]</a>.

## Setting Up Hypotheses

Consider a neurologist testing a drug's effect on rat response times. The mean response time for rats not injected with the drug is known to be 1.2 seconds <a class="yt-timestamp" data-t="00:13:00">[00:13:00]</a>. After injecting 100 rats, the observed mean response time is 1.05 seconds with a [[standard_deviation_explained | sample standard deviation]] of 0.5 seconds <a class="yt-timestamp" data-t="00:21:00">[00:21:00]</a>.

### Null Hypothesis (H₀)
The null hypothesis represents the status quo or the assumption that there is no effect <a class="yt-timestamp" data-t="00:44:00">[00:44:00]</a>. In this case, it states that the drug has no effect on response time <a class="yt-timestamp" data-t="00:47:00">[00:47:00]</a>. This implies that the mean response time for rats given the drug would still be 1.2 seconds, the same as for untreated rats <a class="yt-timestamp" data-t="01:11:00">[01:11:00]</a>.

### Alternative Hypothesis (H₁)
The alternative hypothesis is what the researcher typically wants to prove <a class="yt-timestamp" data-t="01:38:00">[01:38:00]</a>. It states that the drug *does* have an effect on response time <a class="yt-timestamp" data-t="01:52:00">[01:52:00]</a>. This means the mean response time with the drug would not be equal to 1.2 seconds <a class="yt-timestamp" data-t="01:56:00">[01:56:00]</a>.

## The Logic of Hypothesis Testing

To determine whether to accept the alternative hypothesis or default to the null hypothesis, the standard approach is to assume the null hypothesis is true <a class="yt-timestamp" data-t="02:27:00">[02:27:00]</a>. Then, one calculates the probability of observing results as extreme as, or more extreme than, the collected sample data <a class="yt-timestamp" data-t="02:32:00">[02:32:00]</a>. If this [[probability_and_distribution_modeling | probability]] is very small, it suggests the null hypothesis is likely untrue, allowing for its rejection in favor of the alternative hypothesis <a class="yt-timestamp" data-t="02:39:00">[02:39:00]</a>.

## Sampling Distribution

Assuming the null hypothesis is true, we consider the [[sampling_distribution_and_sample_mean | sampling distribution]] of the sample mean. With a sample size of 100, this distribution can be approximated as a normal distribution <a class="yt-timestamp" data-t="03:40:00">[03:40:00]</a>.

*   **Mean of the Sampling Distribution**: If the null hypothesis is true (drug has no effect), the mean of the [[sampling_distribution_and_sample_mean | sampling distribution]] would be the same as the [[population_vs_sample_in_statistics | population]] mean, which is 1.2 seconds <a class="yt-timestamp" data-t="03:52:00">[03:52:00]</a>.

*   **Standard Deviation of the Sampling Distribution (Standard Error)**: The [[standard_deviation_and_its_significance | standard deviation]] of the [[sampling_distribution_and_sample_mean | sampling distribution]], also known as the standard error, is calculated using the formula:
    $$ \sigma_{\bar{x}} = \frac{\sigma}{\sqrt{n}} $$
    where $\sigma$ is the [[standard_deviation_and_its_significance | population standard deviation]] and $n$ is the sample size <a class="yt-timestamp" data-t="04:13:00">[04:13:00]</a>. Since the [[standard_deviation_and_its_significance | population standard deviation]] is unknown, it is estimated using the [[standard_deviation_explained | sample standard deviation]] (0.5 seconds), which is a reasonable approximation for a sample size of 100 <a class="yt-timestamp" data-t="04:31:00">[04:31:00]</a>.

    Plugging in the values:
    $$ \hat{\sigma}_{\bar{x}} = \frac{0.5}{\sqrt{100}} = \frac{0.5}{10} = 0.05 $$
    So, the estimated [[standard_deviation_and_its_significance | standard deviation]] of the [[sampling_distribution_and_sample_mean | sampling distribution]] is 0.05 seconds <a class="yt-timestamp" data-t="05:12:00">[05:12:00]</a>.

## Calculating the Z-Score

To understand how unusual our sample mean (1.05 seconds) is if the null hypothesis were true, we calculate its Z-score. The Z-score measures how many [[standard_deviation_and_its_significance | standard deviations]] a data point is from the mean <a class="yt-timestamp" data-t="05:57:00">[05:57:00]</a>.

$$ Z = \frac{\bar{x} - \mu}{\hat{\sigma}_{\bar{x}}} $$
Where:
*   $\bar{x}$ = sample mean (1.05 seconds)
*   $\mu$ = hypothesized [[population_vs_sample_in_statistics | population]] mean (1.2 seconds)
*   $\hat{\sigma}_{\bar{x}}$ = estimated [[standard_deviation_and_its_significance | standard deviation]] of the [[sampling_distribution_and_sample_mean | sampling distribution]] (0.05 seconds)

$$ Z = \frac{1.05 - 1.2}{0.05} = \frac{-0.15}{0.05} = -3 $$
This means the observed sample mean of 1.05 seconds is 3 [[standard_deviation_and_its_significance | standard deviations]] below the hypothesized population mean <a class="yt-timestamp" data-t="07:15:00">[07:15:00]</a>.

## P-Value and Conclusion

The P-value is the [[probability_and_distribution_modeling | probability]] of obtaining a result as extreme as, or more extreme than, the observed data, assuming the null hypothesis is true <a class="yt-timestamp" data-t="10:32:00">[10:32:00]</a>.

Using the empirical rule, approximately 99.7% of data in a normal distribution falls within 3 [[standard_deviation_and_its_significance | standard deviations]] of the mean <a class="yt-timestamp" data-t="08:30:00">[08:30:00]</a>. This implies that the remaining 0.3% of the [[probability_and_distribution_modeling | probability]] is distributed in the tails beyond $\pm$3 [[standard_deviation_and_its_significance | standard deviations]] <a class="yt-timestamp" data-t="09:01:00">[09:01:00]</a>.

Since our Z-score is -3, we are interested in the [[probability_and_distribution_modeling | probability]] of being 3 [[standard_deviation_and_its_significance | standard deviations]] or more away from the mean in either direction (meaning values less than -3 or greater than +3) <a class="yt-timestamp" data-t="08:05:00">[08:05:00]</a>.

*   The P-value for a Z-score of -3 (two-tailed) is 0.003 or 0.3% <a class="yt-timestamp" data-t="09:07:00">[09:07:00]</a>.

This means that if the drug had no effect, there would only be a 0.3% chance of getting a sample mean as extreme as 1.05 seconds <a class="yt-timestamp" data-t="09:33:00">[09:33:00]</a>. This is less than 1 in 300 <a class="yt-timestamp" data-t="09:42:00">[09:42:00]</a>.

### Decision
Researchers often use a significance level (e.g., 5% or 0.05) as a threshold. If the P-value is less than this threshold, the null hypothesis is typically rejected <a class="yt-timestamp" data-t="11:03:00">[11:03:00]</a>.

In this case, since the P-value (0.003) is much less than 0.05, we reject the null hypothesis <a class="yt-timestamp" data-t="10:00:00">[10:00:00]</a>. The evidence strongly suggests that the drug *does* have an effect on response time <a class="yt-timestamp" data-t="11:16:00">[11:16:00]</a>.
