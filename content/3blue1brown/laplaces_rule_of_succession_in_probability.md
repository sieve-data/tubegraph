---
title: Laplaces rule of succession in probability
videoId: 8idr1WZ1A7Q
---

From: [[3blue1brown]] <br/> 

When evaluating online products with varying seller ratings and review counts, a common challenge is deciding which seller to trust <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. For instance:
*   Seller 1: 100% positive rating, 10 reviews <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>
*   Seller 2: 96% positive rating, 50 reviews <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>
*   Seller 3: 93% positive rating, 200 reviews <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>

There's an intuitive sense that more data provides greater confidence, even if the absolute percentage is slightly lower <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>. The goal is to quantify this intuition and rationally reason about the trade-off between confidence from data and the reported percentage <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. This problem is a modification of an example given by John Cook in his blog post, "A [[bayesian_probability_concepts_and_bayes_rule | Bayesian]] Review of Amazon Resellers" <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.

## Introducing Laplace's Rule of Succession

One simple and "delightfully simple" answer to this problem is provided by Laplace's Rule of Succession <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>, <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>. This rule dates back to the 18th century <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.

### How it Works

When applying Laplace's Rule to an online rating, you "pretend that there were two more reviews, one that was positive and one that's negative" <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>. The resulting percentage is then considered your probability of having a good experience with that seller <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.

### Examples

Let's apply this rule to the online seller scenarios:

*   **Seller 1:**
    *   Original rating: 10 out of 10 positive reviews (100%) <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>.
    *   Applying the rule: Pretend it's 11 positive reviews and 1 negative review, out of 12 total <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.
    *   Resulting probability: 11/12 = 91.7% <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.

*   **Seller 2:**
    *   Original rating: 96% positive with 50 total reviews (48 positive, 2 negative) <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>, <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.
    *   Applying the rule: Pretend it's 49 positive reviews and 3 negative reviews, out of 52 total <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>.
    *   Resulting probability: 49/52 = 94.2% <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.

*   **Seller 3:**
    *   Original rating: 93% positive with 200 total reviews (186 positive, 14 negative) <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>.
    *   Applying the rule: Pretend it's 187 positive reviews and 15 negative reviews, out of 202 total <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.
    *   Resulting probability: 187/202 = 92.6% <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.

According to Laplace's Rule of Succession, Seller 2, with an adjusted probability of 94.2%, would be the best choice among the three <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>.

## Limitations and Further Exploration

While simple, understanding the assumptions underlying Laplace's rule and how changing those assumptions or your optimization goal might change the choice requires deeper mathematical analysis <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>, <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.

The problem models each seller as having a constant underlying success rate (S) for good experiences, which is unknown <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>. For example, a 100% positive rating from 10 reviews doesn't guarantee a 100% success rate; it could be 95%, and a simulation shows that even a 95% success rate yields 10 out of 10 positives about 60% of the time in sequences of 10 reviews <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>, <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.

The challenge is to find the most likely success rate for each seller, essentially dealing with a "probability of probabilities" <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>. This differs from typical probability problems where the long-run frequency is assumed (e.g., 1/2 for a coin flip) <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.

The problem can be explored further using concepts such as the binomial distribution to calculate the probability of seeing the observed data given an assumed success rate <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>, and later [[bayesian_probability_concepts_and_bayes_rule | Bayes' rule]] and [[continuous_values_and_probability_paradox | probability density functions]] to infer the probability of a success rate given the data <a class="yt-timestamp" data-t="00:11:55">[00:11:55]</a>.