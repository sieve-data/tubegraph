---
title: Hypothesis testing
videoId: -FtlH4svqx4
---

From: [[khanacademy]] <br/> 

[[Inferential statistics | Hypothesis testing]] is a statistical method used to make inferences about a population based on sample data <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>. It involves setting up two competing hypotheses and then using evidence from a sample to decide which hypothesis is more likely to be true <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.

## Case Study: Drug Effect on Response Time

Consider an experiment where a neurologist tests the effect of a drug on the response time of rats <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>.
*   The mean response time for rats *not* injected with the drug is known to be 1.2 seconds <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.
*   100 rats are injected with a unit dose of the drug <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>.
*   The mean response time for these 100 injected rats is 1.05 seconds <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>, with a sample standard deviation of 0.5 seconds <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.

The question is: Does the drug have an effect on response time <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>?

## Setting Up Hypotheses

To answer this question, two hypotheses are established <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>:

### [[null_and_alternative_hypotheses | Null Hypothesis]] ($H_0$)
The [[null_and_alternative_hypotheses | null hypothesis]] represents the status quo or the assumption that there is no effect or no difference <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.
*   **Statement**: The drug has no effect on response time <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.
*   **Statistical form**: The mean response time for rats with the drug ($\mu_{\text{drug}}$) is still 1.2 seconds ($\mu_{\text{drug}} = 1.2$ seconds) <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.

### [[null_and_alternative_hypotheses | Alternative Hypothesis]] ($H_A$)
The [[null_and_alternative_hypotheses | alternative hypothesis]] is what the researcher is trying to prove or suggests that there is an effect or a difference <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.
*   **Statement**: The drug has an effect on response time <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.
*   **Statistical form**: The mean response time for rats with the drug ($\mu_{\text{drug}}$) does *not* equal 1.2 seconds ($\mu_{\text{drug}} \neq 1.2$ seconds) <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>.

## The Hypothesis Testing Process

The general approach to [[inferential_statistics | hypothesis testing]] is as follows:
1.  **Assume the [[null_and_alternative_hypotheses | null hypothesis]] is true** <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.
2.  **Calculate the probability** of observing the obtained sample results (or more extreme results) *if* the [[null_and_alternative_hypotheses | null hypothesis]] were true <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.
3.  **Make a decision**: If this probability is very small, it suggests the observed results are unlikely under the [[null_and_alternative_hypotheses | null hypothesis]], leading to [[rejecting_the_null_hypothesis | rejecting the null hypothesis]] in favor of the alternative <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>. If the probability is not small enough, the data isn't convincing enough to [[rejecting_the_null_hypothesis | reject the null hypothesis]] <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.

### Modeling the Sampling Distribution

Assuming the [[null_and_alternative_hypotheses | null hypothesis]] is true, we can model the sampling distribution of sample means <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>:
*   **Shape**: Since the sample size (100 rats) is large, the sampling distribution will be approximately a normal distribution <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.
*   **Mean**: If the drug has no effect (as per the [[null_and_alternative_hypotheses | null hypothesis]]), the mean of the sampling distribution will be the same as the population mean, which is 1.2 seconds <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.
*   **Standard Deviation (Standard Error)**: The standard deviation of the sampling distribution (also called the standard error) is calculated as the population standard deviation divided by the square root of the sample size <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.
    *   Since the population standard deviation is unknown, it is estimated using the sample standard deviation (0.5 seconds) <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>. This is a reasonable approximation for a sample size greater than 100 <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>.
    *   Estimated standard error ($\hat{\sigma}_{\bar{x}}$) = (Sample Standard Deviation) / $\sqrt{\text{Sample Size}}$ <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>
    *   $\hat{\sigma}_{\bar{x}}$ = 0.5 / $\sqrt{100}$ = 0.5 / 10 = 0.05 seconds <a class="yt-timestamp" data-t="00:04:58">[00:04:58]</a>.

### [[calculating_zscores_and_pvalues | Calculating Z-scores and P-values]]

To determine how extreme the observed sample mean (1.05 seconds) is, we calculate its [[calculating_zscores_and_pvalues | Z-score]] relative to the sampling distribution assumed under the [[null_and_alternative_hypotheses | null hypothesis]] <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>.
*   **[[calculating_zscores_and_pvalues | Z-score]] formula**: Z = (Observed Sample Mean - Hypothesized Population Mean) / Standard Error <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>
*   **Calculation**: Z = (1.05 - 1.2) / 0.05 = -0.15 / 0.05 = -3 <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>.

This means the observed sample mean of 1.05 seconds is 3 standard deviations below the hypothesized mean of 1.2 seconds <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a>.

The next step is to find the [[calculating_zscores_and_pvalues | P-value]] <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>. The [[calculating_zscores_and_pvalues | P-value]] is the probability of obtaining a result as extreme as, or more extreme than, the observed sample mean, assuming the [[null_and_alternative_hypotheses | null hypothesis]] is true <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>.
*   "More extreme" in this two-tailed test (since the [[null_and_alternative_hypotheses | alternative hypothesis]] was "not equal") means being 3 standard deviations below the mean *or* 3 standard deviations above the mean <a class="yt-timestamp" data-t="00:08:05">[00:08:05]</a>.
*   According to the empirical rule, approximately 99.7% of data in a normal distribution falls within 3 standard deviations of the mean <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>.
*   Therefore, the probability of being *outside* 3 standard deviations (in either direction) is 100% - 99.7% = 0.3% <a class="yt-timestamp" data-t="00:08:56">[00:08:56]</a>.
*   The [[calculating_zscores_and_pvalues | P-value]] = 0.003 <a class="yt-timestamp" data-t="00:09:13">[00:09:13]</a>.

## Conclusion

The [[calculating_zscores_and_pvalues | P-value]] of 0.003 means that if the drug truly had no effect (i.e., if the [[null_and_alternative_hypotheses | null hypothesis]] were true), there would only be a 0.3% chance of observing a sample mean as extreme as 1.05 seconds (or more extreme) <a class="yt-timestamp" data-t="00:09:33">[00:09:33]</a>. This is less than 1 in 300 <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>.

Commonly, a threshold (significance level, or alpha ($\alpha$)) is set, often at 5% (or 0.05) <a class="yt-timestamp" data-t="00:11:03">[00:11:03]</a>. If the [[calculating_zscores_and_pvalues | P-value]] is less than this threshold, the [[null_and_alternative_hypotheses | null hypothesis]] is [[rejecting_the_null_hypothesis | rejected]] <a class="yt-timestamp" data-t="00:11:03">[00:11:03]</a>.

Since the calculated [[calculating_zscores_and_pvalues | P-value]] (0.003) is much less than 0.05, it provides strong evidence to [[rejecting_the_null_hypothesis | reject the null hypothesis]] <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>.

> [!Conclusion]
> Based on the data, it is concluded that the drug definitely has some effect on response time <a class="yt-timestamp" data-t="00:11:16">[00:11:16]</a>.