---
title: Using Conditional Formatting in Facebook Ads Reporting
videoId: 9mGvU3flyLE
---

From: [[mansonchen]] <br/> 

To effectively manage [[creative_testing_in_facebook_ads | creative testing]] at scale, a dashboard is essential for visualizing and understanding which creative elements, ads, and concepts are performing well <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. Facebook's ad reporting is a powerful, flexible, and free tool that pulls data from the same source as other platforms like Motion <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.

## Setting Up Your Reporting for Creative Testing

When conducting [[creative_testing_for_facebook_ads | creative testing]], the strategy involves uploading approximately four to six video or ad variations within an ad set <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>. Variables are isolated within each variation to identify which hooks, visual elements, or scripts are most effective <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. The overall concept is grouped at the ad set level <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>, with individual ad names listed within the ad set <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.

It is recommended to set up a separate [[creative_testing_in_facebook_ads | creative testing]] campaign, especially for ad accounts spending over $50,000 per month <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>. This helps in dedicated testing, as Facebook might otherwise disproportionately allocate budget to one ad within an ad set, even if it's not the best performer <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.

### Essential Columns for Your Report

Key columns to include in your Facebook Ads report for [[creative_testing_in_facebook_ads | creative testing]] are:
*   Adset name <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>
*   Ad name <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>
*   Delivery status (active or not) <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>
*   Amount spent <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>
*   Number of results (e.g., purchases) <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>
*   Cost per purchase or cost per result <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>

Less critical but still useful metrics include:
*   Impression <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>
*   CPM <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>
*   Reach <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>
*   Frequency <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>
*   Hook rate (3-second video view divided by impressions) <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a> <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>
*   Hold rate (through play or 15-second video view divided by impressions) <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a> <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>
*   Cost per 3-second video play <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>
*   Average view duration <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>
*   Link click CTR <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>
*   Result rate <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>

## Implementing Conditional Formatting

Conditional formatting is a powerful feature in Facebook Ads reporting, similar to Excel or Google Sheets, allowing for easy visualization of ad performance <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>. This feature can be applied to metrics like "cost per purchase" or "cost per result" to quickly identify what's working <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.

A common rule for identifying successful ads is: if an ad has a cost per purchase less than $65 after $150 in spend, it's considered good enough <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>. These winning ads can then be duplicated into main winning ad campaigns, often run worldwide, while the [[creative_testing_in_facebook_ads | creative testing]] campaign might be localized (e.g., in the US) <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>.

### Automated Trigger Rules for Pausing Ads

To manage ad spend and optimize [[creative_testing_in_facebook_ads | creative testing]], automated triggers can be set to pause ads that do not meet Key Performance Indicator (KPI) goals <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>. These triggers are based on observed ad performance and how ads typically [[scaling_facebook_ads | scale]] over time:

1.  **First Gate**: Pause an ad if it has spent $150 and received zero purchases. There's a very small chance such an ad will become a winner <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>. This helps test more ads while keeping costs low <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.
2.  **Second Gate**: Pause an ad if it has spent $300 and its Cost Per Acquisition (CPA) is higher than $75 or $80 <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>.
3.  **Third Gate**: Pause an ad if its spend is over $500 and its CPA is over $65 <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>.

## Creative Win Rate

Monitoring your [[key_metrics_for_evaluating_creative_performance_in_facebook_ads | creative win rate]] is another important metric <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>. This is calculated by dividing the number of ads that meet your CPA goal (or other criteria) by the total number of ad variations tested that have met minimum spend criteria <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>. For example, if 6 out of 47 tested ad variations hit the CPA goal, the win rate would be approximately 12-13% <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>. A typical win rate is around 10%, though it can range from 2% depending on the scale and maturity of testing <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>.