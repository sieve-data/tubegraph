---
title: Metrics and measuring product success
videoId: qbZQjprTnrU
---

From: [[lennyspodcast]] <br/> 

Measuring product success effectively requires understanding the value being produced for the customer and measuring it from their perspective <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>. It's crucial to combine quantitative charts showing growth with qualitative feedback, such as customer tweets <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>, to determine if you have [[the_importance_of_productmarket_fit_and_customer_feedback | product market fit]] <a class="yt-timestamp" data-t="00:46:06">[00:46:06]</a>.

## The Role of Metrics

Metrics, at their best, are a numerical representation of the value a product provides to the customer <a class="yt-timestamp" data-t="00:46:50">[00:46:50]</a>. While it's easy to count anything, the privilege lies in choosing *what* to measure <a class="yt-timestamp" data-t="00:47:04">[00:47:04]</a>. The focus should be on measuring the value from the customer's perspective, rather than an internal, company-centric view (e.g., how many people logged in versus how many accomplished their goal after logging in) <a class="yt-timestamp" data-t="00:47:15">[00:47:15]</a>.

Metrics also serve as a tool to force tradeoffs and decisions, helping to align large groups towards a common goal and track progress over time <a class="yt-timestamp" data-t="00:47:54">[00:47:54]</a>.

## Atlas's Approach to Metrics

When Jeff Weinstein started working on Stripe Atlas, he found that many support tickets indicated customer unhappiness <a class="yt-timestamp" data-t="00:49:08">[00:49:08]</a>. This led to the question: "Why would someone recommend Atlas to a friend?" <a class="yt-timestamp" data-t="00:49:48">[00:49:48]</a>. The answer was that customers wouldn't recommend it if they had to contact support <a class="yt-timestamp" data-t="00:50:04">[00:50:04]</a>.

This insight led to the adoption of a key metric for Atlas: **"Companies with zero support tickets"** <a class="yt-timestamp" data-t="00:50:27">[00:50:27]</a>. This metric measured the percentage of founders who completed the entire incorporation process, including a two-week buffer for support inquiries, without needing to contact support <a class="yt-timestamp" data-t="00:50:50">[00:50:50]</a>.

> [!tip] Customer-Oriented Metrics
> This metric directly reflects the customer's desired outcome (a smooth, problem-free experience) <a class="yt-timestamp" data-t="00:52:07">[00:52:07]</a>. If customers knew this was the primary metric, they would be ecstatic, as it shows the company is focused on their success <a class="yt-timestamp" data-t="00:52:19">[00:52:19]</a>.

Initially, only 15% of founders completed the process with zero support tickets <a class="yt-timestamp" data-t="00:51:21">[00:51:21]</a>. By addressing the issues causing support tickets and baking solutions into the product, Atlas increased this number to 85% in about 18 months <a class="yt-timestamp" data-t="00:51:40">[00:51:40]</a>. This improvement directly correlated with market share growth <a class="yt-timestamp" data-t="00:51:57">[00:51:57]</a>.

This single, clear metric motivated the entire engineering team. Engineers could be assigned specific problem areas (e.g., support tickets related to delayed risk reviews) and were empowered to propose and build solutions <a class="yt-timestamp" data-t="00:52:37">[00:52:37]</a>. This approach turned engineers into de facto product managers for specific issues <a class="yt-timestamp" data-t="00:52:57">[00:52:57]</a>.

## Avoiding Perverse Incentives and Choosing the Right Metric

While focusing on a single metric is powerful, it's essential to monitor other metrics to avoid perverse incentives <a class="yt-timestamp" data-t="00:54:47">[00:54:47]</a>. For example, if the goal is to reduce support tickets, a team might make it harder to contact support rather than solving underlying problems <a class="yt-timestamp" data-t="00:54:30">[00:54:30]</a>.

> [!tip] The "Users Having a Bad Day" Metric
> A highly exportable metric is **"Users having a bad day"** <a class="yt-timestamp" data-t="01:01:01">[01:01:01]</a>. This involves emitting a log line whenever a user encounters a known problem (e.g., 404 errors, delayed payouts, excessive payment declines) <a class="yt-timestamp" data-t="01:01:09">[01:01:09]</a>. Visualizing these "bad day" reasons in a stacked bar chart can reveal surprising frequencies and prioritize areas for improvement <a class="yt-timestamp" data-t="01:01:38">[01:01:38]</a>. This metric helps track problems that might otherwise go unnoticed <a class="yt-timestamp" data-t="01:01:53">[01:01:53]</a>.

## Dashboard Hygiene and Cultural Impact

The presentation and hygiene of metrics are also critical for team engagement and trust <a class="yt-timestamp" data-t="01:06:47">[01:06:47]</a>:
*   **Meaningful Titles**: Metric titles should be concise and evoke a feeling, directly reflecting the customer's perspective (e.g., "Companies with zero support tickets" instead of complex, technical names) <a class="yt-timestamp" data-t="01:05:24">[01:05:24]</a>. This helps the metric become a cultural currency within the company <a class="yt-timestamp" data-t="01:06:04">[01:06:04]</a>.
*   **Clarity and Consistency**: Percentages should have relevant significant digits, and all measures on a dashboard should share the same x-axis for easier interpretation <a class="yt-timestamp" data-t="01:06:51">[01:06:51]</a>.
*   **Accessibility**: Dashboards should be discoverable and frequently viewed by the team. Having a single, trusted source for metrics (e.g., a "go metrics" link) prevents relying on one-off queries or screenshots, which can be inconsistent or incorrect <a class="yt-timestamp" data-t="01:08:43">[01:08:43]</a>.

When a team consistently looks at the same set of information, it creates a shared understanding of the customer's heartbeat <a class="yt-timestamp" data-t="01:07:19">[01:07:19]</a>. This focus on a few, high-signal metrics forces prioritization and deep understanding of customer needs <a class="yt-timestamp" data-t="01:10:59">[01:10:59]</a>.

## Connecting Product Quality to Business Value

While product quality and user experience are paramount, they must eventually connect to business value. This connection often lies in how product improvements drive customer acquisition, retention, and ultimately, revenue <a class="yt-timestamp" data-t="01:25:29">[01:25:29]</a>. The entire customer journey, including sales, support, and even administrative processes, should be considered part of the product experience <a class="yt-timestamp" data-t="01:29:57">[01:29:57]</a>. By continuously improving this holistic experience, a company can foster growth and ensure long-term viability <a class="yt-timestamp" data-t="01:30:07">[01:30:07]</a>.