---
title: Introduction to Bayesian statistics
videoId: 8idr1WZ1A7Q
---

From: [[3blue1brown]] <br/> 

When buying a product online, faced with multiple sellers offering the same item at a similar price but with varying positive ratings and review counts, a common intuition suggests that more data provides greater confidence in a given rating <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. For instance, a seller with a 100% positive rating from only 10 reviews might be viewed with more suspicion than one with a 96% rating from 50 reviews, or even a 93% rating from 200 reviews <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. The core challenge is how to quantify this intuition and rationally weigh the confidence gained from more data against a lower absolute percentage <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.

This problem, a modification of an example from John Cook's blog post "A Bayesian Review of Amazon Resellers," serves as an excellent case study for exploring core topics in probability and statistics <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.

## Modeling the Situation

To address this problem, each seller can be modeled as having a constant underlying probability of providing a good experience, referred to as their "success rate" (S) <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>. The main challenge is that this true success rate (S) is unknown <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>. For example, a 100% positive rating from 10 reviews does not guarantee a 100% underlying success rate; it could plausibly be 95% <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.

The objective is to maximize the probability of having a positive experience, despite the uncertainty surrounding the true success rate <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>. This involves considering a "probability of probabilities" – assessing how likely each possible success rate (from 0 to 1) is for a given seller <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>. This differs from typical introductory probability problems where long-run frequencies are often assumed; here, the uncertainty lies in the long-run frequency itself <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>. This setup is highly relevant to real-world scenarios where judgments about random processes must be made from limited data, such as estimating car defect rates in a factory based on initial tests <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>.

## Calculating the Probability of Observed Data

A crucial first step is to compute the probability of observing the specific review data (e.g., 10 positive and 0 negative, or 48 positive and 2 negative) given an assumed success rate (S) <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>. This is represented by P(Data|S).

This calculation involves the [[Binomial distribution concept and calculation | Binomial distribution]], which is fundamental in probability and applies whenever there are independent random events with two possible outcomes (like a coin flip or a review being positive/negative) repeated a certain number of times <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.

For example, the probability of seeing exactly 48 positive reviews out of 50, assuming a success rate S, is given by the formula:

$$
P(\text{48 positive, 2 negative | S}) = \binom{50}{48} \cdot S^{48} \cdot (1-S)^2
$$
<a class="yt-timestamp" data-t="00:06:52">[00:06:52]</a>

Here:
*   $\binom{50}{48}$ (pronounced "50 choose 48") represents the total number of distinct ways to arrange 48 positive reviews and 2 negative reviews within a sequence of 50 reviews. In this case, it equals 1225 <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>.
*   $S^{48}$ is the probability of 48 positive outcomes.
*   $(1-S)^2$ is the probability of 2 negative outcomes.

This formula assumes each review is independent of the last <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>. For an assumed success rate of 95% (S=0.95), this calculation yields approximately 0.261 (26.1%) for 48 out of 50 reviews, which matches empirical simulations <a class="yt-timestamp" data-t="00:07:52">[00:07:52]</a>.

The [[Binomial distribution concept and calculation | binomial distribution]] shows that the probability of observing 48 out of 50 reviews peaks when the assumed success rate (S) is 0.96 (96%), which makes intuitive sense as it matches the observed rating <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>.

However, for a perfect 10 out of 10 rating, the formula simplifies to $S^{10}$ <a class="yt-timestamp" data-t="00:11:05">[00:11:05]</a>. This means the probability of seeing 10 out of 10 increases as S approaches 1. While S=1 maximizes this probability, it is generally not reasonable to conclude a 100% probability of a good experience with that seller <a class="yt-timestamp" data-t="00:11:27">[00:11:27]</a>.

## From Data to Underlying Probability

The ultimate goal is to move from the probability of seeing the data given an assumed success rate, P(Data|S), to the probability of a success rate given the observed data, P(S|Data) <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>. This is where [[Bayes theorem and its significance | Bayes' rule]] becomes essential, along with concepts of [[applications_of_probability_density | probability density functions]] for continuous values of S <a class="yt-timestamp" data-t="00:11:51">[00:11:51]</a>.

### Laplace's Rule of Succession

As a preliminary answer, [[Laplace's rule of succession]], an 18th-century concept, offers a delightfully simple heuristic <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>:

*   **For 10 out of 10 reviews:** Pretend there were two additional reviews, one positive and one negative. This converts 10/10 to 11/12, or approximately 91.7% <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>. This adjusted percentage represents the probability of a good experience with that seller.
*   **For 48 out of 50 reviews:** Similarly, pretend it's 49 positive and 3 negative, yielding 49/52 or 94.2% <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.
*   **For 186 out of 200 reviews:** This becomes 187 out of 202, or 92.6% <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>.

According to this rule, the second seller (48/50 reviews adjusted to 94.2%) would be the best choice <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>. Understanding the underlying assumptions and how different goals might change this choice requires a deeper dive into [[Bayesian updating]] and [[probability of a probability | probability over continuous values]], including concepts like the Beta distribution <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>.