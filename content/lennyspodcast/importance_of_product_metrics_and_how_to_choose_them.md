---
title: Importance of product metrics and how to choose them
videoId: qbZQjprTnrU
---

From: [[lennyspodcast]] <br/> 

Product metrics are crucial for building successful products, serving as a numerical representation of the value a product provides to its customers <a class="yt-timestamp" data-t="00:46:50">[00:46:50]</a>. Jeff Weinstein emphasizes that a product manager's core responsibility is to achieve [[Creating productmarket fit and operationalizing product quality | product-market fit]] <a class="yt-timestamp" data-t="00:45:58">[00:45:58]</a>, and metrics are essential for knowing when this has been accomplished <a class="yt-timestamp" data-t="00:46:06">[00:46:06]</a>.

## Why Metrics Are Important

Metrics, when well-chosen, are vital because they:
*   **Force Tradeoffs and Decisions** By providing clear, objective data, metrics help teams make difficult choices and prioritize work, preventing endless arguments and slow progress <a class="yt-timestamp" data-t="00:47:54">[00:47:54]</a>.
*   **Orient Teams** They naturally align larger groups of people toward a common goal every day, helping them understand if their tactics are generating progress over time <a class="yt-timestamp" data-t="00:48:21">[00:48:21]</a>.
*   **Indicate Product-Market Fit** Charts showing "up and to the right" trends, combined with qualitative feedback like customer tweets, are key indicators of product-market fit <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>, forming a "deep deep" partnership between quantitative and qualitative data <a class="yt-timestamp" data-t="00:46:22">[00:46:22]</a>.

The presence of a product outage where customers weren't "furious" and didn't desperately try to get the service back online indicated a lack of product-market fit. This showed that mere "craft" or "beauty" in a product cannot solve the fundamental issue of users not needing the product <a class="yt-timestamp" data-t="00:18:11">[00:18:11]</a>. People are motivated by their "first problem," not their second <a class="yt-timestamp" data-t="00:30:36">[00:30:36]</a>.

## How to Choose Effective Metrics

Choosing the right metrics involves a combination of deep customer understanding, strategic alignment, and clear communication.

### 1. Focus on Customer Value
Metrics should numerically represent the value being produced for the customer, measured from their perspective <a class="yt-timestamp" data-t="00:47:15">[00:47:15]</a>. It's easy for metrics to become internal-oriented (e.g., "how many people logged in"), but more crucial is measuring "how many people accomplished what they were trying to do after they logged in" <a class="yt-timestamp" data-t="00:47:32">[00:47:32]</a>.

### 2. The "Companies with Zero Support Tickets" Metric
For Stripe Atlas, the team observed that customer support tickets were largely negative, indicating that users wouldn't recommend the service <a class="yt-timestamp" data-t="00:50:04">[00:50:04]</a>. This led to the adoption of a key metric: "companies that have no support tickets through the incorporation service" <a class="yt-timestamp" data-t="00:50:28">[00:50:28]</a>. This metric directly reflected customer satisfaction and their likelihood to recommend Atlas <a class="yt-timestamp" data-t="00:51:21">[00:51:21]</a>. By focusing on this, Atlas increased the percentage of founders with zero support tickets from 15% to 85% in 18 months, directly correlating with market share growth <a class="yt-timestamp" data-t="00:51:48">[00:51:48]</a>.

This metric:
*   **Speaks to Customer Desire:** If customers saw this metric, they would be "ecstatic" that the company was prioritizing their smooth experience <a class="yt-timestamp" data-t="00:52:16">[00:52:16]</a>.
*   **Motivates the Team:** Engineers could be assigned topics based on support tickets, becoming "PMs" to solve specific user problems, such as automating 83b elections <a class="yt-timestamp" data-t="00:52:50">[00:52:50]</a>.
*   **Aligns Go-to-Market:** It aligns with a go-to-market strategy centered on delighted customers telling their friends <a class="yt-timestamp" data-t="00:59:43">[00:59:43]</a>.

### 3. The "Users Having a Bad Day" Metric
Another powerful metric to track is "users having a bad day" <a class="yt-timestamp" data-t="01:01:05">[01:01:05]</a>. This involves emitting a log line anytime a user encounters a problem, such as a 404 error, delayed payout, or multiple payment declines <a class="yt-timestamp" data-t="01:01:09">[01:01:09]</a>. By creating a stacked bar chart of "bad day reasons" and their frequencies, teams gain eye-opening insights into common pain points <a class="yt-timestamp" data-t="01:01:40">[01:01:40]</a>. This metric helps identify unexpected problems and allows teams to make informed decisions about where to invest resources <a class="yt-timestamp" data-t="01:03:19">[01:03:19]</a>.

### 4. Optimize One Metric, Monitor Others
While multiple metrics are monitored, it's effective to optimize around one primary metric for a period (e.g., a year) <a class="yt-timestamp" data-t="00:55:03">[00:55:03]</a>. For example, within the "zero support tickets" goal, specific KRs can focus on tactical metrics like reducing risk review time <a class="yt-timestamp" data-t="00:56:32">[00:56:32]</a>. This allows teams to avoid perverse incentives by choosing which tactics to pursue and setting clear metrics for them <a class="yt-timestamp" data-t="00:56:39">[00:56:39]</a>. Metrics also help determine when a tactic can be put down, reaching a comfortable level of success <a class="yt-timestamp" data-t="01:15:15">[01:15:15]</a>.

### 5. Good Metric Hygiene
Presentation matters for [[effective_metrics_and_goal_setting_for_data_teams | effective metrics]]. Key practices include:
*   **Meaningful Titles:** Metric titles should evoke feeling and clearly convey the customer mindset, e.g., "companies with zero support tickets" instead of complex, technical names <a class="yt-timestamp" data-t="01:05:40">[01:05:40]</a>.
*   **Visual Clarity:** Maintain consistent x-axes on dashboards, avoid excessive decimal places in percentages, and present data cleanly <a class="yt-timestamp" data-t="01:06:51">[01:06:51]</a>. These aesthetic choices dramatically increase the team's willingness to engage with the dashboard daily <a class="yt-timestamp" data-t="01:07:13">[01:07:13]</a>.
*   **Single Source of Truth:** Centralize metrics on a reliable dashboard system (e.g., "go metrics") to ensure everyone trusts the data and to avoid relying on inconsistent one-off queries <a class="yt-timestamp" data-t="01:08:43">[01:08:43]</a>.
*   **Ritualistic Review:** Establish a ritual of frequently reviewing metrics as a team, using the live dashboard rather than screenshots <a class="yt-timestamp" data-t="01:10:37">[01:10:37]</a>. This continuous engagement helps identify and correct data inaccuracies early <a class="yt-timestamp" data-t="01:10:04">[01:10:04]</a>.

Ultimately, these practices help teams focus on a small number of critical metrics, ensuring they deeply understand what their customers want and whether their tactics are improving the product over time <a class="yt-timestamp" data-t="01:11:08">[01:11:08]</a>. This continuous measurement and adaptation also ties into [[balancing_customer_focus_and_business_metrics | balancing customer focus and business metrics]], ensuring that product quality directly contributes to business success <a class="yt-timestamp" data-t="01:00:31">[01:00:31]</a>.