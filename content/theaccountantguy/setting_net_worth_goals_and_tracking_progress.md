---
title: Setting net worth goals and tracking progress
videoId: G2UuEnUUCos
---

From: [[theaccountantguy]] <br/> 

A robust [[building_a_net_worth_tracker_using_notion | net worth tracker using Notion]] can help individuals [[setting_financial_goals_and_net_worth_targets | set financial goals]] and monitor their progress <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. This system allows for a comprehensive overview of financial health, including assets, liabilities, and overall net worth changes <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.

## Components of the Net Worth Tracker

The Notion-based net worth tracker includes several key sections:

### Summary Section
The summary section provides an at-a-glance view of financial targets and current status <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. It typically features:
*   The [[setting_financial_goals_and_net_worth_targets | net worth goal]] amount being targeted <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.
*   The present total net worth <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.
*   The remaining amount required to reach the net worth goal <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.
*   Total growth achieved in net worth since a specific period (e.g., January) <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.
*   A percentage indicating the net worth achieved relative to the targeted amount <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.

### Monthly Net Worth Overview
This section offers a detailed [[monthly_net_worth_overview_and_changes | monthly net worth overview]] of financial changes <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>. It tracks:
*   Total assets for each month <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>.
*   Total liabilities for each month <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.
*   Net worth for the specific month <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.
*   The change in net worth for the month <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>.

### Assets and Liabilities Breakdowns
Separate sections provide detailed breakdowns:
*   **Assets Breakdown:** Specifies individual assets classified into categories, their respective amounts, and their proportion to the total assets <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.
*   **Liabilities Breakdown:** Details different types of liabilities, their corresponding amounts, and their proportion to the total liabilities <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.

## Building the Tracker: Databases

The [[building_a_net_worth_tracker_using_notion | net worth tracker]] is constructed using five types of databases in Notion, each serving a distinct purpose <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>:

### 1. Assets and Liabilities Database
This database is central to recording all assets and liabilities for each specific month <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.
*   **Asset Description:** Lists various types of assets (e.g., five specified categories) <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>.
*   **Opening Balance:** A number property representing the asset's balance at the start of the month <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.
*   **Amount:** Shows additions or deletions of assets during the period <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.
*   **Closing Balance:** Calculated as the opening balance plus or minus the amount changed during the month <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.
    *   *Note:* The closing balance of one month must be manually copied to become the opening balance of the subsequent month for all assets and liabilities <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.

### 2. Assets Breakdown Database
This database provides a breakup of all assets and their individual proportions to the total <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.
*   It lists the same assets from the Assets and Liabilities Database <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.
*   The total amount for each asset is rolled up from the Assets and Liabilities database <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
*   Total assets value is calculated and rolled up from another database using a formula <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>.
*   The percentage of each asset relative to the total value of all assets combined is calculated and displayed <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.

### 3. Liabilities Breakdown Database
Similar to the assets breakdown, this database provides a detailed breakdown of liabilities, typically comprising four types of liabilities <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.

### 4. Net Worth Database
This database calculates key financial figures for each month <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>:
*   **Total Assets:** Considers the closing balance of assets for each month <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.
*   **Total Liabilities:** Uses the closing balance of liabilities for each month <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.
*   **Net Worth:** Calculated by deducting liabilities from assets for the month <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>.
*   **Change in Net Worth:** Determined by deducting the opening net worth from the closing net worth for the period <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.
    *   *Note:* All amounts in this database are rolled over from the Assets and Liabilities database <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.

### 5. Net Worth Summary Database
This database summarizes all the discussed metrics to provide an overall summary <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>. It calculates and displays:
*   [[setting_financial_goals_and_net_worth_targets | Net worth goal]] <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>.
*   Total net worth amount <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.
*   Amount to goal <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>.
*   Total growth in net worth <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.
*   Percentage of net worth achieved relative to the targeted net worth <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.
Values are pulled from the other databases to compile this summary <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>.

## Primary Dashboard
The primary dashboard serves as the central hub for the [[using_notion_to_track_net_worth | Notion net worth tracker]] <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.
*   It displays the **summary section**, including the [[setting_financial_goals_and_net_worth_targets | net worth goal]], total net worth, amount to goal, total growth, and percentage of the net worth goal <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>. This section is linked to the Net Worth Goal database and displayed in a gallery layout <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.
*   The [[monthly_net_worth_overview_and_changes | monthly net worth overview]] is also displayed, showing total assets, total liabilities, net worth, and change in net worth <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>. This is linked to the Net Worth database and also set out in a gallery layout <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>.
*   The **assets breakdown** and **liabilities breakdown** sections are linked to their respective databases and presented in a gallery layout <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.

This comprehensive setup allows for effective [[tracking_savings_goals_and_progress | tracking progress]] towards financial targets <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>.