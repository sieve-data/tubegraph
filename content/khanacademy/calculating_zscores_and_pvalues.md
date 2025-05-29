---
title: Calculating Zscores and Pvalues
videoId: -FtlH4svqx4
---

From: [[khanacademy]] <br/> 

This article explores a statistical method for determining whether an observed effect of a drug on response time is statistically significant, using the concepts of Z-scores and P-values.

## Case Study: Drug Effect on Rat Response Time

A neurologist is testing a drug's effect on response time. Here's the data collected:
*   **Population Mean**: The [[Mean in statistics | mean]] response time for rats *not* injected with the drug is 1.2 seconds <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>, <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.
*   **Sample Data**: 100 rats were injected with the drug <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>.
    *   **Sample Mean**: The [[Mean in statistics | mean]] response time for the 100 injected rats is 1.05 seconds <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.
    *   **Sample [[Calculating standard deviation and probability | Standard Deviation]]**: The sample [[Calculating standard deviation and probability | standard deviation]] is 0.5 seconds <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.

The question is: does the drug affect response time? <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>

## Setting Up Hypotheses

To answer this question, two hypotheses are set up:

### Null Hypothesis ($H_0$)
The null hypothesis represents the status quo or the assumption that there is no effect <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.
*   **Statement**: The drug has no effect on response time <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.
*   **Statistical form**: The [[Mean in statistics | mean]] response time for rats given the drug is still 1.2 seconds (i.e., the same as rats not given the drug) <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>.

### Alternative Hypothesis ($H_1$)
The alternative hypothesis proposes that there *is* an effect <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.
*   **Statement**: The drug has an effect on response time <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.
*   **Statistical form**: The [[Mean in statistics | mean]] response time for rats given the drug is *not equal* to 1.2 seconds <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>.

## The Approach: Assuming the Null Hypothesis

The standard approach in [[Inferential statistics | inferential statistics]] is to assume the null hypothesis is true <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>. Then, calculate the [[Calculating probability of an event | probability]] of obtaining the observed sample results (or something more extreme) *if the null hypothesis were true* <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>. If this [[Calculating probability of an event | probability]] is very small, it suggests the null hypothesis is likely false, and the alternative hypothesis might be true <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>.

### Sampling Distribution Under the Null Hypothesis

If the null hypothesis (drug has no effect) is true, the [[Mean in statistics | mean]] of the sampling distribution of sample [[Mean in statistics | means]] would be 1.2 seconds <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>, <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>. Since the sample size (100 rats) is sufficiently large <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>, the sampling distribution can be approximated as a normal distribution <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.

To find the [[Calculating standard deviation and probability | standard deviation]] of this sampling distribution (also known as the standard error of the mean), we use the formula:
$$ \sigma_{\bar{x}} = \frac{\sigma}{\sqrt{n}} $$
where:
*   $\sigma_{\bar{x}}$ is the [[Calculating standard deviation and probability | standard deviation]] of the sampling distribution.
*   $\sigma$ is the population [[Calculating standard deviation and probability | standard deviation]].
*   $n$ is the sample size.

Since the population [[Calculating standard deviation and probability | standard deviation]] ($\sigma$) is unknown, it is estimated using the sample [[Calculating standard deviation and probability | standard deviation]] (0.5 seconds) <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>. This is a reasonable approximation for a large sample size like 100 <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>.

Estimated standard deviation of the sampling distribution ($\hat{\sigma}_{\bar{x}}$):
$$ \hat{\sigma}_{\bar{x}} = \frac{0.5}{\sqrt{100}} = \frac{0.5}{10} = 0.05 $$ <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>, <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>

## Calculating the Z-score

A [[Difference between Zstatistic and Tstatistic | Z-score]] (or [[Difference between Zstatistic and Tstatistic | Z-statistic]]) measures how many [[Calculating standard deviation and probability | standard deviations]] an observed sample mean is from the hypothesized population [[Mean in statistics | mean]] <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>, <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>.

The formula for the [[Difference between Zstatistic and Tstatistic | Z-statistic]] is:
$$ Z = \frac{\bar{x} - \mu_0}{\hat{\sigma}_{\bar{x}}} $$
where:
*   $\bar{x}$ is the sample [[Mean in statistics | mean]] (1.05 seconds).
*   $\mu_0$ is the hypothesized population [[Mean in statistics | mean]] under the null hypothesis (1.2 seconds).
*   $\hat{\sigma}_{\bar{x}}$ is the estimated [[Calculating standard deviation and probability | standard deviation]] of the sampling distribution (0.05 seconds).

Calculating the [[Difference between Zstatistic and Tstatistic | Z-score]]:
$$ Z = \frac{1.05 - 1.2}{0.05} = \frac{-0.15}{0.05} = -3 $$
The transcript calculates it as `(1.2 - 1.05) / 0.05 = 3` to get a positive distance <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>. This means the observed sample [[Mean in statistics | mean]] of 1.05 seconds is 3 [[Calculating standard deviation and probability | standard deviations]] *below* the hypothesized population [[Mean in statistics | mean]] of 1.2 seconds <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a>, <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.

## Determining the P-value

The [[Calculating probability of an event | P-value]] is the [[Calculating probability of an event | probability]] of getting a result as extreme as, or more extreme than, the observed result, *assuming the null hypothesis is true* <a class="yt-timestamp" data-t="00:10:32">[00:10:32]</a>, <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>. "Extreme" includes results 3 [[Calculating standard deviation and probability | standard deviations]] below the [[Mean in statistics | mean]] *or* 3 [[Calculating standard deviation and probability | standard deviations]] above the [[Mean in statistics | mean]] (a two-tailed test) <a class="yt-timestamp" data-t="00:08:05">[00:08:05]</a>.

Based on the empirical rule for a normal distribution:
*   Approximately 99.7% of data falls within 3 [[Calculating standard deviation and probability | standard deviations]] of the [[Mean in statistics | mean]] <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>, <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>.
*   Therefore, the remaining [[Calculating probability of an event | probability]] (100% - 99.7% = 0.3%) is distributed in the tails beyond $\pm$3 [[Calculating standard deviation and probability | standard deviations]] <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>.

The [[Calculating probability of an event | P-value]] for a Z-score of -3 (or an absolute Z-score of 3) is 0.3% <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>, or 0.003 as a decimal <a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a>, <a class="yt-timestamp" data-t="00:10:45">[00:10:45]</a>.

## Conclusion

The [[Calculating probability of an event | P-value]] of 0.003 means there is only a 0.3% chance (less than 1 in 300) of observing a sample [[Mean in statistics | mean]] as extreme as 1.05 seconds if the drug truly had no effect <a class="yt-timestamp" data-t="00:09:33">[00:09:33]</a>, <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>.

Because this [[Calculating probability of an event | probability]] is very small, we reject the null hypothesis <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>. This suggests that the observed difference is unlikely due to random chance, and the drug likely *does* have an effect on response time <a class="yt-timestamp" data-t="00:11:16">[00:11:16]</a>.

Statistical significance is often determined by comparing the [[Calculating probability of an event | P-value]] to a pre-defined significance level (alpha, $\alpha$). A common threshold is 5% (0.05) <a class="yt-timestamp" data-t="00:11:03">[00:11:03]</a>. Since 0.003 is much less than 0.05, the result is considered statistically significant.