---
title: Sinking funds progress and contributions analysis
videoId: -V7ovjYG2vg
---

From: [[theaccountantguy]] <br/> 

The Notion-based [[notion_sinking_funds_tracker_setup | sinking funds tracker]] is designed to monitor and analyze the progress and contributions made towards various [[sinking_funds | sinking funds]] <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. This system allows users to track their savings goals, contributions, and overall financial performance across different categories <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.

## Key Metrics Tracked

The tracker provides a comprehensive view of savings progress by monitoring several key metrics <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>:
*   **Overall Amount of Savings Needed**: The total financial goal for a specific period <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.
*   **Amount Saved Over Time**: The cumulative amount saved to date <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.
*   **Amount Left to Save**: The remaining balance required to reach the goal <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.
*   **Contribution Made in Percentage**: The proportion of the total goal that has been saved <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.

## Sinking Fund Categories

The tracker supports six distinct categories of [[sinking_funds | sinking funds]] <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>:
*   Education <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>
*   Events <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>
*   Family <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>
*   Healthcare <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>
*   Transportation <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>
*   Utilities <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>

For each category, the tracker monitors specific details <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>:
*   **Goal Amount**: The targeted savings for that specific fund <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.
*   **Amount Saved Over Time**: Current savings for the individual fund <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.
*   **Amount Left to Save**: Remaining amount needed for the fund <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.
*   **Contribution Made in Percentage**: Progress towards the individual fund's goal <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.
*   **Targeted Date**: The planned completion date for the fund <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.
*   **Required Contribution Each Month**: The calculated monthly contribution needed to meet the goal by the targeted date <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.

## Database Structure for Tracking

The [[notion_sinking_funds_tracker_setup | Notion sinking funds tracker setup]] utilizes five interlinked databases to manage and track financial data <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>:

1.  **Sinking Funds Database**: Holds all primary details for each [[sinking_funds | sinking fund]] <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>.
    *   **Details**: Categorized as Healthcare, Transportation, Utilities, Events, Family, and Education <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.
    *   **Goal Amount**: The targeted savings <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.
    *   **Starting Balance**: Initial savings at the start of the journey <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.
    *   **Start Date**: When saving began <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.
    *   **Goal Date**: Targeted end date for building the fund <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.
    *   **Months**: Duration between start and end dates <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.
    *   **Payment Breakdown (Required Contribution)**: Monthly payment calculated as `(Goal Amount - Starting Balance) / Months` <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.
    *   **Account**: Where the fund is held <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.
    *   **Amount Saved**: Rolled up from other databases <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.
    *   **Amount Left**: Calculated as `Goal Amount - Amount Saved` <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.

2.  **Sinking Funds Details Database**: Stores information on individual contributions <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.
    *   **Sinking Fund**: The specific fund being contributed to <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.
    *   **Category**: Links to the Sinking Funds database <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.
    *   **Contribution Date**: Date of contribution <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>.
    *   **Starting Balance**: Opening balance for the contribution period (closing balance of previous month) <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.
    *   **Contribution Amount**: Amount contributed on the specific date <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.
    *   **Closing Balance**: `Opening Balance + Contribution Amount` <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.
    *   **Contribution Required Per Month**: Rolled over from the Sinking Funds database <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.

3.  **Sinking Funds Overview Database**: Provides a complete overview of all [[sinking_funds | sinking funds]] <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.
    *   **Goal Amount**: Total targeted savings for all funds <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.
    *   **Amount Saved**: Total contributions made across all funds <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.
    *   **Amount Left**: Total remaining contributions needed <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.
    *   **Targeted Savings**: Minimum total contribution required each month <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.
    *   **Contribution in Percentage**: Total amount saved divided by the total targeted amount <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>.
    *   **Goal Date**: The target completion date for all funds <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.

4.  **Sinking Fund Summary Database**: Summarizes individual [[sinking_funds | sinking fund]] performance <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>.
    *   Aggregates the goal amount, amount saved, amount left, contribution percentage, targeted goal date, and required monthly contribution for *each* individual fund <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>.
    *   All values are rolled up from earlier databases <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.

5.  **Total Sinking Funds Database**: Calculates the combined total values of all [[sinking_funds | sinking funds]] <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>.
    *   Calculates the sum total of targeted contributions, amount saved, amount left, and combined contribution percentage <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>.
    *   Contribution percentage is `Total Contribution / Targeted Amount` <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.
    *   All values are rolled up from previous databases <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>.

## Dashboard View and Analysis

The primary dashboard provides a dynamic overview of the [[sinking_funds | sinking funds]]' progress <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>:

### Summary Section
Displays the total goal amount, total amount saved, total amount left, and overall contribution percentage across all [[sinking_funds | sinking funds]] <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>. This section is linked to the Total Sinking Funds database in a gallery view <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>.

### Sinking Funds Overview
Provides a detailed overview of each of the six [[sinking_funds | sinking fund]] types <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>. It shows the individual goal amount, amount saved, amount left to save, contribution percentage, end goal date, and the required monthly contribution for each fund <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>. This is linked to the Sinking Fund Summary database with a gallery mode layout <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>.

### Sinking Funds Progress
This section tracks [[monthly_and_quarterly_contribution_breakdown | monthly contributions]] towards each [[sinking_funds | sinking fund]] <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>. It visually indicates whether contributions meet the minimum required criteria <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>:
*   A green tick signifies that the contribution for a given month exceeds the minimum requirement <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>.
*   A red cross indicates that the contribution did not meet the minimum required amount <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>.

This progress view is linked to the individual Sinking Funds Details database, displayed in a list format <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>. This allows for clear [[analyzing_fund_allocation_and_financial_performance | analysis of fund allocation and financial performance]] on a month-by-month basis.