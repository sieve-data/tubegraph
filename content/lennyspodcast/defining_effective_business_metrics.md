---
title: Defining effective business metrics
videoId: D4PDb_C8Dww
---

From: [[lennyspodcast]] <br/> 

Analytics should be a business impact-driving function, not purely a service function. It should focus on finding opportunities and providing a point of view on decisions, not just answering "why" but also "what do we do now that we know this" <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>.

## Principles for Picking Good Metrics

Jessica Lax, VP of Analytics and Data Science at DoorDash, emphasizes several key principles for defining effective business metrics, often learned from the pitfalls of using ineffective ones <a class="yt-timestamp" data-t="00:44:45">[00:44:45]</a>:

### 1. Identify Short-Term Proxies for Long-Term Outcomes
It is crucial to find a short-term metric that can be measured and that demonstrably drives a desired long-term outcome <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.

- **Avoid direct long-term goals for short-term iteration**: For instance, "retention" is a poor metric to set goals on because it's almost impossible to drive meaningfully in the short term <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>. Instead, identify the specific inputs that influence retention <a class="yt-timestamp" data-t="00:45:17">[00:45:17]</a>.
- **Experimentation**: Use experimentation to test whether these short-term inputs are, in fact, driving the desired long-term outputs <a class="yt-timestamp" data-t="00:45:24">[00:45:24]</a>. This aligns with the concept of [[developing_and_using_northstar_metrics | Northstar metrics]], where short-term, actionable metrics serve as leading indicators for long-term strategic goals.

### 2. Keep Metrics Simple
Simplicity is paramount for effective metrics. Complex, composite metrics tend to be misunderstood and thus difficult to act upon <a class="yt-timestamp" data-t="00:45:33">[00:45:33]</a>.

- **Focus on intuition and understanding**: Even if a simpler metric isn't "perfect" or as comprehensive as a composite one, it is far more effective if people across the company understand it and have an intuition around its meaning <a class="yt-timestamp" data-t="00:46:07">[00:46:07]</a>.
- **Example: Merchant Health Score**: An earlier attempt at a "Merchant Health" score combined many factors with coefficients, resulting in a number (e.g., "35") that lacked intuitive meaning <a class="yt-timestamp" data-t="00:50:56">[00:50:56]</a>. Switching to simpler, understandable metrics like "percentage of new merchants getting an order in the first seven days" or "merchant photo coverage" proved more effective, even if it meant tracking several metrics instead of one <a class="yt-timestamp" data-t="00:51:48">[00:51:48]</a>. This approach makes it easier for teams to know what to move and prioritize efforts <a class="yt-timestamp" data-t="00:52:30">[00:52:30]</a>.

### 3. Quantify Levers in a Common Currency
Understanding how different metrics across the company equate to one another, particularly in a common currency, enables informed trade-offs and faster decision-making <a class="yt-timestamp" data-t="00:46:38">[00:46:38]</a>.

- **Translate impact to core business value**: At DoorDash, various initiatives are quantified in terms of their impact on Gross Order Value (GOV) and volume <a class="yt-timestamp" data-t="00:48:28">[00:48:28]</a>. For example, the impact of lowering prices by a dollar versus reducing delivery times by a minute can be compared by their respective effects on volume <a class="yt-timestamp" data-t="00:46:53">[00:46:53]</a>.
- **Enable cross-functional trade-offs**: This common currency allows for strategic decisions across different teams, such as marketing and logistics, by understanding the return on investment for various actions (e.g., improving login flow, adding new restaurants, onboarding more Dashers) <a class="yt-timestamp" data-t="00:47:09">[00:47:09]</a>. This supports [[strategies_for_measuring_product_success | strategies for measuring product success]] and [[business_sustainability_and_profitability | business sustainability and profitability]].

### 4. Focus on Edge Cases and Fail States
While averages are often the focus, it is vital to examine and set goals around edge cases and "fail states" that can have disproportionately negative impacts <a class="yt-timestamp" data-t="00:55:29">[00:55:29]</a>.

- **"Never Delivered" orders**: At DoorDash, "never delivered" orders are rare, but they represent terrible customer experiences, lead directly to churn, and are incredibly costly due to refunds and re-purchases <a class="yt-timestamp" data-t="00:56:02">[00:56:02]</a>.
- **Hidden problems**: Some issues, like login errors, might not even appear in conventional data because affected users cannot access the system to generate data <a class="yt-timestamp" data-t="00:59:26">[00:59:26]</a>. Data teams must consider what data they might be missing <a class="yt-timestamp" data-t="00:59:46">[00:59:46]</a>.
- **Impact on brand and profitability**: Addressing these infrequent but critical failures significantly impacts brand reputation, prevents churn (which represents lost future orders), and improves profitability, even if the frequency of such events is very low <a class="yt-timestamp" data-t="00:58:31">[00:58:31]</a>. This is a form of [[quality_improvement_leading_to_business_impact | quality improvement leading to business impact]].

## Aligning Incentives Through Metrics

Metrics are crucial for aligning incentives within teams. By ensuring the analytics team shares the same goals as their business partners (e.g., marketing, product, operations), everyone is incentivized to work on the most important things <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>. This creates a shared sense of success and purpose.