---
title: Normal Distribution
videoId: JNm3M9cqWyc
---

From: [[khanacademy]] <br/> 

The normal distribution is considered one of the most fundamental and profound concepts in statistics and mathematics <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. It frequently appears in statistics due to its utility as a good approximation for the sum or means of many processes <a class="yt-timestamp" data-t="00:09:28">[00:09:28]</a>.

## Emergence from the Central Limit Theorem

The power of the normal distribution is revealed through the [[central_limit_theorem | Central Limit Theorem]] <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. This theorem states that if one starts with any distribution that has a well-defined mean and variance (and thus a well-defined [[standard_deviation_and_sampling_distribution | standard deviation]]) <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>, whether continuous or discrete <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>, the [[sampling_distribution_and_standard_deviation | sampling distribution]] of its sample means will approximate a normal distribution <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>.

### Illustrative Example

Consider a highly asymmetric discrete [[probability_distribution_functions | probability distribution function]] that is not close to a normal distribution <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>. For example, a distribution where values 1 and 6 are very likely, 2 and 5 are impossible, and 3 and 4 have an average likelihood <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.

Instead of directly sampling from this original distribution, one can take multiple samples of a specific size (n) from it, calculate the mean of each sample, and then plot the frequency of these sample means <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>.

*   **Sample Size (n=4):** If samples of size n=4 are repeatedly drawn (e.g., 10,000 times) and their means calculated and plotted, the resulting frequency distribution will begin to approximate a normal distribution <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>.
*   **Larger Sample Sizes (e.g., n=20):** As the sample size (n) increases (e.g., to 20) <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>, the [[sampling_distribution_and_standard_deviation | sampling distribution]] of the sample means will even more closely approximate a normal distribution <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>. While the mean of this distribution of sample means will remain the same as the original distribution's mean, its [[standard_deviation_and_sampling_distribution | standard deviation]] will be smaller <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>.

### The Role of Sample Size

The approximation to a normal distribution becomes more accurate as the sample size (n) becomes larger, theoretically approaching a perfect normal distribution as n approaches infinity <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>. However, even with relatively small sample sizes like 10 or 20, the approximation can be very close to a normal distribution, often as good as approximations seen in everyday life <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>.

> "What's cool is we can start with some crazy distribution. This has nothing to do with a normal distribution." <a class="yt-timestamp" data-t="00:08:07">[00:08:07]</a>

This phenomenon also applies to the sample sum, not just the sample mean <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>.

## Real-World Significance

The [[application_of_central_limit_theorem_in_real_life | Central Limit Theorem]] explains why the normal distribution is so prevalent <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>. In real-life scenarios, where the underlying [[probability_distribution_functions | probability distribution functions]] of complex processes (e.g., protein interactions, human behaviors) are unknown <a class="yt-timestamp" data-t="00:08:51">[00:08:51]</a>, the theorem provides a powerful tool. If many such actions are added together or their means are taken, and their frequencies are plotted, the result will tend towards a normal distribution <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>. This makes the normal distribution a very good approximation for sums or means across many processes <a class="yt-timestamp" data-t="00:09:28">[00:09:28]</a>.