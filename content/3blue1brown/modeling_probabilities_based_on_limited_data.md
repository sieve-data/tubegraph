---
title: Modeling probabilities based on limited data
videoId: 8idr1WZ1A7Q
---

From: [[3blue1brown]] <br/> 

When evaluating options online, such as product sellers, users often encounter varying levels of data confidence. For example, a seller might have a 100% positive rating from 10 reviews, another 96% from 50 reviews, and a third 93% from 200 reviews <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This scenario highlights the challenge of making a rational decision given the trade-off between a higher absolute percentage and the confidence gained from more data <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.

Our natural [[human_judgment_and_probability_misconceptions | intuition]] suggests that more data provides greater confidence in a rating <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>. High percentages from very few reviews, like 100%, can be suspicious because a small number of reviews makes it more plausible that outcomes could have been different, leading to a lower rating <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>. The key is to quantify this intuition. This particular problem is a slight modification of an example provided by John Cook in his blog post, "A Bayesian Review of Amazon Resellers" <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.

## Laplace's Rule of Succession

Before diving into the mathematical details, one simple answer to this problem is provided by Laplace's rule of succession, dating back to the 18th century <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>. This rule suggests that when you see an online rating, you should "pretend" that there were two additional reviews: one positive and one negative <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>. The resulting percentage can be considered your probability of having a good experience with that seller <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.

Let's apply this to the example sellers:
*   **Seller 1**: 100% positive rating from 10 reviews (10 out of 10). Applying the rule, this becomes 11 out of 12 reviews, resulting in 91.7% <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.
*   **Seller 2**: 96% positive rating from 50 reviews (48 out of 50). Applying the rule, this becomes 49 positive and 3 negative (49 out of 52), yielding 94.2% <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.
*   **Seller 3**: 93% positive rating from 200 reviews (186 out of 200). Applying the rule, this becomes 187 out of 202, yielding 92.6% <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>.

According to Laplace's rule, Seller 2 would be the best choice, as it offers the highest probability (94.2%) of a good experience <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>. Understanding the assumptions behind this rule and how changing goals or assumptions can alter the best choice requires a deeper dive into the mathematics <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.

## Modeling the Situation

To model this, each seller can be viewed as producing random experiences that are either positive or negative <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>. Each seller is assumed to have a constant underlying probability of giving a good experience, referred to as the **success rate (S)** <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>. The main challenge is that this true success rate S is unknown <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>. For example, a 100% rating from 10 reviews does not mean the underlying success rate is truly 100%; it could plausibly be 95% <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.

A [[simulation_of_random_processes_and_probability | simulation]] can illustrate this: if a seller's true success rate is 95%, about 60% of sequences of 10 reviews would still result in 10 out of 10 positive reviews <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>. This means observing 10 positive reviews is perfectly plausible even if the true success rate is 95% (or 90% or 99%) <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>.

The primary goal in this context is to maximize the [[probability_of_a_probability | probability]] of having a positive experience, despite the uncertainty about the success rate <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>. This involves reasoning about a "[[probability_of_a_probability | probability of probabilities]]"—determining how likely each possible success rate (from 0 to 1) is <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>. Unlike simple probability examples (like coin flips) where the long-run frequency is assumed (e.g., 0.5 or 0.6), here there is uncertainty about the long-run frequency itself, representing a more significant type of doubt <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>.

This modeling approach is relevant to many real-world scenarios requiring judgment from limited data, such as estimating the defect rate in a factory producing cars based on initial tests <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>.

## The Binomial Distribution

A core question is: if the true success rate (S) for a seller were known (e.g., 95%), how would one compute the probability of seeing a specific set of reviews, like 10 positive and 0 negative, or 48 positive and 2 negative <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>? In other words, what is the probability of observing the data *given* an assumed success rate? <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>

One way to approach this is through [[simulation_of_random_processes_and_probability | simulation]]. By generating many sets of random reviews (e.g., 10 or 50 reviews) based on an assumed success rate, one can build a histogram to understand the distribution of outcomes <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>. For instance, assuming a 95% success rate for 50 reviews, a simulation might show that about 26.1% of trials would result in 48 positive reviews out of 50 <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>.

Fortunately, an exact formula exists for this, known as the **binomial distribution** <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>. It is one of the most fundamental distributions in probability and applies when there are independent, binary random events repeated a number of times <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.

The probability of seeing exactly *k* positive reviews out of *n* total reviews, given a success rate *S*, is given by:

$$P(\text{k positives out of n} | S) = \binom{n}{k} \times S^k \times (1-S)^{n-k}$$
<a class="yt-timestamp" data-t="00:06:52">[00:06:52]</a>

Where:
*   $\binom{n}{k}$ (pronounced "n choose k") represents the total number of ways to choose *k* successes from *n* trials <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>. For example, 50 choose 48 is 1225 <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>.
*   $S^k$ is the probability of *k* positive reviews.
*   $(1-S)^{n-k}$ is the probability of *n-k* negative reviews.

The assumption of independent reviews is crucial for multiplying probabilities in this way <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>. Using this formula, for 48 out of 50 reviews with $S=0.95$, the probability is 0.261, matching the simulation <a class="yt-timestamp" data-t="00:07:52">[00:07:52]</a>.

When plotting the probability of seeing 48 out of 50 reviews as a function of the success rate S, the value peaks at S = 0.96, which is the observed rating <a class="yt-timestamp" data-t="00:09:19">[00:09:19]</a>. This plot of P(Data | S) provides a quantitative description of which values of S are more or less plausible given the observed data <a class="yt-timestamp" data-t="00:10:06">[00:10:06]</a>. The curve generally looks like a constant multiplied by $S^{\text{positive reviews}} \times (1-S)^{\text{negative reviews}}$ <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>.

With more data, such as 480 positive reviews and 20 negative reviews (still centered around 0.96), the resulting plot would be narrower and more concentrated, indicating higher confidence in the true success rate being near 0.96 <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>.

## From Data Given S to S Given Data

The ultimate goal is to determine the probability of a specific success rate *given* the observed data (P(S | Data)), rather than the probability of the data given a success rate (P(Data | S)) <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>. These are distinct, though related, probabilities <a class="yt-timestamp" data-t="00:08:51">[00:08:51]</a>.

Consider the example of 10 out of 10 positive reviews. The binomial formula simplifies to $S^{10}$ <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>. The probability of seeing 10 consecutive good reviews increases as S approaches 1. This means the plot of P(Data | S) for 10/10 reviews continuously increases towards S=1 <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a>. However, even if S=1 maximizes this probability, it does not mean one should assume a 100% probability of a good experience with that seller <a class="yt-timestamp" data-t="00:11:32">[00:11:32]</a>.

To bridge this gap and properly calculate P(S | Data), methods like finding the "center of mass" of the graph are on the right track <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>. This requires applying **Bayes' Rule** and understanding [[applications_of_probability_density | probability density functions]] <a class="yt-timestamp" data-t="00:11:51">[00:11:51]</a>.