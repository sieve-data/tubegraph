---
title: Overview of net worth goal and progress tracking
videoId: G2UuEnUUCos
---

From: [[theaccountantguy]] <br/> 

This article outlines how to [[building_a_net_worth_tracker_using_notion | build a net worth tracker using Notion]] <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>, designed to help monitor and achieve [[setting_financial_goals_and_net_worth_tracking | net worth goals]] <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>. The [[creating_and_using_a_notion_net_worth_tracker | net worth tracker]] includes various sections for summarizing financial data and visualizing progress <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.

## Key Sections of the Net Worth Tracker

### Summary Section
The [[using_notion_to_monitor_financial_summaries_and_net_worth | summary section]] provides a high-level overview of financial progress <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. It includes:
*   The [[setting_financial_goals_and_net_worth_tracking | net worth goal]] amount being targeted <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>.
*   The total net worth at present <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.
*   The amount still required to reach the [[setting_financial_goals_and_net_worth_tracking | net worth goal]] <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.
*   The total growth achieved in net worth since January <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.
*   A percentage indicating the net worth achieved in proportion to the targeted amount <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.

### Monthly Net Worth Overview
The [[monthly_net_worth_breakdown_including_assets_and_liabilities | monthly net worth overview]] provides a detailed breakdown of financial changes on a monthly basis <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>. This section specifies:
*   Total assets for each month <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>.
*   Total liabilities <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.
*   Net worth for the specific month <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.
*   The change in net worth for the month <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>.

### Asset and Liability Breakdowns
These sections detail the composition of assets and liabilities <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>:
*   **Assets Breakdown**: Individual assets are classified into five categories, showing the amount of each asset and its proportion to the total assets <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.
*   **Liabilities Breakdown**: Specifies four types of liabilities, along with their corresponding amounts and proportions relative to the total liabilities <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.

## Underlying Databases for the Net Worth Tracker
Building this [[creating_and_using_a_notion_net_worth_tracker | net worth tracker]] requires the use of five distinct databases in Notion, each serving a specific function <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>:

### 1. Assets and Liabilities Database
This database records all assets and liabilities for each specific month during the year <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>. It includes:
*   **Asset Description**: Five types of assets are specified <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.
*   **Opening Balance**: A number property representing the balance at the start of the month <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.
*   **Amount**: Shows additions or deletions of assets/liabilities for the period <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.
*   **Closing Balance**: Calculated as the opening balance plus or minus the amount during the month <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.
    *   The closing balance of each month for all assets and liabilities must be copied and pasted as the opening balance of the subsequent month <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.

### 2. Assets Breakdown Database
This database provides a breakup of all assets and their individual proportions to the total amount <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>. It lists the same five asset categories, with their total amounts for each month rolled up from the Assets and Liabilities Database <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>. The total assets value is calculated and rolled up from another database using a formula <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>, and the percentage of each asset to the total value is calculated and shown <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.

### 3. Liabilities Breakdown Database
Similar to the Assets Breakdown Database, this one comprises four types of liabilities and follows the same calculation methodology for proportions <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.

### 4. Net Worth Database
This database calculates key financial figures <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>:
*   **Total Assets**: Considers the closing balance of assets from each month <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.
*   **Total Liabilities**: Uses the closing balance of liabilities for each month <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.
*   **Net Worth**: Calculated by deducting liabilities from assets for the month <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
*   **Change in Net Worth**: Determined by deducting the opening net worth from the closing net worth of assets and liabilities <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.
All amounts in this database are rolled over from the Assets and Liabilities Database <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.

### 5. Net Worth Summary Database
This database summarizes all the figures discussed previously <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>. It calculates five key items <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>:
*   [[setting_financial_goals_and_net_worth_tracking | Net worth goal]] <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.
*   Total net worth amount <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.
*   Amount to goal <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.
*   Total growth in net worth <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.
*   The percentage of the net worth to the targeted net worth <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.
Values are pulled and totaled from the other databases <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>.

## Primary Dashboard
The [[summarizing_and_visualizing_net_worth_data_in_a_dashboard | primary dashboard]] of the [[creating_and_using_a_notion_net_worth_tracker | net worth tracker]] integrates all these sections for a comprehensive view <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>:
*   The [[using_notion_to_monitor_financial_summaries_and_net_worth | summary section]] displays the net worth goal, total net worth, amount to goal, total growth, and percentage of net worth goal, linked to the Net Worth Goal Database and set in a gallery layout <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>.
*   The [[monthly_net_worth_breakdown_including_assets_and_liabilities | monthly net worth overview]] shows total assets, liabilities, net worth, and change in net worth, linked to the Net Worth Database and displayed in a gallery layout <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>.
*   The assets breakdown and liabilities breakdown sections are linked to their respective databases and also presented in a gallery layout <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.