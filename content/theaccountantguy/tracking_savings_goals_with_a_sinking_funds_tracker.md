---
title: Tracking savings goals with a Sinking Funds Tracker
videoId: -V7ovjYG2vg
---

From: [[theaccountantguy]] <br/> 

This article details how to build a [[sinking_funds_tracker | sinking funds tracker]] using Notion to help with [[tracking_savings_and_net_worth | tracking savings]] goals <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>. The tracker allows users to monitor the overall amount of savings needed, the amount saved over time, the remaining amount to save, and the percentage of contribution made during a period <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.

Each individual sinking fund within the tracker can monitor its goal amount, the amount saved, the amount left to save, the contribution in percentage, the targeted contribution date, and the required monthly contribution <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. The tracker also shows the overall progress of each fund, indicating if monthly contributions meet the minimum criteria <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.

## Types of Sinking Funds Tracked

Six types of sinking funds are supported within this tracker <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>:
*   Education <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>
*   Events <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>
*   Family <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>
*   Healthcare <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>
*   Transportation <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>
*   Utilities <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>

## Building the Sinking Funds Tracker in Notion

The [[how_to_build_a_sinking_funds_tracker_in_notion | sinking funds tracker]] relies on five interconnected databases in Notion <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>.

### 1. Sinking Funds Database

This database holds all the details for each [[types_of_sinking_funds_for_personal_finance | sinking fund]] being created <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>. Its key fields include:
*   **Sinking Funds Details** (categorized as Healthcare, Transportation, Utilities, Events, Family, and Education) <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>
*   **Goal Amount**: The targeted savings amount <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.
*   **Starting Balance**: The initial savings at the start of the journey <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.
*   **Start Date**: The date when saving for the fund began <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.
*   **Goal Date**: The targeted end date for building the fund <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.
*   **Months**: The duration in months between the start and goal dates <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.
*   **Payment Breakdown**: The required monthly payment towards the fund, calculated as `(Goal Amount - Starting Balance) / Months` <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.
*   **Account**: The account where the sinking fund is created <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.
*   **Amount Saved**: A rolled-up value from another database, indicating current savings <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.
*   **Amount Left**: The remaining balance needed, calculated as `Goal Amount - Amount Saved` <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.

### 2. Sinking Funds Details Database

This database stores information related to each sinking fund and its contributions <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>. Key fields include:
*   **Sinking Fund**: The specific sinking fund receiving contributions (e.g., Education, Events, Family, Healthcare, Transportation, Utilities) <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.
*   **Category**: Used for linking different databases together, mirroring the sinking fund name <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.
*   **Contribution Date**: The date of the contribution <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>.
*   **Starting Balance**: The balance when beginning contributions on a specific date; this is the previous month's closing balance (or zero for the first month) <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.
*   **Contribution Amount**: The amount contributed on the specific date <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.
*   **Closing Balance**: Calculated as `Opening Balance + Contribution Amount` <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>. This balance is copied to the next month's opening balance <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>.
*   **Contribution Required Per Month**: Rolled over from the Sinking Funds Database <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.

### 3. Sinking Funds Overview Database

This database provides a complete overview of all created sinking funds <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>. It includes:
*   **Goal Amount**: The total targeted sinking fund amount <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.
*   **Amount Saved**: The total contributions made across all funds <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.
*   **Amount Left**: Indicates the further contribution needed, calculated as `Goal Amount - Amount Saved` <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.
*   **Targeted Savings**: The minimum required monthly contribution, rolled up from other databases <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.
*   **Contribution in Percentage**: Total amount saved divided by the targeted amount <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>.
*   **Goal Date**: The date by which the sinking funds should be established <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.

### 4. Sinking Fund Summary Database

This database provides a summarized view for each individual sinking fund <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>. It reflects:
*   Targeted goal amount <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>
*   Amount saved <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>
*   Amount left to contribute <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>
*   Contribution made in percentage <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>
*   Targeted goal date <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>
*   Contribution required for each month <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>

All these values are rolled up from earlier databases <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.

### 5. Total Sinking Funds Database

This database calculates the combined total values for all sinking funds <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>. It sums up:
*   Targeted sinking funds contribution <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>
*   Amount saved <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>
*   Amount left <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>
*   Contribution in percentage (total contribution divided by targeted amount) <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>

All values in this database are rolled up from previous databases <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>.

## Primary Dashboard Layout

The [[creating_a_savings_funds_tracker_in_notion | Notion sinking funds tracker]] dashboard features several key sections <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>:

### Summary Section
This section displays the total goal amount, amount saved, amount left, and contribution in percentage across all sinking funds combined <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>. It is linked to the Total Sinking Funds database in a gallery view <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>.

### Sinking Funds Overview
Providing an overview of all six types of sinking funds, this section shows the goal amount, amount saved, amount left to save, contribution percentage, end goal date, and required monthly contribution for each <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>. This is linked to the Sinking Fund Summary database, also in a gallery mode layout <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>.

### Sinking Funds Progress
This section tracks monthly payments made towards each sinking fund and the number of contributions <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>. It visually indicates progress: a green tick appears if a monthly contribution exceeds the minimum required, while a red cross signifies it does not <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>. This section is linked to the individual Sinking Funds Details database, displayed in a list format <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>.

Templates for this [[sinking_funds_tracker | sinking funds tracker]] are available for download <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>.