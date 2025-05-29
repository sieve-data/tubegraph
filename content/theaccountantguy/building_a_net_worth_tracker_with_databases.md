---
title: Building a net worth tracker with databases
videoId: G2UuEnUUCos
---

From: [[theaccountantguy]] <br/> 

A [[how_to_track_net_worth_using_notion | net worth tracker]] can be built using [[using_databases_in_notion_for_financial_tracking | Notion]] to manage personal finances <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>. This tracker provides a comprehensive overview of financial standing, including assets, liabilities, and progress towards financial goals <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.

## Tracker Sections Overview

The [[how_to_track_net_worth_using_notion | net worth tracker]] is structured into several key sections:

### Summary Section
This section displays key financial metrics <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>:
*   The [[net_worth_goal_and_progress_tracking | net worth goal]] amount being targeted <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.
*   The current total [[how_to_track_net_worth_using_notion | net worth]] <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.
*   The remaining amount needed to achieve the [[net_worth_goal_and_progress_tracking | net worth goal]] <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.
*   The total growth in [[how_to_track_net_worth_using_notion | net worth]] since January <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.
*   A percentage indicating the [[how_to_track_net_worth_using_notion | net worth]] achieved in proportion to the targeted amount <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.

### Monthly Net Worth Overview
This section provides a month-by-month breakdown of financial status <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>:
*   Total assets for each month <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.
*   Total liabilities for each month <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.
*   [[how_to_track_net_worth_using_notion | Net worth]] for the month <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>.
*   Change in [[how_to_track_net_worth_using_notion | net worth]] for the month <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>.

### Assets Breakdown
This section details individual assets, categorized into five types <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>. It shows the amount of each asset and its proportion to the total assets <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

### Liabilities Breakdown
Similar to the assets breakdown, this section specifies four types of liabilities, along with their corresponding amounts and proportions to the total liabilities <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>.

## Databases Required for Building the Tracker
Building this [[how_to_track_net_worth_using_notion | net worth tracker]] necessitates the use of five types of [[utilizing_notion_databases_for_financial_tracking | databases]] <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>, each with its own specific requirements <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.

### Assets and Liabilities Database
This [[setting_up_databases_for_income_tracking | database]] is used to record all assets and liabilities for each specific month during the year <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.
*   **Asset Description**: Five types of assets are specified <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.
*   **Opening Balance**: A number property indicating the asset's value at the start of the month <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>.
*   **Amount**: Shows additions or deletions of assets for the specific period <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.
*   **Closing Balance**: Calculated by adding the opening balance to the amount during the month <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.
The closing balance of each month for all assets must be copied and pasted onto the opening balance of the subsequent month <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>. The same process applies to the liabilities within this [[setting_up_databases_for_income_tracking | database]] <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>.

### Assets Breakdown Database
This [[setting_up_databases_for_income_tracking | database]] provides a breakup of all assets and their individual proportions to the total amount <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.
*   It lists the same five assets created earlier <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
*   The total amount for each asset, combined from all months, is represented by a formula rolled up from the Assets and Liabilities [[setting_up_databases_for_income_tracking | database]] <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.
*   The total assets value is calculated and rolled up from another [[setting_up_databases_for_income_tracking | database]] using a formula <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.
*   The percentage of each asset relative to the total value of all combined assets is calculated and represented visually <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.

### Liabilities Breakdown Database
This [[setting_up_databases_for_income_tracking | database]] is similar to the Assets Breakdown Database, comprising four types of liabilities <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>.

### Net Worth Database
This [[setting_up_databases_for_income_tracking | database]] calculates key [[how_to_track_net_worth_using_notion | net worth]] figures for each subsequent month <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>. All amounts are rolled over from the Assets and Liabilities [[setting_up_databases_for_income_tracking | database]] <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>.
*   **Total Assets**: Considers the closing balance of assets for each month <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>.
*   **Total Liabilities**: Uses the closing balance of liabilities for each month <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>.
*   **Net Worth**: Calculated by deducting liabilities from assets for the month <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>.
*   **Change in Net Worth**: Determined by deducting the closing [[how_to_track_net_worth_using_notion | net worth]] from the opening [[how_to_track_net_worth_using_notion | net worth]] of the assets and liabilities <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.

### Net Worth Summary Database
This [[setting_up_databases_for_income_tracking | database]] summarizes the overall financial picture <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>. It calculates:
*   [[net_worth_goal_and_progress_tracking | Net worth goal]] <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.
*   Total [[how_to_track_net_worth_using_notion | net worth]] amount to goal <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>.
*   Total growth in [[how_to_track_net_worth_using_notion | net worth]] <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.
*   Percentage of [[how_to_track_net_worth_using_notion | net worth]] to the targeted [[how_to_track_net_worth_using_notion | net worth]] <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.
All values are pulled from the previously discussed [[utilizing_notion_databases_for_financial_tracking | databases]] <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.

## Primary Dashboard
The primary dashboard of the [[how_to_track_net_worth_using_notion | net worth tracker]] integrates views from the different [[utilizing_notion_databases_for_financial_tracking | databases]] into a cohesive display <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>.
*   **Summary Section**: Linked to the [[net_worth_goal_and_progress_tracking | net worth goal]] [[setting_up_databases_for_income_tracking | database]] and displayed in a gallery layout <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>.
*   **Monthly Net Worth Overview**: Linked to the [[how_to_track_net_worth_using_notion | net worth]] [[setting_up_databases_for_income_tracking | database]] and also set in a gallery layout, showing total assets, total liabilities, [[how_to_track_net_worth_using_notion | net worth]], and change in [[how_to_track_net_worth_using_notion | net worth]] <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>.
*   **Assets Breakdown and Liabilities Breakdown**: Linked to their respective [[setting_up_databases_for_income_tracking | databases]] and presented in a gallery layout <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.