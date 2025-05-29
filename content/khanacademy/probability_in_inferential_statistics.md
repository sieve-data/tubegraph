---
title: Probability in inferential statistics
videoId: -FtlH4svqx4
---

From: [[khanacademy]] <br/> 

[[introduction_to_inferential_statistics | Inferential statistics]] often employs probability to evaluate hypotheses and make decisions about populations based on sample data <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>. This process helps determine if observed sample results are likely due to chance or indicate a true effect.

## Hypothesis Testing Framework

A common approach involves setting up two opposing hypotheses:
*   **Null Hypothesis (H₀)**: This represents the status quo or the assumption that there is no effect or no difference <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. For example, if a drug is being tested, the null hypothesis would be that the drug has no effect on response time <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>. This means the mean response time with the drug would be the same as without it (e.g., 1.2 seconds) <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.
*   **Alternative Hypothesis (H₁ or Hₐ)**: This is what the researcher is trying to prove, suggesting that there is an effect or a difference <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>. In the drug example, it would state that the drug *does* have an effect on response time <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>, meaning the mean response time is not equal to 1.2 seconds when the drug is given <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>.

## Using Probability to Make Decisions

The core idea is to assume the null hypothesis is true and then calculate the probability of obtaining the observed sample results (or more extreme results) under that assumption <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>. If this probability is very small, it suggests that the null hypothesis is likely false, leading to its rejection in favor of the alternative hypothesis <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>.

### The Sampling Distribution

To calculate this probability, the concept of a sampling distribution is used <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.
*   Assuming the null hypothesis is true, the mean of the sampling distribution is expected to be the population mean (e.g., 1.2 seconds) <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.
*   The standard deviation of the sampling distribution (also known as the standard error) is calculated as the population standard deviation divided by the square root of the sample size <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>. If the population standard deviation is unknown, it can be estimated using the sample standard deviation, especially for larger sample sizes (e.g., N > 100) <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.

### Z-statistic and Probability Calculation

To determine how extreme a sample result is, a [[use_of_zstatistic_in_inferential_statistics | Z-statistic]] (or Z-score) is calculated <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>. This value indicates how many standard deviations the sample mean is from the hypothesized population mean <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>.

For example, if the hypothesized mean is 1.2 seconds and a sample mean is 1.05 seconds with a sampling distribution standard deviation of 0.05 seconds, the Z-statistic would be:
Z = (1.2 - 1.05) / 0.05 = 0.15 / 0.05 = 3 <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>, <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>, <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a>.
This means the observed sample mean is 3 standard deviations away from the hypothesized mean <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a>.

## The P-value

The "P-value" is the probability of obtaining a test statistic result as extreme as, or more extreme than, the observed result, assuming the null hypothesis is true <a class="yt-timestamp" data-t="00:10:32">[00:10:32]</a>.
*   It quantifies the likelihood of the observed data occurring by random chance under the null hypothesis <a class="yt-timestamp" data-t="00:09:28">[00:09:28]</a>.
*   Using the empirical rule, approximately 99.7% of data in a normal distribution falls within 3 standard deviations of the mean <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>. Therefore, the probability of being *outside* this range (i.e., more extreme than 3 standard deviations in either direction) is 100% - 99.7% = 0.3% <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>.
*   In the example, the P-value for a Z-statistic of 3 is 0.003 (or 0.3%) <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>. This means there's a 0.3% chance of getting a sample mean as extreme as 1.05 seconds (or more extreme in either direction) if the drug truly had no effect <a class="yt-timestamp" data-t="00:09:33">[00:09:33]</a>.

## Conclusion and Decision Making

A small P-value (e.g., P < 0.05 or 5%) indicates that the observed result is unlikely if the null hypothesis were true <a class="yt-timestamp" data-t="00:11:03">[00:11:03]</a>.
*   If the P-value is less than a predetermined significance level (e.g., 0.05), the null hypothesis is rejected <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>. This suggests that the observed effect is statistically significant and likely not due to random chance <a class="yt-timestamp" data-t="00:11:16">[00:11:16]</a>.
*   In the drug example, a P-value of 0.003 (0.3%) is much less than 0.05 (5%), leading to the rejection of the null hypothesis. The conclusion is that the drug likely has an effect on response time <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>.