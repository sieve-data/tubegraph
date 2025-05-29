---
title: Modeling probabilities for online seller ratings
videoId: 8idr1WZ1A7Q
---

From: [[3blue1brown]] <br/> 

When shopping online, consumers often face a dilemma: choosing between sellers with varying positive ratings and review counts <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. For example, one seller might have a 100% positive rating from 10 reviews, another 96% from 50 reviews, and a third 93% from 200 reviews <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. While there's an instinct that more data provides greater confidence <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>, quantifying the trade-off between higher percentages and fewer reviews versus lower percentages and more data requires a rational approach <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>. This problem, a slight modification from John Cook's blog post "A Bayesian Review of Amazon Resellers," serves as an excellent case study for [[bayesian_probability_concepts_and_bayes_rule | Bayesian probability concepts]] and statistics <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.

This topic can be broken down into three main parts:
1.  **Setting up a model for the situation**: Focusing on the binomial distribution <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.
2.  **[[bayesian_probability_concepts_and_bayes_rule | Bayesian updating]]**: Working with probabilities over continuous values <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>.
3.  **Beta distribution analysis**: Using Python to optimize choices based on different criteria <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.

## Laplace's Rule of Succession: A Practical Approximation

Before diving into the detailed mathematics, a simple, delightfully elegant answer exists known as Laplace's rule of succession, dating back to the 18th century <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a> <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>.

> [!NOTE] Laplace's Rule
> When seeing an online rating of 'X out of Y' positive reviews, pretend there were two more reviews: one positive and one negative <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>. This adjusted percentage represents your estimated [[understanding_success_rates_and_probability_of_positive_experiences | probability of having a good experience]] with that seller <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.

Applying this rule to the example sellers:
*   **Seller 1 (100% positive, 10 reviews)**: 10 out of 10 becomes 11 out of 12 (10+1 positive, 0+1 negative), which is 91.7% <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.
*   **Seller 2 (96% positive, 50 reviews)**: 48 positive, 2 negative reviews become 49 out of 52 (48+1 positive, 2+1 negative), which is 94.2% <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.
*   **Seller 3 (93% positive, 200 reviews)**: 186 positive, 14 negative reviews become 187 out of 202 (186+1 positive, 14+1 negative), which is 92.6% <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>.

According to Laplace's rule, Seller 2 would be the best choice, offering the highest [[understanding_success_rates_and_probability_of_positive_experiences | probability of having a good experience]] at 94.2% <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>. Understanding the underlying assumptions and when this rule applies requires a deeper dive into the math <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.

## Modeling the Situation and Defining the Goal

The first step in a rational approach is to model the situation <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>. Each seller can be thought of as producing random experiences (positive or negative), with some constant underlying [[understanding_success_rates_and_probability_of_positive_experiences | probability of giving a good experience]], referred to as the "success rate" (S) <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>. The central challenge is that the true success rate (S) is unknown <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.

> [!EXAMPLE]
> A seller with a 100% rating from 10 reviews doesn't mean their true success rate is 100%. It could be 95% <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>. A [[simulation_examples_of_probability_distribution | simulation]] shows that a seller with a 95% success rate will still yield 10 out of 10 positive reviews approximately 60% of the time in sequences of 10 <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a> <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.

The goal is to maximize the [[understanding_success_rates_and_probability_of_positive_experiences | probability of having a positive experience]], despite the uncertainty about the seller's true success rate <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>. This requires thinking about a [[understanding_probability_of_probabilities | probability of probabilities]]: how likely each possible success rate (from 0 to 1) is for a given seller <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>. This differs from simpler probability problems where long-run frequencies are assumed; here, there's uncertainty about the frequency itself <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.

This type of modeling is relevant to many real-world situations, such as judging the quality of a manufacturing process based on limited test data <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>.

## Probability of Seeing Data Given a Success Rate: The Binomial Distribution

A key question is: If you knew the true success rate (e.g., 95%), how would you compute the probability of observing a specific number of positive and negative reviews (e.g., 10 positive, 0 negative; or 48 positive, 2 negative)? <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a> This is the probability of seeing the *data* given an assumed *success rate* <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>.

One approach is through [[simulation_examples_of_probability_distribution | simulation]] <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>. By generating many sets of reviews based on an assumed success rate, a histogram can illustrate the distribution of outcomes <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>. For instance, with a 95% success rate over 50 reviews, a [[simulation_examples_of_probability_distribution | simulation]] might show that 48 out of 50 reviews occur about 26.1% of the time <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>.

Fortunately, there's an exact formula for this: the **binomial distribution** <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a> <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.

> [!FORMULA] Binomial Probability
> For `k` positive reviews out of `n` total reviews, with a success rate `S`:
> $P(\text{k successes out of n trials} | S) = \binom{n}{k} \cdot S^k \cdot (1-S)^{(n-k)}$
>
> Where:
> *   $\binom{n}{k}$ (pronounced "n choose k") is the number of ways to choose `k` successes from `n` trials <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>. For 50 choose 48, this is 1225 ways <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>.
> *   $S^k$ is the probability of `k` positive reviews.
> *   $(1-S)^{(n-k)}$ is the probability of `n-k` negative reviews.
>
> This formula assumes each review is independent <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>. For 48 out of 50 reviews with S=0.95, the calculation yields 0.261, matching the [[simulation_examples_of_probability_distribution | simulation]] <a class="yt-timestamp" data-t="00:07:52">[00:07:52]</a>.

The binomial distribution applies whenever there's a fixed number of independent trials, each with two possible outcomes (like a coin flip), and you want to know the probability of various totals <a class="yt-timestamp" data-t="00:08:23">[00:08:23]</a>.

### Plotting Probability of Data Given Success Rate

By varying the assumed success rate `S` from 0 to 1, we can see how the probability of observing our specific data (e.g., 48 out of 50 reviews) changes <a class="yt-timestamp" data-t="00:08:54">[00:08:54]</a>.

For 48 out of 50 reviews, the probability of seeing this data is highest when `S` is 0.96 <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a>. This makes intuitive sense: the observed rating is most likely if the true underlying success rate matches it <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>. The probability approaches zero as `S` approaches 1 (a perfect success rate would never yield negative reviews) or as `S` approaches 0 (very low success rates would rarely yield many positive reviews) <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>.

The general form of this curve, as a function of the success rate `S`, looks like:
$P(\text{Data} | S) \propto S^{\text{positive reviews}} \cdot (1-S)^{\text{negative reviews}}$ <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>

If more data were available, such as 480 positive and 20 negative reviews (still 96% positive), the resulting plot would still be centered around 0.96, but it would be narrower and more concentrated, reflecting increased confidence in the true success rate <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>.

## Next Steps: From Data to Success Rate

While the binomial distribution helps compute the probability of seeing data *given* a success rate, our ultimate goal is to infer the [[understanding_success_rates_and_probability_of_positive_experiences | probability of a success rate]] *given* the data we've observed <a class="yt-timestamp" data-t="00:11:51">[00:11:51]</a>.

It's tempting to assume the most likely success rate is simply the observed percentage (e.g., 96% for 48/50 reviews) <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>. However, consider the 10 out of 10 positive reviews example. The binomial formula simplifies to $S^{10}$ <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>. This function continuously increases as S approaches 1. While S=1 maximizes the probability of seeing 10/10, it's unrealistic to conclude a 100% chance of a good experience <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a>.

To properly infer the unknown success rate from the observed data, it's necessary to explore [[bayesian_probability_concepts_and_bayes_rule | Bayes' rule]] and [[probability_density_and_distribution | probability density functions]], which will be covered in the next part <a class="yt-timestamp" data-t="00:11:51">[00:11:51]</a>.