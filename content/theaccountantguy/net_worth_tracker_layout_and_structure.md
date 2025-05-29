---
title: Net Worth Tracker Layout and Structure
videoId: G2UuEnUUCos
---

From: [[theaccountantguy]] <br/> 

A [[building_a_net_worth_tracker_using_notion | net worth tracker using Notion]] is designed to provide a comprehensive overview of financial standing. It features a structured layout encompassing various sections and utilizes multiple interconnected databases to function effectively <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

## Overview of Tracker Sections

The primary interface of the net worth tracker is organized into several key sections:

*   **Summary Section:** This area displays crucial financial metrics, including the targeted net worth goal, the current total net worth, the amount still needed to reach the goal, the total growth achieved since January, and the percentage of the net worth goal attained <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.
*   **Monthly Net Worth Overview:** This section provides a month-by-month breakdown of total assets, total liabilities, net worth for the specific month, and the change in net worth for that period <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.
*   **Assets Breakdown:** Here, individual assets are categorized (into five types) with their respective amounts and their proportion relative to the total assets <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.
*   **Liabilities Breakdown:** Similar to assets, this section details four types of liabilities, their corresponding amounts, and their proportion to the total liabilities <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.

## Database Structure

Building this [[calculating_and_tracking_net_worth_over_time | net worth tracker]] necessitates the use of five distinct databases, each serving a specific purpose <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>:

### 1. Assets and Liabilities Database
This database records all assets and liabilities for each specific month <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.
*   **Asset Description:** Specifies five types of assets <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>.
*   **Opening Balance:** A number property representing the balance at the start of the month <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.
*   **Amount:** Shows additions or deletions of assets during the period <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.
*   **Closing Balance:** Calculated as the opening balance plus the amount for the month <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.
    *   *Note:* The closing balance of one month must be copied to the opening balance of the subsequent month for all assets and liabilities <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.

### 2. Assets Breakdown Database
This database provides a detailed breakup of assets and their individual proportions to the total amount <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>.
*   Lists the five asset types created earlier <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.
*   Includes the total amount for each asset, rolled up from the Assets and Liabilities Database <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
*   Calculates the percentage of each asset to the total value of all assets combined <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.

### 3. Liabilities Breakdown Database
Similar to the assets breakdown, this database comprises four types of liabilities and their proportions <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.

### 4. Net Worth Database
This database calculates key financial figures monthly <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>:
*   **Total Assets:** Considers the closing balance of assets from the Assets and Liabilities Database <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.
*   **Total Liabilities:** Considers the closing balance of liabilities from the Assets and Liabilities Database <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>.
*   **Net Worth:** Calculated by deducting liabilities from assets for the month <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>.
*   **Change in Net Worth:** Calculated by deducting the closing net worth from the opening net worth for the month <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.
    *   *Note:* All amounts in this database are rolled over from the Assets and Liabilities database <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.

### 5. Net Worth Summary (Database)
This section summarizes all the information from the other databases to present key metrics <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>:
*   Net worth goal <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>
*   Total net worth amount <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>
*   Amount to goal <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>
*   Total growth in net worth <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>
*   Percentage of net worth to targeted net worth <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>

## Primary Dashboard Layout

The primary dashboard of this [[setting_up_a_personal_finance_tracker_in_notion | personal finance tracker in Notion]] links and displays the data from the various databases <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>:
*   **Summary Section:** Links to the Net Worth Goal database and is displayed in a gallery layout <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>.
*   **Monthly Net Worth Overview:** Links to the Net Worth Database and is set out in a gallery layout <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>.
*   **Assets Breakdown and Liabilities Breakdown:** These sections are linked to their respective Assets Breakdown and Liabilities Breakdown databases, also set out in a gallery layout <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.

This structured approach allows for detailed [[net_worth_tracking_and_goals_in_notion | Net worth tracking]] and visualization within Notion <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>.