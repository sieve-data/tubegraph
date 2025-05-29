---
title: Strategies for measuring product success
videoId: qbZQjprTnrU
---

From: [[lennyspodcast]] <br/> 

Understanding and measuring product success is crucial for building and scaling products. Jeff Weinstein, a product leader at Stripe, emphasizes that a product manager's core responsibility is to achieve product-market fit <a class="yt-timestamp" data-t="00:46:00">[00:46:00]</a>. To determine if product-market fit has been achieved, one must look at both quantitative charts showing growth and qualitative feedback like tweets <a class="yt-timestamp" data-t="00:46:09">[00:46:09]</a>.

## Qualitative and Quantitative Metrics: Deep Siblings and Equals
Metrics and qualitative feedback are considered "deep, deep siblings and equals" <a class="yt-timestamp" data-t="00:46:25">[00:46:25]</a>. While charts indicate economic viability and scalability, direct customer feedback provides the necessary texture and understanding of user experience <a class="yt-timestamp" data-t="00:46:34">[00:46:34]</a>.

## Customer-Centric Metrics
Metrics, at their best, are a numerical representation of the value being provided to the customer <a class="yt-timestamp" data-t="00:46:50">[00:46:50]</a>. It's essential to measure success from the customer's perspective, rather than focusing solely on internal-oriented metrics like the number of logins <a class="yt-timestamp" data-t="00:47:15">[00:47:15]</a>. The question should be: how many people accomplished what they were trying to do after they logged in? <a class="yt-timestamp" data-t="00:47:38">[00:47:38]</a>

Choosing a small number of key metrics forces important trade-offs and decisions, helping larger groups of people align and make progress over time <a class="yt-timestamp" data-t="00:47:51">[00:47:51]</a>.

## Case Study: Stripe Atlas and the "Zero Support Tickets" Metric
When Jeff Weinstein started working on Stripe Atlas, a service for incorporating new companies <a class="yt-timestamp" data-t="01:14:00">[01:14:00]</a>, he observed that founders were frequently unhappy, often submitting support tickets <a class="yt-timestamp" data-t="00:49:08">[00:49:08]</a>. The team asked: "Why would someone recommend Atlas to a friend?" <a class="yt-timestamp" data-t="00:49:48">[00:49:48]</a>

The answer led to a key metric: "companies that have no support tickets through the incorporation service" <a class="yt-timestamp" data-t="00:50:28">[00:50:28]</a>. This metric measured the percentage of founders who completed the entire incorporation process—from the first page load to two weeks post-completion—without submitting any support tickets <a class="yt-timestamp" data-t="00:50:35">[00:50:35]</a>.

Initially, only 15% of founders achieved this "zero support tickets" status <a class="yt-timestamp" data-t="00:51:21">[00:51:21]</a>. Over 18 months, by analyzing support tickets and baking solutions into the product, this figure was driven up to 85% <a class="yt-timestamp" data-t="00:51:48">[00:51:48]</a>. This improvement directly correlated with an increase in market share, demonstrating the metric's effectiveness in [[implementing_productled_growth | product-led growth]] <a class="yt-timestamp" data-t="00:51:57">[00:51:57]</a>.

By focusing on this metric, engineers were empowered to act as product managers, identifying issues from support tickets and designing solutions directly <a class="yt-timestamp" data-t="00:52:57">[00:52:57]</a>. This approach led to significant product improvements, such as automating 83(b) elections, building a custom signing service, and turning every step into a single click <a class="yt-timestamp" data-t="00:53:10">[00:53:10]</a>.

## The "Users Having a Bad Day" Metric
Another valuable metric is "users having a bad day" <a class="yt-timestamp" data-t="01:01:05">[01:01:05]</a>. This involves emitting a log line anytime a user encounters a problem, such as hitting a 404 error, experiencing a delayed payout, or having multiple payment declines <a class="yt-timestamp" data-t="01:01:09">[01:01:09]</a>.

By brainstorming what would cause a customer to have a bad day and then tracking these events, a stacked bar chart can reveal the frequency of different "bad day" reasons <a class="yt-timestamp" data-t="01:01:30">[01:01:30]</a>. This provides eye-opening insights, helping teams prioritize which issues to address and eradicate <a class="yt-timestamp" data-t="01:01:45">[01:01:45]</a>. It's a way to scale understanding of users through metrics <a class="yt-timestamp" data-t="01:02:24">[01:02:24]</a>.

## Best Practices for Metrics and Dashboards
*   **Customer-Facing Titles**: Metrics should have titles that "make you feel something" and resonate with the customer's experience, e.g., "companies with zero support tickets" <a class="yt-timestamp" data-t="01:05:27">[01:05:27]</a>. This brevity and customer focus helps foster a shared understanding and motivation within the company <a class="yt-timestamp" data-t="01:05:58">[01:05:58]</a>.
*   **Good Hygiene**: Dashboards should adhere to good visual hygiene, such as appropriate significant digits for percentages and consistent x-axes for all measures <a class="yt-timestamp" data-t="01:06:51">[01:06:51]</a>. This increases the frequency with which people want to open and use the dashboard daily <a class="yt-timestamp" data-t="01:07:13">[01:07:13]</a>.
*   **Frequent Review**: Teams should regularly review their metrics in a discoverable, trusted place, rather than relying on one-off queries or screenshots <a class="yt-timestamp" data-t="01:09:43">[01:09:43]</a>. This ritual builds confidence in the data and helps identify and correct any inaccuracies over time <a class="yt-timestamp" data-t="01:09:52">[01:09:52]</a>.
*   **Limited Number of Metrics**: To ensure proper care and understanding, focus on a small number of critical metrics that truly reflect customer needs and drive the business forward <a class="yt-timestamp" data-t="01:10:59">[01:10:59]</a>.

## Connecting Metrics to Business Value
Obsession with user experience and quality directly correlates with growth and revenue <a class="yt-timestamp" data-t="01:25:29">[01:25:29]</a>. If a product isn't solving a burning problem, no amount of craft or delight will make it successful <a class="yt-timestamp" data-t="01:19:00">[01:19:00]</a>. The ultimate sign that a problem is burning enough to be solved is a customer's willingness to *pay* for the solution, not just *say* they would pay <a class="yt-timestamp" data-t="00:39:27">[00:39:27]</a>.

To ensure long-term product success, it's crucial to connect product quality and customer experience to economic viability. Products should demonstrate why they are the best customer acquisition channel or a strong margin-generating, ecosystem-growing part of the business <a class="yt-timestamp" data-t="02:09:22">[02:09:22]</a>. This provides confidence for continued investment and helps build a sustainable competitive advantage <a class="yt-timestamp" data-t="02:10:02">[02:10:02]</a>. This holistic approach ensures that [[effective_product_management_strategies | product management strategies]] align with business goals.