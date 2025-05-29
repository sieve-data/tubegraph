---
title: Monthly net worth breakdown including assets and liabilities
videoId: G2UuEnUUCos
---

From: [[theaccountantguy]] <br/> 

This article outlines how to build a [[creating_and_using_a_notion_net_worth_tracker | net worth tracker]] using [[using_notion_to_monitor_financial_summaries_and_net_worth | Notion]] to monitor and break down monthly net worth, including assets and liabilities <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

## Tracker Sections Overview

The tracker is structured into several key sections:

*   **Summary Section**: Displays the [[setting_financial_goals_and_net_worth_tracking | net worth goal]], current [[overview_of_net_worth_goal_and_progress_tracking | total net worth]], amount needed to reach the goal, total growth since January, and the percentage of the [[setting_financial_goals_and_net_worth_tracking | net worth goal]] achieved <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.
*   **Monthly Net Worth Overview**: Provides a monthly breakdown of total assets, total liabilities, net worth for the month, and the change in net worth for that period <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.
*   **Assets Breakdown**: Categorizes individual assets into five types, showing their respective amounts and their proportion to the total assets <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.
*   **Liabilities Breakdown**: Specifies four types of liabilities, detailing their corresponding amounts and their proportion to the total liabilities <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.

## Building the Net Worth Tracker: Databases

Building this [[creating_and_using_a_notion_net_worth_tracker | net worth tracker]] requires the use of five distinct databases <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>.

### 1. Assets and Liabilities Database

This database is where all assets and liabilities are recorded for each specific month during the year <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.

*   **Asset/Liability Description**: Records five specified types of assets <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>.
*   **Opening Balance**: A number property representing the balance at the start of the month <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.
*   **Amount (Addition/Deletion)**: Shows additions or deletions of assets/liabilities for the specific period <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.
*   **Closing Balance**: Calculated as the opening balance plus/minus the amount during the month <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.
    *   *Important Note*: The closing balance of each month for all assets and liabilities must be copied and pasted onto the opening balance of the subsequent month <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.

### 2. Assets Breakdown Database

This database provides a breakup of all assets and their individual proportions to the total amount <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.

*   It lists the same five assets created earlier <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.
*   The total amount for each asset is rolled up from the Assets and Liabilities Database <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
*   The [[overview_of_net_worth_goal_and_progress_tracking | total assets]] value is calculated and rolled up from another database using a formula <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>.
*   The percentage of each asset to the total value of all assets combined is calculated and represented <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.

### 3. Liabilities Breakdown Database

Similar to the assets breakdown, this database comprises four types of liabilities, detailing their amounts and proportions <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.

### 4. Net Worth Database

This database calculates the total assets, total liabilities, net worth (assets less liabilities), and the change in net worth for each subsequent month <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.

*   **Total Assets**: Considers the closing balance of assets for each month <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.
*   **Total Liabilities**: Considers the closing balance of liabilities for each month <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.
*   **Net Worth**: Calculated by deducting liabilities from assets for the month <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>.
*   **Change in Net Worth**: Calculated by deducting the closing net worth from the opening net worth of assets and liabilities <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.
*   All amounts are rolled over from the Assets and Liabilities database <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.

### 5. Net Worth Summary Database

This database summarizes the key figures of the tracker <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>.

*   It calculates five main figures: [[setting_financial_goals_and_net_worth_tracking | net worth goal]], [[overview_of_net_worth_goal_and_progress_tracking | total net worth]], amount required to reach the goal, total growth in net worth, and the percentage of [[overview_of_net_worth_goal_and_progress_tracking | net worth]] to the targeted net worth <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.
*   All values are pulled from the previously discussed databases <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>.

## Primary Dashboard

The primary dashboard serves as the main interface for the [[summarizing and visualizing net worth data in a dashboard | net worth tracker]] <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.

*   **Summary Section**: Displays the [[setting_financial_goals_and_net_worth_tracking | net worth goal]], [[overview_of_net_worth_goal_and_progress_tracking | total net worth]], amount to goal, total growth, and the percentage of the [[setting_financial_goals_and_net_worth_tracking | net worth goal]] <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>. This section is linked to the Net Worth Goal database and set in a gallery layout <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.
*   **Monthly Net Worth Overview**: Specifies total assets, total liabilities, net worth, and change in net worth <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>. It is linked to the Net Worth database and set in a gallery layout <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>.
*   **Assets and Liabilities Breakdown**: Linked to their respective breakdown databases and also displayed in a gallery layout <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.