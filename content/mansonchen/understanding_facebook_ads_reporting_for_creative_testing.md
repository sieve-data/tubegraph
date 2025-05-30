---
title: Understanding Facebook Ads Reporting for Creative Testing
videoId: 9mGvU3flyLE
---

From: [[mansonchen]] <br/> 

To effectively manage [[creative_testing_for_facebook_ads | creative testing]] at scale, a dashboard is essential for visualizing and understanding which creative elements, ads, and concepts are performing well <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This guide outlines how to use Facebook's ad reporting, which is a powerful and flexible tool <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>.

## Setting Up Your Dashboard Columns

When [[setting_up_a_facebook_ads_dashboard_for_creative_tests | setting up a Facebook Ads dashboard for creative tests]], the following columns are recommended:

*   **Adset Name** The concept for [[creative_testing_in_facebook_ads | creative testing in Facebook ads]] is typically grouped at the ad set level <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. Within each ad set, about four to six ad variations are uploaded, with variables isolated to determine what works (e.g., hooks, visuals, scripts, concepts) <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.
*   **Ad Name** This column breaks down performance at the individual ad level <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.
*   **Delivery** Indicates if the ad is active <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.
*   **Amount Spent** The total amount spent on the ad so far <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.
*   **Results / Purchases** The number of desired results (e.g., purchases) <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.
*   **Cost Per Purchase / Cost Per Result** The cost associated with each desired result <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>. [[using_conditional_formatting_in_facebook_ads_reporting | Conditional formatting]] can be applied to this metric for easy visualization of performance <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>.

### Less Important Metrics

While the above are crucial, these [[key_metrics_for_evaluating_creative_performance_in_facebook_ads | key metrics for evaluating creative performance in Facebook Ads]] can also provide valuable insights:

*   **Impression** <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>
*   **CPM** (Cost Per Mille/Thousand Impressions) <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>
*   **Reach** <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>
*   **Frequency** <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>
*   **Hook Rate** Defined as 3-second video views divided by impressions <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.
*   **Hold Rate** Defined as throughplays (15-second video views) divided by impressions <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.
*   **Cost Per 3 Second Video Play** <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>
*   **Average View Duration** <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>
*   **Link Click CTR** (Click-Through Rate) <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>
*   **Result Rate** <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>

## Campaign Structure for Effective Testing

It is highly recommended to set up a separate [[facebook_creative_testing_strategies | creative testing campaign]] for ad accounts spending above $50,000 per month <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>. This is because Facebook often allocates most of an ad set's budget to a single ad, and its initial guess might not be the best performing one <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>. Isolating tests allows for more controlled evaluation <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.

## Automated Triggers for Pausing Ads

To keep costs low and efficiently test more ads, implement automated rules (gates) to pause ads that do not meet KPI goals <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.

*   **First Gate:** Pause an ad after $150 in spend if it has zero purchases/conversions <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>. This threshold is based on observing ad performance and the likelihood of becoming a winner <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.
*   **Second Gate:** If an ad has spent $300 and has a CPA (Cost Per Acquisition) higher than $75 or $80, pause it <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>.
*   **Third Gate:** If an ad has spent over $500 and its CPA is over $65, pause it <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>.

## Identifying Winning Ads and [[Scaling Facebook Ads | Scaling]]

An ad is considered "good enough" if its cost per purchase is less than $65 after $150 in spend <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>. Winning ads can then be duplicated into winning ad campaigns, often run worldwide, especially if the [[effective_creative_testing_strategies_on_facebook | creative testing strategy]] was conducted in a specific region like the US <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>.

## Creative Win Rate

The **Creative Win Rate** is another important metric to monitor <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>. It's calculated by dividing the number of ads that meet your CPA goal by the total number of ad variations tested <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>. For example, if 6 out of 47 tested ad variations hit the CPA goal, the win rate is approximately 12-13% <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.
*   A common win rate is around 10% <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>, though it can be as low as 2% <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>.
*   This rate can vary significantly based on the scale of your testing and whether you are new to testing <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>.

## Customizing Your Reporting

Facebook's ad reporting allows for the creation of [[custom_metrics_in_facebook_ads | custom metrics in Facebook Ads]] and conditional formatting rules to suit specific KPIs, such as cost per result, cost per trial, or cost per purchase <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.