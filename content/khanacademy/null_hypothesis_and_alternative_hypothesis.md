---
title: Null hypothesis and alternative hypothesis
videoId: -FtlH4svqx4
---

From: [[khanacademy]] <br/> 

In statistical hypothesis testing, two main hypotheses are established to determine the effect of a treatment or condition: the null hypothesis and the alternative hypothesis <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. This framework helps researchers decide whether observed data is statistically significant enough to reject a default assumption.

## The Null Hypothesis (H₀)

The null hypothesis is typically viewed as the "status quo" or the default assumption <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>. It posits that whatever is being researched has no effect or that there is no difference between a population parameter and a hypothesized value <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.

### Example Scenario: Drug Effect on Response Time

Consider a neurologist testing a drug's effect on rat response time <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>.
*   The known mean response time for rats not injected with the drug is 1.2 seconds <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.
*   **Null Hypothesis (H₀)**: The drug has no effect on response time <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>. This means that even with the drug, the mean response time for rats would still be 1.2 seconds <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.

## The Alternative Hypothesis (H₁)

The alternative hypothesis is what the researcher is trying to prove or find evidence for <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. It proposes that there *is* an effect or a significant difference.

### Example Scenario: Drug Effect on Response Time

Continuing with the neurologist's study:
*   **Alternative Hypothesis (H₁)**: The drug *does* have an effect on response time <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>. This means that the mean response time when the drug is given does not equal 1.2 seconds <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>.

## The Hypothesis Testing Process

To determine whether to accept the alternative hypothesis or default to the null hypothesis, a standard scientific approach is used <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>:
1.  **Assume the Null Hypothesis is True**: Begin by assuming that the drug has no effect <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.
2.  **Calculate Probability of Observed Results**: Determine the probability of observing the sample data (or more extreme data) *if* the null hypothesis were true <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.
3.  **Decision**: If this probability is very small, it suggests the null hypothesis is likely untrue, leading to its rejection in favor of the alternative hypothesis <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.

### Application: Neurologist's Drug Study

The neurologist injected 100 rats, observing a sample mean response time of 1.05 seconds with a sample standard deviation of 0.5 seconds <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

To assess the probability of this result under the null hypothesis (mean = 1.2 seconds):
1.  **Sampling Distribution**: Assuming the null hypothesis, the sampling distribution of sample means for 100 rats would be a normal distribution with a mean of 1.2 seconds <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.
2.  **Standard Deviation of the Sampling Distribution**: This is estimated using the sample standard deviation (0.5 seconds) divided by the square root of the sample size (100) <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>, resulting in:
    0.5 / √100 = 0.5 / 10 = 0.05 seconds <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
3.  **Calculate [[use_of_zstatistic_in_inferential_statistics | Z-score]]**: The [[use_of_zstatistic_in_inferential_statistics | Z-score]] indicates how many standard deviations the observed sample mean (1.05s) is from the hypothesized population mean (1.2s) <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>.
    [[use_of_zstatistic_in_inferential_statistics | Z-score]] = (Observed Mean - Hypothesized Mean) / Standard Deviation of Sampling Distribution
    [[use_of_zstatistic_in_inferential_statistics | Z-score]] = (1.2 - 1.05) / 0.05 = 0.15 / 0.05 = 3 <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>.
    This means the observed sample mean is 3 standard deviations below the mean <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.

## The [[pvalue_in_hypothesis_testing | P-value]]

The probability of getting a result as extreme as (or more extreme than) the observed sample mean, *assuming the null hypothesis is true*, is known as the [[pvalue_in_hypothesis_testing | P-value]] <a class="yt-timestamp" data-t="00:10:32">[00:10:32]</a>.
*   For a [[use_of_zstatistic_in_inferential_statistics | Z-score]] of 3, the empirical rule states that 99.7% of the data falls within 3 standard deviations of the mean <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>.
*   Therefore, the probability of being *outside* this range (i.e., more than 3 standard deviations away in either direction) is 100% - 99.7% = 0.3% <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>.
*   Expressed as a decimal, the [[pvalue_in_hypothesis_testing | P-value]] is 0.003 <a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a>.

This means there is only a 0.3% chance (less than 1 in 300) of obtaining such an extreme result if the drug truly had no effect <a class="yt-timestamp" data-t="00:09:33">[00:09:33]</a>.

### Conclusion

A small [[pvalue_in_hypothesis_testing | P-value]] (e.g., less than 0.05 or 5%) indicates that the observed data is unlikely to have occurred by chance if the null hypothesis were true <a class="yt-timestamp" data-t="00:11:03">[00:11:03]</a>. In this case, with a [[pvalue_in_hypothesis_testing | P-value]] of 0.003, there is a very strong indication that the null hypothesis is incorrect <a class="yt-timestamp" data-t="00:11:16">[00:11:16]</a>.

> [!INFO] Decision
> Based on the low [[pvalue_in_hypothesis_testing | P-value]], the null hypothesis is rejected <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>. This favors the alternative hypothesis, suggesting the drug *does* have an effect on response time <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>.