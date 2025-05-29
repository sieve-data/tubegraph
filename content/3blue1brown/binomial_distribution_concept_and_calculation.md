---
title: Binomial distribution concept and calculation
videoId: 8idr1WZ1A7Q
---

From: [[3blue1brown]] <br/> 

The binomial distribution is a fundamental concept in probability theory, particularly useful when analyzing situations involving a series of independent trials, each with only two possible outcomes <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>. This article explores its application in understanding online seller ratings, where each customer experience is either positive or negative <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>.

## Modeling the Situation

When evaluating online sellers, each seller can be thought of as having a constant, underlying "success rate" (S), which represents the probability of providing a good experience <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a> <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>. The challenge is that this true success rate (S) is unknown <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>. For example, a seller with 100% positive ratings from 10 reviews might not have a true success rate of 100%; it could plausibly be 95% <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a> <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>. Simulations show that a seller with a 95% success rate could still yield 10 out of 10 positive reviews approximately 60% of the time <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a> <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>.

The ultimate goal in such scenarios is to maximize the [[probability_of_a_probability|probability]] of a positive experience, despite this uncertainty about the true success rate <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a> <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>. This setup is relevant to many real-world situations, such as judging the error rate of cars produced in a factory based on an initial test batch <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a> <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.

## Calculating Probabilities with the Binomial Distribution

Given an assumed true success rate (S) for a seller, the binomial distribution allows us to compute the probability of observing a specific number of positive and negative reviews <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a> <a class="yt-timestamp" data-t="00:05:45">[00:05:45]</a>. This provides the probability of seeing the data *given* an assumed success rate <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>.

The formula for the binomial distribution is:

$P(\text{k successes in n trials}) = \binom{n}{k} S^k (1-S)^{n-k}$ <a class="yt-timestamp" data-t="00:06:52">[00:06:52]</a>

Where:
*   $\binom{n}{k}$ (pronounced "n choose k") represents the number of ways to choose k successes out of n total trials <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a> <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>. For example, "50 choose 48" is 1225 <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>.
*   $S^k$ is the probability of getting $k$ positive reviews (successes), where S is the success rate.
*   $(1-S)^{n-k}$ is the probability of getting $n-k$ negative reviews (failures), where $(1-S)$ is the failure rate.

This formula relies on the assumption that each review (or trial) is independent of the last <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>.

### Example Calculation

Consider a seller with 50 reviews, 48 of which are positive and 2 are negative. If we assume a success rate (S) of 95% (0.95), the probability of observing exactly 48 out of 50 positive reviews is calculated as follows:

$\binom{50}{48} \times (0.95)^{48} \times (1-0.95)^2$ <a class="yt-timestamp" data-t="00:06:52">[00:06:52]</a>

This calculates to approximately 0.261 (or 26.1%), matching empirical simulations <a class="yt-timestamp" data-t="00:07:52">[00:07:52]</a> <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.

## Interpreting the Distribution

When the true success rate (S) varies, the binomial distribution for a given set of observed data (e.g., 48 positive reviews out of 50) changes <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>. For 48 out of 50 reviews, the probability of seeing this outcome is maximized when S is 0.96 <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a> <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>. As S approaches 1, the probability decreases because two negative reviews would not occur if the true success rate was perfect <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a> <a class="yt-timestamp" data-t="00:09:45">[00:09:45]</a>. Similarly, as S moves away from 0.96 to the left (e.g., to 0.8), the probability of observing 48 out of 50 positive reviews becomes exceedingly rare <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a> <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>.

The general form of this probability curve as a function of the success rate S is:
`Constant` $\times S^{\text{number of positive reviews}} \times (1-S)^{\text{number of negative reviews}}$ <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a> <a class="yt-timestamp" data-t="00:10:18">[00:10:18]</a>.

More data makes this plot "smaller and more concentrated" around the observed success rate <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a> <a class="yt-timestamp" data-t="00:10:36">[00:10:36]</a>.

## Limitations and Future Steps

While the binomial distribution helps compute the probability of observing data given an assumed success rate, our ultimate goal is the inverse: to determine the probability of a success rate given the fixed data we observe <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a> <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>. A naive approach of simply taking the peak probability (e.g., 96% for 48/50 reviews) doesn't account for uncertainty <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a> <a class="yt-timestamp" data-t="00:11:04">[00:11:04]</a>. For instance, with 10 out of 10 positive reviews, the binomial formula simplifies to $S^{10}$, which continuously increases as S approaches 1 <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a> <a class="yt-timestamp" data-t="00:11:15">[00:11:15]</a>. This would suggest a 100% probability of a good experience, which is intuitively incorrect due to the small sample size <a class="yt-timestamp" data-t="00:11:35">[00:11:35]</a> <a class="yt-timestamp" data-t="00:11:39">[00:11:39]</a>.

To move from the probability of data given S to the probability of S given the data, concepts like [[Bayes theorem and its significance|Bayes' rule]] and [[probability_distributions_and_softmax_function|probability density functions]] are required <a class="yt-timestamp" data-t="00:11:51">[00:11:51]</a> <a class="yt-timestamp" data-t="00:11:55">[00:11:55]</a>. These topics are crucial for [[introduction_to_bayesian_statistics|Bayesian updating]] and working with probabilities over continuous values <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a> <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.