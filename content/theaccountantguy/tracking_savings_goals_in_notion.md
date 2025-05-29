---
title: Tracking savings goals in Notion
videoId: -V7ovjYG2vg
---

From: [[theaccountantguy]] <br/> 

A [[setting_up_a_savings_funds_tracker_in_notion | sinking funds tracker using Notion]] helps users monitor their progress toward specific savings goals over a period of time <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>. This tracker allows for monitoring the overall savings needed, the amount saved to date, the remaining amount to save, and the percentage of contribution made over time <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.

Common categories for sinking funds include:
*   Education <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>
*   Events <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>
*   Family <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>
*   Healthcare <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>
*   Transportation <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>
*   Utilities <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>

For each sinking fund, the system tracks:
*   Goal amount <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>
*   Amount saved over time <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>
*   Amount left to save <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>
*   Contribution made over time (as a percentage) <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>
*   Targeted date for contribution <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>
*   Required monthly contribution <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>

The tracker also visualizes the overall progress of each sinking fund, showing month-wise contributions and indicating whether they meet the minimum contribution criteria <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.

## Database Structure

Building this [[setting_up_a_savings_funds_tracker_in_notion | Notion sinking funds tracker]] requires the use of five interlinked databases <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>.

### 1. Sinking Funds Database

This database holds the core details for each sinking fund being tracked <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>.
It includes:
*   **Sinking Fund Name**: Categorized as Healthcare, Transportation, Utilities, Events, Family, and Education <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.
*   **Goal Amount**: The target savings amount <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.
*   **Starting Balance**: The initial savings at the beginning of the tracking journey <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.
*   **Start Date**: The date when saving for the fund began <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.
*   **Goal Date**: The target end date by which the fund should be built <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.
*   **Months**: The duration in months between the start and goal dates <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.
*   **Payment Breakdown**: The required monthly payment, calculated as `(Goal Amount - Starting Balance) / Months` <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.
*   **Account**: The account where the sinking fund is created <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.
*   **Amount Saved**: A rollup from another database, showing total savings to date <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.
*   **Amount Left**: Calculated as `Goal Amount - Amount Saved`, indicating the remaining balance to contribute <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.

### 2. Sinking Funds Details Database

This database stores information about each sinking fund's contributions over time <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>.
Key properties include:
*   **Sinking Fund**: Links to the specific sinking fund to which a contribution is made <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.
*   **Category**: Helps link different databases together, mirroring the sinking fund name <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.
*   **Contribution Date**: The date of the specific contribution <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>.
*   **Starting Balance**: The opening balance for the contribution period, typically the closing balance of the previous month (zero for the first month) <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.
*   **Contribution Amount**: The amount contributed on a specific date <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.
*   **Closing Balance**: Calculated as `Opening Balance + Contribution Amount` <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>. This balance is manually copied to the next month's opening balance <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>.
*   **Contribution Required Per Month**: Rolled up from the Sinking Funds database <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.

### 3. Sinking Funds Overview Database

This database provides a summary of all sinking funds created <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.
It displays:
*   **Goal Amount**: The overall targeted savings <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.
*   **Amount Saved**: Total contributions made across all sinking funds <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.
*   **Amount Left**: Remaining contributions needed (`Goal Amount - Amount Saved`) <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.
*   **Targeted Savings**: The minimum required monthly contribution rolled up from other databases <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.
*   **Contribution in Percentage**: Total amount saved divided by the targeted amount <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>.
*   **Goal Date**: The target completion date for the sinking funds <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.

### 4. Sinking Fund Summary Database

This database summarizes the individual details for each sinking fund, similar to the overview but on a per-fund basis <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>. All values in this database are rolled up from the earlier databases <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>.
It includes:
*   Targeted goal amount <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>
*   Amount saved so far <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>
*   Amount left to contribute <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>
*   Contribution made in percentage <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>
*   Targeted goal date <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>
*   Contribution required for each month <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>

### 5. Total Sinking Funds Database

This database calculates the combined total values across all sinking funds <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>.
It aggregates:
*   Targeted sinking funds contribution (total goal amount) <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>
*   Total amount saved <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>
*   Total amount left <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>
*   Overall contribution percentage (`Total Contribution / Targeted Amount`) <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>

All values in this database are rolled up from the previously discussed databases <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>.

## Primary Dashboard

The primary dashboard provides a comprehensive view of the sinking funds tracker <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.

### Summary Section
This section displays the aggregated goal amount, amount saved, amount left, and contribution percentage for all sinking funds combined <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>. It is linked to the Total Sinking Funds database and displayed in a gallery view <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>.

### Sinking Funds Overview
Provides a detailed overview of the six types of sinking funds, showing the goal amount, amount saved, amount left to save, contribution percentage, end goal date, and required monthly contribution for each <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>. This section is linked to the Sinking Fund Summary database and uses a gallery layout <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>.

### Sinking Funds Progress
This section tracks monthly payments made towards each sinking fund and indicates whether contributions meet the minimum required amount <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>. A green tick signifies meeting or exceeding the minimum contribution, while a red cross indicates it was not met <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>. This is linked to the individual Sinking Funds Details database and displayed in a list format <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>.