---
title: Zscore and probability in hypothesis testing
videoId: -FtlH4svqx4
---

From: [[khanacademy]] <br/> 

This article explores how [[Z-score and probability in hypothesis testing | Z-scores]] and probability are utilized in [[hypothesis_testing_in_scientific_research | hypothesis testing]] to determine the effect of a drug on response time.

## Scenario: Neurologist's Drug Test

A neurologist investigates the effect of a drug on the response time of rats.
*   100 rats are injected with a unit dose of the drug <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>.
*   Each rat is subjected to a neurological stimulus, and its response time is recorded <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>.
*   The known mean response time for rats *not* injected with the drug is 1.2 seconds <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.
*   The observed mean response time for the 100 injected rats is 1.05 seconds, with a sample standard deviation of 0.5 seconds <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.
*   The question is whether the drug has an effect on response time <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.

## Formulating Hypotheses

To address this question, two hypotheses are established:

### Null Hypothesis ($H_0$)
The [[understanding_null_and_alternative_hypotheses | null hypothesis]] represents the status quo or the assumption that there is no effect <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.
*   **Statement**: The drug has no effect on response time <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.
*   **Implication**: The mean response time for rats receiving the drug is still 1.2 seconds, consistent with rats not given the drug <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.

### Alternative Hypothesis ($H_A$)
The [[understanding_null_and_alternative_hypotheses | alternative hypothesis]] proposes that an effect exists <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.
*   **Statement**: The drug *does* have an effect on response time <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.
*   **Implication**: The mean response time for rats receiving the drug is *not* equal to 1.2 seconds <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>.

## Hypothesis Testing Strategy

The approach to deciding between the null and alternative hypotheses involves a crucial step:
1.  **Assume the Null Hypothesis is True**: Begin by assuming the drug has no effect <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.
2.  **Calculate Probability of Observed Results**: Determine the probability of obtaining the observed sample results (mean of 1.05 seconds) *if* the null hypothesis were true <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.
3.  **Decision**: If this probability is extremely small, it suggests the null hypothesis is likely false, leading to its rejection in favor of the alternative hypothesis <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.

## Sampling Distribution Under the Null Hypothesis

To calculate the probability, we consider the sampling distribution of sample means, assuming the null hypothesis is true.

*   **Mean of Sampling Distribution**: If the null hypothesis ($H_0$) is true (drug has no effect), the mean of the sampling distribution will be the same as the population mean, which is 1.2 seconds <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.
*   **Standard Deviation of Sampling Distribution (Standard Error)**: This is calculated as the population standard deviation divided by the square root of the sample size ($n$) <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>. Since the population standard deviation is unknown, it is estimated using the sample standard deviation (0.5 seconds) <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>. With a sample size of 100, this is a reasonable approximation <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>.

    $$ \text{Standard Error} (\sigma_{\bar{x}}) \approx \frac{S}{\sqrt{n}} = \frac{0.5}{\sqrt{100}} = \frac{0.5}{10} = 0.05 $$
    So, the estimated standard deviation of the sampling distribution is 0.05 seconds <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.

## Calculating the Z-score (Z-statistic)

To understand how unusual our observed sample mean (1.05 seconds) is, we calculate its [[difference_between_zstatistics_and_tstatistics | Z-score]] (or [[difference_between_zstatistics_and_tstatistics | Z-statistic]]). The [[difference_between_zstatistics_and_tstatistics | Z-score]] measures how many standard deviations an observation is from the mean.

$$ Z = \frac{\bar{x} - \mu}{ \sigma_{\bar{x}} } $$
Where:
*   $\bar{x}$ = observed sample mean (1.05 seconds)
*   $\mu$ = population mean under null hypothesis (1.2 seconds)
*   $\sigma_{\bar{x}}$ = standard error of the sampling distribution (0.05 seconds)

$$ Z = \frac{1.05 - 1.2}{0.05} = \frac{-0.15}{0.05} = -3 $$
The observed sample mean of 1.05 seconds is 3 standard deviations *below* the mean of the sampling distribution (1.2 seconds) <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a>.

## Interpreting the Z-score and P-value

We want to find the probability of getting a result *as extreme or more extreme* than 1.05 seconds. Since the alternative hypothesis states the mean "does not equal" 1.2 seconds, we are interested in extreme values in both directions (a two-tailed test) <a class="yt-timestamp" data-t="00:08:05">[00:08:05]</a>. This means we look at the probability of being 3 standard deviations below the mean *or* 3 standard deviations above the mean.

*   **Empirical Rule**: Based on the empirical rule for normal distributions, approximately 99.7% of data falls within 3 standard deviations of the mean <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>.
*   **Probability of Extremes**: This leaves 100% - 99.7% = 0.3% of the probability distributed in the tails beyond $\pm$3 standard deviations <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>.

This probability (0.3% or 0.003) is known as the [[calculating_and_interpreting_pvalues | P-value]] <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>.
*   The [[calculating_and_interpreting_pvalues | P-value]] represents the probability of observing a result as extreme as, or more extreme than, the one observed, assuming the null hypothesis is true <a class="yt-timestamp" data-t="00:10:32">[00:10:32]</a>.
*   In this case, the [[calculating_and_interpreting_pvalues | P-value]] is 0.003 <a class="yt-timestamp" data-t="00:10:52">[00:10:52]</a>. This means there's only a 0.3% chance (or 1 in 300) of getting a sample mean of 1.05 seconds (or further from 1.2 seconds) if the drug truly had no effect <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>.

## Conclusion and Decision

Given the very small [[calculating_and_interpreting_pvalues | P-value]] (0.003), it is highly unlikely to observe such a result if the null hypothesis were true <a class="yt-timestamp" data-t="00:10:52">[00:10:52]</a>.

*   **Decision**: The null hypothesis is rejected <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>.
*   **Interpretation**: This provides strong evidence to favor the [[understanding_null_and_alternative_hypotheses | alternative hypothesis]], suggesting that the drug *does* have an effect on response time <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>.

Commonly, a [[calculating_and_interpreting_pvalues | P-value]] less than 5% (0.05) is considered a sufficient threshold for rejecting the null hypothesis <a class="yt-timestamp" data-t="00:11:03">[00:11:03]</a>. Since 0.003 is significantly less than 0.05, this is a strong indicator that the drug has an effect <a class="yt-timestamp" data-t="00:11:16">[00:11:16]</a>.