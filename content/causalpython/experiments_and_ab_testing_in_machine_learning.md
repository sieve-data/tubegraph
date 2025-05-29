---
title: Experiments and AB testing in machine learning
videoId: xkx1tXLAP-o
---

From: [[causalpython]] <br/> 

At Booking.com, the approach to product development and machine learning deployments is deeply rooted in an experimentation culture where everything is data-driven, and every change, down to bug fixes, undergoes A/B testing <a class="yt-timestamp" data-t="00:15:01">[00:15:01]</a>, <a class="yt-timestamp" data-t="00:21:27">[00:21:27]</a>. This environment fosters an "evolutionary game" where the best solutions, those that prove to be better over time, are the ones that survive and evolve <a class="yt-timestamp" data-t="00:21:55">[00:21:55]</a>.

## Merging Recommended Systems with Causal Inference

Traditionally, recommended systems are taught as predictive or associative devices, aiming to identify the most suitable items based on correlations <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>, <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>. However, in practice, a recommender system that performs well on offline accuracy metrics (like accuracy or top-k) might not "move the needle" in a [[causal_inference_and_machine_learning | causal]] way when deployed online <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>, <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>. This is because it might merely confirm a user's existing intent, moving traffic from one part of the website to another without generating incremental impact <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.

The key shift is to think in terms of [[causal_inference_and_machine_learning | counterfactual outcomes]] – what would a customer do differently if a recommendation or treatment wasn't provided <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>, <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>? The goal is to introduce a change that genuinely shifts customer behavior, not just predict what they would do anyway <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>. This means focusing on innovative solutions that incentivize behavioral change, rather than just the most popular or frequent options <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.

### Role of Pricing and Discounts

Price differences, discounts, promotions, and coupons are significant drivers of customer behavior in the travel industry <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>, <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>. Offering a discount can be more beneficial for incentivizing bookings than merely being relevant <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>.

However, giving discounts comes with a cost <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>. This leads to an optimization problem: determining when and what discount to offer to maximize incremental bookings while staying within budget constraints <a class="yt-timestamp" data-t="00:07:25">[00:07:25]</a>, <a class="yt-timestamp" data-t="00:10:25">[00:10:25]</a>. The challenge is to identify customers whose behavior will actually change due to the discount, rather than those who would have booked anyway <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>, <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>.

Unlike marketing campaigns with upfront costs (e.g., pay-per-click), discounts often have a "trigger cost" – the cost is incurred only if the customer books after receiving the offer <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>, <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>. This framework, focusing on maximizing incremental volumes (new customers, reservations) while controlling for incremental costs, aligns with a modified "knapsack problem" in optimization <a class="yt-timestamp" data-t="00:11:22">[00:11:22]</a>, <a class="yt-timestamp" data-t="00:12:34">[00:12:34]</a>.

## Challenges in Causal Machine Learning Applications

Combining [[causal_inference_and_machine_learning | causal inference]] with optimization and recommendation systems presents several challenges:

*   **Noisy Data and Overfitting:** Real-world data is often noisy, making it difficult to accurately measure uplift and avoid overfitting <a class="yt-timestamp" data-t="00:14:28">[00:14:28]</a>.
*   **Seasonality and Dynamic Environments:** Business problems are dynamic, with seasonality and evolving customer needs. Solutions must be robust and adaptable <a class="yt-timestamp" data-t="00:15:03">[00:15:03]</a>, <a class="yt-timestamp" data-t="00:15:31">[00:15:31]</a>.
*   **Monitoring and Maintenance:** Deploying changes, especially for pricing, requires continuous monitoring against holdout groups, as environmental factors can change rapidly <a class="yt-timestamp" data-t="00:16:31">[00:16:31]</a>.
*   **Independent Assumptions vs. Reality:** Initial independent assumptions in models often don't hold with real users, necessitating continuous adjustment and control <a class="yt-timestamp" data-t="00:17:12">[00:17:12]</a>.
*   **Cost of Online Testing:** Online A/B tests can be costly, especially if discounts are given incorrectly, leading to sub-optimal results <a class="yt-timestamp" data-t="00:17:59">[00:17:59]</a>. This emphasizes the importance of robust offline testing and alignment.

## Strategies for Online and Offline Model Evaluation

To bridge the gap between offline model performance and online impact, several strategies are crucial:

*   **Metric Alignment:** Ensure the same metrics are used and defined consistently across online and offline evaluations, accounting for different data sources and timings <a class="yt-timestamp" data-t="00:18:40">[00:18:40]</a>.
*   **Data Collection Consistency:** Verify that data collection processes for online and offline models are identical to avoid fundamental biases <a class="yt-timestamp" data-t="00:19:00">[00:19:00]</a>. A simple baseline run offline should ideally match online measurements, or at least the gap should be predictable <a class="yt-timestamp" data-t="00:19:15">[00:19:15]</a>.
*   **Continuous Experimentation:** Rather than one-off tests, continuous experimentation helps observe how the gap between treatment and control evolves over time and allows for reactions to changes <a class="yt-timestamp" data-t="00:19:34">[00:19:34]</a>.
*   **Portfolio Approach:** Instead of relying on a single "optimal" treatment, building a portfolio of diverse strategies provides robustness. If one method breaks, others can still be relied upon <a class="yt-timestamp" data-t="00:20:01">[00:20:01]</a>.
*   **Simplicity:** Prioritize simple models over complex ones with many features. While complex models might show good [[benchmarking_in_causal_machine_learning | benchmarking]] offline, they are harder to deploy, maintain, and are more susceptible to overfitting and data drift <a class="yt-timestamp" data-t="00:20:30">[00:20:30]</a>.

## Communication with Business Stakeholders

Effective communication with business stakeholders is paramount for technical teams. A key lesson is to understand the **expected impact** of the work <a class="yt-timestamp" data-t="00:24:14">[00:24:14]</a>. Unlike purely technical domains where accuracy might be the primary metric, in a business context, the true value lies in how a model changes behavior and moves key business metrics <a class="yt-timestamp" data-t="00:24:45">[00:24:45]</a>. This requires close collaboration with product managers to connect models to actual product needs and ensure they address important business problems <a class="yt-timestamp" data-t="00:25:11">[00:25:11]</a>, <a class="yt-timestamp" data-t="00:25:27">[00:25:27]</a>.

A critical piece of advice is: "Don't fall in love with the cool technical stuff" <a class="yt-timestamp" data-t="00:26:57">[00:26:57]</a>. Often, the simplest solution, even a basic average or a "magic number," can have a huge impact on customer behavior and results <a class="yt-timestamp" data-t="00:27:06">[00:27:06]</a>. Fancy deep learning models should only be considered after understanding the fundamental problem and testing simpler approaches <a class="yt-timestamp" data-t="00:27:32">[00:27:32]</a>.

### Case Study: Recommending Nights in Paris

An example illustrates this principle: A sophisticated model was built to recommend the optimal number of nights to stay in Paris, based on historical booking distributions <a class="yt-timestamp" data-t="00:27:57">[00:27:57]</a>. However, when deployed, it failed to increase bookings or page navigation <a class="yt-timestamp" data-t="00:28:35">[00:28:35]</a>. The [[causal_ai_and_its_role_in_experiments | causal]] insight gained from A/B testing was counterintuitive: recommending just one night, despite people typically staying longer, resulted in a much cheaper displayed price and more available properties <a class="yt-timestamp" data-t="00:29:01">[00:29:01]</a>, <a class="yt-timestamp" data-t="00:29:17">[00:29:17]</a>. This encouraged users to continue their search, leading to more engagement. The "most accurate" answer was not the "right" one for changing behavior <a class="yt-timestamp" data-t="00:29:34">[00:29:34]</a>.

## Human Psychology and Inconsistency

[[Causal inference and machine learning | Causal inference]] in real-world applications often involves understanding human psychology, which is not always rational or consistent <a class="yt-timestamp" data-t="00:30:11">[00:30:11]</a>, <a class="yt-timestamp" data-t="00:31:04">[00:31:04]</a>. What works in one experimental setup (e.g., a specific color on a laptop) might yield inverse results on another platform (e.g., mobile app) <a class="yt-timestamp" data-t="00:32:31">[00:32:31]</a>, <a class="yt-timestamp" data-t="00:32:48">[00:32:48]</a>. People from different countries might react differently, or even the same person might behave differently over time <a class="yt-timestamp" data-t="00:32:54">[00:32:54]</a>. This highlights the limitations of A/B tests regarding external validity: a proven effect in one environment doesn't automatically translate to another <a class="yt-timestamp" data-t="00:34:27">[00:34:27]</a>. This necessitates continuous validation and a humble approach to claims of causality <a class="yt-timestamp" data-t="00:33:14">[00:33:14]</a>.

## The Challenge of Thinking in Counterfactuals

The concept of [[causal_inference_and_machine_learning | counterfactuals]] (what would have happened if a treatment wasn't applied) is challenging even for experienced professionals <a class="yt-timestamp" data-t="00:36:18">[00:36:18]</a>.

> "I think this kind of thinking is requires you an extra level of like of cognitive load of understanding that he there's a completely different scenario that I could do completely different actions and the outcomes could be different..." <a class="yt-timestamp" data-t="00:36:40">[00:36:40]</a>

The difficulty arises because:
*   **Missing Labels:** One never observes both scenarios (treatment given and not given) for the same individual at the same time <a class="yt-timestamp" data-t="00:37:07">[00:37:07]</a>. This makes model evaluation, explainability, and [[benchmarking_in_causal_machine_learning | benchmarking]] harder <a class="yt-timestamp" data-t="00:37:40">[00:37:40]</a>.
*   **Simulations:** [[optimal_experimentation_in_causal_analysis | Simulations]] can help by creating hypothetical worlds where both outcomes are known, but this is an extensive thinking process <a class="yt-timestamp" data-t="00:37:54">[00:37:54]</a>.
*   **Human Intuition:** It's not natural for people to spontaneously construct parallel scenarios for decisions in their own lives <a class="yt-timestamp" data-t="00:38:21">[00:38:21]</a>.

However, once grasped, this thinking can be applied everywhere, from marketing discounts to public policies <a class="yt-timestamp" data-t="00:38:51">[00:38:51]</a>. It's often easier to be "smart in retrospective" about behavioral changes than to predict them in advance <a class="yt-timestamp" data-t="00:39:33">[00:39:33]</a>.

## Technological Building Blocks

For [[causal_machine_learning_and_treatment_effect_estimation | causal recommended systems]], the focus is on [[timevarying_treatments_in_machine_learning | uplift modeling]], also known as heterogeneous treatment effect estimation <a class="yt-timestamp" data-t="00:40:43">[00:40:43]</a>. This aims to find the conditional average treatment effect of a set of treatments <a class="yt-timestamp" data-t="00:40:53">[00:40:53]</a>.

Key aspects include:
*   **Randomized Data:** Starting with randomized data from A/B tests simplifies the problem, as it provides a clear comparison between treatment and control outcomes <a class="yt-timestamp" data-t="00:41:37">[00:41:37]</a>.
*   **Observational Data:** For observational data, debiasing techniques (e.g., propensity score methods) are necessary to account for inherent biases <a class="yt-timestamp" data-t="00:41:44">[00:41:44]</a>.
*   **Multi-objective Optimization:** When multiple metrics are involved (e.g., incremental volume vs. cost), multi-objective optimization or Pareto tradeoffs are employed <a class="yt-timestamp" data-t="00:41:26">[00:41:26]</a>.
*   **Budget Constraints:** If treatments cannot be applied to everyone due to budget constraints, the goal is to identify the most suitable segments for the treatment, often based on their predicted uplift <a class="yt-timestamp" data-t="00:43:46">[00:43:46]</a>. This is typically visualized and optimized using [[benchmarking_in_causal_machine_learning | K-curves]] to find the optimal threshold <a class="yt-timestamp" data-t="00:45:04">[00:45:04]</a>.
*   **Retrospective Estimation:** A technique developed at Booking.com involves training an uplift model from converted data to estimate the potential impact of a discount on each individual <a class="yt-timestamp" data-t="00:44:16">[00:44:16]</a>.

## Advice for Newcomers

*   **Keep it Simple:** Focus on understanding the fundamental problem first and then choose the appropriate tools. Simple solutions can often have a huge impact <a class="yt-timestamp" data-t="00:51:53">[00:51:53]</a>, <a class="yt-timestamp" data-t="00:52:21">[00:52:21]</a>. Don't be ashamed of simple solutions, especially in a business environment focused on impact <a class="yt-timestamp" data-t="00:52:50">[00:52:50]</a>.
*   **Understand the Problem:** Before jumping into complex architectures or [[hyperparameter_tuning_for_causal_machine_learning | hyperparameter tuning]], understand what needs to be solved <a class="yt-timestamp" data-t="00:53:14">[00:53:14]</a>, <a class="yt-timestamp" data-t="00:53:42">[00:53:42]</a>.
*   **Focus on Evaluation:** Ensure that evaluation metrics are well-defined, consistent, correlated with the problem, and understandable to all stakeholders <a class="yt-timestamp" data-t="00:54:40">[00:54:40]</a>. Cracking the evaluation makes it straightforward to know what to improve <a class="yt-timestamp" data-t="00:54:57">[00:54:57]</a>.
*   **Share Learnings:** Engage with the community and share results and approaches <a class="yt-timestamp" data-t="01:07:03">[01:07:03]</a>. Different disciplines might use different terminology for similar problems (e.g., "heterogeneous treatment effect" vs. "uplift modeling"), highlighting the need for bridging knowledge gaps <a class="yt-timestamp" data-t="01:03:01">[01:03:01]</a>.