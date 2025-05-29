---
title: Net worth goal and progress tracking
videoId: G2UuEnUUCos
---

From: [[theaccountantguy]] <br/> 
This article details [[how_to_track_net_worth_using_notion | how to build a net worth tracker using Notion]] <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>. The tracker includes a summary section, a monthly overview, and breakdowns of assets and liabilities <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.

### Tracker Overview

The net worth tracker built in Notion features several key sections:
*   **Summary Section**: Displays the net worth goal, current total net worth, amount needed to reach the goal, total growth achieved since January, and the percentage of the goal achieved <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. This section effectively supports [[setting_net_worth_goals_in_notion | setting net worth goals in Notion]] and [[monitoring_savings_progress_and_goals | monitoring savings progress and goals]] <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.
*   **Monthly Net Worth Overview**: Specifies total assets, total liabilities, net worth for each month, and the change in net worth for the month <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>. This helps in [[monthly_net_worth_and_financial_breakdown | tracking monthly net worth and financial breakdown]] <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.
*   **Breakdown of Assets**: Lists individual assets, classified into five categories, their respective amounts, and their proportion to total assets <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.
*   **Liabilities Breakdown**: Details four types of liabilities, their corresponding amounts, and their proportion to total liabilities <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.

### Building the Net Worth Tracker with Databases

[[Building a net worth tracker with databases | Building this net worth tracker]] requires the use of five distinct databases in Notion, each serving a specific purpose <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>:

#### 1. Assets and Liabilities Database
This database is used to record all assets and liabilities for each specific month during the year <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.
*   **Asset Description**: Specifies five types of assets <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.
*   **Opening Balance**: A number property indicating the balance at the start of the month <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.
*   **Amount**: Shows additions or deletions of assets/liabilities for the period <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.
*   **Closing Balance**: Calculated as the opening balance plus or minus the amount during the month <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.
*   The closing balance of each month for all assets must be copied to the opening balance of the subsequent month, and the same process applies to liabilities <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>. This method helps in [[tracking_assets_liabilities_and_net_worth_in_business | tracking assets, liabilities, and net worth]] over time <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.

#### 2. Assets Breakdown
This database provides a breakup of all assets and their individual proportions to the total amount <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.
*   It lists the same five assets defined earlier <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.
*   The total amount for each asset from all combined months is rolled up from the Assets and Liabilities database <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
*   The total assets value is calculated and rolled up from another database using a formula <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>.
*   The percentage of each asset to the total value of all combined assets is calculated and represented visually <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.

#### 3. Liabilities Breakdown
Similar to the assets breakdown, this database details four types of liabilities <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.

#### 4. Net Worth Database
This database calculates the total assets, total liabilities, net worth (assets minus liabilities), and the change in net worth for each subsequent month <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.
*   **Total Assets**: Considers the closing balance of assets for each month <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.
*   **Total Liabilities**: Uses the closing balance of liabilities for each month <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.
*   **Net Worth**: Calculated by deducting liabilities from assets for the month <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>.
*   **Change in Net Worth**: Determined by deducting the opening net worth from the closing net worth for the period <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.
All amounts in this database are rolled over from the Assets and Liabilities database <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.

#### 5. Net Worth Summary
This database summarizes all the information from the other databases <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>. It calculates:
*   Net worth goal <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>
*   Total net worth amount <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>
*   Amount required to reach the goal <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>
*   Total growth in net worth <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>
*   Percentage of net worth achieved against the targeted net worth <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>

### Primary Dashboard

The primary dashboard of the net worth tracker integrates information from the various databases to provide a comprehensive view, facilitating [[monitoring_investments_and_net_worth | monitoring investments and net worth]] <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>:

*   **Summary Section**: Displays the net worth goal, total net worth, amount remaining to goal, total growth, and the percentage of the net worth goal <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>. This section is linked to the Net Worth Goal database and set out in a gallery layout <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.
*   **Monthly Net Worth Overview**: Specifies total assets, total liabilities, net worth, and change in net worth <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>. This is linked to the Net Worth database and also set out in a gallery layout <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>.
*   **Assets Breakdown and Liabilities Breakdown**: These sections are linked to their respective databases (Assets Breakdown and Liabilities Breakdown) and displayed in a gallery layout <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.