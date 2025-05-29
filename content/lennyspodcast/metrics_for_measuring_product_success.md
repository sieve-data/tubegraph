---
title: Metrics for measuring product success
videoId: qbZQjprTnrU
---

From: [[lennyspodcast]] <br/> 

Measuring product success is crucial for understanding whether a product is delivering value and driving the business forward. The core responsibility of a product manager is to achieve [[product_market_fit_strategies | product market fit]] <a class="yt-timestamp" data-t="00:46:00">[00:46:00]</a>. This fit is indicated by quantitative charts showing growth ("up and to the right") and qualitative feedback like customer tweets <a class="yt-timestamp" data-t="00:30:13">[00:30:13]</a>, <a class="yt-timestamp" data-t="00:46:12">[00:46:12]</a>.

## Aligning Metrics with Customer Value
Effective [[key_performance_indicators_for_marketplaces | metrics]] are numerical representations of the value provided to the customer, measured from their perspective <a class="yt-timestamp" data-t="00:46:50">[00:46:50]</a>. Instead of focusing solely on internal metrics like "how many people logged in," it's more insightful to track "how many people accomplished what they were trying to do after they logged in" <a class="yt-timestamp" data-t="00:47:32">[00:47:32]</a>.

Metrics serve to:
*   **Force tradeoffs and decisions** <a class="yt-timestamp" data-t="00:47:54">[00:47:54]</a>.
*   **Orient large groups towards the right direction** daily <a class="yt-timestamp" data-t="00:48:21">[00:48:21]</a>.
*   **Generate progress for customers** from their perspective <a class="yt-timestamp" data-t="00:48:29">[00:48:29]</a>.

## Case Study: Stripe Atlas's "Zero Support Tickets" Metric
When evaluating Stripe Atlas, the team noticed a high volume of unhappy support tickets related to common issues like DocuSign problems, co-founder addresses, or login difficulties <a class="yt-timestamp" data-t="00:49:08">[00:49:08]</a>. This indicated that customers with support tickets were unlikely to recommend Atlas to others <a class="yt-timestamp" data-t="00:50:04">[00:50:04]</a>.

The chosen [[choosing_and_using_north_star_metrics_effectively | North Star metric]] for Atlas became **"companies that have no support tickets"** throughout the entire incorporation process, including a two-week buffer after completion <a class="yt-timestamp" data-t="00:50:28">[00:50:28]</a>.
*   **Initial State**: Only 15% of founders completed the Atlas process with zero support tickets <a class="yt-timestamp" data-t="00:51:21">[00:51:21]</a>.
*   **Goal**: Drive this number significantly up by baking solutions to common support issues directly into the product <a class="yt-timestamp" data-t="00:51:32">[00:51:32]</a>.
*   **Outcome**: Over 18 months, the percentage of founders with zero support tickets increased from 15% to 85% <a class="yt-timestamp" data-t="00:51:48">[00:51:48]</a>. This directly correlated with Atlas's market share growth <a class="yt-timestamp" data-t="00:51:57">[00:51:57]</a>.

This [[single metric | single metric]] was highly effective because:
*   It spoke directly to what the customer wanted <a class="yt-timestamp" data-t="00:52:07">[00:52:07]</a>.
*   It was transparent and encouraging for the team <a class="yt-timestamp" data-t="00:52:34">[00:52:34]</a>.
*   It motivated engineers to act as product managers, identifying problems from support tickets and building solutions <a class="yt-timestamp" data-t="00:52:57">[00:52:57]</a>.
*   It aligned with the [[role_of_marketing_in_product_success | go-to-market strategy]] of delighting current customers to encourage word-of-mouth recommendations <a class="yt-timestamp" data-t="00:59:43">[00:59:43]</a>.

## Identifying Problems with "Users Having a Bad Day"
A valuable metric for almost any business is **"users having a bad day"** <a class="yt-timestamp" data-t="01:01:05">[01:01:05]</a>.
*   **Concept**: Emit a log line whenever a user encounters a problem that would cause them to have a bad day (e.g., hitting a 404 error, a payout delay, or more than 10 payment declines) <a class="yt-timestamp" data-t="01:01:09">[01:01:09]</a>.
*   **Visualization**: Create a stacked bar chart of all "bad day" reasons and their frequencies <a class="yt-timestamp" data-t="01:01:40">[01:01:40]</a>.
*   **Benefit**: This eye-opening metric helps scale the team's understanding of user pain points and informs which issues to prioritize and "burn down" <a class="yt-timestamp" data-t="01:02:19">[01:02:19]</a>. If a new "bad day" occurs that isn't being tracked, it warrants immediate action to count it and add it to the chart <a class="yt-timestamp" data-t="01:03:16">[01:03:16]</a>.

## Best Practices for Metrics and Dashboards
*   **Clear, Simple Titles**: Metric titles should be short, focused, and reflect a customer mindset, like "companies with zero support tickets" <a class="yt-timestamp" data-t="01:05:51">[01:05:51]</a>. This brevity and focus make the metric a "currency" within the company and motivate teams <a class="yt-timestamp" data-t="01:06:04">[01:06:04]</a>.
*   **Good Hygiene**: Maintain consistent formatting (e.g., decimal points, x-axis) and ensure data accuracy. This increases the frequency with which people open and trust the dashboard <a class="yt-timestamp" data-t="01:07:07">[01:07:07]</a>.
*   **Centralized Source of Truth**: Metrics should live in a discoverable, trusted system (e.g., `go/metrics`) rather than scattered one-off queries or screenshots <a class="yt-timestamp" data-t="01:08:54">[01:08:54]</a>. This ritualistic, frequent review of consistent data builds trust and informs decision-making <a class="yt-timestamp" data-t="01:10:45">[01:10:45]</a>.
*   **Limited Number of Metrics**: Focus care and understanding on a small number of core metrics to avoid spreading attention too thin <a class="yt-timestamp" data-t="01:10:57">[01:10:57]</a>.

## Economic Viability and Long-Term Impact
Ultimately, metrics should demonstrate the economic viability of the product <a class="yt-timestamp" data-t="02:08:20">[02:08:20]</a>. Even highly successful products, like Atlas with an 80+ NPS, continue to invest in automation if it leads to customers generating revenue sooner <a class="yt-timestamp" data-t="01:46:33">[01:46:33]</a>. For Atlas, reducing the time for a company to get started by a week or two directly accelerates GDP generation <a class="yt-timestamp" data-t="01:47:50">[01:47:50]</a>.

This [[effective_metrics_for_longterm_business_outcomes | long-term compounding approach]] ensures that investments in product quality and user experience are tied to sustainable business growth and competitive advantage <a class="yt-timestamp" data-t="02:09:50">[02:09:50]</a>.

## Importance of [[the_importance_of_following_up_on_results_in_product_management | Following Up on Results]]
Companies should look at whether their teams are looking at their own metrics <a class="yt-timestamp" data-t="01:07:34">[01:07:34]</a>. This is an incredibly useful predictor of how aligned teams are and how customer-obsessed they are <a class="yt-timestamp" data-t="01:07:39">[01:07:39]</a>.