---
title: Calculating and interpreting pvalues
videoId: -FtlH4svqx4
---

From: [[khanacademy]] <br/> 

The P-value is a crucial concept in [[inferential_statistics | inferential statistics]], particularly in hypothesis testing, which helps determine the statistical significance of observed results. It represents the [[probability_calculation | probability]] of obtaining results as extreme as, or more extreme than, the observed results, assuming the [[understanding_null_and_alternative_hypotheses | null hypothesis]] is true <a class="yt-timestamp" data-t="02:32:00">[02:32:00]</a>.

## Scenario: Drug Effect on Response Time

Consider a neurologist testing a drug's effect on response time <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>.
*   **Known Population Mean:** The mean response time for rats *not* injected with the drug is 1.2 seconds <a class="yt-timestamp" data-t="00:13:00">[00:13:00]</a>.
*   **Sample Data:** 100 rats were injected with the drug, yielding a sample mean response time of 1.05 seconds and a sample standard deviation of 0.5 seconds <a class="yt-timestamp" data-t="00:21:00">[00:21:00]</a>.
*   **Question:** Does the drug have an effect on response time <a class="yt-timestamp" data-t="00:31:00">[00:31:00]</a>?

## Setting Up Hypotheses

To address this question, two hypotheses are established <a class="yt-timestamp" data-t="00:36:00">[00:36:00]</a>:

### [[understanding_null_and_alternative_hypotheses | Null Hypothesis]] (H₀)
The [[understanding_null_and_alternative_hypotheses | null hypothesis]] assumes no effect or "status quo" <a class="yt-timestamp" data-t="00:50:00">[00:50:00]</a>.
*   **H₀:** The drug has no effect on response time <a class="yt-timestamp" data-t="00:44:00">[00:44:00]</a>.
*   This implies that the mean response time for rats with the drug is still 1.2 seconds (μ = 1.2 seconds) <a class="yt-timestamp" data-t="01:11:00">[01:11:00]</a>.

### Alternative Hypothesis (Hₐ)
The alternative hypothesis proposes that there *is* an effect <a class="yt-timestamp" data-t="01:38:00">[01:38:00]</a>.
*   **Hₐ:** The drug has an effect on response time <a class="yt-timestamp" data-t="01:52:00">[01:52:00]</a>.
*   This means the mean response time with the drug is not equal to 1.2 seconds (μ ≠ 1.2 seconds) <a class="yt-timestamp" data-t="01:56:00">[01:56:00]</a>.

## Approach to Hypothesis Testing

The standard approach to determine whether to accept the alternative hypothesis is to assume the [[understanding_null_and_alternative_hypotheses | null hypothesis]] is true and then calculate the [[probability_calculation | probability]] of observing the sample results (or more extreme) <a class="yt-timestamp" data-t="02:27:00">[02:27:00]</a>. If this [[probability_calculation | probability]] is very small, it suggests the [[understanding_null_and_alternative_hypotheses | null hypothesis]] is likely false, leading to its rejection in favor of the alternative hypothesis <a class="yt-timestamp" data-t="02:39:00">[02:39:00]</a>.

## Calculating the P-value

### 1. Sampling Distribution Characteristics (Under H₀)

Assuming the [[understanding_null_and_alternative_hypotheses | null hypothesis]] is true:
*   **Mean of the Sampling Distribution (μₓ̄):** This would be equal to the population mean, 1.2 seconds <a class="yt-timestamp" data-t="03:52:00">[03:52:00]</a>.
*   **Standard Deviation of the Sampling Distribution (Standard Error, σₓ̄):** This is calculated as the population standard deviation (σ) divided by the square root of the sample size (n) <a class="yt-timestamp" data-t="04:13:00">[04:13:00]</a>.
    *   Since the population standard deviation is unknown, the sample standard deviation (s = 0.5 seconds) is used as an estimate, which is reasonable for a large sample size (n=100) <a class="yt-timestamp" data-t="04:31:00">[04:31:00]</a>.
    *   σₓ̄ ≈ s / √n = 0.5 / √100 = 0.5 / 10 = 0.05 <a class="yt-timestamp" data-t="04:48:00">[04:48:00]</a>.

### 2. Calculate the Z-score

The [[zscore_and_probability_in_hypothesis_testing | Z-score]] measures how many standard deviations the sample mean (1.05 seconds) is away from the hypothesized population mean (1.2 seconds) <a class="yt-timestamp" data-t="05:54:00">[05:54:00]</a>.

*   **Z-score Formula:** Z = (Observed Sample Mean - Hypothesized Population Mean) / Standard Error <a class="yt-timestamp" data-t="06:15:00">[06:15:00]</a>
*   **Calculation:** Z = (1.05 - 1.2) / 0.05 = -0.15 / 0.05 = -3 <a class="yt-timestamp" data-t="07:00:00">[07:00:00]</a>.
    *   This means the observed sample mean of 1.05 seconds is 3 standard deviations below the hypothesized population mean of 1.2 seconds <a class="yt-timestamp" data-t="07:15:00">[07:15:00]</a>.

### 3. Determine the P-value

The P-value is the [[probability_calculation | probability]] of getting a result as extreme as or more extreme than the observed Z-score (-3), in *both* tails of the distribution <a class="yt-timestamp" data-t="08:05:00">[08:05:00]</a>. This means considering results ≤ -3 standard deviations and results ≥ +3 standard deviations.

*   From the empirical rule, approximately 99.7% of data falls within 3 standard deviations of the mean in a normal distribution <a class="yt-timestamp" data-t="08:30:00">[08:30:00]</a>.
*   Therefore, the remaining 0.3% of the [[probability_calculation | probability]] is distributed in the two tails <a class="yt-timestamp" data-t="09:01:00">[09:01:00]</a>.
*   **P-value = 0.3% or 0.003** <a class="yt-timestamp" data-t="09:13:00">[09:13:00]</a>.

## Interpretation and Decision

A P-value of 0.003 means that if the drug truly had no effect (i.e., the [[understanding_null_and_alternative_hypotheses | null hypothesis]] was true), there would only be a 0.3% (less than 1 in 300) chance of observing a sample mean as extreme as 1.05 seconds <a class="yt-timestamp" data-t="09:33:00">[09:33:00]</a>.

*   **Decision Rule:** Typically, a P-value less than a pre-defined significance level (e.g., 0.05 or 5%) leads to rejecting the [[understanding_null_and_alternative_hypotheses | null hypothesis]] <a class="yt-timestamp" data-t="11:00:00">[11:00:00]</a>.
*   **Conclusion:** Since 0.003 is much less than 0.05, the [[understanding_null_and_alternative_hypotheses | null hypothesis]] is rejected <a class="yt-timestamp" data-t="09:56:00">[09:56:00]</a>. This provides strong evidence to support the alternative hypothesis that the drug does have an effect on response time <a class="yt-timestamp" data-t="11:16:00">[11:16:00]</a>.