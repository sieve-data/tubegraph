---
title: Databases required for a net worth tracker in Notion
videoId: G2UuEnUUCos
---

From: [[theaccountantguy]] <br/> 

To effectively build a [[tracking_personal_finances_in_notion | net worth tracker]] using [[tracking_personal_finances_using_notion | Notion]], the creation and integration of five distinct types of [[setting_up_and_using_databases_in_notion | databases]] are required <a class="yt-timestamp" data-t="01:26">[01:26]</a>. Each [[setting_up_and_using_databases_in_notion | database]] serves a specific function in [[building_a_net_worth_tracker_using_notion | tracking personal finances]] <a class="yt-timestamp" data-t="01:31">[01:31]</a>.

## Overview of Database Requirements

A comprehensive [[using_notion_to_track_net_worth | Notion net worth tracker]] includes a summary section, a monthly overview, and breakdowns of assets and liabilities <a class="yt-timestamp" data-t="00:35">[00:35]</a>. This structure necessitates several interconnected [[using_databases_in_notion_for_finance_management | databases]] to compile and display the relevant financial data <a class="yt-timestamp" data-t="01:26">[01:26]</a>.

## Core Databases

### 1. Assets and Liabilities Database

This is the primary [[setting_up_and_using_databases_in_notion | database]] where all assets and liabilities are recorded for each specific month <a class="yt-timestamp" data-t="01:40">[01:40]</a>.

*   **Asset/Liability Description**: Assets are classified into five types <a class="yt-timestamp" data-t="01:51">[01:51]</a>.
*   **Opening Balance**: A number property representing the balance at the start of the month <a class="yt-timestamp" data-t="01:55">[01:55]</a>.
*   **Amount**: Shows additions or deletions of assets/liabilities for the period <a class="yt-timestamp" data-t="02:00">[02:00]</a>.
*   **Closing Balance**: Calculated as the opening balance plus the amount for the month <a class="yt-timestamp" data-t="02:06">[02:06]</a>.
*   **Process**: The closing balance of each month must be copied and pasted as the opening balance for the subsequent month for all assets and liabilities <a class="yt-timestamp" data-t="02:16">[02:16]</a>.

### 2. Assets Breakdown Database

This [[setting_up_and_using_databases_in_notion | database]] provides a detailed breakup of all assets and their individual proportions relative to the total <a class="yt-timestamp" data-t="02:42">[02:42]</a>.

*   **Assets Listed**: The same five asset types created in the Assets and Liabilities [[setting_up_and_using_databases_in_notion | database]] are listed here <a class="yt-timestamp" data-t="02:48">[02:48]</a>.
*   **Total Amount of Each Asset**: Represents the combined total for each asset type across all months, rolled up from the earlier [[setting_up_and_using_databases_in_notion | database]] <a class="yt-timestamp" data-t="02:50">[02:50]</a>.
*   **Total Assets Value**: Calculated and rolled up from another [[setting_up_and_using_databases_in_notion | database]] using a formula <a class="yt-timestamp" data-t="03:02">[03:02]</a>.
*   **Percentage of Each Asset**: Calculates the proportion of each asset to the total value of all assets combined <a class="yt-timestamp" data-t="03:13">[03:13]</a>.

### 3. Liabilities Breakdown Database

Similar to the Assets Breakdown, this [[setting_up_and_using_databases_in_notion | database]] provides a detailed breakup for liabilities <a class="yt-timestamp" data-t="03:20">[03:20]</a>.

*   **Liabilities Listed**: Comprises four types of liabilities <a class="yt-timestamp" data-t="03:21">[03:21]</a>.
*   **Corresponding Amount and Proportion**: Shows the amount and proportion of each liability to the total amount <a class="yt-timestamp" data-t="01:20">[01:20]</a>.

### 4. Net Worth Database

This [[setting_up_and_using_databases_in_notion | database]] calculates key financial metrics for each month <a class="yt-timestamp" data-t="03:32">[03:32]</a>.

*   **Total Assets**: Considers the closing balance of assets for each month <a class="yt-timestamp" data-t="03:42">[03:42]</a>. All amounts are rolled over from the Assets and Liabilities [[setting_up_and_using_databases_in_notion | database]] <a class="yt-timestamp" data-t="04:06">[04:06]</a>.
*   **Total Liabilities**: Reflects the closing balance of liabilities for each month <a class="yt-timestamp" data-t="03:47">[03:47]</a>.
*   **Net Worth**: Calculated by deducting total liabilities from total assets for the month <a class="yt-timestamp" data-t="03:50">[03:50]</a>.
*   **Change in Net Worth**: Determined by deducting the closing net worth from the opening net worth of assets and liabilities <a class="yt-timestamp" data-t="03:56">[03:56]</a>.

### 5. Net Worth Summary Database

This [[setting_up_and_using_databases_in_notion | database]] provides an aggregated summary of the overall financial standing <a class="yt-timestamp" data-t="04:14">[04:14]</a>.

*   **Net Worth Goal**: The targeted net worth amount <a class="yt-timestamp" data-t="00:37">[00:37]</a>.
*   **Total Net Worth**: The current net worth amount <a class="yt-timestamp" data-t="00:41">[00:41]</a>.
*   **Amount to Goal**: The remaining amount required to reach the net worth goal <a class="yt-timestamp" data-t="00:43">[00:43]</a>.
*   **Total Growth in Net Worth**: The total growth achieved since January <a class="yt-timestamp" data-t="00:47">[00:47]</a>.
*   **Percentage of Net Worth to Targeted Net Worth**: Specifies the net worth achieved in proportion to the targeted amount <a class="yt-timestamp" data-t="00:50">[00:50]</a>.
*   **Data Source**: All values are pulled and totaled from the other [[setting_up_and_using_databases_in_notion | databases]] discussed <a class="yt-timestamp" data-t="04:29">[04:29]</a>.

## Dashboard Integration

The primary dashboard of the [[using_notion_to_track_net_worth | net worth tracker]] visually presents the summarized data from these [[using_databases_in_notion_for_finance_management | databases]] <a class="yt-timestamp" data-t="04:46">[04:46]</a>.

*   The **Summary Section** links to the Net Worth Summary [[setting_up_and_using_databases_in_notion | database]] and is set in a gallery layout <a class="yt-timestamp" data-t="04:48">[04:48]</a>.
*   The **Monthly Net Worth Overview** displays total assets, liabilities, net worth, and change in net worth, linked to the Net Worth [[setting_up_and_using_databases_in_notion | database]] in a gallery layout <a class="yt-timestamp" data-t="05:03">[05:03]</a>.
*   The **Assets Breakdown** and **Liabilities Breakdown** sections are linked to their respective [[setting_up_and_using_databases_in_notion | databases]] and also presented in a gallery layout <a class="yt-timestamp" data-t="05:15">[05:15]</a>.

This comprehensive set of [[setting_up_and_using_databases_in_notion | databases]] enables robust [[using_notion_to_track_net_worth | net worth tracking]] within [[tracking_personal_finances_using_notion | Notion]].