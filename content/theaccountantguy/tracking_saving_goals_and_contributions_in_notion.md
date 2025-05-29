---
title: Tracking saving goals and contributions in Notion
videoId: -V7ovjYG2vg
---

From: [[theaccountantguy]] <br/> 

This article details how to build a [[creating_a_savings_funds_tracker_in_notion | sinking funds tracker using Notion]] to manage saving goals and contributions <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. The tracker allows users to monitor the overall savings needed, the amount saved, the remaining balance, and the percentage contribution made over time <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.

## Key Information Tracked

For each sinking fund, the tracker monitors:
*   The goal amount <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>
*   The amount saved over time <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>
*   The amount left to save <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>
*   The contribution made over time, reflected as a percentage <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>
*   The targeted date for making the contribution <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>
*   The required monthly contribution <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>

The tracker also provides an overall progress view, showing monthly contributions and indicating whether they meet the minimum criteria <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.

## Types of Sinking Funds

Six categories of sinking funds are demonstrated in this [[tracking_personal_finances_in_notion | Notion]] setup:
*   Education <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>
*   Events <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>
*   Family <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>
*   Healthcare <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>
*   Transportation <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>
*   Utilities <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>

## Databases Required

Building the [[creating_a_savings_funds_tracker_in_notion | sinking funds tracker]] in [[tracking_personal_finances_in_notion | Notion]] requires five databases <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>:
1.  Sinking Funds Database <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>
2.  Sinking Funds Details Database <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>
3.  Sinking Funds Overview Database <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>
4.  Sinking Fund Summary Database <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>
5.  Total Sinking Funds Database <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>

### 1. Sinking Funds Database

This database stores all the detailed information related to each sinking fund <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.
*   **Sinking Funds Details:** Categories such as Healthcare, Transportation, Utilities, Events, Family, and Education <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.
*   **Goal Amount:** The targeted savings amount <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.
*   **Starting Balance:** The initial savings at the beginning of the journey <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.
*   **Start Date:** The date saving began for the sinking fund <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.
*   **Goal Date:** The targeted end date by which the sinking fund should be built <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.
*   **Months:** The duration in months between the start and end dates <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.
*   **Payment Breakdown:** The required monthly payment towards the sinking fund, calculated as (Goal Amount - Starting Balance) / Months <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.
*   **Account:** The account under which the sinking fund is created <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.
*   **Amount Saved:** A rolled-up value from another database, indicating current total savings <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.
*   **Amount Left:** The goal amount minus the amount saved, representing the remaining balance needed <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.

### 2. Sinking Funds Details Database

This database stores information related to each sinking fund and its contributions <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>.
*   **Sinking Fund:** The specific sinking fund to which contributions are being made (e.g., Education, Events, Family, Healthcare, Transportation, Utilities) <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.
*   **Category:** Used for linking different databases together, mirroring the Sinking Fund name <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.
*   **Contribution Date:** The date a contribution is made <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>.
*   **Starting Balance:** The balance at the beginning of the contribution date, typically the closing balance of the previous month (zero for the first month) <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.
*   **Contribution Amount:** The amount contributed on a specific date <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.
*   **Closing Balance:** Calculated as the Opening Balance plus the Contribution Amount <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>. The closing balance of one month is copied to the next month's opening balance <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>.
*   **Contribution Required Per Month:** Rolled up from the Sinking Funds Database <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.

### 3. Sinking Funds Overview Database

This database provides a comprehensive overview of all created sinking funds <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.
*   **Goal Amount:** The total targeted amount for all sinking funds <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.
*   **Amount Saved:** The total contributions made across all sinking funds to date <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.
*   **Amount Left:** The remaining contribution needed for all sinking funds (Goal Amount - Amount Saved) <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.
*   **Targeted Savings:** The minimum total monthly contribution required, rolled up from other databases <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.
*   **Contribution and Percentage:** Total amount saved divided by the targeted amount <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>.
*   **Goal Date:** The target date by which all sinking funds should be established <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.

### 4. Sinking Fund Summary Database

This database summarizes the targeted goal amount, amount saved, amount left, percentage contributed, targeted goal date, and required monthly contribution for *each individual* sinking fund <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>. All respective amounts are rolled up from the earlier databases, creating a summarized view of the tracker <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>.

### 5. Total Sinking Funds Database

This database calculates the combined total values for all sinking funds <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>. It sums up the targeted contribution, amount saved, amount left, and percentage contribution for all sinking funds combined <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>. The contribution percentage is calculated as total contribution divided by the total targeted amount <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>. All these values are derived by rolling up data from the previous databases <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>.

## Primary Dashboard Layout

The primary dashboard for the [[creating_a_savings_funds_tracker_in_notion | Notion sinking funds tracker]] features several sections <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>:

*   **Summary Section:** Displays the overall goal amount, amount saved, amount left, and contribution in percentage, representing the sum total of all sinking funds <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>. This section is linked to the "Total Sinking Funds" database in a gallery view <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>.
*   **Sinking Funds Overview:** Provides an overview of all six types of sinking funds, showing their individual goal amount, amount saved, amount left, contribution percentage, end goal date, and required monthly contribution <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>. This section is linked to the "Sinking Fund Summary" database in a gallery mode layout <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>.
*   **Sinking Funds Progress:** Shows monthly payments made towards each sinking fund, along with the number of contributions <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>. A green tick indicates if a monthly contribution exceeds the minimum required amount, while a red cross signifies it does not meet the criteria <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>. These are linked to the "Individual Sinking Funds Details" database in a list format <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>.