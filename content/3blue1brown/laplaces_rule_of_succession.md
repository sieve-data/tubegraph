---
title: Laplaces rule of succession
videoId: 8idr1WZ1A7Q
---

From: [[3blue1brown]] <br/> 

When evaluating online seller ratings, a common problem is balancing high positive percentages with low review counts against lower percentages with many reviews <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. This dilemma highlights an intuitive suspicion of 100% ratings from a small number of reviews, as it feels more plausible that outcomes could have varied, leading to a lower rating <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>. [[leonhard_eulers_role_in_mathematical_constants | John Cook's]] blog post, "A Bayesian Review of Amazon Resellers," provides a modification of an example used to explore this challenge <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.

## The Rule

One delightfully simple answer to this problem is known as Laplace's rule of succession, which dates back to the 18th century <a class="yt-timestamp" data-t="02:39:00">[02:39:00]</a>.

> [!INFO] Laplace's Rule of Succession
> When you see an online rating, such as 10 positive reviews out of 10 total reviews, you **pretend** that there were two additional reviews: one positive and one negative <a class="yt-timestamp" data-t="01:50:00">[01:50:00]</a>. This adjusted percentage represents your probability of having a good experience with that seller <a class="yt-timestamp" data-t="02:01:00">[02:01:00]</a>.

## Application Examples

Let's apply this rule to the example of three online sellers:

*   **Seller 1:** 100% positive rating with 10 reviews (10 out of 10) <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>.
    *   Applying the rule: Pretend it's 11 positive reviews out of 12 total reviews (10+1 positive, 0+1 negative) <a class="yt-timestamp" data-t="01:50:00">[01:50:00]</a>.
    *   Resulting probability: 11/12 = 91.7% <a class="yt-timestamp" data-t="01:55:00">[01:55:00]</a>.

*   **Seller 2:** 96% positive rating with 50 reviews (48 positive, 2 negative) <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.
    *   Applying the rule: Pretend it's 49 positive reviews out of 52 total reviews (48+1 positive, 2+1 negative) <a class="yt-timestamp" data-t="02:08:00">[02:08:00]</a>.
    *   Resulting probability: 49/52 = 94.2% <a class="yt-timestamp" data-t="02:13:00">[02:13:00]</a>.

*   **Seller 3:** 93% positive rating with 200 reviews (186 positive, 14 negative) <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>.
    *   Applying the rule: Pretend it's 187 positive reviews out of 202 total reviews (186+1 positive, 14+1 negative) <a class="yt-timestamp" data-t="02:25:00">[02:25:00]</a>.
    *   Resulting probability: 187/202 = 92.6% <a class="yt-timestamp" data-t="02:30:00">[02:30:00]</a>.

Based on Laplace's rule, the best option for the consumer would be to choose Seller 2, as they offer the highest probability of a good experience (94.2%) among the three <a class="yt-timestamp" data-t="02:34:00">[02:34:00]</a>.

## Underlying Assumptions

While simple and intuitive, understanding the assumptions underlying Laplace's rule of succession is crucial, as changing these assumptions or the goal can alter the resulting decision <a class="yt-timestamp" data-t="02:42:00">[02:42:00]</a>. The full mathematical exploration of this problem involves modeling each seller as having a constant underlying "success rate" (S) for producing good experiences, where the challenge lies in not knowing this true rate <a class="yt-timestamp" data-t="03:06:00">[03:06:00]</a>.

Further analysis involves topics such as:
*   The binomial distribution, used to calculate the probability of seeing observed data (e.g., 48 positive reviews out of 50) given an assumed success rate <a class="yt-timestamp" data-t="01:17:00">[01:17:00]</a>.
*   Bayesian updating, which helps determine the probability of a success rate given the observed data <a class="yt-timestamp" data-t="01:19:00">[01:19:00]</a>.
*   Probability density functions <a class="yt-timestamp" data-t="01:23:00">[01:23:00]</a>.
*   The Beta distribution, which can be used to analyze such data and optimize for different goals <a class="yt-timestamp" data-t="01:27:00">[01:27:00]</a>.