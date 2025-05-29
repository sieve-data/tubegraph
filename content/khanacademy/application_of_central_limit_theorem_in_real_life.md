---
title: Application of Central Limit Theorem in Real Life
videoId: JNm3M9cqWyc
---

From: [[khanacademy]] <br/> 

The [[central_limit_theorem | Central Limit Theorem]] is considered one of the most fundamental and profound concepts in [[statistics]] and potentially all of mathematics <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. It explains why the [[normal_distribution | normal distribution]] appears so frequently in various processes and phenomena <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>.

## Core Concept of the Central Limit Theorem

The [[central_limit_theorem | Central Limit Theorem]] states that if you start with *any* distribution that has a well-defined [[mean_or_central_tendency_in_statistics | mean]] and variance (and thus a well-defined standard deviation), whether it's continuous or discrete, the distribution of its sample means will approximate a [[normal_distribution | normal distribution]] as the sample size increases <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>, <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>, <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>, <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>, <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>, <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>, <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>, <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>, <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.

### Illustrative Example: The "Crazy Dice" Distribution

To demonstrate the power of the [[central_limit_theorem | Central Limit Theorem]], consider a highly irregular discrete [[experimentation_in_probability | probability distribution function]] that does not resemble a [[normal_distribution | normal distribution]] at all <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>, <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>, <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>. For instance, imagine a "crazy dice" that can take on values from 1 through 6, but with an uneven likelihood:
*   Very high likelihood of getting a 1 <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>, <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.
*   Impossible to get a 2 or a 5 (probability of 0) <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>, <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>, <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.
*   Okay likelihood of getting a 3 or a 4 <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.
*   Very likely to get a 6 <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.

#### The Process of Sampling Means

Instead of just taking samples of this [[concept_of_random_variables | random variable]], the process involves:
1.  **Defining Sample Size (n)**: For example, let's start with a sample size of n=4 <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>, <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.
2.  **Taking Multiple Samples**: Take four samples from the original "crazy dice" distribution for one "sample" <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>. For example, a sample might be (1, 1, 3, 6) <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>.
3.  **Calculating the Sample Mean**: Calculate the [[mean_or_central_tendency_in_statistics | mean]] of this set of samples. For (1, 1, 3, 6), the mean is (1+1+3+6)/4 = 2.75 <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>, <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>, <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.
4.  **Repeating and Plotting Frequencies**: Repeat this process many times (e.g., 10,000 times), each time calculating a new sample mean and plotting its frequency on a distribution graph <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>, <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>, <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>, <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.

#### Observation for n=4
Even with a small sample size like n=4, the frequency distribution of these sample means will begin to approximate a [[normal_distribution | normal distribution]] <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>, <a class="yt-timestamp" data-t="00:06:12">[00:06:12]</a>, <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>.

## Effect of Sample Size

As the sample size (n) becomes larger (e.g., n=20 instead of n=4) and approaches infinity, the distribution of the sample means exhibits distinct characteristics according to the [[central_limit_theorem_and_sample_size_considerations | Central Limit Theorem and sample size considerations]]:
*   **Closer Approximation to Normal Distribution**: The distribution of sample means will even more closely approximate a [[normal_distribution | normal distribution]] <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>, <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>, <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>, <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>.
*   **Same Mean**: The [[mean_or_central_tendency_in_statistics | mean]] of the sampling distribution will be the same as the [[mean_or_central_tendency_in_statistics | mean]] of the original population distribution <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>, <a class="yt-timestamp" data-t="00:07:25">[00:07:25]</a>.
*   **Smaller Standard Deviation**: The standard deviation of the sampling distribution (also known as the standard error) will be smaller, indicating less spread <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>.

Even relatively small sample sizes (like 10 or 20) can yield a very good approximation of a [[normal_distribution | normal distribution]] for the sample means <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>, <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>. If an infinite sample size were possible, a perfect [[normal_distribution | normal distribution]] would be found for the sample means <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a>, <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>. The theorem also applies to the sample sum, not just the sample [[mean_or_central_tendency_in_statistics | mean]] <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>, <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>, <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>, <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>.

## Real-Life Applications

The power of the [[central_limit_theorem | Central Limit Theorem]] lies in its applicability to various real-world scenarios, even when the underlying probability distributions are unknown <a class="yt-timestamp" data-t="00:08:51">[00:08:51]</a>, <a class="yt-timestamp" data-t="00:08:54">[00:08:54]</a>. Many natural and social phenomena involve countless individual actions or processes (e.g., protein interactions, human behaviors) whose individual distributions might be complex or unknown <a class="yt-timestamp" data-t="00:08:54">[00:08:54]</a>, <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>, <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.

The [[central_limit_theorem | Central Limit Theorem]] tells us that if we aggregate or average a large number of these actions, the distribution of these aggregates or means will tend towards a [[normal_distribution | normal distribution]], assuming each action has the same distribution <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>, <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>, <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>, <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>, <a class="yt-timestamp" data-t="00:09:13">[00:09:13]</a>, <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>. This is why the [[normal_distribution | normal distribution]] is so prevalent and useful in [[statistics]], serving as a good approximation for the sums or means of many processes <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>, <a class="yt-timestamp" data-t="00:09:22">[00:09:22]</a>, <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a>, <a class="yt-timestamp" data-t="00:09:28">[00:09:28]</a>. The demonstration of this reality, where increasing sample size leads to a frequency plot closely resembling a [[normal_distribution | normal distribution]], is crucial for understanding its [[reallife_calculations_and_examples_of_statistical_measures | real-life calculations and examples of statistical measures]] <a class="yt-timestamp" data-t="00:09:33">[00:09:33]</a>, <a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a>, <a class="yt-timestamp" data-t="00:09:39">[00:09:39]</a>, <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>, <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a>, <a class="yt-timestamp" data-t="00:09:45">[00:09:45]</a>.