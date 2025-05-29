---
title: How to build a Sinking Funds Tracker in Notion
videoId: -V7ovjYG2vg
---

From: [[theaccountantguy]] <br/> 

This article details how to build a [[Sinking Funds Tracker]] using Notion to monitor various savings goals <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. The tracker helps monitor the overall savings needed, the amount saved over time, the remaining amount to save, and the percentage contribution made <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.

The tracker is designed to manage six types of [[Sinking Funds Tracker|sinking funds]]: Education, Events, Family, Healthcare, Transportation, and Utilities <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.

For each individual [[Sinking Funds Tracker|sinking fund]], the system tracks:
*   The goal amount <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.
*   The amount saved over time <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.
*   The amount left to save <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.
*   The contribution made over time, reflected as a percentage <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.
*   The targeted date for making the contribution <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.
*   The required contribution to be made each month <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.

The tracker also shows the overall progress of each [[Sinking Funds Tracker|sinking fund]], detailing monthly contributions and indicating whether they meet the minimum contribution criteria <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.

## Database Structure

Building the [[Sinking Funds Tracker]] requires the use of five distinct Notion databases <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>:
1.  Sinking Funds
2.  Sinking Funds Details
3.  Sinking Funds Overview
4.  Sinking Fund Summary
5.  Total Sinking Funds <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>

### 1. Sinking Funds Database

This database holds all specific information for each [[Sinking Funds Tracker|sinking fund]] being created <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>.

Key fields include:
*   **Sinking Funds Details**: Categorized as Healthcare, Transportation, Utilities, Events, Family, and Education <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.
*   **Goal Amount**: The targeted savings amount <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.
*   **Starting Balance**: The initial savings at the start of the journey <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.
*   **Start Date**: The date when saving began for the [[Sinking Funds Tracker|sinking fund]] <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.
*   **Goal Date**: The targeted end date for building the [[Sinking Funds Tracker|sinking fund]] <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.
*   **Months**: The duration in months between the Start Date and the Goal Date <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.
*   **Payment Breakdown**: The required monthly payment towards the [[Sinking Funds Tracker|sinking fund]], calculated as `(Goal Amount - Starting Balance) / Months` <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.
*   **Account**: The account under which the [[Sinking Funds Tracker|sinking fund]] is created <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.
*   **Amount Saved**: This value is rolled up from another database and indicates the total savings to date <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.
*   **Amount Left**: Calculated as `Goal Amount - Amount Saved`, showing the remaining balance to contribute <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.

### 2. Sinking Funds Details Database

This database stores information related to each [[Sinking Funds Tracker|sinking fund]] and its contributions <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>.

Key fields include:
*   **Sinking Fund**: The specific [[Sinking Funds Tracker|sinking fund]] receiving the contribution (e.g., Education, Events, Family, Healthcare, Transportation, Utilities) <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.
*   **Category**: A linking field for connecting different databases <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.
*   **Contribution Date**: The date when a contribution is made to the [[Sinking Funds Tracker|sinking fund]] <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>.
*   **Starting Balance**: The opening balance when a contribution is made on a specific date, which is the closing balance of the previous month (zero for the first month) <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.
*   **Contribution Amount**: The amount contributed on a specific date <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.
*   **Closing Balance**: Calculated as `Opening Balance + Contribution Amount` <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>. This closing balance is then manually copied to the next month's opening balance <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>.
*   **Contribution Required Per Month**: Rolled over from the "Sinking Funds" database <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.

### 3. Sinking Funds Overview Database

This database provides a comprehensive overview of all [[Sinking Funds Tracker|sinking funds]] created <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.

Key fields include:
*   **Goal Amount**: The targeted [[Sinking Funds Tracker|sinking fund]] amount <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.
*   **Amount Saved**: Total contributions made across all [[Sinking Funds Tracker|sinking funds]] <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.
*   **Amount Left**: Indicates further contributions needed, calculated as `Goal Amount - Amount Saved` <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.
*   **Targeted Savings**: The minimum monthly contribution required, rolled up from other databases <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.
*   **Contribution Percentage**: `Total Amount Saved / Targeted Amount` <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>.
*   **Goal Date**: The target date by which the [[Sinking Funds Tracker|sinking funds]] should be complete <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.

### 4. Sinking Fund Summary Database

This database summarizes the targeted goal amount, amount saved, amount left, percentage contribution, targeted goal date, and required monthly contribution for each individual [[Sinking Funds Tracker|sinking fund]] <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>. All amounts are rolled up from earlier databases <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>. For example, it shows specific calculations for "Healthcare" <a class="yt-timestamp" data-t="00:05:59">[00:05:59]</a>.

### 5. Total Sinking Funds Database

This database calculates the combined total values for all [[Sinking Funds Tracker|sinking funds]] <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>. It sums up the targeted contributions, amount saved, amount left, and percentage contribution for all [[Sinking Funds Tracker|sinking funds]] combined <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>. The contribution percentage is calculated as `Total Contribution / Targeted Amount` <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>. All values are rolled up from previous databases <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>.

## Primary Dashboard Layout

The primary dashboard serves as the central hub for the [[Sinking Funds Tracker]] <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.

It includes:
*   **Summary Section**: Displays the combined goal amount, amount saved, amount left, and contribution percentage for all [[Sinking Funds Tracker|sinking funds]] <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>. This section is linked to the "Total Sinking Funds" database in a gallery view <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>.
*   **Sinking Funds Overview**: Provides a summary of all six types of [[Sinking Funds Tracker|sinking funds]], showing the goal amount, amount saved, amount left to save, contribution percentage, end goal date, and required monthly contribution for each <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>. This is linked to the "Sinking Fund Summary" database with a gallery layout <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>.
*   **Sinking Funds Progress**: Shows monthly payments made towards each [[Sinking Funds Tracker|sinking fund]] and indicates whether contributions meet the minimum required amount. A green tick signifies that the minimum contribution criterion is met, while a red cross indicates it is not <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>. These are linked to the individual "Sinking Funds Details" database in a list format <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>.

For those interested in building this tracker, a template can be downloaded <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>.