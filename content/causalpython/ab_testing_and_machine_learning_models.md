---
title: AB Testing and Machine Learning Models
videoId: xkx1tXLAP-o
---

From: [[causalpython]] <br/> 

In the realm of e-commerce, companies often use A/B testing to evaluate virtually any change to their website, including the implementation of machine learning (ML) solutions and recommender systems <a class="yt-timestamp" data-t="02:39:00">[02:39:00]</a>, <a class="yt-timestamp" data-t="02:44:57">[02:44:57]</a>. This rigorous experimentation culture aims to validate that new models not only achieve good offline metrics but also deliver a tangible impact on key business metrics <a class="yt-timestamp" data-t="02:47:00">[02:47:00]</a>.

## The Role of A/B Testing in Machine Learning

Traditional machine learning courses often present recommended systems as predictive or associative devices <a class="yt-timestamp" data-t="01:34:00">[01:34:00]</a>. However, in practice, a good recommender that improves offline metrics like accuracy or top-k might not "move the needle" causally <a class="yt-timestamp" data-t="02:59:00">[02:59:00]</a>. This is because it might simply predict what users would do anyway, moving traffic from one part of the website to another without generating incremental impact <a class="yt-timestamp" data-t="03:11:00">[03:11:00]</a>.

To address this, the focus shifts to using [[causality_and_machine_learning | causal inference]] to understand how to change user behavior incrementally <a class="yt-timestamp" data-t="03:32:00">[03:32:00]</a>. Instead of just predicting likely outcomes, the goal is to think in terms of counterfactual outcomes: what would happen with and without a specific intervention <a class="yt-timestamp" data-t="05:35:00">[05:35:00]</a>, <a class="yt-timestamp" data-t="08:02:00">[08:02:00]</a>. This approach is crucial when evaluating promotional strategies, such as discounts, where the objective is to incentivize customers to book who otherwise wouldn't have <a class="yt-timestamp" data-t="07:05:00">[07:05:00]</a>, <a class="yt-timestamp" data-t="08:31:00">[08:31:00]</a>.

### Operational Constraints and Optimization

When offering promotions like discounts, companies operate under budget constraints <a class="yt-timestamp" data-t="10:25:00">[10:25:00]</a>. The cost is often triggered only if the customer acts on the offer and books, meaning there is no cost for non-converting users <a class="yt-timestamp" data-t="09:21:00">[09:21:00]</a>. This creates an optimization problem where the aim is to maximize incremental volumes (new customers, new reservations) while controlling for incremental costs and ensuring the budget is not exceeded or the return on investment (ROI) falls below a threshold <a class="yt-timestamp" data-t="11:22:00">[11:22:00]</a>. This blends [[causality_and_machine_learning | causal inference]] with optimization, akin to a knapsack problem, where the challenge is to select which items (or in this case, which users to offer discounts to) fit within budget constraints to maximize value <a class="yt-timestamp" data-t="12:48:00">[12:48:40]</a>.

## Challenges in Combining Optimization and Causal Inference

The integration of optimization, [[causality_and_machine_learning | causal inference]], and recommendation systems presents several challenges:
*   **Noisy Data** The data is often noisy, leading to overfitting and issues with seasonality <a class="yt-timestamp" data-t="14:28:00">[14:28:00]</a>.
*   **Evolving Problems** Business needs and constraints are dynamic and constantly evolve, requiring continuous adaptation of solutions <a class="yt-timestamp" data-t="15:03:00">[15:03:00]</a>.
*   **Dynamic Environment** Pricing and promotion experiments operate in a highly dynamic environment, making "ship and forget" approaches impossible <a class="yt-timestamp" data-t="16:26:00">[16:26:00]</a>. Continuous monitoring and comparison with holdouts are essential to track changes over time <a class="yt-timestamp" data-t="16:34:00">[16:34:00]</a>.
*   **Misalignment Between Online and Offline Evaluation** There is often a disparity between offline model performance and online results, indicating that the initial assumptions about the data may not hold true for real users <a class="yt-timestamp" data-t="17:15:00">[17:15:00]</a>. Testing models online can be costly, especially when dealing with discounts, making it crucial to improve offline training and testing <a class="yt-timestamp" data-t="17:57:00">[17:57:00]</a>.

## Strategies for Online Evaluation and Learning

To bridge the gap between offline and online performance, several strategies are employed:
*   **Metric and Data Alignment** Ensure consistency in metrics and data collection processes between online and offline environments <a class="yt-timestamp" data-t="18:40:00">[18:40:00]</a>. A simple baseline should yield the same measurement both offline and online, or at least a predictable gap <a class="yt-timestamp" data-t="19:15:00">[19:15:00]</a>.
*   **Continuous Experimentation** Run experiments continuously, not just for specific periods, to observe if the gap between treatment and no-treatment or different treatments remains consistent <a class="yt-timestamp" data-t="19:34:00">[19:34:00]</a>.
*   **Portfolio Approach** Develop a robust solution with multiple, diverse strategies. This ensures that if one method fails, others can still be relied upon <a class="yt-timestamp" data-t="20:01:00">[20:01:00]</a>.
*   **Simple Models** Prioritize simple models over complex ones <a class="yt-timestamp" data-t="20:30:00">[20:30:00]</a>. While complex models might show good offline benchmarks, they are harder to deploy, maintain, and are more prone to overfitting due to numerous moving parts and potential data drift or seasonality <a class="yt-timestamp" data-t="20:45:00">[20:45:00]</a>.

## Experimentation Culture

Operating within an experimentation culture means everything is data-driven, and any solution must be confirmed by data to be deployed <a class="yt-timestamp" data-t="21:39:00">[21:39:00]</a>. This creates an "evolutional game" where only the best solutions survive and evolve <a class="yt-timestamp" data-t="21:55:00">[21:55:00]</a>. While intimidating due to many competing teams and directions, data helps determine which solutions are superior <a class="yt-timestamp" data-t="22:06:00">[22:06:00]</a>. Centralized departments often build common methodologies or platforms to serve as services for other teams, fostering collaboration and shared knowledge <a class="yt-timestamp" data-t="22:31:00">[22:31:00]</a>.

## Connecting Technical Work to Business Needs

A crucial lesson for technical teams is to understand the expected impact of their work and its actual use case <a class="yt-timestamp" data-t="24:14:00">[24:14:00]</a>. For example, a highly accurate image recognition model for toilets is only useful if it solves a real product need, such as helping onboard new properties that haven't tagged their amenities <a class="yt-timestamp" data-t="25:32:00">[25:32:00]</a>. Machine learning progress doesn't always correlate with incremental value to the business or customer <a class="yt-timestamp" data-t="25:53:00">[25:53:00]</a>.

Technical individuals, especially those new to [[causality_and_machine_learning | causal inference]], should avoid falling in love with complex technical solutions <a class="yt-timestamp" data-t="26:56:00">[26:56:00]</a>. Often, the simplest baseline or even a "magic number" can have a huge impact on results and customer behavior <a class="yt-timestamp" data-t="27:06:00">[27:06:00]</a>.

### The Paris Nights Example

A classic example illustrates this point: recommending the number of nights to stay in Paris <a class="yt-timestamp" data-t="27:50:00">[27:50:00]</a>. While data might show that people typically book for two or three nights, recommending a three-night stay can present a high price, potentially discouraging users <a class="yt-timestamp" data-t="29:01:00">[29:01:00]</a>. Recommending just one night, despite being less "accurate" based on typical booking patterns, shows a much cheaper price and greater availability, encouraging users to continue browsing <a class="yt-timestamp" data-t="29:09:00">[29:09:00]</a>. This counter-intuitive outcome highlights that the most accurate prediction is not always the most effective in driving desired user behavior <a class="yt-timestamp" data-t="29:34:00">[29:34:00]</a>.

## Human Psychology and A/B Testing

[[causality_and_machine_learning | Causality]] isn't just about discovering action-reaction dynamics; it deeply involves human psychology, which is not always rational <a class="yt-timestamp" data-t="30:11:00">[30:11:00]</a>. Understanding what drives people to a desired action often requires user interviews and research, but sometimes users themselves don't consciously know why they make certain decisions <a class="yt-timestamp" data-t="30:50:00">[30:50:00]</a>. Experiments can reveal counterintuitive patterns and behaviors <a class="yt-timestamp" data-t="31:17:00">[31:17:00]</a>.

A key finding about human psychology in this context is its inconsistency <a class="yt-timestamp" data-t="32:08:00">[32:08:00]</a>. An experiment that proves highly successful on one platform (e.g., laptop) might yield inverse results on another (e.g., mobile app) <a class="yt-timestamp" data-t="32:31:00">[32:31:00]</a>. Different countries or even the same person at a later time might react differently <a class="yt-timestamp" data-t="32:54:00">[32:54:00]</a>. This demonstrates the limitations of A/B tests regarding external validity; an effect shown in one environment doesn't automatically translate to another <a class="yt-timestamp" data-t="34:24:00">[34:24:00]</a>. While patterns can be learned, continuous validation is essential, fostering humility in making causal claims <a class="yt-timestamp" data-t="33:12:00">[33:12:00]</a>.

## Advice for Newcomers

For those starting in [[causality_and_machine_learning | causal inference]] or [[developing_effective_machine_learning_models | machine learning]] in general, the advice is to:
1.  **Keep it Simple** <a class="yt-timestamp" data-t="51:53:00">[51:53:00]</a>. Focus on the fundamental factors shaping the problem.
2.  **Understand the Problem** <a class="yt-timestamp" data-t="52:04:00">[52:04:00]</a>. Only then choose the appropriate tools.
3.  **Don't Be Ashamed of Simple Solutions** <a class="yt-timestamp" data-t="52:28:00">[52:28:00]</a>. These often have the biggest impact, especially in a business environment.
4.  **Focus on Impact** <a class="yt-timestamp" data-t="52:57:00">[52:57:00]</a>. Navigate efforts toward what actually moves the needle, rather than just fancy, complex technologies like deep learning architectures <a class="yt-timestamp" data-t="53:05:00">[53:05:00]</a>.
5.  **Prioritize Evaluation** <a class="yt-timestamp" data-t="54:40:00">[54:40:00]</a>. Ensure the right metric is evaluated, that it's consistent, useful across applications, and easy for stakeholders to understand. Cracking evaluation makes improvement straightforward <a class="yt-timestamp" data-t="54:57:00">[54:57:00]</a>.

## Building Blocks of Causal Recommended Systems

In the context of causal recommender systems, a common approach is "uplift modeling" (also known as heterogeneous treatment effect) <a class="yt-timestamp" data-t="40:48:00">[40:48:00]</a>. This involves finding the conditional average treatment effect of various interventions. Given a set of treatments (e.g., giving a discount or not, or multiple discount levels), the goal is to understand which outcome is better, defined by specific metrics <a class="yt-timestamp" data-t="41:00:00">[41:00:00]</a>.

Key aspects include:
*   **Randomized Data** Starting with randomized data (e.g., A/B tests) simplifies the problem by providing treatment A with its outcome and treatment B with its outcome <a class="yt-timestamp" data-t="41:37:00">[41:37:00]</a>.
*   **Observational Data** For observational data, which often has bias (e.g., in ranking recommendations), techniques like propensity score weighting or other debiasing methods are necessary <a class="yt-timestamp" data-t="41:44:00">[41:44:00]</a>.
*   **Average Treatment Effect** Initially, one can measure the average treatment effect to see if one treatment is generally better than another <a class="yt-timestamp" data-t="42:29:00">[42:29:00]</a>.
*   **Budget Constraints** If a treatment (like discounts) cannot be given to everyone due to cost, the problem becomes finding the most suitable customer segments <a class="yt-timestamp" data-t="42:47:00">[42:47:00]</a>. This requires modeling what would happen with and without the treatment, which is the essence of [[causality_and_machine_learning | causal modeling]] or uplift modeling <a class="yt-timestamp" data-t="44:05:00">[44:05:00]</a>.
*   **Retrospective Estimation** One technique developed involves training uplift models directly from converted data to identify who should receive a discount and who shouldn't <a class="yt-timestamp" data-t="44:16:00">[44:16:00]</a>.
*   **Causal Measurements** Causal measurements, such as K-curves, help determine the optimal threshold for applying policies and identifying affected segments <a class="yt-timestamp" data-t="44:56:00">[44:56:00]</a>.

This ongoing tuning and comparison between offline outcomes and online performance requires specific expertise, iterative learning, and adaptability based on application and company context <a class="yt-timestamp" data-t="45:09:00">[45:09:00]</a>.