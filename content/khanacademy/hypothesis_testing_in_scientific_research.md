---
title: Hypothesis testing in scientific research
videoId: -FtlH4svqx4
---

From: [[khanacademy]] <br/> 

Hypothesis testing is a fundamental statistical method used in scientific research to determine whether the results of a study are statistically significant or occurred merely by chance <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>. It involves setting up two opposing hypotheses and using data to decide which one is more likely to be true <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>.

## Setting Up Hypotheses

The process begins by formulating two key hypotheses:

### The Null Hypothesis (H0)
The [[understanding_null_and_alternative_hypotheses | null hypothesis]] (H0) represents the status quo or the assumption that there is no effect or no difference <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>. It assumes that whatever is being researched has no effect <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.

*   **Example:** In a study testing a drug's effect on rat response time, the [[understanding_null_and_alternative_hypotheses | null hypothesis]] would state that the drug has no effect on response time <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>. This means the mean response time for rats given the drug would still be 1.2 seconds, which is the known mean for rats not injected with the drug <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>.

### The Alternative Hypothesis (H1)
The [[understanding_null_and_alternative_hypotheses | alternative hypothesis]] (H1) is what the researcher aims to prove or suggests that there *is* an effect or a significant difference <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.

*   **Example:** For the drug study, the [[understanding_null_and_alternative_hypotheses | alternative hypothesis]] would state that the drug *does* have an effect on response time <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>, meaning the mean response time is not equal to 1.2 seconds when the drug is given <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.

## The Experiment and Data Collection

Consider a neurologist testing a drug on the response time of rats <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>.
*   **Known Information:** The mean response time for rats *not* injected with the drug is 1.2 seconds <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.
*   **Experiment:** 100 rats are injected with a unit dose of the drug, subjected to neurological stimulus, and their response times are recorded <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>.
*   **Results:** The mean response time for the 100 injected rats is 1.05 seconds, with a sample standard deviation of 0.5 seconds <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

The question is whether this observed difference (1.05 seconds vs. 1.2 seconds) is due to the drug or simply random variation <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.

## The Core Principle: Assuming the Null Hypothesis is True

To evaluate the data, researchers assume that the [[understanding_null_and_alternative_hypotheses | null hypothesis]] is true <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>. Then, they calculate the probability of obtaining the observed results (or results even more extreme) if this assumption were correct <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>. If this probability is very small, it suggests the [[understanding_null_and_alternative_hypotheses | null hypothesis]] is likely false, and the alternative hypothesis might be true <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.

### Sampling Distribution Under the Null Hypothesis
If the [[understanding_null_and_alternative_hypotheses | null hypothesis]] (drug has no effect) is true, then the mean of the sampling distribution of response times would be 1.2 seconds <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.
*   The standard deviation of the sampling distribution (also known as the standard error of the mean) is calculated by dividing the population standard deviation by the square root of the sample size <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.
*   Since the population standard deviation is unknown, it is estimated using the sample standard deviation (0.5 seconds) <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>. With a sample size of 100, this is a reasonable approximation <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>.
*   Estimated standard deviation of the sampling distribution: $0.5 / \sqrt{100} = 0.5 / 10 = 0.05$ seconds <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.

### Calculating the Z-score
To determine how unusual the observed sample mean (1.05 seconds) is, a [[zscore_and_probability_in_hypothesis_testing | Z-score]] is calculated <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>. The [[zscore_and_probability_in_hypothesis_testing | Z-score]] indicates how many standard deviations an observation is away from the mean of the distribution <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.

$Z = \frac{\text{Observed Sample Mean} - \text{Population Mean (under Null Hypothesis)}}{\text{Standard Deviation of Sampling Distribution}}$
$Z = \frac{1.05 - 1.2}{0.05} = \frac{-0.15}{0.05} = -3$ <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>

The observed sample mean of 1.05 seconds is 3 standard deviations below the hypothesized population mean of 1.2 seconds <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.

### Determining the P-value
The next step is to find the [[calculating_and_interpreting_pvalues | P-value]], which is the probability of obtaining a result as extreme as, or more extreme than, the observed result, *assuming the [[understanding_null_and_alternative_hypotheses | null hypothesis]] is true* <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>. "Extreme" here means being 3 standard deviations away from the mean in either the positive or negative direction <a class="yt-timestamp" data-t="00:08:13">[00:08:13]</a>.

Based on the empirical rule for normal distributions:
*   Approximately 99.7% of the data falls within 3 standard deviations of the mean <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>.
*   Therefore, the probability of a result being *outside* 3 standard deviations (i.e., more extreme) is $100\% - 99.7\% = 0.3\%$ <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>.

The [[calculating_and_interpreting_pvalues | P-value]] for this result is 0.003, or 0.3% <a class="yt-timestamp" data-t="00:10:45">[00:10:45]</a>.

## Decision Making

A small [[calculating_and_interpreting_pvalues | P-value]] indicates that the observed result is unlikely if the [[understanding_null_and_alternative_hypotheses | null hypothesis]] were true <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>.

*   In this case, a [[calculating_and_interpreting_pvalues | P-value]] of 0.3% means there's only a 1 in 300 chance of getting such an extreme result if the drug actually had no effect <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>.
*   Because this probability is very small, the [[understanding_null_and_alternative_hypotheses | null hypothesis]] is rejected <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>. This suggests that the alternative hypothesis is favored, meaning the drug *does* have an effect on response time <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>.

### Significance Threshold
Researchers typically use a threshold (often 5% or 0.05) to decide whether to reject the [[understanding_null_and_alternative_hypotheses | null hypothesis]] <a class="yt-timestamp" data-t="00:11:03">[00:11:03]</a>. If the [[calculating_and_interpreting_pvalues | P-value]] is less than this threshold, the result is considered statistically significant, and the [[understanding_null_and_alternative_hypotheses | null hypothesis]] is rejected <a class="yt-timestamp" data-t="00:11:03">[00:11:03]</a>. In this example, 0.3% is much less than 5%, providing a strong indicator that the [[understanding_null_and_alternative_hypotheses | null hypothesis]] is incorrect and the drug has a definite effect <a class="yt-timestamp" data-t="00:11:16">[00:11:16]</a>.

This process is a core component of [[inferential statistics | inferential statistics]], allowing conclusions about a population based on sample data.