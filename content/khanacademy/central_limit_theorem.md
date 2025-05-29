---
title: Central limit theorem
videoId: JNm3M9cqWyc
---

From: [[khanacademy]] <br/> 

The [[importance_of_central_limit_theorem_in_statistics | Central Limit Theorem]] (CLT) is considered one of the most fundamental and profound concepts in statistics, and possibly in all of mathematics <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>.

## Core Principle

The theorem states that if you start with any distribution that possesses a well-defined [[mean_and_central_tendency | mean]] and variance (which implies a well-defined standard deviation), whether it's a continuous or discrete distribution, you can predict the shape of the distribution of its sample [[mean_and_central_tendency | means]] <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>.

The power of the Central Limit Theorem lies in its ability to transform nearly any initial probability distribution into a [[normal_distribution | normal distribution]] when dealing with sample averages <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.

## Demonstration Process

To illustrate the CLT, consider an arbitrary discrete probability distribution, such as a "crazy dice" that can yield values from 1 to 6 with uneven probabilities (e.g., high likelihood for 1 and 6, impossible for 2 and 5) <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.

The process involves:
1.  **Taking Samples:** Instead of just taking individual samples from the original distribution, you take multiple samples of a specific size `n` <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.
2.  **Averaging Samples:** For each set of `n` samples, calculate their [[mean_and_central_tendency | mean]] <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>. This is referred to as a "sample mean" <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>.
3.  **Plotting Frequencies:** Plot the frequency of these calculated sample [[mean_and_central_tendency | means]] on a distribution graph <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>.

### Example with Sample Size `n=4`

If you set the sample size `n` to 4, you would repeatedly take four samples from the original distribution, calculate their [[mean_and_central_tendency | mean]], and record it <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.
*   **Sample 1:** If samples are (1, 1, 3, 6), the sample [[mean_and_central_tendency | mean]] is (1+1+3+6)/4 = 2.75 <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>.
*   **Sample 2:** If samples are (3, 4, 3, 1), the sample [[mean_and_central_tendency | mean]] is (3+4+3+1)/4 = 2.75 <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.
*   **Sample 3:** If samples are (1, 1, 6, 6), the sample [[mean_and_central_tendency | mean]] is (1+1+6+6)/4 = 3.5 <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>.

As you collect thousands of these sample [[mean_and_central_tendency | means]] (e.g., 10,000 samples) and plot their frequencies, the resulting distribution of sample [[mean_and_central_tendency | means]] will begin to approximate a [[normal_distribution | normal distribution]] <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>.

### Effect of Increasing Sample Size (`n`)

The approximation to a [[normal_distribution | normal distribution]] becomes even closer as the sample size `n` increases <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a>. For example, if you repeat the process with a sample size of `n=20`, the distribution of sample [[mean_and_central_tendency | means]] will be even more tightly clustered around the original distribution's [[mean_and_central_tendency | mean]] and will look more like a [[normal_distribution | normal distribution]] <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>.

Even with relatively small sample sizes like 10 or 20, the approximation to a [[normal_distribution | normal distribution]] is often very good for practical purposes <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>. If an infinite sample size were taken, the resulting distribution would be a perfect [[normal_distribution | normal distribution]] <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>.

## Applications and Significance

The CLT applies not only to sample [[mean_and_central_tendency | means]] but also to sample sums <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>. This is incredibly useful because in real-world scenarios, the underlying probability distributions of complex processes (e.g., protein interactions, human behavior) are often unknown <a class="yt-timestamp" data-t="00:08:51">[00:08:51]</a>.

Despite this lack of knowledge, the CLT allows statisticians to use the [[normal_distribution | normal distribution]] as a model for the [[mean_and_central_tendency | means]] or sums of many independent observations, even if the individual observations come from a non-normal distribution <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>. This is why the [[normal_distribution | normal distribution]] appears so frequently in statistics and serves as a robust approximation for the [[mean_and_central_tendency | mean]] or sum of various processes <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>.