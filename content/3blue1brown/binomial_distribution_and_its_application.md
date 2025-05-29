---
title: Binomial distribution and its application
videoId: 8idr1WZ1A7Q
---

From: [[3blue1brown]] <br/> 

When evaluating online sellers based on their positive ratings and total reviews, a common intuition is that more data provides greater confidence in a given rating <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>. For example, a 100% positive rating with only 10 reviews feels less reliable than a 96% positive rating with 50 reviews, or even a 93% positive rating with 200 reviews <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. The challenge is to quantify this intuition and rationally assess the trade-off between confidence gained from more data and a lower absolute percentage <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.

This problem is a modification of an example by John Cook in his blog post, "A Bayesian Review of Amazon Resellers" <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. It provides a practical context to delve into core topics in [[probability_density_and_distribution | probability]] and statistics <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.

## Modeling the Situation

To model this scenario, each seller is considered to produce random experiences that are either positive or negative <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>. Each seller is assumed to have a constant underlying "success rate" (S) for giving a good experience <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>. The core challenge lies in the fact that this true success rate (S) is unknown <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.

For instance, a 100% positive rating from 10 reviews does not guarantee a true success rate of 100%; it could be 95% <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>. [[simulation_examples_of_probability_distribution | Simulations]] demonstrate that even with a 95% true success rate, approximately 60% of 10-review sequences would result in 10 out of 10 positive reviews <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>. The objective is to maximize the probability of having a positive experience, despite this uncertainty about the true success rate <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>. This requires reasoning about a "probability of probabilities" for various possible success rates between 0 and 1 <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>.

This setup is relevant to many real-world situations where judgments must be made about a random process based on limited data, such as estimating car defect rates in a factory based on initial tests <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>.

## Probability of Data Given Success Rate

A fundamental question is: If the true success rate for a seller were known (e.g., 95%), how would one compute the probability of observing specific review data (e.g., 10 positive and 0 negative, or 48 positive and 2 negative)? <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>

While [[simulation_examples_of_probability_distribution | simulations]] can give an empirical sense of this [[probability_density_and_distribution | distribution]] <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>, an exact formula exists <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>.

Consider the example of 48 positive reviews out of 50, with an assumed success rate (S) of 95% <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>. The probability is calculated as:

`P(48 positive out of 50 | S=0.95) = (50 choose 48) * S^48 * (1-S)^2` <a class="yt-timestamp" data-t="00:06:52">[00:06:52]</a>

Where:
*   `(50 choose 48)` represents the total number of ways to have 48 positive reviews out of 50 <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>. This calculates to 1225 <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>.
*   `S^48` is the probability of 48 positive reviews.
*   `(1-S)^2` is the probability of 2 negative reviews.

This formula assumes each review is independent <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>. For S=0.95, this calculation yields approximately 0.261 (26.1%), matching [[simulation_examples_of_probability_distribution | empirical simulations]] <a class="yt-timestamp" data-t="00:07:52">[00:07:52]</a>.

### The Binomial Distribution

The distribution described above is known as the **binomial distribution** <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>. It is a fundamental distribution in [[probability_density_and_distribution | probability]] that applies when:
*   There's a random event with two possible outcomes (like a coin flip or a review being positive/negative) <a class="yt-timestamp" data-t="00:08:23">[00:08:23]</a>.
*   The event is repeated a fixed number of times <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>.
*   The goal is to find the probability of various total counts for one of the outcomes <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>.

As a function of the success rate `S`, the probability curve for `k` positive reviews out of `n` total reviews takes the form: `Constant * S^k * (1-S)^(n-k)` <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>.

For 48 positive reviews out of 50, the probability of seeing this data peaks when the assumed success rate `S` is 0.96 (or 96%) <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a>. This intuitively makes sense, as the observed rating is 96% <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>. If `S` approaches 1, the probability of observing two negative reviews goes to zero <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>. Similarly, if `S` is very low (e.g., 0.8), getting 48 out of 50 positive reviews becomes exceedingly rare (1 in 1000 times) <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>.

### The Challenge of Interpretation

While this formula gives the probability of seeing the data *given* an assumed success rate, the ultimate goal is to determine the probability of a success rate *given* the fixed data observed <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>. These are related but distinct concepts <a class="yt-timestamp" data-t="00:08:51">[00:08:51]</a>.

For instance, with 10 out of 10 positive reviews, the binomial formula simplifies to `S^10` <a class="yt-timestamp" data-t="00:11:05">[00:11:05]</a>. This function continuously increases as `S` approaches 1 <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a>. Even if `S=1` maximizes this probability, it doesn't mean one can confidently say there's a 100% probability of a good experience <a class="yt-timestamp" data-t="00:11:32">[00:11:32]</a>.

To bridge this gap and get to the probability of `S` given the data, concepts like [[bayesian_probability_concepts_and_bayes_rule | Bayes' Rule]] and [[probability_density_and_distribution | probability density functions]] are necessary <a class="yt-timestamp" data-t="00:11:51">[00:11:51]</a>.

### Laplace's Rule of Succession

As a simplified practical rule, known as **Laplace's rule of succession** (dating back to the 18th century), one can estimate the probability of a good experience by pretending there were two more reviews: one positive and one negative <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.

For the initial examples:
*   **Seller 1 (10 out of 10 reviews)**: Pretend 11 out of 12 reviews, yielding 91.7% <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.
*   **Seller 2 (48 out of 50 reviews)**: Pretend 49 out of 52 reviews, yielding 94.2% <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.
*   **Seller 3 (186 out of 200 reviews)**: Pretend 187 out of 202 reviews, yielding 92.6% <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>.

According to this rule, Seller 2 would be the best choice <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>. Understanding the underlying assumptions and how different goals can change this choice requires further mathematical exploration <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.