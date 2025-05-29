---
title: Central Limit Theorem
videoId: JNm3M9cqWyc
---

From: [[khanacademy]] <br/> 

The [[central_limit_theorem_and_sample_size_considerations | Central Limit Theorem]] is considered one of the most fundamental and profound concepts in statistics, and possibly in all of mathematics <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>.

## Core Concept

The [[central_limit_theorem_and_sample_size_considerations | Central Limit Theorem]] states that if you start with any distribution that has a well-defined [[mean_or_central_tendency_in_statistics | mean]] and variance (and thus a well-defined standard deviation), whether continuous or discrete, and you take repeated samples of a certain size (`n`) from this distribution, the distribution of the sample [[mean_or_central_tendency_in_statistics | means]] will approximate a normal distribution <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>.

### Illustrative Example: A "Crazy" Dice Distribution

To demonstrate the power of the [[central_limit_theorem_and_sample_size_considerations | Central Limit Theorem]], consider a discrete probability distribution function that is far from a normal distribution <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>. For instance, a "crazy dice" that can take on values 1 through 6, with specific probabilities:
*   Very high likelihood of getting a 1 <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.
*   Impossible to get a 2 <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>.
*   OK likelihood of getting a 3 or a 4 <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.
*   Impossible to get a 5 <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>.
*   Very likely to get a 6 <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.

This distribution has its own [[mean_or_central_tendency_in_statistics | mean]] and standard deviation <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.

#### The Sampling Process

Instead of just taking individual samples, the process involves:
1.  **Defining a sample size (n):** For example, `n = 4` <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>.
2.  **Taking multiple samples:** Each sample consists of `n` observations drawn from the original distribution <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.
    *   *Sample 1 (n=4):* 1, 1, 3, 6. The [[mean_or_central_tendency_in_statistics | mean]] is (1+1+3+6)/4 = 2.75 <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>.
    *   *Sample 2 (n=4):* 3, 4, 3, 1. The [[mean_or_central_tendency_in_statistics | mean]] is (3+4+3+1)/4 = 2.75 <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.
    *   *Sample 3 (n=4):* 1, 1, 6, 6. The [[mean_or_central_tendency_in_statistics | mean]] is (1+1+6+6)/4 = 3.5 <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>.
3.  **Plotting the frequency of sample [[mean_or_central_tendency_in_statistics | means]]:** As each sample [[mean_or_central_tendency_in_statistics | mean]] is calculated, it is plotted on a frequency distribution <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>.

### Impact of Sample Size (`n`)

When many samples (e.g., 10,000) are taken for a given sample size `n`, the frequency distribution of these sample [[mean_or_central_tendency_in_statistics | means]] begins to approximate a normal distribution <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.

*   **For n = 4:** The distribution of sample [[mean_or_central_tendency_in_statistics | means]] will start to look like a normal distribution <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>.
*   **For n = 20 (or larger):** If the sample size `n` is increased (e.g., to 20), the distribution of sample [[mean_or_central_tendency_in_statistics | means]] will even more closely approximate a normal distribution <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a>.
    *   It will also have the same [[mean_or_central_tendency_in_statistics | mean]] as the original distribution <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>.
    *   It will have a smaller standard deviation compared to the distribution for `n=4` <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>.

The approximation to a normal distribution improves as the sample size `n` becomes larger <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>. Even sample sizes of 10 or 20 can yield a very good approximation, often as good as approximations seen in everyday life <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>. If an infinite sample size were taken, the result would be a perfect normal distribution <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>.

### Generalizability

The [[central_limit_theorem_and_sample_size_considerations | Central Limit Theorem]] also applies to the sum of samples, not just their [[mean_or_central_tendency_in_statistics | mean]] <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>.

## Significance and [[application_of_central_limit_theorem_in_real_life | Real-Life Application]]

The [[central_limit_theorem_and_sample_size_considerations | Central Limit Theorem]] is incredibly useful because in many real-world scenarios, the underlying probability distribution functions for processes (e.g., protein interactions, human behavior) are unknown <a class="yt-timestamp" data-t="00:08:51">[00:08:51]</a>.

However, the theorem tells us that if we sum or average a large number of independent actions or observations from such processes, the frequency distribution of these sums or [[mean_or_central_tendency_in_statistics | means]] will tend towards a normal distribution <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>. This is why the normal distribution appears so frequently in statistics and serves as a good approximation for the sums or [[mean_or_central_tendency_in_statistics | means]] of various processes <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>.

The principles of the [[central_limit_theorem_and_sample_size_considerations | Central Limit Theorem]], particularly how increasing sample size (`n`) leads to a frequency plot closely resembling a normal distribution, can be empirically demonstrated <a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a>.