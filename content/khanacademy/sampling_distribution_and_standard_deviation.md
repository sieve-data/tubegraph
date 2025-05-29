---
title: Sampling distribution and standard deviation
videoId: -FtlH4svqx4
---

From: [[khanacademy]] <br/> 

This article explores how [[standard_deviation_and_sampling_distribution|sampling distribution]] and [[variance_and_standard_deviation|standard deviation]] are used in the context of a hypothesis test to determine the effect of a drug on response time in rats <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>.

## Experimental Setup <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>
A neurologist injected 100 rats with a unit dose of a drug and recorded their response times to a neurological stimulus <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. The known mean response time for rats *not* injected with the drug is 1.2 seconds <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. For the 100 injected rats, the mean response time was 1.05 seconds with a [[Variance and its Calculation for Population and Sample|sample standard deviation]] of 0.5 seconds <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>. The objective is to determine if the drug affects response time <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.

## Hypothesis Formulation <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>
To address this question, two hypotheses are set up:

### Null Hypothesis (H₀) <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>
The null hypothesis is considered the "status quo" <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>, assuming that the research subject has no effect <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.
*   **Statement:** The drug has no effect on response time <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.
*   **Statistical Representation:** The mean response time for rats taking the drug is still 1.2 seconds (μ = 1.2 seconds) <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.

### Alternative Hypothesis (H₁) <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>
The alternative hypothesis proposes that the drug does have an effect <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.
*   **Statement:** The drug has an effect on response time <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.
*   **Statistical Representation:** The mean response time when the drug is given does not equal 1.2 seconds (μ ≠ 1.2 seconds) <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>.

## The Approach: P-Value Calculation <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>
The method to determine whether to accept the alternative hypothesis or default to the null hypothesis involves calculating a P-value <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>. This is done by assuming the null hypothesis is true and then calculating the [[probability_distribution_and_density_functions|probability]] of obtaining the observed sample results, or results even more extreme <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>. If this [[probability_distribution_and_density_functions|probability]] (P-value) is very small, it suggests the null hypothesis is likely untrue and can be rejected in favor of the alternative hypothesis <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>.

### Sampling Distribution under the Null Hypothesis <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>
Assuming the null hypothesis is true (drug has no effect), the [[standard_deviation_and_sampling_distribution|sampling distribution]] of sample means:
*   Will be a [[Normal Distribution|normal distribution]] due to a sufficiently large [[Sample Size and Sampling|sample size]] (100 rats) <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.
*   Its mean will be equal to the population mean under the null hypothesis, which is 1.2 seconds <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.

### Standard Deviation of the Sampling Distribution (Standard Error) <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>
The [[standard_deviation_and_sampling_distribution|standard deviation]] of the [[standard_deviation_and_sampling_distribution|sampling distribution]] (also known as the standard error of the mean) is calculated as:
$$ \sigma_{\bar{x}} = \frac{\sigma}{\sqrt{n}} $$
where:
*   $\sigma$ is the population [[variance_and_standard_deviation|standard deviation]] <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.
*   $n$ is the [[Sample Size and Sampling|sample size]] (square root of 100 in this case) <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>.

Since the population [[variance_and_standard_deviation|standard deviation]] ($\sigma$) is unknown, it is estimated using the [[Variance and its Calculation for Population and Sample|sample standard deviation]] (0.5 seconds), which is reasonable given the [[Sample Size and Sampling|sample size]] of 100 <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.

The estimated [[standard_deviation_and_sampling_distribution|standard deviation]] of the [[standard_deviation_and_sampling_distribution|sampling distribution]] is:
$$ \hat{\sigma}_{\bar{x}} = \frac{0.5}{\sqrt{100}} = \frac{0.5}{10} = 0.05 $$
So, the standard deviation of the sampling distribution is 0.05 <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.

### Calculating the Z-score <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>
A Z-score is calculated to determine how many [[variance_and_standard_deviation|standard deviations]] the observed sample mean (1.05 seconds) is from the hypothesized population mean (1.2 seconds) <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>.
$$ Z = \frac{\text{Sample Mean} - \text{Hypothesized Population Mean}}{\text{Standard Deviation of Sampling Distribution}} $$
$$ Z = \frac{1.05 - 1.2}{0.05} = \frac{-0.15}{0.05} = -3 $$
The absolute value of the Z-score is 3 <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a>. This means the observed sample mean is 3 [[variance_and_standard_deviation|standard deviations]] below the hypothesized population mean <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.

## Determining the P-Value <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>
The P-value is the [[probability_distribution_and_density_functions|probability]] of obtaining a result as extreme as, or more extreme than, the observed sample mean, assuming the null hypothesis is true <a class="yt-timestamp" data-t="00:10:32">[00:10:32]</a>. Since the alternative hypothesis is that the mean does not equal 1.2 seconds (two-tailed test), we consider results that are 3 [[variance_and_standard_deviation|standard deviations]] or more away from the mean in either direction <a class="yt-timestamp" data-t="00:08:05">[00:08:05]</a>.

Using the empirical rule for a [[Normal Distribution|normal distribution]], 99.7% of the [[probability_distribution_and_density_functions|probability]] lies within 3 [[variance_and_standard_deviation|standard deviations]] of the mean <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>. Therefore, the remaining 0.3% of the [[probability_distribution_and_density_functions|probability]] is distributed in the tails beyond ±3 [[variance_and_standard_deviation|standard deviations]] <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>.

*   P-value = 0.3% or 0.003 <a class="yt-timestamp" data-t="00:09:07">[00:09:07]</a>.

## Conclusion <a class="yt-timestamp" data-t="00:09:28">[00:09:28]</a>
If the null hypothesis were true, there would only be a 0.3% [[probability_distribution_and_density_functions|probability]] of obtaining a sample mean as extreme as 1.05 seconds (or more extreme) by chance <a class="yt-timestamp" data-t="00:09:33">[00:09:33]</a>. This is less than 1 in 300 <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>.

Because the P-value (0.003) is very small, it is a strong indicator that the null hypothesis is incorrect <a class="yt-timestamp" data-t="00:11:16">[00:11:16]</a>. Most common thresholds for rejecting the null hypothesis (e.g., 5% or 0.05) are much higher than this P-value <a class="yt-timestamp" data-t="00:11:03">[00:11:03]</a>. Therefore, the null hypothesis is rejected, and it is concluded that the drug definitely has an effect on response time <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>.