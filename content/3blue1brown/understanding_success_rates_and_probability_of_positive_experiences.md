---
title: Understanding success rates and probability of positive experiences
videoId: 8idr1WZ1A7Q
---

From: [[3blue1brown]] <br/> 

When buying a product online, consumers often face a choice between multiple sellers offering the same item at similar prices, but with varying ratings and review counts <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. For example, consider three sellers:
*   **Seller 1:** 100% positive rating from 10 reviews <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>.
*   **Seller 2:** 96% positive rating from 50 reviews <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.
*   **Seller 3:** 93% positive rating from 200 reviews <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>.

The challenge is to determine which seller to choose <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. Intuitively, more data generally provides greater confidence in a rating <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>. High percentages from very few reviews often trigger suspicion, as a small number of reviews makes it more plausible that outcomes could have been different, leading to a lower rating <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>. The key is to quantify this intuition and rationally weigh the confidence gained from more data against a lower absolute percentage <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.

This problem is a modification of an example provided by John Cook in his blog post, "A Bayesian Review of Amazon Resellers" <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. It serves as an excellent case study to explore core topics in [[probability_and_information_measurement|probability]] and statistics <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>.

This topic will be explored in three parts:
1.  **Setting up the Model:** Defining the situation and introducing the [[probability_density_and_distribution|binomial distribution]] <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.
2.  **Bayesian Updating and Continuous Values:** Incorporating ideas of Bayesian updating and working with probabilities over [[continuous_values_and_probability_paradox|continuous values]] <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>.
3.  **Beta Distribution and Optimization:** Examining the Beta distribution and using Python to analyze data and determine optimal choices <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.

## A Simple Solution: Laplace's Rule of Succession

Before diving into the mathematical details, one delightfully simple answer comes from Laplace's rule of succession <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>. This rule suggests that when observing an online rating, such as 10 positive reviews out of 10 total, one should pretend there were two additional reviews: one positive and one negative <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.

Applying this rule to the seller examples:
*   **Seller 1 (10 out of 10):** Pretend it's 11 positive out of 12 total (10+1 positive, 0+1 negative), yielding a perceived 91.7% success rate (11/12) <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>. This is considered the [[probability_of_probabilities|probability]] of a good experience with that seller <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.
*   **Seller 2 (48 positive out of 50):** Pretend it's 49 positive out of 52 total (48+1 positive, 2+1 negative), yielding 94.2% (49/52) <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.
*   **Seller 3 (186 positive out of 200):** Pretend it's 187 positive out of 202 total (186+1 positive, 14+1 negative), yielding 92.6% (187/202) <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>.

Based on this rule, Seller 2 would be the best choice <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>. Laplace's rule of succession dates back to the 18th century <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>. Understanding its underlying assumptions and how different goals might alter the choice requires a deeper mathematical dive <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.

## Modeling the Situation and Defining the Goal

To properly approach this, we first need to model the situation and define what we want to optimize <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>. Each seller can be thought of as a source of random experiences, which are either positive or negative <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>. Each seller has a constant, underlying [[probability_of_probabilities|probability]] of providing a good experience, referred to as their "success rate," or *S* <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>. The core challenge is that this true success rate *S* is unknown <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.

For instance, a 100% positive rating from 10 reviews doesn't mean the seller's true success rate is 100%; it could plausibly be 95% <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>. A simulation demonstrates this: if a seller genuinely has a 95% success rate, approximately 60% of sequences of 10 reviews would still result in 10 out of 10 positive reviews <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>. The observed data is perfectly plausible even if the true success rate is not 100% <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>. The uncertainty lies in not knowing the true *S* <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>.

The goal is generally to maximize the [[probability_of_probabilities|probability]] of having a positive experience, despite the uncertainty about the success rate <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>. This requires saying something about the likelihood of each possible success rate (from 0 to 1), a concept known as a [[understanding_probability_of_probabilities|probability of probabilities]] <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>. Unlike basic [[probability_and_information_measurement|probability]] problems like coin flips where the long-run frequency is assumed (e.g., 0.5 for heads), here we have uncertainty about the long-run frequency itself, which is a more profound type of doubt <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.

This setup is highly relevant to many real-world situations where judgments about random processes must be made from limited data <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>. For example, if a factory's initial test of 100 cars shows 2 problems, what can be confidently said about the error rate for a million cars, given that a 2% error rate is not guaranteed? <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.

## Probability of Data Given Success Rate

A fundamental question is: If the true success rate for a seller were known (e.g., 95%), how would one compute the [[probability_of_probabilities|probability]] of observing specific review data (e.g., 10 positive and 0 negative, 48 positive and 2 negative, or 186 positive and 14 negative)? This is asking for the probability of seeing the data *given* an assumed success rate <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.

One approach is to use [[simulation_examples_of_probability_distribution|simulations]] <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>. By running many simulations of 10 or 50 reviews with a fixed success rate, one can build a histogram to understand the [[probability_density_and_distribution|distribution]] of outcomes <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>. For instance, after hundreds of thousands of simulations of 50 reviews with a 95% success rate, it appears about 26.1% would result in 48 out of 50 positive reviews <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>.

Fortunately, an exact formula exists for this scenario: the [[probability_density_and_distribution|binomial distribution]] <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>.
The probability of seeing exactly *k* positive reviews out of *n* total reviews, given a success rate *S*, is:

P(*k* positive reviews | *S*) = (n choose k) * S^k * (1-S)^(n-k)

Where:
*   (n choose k) represents the number of ways to choose *k* positive outcomes from *n* trials <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>. For example, "50 choose 48" is 1225 ways <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>.
*   S^k is the [[probability_of_probabilities|probability]] of *k* positive reviews.
*   (1-S)^(n-k) is the [[probability_of_probabilities|probability]] of *n-k* negative reviews.
*   Each review is assumed to be independent <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>.

Using this formula for 48 positive reviews out of 50 with an assumed 95% success rate yields 0.261, matching the simulation <a class="yt-timestamp" data-t="00:07:52">[00:07:52]</a>.

### The Binomial Distribution

This formula describes the [[probability_density_and_distribution|binomial distribution]], a fundamental concept in [[probability_and_information_measurement|probability]] that applies whenever there are repeated independent trials with two possible outcomes (like a coin flip) <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.

By varying the success rate *S* (from 0 to 1), while keeping the observed data fixed (e.g., 48 positive out of 50), we can plot how the probability of seeing that data changes <a class="yt-timestamp" data-t="00:08:54">[00:08:54]</a>. This plot shows that the [[probability_of_probabilities|probability]] is maximized when *S* is equal to the observed percentage (e.g., 0.96 for 48/50) <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a>. As *S* approaches 1, the [[probability_of_probabilities|probability]] drops to zero, because a perfect seller would never have negative reviews <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>. Similarly, as *S* decreases, the [[probability_of_probabilities|probability]] rapidly approaches zero <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>. This curve provides a quantitative description of which values of *S* are more or less plausible given the observed data <a class="yt-timestamp" data-t="00:10:06">[00:10:06]</a>.

The formula for this curve, as a function of the success rate *S*, is proportional to:
S^(number of positive reviews) * (1-S)^(number of negative reviews) <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>.

If more data were available, such as 480 positive reviews out of 500, the resulting plot would still be centered around 0.96 but would be narrower and more concentrated, indicating greater confidence in the true success rate being near 0.96 <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>.

## From Data-Given-S to S-Given-Data

The goal is to compute the [[probability_of_probabilities|probability]] of having a good experience with a seller <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>. While the peak of the graph (e.g., 96% for the 48/50 seller) might seem like the answer, this is the most likely success rate *given the data*, not necessarily the [[probability_of_probabilities|probability]] of a future good experience <a class="yt-timestamp" data-t="00:10:59">[00:10:59]</a>.

Consider the 10 out of 10 positive reviews example. The binomial formula simplifies to S^10. This plot shows that the [[probability_of_probabilities|probability]] of seeing 10 consecutive good reviews increases as *S* approaches 1 <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>. Even though *S* = 1 maximizes this probability, it is unrealistic to assume a 100% [[probability_of_probabilities|probability]] of a good experience <a class="yt-timestamp" data-t="00:11:32">[00:11:32]</a>.

Instead, we need to understand how to convert the [[probability_of_probabilities|probability]] of the data given *S* into the [[probability_of_probabilities|probability]] of *S* given the data we observe. This crucial step requires understanding Bayes' rule and [[applications_of_probability_density_function|probability density functions]] <a class="yt-timestamp" data-t="00:11:51">[00:11:51]</a>.