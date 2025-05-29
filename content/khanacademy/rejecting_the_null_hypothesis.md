---
title: Rejecting the null hypothesis
videoId: -FtlH4svqx4
---

From: [[khanacademy]] <br/> 

[[Hypothesis testing | Hypothesis testing]] is a statistical method used to determine if there is enough evidence in a sample data to infer that a certain condition is true for the entire population. A key component of this process involves the [[null_and_alternative_hypotheses | null and alternative hypotheses]].

## Setting up the Hypotheses

When conducting a statistical test, two main hypotheses are established:

### The Null Hypothesis ($H_0$)
The null hypothesis represents the status quo or the assumption that there is no effect or no difference <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>. It's the hypothesis that researchers try to disprove or reject.

In the example of a neurologist testing a drug's effect on rat response times:
*   The mean response time for rats not injected with the drug is known to be 1.2 seconds <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.
*   The [[null_and_alternative_hypotheses | null hypothesis]] ($H_0$) would state that the drug has no effect on response time <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.
*   This can be represented as: The mean response time for rats taking the drug is still 1.2 seconds ($ \mu = 1.2s $) <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>.

### The Alternative Hypothesis ($H_A$ or $H_1$)
The alternative hypothesis is what the researcher is trying to prove <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. It suggests that there *is* an effect or a difference.

For the drug study example:
*   The [[null_and_alternative_hypotheses | alternative hypothesis]] ($H_A$) would state that the drug *does* have an effect on response time <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.
*   This means the mean response time is not equal to 1.2 seconds when the drug is given ($ \mu \neq 1.2s $) <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.

## The Decision-Making Process

To determine whether to accept the alternative hypothesis or default to the null hypothesis, the following approach is generally taken in science <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>:

1.  **Assume the Null Hypothesis is True:** The first step is to assume that the null hypothesis is correct <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.
2.  **Calculate Probability of Observed Results:** Under this assumption, determine the probability of obtaining the observed sample results (or results even more extreme) <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.
3.  **Decision:** If this probability is very small, it suggests that the initial assumption (the null hypothesis) is likely incorrect, and thus the null hypothesis can be rejected in favor of the alternative hypothesis <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.

## Applying the Method to the Drug Study

A sample of 100 injected rats had a mean response time of 1.05 seconds with a sample standard deviation of 0.5 seconds <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

### Sampling Distribution under Null Hypothesis
If the null hypothesis is true (i.e., the drug has no effect and the mean is still 1.2 seconds), the sampling distribution of sample means would be:
*   **Mean ($ \mu $):** 1.2 seconds (same as the population mean) <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.
*   **Standard Deviation of the Sampling Distribution ($ \sigma_{\bar{x}} $):** This is calculated by dividing the population standard deviation ($ \sigma $) by the square root of the sample size ($ \sqrt{n} $) <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>. Since the population standard deviation is unknown, it's estimated using the sample standard deviation (s) <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.
    $ \sigma_{\bar{x}} \approx \frac{s}{\sqrt{n}} $ <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>
    $ \sigma_{\bar{x}} \approx \frac{0.5}{ \sqrt{100} } = \frac{0.5}{10} = 0.05 $ seconds <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>

### [[calculating_zscores_and_pvalues | Calculating Z-scores and P-values]]
To determine how extreme the observed sample mean (1.05 seconds) is, a Z-score is calculated <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>:
$ Z = \frac{\text{Sample Mean} - \text{Population Mean (under } H_0 \text{)}}{\text{Standard Deviation of Sampling Distribution}} $ <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>
$ Z = \frac{1.05 - 1.2}{0.05} = \frac{-0.15}{0.05} = -3 $ <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>

This means the observed sample mean of 1.05 seconds is 3 standard deviations below the assumed population mean of 1.2 seconds <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a>.

The next step is to find the probability of getting a result *this extreme* or *more extreme* in either direction (meaning 3 standard deviations or more away from the mean). This probability is known as the **P-value** <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>.

*   According to the empirical rule, approximately 99.7% of data falls within 3 standard deviations of the mean in a normal distribution <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>.
*   Therefore, the area outside of 3 standard deviations (in both tails) is $100\% - 99.7\% = 0.3\%$ <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>.
*   As a decimal, the P-value is 0.003 <a class="yt-timestamp" data-t="00:10:45">[00:10:45]</a>.

## Conclusion: Rejecting the Null Hypothesis

The P-value of 0.003 means that if the drug truly had no effect (i.e., the null hypothesis was true), there would only be a 0.3% chance of observing a sample mean as extreme as 1.05 seconds or more <a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a>. This is less than 1 in 300 <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>.

Because this probability is very small, it provides strong evidence against the null hypothesis <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.

> [!tip] Significance Level
> In [[inferential_statistics | inferential statistics]], a common threshold for rejecting the null hypothesis is a P-value less than 5% (0.05) <a class="yt-timestamp" data-t="00:11:03">[00:11:03]</a>. If the P-value is below this threshold, the result is considered statistically significant, and the null hypothesis is rejected.

In this case, a P-value of 0.003 is much less than 0.05, indicating a very strong reason to reject the null hypothesis <a class="yt-timestamp" data-t="00:11:14">[00:11:14]</a>. Thus, it is concluded that the drug definitely has some effect on response time <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a>.