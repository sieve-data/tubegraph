---
title: Building a net worth tracker using Notion
videoId: G2UuEnUUCos
---

From: [[theaccountantguy]] <br/> 

This article details how to [[creating_and_using_a_notion_net_worth_tracker | build a net worth tracker using Notion]] <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>. The tracker is designed to help users monitor their financial progress, offering a comprehensive view of assets, liabilities, and overall net worth. This system is part of a broader approach to [[tracking_personal_finances_in_notion | tracking personal finances in Notion]] <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>.

## Tracker Overview

The net worth tracker is structured into several key sections to provide a complete financial picture <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.

### Summary Section
This section offers an at-a-glance summary of financial goals and current status <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>:
*   **Net Worth Goal Amount**: The target net worth to achieve <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.
*   **Total Net Worth at Present**: Current net worth <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.
*   **Amount Required to Reach Goal**: The difference between the goal and current net worth <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.
*   **Total Growth Achieved**: Net worth growth since January <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.
*   **Percentage Achieved**: Net worth achieved in proportion to the targeted amount <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.

### Monthly Net Worth Overview
This section provides a month-by-month breakdown of financial changes <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>:
*   Total assets for each month <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.
*   Total liabilities for each month <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.
*   Net worth for the month <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.
*   Change in net worth for the month <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>.

### Breakdown of Assets
This section details individual assets, classified into five categories <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>:
*   Amount of each asset <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.
*   Proportion of each asset to the total assets <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.

### Liabilities Breakdown
Similar to assets, this section details liabilities, specifying four types <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>:
*   Corresponding amount of each liability <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.
*   Proportion of each liability to the total amount <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.

## Databases Required
To [[creating_and_using_a_notion_net_worth_tracker | build this net worth tracker]], five types of [[databases_required_for_tracking_net_worth_in_notion | databases]] are required <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>. Each database serves a distinct purpose <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.

### 1. Assets and Liabilities Database
This database records all assets and liabilities for each specific month <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.
*   **Asset Description**: Five types of assets are specified <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>.
*   **Opening Balance**: A number property for the asset balance at the start of the month <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.
*   **Amount**: Shows additions or deletions of assets for the specific period <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.
*   **Closing Balance**: Calculated as the opening balance plus or minus the amount during the month <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.
*   The closing balance of each month must be copied to the opening balance of the subsequent month for all assets and liabilities <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.

### 2. Assets Breakdown Database
This database provides a breakup of all assets and their individual proportions to the total amount <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.
*   It lists the same five assets created earlier <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.
*   The total amount of each asset is rolled up from the Assets and Liabilities database, combining values from all months <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
*   Total assets value is calculated and rolled up from another database using a formula <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>.
*   The percentage of each asset to the total value of all assets combined is calculated and represented by a green bar <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.

### 3. Liabilities Breakdown Database
This database functions similarly to the Assets Breakdown, comprising four types of liabilities <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.

### 4. Net Worth Database
This database calculates key financial figures monthly <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>:
*   **Total Assets**: Considers the closing balance of assets for each month <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.
*   **Total Liabilities**: Considers the closing balance of liabilities for each month <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.
*   **Net Worth**: Calculated by deducting liabilities from assets for the month <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.
*   **Change in Net Worth**: Calculated by deducting the closing net worth from the opening net worth of assets and liabilities <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.
*   All amounts in this database are rolled over from the Assets and Liabilities database <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.

### 5. Net Worth Summary Database
This database summarizes all the calculated data <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>, crucial for [[using_notion_to_monitor_financial_summaries_and_net_worth | monitoring financial summaries and net worth]] <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>:
*   Net worth goal <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.
*   Total net worth amount <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.
*   Amount to goal <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>.
*   Total growth in net worth <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>.
*   Percentage of the net worth to the targeted net worth <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.
*   All values are pulled from the previously discussed databases and totaled as desired <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>.

## Primary Dashboard
The primary dashboard of the net worth tracker integrates all the databases to present a cohesive view <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.

### Summary Section
Displays the net worth goal, total net worth, amount to goal, total growth, and percentage of net worth goal <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>. This section is linked to the net worth goal database and set out in a gallery layout <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.

### Monthly Net Worth Overview
Specifies the total assets, total liabilities, net worth, and change in net worth <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>. This is linked to the net worth database and also set out in a gallery layout <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>.

### Assets Breakdown and Liabilities Breakdown
These sections are linked to their respective databases and are also displayed in a gallery layout <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.