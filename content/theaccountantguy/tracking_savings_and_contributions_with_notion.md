---
title: Tracking savings and contributions with Notion
videoId: -V7ovjYG2vg
---

From: [[theaccountantguy]] <br/> 

A Notion-based tracker can be built to manage sinking funds, allowing users to monitor their overall savings goals, track amounts saved and remaining, and view contribution percentages over time <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. This system also tracks the progress of individual sinking funds on a month-by-month basis, indicating whether contributions meet minimum criteria <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.

## Sinking Fund Categories
The tracker supports six distinct categories for sinking funds <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>:
*   Education <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>
*   Events <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>
*   Family <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>
*   Healthcare <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>
*   Transportation <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>
*   Utilities <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>

For each category, the tracker monitors the goal amount, the amount saved, the remaining amount, the contribution percentage, the targeted completion date, and the required monthly contribution <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.

## Database Structure for [[Using Notion for Financial Tracking | Financial Tracking]]

To build this sinking funds tracker, five interconnected databases are utilized <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>:
1.  Sinking Funds Database <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>
2.  Sinking Funds Details Database <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>
3.  Sinking Funds Overview Database <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>
4.  Sinking Fund Summary Database <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>
5.  Total Sinking Funds Database <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>

### 1. Sinking Funds Database
This database stores all the primary information for each sinking fund <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>.
*   **Sinking Funds Details**: Categories like Healthcare, Transportation, Utilities, Events, Family, and Education <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.
*   **Goal Amount**: The target amount of savings for the fund <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.
*   **Starting Balance**: The initial savings at the beginning of the saving period <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.
*   **Start Date**: The date when saving for the fund began <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.
*   **Goal Date**: The targeted end date for accumulating the fund <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.
*   **Months**: The duration in months between the Start Date and the Goal Date <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.
*   **Payment Breakdown**: The required monthly payment towards the fund, calculated as (Goal Amount - Starting Balance) / Months <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.
*   **Account**: The financial account where the sinking fund is held <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.
*   **Amount Saved**: A rolled-up value from another database, showing the total savings accumulated to date <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.
*   **Amount Left**: The remaining balance needed (Goal Amount - Amount Saved) <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.

### 2. Sinking Funds Details Database
This database records specific contributions made to each sinking fund <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>.
*   **Sinking Fund**: Links to the specific sinking fund being contributed to (e.g., Education, Events) <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.
*   **Category**: Helps link different databases together, typically duplicating the Sinking Fund name <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.
*   **Contribution Date**: The date when a contribution is made <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>.
*   **Starting Balance**: The opening balance for the specific contribution date; this is the previous month's closing balance (or zero for the first month) <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>.
*   **Contribution Amount**: The specific amount added to the fund on that date <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.
*   **Closing Balance**: Calculated as Starting Balance + Contribution Amount <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.
*   **Contribution Required per Month**: Rolled over from the Sinking Funds Database <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.

### 3. Sinking Funds Overview Database
Provides a comprehensive summary of all sinking funds created <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.
*   **Goal Amount**: The collective targeted amount across all funds <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.
*   **Amount Saved**: The total contributions made across all funds <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.
*   **Amount Left**: The remaining total contribution needed (Goal Amount - Amount Saved) <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.
*   **Targeted Savings**: The minimum collective monthly contribution required, rolled up from other databases <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.
*   **Contribution in Percentage**: Total Amount Saved / Targeted Amount <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>.
*   **Goal Date**: The collective goal date for all funds <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.

### 4. Sinking Fund Summary Database
This database offers a summarized view of each individual sinking fund, with values rolled up from earlier databases <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>.
*   Targeted goal amount <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>
*   Amount saved so far <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>
*   Amount left to contribute <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>
*   Contribution made in percentage <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>
*   Targeted goal date <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>
*   Contribution required for each month <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>

### 5. Total Sinking Funds Database
This database calculates the combined totals for all sinking funds <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>.
*   Total targeted sinking funds contribution <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>
*   Total amount saved <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>
*   Total amount left <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>
*   Total contribution in percentage (Total Contribution / Targeted Amount) <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>

All these values are calculated by rolling up relevant data from the previously discussed databases <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>.

## Dashboard Components
The primary dashboard integrates these databases to provide a comprehensive view:

### Summary Section
This section displays the overall financial progress across all sinking funds <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>.
*   Goal amount <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>
*   Amount saved <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>
*   Amount left <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>
*   Contribution in percentage <a class="yt-timestamp" data-t="00:06:59">[00:06:59]</a>

This section is linked to the Total Sinking Funds database and displayed in a gallery view <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>.

### Sinking Funds Overview
This section gives an overview of all six types of sinking funds <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>.
*   Goal amount <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>
*   Amount saved <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a>
*   Amount left to save <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>
*   Contribution in percentage <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>
*   End goal date <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>
*   Contribution required for each month <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>

This view is linked to the Sinking Fund Summary database and displayed in gallery mode <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>.

### Sinking Funds Progress
This section tracks monthly payments for each sinking fund and the number of contributions made <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.
*   If a monthly contribution exceeds the minimum requirement, a green tick is displayed <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>.
*   If it does not meet the minimum, a red cross is shown <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>.

These progress details are linked to the individual Sinking Funds Details database and presented in a list format <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>.