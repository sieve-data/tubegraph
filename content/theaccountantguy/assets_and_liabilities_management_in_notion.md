---
title: Assets and liabilities management in Notion
videoId: G2UuEnUUCos
---

From: [[theaccountantguy]] <br/> 

This article details how to build a [[tracking_personal_finances_in_notion | net worth tracker]] using [[using_notion_for_personal_finance_management | Notion]] <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>. This tracker provides a comprehensive view of assets and liabilities over time.

## Net Worth Tracker Overview

The [[tracking_personal_finances_in_notion | net worth tracker]] in [[using_notion_for_personal_finance_management | Notion]] includes several key sections:

*   **Summary Section** <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>:
    *   Net worth goal amount <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>
    *   Current total net worth <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>
    *   Amount required to reach the net worth goal <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>
    *   Total growth in net worth since January <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>
    *   Percentage of net worth achieved relative to the target <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>
*   **Monthly Net Worth Overview** <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>:
    *   Total assets for each month <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>
    *   Total liabilities for each month <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>
    *   Net worth for the month <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>
    *   Change in net worth for the month <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>
*   **Assets Breakdown** <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>:
    *   Individual assets classified into five categories <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>
    *   Amount of each asset <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>
    *   Proportion of each asset to total assets <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>
*   **Liabilities Breakdown** <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>:
    *   Four types of liabilities <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>
    *   Corresponding amount and proportion of each liability to the total <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>

## Required Databases for the Tracker

Building this [[tracking_personal_finances_in_notion | net worth tracker]] requires five types of databases in [[using_notion_for_personal_finance_management | Notion]] <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>:

### 1. Assets and Liabilities Database

This database records all assets and liabilities for each specific month <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.

*   **Asset Description**: Specifies five types of assets <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>.
*   **Opening Balance**: A number property representing the asset's balance at the start of the month <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.
*   **Amount**: Shows additions or deletions of assets for the specific period <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.
*   **Closing Balance**: Calculated by adding the opening balance to the amount during the month <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.
*   The closing balance of each month must be copied and pasted as the opening balance for the subsequent month for all assets and liabilities <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.

### 2. Assets Breakdown Database

This database provides a breakup of all assets and their individual proportions to the total amount <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.

*   Lists the same five assets created earlier <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.
*   **Total Amount**: Represents the combined total amount of each asset from all months, rolled up from the earlier database <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
*   **Total Assets Value**: Calculated and rolled up from another database using a formula <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>.
*   **Percentage**: Calculates the percentage of each asset relative to the total value of all combined assets, visualized with a green bar <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.

### 3. Liabilities Breakdown Database

This database is similar to the Assets Breakdown, comprising four types of liabilities <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.

### 4. Net Worth Database

This database calculates key financial figures <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>:

*   **Total Assets**: Considers the closing balance of assets for each month <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.
*   **Total Liabilities**: Considers the closing balance of liabilities for each month <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.
*   **Net Worth**: Calculated by deducting liabilities from assets for the month <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>.
*   **Change in Net Worth**: Calculated by deducting the closing net worth from the opening net worth of assets and liabilities <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.
*   All amounts in this database are rolled over from the Assets and Liabilities Database <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.

### 5. Net Worth Summary Database

This database summarizes all the discussed elements <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>.

*   Calculates five key figures <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>:
    *   Net worth goal <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>
    *   Total net worth amount <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>
    *   Amount to goal <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>
    *   Total growth in net worth <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>
    *   Percentage of net worth to the targeted net worth <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>
*   All values are pulled and totaled from the previously discussed databases <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>.

## Primary Dashboard

The primary dashboard of the [[tracking_personal_finances_in_notion | net worth tracker]] integrates all the data <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>:

*   **Summary Section**: Displays the net worth goal, total net worth, amount to goal, total growth, and percentage of net worth goal <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>. This section is linked to the Net Worth Goal database and displayed in a gallery layout <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.
*   **Monthly Net Worth Overview**: Specifies total assets, total liabilities, net worth, and change in net worth <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>. It is linked to the Net Worth database and set out in a gallery layout <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>.
*   **Assets Breakdown** and **Liabilities Breakdown**: These sections are linked to their respective databases and also displayed in a gallery layout <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.