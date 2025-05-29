---
title: Using Notion for Financial Tracking
videoId: G2UuEnUUCos
---

From: [[theaccountantguy]] <br/> 

This article describes how to build a net worth tracker using [[using_notion_for_personal_finance | Notion]] <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>. The tracker includes a summary, a monthly overview, and breakdowns of assets and liabilities <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.

## Tracker Sections Overview

The net worth tracker is designed with several key sections:
*   **Summary Section** This displays the net worth goal, current total net worth, amount needed to reach the goal, total growth achieved since January, and the percentage of the net worth goal achieved <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.
*   **Monthly Net Worth Overview** This section provides monthly totals for assets, liabilities, net worth for the month, and the change in net worth for that month <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.
*   **Assets Breakdown** This details individual assets, classifying them into five categories, showing their amount, and their proportion to total assets <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.
*   **Liabilities Breakdown** Similar to assets, this section specifies four types of liabilities, their corresponding amounts, and their proportion to the total liabilities <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.

## Building the Tracker: Database Requirements

To build this net worth tracker, [[using_databases_for_financial_tracking_in_notion | five types of databases]] are required <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>. Each database has distinct requirements <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.

### Assets and Liabilities Database

This database is used to record all assets and liabilities for each specific month during the year <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.
*   **Asset Description** Specifies up to five types of assets <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>.
*   **Opening Balance** A number property for the asset's balance at the start of the month <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.
*   **Amount** Shows additions or deletions of assets for the specific period <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.
*   **Closing Balance** Calculated as the opening balance plus the amount during the month <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.

For continuous tracking, the closing balance of each month must be copied to the opening balance of the subsequent month for all assets <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>. The same process is repeated for the liabilities database <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>. This method records assets and liabilities monthly with opening balance, amount, and closing balance <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>.

### Assets Breakdown

This database provides a breakup of all assets and their individual proportions to the total amount <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.
*   It lists the same five assets created earlier <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.
*   The total amount of each asset from all months combined is represented in a rolled-up formula from the earlier database <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
*   Total assets value is calculated and rolled up from another database using a formula <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>.
*   The percentage of each asset to the total value of all combined assets is calculated and represented visually <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.

The same process is repeated for the liabilities breakdown, which comprises four types of liabilities <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.

### Net Worth Database

In this database, the following are calculated for each subsequent month:
*   **Total Assets** Considers the closing balance of assets for each month <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.
*   **Total Liabilities** Considers the closing balance of liabilities for each month <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>.
*   **Net Worth** Calculated by deducting liabilities from assets for the month <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>.
*   **Change in Net Worth** Calculated by deducting the closing net worth from the opening net worth of assets and liabilities <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.

All amounts in this database are rolled over from the Assets and Liabilities Database <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.

### Net Worth Summary

This database summarizes all previously discussed financial metrics <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>. It calculates:
*   Net worth goal <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>
*   Total net worth amount <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>
*   Amount to goal <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>
*   Total growth in net worth <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>
*   Percentage of net worth to the targeted net worth <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>

All values are pulled from the previously discussed databases and totaled as desired <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>.

## Primary Dashboard Overview

The primary dashboard of the net worth tracker provides a consolidated view of the financial data <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.
*   **Summary Section** Displays the net worth goal, total net worth, amount to goal, total growth, and the percentage of the net worth goal <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>. This section links to the Net Worth Goal database and is set out in a gallery layout <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.
*   **Monthly Net Worth Overview** Specifies total assets, total liabilities, net worth, and change in net worth <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>. This is linked to the Net Worth database and also set out in a gallery layout <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>.
*   **Assets Breakdown and Liabilities Breakdown** These sections are linked to their respective databases and are displayed using the gallery layout <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.

This setup facilitates [[how_to_set_up_and_use_a_personal_finance_tracker_in_notion | setting up a finance tracker in Notion]] for comprehensive personal financial tracking <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>.