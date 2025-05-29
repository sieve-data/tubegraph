---
title: Structure of a net worth tracker
videoId: G2UuEnUUCos
---

From: [[theaccountantguy]] <br/> 

A [[net_worth_tracking_with_notion | net worth tracker built using Notion]] is designed to help users monitor their financial progress towards a specific net worth goal <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>. The tracker is structured into several key sections and relies on five types of interconnected databases to function <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.

## Overview of Tracker Sections

The tracker is organized into primary sections to provide a comprehensive financial overview:

*   **Summary Section**
    *   Displays the targeted net worth goal <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.
    *   Shows the current total net worth <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.
    *   Calculates the remaining amount needed to reach the net worth goal <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.
    *   Indicates the total growth achieved in net worth since January <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.
    *   Presents a percentage indicating the proportion of the targeted net worth that has been achieved <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.
*   **Monthly Net Worth Overview**
    *   Provides a breakdown of total assets for each month <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.
    *   Shows total liabilities for each month <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.
    *   Calculates the net worth for each specific month <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>.
    *   Indicates the change in net worth for the month <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>.
*   **Breakdown of Assets**
    *   Categorizes individual assets into five types <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>.
    *   Lists the amount for each asset <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.
    *   Displays the proportion of each asset relative to the total assets <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.
*   **Breakdown of Liabilities**
    *   Specifies four types of liabilities <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.
    *   Shows the corresponding amount for each liability <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.
    *   Presents the proportion of each liability to the total liabilities <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.

## Essential Databases

To [[net_worth_tracking_with_notion | build this net worth tracker]], five specific databases are required <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>:

### 1. Assets and Liabilities Database

This database records all assets and liabilities for each month of the year <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.
*   **Asset Description**: Specifies up to five types of assets <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>.
*   **Opening Balance**: A number property representing the asset's balance at the start of the month <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.
*   **Amount**: Records additions or deletions of assets during the specific period <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.
*   **Closing Balance**: Calculated as the opening balance plus or minus the amount during the month <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.

It is crucial to copy the closing balance of each month and paste it as the opening balance for the subsequent month for all assets and liabilities <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.

### 2. Assets Breakdown Database

This database provides a detailed breakup of all assets and their individual proportions to the total <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.
*   Lists the five asset types created earlier <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.
*   The total amount for each asset from all months is rolled up from the `Assets and Liabilities Database` <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
*   The `Total Assets Value` is calculated and rolled up from another database using a formula <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>.
*   The percentage of each asset's value relative to the total value of all assets combined is calculated <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.

### 3. Liabilities Breakdown Database

Similar to the `Assets Breakdown Database`, this database tracks liabilities and their proportions.
*   Comprises four types of liabilities <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.
*   Calculates the percentage of each liability to the total value of all liabilities <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.

### 4. Net Worth Database

This database is central to [[tracking_savings_and_net_worth | tracking savings and net worth]] changes over time <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>.
*   **Total Assets**: Considers the closing balance of assets for each month <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.
*   **Total Liabilities**: Uses the closing balance of liabilities for each month <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.
*   **Net Worth**: Calculated by deducting liabilities from assets for the month <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.
*   **Change in Net Worth**: Determined by subtracting the opening net worth from the closing net worth of assets and liabilities <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.

All amounts in this database are rolled over from the `Assets and Liabilities Database` <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.

### 5. Net Worth Summary Database

This database consolidates all the information collected from the other databases to provide a high-level summary <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.
*   Calculates five key metrics:
    *   Net worth goal <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>
    *   Total net worth amount <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>
    *   Amount needed to reach the goal <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>
    *   Total growth in net worth <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>
    *   Percentage of net worth achieved relative to the targeted net worth <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>

Values are pulled from the previously discussed databases and totaled as required <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>. This database completes the discussion of the data structure for a [[net_worth_tracking_and_financial_goals | net worth tracking]] system <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>.

## Primary Dashboard Layout

The primary dashboard of the [[net_worth_tracking_with_notion | net worth tracker]] serves as a user interface for all the calculated data <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.

*   The **Summary section** on the dashboard displays the net worth goal, total net worth, amount to goal, total growth, and the percentage of the net worth goal achieved <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>. This section links to the `Net Worth Goal Database` and is set in a gallery layout <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.
*   The **Monthly Net Worth Overview** section specifies total assets, total liabilities, net worth, and change in net worth <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>. It links to the `Net Worth Database` and is also presented in a gallery layout <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>.
*   The **Assets Breakdown** and **Liabilities Breakdown** sections are linked to their respective breakdown databases and are displayed in a gallery layout <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.

This comprehensive structure enables efficient [[personal_finance_tracker | personal finance tracking]] and helps users visualize their progress towards financial goals.