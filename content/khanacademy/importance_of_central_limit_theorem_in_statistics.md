---
title: Importance of central limit theorem in statistics
videoId: JNm3M9cqWyc
---

From: [[khanacademy]] <br/> 

The [[central_limit_theorem | Central Limit Theorem]] (CLT) is considered one of the most fundamental and profound concepts in [[introduction_to_statistics | statistics]] and perhaps in all of mathematics <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. Its significance stems from its ability to connect virtually any probability distribution to the normal distribution under specific conditions.

## Core Concept of the Central Limit Theorem

The theorem states that if one starts with *any* distribution that possesses a well-defined [[measures_of_central_tendency | mean]] and variance (and consequently, a standard deviation) <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>, the distribution of sample means (or sums) will approximate a normal distribution, regardless of the original distribution's shape <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>, <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>. This holds true whether the original distribution is continuous or discrete <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>.

## How it Works: Sampling Distribution of the Mean

Consider a hypothetical "crazy" discrete probability distribution, which is far from a normal distribution <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>. This distribution might have values like 1, 3, 4, and 6, with varying probabilities, and even impossible values like 2 and 5 <a class="yt-timestamp" data-t="00:00:45">[00:01:04]</a>.

Instead of just taking individual samples from this distribution, the [[central_limit_theorem | Central Limit Theorem]] focuses on taking *samples of averages* <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>. This process involves:
1.  Defining a sample size, `n` (e.g., `n` = 4) <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.
2.  Taking `n` samples from the original distribution <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.
3.  Calculating the [[mean_and_central_tendency | mean]] of these `n` samples <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.
4.  Repeating this process many, many times (e.g., 10,000 times) <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.
5.  Plotting the frequency of each calculated sample [[mean_and_central_tendency | mean]] <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>.

### [[implications_of_sample_size_on_statistical_distribution | Implications of Sample Size on Statistical Distribution]]

As the number of repetitions increases and, crucially, as the sample size (`n`) becomes larger:
*   The frequency distribution of these sample means will begin to approximate a normal distribution <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>, <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a>.
*   This approximated normal distribution will have the same [[central_tendency | mean]] as the original distribution <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>.
*   The standard deviation of this sampling distribution of means will be smaller as `n` increases <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>.
*   Even with relatively small sample sizes like 10 or 20, the approximation to a normal distribution can be very good <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>. If an infinite sample size were possible, a perfect normal distribution would be found <a class="yt-timestamp" data-t="00:08:32">[00:08:35]</a>.

## Broad Utility in Statistics

The [[central_limit_theorem | Central Limit Theorem]]'s profound utility lies in its wide applicability:
*   **Beyond Means**: It applies not only to the sample [[mean_and_central_tendency | mean]] but also to the sample sum <a class="yt-timestamp" data-t="00:08:44">[00:08:46]</a>.
*   **Real-World Phenomena**: Many real-world processes have unknown or complex probability distribution functions <a class="yt-timestamp" data-t="00:09:00">[00:09:02]</a>. Examples include the interactions of proteins or human behaviors <a class="yt-timestamp" data-t="00:08:54">[00:08:59]</a>.
*   **Justification for Normal Distribution**: The CLT provides a statistical justification for why the normal distribution is observed so frequently in nature and social sciences <a class="yt-timestamp" data-t="00:09:18">[00:09:22]</a>. When many independent random variables are added together (or averaged), their collective distribution tends towards normality, regardless of their individual distributions <a class="yt-timestamp" data-t="00:09:04">[00:09:16]</a>. This makes the normal distribution a very good approximation for the sum or means of many processes <a class="yt-timestamp" data-t="00:09:25">[00:09:28]</a>.

The practical consequence for [[introduction_to_inferential_statistics | inferential statistics]] is immense. It allows statisticians to use the properties of the normal distribution (e.g., for calculating [[probability_in_inferential_statistics | probability]] or constructing confidence intervals and performing hypothesis tests using concepts like the [[use_of_zstatistic_in_inferential_statistics | Z-statistic]]) even when the original population distribution is unknown or non-normal, provided that the sample size is sufficiently large.