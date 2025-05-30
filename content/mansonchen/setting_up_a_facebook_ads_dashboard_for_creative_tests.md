---
title: Setting Up a Facebook Ads Dashboard for Creative Tests
videoId: 9mGvU3flyLE
---

From: [[mansonchen]] <br/> 

To effectively conduct [[creative_testing_for_facebook_ads | creative testing]] at scale, a dashboard is essential for visualizing and understanding which creative elements, ads, and concepts are performing well <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This article outlines a method for monitoring [[creative_testing_in_facebook_ads | creative tests]] using Facebook's ad reporting, which is considered powerful, flexible, and free, drawing from the same data source as other tools like Motion <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.

## Dashboard Columns

The recommended dashboard setup in Facebook Ads includes specific columns to provide a comprehensive view of ad performance:

*   **Adset Name** <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>: Ad sets are used to group different creative concepts <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. For [[creative_testing_for_facebook_ads | creative testing]], typically 4-6 video or ad variations are uploaded within an ad set, with variables isolated in each variance to identify effective hooks, visuals, or scripts <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.
*   **Ad Name** <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>: The individual ad variations within the ad set <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.
*   **Delivery**: Indicates if the ad is active <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.
*   **Amount Spent**: The total expenditure on the ad <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.
*   **Results/Purchases**: The number of conversions or purchases generated <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.
*   **Cost Per Purchase/Result**: The cost associated with each conversion <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>. A conditional rule can be applied to this metric, similar to Excel or Google Sheets, to visually highlight performance <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>. [[Custom metrics in Facebook Ads | Custom conditional formatting]] can be set for metrics like cost per result, cost per trial, or cost per purchase <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.

### Less Critical Metrics

Additional "soft metrics" that can be monitored include:
*   Impression <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>
*   CPM (Cost Per Mille) <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>
*   Reach <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>
*   Frequency <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>
*   Hook Rate: 3-second video view divided by impression <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>
*   Hold Rate: Throughplay (15-second video view) divided by impression <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>
*   Cost per 3-second video play <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>
*   Average View Duration <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>
*   Link Click CTR (Click-Through Rate) <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>
*   Result Rate <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>

## Campaign Structure for Creative Testing

It is recommended to set up a separate [[creative_testing_for_facebook_ads | creative testing]] campaign, especially for those spending over $50,000 per month <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>. This ensures that ad testing can occur effectively, as Facebook might otherwise spend most of an ad set's budget on a single ad, which may not always be the best performer <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>. Forcing spend to each ad allows for more comprehensive testing, as Facebook's initial guesses on ad performance can sometimes be incorrect <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>.

## Automated Rules for Pausing Underperforming Ads

To manage costs and optimize [[effective_creative_testing_strategies_on_facebook | effective creative testing strategies]], automated triggers should be set up to pause ads that do not meet Key Performance Indicator (KPI) goals <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>. These "gates" are based on spend and conversion performance:

1.  **First Gate**: Pause an ad if it reaches $150 in spend without generating any purchases <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>. Based on observation, there is a very small chance an ad becomes a winner if it hasn't secured any purchases by this spend threshold <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.
2.  **Second Gate**: Pause an ad if it reaches $300 in spend and has a Cost Per Acquisition (CPA) higher than $75 or $80 <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>.
3.  **Third Gate**: Pause an ad if its spend is over $500 and its CPA is over $65 <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>.

These gates help to test more ads efficiently while keeping costs down <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.

## Identifying Winning Ads

An ad is considered "good enough" if its cost per purchase is less than $65 after spending $150 <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>. Winning ads that meet this criterion are then duplicated into winning ad campaigns, which often run worldwide, as opposed to the testing campaign that might be limited to a specific region like the US <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>.

## Creative Win Rate

The **creative win rate** is a crucial metric to monitor <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>. It is calculated by dividing the number of ads that meet the minimum spend criteria and CPA goal by the total number of ad variations tested <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>. For example, if 6 out of 47 ad variations tested over a month hit the CPA goal, the creative win rate is approximately 12-13% <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>. A typical creative win rate observed is around 10%, though rates can range from 2% depending on the scale and whether testing is just starting <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>.

By utilizing this dashboard setup and automated rules, advertisers can efficiently identify successful creative elements and scale their [[scaling_facebook_ads | Facebook Ads]] efforts <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>.