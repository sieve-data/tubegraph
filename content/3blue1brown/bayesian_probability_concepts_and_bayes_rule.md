---
title: Bayesian probability concepts and Bayes rule
videoId: 8idr1WZ1A7Q
---

From: [[3blue1brown]] <br/> 

When buying a product online, consumers often face a dilemma: choosing between sellers with varying positive ratings and review counts <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. For instance, one seller might have 100% positive ratings from 10 reviews, another 96% from 50 reviews, and a third 93% from 200 reviews <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. This scenario naturally leads to an intuition that more data provides greater confidence in a given rating <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>. There's often suspicion about 100% ratings, as they frequently come from a small number of reviews, making it seem plausible that outcomes could have been different and resulted in a lower rating <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>. The core challenge is how to quantify this intuition and rationally weigh the confidence gained from more data against a lower absolute percentage <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.

This problem is a variation of an example provided by John Cook in his blog post, "A [[bayesian_approach_to_updating_beliefs_with_new_evidence | Bayesian]] Review of Amazon Resellers" <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. It serves as an excellent case study to delve into fundamental concepts in [[probability_and_information_measurement | probability]] and statistics <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>.

## A Glimpse at the Solution

Before diving into the mathematical details, one simple answer to the seller dilemma is provided by Laplace's rule of succession, which dates back to the 18th century <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>.

According to this rule:
*   For a 10 out of 10 rating (100% with 10 reviews), you pretend there were two additional reviews—one positive and one negative <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>. This results in an effective 11 out of 12 (91.7%) as the probability of a good experience <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.
*   For 48 out of 50 positive reviews (96% with 50 reviews), you pretend it's 49 positive and 3 negative, yielding 49 out of 52 (94.2%) <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.
*   For 186 out of 200 positive reviews (93% with 200 reviews), you pretend it's 187 out of 202 (92.6%) <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>.

Based on Laplace's rule, the second seller (96% with 50 reviews, effectively 94.2%) would be the best choice <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>. However, to understand the assumptions behind this rule and how different objectives might alter the choice, a deeper mathematical understanding is necessary <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.

## Modeling the Situation

To approach this problem rationally, the first step is to model the situation and define what needs to be optimized <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.

### The Success Rate (S)

Each seller can be thought of as producing random experiences that are either positive or negative <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>. Each seller possesses an underlying, constant probability of providing a good experience, referred to as their "success rate" (S) <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>. The central challenge lies in the fact that this true success rate (S) is unknown <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>. For example, a 100% rating from 10 reviews doesn't mean the true success rate is 100%; it could be 95% <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>. Simulations show that if a seller's true success rate was 95%, about 60% of 10-review sequences would still yield 10 out of 10 positive reviews <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.

### The Goal: Maximize Positive Experience

The objective is to maximize the probability of having a positive experience with a seller, despite the uncertainty regarding their true success rate <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>. This requires considering various possible success rates for each seller (any value from 0 to 1) and determining the likelihood of each <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>. This introduces the concept of a [[understanding_probability_of_probabilities | probability of probabilities]], which deals with uncertainty about the long-run frequency of an event, rather than assuming a fixed frequency <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>. This setup is highly relevant to real-world scenarios, such as assessing the error rate of a factory producing cars based on limited test data <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>.

## Understanding P(Data | S): The Binomial Distribution

A key step is to understand how to calculate the probability of observing the given review data (e.g., 10 positive and 0 negative, or 48 positive and 2 negative) if the true success rate (S) were magically known <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>. This is expressed as P(Data | S).

### Simulating the Data

One way to grasp this is through simulation <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>. By repeatedly generating a set number of random reviews (e.g., 50) based on an assumed success rate (e.g., 95%), one can build a histogram to understand the distribution of outcomes <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>. For example, simulating hundreds of thousands of sets of 50 reviews with a 95% success rate shows that approximately 26.1% of them would result in 48 positive reviews out of 50 <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>.

### The Binomial Distribution Formula

Fortunately, there's an exact formula for this: the binomial distribution <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a> <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>. The probability of seeing exactly *k* positive reviews out of *n* total reviews, given a success rate *s*, is <a class="yt-timestamp" data-t="00:06:52">[00:06:52]</a>:

$$P(\text{k successes out of n trials } | s) = \binom{n}{k} s^k (1-s)^{(n-k)}$$

Where:
*   $\binom{n}{k}$ (pronounced "n choose k") represents the total number of ways to arrange *k* successes within *n* trials <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>. For example, 50 choose 48 is 1225 <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>.
*   $s^k$ is the probability of *k* positive reviews <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>.
*   $(1-s)^{(n-k)}$ is the probability of *(n-k)* negative reviews <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>.

This formula relies on the crucial assumption that each review is independent of the last <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>. Using this formula, if the success rate is 95%, the probability of seeing 48 out of 50 reviews is 0.261, matching the simulation <a class="yt-timestamp" data-t="00:07:52">[00:07:52]</a>. The [[probability_density_and_distribution | binomial distribution]] is a fundamental [[probability_and_information_measurement | probability]] distribution, applicable whenever there's a random event with two possible outcomes repeated a fixed number of times <a class="yt-timestamp" data-t="00:08:23">[00:08:23]</a>.

### Analyzing P(Data | S) as a Function of S

By plotting P(Data | S) as a function of *s* (the success rate), for observed data like 48 out of 50 reviews, the curve peaks at *s* = 0.96 (96%) <a class="yt-timestamp" data-t="00:09:19">[00:09:19]</a>. This intuitively makes sense: observing 96% positive reviews is most likely if the true underlying success rate is indeed 96% <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>. The curve approaches zero as *s* approaches 1 (since a perfect success rate would not produce two negative reviews) and also rapidly approaches zero for much lower values of *s* <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>.

However, consider the case of 10 out of 10 positive reviews <a class="yt-timestamp" data-t="00:11:05">[00:11:05]</a>. Here, the binomial formula simplifies to *s*<sup>10</sup> <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>. This function continuously increases as *s* approaches 1, meaning the probability of seeing 10 out of 10 is maximized when the true success rate is 100% <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a>. Yet, intuitively, one wouldn't assume a 100% chance of a good experience with this seller <a class="yt-timestamp" data-t="00:11:32">[00:11:32]</a>.

## Towards P(S | Data): The Need for Bayes' Rule

The binomial distribution provides P(Data | S)—the probability of seeing the data *given* an assumed success rate <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>. However, our ultimate goal is to determine P(S | Data)—the probability of a success rate *given* the fixed data we observe <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>. These are related but distinct <a class="yt-timestamp" data-t="00:08:51">[00:08:51]</a>. While looking for a "center of mass" of these curves is on the right track, accurately translating P(Data | S) into P(S | Data) requires the application of [[understanding_bayes_theorem | Bayes' rule]] and an understanding of [[probability_density_and_distribution | probability density functions]] <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>.