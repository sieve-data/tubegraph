---
title: Causal inference in personalized recommendations
videoId: xkx1tXLAP-o
---

From: [[causalpython]] <br/> 

Traditionally, recommender systems are viewed as predictive or associative devices, aiming to identify the most suitable items for users based on historical data <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>. However, this approach often falls short in driving incremental business value <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>. [[causal_inference_and_machine_learning | Causal inference]] offers a paradigm shift by focusing on understanding what actions will *change* user behavior, rather than simply predicting what they might do anyway <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.

## The Shift to Causal Thinking

For e-commerce platforms, the goal of personalization and recommendations is to introduce a change that makes customers do something different from what they would have done without the intervention <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>, <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>. While a well-built recommender might improve accuracy metrics, it may not "move the needle" in a causal way if it merely recommends what a user would have naturally found or chosen <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.

The key lies in [[psychology_and_user_behavior_in_recommendation_systems | thinking in terms of counterfactual outcomes]] – considering what would happen with and without a specific recommendation or treatment <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>, <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>. This means shifting focus from merely predicting the most popular or frequent solution to identifying innovative recommendations that incentivize behavior change <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>, <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>. Elements like user experience (UX), copywriting, and timing also play a crucial role in framing recommendations to encourage different actions <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.

## Case Study: Booking.com

At Booking.com, every change, including machine learning solutions and recommenders, is tested via A/B tests to observe their impact on key metrics <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>, <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>. The company runs hundreds or even thousands of A/B tests in parallel, even for bug fixes <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>, <a class="yt-timestamp" data-t="00:21:27">[00:21:27]</a>. This creates an "evolutionary game" where the best solution survives and evolves based on data <a class="yt-timestamp" data-t="00:21:55">[00:21:55]</a>.

### The Problem of Discounts and Promotions

In the travel industry, price differences (discounts, promotions, coupons) are strong drivers of customer behavior <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>. Offering discounts can be more beneficial for incentivizing bookings than simply being relevant <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>. However, giving discounts to everyone is not financially viable, leading to an optimization problem: determining when and what discount to offer <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>, <a class="yt-timestamp" data-t="00:10:25">[00:10:25]</a>.

This necessitates a [[causal_inference_in_practical_applications | counterfactual problem]] approach <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>. Marketers need to understand what would happen *with* a discount versus *without* one to ensure the discount changes customer behavior positively, rather than just being given to someone who would have booked anyway <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a>, <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>. The cost of a discount is typically triggered only if the customer makes a booking <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>.

### Budget Constraints and Optimization

Operating under fixed budget constraints means the focus shifts from maximizing incremental profit to maximizing incremental volumes (new customers, new reservations) while controlling incremental cost <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>, <a class="yt-timestamp" data-t="00:11:29">[00:11:29]</a>. This creates a two-dimensional incremental game, balancing bookings and costs <a class="yt-timestamp" data-t="00:11:47">[00:11:47]</a>. This problem can be framed as a fundamental optimization problem, similar to the knapsack problem, where decisions involve selecting which items (discounts) to "pick" to fit within a budget capacity <a class="yt-timestamp" data-t="00:12:34">[00:12:34]</a>, <a class="yt-timestamp" data-t="00:13:36">[00:13:36]</a>.

## Challenges in Combining Causal Inference and Recommendations

Integrating [[machine_learning_and_causal_inference_methodologies | causal inference]] and optimization with recommendations presents several challenges:

### Technical Challenges
*   **Noisy Data and Overfitting**: Real-world data is often noisy, making it difficult to find clean causal signals and leading to overfitting in models <a class="yt-timestamp" data-t="00:14:28">[00:14:28]</a>.
*   **Seasonality**: Seasonal fluctuations can impact model performance and the observed effects <a class="yt-timestamp" data-t="00:14:33">[00:14:33]</a>.
*   **Dynamic Environment**: The business environment is constantly evolving with new products, markets, and ongoing experiments, requiring continuous monitoring and adaptation <a class="yt-timestamp" data-t="00:14:54">[00:14:54]</a>, <a class="yt-timestamp" data-t="00:16:26">[00:16:26]</a>. "Ship and forget" is not an option <a class="yt-timestamp" data-t="00:16:31">[00:16:31]</a>.
*   **Lack of Counterfactual Labels**: In [[causal_inference_and_individual_treatment_effects | causal inference]], one never observes both outcomes (with and without treatment) for the same individual at the same time, making model evaluation and explainability harder <a class="yt-timestamp" data-t="00:37:05">[00:37:05]</a>, <a class="yt-timestamp" data-t="00:37:38">[00:37:38]</a>.

### Human Psychology and Inconsistency
Human behavior is often counterintuitive and inconsistent <a class="yt-timestamp" data-t="00:31:20">[00:31:20]</a>. A recommendation that seems logically optimal (e.g., suggesting a multi-night stay in Paris because that's what people usually book) might deter users if it presents a high initial price, whereas a cheaper, single-night option might encourage further exploration <a class="yt-timestamp" data-t="00:28:00">[00:28:00]</a>. What drives people to the desired action is not always rational and can even be influenced by seemingly minor details like button color or pop-ups, with results varying across platforms, countries, or even for the same person over time <a class="yt-timestamp" data-t="00:30:11">[00:30:11]</a>, <a class="yt-timestamp" data-t="00:32:05">[00:32:05]</a>.

> "Many times it's counterintuitive and the fact that you can connect between people Behavior from one side and the data in the results from Another Side I think it's also one of the most exciting parts of my work." <a class="yt-timestamp" data-t="00:31:17">[00:31:17]</a>

### Evaluating Models Online vs. Offline
It is crucial to align online and offline evaluation, ensuring consistent metrics and data collection processes <a class="yt-timestamp" data-t="00:18:40">[00:18:40]</a>. A simple baseline should yield the same measurement online and offline, or at least a predictable gap <a class="yt-timestamp" data-t="00:19:15">[00:19:15]</a>. Since testing models online (e.g., by giving discounts) can be costly if done incorrectly, it's better to test and train extensively offline <a class="yt-timestamp" data-t="00:17:57">[00:17:57]</a>.

## Strategies for Success

### Continuous Experimentation
Running continuous A/B tests and monitoring outcomes is essential to track changes over time and react to shifts in user behavior or business conditions <a class="yt-timestamp" data-t="00:19:34">[00:19:34]</a>. Maintaining a holdout group is a common practice to continuously assess "what would happen if we didn't give this discount" <a class="yt-timestamp" data-t="00:16:34">[00:16:34]</a>.

### Prioritizing Simplicity and Robustness
While complex models with many features might perform well offline, they are harder to deploy, maintain, and are more prone to overfitting and data drift in dynamic online environments <a class="yt-timestamp" data-t="00:20:50">[00:20:50]</a>. Sticking to simple models initially, and gradually introducing complexity, is often more effective <a class="yt-timestamp" data-t="00:20:30">[00:20:30]</a>, <a class="yt-timestamp" data-t="00:47:00">[00:47:00]</a>. A portfolio approach, using several different strategies, ensures that if one method breaks, others can still be relied upon <a class="yt-timestamp" data-t="00:20:01">[00:20:01]</a>.

### Effective Communication with Stakeholders
For technical teams, clear communication with business stakeholders is paramount. This involves:
*   **Understanding Expected Impact**: Focus on the actual product need and how the work will move the needle for the business and benefit the customer/partner <a class="yt-timestamp" data-t="00:24:14">[00:24:14]</a>, <a class="yt-timestamp" data-t="00:25:00">[00:25:00]</a>.
*   **Connecting with Product Needs**: Machine learning models should be integrated with actual product needs, with product managers collaborating closely to ensure alignment with business objectives <a class="yt-timestamp" data-t="00:25:07">[00:25:07]</a>.
*   **Not Falling in Love with Complexity**: The simplest solution that drives significant impact is often the best, even if it doesn't involve fancy, cutting-edge techniques like deep learning <a class="yt-timestamp" data-t="00:26:57">[00:26:57]</a>, <a class="yt-timestamp" data-t="00:52:50">[00:52:50]</a>.

## Key Takeaways and Advice

### For Practitioners
*   **Keep it Simple**: Understand the fundamental problem first, then pick the appropriate tools. Don't be ashamed of simple solutions <a class="yt-timestamp" data-t="00:51:53">[00:51:53]</a>, <a class="yt-timestamp" data-t="00:52:21">[00:52:21]</a>.
*   **Focus on Impact**: Navigate efforts towards what actually moves the needle and changes outcomes for the business and customers <a class="yt-timestamp" data-t="00:52:57">[00:52:57]</a>.
*   **Validate Relentlessly**: Given the inconsistencies in human behavior, continuous validation is key <a class="yt-timestamp" data-t="00:33:05">[00:33:05]</a>.
*   **Understand Evaluation**: Before any modeling, ensure the right metric is evaluated, that it's consistent, correlated with the problem, and easy for stakeholders to understand <a class="yt-timestamp" data-t="00:54:40">[00:54:40]</a>.
*   **Continuous Learning**: The field is constantly evolving; embrace continuous learning and exploration <a class="yt-timestamp" data-t="00:50:44">[00:50:44]</a>.

### For the Causal Python Community
*   **Share Learnings**: Share results, approaches, and challenges. Engage with others in the community to find better solutions <a class="yt-timestamp" data-t="01:07:03">[01:07:03]</a>.
*   **Bridge Disciplinary Gaps**: Acknowledge that different disciplines (e.g., economics, healthcare) may use different terminology for similar problems (e.g., "uplift modeling" vs. "heterogeneous treatment effect") <a class="yt-timestamp" data-t="01:03:04">[01:03:04]</a>, <a class="yt-timestamp" data-t="01:04:44">[01:04:44]</a>. Building bridges between these "ghettos" can lead to significant advancements <a class="yt-timestamp" data-t="01:05:29">[01:05:29]</a>.

> "People don't even know that other people were working on this a similar problem because there is a citation Gap in the literature and nobody never cited a person from this other stream." <a class="yt-timestamp" data-t="01:03:10">[01:03:10]</a>

The [[causal_inference_using_pymc | causal machine learning]] community is growing, with many workshops, conferences, and Python packages available <a class="yt-timestamp" data-t="01:06:21">[01:06:21]</a>. Booking.com actively publishes on uplift modeling and A/B testing <a class="yt-timestamp" data-t="01:05:47">[01:05:47]</a>.