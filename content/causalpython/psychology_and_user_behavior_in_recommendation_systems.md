---
title: Psychology and user behavior in recommendation systems
videoId: xkx1tXLAP-o
---

From: [[causalpython]] <br/> 

In the realm of machine learning, particularly with recommendation systems, the focus is often on predicting what users might like or do based on historical data. However, the true impact of recommendations extends beyond mere prediction, delving into the intricacies of human psychology and behavior to drive desired outcomes. This shift from purely predictive models to those informed by [[causal_inference_in_personalized_recommendations | causal inference]] is crucial for platforms aiming to influence user actions meaningfully <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>.

## Shifting from Predictive to Causal Recommenders

Traditionally, recommended systems are taught as predictive or associative devices, aiming to identify the most suitable item or recommendation for a user based on correlations <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>, <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>. While these models can achieve high accuracy in offline metrics, they often fail to "move the needle" in real-world application <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>. This is because merely recommending what a user would have found anyway, or shifting traffic from one part of the website to another, doesn't create incremental value <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.

The goal shifts to understanding how to introduce a "change treatment" that incentivizes customers to do something different from what they would have done without the intervention <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>. This involves:
*   **Thinking counterfactually** about what would happen with and without a specific recommendation <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>, <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.
*   **Framing recommendations** in terms of user experience, copywriting, and timing to elicit a different reaction <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.
*   **Focusing on innovation** rather than just popularity, recommending something trending or incentivizing a change in behavior <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.

Even if a recommendation is highly relevant, it might not be enough to truly change customer behavior <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>. The objective becomes influencing the outcome between different scenarios, rather than just predicting a likely action <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>.

## The Role of Pricing and Discounts

One of the most impactful strategies observed in the travel industry is the use of pricing, discounts, and promotions <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>. These can significantly change customer behavior, often proving more beneficial than simple relevance in incentivizing bookings <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>. However, this strategy comes with a cost: giving discounts to everyone can lead to financial losses <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>.

To optimize this, it's essential to:
*   Understand the **counterfactual problem** of whether a customer would have booked anyway without the discount <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>. Discounts should primarily be given when they change behavior positively <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>.
*   Consider the **trigger cost** associated with discounts, which only occurs if the customer accepts the offer and books <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>.
*   Operate under **budget constraints** to ensure profitability while maximizing incremental volumes <a class="yt-timestamp" data-t="00:10:25">[00:10:25]</a>, <a class="yt-timestamp" data-t="00:11:22">[00:11:22]</a>. This transforms the problem into a type of [[machine_learning_and_treatment_effect_estimation | Knapsack problem]] where incremental value and cost must be balanced <a class="yt-timestamp" data-t="00:12:36">[00:12:36]</a>.

## Understanding Human Psychology: Inconsistency and Irrationality

One of the most surprising findings about human psychology in this work is its **inconsistency** <a class="yt-timestamp" data-t="00:32:10">[00:32:10]</a>. An experiment that works well on one platform (e.g., laptop) might yield inverse results on another (e.g., mobile app) <a class="yt-timestamp" data-t="00:32:31">[00:32:31]</a>. User reactions can also differ by country or even for the same person over time <a class="yt-timestamp" data-t="00:32:54">[00:32:54]</a>. This highlights that external validity cannot be taken for granted in [[experiments_and_ab_testing_in_machine_learning | AB tests]] <a class="yt-timestamp" data-t="00:34:24">[00:34:24]</a>.

Humans are not always rational <a class="yt-timestamp" data-t="00:30:14">[00:30:14]</a>. For instance, recommending a three-night stay in Paris, while statistically more common, might show a higher price and less availability, potentially scaring customers away <a class="yt-timestamp" data-t="00:29:01">[00:29:01]</a>. Recommending a single night, though less accurate to the average stay, presents a cheaper price and more availability, encouraging continued engagement <a class="yt-timestamp" data-t="00:29:09">[00:29:09]</a>. This counterintuitive behavior demonstrates that the "most accurate" answer isn't always the "right" one for driving desired actions <a class="yt-timestamp" data-t="00:29:34">[00:29:34]</a>.

Understanding what drives people to a desired action often requires combining user interviews and UX research with data analysis <a class="yt-timestamp" data-t="00:30:50">[00:30:50]</a>. The beauty of running experiments is uncovering these counterintuitive patterns in behavior <a class="yt-timestamp" data-t="00:31:07">[00:31:07]</a>.

## Challenges and Strategies in Model Evaluation

Online evaluation of models, especially those involving [[the_impact_of_pricing_strategies_on_consumer_behavior | pricing strategies]], is dynamic and costly if done incorrectly <a class="yt-timestamp" data-t="00:16:26">[00:16:26]</a>, <a class="yt-timestamp" data-t="00:18:00">[00:18:00]</a>. Key strategies for effective online evaluation and learning include:
1.  **Aligning Metrics and Data**: Ensure the same metrics and data collection processes are used consistently between online and offline evaluations to minimize biases and gaps <a class="yt-timestamp" data-t="00:18:40">[00:18:40]</a>.
2.  **Continuous Experimentation**: Run tests continuously to monitor the gap between treatment and no-treatment scenarios, reacting to changes over time <a class="yt-timestamp" data-t="00:19:34">[00:19:34]</a>.
3.  **Robust Solutions/Portfolio Approach**: Instead of relying on a single optimal treatment, develop several diverse strategies. This provides resilience if one method fails <a class="yt-timestamp" data-t="00:19:57">[00:19:57]</a>.
4.  **Monitoring Outcomes**: Actively monitor deployed solutions, comparing them to holdouts to understand their evolution and adapt to changes in the business environment <a class="yt-timestamp" data-t="00:16:01">[00:16:01]</a>.

## Simplicity in Design

A crucial lesson is the effectiveness of simple models <a class="yt-timestamp" data-t="00:20:30">[00:20:30]</a>. While complex models with numerous features might seem appealing in offline benchmarking, they often lead to deployment issues, maintenance challenges, and increased overfitting in production <a class="yt-timestamp" data-t="00:20:45">[00:20:45]</a>. Adding more variables introduces more "moving parts" and risks related to data drift, seasonality, and differing effects on outcomes <a class="yt-timestamp" data-t="00:21:05">[00:21:05]</a>.

The initial approach should be to understand the problem and explore simple solutions, even if they seem basic <a class="yt-timestamp" data-t="00:27:06">[00:27:06]</a>, <a class="yt-timestamp" data-t="00:51:53">[00:51:53]</a>. For example, when initiating promotions, one might start by simply running a test to see if it's beneficial or losing money <a class="yt-timestamp" data-t="00:47:36">[00:47:36]</a>. Only then should more complexity be introduced, such as determining which promotion to give, different discount levels, or optimal timing <a class="yt-timestamp" data-t="00:48:05">[00:48:05]</a>.

## Learning from Experience

The process of building effective recommendation systems is iterative and long-term, akin to continuously refining a game <a class="yt-timestamp" data-t="00:45:52">[00:45:52]</a>. It involves starting with simple solutions, learning from their outcomes, and gradually introducing more complexity <a class="yt-timestamp" data-t="00:47:11">[00:47:11]</a>, <a class="yt-timestamp" data-t="00:47:22">[00:47:22]</a>. This continuous feedback loop helps in adapting to the dynamic environment and evolving business needs <a class="yt-timestamp" data-t="00:14:54">[00:14:54]</a>.

The culture at booking.com emphasizes [[experiments_and_ab_testing_in_machine_learning | experimentation]] and data-driven decisions, where the best solution is the one that proves better over time through data <a class="yt-timestamp" data-t="00:21:41">[00:21:41]</a>, <a class="yt-timestamp" data-t="00:21:59">[00:21:59]</a>. This environment fosters collaboration and shared learning, as teams converge to understand which solutions work best <a class="yt-timestamp" data-t="00:22:57">[00:22:57]</a>.

Ultimately, connecting machine learning deployments with actual product needs is paramount <a class="yt-timestamp" data-t="00:25:07">[00:25:07]</a>. The focus should be on the incremental value brought to the business and, more importantly, to the customer <a class="yt-timestamp" data-t="00:25:57">[00:25:57]</a>. Ensuring that the outcomes benefit the end-users (travelers) and service providers (hotels) aligns with the overall business goal of facilitating more transactions <a class="yt-timestamp" data-t="00:26:07">[00:26:07]</a>.