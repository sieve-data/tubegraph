---
title: Online seller ratings and decisionmaking
videoId: 8idr1WZ1A7Q
---

From: [[3blue1brown]] <br/> 

When purchasing products online, consumers often face a dilemma: choosing among multiple sellers offering the same product at similar prices, but with varying review counts and positive ratings <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. For instance, one seller might have a 100% positive rating from 10 reviews, another 96% from 50 reviews, and a third 93% from 200 reviews <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. The challenge is to quantitatively determine the most rational choice, balancing the confidence gained from more data against a lower absolute percentage <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.

This problem is a modification of an example from John Cook's blog post, "A Bayesian Review of Amazon Resellers," and serves as an excellent case study for [[human_judgment_and_probability_misconceptions | core topics in probability and statistics]] <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.

## A Quick Solution: Laplace's Rule of Succession

Before delving into the underlying mathematics, one simple and "delightfully simple" answer to this problem is given by **Laplace's rule of succession** <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>. This rule suggests that for any online rating (e.g., 10 positive reviews out of 10 total), one should "pretend" that there were two additional reviews: one positive and one negative <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.

Applying this rule to the given examples:
*   For the seller with 10 out of 10 positive reviews: Pretend it's 11 out of 12, yielding a 91.7% probability of a good experience <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.
*   For the seller with 48 out of 50 positive reviews (96%): Pretend it's 49 out of 52, yielding 94.2% <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.
*   For the seller with 186 out of 200 positive reviews (93%): Pretend it's 187 out of 202, yielding 92.6% <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>.

According to this rule, the best option is to choose seller number 2, with an adjusted 94.2% probability <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>. This rule dates back to the 18th century <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>. However, understanding the assumptions behind it and how different goals might change the outcome requires a deeper dive into the mathematics <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.

## Modeling the Situation

To model this scenario, each seller can be thought of as producing random experiences that are either positive or negative <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>. Each seller possesses an underlying constant probability of giving a good experience, referred to as their "success rate" (S) <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>. The central [[challenges_in_assessing_problem_difficulty | challenge]] is that this true success rate (S) is unknown <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.

For example, a seller with a 100% positive rating from 10 reviews does not necessarily have a 100% success rate <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>. It could be 95%, and a simulation shows that about 60% of sellers with a true 95% success rate would still yield 10 out of 10 positive reviews in a sample of 10 <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>. The objective is to maximize one's probability of having a positive experience despite this uncertainty about S <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.

This problem involves an uncertainty about the "long run frequency" itself, unlike typical probability problems where such frequencies are assumed (e.g., a fair coin is 0.5) <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>. This kind of setup is relevant to many real-world situations where judgments about a random process must be made from [[modeling_probabilities_based_on_limited_data | limited data]], such as estimating car defect rates in a factory based on initial tests <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>.

## Probability of Data Given Success Rate (Binomial Distribution)

To begin, consider how one would compute the probability of seeing a specific number of positive and negative reviews if the true success rate (S) for a seller were known <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.

This can be explored through simulation <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>. For example, by repeatedly generating 50 random reviews assuming a 95% success rate, one can build a histogram to see the distribution of positive outcomes <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>. Empirically, with a 95% success rate, about 26.1% of 50-review samples would show 48 positive reviews <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>.

### The Binomial Distribution Formula

Luckily, an exact formula exists for this calculation. The probability of seeing exactly *k* positive reviews out of *n* total reviews, given a success rate *S*, is defined by the [[binomial_distribution | binomial distribution]] formula <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>:

$P(\text{k successes out of n trials} | S) = \binom{n}{k} * S^k * (1-S)^{(n-k)}$

Where:
*   $\binom{n}{k}$ (pronounced "n choose k") represents the total number of ways to choose *k* successes out of *n* trials <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>. For example, 50 choose 48 is 1225 <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>.
*   $S^k$ is the probability of *k* positive reviews <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>.
*   $(1-S)^{(n-k)}$ is the probability of *(n-k)* negative reviews <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>.

This formula assumes each review is independent <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>. Using this, the probability of 48 out of 50 positive reviews with S=0.95 is indeed 0.261, matching simulations <a class="yt-timestamp" data-t="00:07:52">[00:07:52]</a>.

The [[binomial_distribution | binomial distribution]] is fundamental in probability, used whenever there are repeated independent events with two possible outcomes (like coin flips), and the goal is to find the probability of various total outcomes <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.

## Relating Data to Plausible Success Rates

While the [[binomial_distribution | binomial distribution]] tells us the probability of seeing the data *given* an assumed success rate ($P(\text{Data} | S)$), our actual goal is to make judgments about the opposite: the probability of a success rate *given* the fixed data we observe ($P(S | \text{Data})$) <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>. These are related but distinct <a class="yt-timestamp" data-t="00:08:51">[00:08:51]</a>.

By plotting $P(\text{Data} | S)$ as a function of *S* for the 48 out of 50 reviews example, the curve peaks when S is 0.96 <a class="yt-timestamp" data-t="00:09:19">[00:09:19]</a>. This intuitively makes sense: the observed 96% positive rating is most likely if the true underlying success rate was 96% <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>.

However, consider the 10 out of 10 positive reviews example. The binomial formula simplifies to $S^{10}$ <a class="yt-timestamp" data-t="00:11:05">[00:11:05]</a>. The probability of seeing 10 consecutive good reviews increases as *S* approaches 1 <a class="yt-timestamp" data-t="00:11:15">[00:11:15]</a>. While S=1 maximizes $P(\text{Data} | S)$, it doesn't mean a consumer would feel 100% certain of a good experience with that seller <a class="yt-timestamp" data-t="00:11:32">[00:11:32]</a>.

To bridge the gap between $P(\text{Data} | S)$ and $P(S | \text{Data})$, and to find a "center of mass" for these curves, the concepts of Bayes' rule and probability density functions are necessary <a class="yt-timestamp" data-t="00:11:51">[00:11:51]</a>.