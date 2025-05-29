---
title: The impact of pricing strategies on consumer behavior
videoId: xkx1tXLAP-o
---

From: [[causalpython]] <br/> 

Pricing strategies, such as discounts, promotions, and coupons, are a key component of e-commerce platforms. Their goal is to influence customer behavior and expand the customer base by offering increased value <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>. In the travel industry, people are notably driven by price differences <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>.

## Causal Inference in Pricing Decisions

Traditional recommended systems often operate as predictive or associative devices <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>. However, when applying these systems in real-world business scenarios, particularly with pricing, it becomes crucial to incorporate [[causal_inference_in_business_decisions_at_spotify | causal inference]] <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>. While a well-built recommender might improve accuracy, it may not incrementally impact key metrics because it might just shift traffic or recommend something the user would have found anyway <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.

The focus shifts to understanding how to introduce a "change treatment" that makes customers behave differently than they would otherwise <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>. This means thinking in terms of [[causal_analysis_and_decision_making | counterfactual outcomes]] – what would happen *with* and *without* the treatment <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.

## The Strategy of Discounts

Discounts are a powerful tool to change customer behavior, increase volumes, and extend the customer base <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>. However, they come with a significant cost; companies cannot offer discounts indiscriminately without losing money <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>.

The key challenge is to selectively apply discounts to customers whose behavior will be positively influenced, rather than to those who would have booked anyway <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>. This aligns with a trigger-cost model, where the cost is incurred only if the customer makes a booking due to the offer <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>.

### Budget Constraints and Optimization

Companies often operate under fixed budget constraints for promotions <a class="yt-timestamp" data-t="00:10:25">[00:10:25]</a>. The goal is to maximize incremental volumes (new customers, new reservations) while controlling incremental cost, ensuring the budget is not exceeded and the return on investment (ROI) remains above a threshold <a class="yt-timestamp" data-t="00:11:22">[00:11:22]</a>. This creates a two-dimensional optimization problem, resembling a knapsack problem, where the challenge is to pick the right "items" (customers to offer discounts to) within a capacity budget constraint <a class="yt-timestamp" data-t="00:12:36">[00:12:36]</a>.

This problem combines [[causal_analysis_and_decision_making | causal inference]] with optimization, two distinct fields that come together in a practical application <a class="yt-timestamp" data-t="00:12:48">[00:12:48]</a>.

## Challenges and Learnings in Implementation

Implementing [[application_of_causal_ai_in_marketing_and_business | causal AI in marketing and business]] for pricing strategies presents several challenges:

*   **Noisy Data and Overfitting:** Real-world data is noisy, affected by seasonality, and prone to overfitting <a class="yt-timestamp" data-t="00:14:28">[00:14:28]</a>.
*   **Evolving Problems:** Business needs and constraints are dynamic, constantly evolving and requiring continuous adaptation rather than a one-time solution <a class="yt-timestamp" data-t="00:15:39">[00:15:39]</a>.
*   **Dynamic Environment:** Pricing environments are highly dynamic, necessitating continuous monitoring and comparison to holdout groups rather than a "ship and forget" approach <a class="yt-timestamp" data-t="00:16:26">[00:16:26]</a>.
*   **Misparity between Online and Offline:** Models that perform well in offline evaluations (e.g., uplift models with good uplift curves) may not translate directly to positive online results <a class="yt-timestamp" data-t="00:17:40">[00:17:40]</a>. Aligning metrics and data collection processes between online and offline environments is crucial <a class="yt-timestamp" data-t="00:18:40">[00:18:40]</a>.
*   **Cost of Online Testing:** Testing pricing models online can be costly due to potential financial losses from suboptimal discount allocation <a class="yt-timestamp" data-t="00:18:00">[00:18:00]</a>.

Strategies for success include:
*   **Continuous Experimentation:** Running tests continuously to monitor the gap between treatments and react to changes <a class="yt-timestamp" data-t="00:19:34">[00:19:34]</a>.
*   **Robust Solutions:** Building a portfolio of diverse strategies rather than relying on a single optimal one, ensuring some methods always work <a class="yt-timestamp" data-t="00:20:01">[00:20:01]</a>.
*   **Simplicity:** Sticking to simpler models and solutions, as complex models with many features are harder to deploy and maintain, and are more susceptible to overfitting and data drift <a class="yt-timestamp" data-t="00:20:30">[00:20:30]</a>.

## The Role of [[psychology_and_user_behavior_in_recommendation_systems | Human Psychology]]

Pricing strategies are deeply intertwined with [[psychology_and_user_behavior_in_recommendation_systems | human psychology]]. Customer decisions are not always rational <a class="yt-timestamp" data-t="00:30:14">[00:30:14]</a>. For example, recommending a three-night stay in Paris might display a high price, which could deter a customer. However, recommending a one-night stay, even if less typical, displays a much cheaper price and encourages them to continue browsing for properties, ultimately leading to a booking <a class="yt-timestamp" data-t="00:29:01">[00:29:01]</a>. The most accurate recommendation is not always the most effective <a class="yt-timestamp" data-t="00:30:19">[00:30:19]</a>.

Human behavior is often counterintuitive and inconsistent <a class="yt-timestamp" data-t="00:31:20">[00:31:20]</a>. A strategy that works well on one platform (e.g., laptop) might yield inverse results on another (e.g., mobile app) <a class="yt-timestamp" data-t="00:32:31">[00:32:31]</a>. Different countries or even the same person at different times may react differently <a class="yt-timestamp" data-t="00:32:54">[00:32:54]</a>. This highlights the limitations of AB tests regarding external validity; an effect shown in one environment doesn't automatically translate to another <a class="yt-timestamp" data-t="00:34:24">[00:34:24]</a>.

Understanding what truly drives people towards a desired action often requires user research and interviews, but even then, customers may not consciously know or confess their irrational decision-making processes <a class="yt-timestamp" data-t="00:30:50">[00:30:50]</a>. Experiments can uncover these patterns, sometimes revealing surprising "hacks" into human behavior <a class="yt-timestamp" data-t="00:31:07">[00:31:07]</a>.

> [!NOTE] Practical Application of Causality
> The beauty of [[causal_analysis_and_decision_making | causality]] lies in forming a hypothesis and then testing it against the real world <a class="yt-timestamp" data-t="00:29:48">[00:29:48]</a>. This allows for validation of unexpected behaviors and continuous learning <a class="yt-timestamp" data-t="00:31:04">[00:31:04]</a>.

## Communication with Business Stakeholders

For technical teams working on pricing models, understanding the expected impact of their work is paramount <a class="yt-timestamp" data-t="00:24:14">[00:24:14]</a>. The focus should not just be on optimizing algorithm accuracy (e.g., recognizing objects in images), but on how the solution will be used, deployed, and its real-world effect on business needs and customer value <a class="yt-timestamp" data-t="00:24:45">[00:24:45]</a>.

> [!TIP] Advice for Technical People
> Don't "fall in love" with complex technical solutions or fancy machine learning <a class="yt-timestamp" data-t="00:26:56">[00:26:56]</a>. Often, the simplest baseline solution can have a huge impact <a class="yt-timestamp" data-t="00:27:06">[00:27:06]</a>. The goal is to move the needle and generate business impact, not necessarily to deploy the most sophisticated model <a class="yt-timestamp" data-t="00:53:01">[00:53:01]</a>.

A "portfolio approach" with diverse strategies can provide robustness, ensuring that if one method breaks, others are still available <a class="yt-timestamp" data-t="00:20:01">[00:20:01]</a>.

## Evolution and Continuous Learning

The process of designing and implementing pricing strategies, much like designing a game, is iterative. Start with a simple solution, learn from its performance, and gradually introduce more complexity and levers (e.g., type of promotion, discount levels, timing, specific items) <a class="yt-timestamp" data-t="00:47:11">[00:47:11]</a>.

> [!INFO] Key Takeaway
> In [[challenges_and_strategies_in_credit_decisionmaking | applied machine learning]], especially concerning pricing, understanding the customer and ensuring consistent and correlated evaluation metrics are fundamental <a class="yt-timestamp" data-t="00:54:39">[00:54:39]</a>. This foundation makes it clearer what needs improvement and guides solution development <a class="yt-timestamp" data-t="00:55:01">[00:55:01]</a>.