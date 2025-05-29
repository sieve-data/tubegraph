---
title: Sample Size and Sampling
videoId: JNm3M9cqWyc
---

From: [[khanacademy]] <br/> 

The [[Central limit theorem and sample size considerations | Central Limit Theorem]] is a fundamental concept in [[Introduction to statistics | statistics]] and mathematics <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. It describes the behavior of the [[Sampling distribution and standard deviation | sampling distribution]] of sample means, regardless of the original distribution's shape <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>.

## The Central Limit Theorem and Sample Means

The [[Central limit theorem and sample size considerations | Central Limit Theorem]] states that if you start with *any* distribution that has a well-defined mean and [[Variance and its Calculation for Population and Sample | variance]] (and therefore a well-defined [[Standard deviation and sampling distribution | standard deviation]]), whether continuous or discrete <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>:
If you take sufficiently large samples from this distribution, calculate the mean of each sample, and then plot the frequency of these sample means, the resulting distribution will approximate a normal distribution <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>.

### Illustrative Example

Consider a discrete probability distribution function, such as a "crazy dice" that is very likely to roll a 1 or a 6, impossible to roll a 2 or 5, and has an "OK" likelihood of rolling a 3 or 4 <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>. This distribution is intentionally drawn not to resemble a normal distribution, to highlight the power of the theorem <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>, <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.

Instead of just taking individual values from this distribution, the process involves:
1.  **Defining a Sample Size (n)**: This determines how many individual "samples" (or observations) are taken from the original distribution for each new "sample" <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>. For instance, an initial sample size `n = 4` is chosen <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.
2.  **Taking Samples**: Four values are drawn from the original distribution (e.g., 1, 1, 3, 6 for the first sample; 3, 4, 3, 1 for the second) <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>, <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.
3.  **Calculating the Sample Mean**: The mean (average) of these four values is computed for each sample (e.g., (1+1+3+6)/4 = 2.75; (3+4+3+1)/4 = 2.75; (1+1+6+6)/4 = 3.5) <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>, <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>, <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>, <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.
4.  **Plotting Frequencies**: Each calculated sample mean is plotted on a frequency distribution <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>. As this process is repeated many times (e.g., 10,000 times) <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>, the frequency plot of these sample means begins to approximate a normal distribution <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>.

### The Impact of Sample Size

The [[Central limit theorem and sample size considerations | Central Limit Theorem]] highlights the critical role of sample size (n):
*   **Approximation to Normal Distribution**: As the sample size (`n`) increases, the [[Sampling distribution and standard deviation | sampling distribution]] of the sample means will more closely approximate a normal distribution <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>, <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a>. Even with relatively small sample sizes (e.g., 10 or 20), the approximation can be very good <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>.
*   **Mean of the Sampling Distribution**: The mean of the [[Sampling distribution and standard deviation | sampling distribution]] of the sample means will be the same as the mean of the original [[population versus sample | population]] distribution <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>, <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>.
*   **[[Standard deviation and sampling distribution | Standard Deviation]] of the Sampling Distribution**: As `n` increases, the [[Standard deviation and sampling distribution | standard deviation]] of the [[Sampling distribution and standard deviation | sampling distribution]] of the sample means decreases <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>. This means the sample means cluster more tightly around the true [[population versus sample | population]] mean.

This principle is why the normal distribution is so prevalent in [[Introduction to statistics | statistics]], as it provides a strong approximation for the sum or means of various processes encountered in real life, even if their underlying distributions are unknown or "crazy" <a class="yt-timestamp" data-t="00:08:51">[00:08:51]</a>, <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>.