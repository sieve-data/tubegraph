---
title: Mean and standard deviation in hypothesis testing
videoId: -FtlH4svqx4
---

From: [[khanacademy]] <br/> 

[[mean_and_central_tendency | Mean]] and [[standard_deviation | standard deviation]] are fundamental concepts in hypothesis testing, used to evaluate whether observed sample data provides sufficient evidence to reject a [[null_hypothesis_and_alternative_hypothesis | null hypothesis]]. This process involves setting up hypotheses, calculating a test statistic (like the [[use_of_zstatistic_in_inferential_statistics | Z-statistic]]), and determining the [[probability_in_inferential_statistics | probability]] of observing the sample results if the [[null_hypothesis_and_alternative_hypothesis | null hypothesis]] were true.

## Setting Up Hypotheses

Hypothesis testing begins by formulating two opposing statements about a population parameter, often the [[mean_and_central_tendency | mean]]:

1.  **[[null_hypothesis_and_alternative_hypothesis | Null Hypothesis]] (H₀)**: This represents the status quo or the assumption that there is no effect or no difference <a class="yt-timestamp" data-t="00:52:00">[00:52:00]</a>. For example, if a neurologist is testing a drug, the [[null_hypothesis_and_alternative_hypothesis | null hypothesis]] would state that the drug has no effect on response time <a class="yt-timestamp" data-t="00:47:00">[00:47:00]</a>. This implies that the [[mean_and_central_tendency | mean]] response time for rats taking the drug would still be 1.2 seconds, which is the known [[mean_and_central_tendency | mean]] for rats not injected with the drug <a class="yt-timestamp" data-t="01:24:00">[01:24:00]</a>.
2.  **[[null_hypothesis_and_alternative_hypothesis | Alternative Hypothesis]] (H₁ or Hₐ)**: This is what the researcher aims to prove, suggesting that there *is* an effect or a difference <a class="yt-timestamp" data-t="01:40:00">[01:40:00]</a>. In the drug example, the [[null_hypothesis_and_alternative_hypothesis | alternative hypothesis]] would state that the drug *does* have an effect on response time <a class="yt-timestamp" data-t="01:52:00">[01:52:00]</a>, meaning the population [[mean_and_central_tendency | mean]] response time when the drug is given does not equal 1.2 seconds <a class="yt-timestamp" data-t="02:01:00">[02:01:00]</a>.

## The Role of Mean and Standard Deviation in Hypothesis Testing

To determine whether to accept the [[null_hypothesis_and_alternative_hypothesis | alternative hypothesis]] or default to the [[null_hypothesis_and_alternative_hypothesis | null hypothesis]], the standard approach is to assume the [[null_hypothesis_and_alternative_hypothesis | null hypothesis]] is true and then calculate the [[probability_in_inferential_statistics | probability]] of obtaining the observed sample results <a class="yt-timestamp" data-t="02:37:00">[02:37:00]</a>. If this [[probability_in_inferential_statistics | probability]] is very small, it suggests the [[null_hypothesis_and_alternative_hypothesis | null hypothesis]] is likely not true <a class="yt-timestamp" data-t="02:43:00">[02:43:00]</a>.

Consider an experiment where 100 rats injected with a drug have a sample [[mean_and_central_tendency | mean]] response time of 1.05 seconds and a sample [[standard_deviation | standard deviation]] of 0.5 seconds <a class="yt-timestamp" data-t="00:28:00">[00:28:00]</a>. The known [[mean_and_central_tendency | mean]] response time for rats not injected is 1.2 seconds <a class="yt-timestamp" data-t="00:17:00">[00:17:00]</a>.

### Sampling Distribution

Assuming the [[null_hypothesis_and_alternative_hypothesis | null hypothesis]] is true (i.e., the drug has no effect), the [[Zscore and sampling distribution | sampling distribution]] of sample means will be a normal distribution <a class="yt-timestamp" data-t="03:40:00">[03:40:00]</a>.

*   **Mean of the [[Zscore and sampling distribution | Sampling Distribution]]**: If the [[null_hypothesis_and_alternative_hypothesis | null hypothesis]] is true, the [[mean_and_central_tendency | mean]] of the [[Zscore and sampling distribution | sampling distribution]] will be the same as the population [[mean_and_central_tendency | mean]] under the [[null_hypothesis_and_alternative_hypothesis | null hypothesis]], which is 1.2 seconds <a class="yt-timestamp" data-t="04:04:00">[04:04:00]</a>.
*   **Standard Deviation of the [[Zscore and sampling distribution | Sampling Distribution]] (Standard Error)**: The [[standard_deviation | standard deviation]] of the [[Zscore and sampling distribution | sampling distribution]] (also known as the standard error of the mean) is calculated by dividing the population [[standard_deviation | standard deviation]] by the square root of the sample size <a class="yt-timestamp" data-t="04:24:00">[04:24:00]</a>. Since the population [[standard_deviation | standard deviation]] is often unknown, it is estimated using the sample [[standard_deviation | standard deviation]] (0.5 seconds) <a class="yt-timestamp" data-t="04:35:00">[04:35:00]</a>. Given a large sample size (100 in this case), this is a reasonable approximation <a class="yt-timestamp" data-t="04:37:00">[04:37:00]</a>.
    *   Estimated Standard Error = Sample [[standard_deviation | Standard Deviation]] / √Sample Size <a class="yt-timestamp" data-t="04:50:00">[04:50:00]</a>
    *   = 0.5 / √100 = 0.5 / 10 = 0.05 <a class="yt-timestamp" data-t="05:07:00">[05:07:00]</a>

### Calculating the [[Use of Zstatistic in inferential statistics | Z-Statistic]]

To determine how extreme the observed sample [[mean_and_central_tendency | mean]] (1.05 seconds) is, we calculate a [[use_of_zstatistic_in_inferential_statistics | Z-statistic]] (or Z-score) <a class="yt-timestamp" data-t="06:00:00">[06:00:00]</a>. This statistic measures how many standard deviations the sample [[mean_and_central_tendency | mean]] is away from the hypothesized population [[mean_and_central_tendency | mean]] (under the [[null_hypothesis_and_alternative_hypothesis | null hypothesis]]):

*   [[use_of_zstatistic_in_inferential_statistics | Z-statistic]] = (Sample [[mean_and_central_tendency | Mean]] - Hypothesized Population [[mean_and_central_tendency | Mean]]) / Estimated Standard Error <a class="yt-timestamp" data-t="06:19:00">[06:19:00]</a>
*   = (1.05 - 1.2) / 0.05 <a class="yt-timestamp" data-t="06:52:00">[06:52:00]</a>
*   = -0.15 / 0.05 = -3 <a class="yt-timestamp" data-t="07:15:00">[07:15:00]</a>

A [[use_of_zstatistic_in_inferential_statistics | Z-statistic]] of -3 means the observed sample [[mean_and_central_tendency | mean]] is 3 [[standard_deviation | standard deviations]] below the hypothesized population [[mean_and_central_tendency | mean]] <a class="yt-timestamp" data-t="07:20:00">[07:20:00]</a>.

## Determining the [[Pvalue in hypothesis testing | P-Value]]

The next step is to find the [[probability_in_inferential_statistics | probability]] of getting a result as extreme as, or more extreme than, the observed sample [[mean_and_central_tendency | mean]], assuming the [[null_hypothesis_and_alternative_hypothesis | null hypothesis]] is true <a class="yt-timestamp" data-t="08:03:00">[08:03:00]</a>. This [[probability_in_inferential_statistics | probability]] is known as the [[pvalue in hypothesis testing | P-value]] <a class="yt-timestamp" data-t="10:38:00">[10:38:00]</a>.

For a [[use_of_zstatistic_in_inferential_statistics | Z-statistic]] of -3, and considering both tails of the distribution (since the [[null_hypothesis_and_alternative_hypothesis | alternative hypothesis]] was "not equal to"), the [[probability_in_inferential_statistics | probability]] of being 3 [[standard_deviation | standard deviations]] or more away from the [[mean_and_central_tendency | mean]] (in either direction) is determined:

*   Based on the empirical rule, approximately 99.7% of the data falls within 3 [[standard_deviation | standard deviations]] of the [[mean_and_central_tendency | mean]] in a normal distribution <a class="yt-timestamp" data-t="08:35:00">[08:35:00]</a>.
*   Therefore, the remaining [[probability_in_inferential_statistics | probability]] in the tails is 100% - 99.7% = 0.3% <a class="yt-timestamp" data-t="09:05:00">[09:05:00]</a>.
*   Expressed as a decimal, the [[pvalue in hypothesis testing | P-value]] is 0.003 <a class="yt-timestamp" data-t="09:20:00">[09:20:00]</a>.

### Interpreting the [[Pvalue in hypothesis testing | P-Value]]

A small [[pvalue in hypothesis testing | P-value]] indicates that the observed sample results are unlikely to have occurred by chance if the [[null_hypothesis_and_alternative_hypothesis | null hypothesis]] were true <a class="yt-timestamp" data-t="02:39:00">[02:39:00]</a>.

In this example, a [[pvalue in hypothesis testing | P-value]] of 0.003 (0.3%) means there's only a 1 in 300 chance of getting such an extreme result if the drug truly had no effect <a class="yt-timestamp" data-t="09:44:00">[09:44:00]</a>.

Most researchers use a significance threshold (alpha level), commonly 5% (0.05) <a class="yt-timestamp" data-t="11:03:00">[11:03:00]</a>. If the [[pvalue in hypothesis testing | P-value]] is less than this threshold, the [[null_hypothesis_and_alternative_hypothesis | null hypothesis]] is rejected <a class="yt-timestamp" data-t="11:09:00">[11:09:00]</a>. Since 0.003 is much less than 0.05, the [[null_hypothesis_and_alternative_hypothesis | null hypothesis]] is rejected, suggesting strong evidence that the drug does have an effect on response time <a class="yt-timestamp" data-t="11:16:00">[11:16:00]</a>.

> [!NOTE]
> When the sample size is small (typically less than 30), and the population [[standard_deviation | standard deviation]] is unknown, the [[Use of Tstatistic for small sample sizes | T-statistic]] is used instead of the [[use_of_zstatistic_in_inferential_statistics | Z-statistic]].