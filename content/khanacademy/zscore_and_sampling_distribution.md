---
title: Zscore and sampling distribution
videoId: -FtlH4svqx4
---

From: [[khanacademy]] <br/> 

In hypothesis testing, the [[use_of_zstatistic_in_inferential_statistics | Z-statistic]] and understanding the [[sampling_and_sample_means | sampling distribution]] are crucial for determining the likelihood of observed results under a given assumption, such as the null hypothesis <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.

## Scenario: Drug Effect on Response Time

Consider an experiment where a neurologist tests a drug's effect on rat response time <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>.
*   The known [[mean_and_standard_deviation_in_hypothesis_testing | mean]] response time for rats *not* injected with the drug (the [[population_versus_sample_in_statistics | population]] [[mean_and_standard_deviation_in_hypothesis_testing | mean]]) is 1.2 seconds <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.
*   A [[sampling_and_sample_means | sample]] of 100 injected rats yielded a [[mean_and_standard_deviation_in_hypothesis_testing | mean]] response time of 1.05 seconds <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.
*   The [[sample_space_and_possible_outcomes | sample]] [[mean_and_standard_deviation_in_hypothesis_testing | standard deviation]] for these 100 rats was 0.5 seconds <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>.

The question is whether the drug has an effect on response time <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.

## Setting Up Hypotheses

To answer this, two hypotheses are established:

1.  **Null Hypothesis (H₀)**: The drug has no effect on response time <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.
    *   This represents the "status quo" or the assumption that whatever is being researched has no effect <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.
    *   In this context, it implies that the [[mean_and_standard_deviation_in_hypothesis_testing | mean]] response time for rats given the drug is still 1.2 seconds <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>.
2.  **Alternative Hypothesis (H₁)**: The drug *does* have an effect <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.
    *   This implies that the [[mean_and_standard_deviation_in_hypothesis_testing | mean]] response time when the drug is given does *not* equal 1.2 seconds <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.

## Methodology: Assuming the Null Hypothesis is True

The standard approach in science is to assume the null hypothesis is true and then calculate the probability of obtaining the observed [[sampling_and_sample_means | sample]] results (or more extreme results) under that assumption <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>, <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>. If this probability is very small, it suggests the null hypothesis is likely false, and the alternative hypothesis might be true <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.

## The Sampling Distribution

Assuming the null hypothesis is true:
*   The [[sampling_and_sample_means | sampling distribution]] of [[sampling_and_sample_means | sample means]] will be a normal distribution due to the large [[implications_of_sample_size_on_statistical_distribution | sample size]] (100 rats) <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>, <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>.
*   The [[mean_and_standard_deviation_in_hypothesis_testing | mean]] of this [[sampling_and_sample_means | sampling distribution]] will be the same as the [[population_versus_sample_in_statistics | population]] [[mean_and_standard_deviation_in_hypothesis_testing | mean]] (1.2 seconds) <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>, <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>.
*   The [[mean_and_standard_deviation_in_hypothesis_testing | standard deviation]] of the [[sampling_and_sample_means | sampling distribution]] (also known as the standard error) is calculated as the [[mean_and_standard_deviation_in_hypothesis_testing | population]] [[mean_and_standard_deviation_in_hypothesis_testing | standard deviation]] divided by the square root of the [[implications_of_sample_size_on_statistical_distribution | sample size]] <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.

Since the [[mean_and_standard_deviation_in_hypothesis_testing | population]] [[mean_and_standard_deviation_in_hypothesis_testing | standard deviation]] is unknown, the [[sample_space_and_possible_outcomes | sample]] [[mean_and_standard_deviation_in_hypothesis_testing | standard deviation]] (0.5 seconds) is used as an estimate, which is reasonable given the large [[implications_of_sample_size_on_statistical_distribution | sample size]] <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>, <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>.

The estimated standard error is:
Standard Error ≈ Sample Standard Deviation / sqrt(Sample Size) <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>
= 0.5 / sqrt(100) <a class="yt-timestamp" data-t="00:04:58">[00:04:58]</a>
= 0.5 / 10 <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>
= 0.05 <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>

## Calculating the Z-score

To determine how extreme the observed [[sample_space_and_possible_outcomes | sample]] [[mean_and_standard_deviation_in_hypothesis_testing | mean]] (1.05 seconds) is, a [[calculating_probability_using_zscore | Z-score]] (or [[use_of_zstatistic_in_inferential_statistics | Z-statistic]]) is calculated <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>:

$Z = \frac{\text{Sample Mean} - \text{Population Mean (under H₀)}}{\text{Standard Error of Sampling Distribution}}$ <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>

$Z = \frac{1.05 - 1.2}{0.05} = \frac{-0.15}{0.05} = -3$ <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>, <a class="yt-timestamp" data-t="00:06:52">[00:06:52]</a>, <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>, <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>

This means the observed [[sample_space_and_possible_outcomes | sample]] [[mean_and_standard_deviation_in_hypothesis_testing | mean]] of 1.05 seconds is 3 [[mean_and_standard_deviation_in_hypothesis_testing | standard deviations]] *below* the [[mean_and_standard_deviation_in_hypothesis_testing | mean]] of the [[sampling_and_sample_means | sampling distribution]] (1.2 seconds) <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a>, <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.

## Determining Probability (P-value)

The next step is to find the probability of getting a result at least as extreme as -3 [[mean_and_standard_deviation_in_hypothesis_testing | standard deviations]] from the [[mean_and_standard_deviation_in_hypothesis_testing | mean]] in either direction (i.e., less than -3 or greater than +3) <a class="yt-timestamp" data-t="00:08:05">[00:08:05]</a>. This probability is known as the **P-value** <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>.

Using the empirical rule for a normal distribution:
*   Approximately 99.7% of the data falls within 3 [[mean_and_standard_deviation_in_hypothesis_testing | standard deviations]] of the [[mean_and_standard_deviation_in_hypothesis_testing | mean]] <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>, <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>.
*   Therefore, the remaining 0.3% of the probability is distributed in the tails beyond ±3 [[mean_and_standard_deviation_in_hypothesis_testing | standard deviations]] <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>.

The P-value in this case is 0.003 or 0.3% <a class="yt-timestamp" data-t="00:10:45">[00:10:45]</a>, <a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a>.

## Conclusion

If the null hypothesis (that the drug has no effect) were true, there would only be a 0.3% chance (less than 1 in 300) of observing a [[sample_space_and_possible_outcomes | sample]] [[mean_and_standard_deviation_in_hypothesis_testing | mean]] as extreme as 1.05 seconds <a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a>, <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>.

Because this P-value is very small (much less than a common threshold of 5% or 0.05) <a class="yt-timestamp" data-t="00:11:03">[00:11:03]</a>, the null hypothesis can be rejected <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>, <a class="yt-timestamp" data-t="00:10:59">[00:10:59]</a>. This provides strong evidence to favor the alternative hypothesis: the drug likely has an effect on response time <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>, <a class="yt-timestamp" data-t="00:11:16">[00:11:16]</a>.

```ad-seealso
For related statistical concepts, see:
*   [[calculating_probability_using_zscore | Calculating probability using Z-score]]
*   [[use_of_zstatistic_in_inferential_statistics | Use of Z-statistic in inferential statistics]]
*   [[implications_of_sample_size_on_statistical_distribution | Implications of sample size on statistical distribution]]
*   [[sampling_and_sample_means | Sampling and sample means]]
*   [[use_of_tstatistic_for_small_sample_sizes | Use of T-statistic for small sample sizes]]
*   [[mean_and_standard_deviation_in_hypothesis_testing | Mean and standard deviation in hypothesis testing]]
*   [[difference_between_zstatistic_and_tstatistic | Difference between Z-statistic and T-statistic]]
*   [[population_versus_sample_in_statistics | Population versus sample in statistics]]
*   [[sample_space_and_possible_outcomes | Sample space and possible outcomes]]
```