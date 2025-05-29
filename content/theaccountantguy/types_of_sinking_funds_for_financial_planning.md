---
title: Types of sinking funds for financial planning
videoId: -V7ovjYG2vg
---

From: [[theaccountantguy]] <br/> 

## Introduction to [[notion_sinking_funds_tracker_setup | Sinking Funds Tracking]]

A [[sinking_funds_tracker | sinking funds tracker]] in Notion can be used to manage various financial goals over time <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>. This system allows users to track:
*   The total savings required over a period <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.
*   The amount saved to date <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.
*   The remaining amount to save <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.
*   The percentage of contribution made over time <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.
It also provides an overview of each fund's progress, including monthly contribution achievements <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.

## Common [[sinking_funds | Sinking Fund]] Categories

Six common types of [[sinking_funds | sinking funds]] that can be tracked include:
*   Education <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>
*   Events <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>
*   Family <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>
*   Healthcare <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>
*   Transportation <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>
*   Utilities <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>

## Key Metrics Tracked for Individual [[sinking_funds | Sinking Funds]]

For each specific [[sinking_funds | sinking fund]], the following details are tracked:
*   **Goal Amount**: The total target savings <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.
*   **Amount Saved**: The current accumulated savings <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.
*   **Amount Left**: The remaining balance to save <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.
*   **Contribution Percentage**: The proportion of the goal amount saved so far <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.
*   **Targeted Date**: The planned completion date for the fund <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.
*   **Required Monthly Contribution**: The amount needed to save each month to meet the goal by the targeted date <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.

## [[database_structure_for_managing_sinking_funds_in_notion | Database Structure for Managing Sinking Funds]] in Notion

Building a [[sinking_funds_tracker | sinking funds tracker]] in Notion typically involves five interconnected databases <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>:

### Sinking Funds Database
This primary database holds all details for each [[sinking_funds | sinking fund]] <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>. Key properties include:
*   **Category**: Such as Healthcare, Transportation, Utilities, Events, Family, and Education <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.
*   **Goal Amount**: The targeted savings <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.
*   **Starting Balance**: Initial savings at the start of the journey <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.
*   **Start Date**: When saving began <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.
*   **Goal Date**: The target end date for the fund <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.
*   **Months**: Duration between start and end dates in months <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.
*   **Payment Breakdown**: Required monthly payment, calculated as (Goal Amount - Starting Balance) / Months <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.
*   **Account**: The financial account where the fund is held <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.
*   **Amount Saved**: Rolled up from another database, showing current savings <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.
*   **Amount Left**: Goal Amount minus Amount Saved <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.

### Sinking Funds Details Database
This database stores information related to contributions for each [[sinking_funds | sinking fund]] <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>. It includes:
*   **Sinking Fund**: Links to the specific [[sinking_funds | sinking fund]] being contributed to <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.
*   **Category**: Helps link different databases <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.
*   **Contribution Date**: When a contribution is made <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>.
*   **Starting Balance**: Opening balance on the contribution date, typically the previous month's closing balance <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.
*   **Contribution Amount**: The amount contributed on a specific date <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.
*   **Closing Balance**: Starting Balance plus Contribution Amount <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.
*   **Contribution Required Per Month**: Rolled up from the "Sinking Funds" database <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.

### Sinking Funds Overview Database
This database provides a comprehensive overview of all [[sinking_funds | sinking funds]] <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>, showing:
*   Total Goal Amount <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.
*   Total Amount Saved <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.
*   Total Amount Left (Goal Amount minus Amount Saved) <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.
*   Total Targeted Savings (minimum monthly contribution) <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.
*   Overall Contribution Percentage (Total Amount Saved divided by Total Targeted Amount) <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>.
*   Overall Goal Date <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.

### Sinking Fund Summary Database
This database summarizes the targeted goal amount, amount saved, amount left, contribution percentage, targeted goal date, and required monthly contribution for *each individual* [[sinking_funds | sinking fund]] <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>. All values are rolled up from earlier databases to provide a summarized view of the entire tracker <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>.

### Total Sinking Funds Database
This database calculates the grand totals for all [[sinking_funds | sinking funds]] combined <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>. It sums up the targeted contributions, amount saved, amount left, and the overall contribution percentage for all funds <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>. These values are derived by rolling up respective data from previous databases <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>.

## [[dashboard_and_summary_views_for_sinking_funds_in_notion | Dashboard and Summary Views]]

A primary dashboard integrates these databases to provide a comprehensive view of the [[sinking_funds_tracker | sinking funds]] progress <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>:

*   **Summary Section**: Displays the overall goal amount, amount saved, amount left, and total contribution percentage across all [[sinking_funds | sinking funds]] <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>. This is linked to the "Total Sinking Funds" database in a gallery view <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>.
*   **Sinking Funds Overview**: Provides a detailed overview of all six types of [[sinking_funds | sinking funds]], showing their individual goal amounts, saved amounts, remaining amounts, contribution percentages, end goal dates, and required monthly contributions <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>. This is linked to the "Sinking Fund Summary" database in a gallery view <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>.
*   **Sinking Funds Progress**: Visualizes monthly payments for each fund <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>. It indicates with a green tick if a contribution exceeds the minimum required, or a red cross if it doesn't <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>. This section is linked to the "Individual Sinking Funds Details" database in a list format <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>.