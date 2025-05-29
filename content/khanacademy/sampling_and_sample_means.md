---
title: Sampling and sample means
videoId: JNm3M9cqWyc
---

From: [[khanacademy]] <br/> 

The concept of sampling and the behavior of [[calculating_mean | sample means]] are fundamental to statistics, particularly through the **Central Limit Theorem (CLT)** <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>.

## The Central Limit Theorem (CLT)

The Central Limit Theorem states that if you start with *any* distribution that has a well-defined [[understanding_mean | mean]] and variance (and thus a well-defined standard deviation), whether continuous or discrete, the distribution of its [[understanding_mean | sample means]] will approximate a normal distribution <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. This holds true even if the original distribution is far from normal <a class="yt-timestamp" data-t="00:08:07">[00:08:07]</a>.

### The Sampling Process

To understand the CLT, consider an original probability distribution function. For example, a "crazy dice" distribution where getting a 1 or a 6 is very likely, a 3 or 4 is moderately likely, and a 2 or 5 is impossible <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.

Instead of just taking individual samples from this distribution, the process involves:
1.  **Defining a Sample Size (n):** This is the number of observations taken in each individual "sample" <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>. For instance, if `n = 4`, you take four observations <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.
2.  **Taking Multiple Samples:** Repeatedly draw `n` observations from the original distribution <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.
3.  **Calculating the Sample Mean:** For each sample of size `n`, calculate its [[understanding_mean | mean]] (average) <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>, <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.
    *   *Example 1 (n=4):* If observations are {1, 1, 3, 6}, the [[calculating_mean | sample mean]] is (1+1+3+6)/4 = 2.75 <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.
    *   *Example 2 (n=4):* If observations are {3, 4, 3, 1}, the [[calculating_mean | sample mean]] is (3+4+3+1)/4 = 2.75 <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.
    *   *Example 3 (n=4):* If observations are {1, 1, 6, 6}, the [[calculating_mean | sample mean]] is (1+1+6+6)/4 = 3.5 <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.
4.  **Plotting the Frequency of Sample Means:** Each calculated [[understanding_mean | sample mean]] is plotted on a frequency distribution <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>.

### The Sampling Distribution of the Sample Mean

When many sample means are plotted, the resulting frequency distribution is called the [[zscore_and_sampling_distribution | sampling distribution]] of the [[understanding_mean | sample mean]] <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.

Even if the original distribution is highly irregular, the [[zscore_and_sampling_distribution | sampling distribution]] of the [[understanding_mean | sample mean]] will begin to approximate a normal distribution as more samples are taken <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>.

#### Impact of Sample Size (n)

The sample size (`n`) significantly impacts the shape of the [[zscore_and_sampling_distribution | sampling distribution]]:
*   **Approximation to Normal:** As the sample size (`n`) increases, the [[zscore_and_sampling_distribution | sampling distribution]] of the [[understanding_mean | sample mean]] more closely approximates a normal distribution <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a>, <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>. This approximation can be quite good even with relatively small sample sizes like 10 or 20 <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>.
*   **Mean of the Sampling Distribution:** The [[understanding_mean | mean]] of the [[zscore_and_sampling_distribution | sampling distribution]] of the [[understanding_mean | sample means]] will be the same as the [[understanding_mean | mean]] of the original population distribution <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>.
*   **Standard Deviation of the Sampling Distribution:** The standard deviation of the [[zscore_and_sampling_distribution | sampling distribution]] of the [[understanding_mean | sample means]] (often called the standard error) will decrease as the sample size (`n`) increases <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>. This is part of the [[implications_of_sample_size_on_statistical_distribution | implications of sample size on statistical distribution]].

> "What's cool is we can start with some crazy distribution. This has nothing to do with a normal distribution. But if we were to take 100 of these, instead of four here, and average them and then plot that average, the frequency of it... if we do that a bunch of times, in fact, if we were to do that an infinite time... we would find a perfect normal distribution." <a class="yt-timestamp" data-t="00:08:07">[00:08:07]</a>

### Broader Applications of the CLT

The Central Limit Theorem is not limited to just [[understanding_mean | sample means]]. It also applies to [[understanding_mean | sample sums]] <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>. This generality makes it incredibly useful in practical applications <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>.

In real-world scenarios, where the underlying probability distributions of various processes (e.g., biological interactions, human behavior) are unknown, the CLT provides a powerful insight <a class="yt-timestamp" data-t="00:08:51">[00:08:51]</a>. It explains why the normal distribution is so prevalent in statistics: when many independent random variables are added or averaged together, their aggregate behavior tends toward a normal distribution, regardless of their individual distributions <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>. This makes the normal distribution a very good approximation for the sum or [[understanding_mean | means]] of many processes observed in daily life <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a>.