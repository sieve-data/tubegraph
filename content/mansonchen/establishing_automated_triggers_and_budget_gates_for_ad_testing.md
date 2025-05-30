---
title: Establishing Automated Triggers and Budget Gates for Ad Testing
videoId: 9mGvU3flyLE
---

From: [[mansonchen]] <br/> 

When performing any form of [[setting_up_a_facebook_ads_dashboard_for_creative_tests | creative testing]] at scale, it is crucial to utilize a dashboard to visualize and understand which creative elements, ads, and concepts are performing effectively <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. Facebook's ad reporting is a powerful, free tool that can serve this purpose, pulling from the same data source as other platforms like Motion <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.

## Setting Up for Testing

It is recommended to set up a separate [[testing_and_iteration_for_successful_ads | creative testing]] campaign, especially for accounts spending above $50,000 a month <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>. This separation is vital because Facebook often allocates most of an [[budget_allocation_for_ad_sets | ad set's]] budget to a single ad, and this initial allocation may not always identify the best performer <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>. Separating campaigns helps force spend to each ad variation to ensure adequate testing <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.

Within an [[budget_allocation_for_ad_sets | ad set]], multiple [[testing_and_optimizing_ad_variations | ad variations]] (typically four to six video or ad variations) can be uploaded, with [[setting_up_ad_tests_and_defining_variables | variables isolated]] within each to determine which hooks, visual hooks, scripts, or concepts are most effective <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. The concept is generally grouped at the [[budget_allocation_for_ad_sets | ad set]] level <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.

The goal of this setup is to [[testing_strategies_for_successful_ads | test more ads]] while maintaining low costs <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.

## Key Metrics for Monitoring

A comprehensive ad reporting dashboard should include columns such as:
*   **Adset Name** <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>
*   **Ad Name** <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>
*   **Delivery Status** (active/inactive) <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>
*   **Amount Spent** <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>
*   **Amount of Results/Purchases** <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>
*   **Cost Per Purchase/Result** (with conditional formatting for easy visualization) <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>

Less critical but still useful metrics include:
*   **Impression** <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>
*   **CPM** <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>
*   **Reach** <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>
*   **Frequency** <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>
*   **Hook Rate** (3-second video view divided by impression) <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>
*   **Hold Rate** (through play or 15-second video view divided by impression) <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>
*   **Cost Per 3-Second Video Play** <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>
*   **Average View Duration** <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>
*   **Link Click CTR** <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>
*   **Result Rate** <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>

## Automated Triggers and Budget Gates

To optimize spending and identify winning ads quickly, it's essential to set up [[automated_stoplosses_in_creative_testing | automated triggers to pause ads]] that do not meet Key Performance Indicator (KPI) goals <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>. These "gates" help control costs and focus budget on effective ads.

Here are examples of budget gates:

*   **First Gate:** If an ad spends $150 and achieves zero purchases, it is paused <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>. This threshold is based on observations that ads without purchases at this spend level have a very low chance of becoming winners <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.
*   **Second Gate:** If an ad spends $300 and its Cost Per Acquisition (CPA) is higher than $75 or $80, it is paused <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>.
*   **Third Gate:** If an ad spends over $500 and its CPA is over $65, it is paused <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>.

> [!TIP] Conditional Formatting
> Utilize conditional formatting rules, similar to Excel or Google Sheets, to visually highlight ads that are working or not based on your defined KPIs <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>. For example, if an ad has a cost per purchase less than $65 after $150 in spend, it can be considered a "good enough" ad <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.

## Identifying Winning Ads and Win Rate

Ads that meet the defined criteria (e.g., cost per purchase less than $65 after $150 in spend) are then duplicated into winning ad campaigns, often run worldwide <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>.

Monitoring the **creative win rate** is also valuable <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>. This is calculated by dividing the number of ads that meet your CPA goal by the total number of ad variations tested that meet minimum spend criteria <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>. A typical creative win rate is around 10%, though it can vary significantly based on the scale of testing and whether testing is just beginning <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>. For example, in one case, testing 47 different [[testing_and_optimizing_ad_variations | ad variations]] resulted in 6 ads hitting the CPA goal, yielding a creative win rate of approximately 12-13% <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>. This [[iterative_testing_process_to_find_winning_ads | iterative testing process]] helps to continuously identify and scale effective ad creatives.