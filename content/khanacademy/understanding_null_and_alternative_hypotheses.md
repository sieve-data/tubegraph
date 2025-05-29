---
title: Understanding null and alternative hypotheses
videoId: -FtlH4svqx4
---

From: [[khanacademy]] <br/> 

[[hypothesis_testing_in_scientific_research | Hypothesis testing]] is a fundamental approach in scientific research used to determine if an observed effect is statistically significant or merely due to chance <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. This process involves setting up two opposing statements about a population: the null hypothesis and the alternative hypothesis <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.

## The Scenario: Drug Effect on Response Time

Consider a neurologist testing a drug's effect on response time <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>.
*   **Population Data (No Drug)**: The mean response time for rats *not* injected with the drug is known to be 1.2 seconds <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.
*   **Sample Data (With Drug)**: 100 rats are injected with a unit dose <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. Their mean response time is 1.05 seconds, with a sample standard deviation of 0.5 seconds <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.
The question is whether the drug has an effect on response time <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.

## Null Hypothesis (H₀)

The null hypothesis represents the status quo or the assumption that there is no effect or no difference <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>. It's often the statement that a researcher aims to disprove.

In the neurologist's experiment:
*   **Statement**: The drug has no effect on response time <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.
*   **Statistical Formulation**: The mean response time for rats taking the drug is still 1.2 seconds <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>, meaning the population mean (μ) equals 1.2 seconds (μ = 1.2) <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>.

## Alternative Hypothesis (H₁)

The alternative hypothesis (sometimes denoted as Hₐ) is what the researcher is trying to prove <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>. It contradicts the null hypothesis, suggesting that there *is* an effect or a difference.

In the neurologist's experiment:
*   **Statement**: The drug has an effect <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.
*   **Statistical Formulation**: The mean response time for rats taking the drug does *not* equal 1.2 seconds (μ ≠ 1.2) <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.

## The Hypothesis Testing Process

The core idea of [[hypothesis_testing_in_scientific_research | hypothesis testing]] is to assume the null hypothesis is true and then calculate the [[zscore_and_probability_in_hypothesis_testing | probability]] of obtaining the observed sample results (or more extreme results) under that assumption <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.

*   **Assumption**: Assume the null hypothesis (H₀) is true <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.
*   **Question**: What is the [[zscore_and_probability_in_hypothesis_testing | probability]] that we would have gotten our sample results (mean of 1.05 seconds, standard deviation of 0.5 seconds from 100 rats) if the true mean was actually 1.2 seconds (i.e., the drug had no effect)? <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>
*   **Decision Rule**: If this [[zscore_and_probability_in_hypothesis_testing | probability]] is very small, it suggests that our initial assumption (the null hypothesis) was likely incorrect. In such cases, we reject the null hypothesis and support the alternative hypothesis <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>.

### Applying the Process to the Drug Experiment

1.  **Sampling Distribution**:
    *   Assuming the null hypothesis is true, the sampling distribution of sample means would be a [[conditions_for_using_normal_distribution_vs_tdistribution | normal distribution]] <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.
    *   Its mean would be 1.2 seconds (the assumed population mean) <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.
    *   The standard deviation of the sampling distribution (standard error) is calculated by dividing the population standard deviation by the square root of the sample size <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>. Since the population standard deviation is unknown, the sample standard deviation (0.5 seconds) is used as an estimate, which is reasonable for a sample size of 100 <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.
    *   Standard error = 0.5 / √100 = 0.5 / 10 = 0.05 seconds <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.

2.  **Calculating the Z-score (Z-statistic)**:
    *   A [[zscore_and_probability_in_hypothesis_testing | Z-score]] measures how many standard deviations an observation is from the mean <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>.
    *   Z-score = (Sample Mean - Population Mean) / Standard Error <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>
    *   Z-score = (1.05 - 1.2) / 0.05 = -0.15 / 0.05 = -3 <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>.
    *   This means the observed sample mean of 1.05 seconds is 3 standard deviations below the assumed population mean of 1.2 seconds <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a>.

3.  **Determining the P-value**:
    *   The [[calculating_and_interpreting_pvalues | P-value]] is the [[zscore_and_probability_in_hypothesis_testing | probability]] of observing a result as extreme as, or more extreme than, the one obtained, assuming the null hypothesis is true <a class="yt-timestamp" data-t="00:10:32">[00:10:32]</a>.
    *   Since the alternative hypothesis is that the mean is *not equal* to 1.2 seconds (two-tailed test), we consider results that are 3 standard deviations away in *either* direction (below or above the mean) <a class="yt-timestamp" data-t="00:08:05">[00:08:05]</a>.
    *   According to the empirical rule, approximately 99.7% of the data in a [[conditions_for_using_normal_distribution_vs_tdistribution | normal distribution]] falls within 3 standard deviations of the mean <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>.
    *   Therefore, the [[zscore_and_probability_in_hypothesis_testing | probability]] of being *outside* this range (i.e., more than 3 standard deviations away) is 100% - 99.7% = 0.3% <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>.
    *   The [[calculating_and_interpreting_pvalues | P-value]] for this experiment is 0.003 (or 0.3%) <a class="yt-timestamp" data-t="00:10:45">[00:10:45]</a>.

4.  **Conclusion**:
    *   A [[calculating_and_interpreting_pvalues | P-value]] of 0.003 means there is only a 0.3% chance (less than 1 in 300) of observing a sample mean as extreme as 1.05 seconds if the drug truly had no effect <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>.
    *   This is a very small [[zscore_and_probability_in_hypothesis_testing | probability]] <a class="yt-timestamp" data-t="00:10:52">[00:10:52]</a>. Given this low [[calculating_and_interpreting_pvalues | P-value]], the null hypothesis (that the drug has no effect) is rejected <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>.
    *   The evidence strongly suggests that the drug *does* have an effect on response time, supporting the alternative hypothesis <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>.

> [!NOTE] P-value Threshold
> In statistical analysis, a common threshold for the [[calculating_and_interpreting_pvalues | P-value]] is 0.05 (or 5%) <a class="yt-timestamp" data-t="00:11:03">[00:11:03]</a>. If the [[calculating_and_interpreting_pvalues | P-value]] is less than this threshold, the null hypothesis is typically rejected. A [[calculating_and_interpreting_pvalues | P-value]] of 0.003 is significantly lower than 0.05, indicating a very strong rejection of the null hypothesis <a class="yt-timestamp" data-t="00:11:14">[00:11:14]</a>.