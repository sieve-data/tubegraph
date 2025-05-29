---
title: The importance of AB testing in software development
videoId: hEzpiDuYFoE
---

From: [[lennyspodcast]] <br/> 

A/B testing, also known as experimentation or online controlled experiments, is considered by many as a critical practice in product development to ensure that code changes and new features have a positive impact on users and business metrics <a class="yt-timestamp" data-t="01:17:17">[01:17:17]</a>. It serves as both a safety net for deployments and an oracle for understanding outcomes <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>, <a class="yt-timestamp" data-t="02:52:08">[02:52:08]</a>.

## Why A/B Test Everything?

Every code change and every new feature, no matter how small, should be subjected to an experiment <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. Even minor bug fixes or seemingly insignificant adjustments can have surprising, unexpected impacts <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. It's difficult to experiment too much, and the goal should be to make the marginal cost of running an experiment approach zero <a class="yt-timestamp" data-t="02:55:01">[02:55:01]</a>.

## Surprising Results and Learnings

Experiments often yield unexpected results, highlighting the fallibility of human prediction in product outcomes <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>, <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>.

### Case Studies in Unexpected Success

*   **Bing Ad Title Promotion:** A seemingly trivial change on Bing that involved moving the second line of an ad to the first, making the title larger, resulted in a 12% increase in revenue <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>. This simple modification, which took only a couple of days to implement, generated $100 million at the time without hurting user metrics <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>, <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>.
*   **Airbnb New Tab for Search Results:** Opening a new browser tab when a user clicked on a search result proved to be one of the biggest wins for Airbnb's search team <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>. This idea had been debated and pushed back on by designers but was ultimately highly beneficial <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.

While these "gold nuggets" – small efforts leading to huge gains – are celebrated, they are very rare <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>. Most gains come from "inch by inch" improvements <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>. For example, Bing's relevance team aimed for a 2% annual improvement in their metric, achieved through numerous small gains <a class="yt-timestamp" data-t="00:12:14">[00:12:14]</a>. Similarly, 250 experiments at Airbnb's search relevance led to an overall 6% revenue improvement from many small ideas <a class="yt-timestamp" data-t="00:12:45">[00:12:45]</a>.

### High Failure Rates are Normal

A significant percentage of ideas in software development fail to improve key metrics. Observed failure rates include:
*   **Microsoft (overall):** Around 66% (two-thirds) <a class="yt-timestamp" data-t="00:13:39">[00:13:39]</a>.
*   **Bing (optimized domain):** Around 85% <a class="yt-timestamp" data-t="00:13:52">[00:13:52]</a>.
*   **Airbnb Search Relevance:** 92% of ideas failed to improve the target metric <a class="yt-timestamp" data-t="00:13:08">[00:13:08]</a>.

Other major companies like Booking.com and Google Ads report similar failure rates of 80-90% <a class="yt-timestamp" data-t="00:14:19">[00:14:19]</a>. These high failure rates are humbling, and organizations starting to run experiments are typically humbled early on by smaller changes <a class="yt-timestamp" data-t="00:15:17">[00:15:17]</a>, <a class="yt-timestamp" data-t="00:39:39">[00:39:39]</a>. It's crucial to acknowledge that a significant portion of ideas will not yield positive results <a class="yt-timestamp" data-t="00:22:22">[00:22:22]</a>.

### Learning from Surprising Losers

It's equally important to learn from experiments that produce surprisingly negative results <a class="yt-timestamp" data-t="00:18:13">[00:18:13]</a>. For instance, an improved Windows indexer, which showed better offline test results, killed laptop battery life in a live experiment <a class="yt-timestamp" data-t="00:18:57">[00:18:57]</a>. Such outcomes reveal unexpected factors and inform future design <a class="yt-timestamp" data-t="00:19:17">[00:19:17]</a>.

The concept of a "surprising experiment" is one where the estimated result before the experiment and the actual result differ significantly <a class="yt-timestamp" data-t="00:17:40">[00:17:40]</a>.

## Addressing Concerns about A/B Testing

### Micro-Optimizations vs. Innovation
A common concern is that [[balancing_speed_and_quality_in_software_development | A/B testing]] only leads to micro-optimizations, hindering true innovation <a class="yt-timestamp" data-t="00:20:54">[00:20:54]</a>. However, it's possible to maintain a portfolio of experiments:
*   **Incremental changes:** These move the product in a known successful direction <a class="yt-timestamp" data-t="00:21:54">[00:21:54]</a>.
*   **High-risk, high-reward ideas:** These are more likely to fail but can be "home runs" if successful <a class="yt-timestamp" data-t="00:22:03">[00:22:03]</a>. It is important to allocate some effort to these, while being prepared for most to fail (e.g., 80% failure rate for big bets) <a class="yt-timestamp" data-t="00:22:19">[00:22:19]</a>.

Attempting radical new ideas, like Bing's integration with social media (Twitter and Facebook feeds) <a class="yt-timestamp" data-t="00:22:59">[00:22:59]</a>, may consume significant resources (e.g., 100 person-years) and still fail <a class="yt-timestamp" data-t="00:23:11">[00:23:11]</a>. Even when data shows negative or flat results, organizations may struggle to abort, influenced by sunk cost fallacy <a class="yt-timestamp" data-t="00:23:31">[00:23:31]</a>, <a class="yt-timestamp" data-t="00:37:41">[00:37:41]</a>.

### Avoiding Big Redesigns
Full product redesigns rarely lead to positive results and often require teams to "claw back" lost performance <a class="yt-timestamp" data-t="00:36:33">[00:36:33]</a>. It is generally advisable to:
*   Implement redesigns in steps, testing along the way <a class="yt-timestamp" data-t="00:37:05">[00:37:05]</a>.
*   Decompose large changes into smaller increments (one factor at a time) to learn and adjust <a class="yt-timestamp" data-t="00:38:08">[00:38:08]</a>.
*   Be ready for big redesigns to fail (80% of the time), even if the team is passionate <a class="yt-timestamp" data-t="00:39:10">[00:39:10]</a>, <a class="yt-timestamp" data-t="00:43:21">[00:43:21]</a>.

Shipping features with flat or negative results should be avoided due to maintenance overhead and complexity <a class="yt-timestamp" data-t="00:44:30">[00:44:30]</a>. Even legal requirements should be approached with experimentation, shipping the option that hurts the least <a class="yt-timestamp" data-t="00:45:17">[00:45:17]</a>.

## When to Start A/B Testing

A/B testing requires a sufficient number of users for statistical validity <a class="yt-timestamp" data-t="02:55:16">[02:55:16]</a>.
*   **Tens of thousands of users:** Experiments can start, but only large effects will be detectable <a class="yt-timestamp" data-t="02:53:53">[02:53:53]</a>, <a class="yt-timestamp" data-t="02:56:56">[02:56:56]</a>.
*   **Around 200,000 users:** The "magic starts happening," allowing for more robust testing and the ability to test everything <a class="yt-timestamp" data-t="02:57:32">[02:57:32]</a>.
*   **Below 200,000 users:** Focus on [[building_and_optimizing_an_experimentation_platform | building the culture]] and [[building_and_optimizing_an_experimentation_platform | platform]] so that value can be seen as the user base scales <a class="yt-timestamp" data-t="02:57:52">[02:57:52]</a>.

## Key Concepts for Effective A/B Testing

### Overall Evaluation Criterion (OEC)
The OEC is the primary metric a company optimizes for <a class="yt-timestamp" data-t="02:58:18">[02:58:18]</a>. It's crucial to define an OEC that reflects long-term growth and user value, not just short-term gains <a class="yt-timestamp" data-t="03:28:28">[03:28:28]</a>.

*   **Balancing Metrics:** Purely optimizing for revenue can lead to negative user experiences <a class="yt-timestamp" data-t="02:58:38">[02:58:38]</a>. An OEC should include countervailing metrics (or "guardrail metrics") that measure user experience, such as churn rate, time to find successful results, or percentage of successful sessions <a class="yt-timestamp" data-t="02:58:45">[02:58:45]</a>, <a class="yt-timestamp" data-t="03:09:09">[03:09:09]</a>.
*   **Lifetime Value (LTV):** The OEC should be causally predictive of the user's lifetime value <a class="yt-timestamp" data-t="03:20:07">[03:20:07]</a>. For example, in e-commerce, it's not enough to just convert a user; their satisfaction months later (e.g., product ratings) should be considered <a class="yt-timestamp" data-t="03:11:14">[03:11:14]</a>.

### Institutional Memory and Learning
To maximize value, organizations must document and summarize experiment learnings, fostering [[the_importance_of_following_up_on_results_in_product_management | institutional memory]] <a class="yt-timestamp" data-t="01:17:02">[01:17:02]</a>. This includes:
*   Maintaining internal decks of successes and failures <a class="yt-timestamp" data-t="01:19:35">[01:19:35]</a>.
*   Implementing searchable databases of past experiments (e.g., thousands per year at Microsoft) <a class="yt-timestamp" data-t="01:19:47">[01:19:47]</a>, <a class="yt-timestamp" data-t="02:00:02">[02:00:02]</a>.
*   Holding quarterly meetings to discuss the most surprising (positive or negative) experiments <a class="yt-timestamp" data-t="01:17:28">[01:17:28]</a>.

### Trust in the Platform
Trust is paramount for an experimentation platform because it serves as an "oracle" of truth <a class="yt-timestamp" data-t="02:52:08">[02:52:08]</a>. Loss of trust can undermine the entire data-driven culture.

*   **P-values:** The common interpretation of a p-value (e.g., 0.05 meaning 95% probability that treatment is better) is incorrect <a class="yt-timestamp" data-t="01:02:42">[01:02:42]</a>. It's a conditional probability assuming the null hypothesis is true <a class="yt-timestamp" data-t="01:03:11">[01:03:11]</a>. The actual "false positive risk" (probability that a significant result is wrong) can be much higher (e.g., 26% at Airbnb search with an 8% success rate) <a class="yt-timestamp" data-t="01:04:44">[01:04:44]</a>.
*   **Twyman's Law:** "If any figure looks interesting or different, it is usually wrong" <a class="yt-timestamp" data-t="01:00:56">[01:00:56]</a>. If an experiment result seems too good to be true, it likely indicates a flaw and should be investigated <a class="yt-timestamp" data-t="01:01:13">[01:01:13]</a>.
*   **Sample Ratio Mismatch (SRM):** This is the most common sign of an invalid experiment <a class="yt-timestamp" data-t="00:55:53">[00:55:53]</a>. If the split of users between control and treatment groups deviates from the intended ratio (e.g., 50/50), it's a red flag <a class="yt-timestamp" data-t="00:56:01">[00:56:01]</a>. Common causes include bots or data pipeline issues <a class="yt-timestamp" data-t="00:57:51">[00:57:51]</a>. Organizations should implement checks to flag SRMs, even if it means hiding results until acknowledged, to ensure trust <a class="yt-timestamp" data-t="00:59:37">[00:59:37]</a>.

## Building an Experimentation Culture and Platform

Establishing an experimentation culture and [[building_and_optimizing_an_experimentation_platform | platform]] requires strategic effort:
*   **Build vs. Buy:** Companies must decide whether to build an internal experimentation platform or utilize third-party vendors <a class="yt-timestamp" data-t="01:06:49">[01:06:49]</a>. For new initiatives, third-party products are often a good starting point <a class="yt-timestamp" data-t="01:07:38">[01:07:38]</a>.
*   **Starting Point:** Begin with teams that launch frequently (e.g., weekly sprints, multiple times a day) and have a clear, agreed-upon OEC <a class="yt-timestamp" data-t="01:08:42">[01:08:42]</a>.
*   **Platform Benefits:** A robust platform aims to minimize the marginal cost of running experiments through self-service setup, automated metric definition (potentially thousands of metrics broken into templates), and comprehensive analysis <a class="yt-timestamp" data-t="01:10:34">[01:10:34]</a>. This reduces the need for constant data scientist intervention in analysis <a class="yt-timestamp" data-t="01:11:31">[01:11:31]</a>.
*   **Structured Narratives:** Adopting a structured narrative approach, as pioneered by Amazon, for presenting ideas and feature proposals instead of traditional presentations (like PowerPoint) can significantly improve the quality of discussions and facilitate honest feedback and [[understanding_work_for_product_development | institutional learning]] <a class="yt-timestamp" data-t="01:19:16">[01:19:16]</a>.

## Speeding Up Experiments

While trust is key, speed is also important. To get faster results:
*   **Automated Scorecards:** The platform should provide an automated scorecard immediately after an experiment finishes, eliminating wait times for data scientists to interpret results <a class="yt-timestamp" data-t="01:12:47">[01:12:47]</a>.
*   **Variance Reduction Techniques:** These methods help reduce the variance of metrics, allowing statistically significant results to be achieved with fewer users and in less time <a class="yt-timestamp" data-t="01:13:04">[01:13:04]</a>. Examples include:
    *   **Capping Metrics:** Setting an upper limit on highly skewed metrics (e.g., capping nights booked at 30 days) <a class="yt-timestamp" data-t="01:17:16">[01:17:16]</a>, <a class="yt-timestamp" data-t="01:17:40">[01:17:40]</a>.
    *   **CUPED (Controlled-experiment Using Pre-Experiment Data):** This technique uses pre-experiment data to adjust results, reducing variance without introducing bias <a class="yt-timestamp" data-t="01:13:52">[01:13:52]</a>.