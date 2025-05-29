---
title: Using databases for Notion sinking funds
videoId: -V7ovjYG2vg
---

From: [[theaccountantguy]] <br/> 

A sinking funds tracker in Notion can be built to monitor overall savings needed, the amount saved over time, the remaining amount to save, and the percentage of contribution made during a period <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. The tracker also shows the overall progress of each sinking fund's contributions month-wise, indicating if contributions meet the minimum required criteria <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.

## Types of Sinking Funds
Six types of sinking funds are typically created for this tracker:
*   Education <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>
*   Events <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>
*   Family <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>
*   Healthcare <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>
*   Transportation <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>
*   Utilities <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>

For each sinking fund, the tracker monitors:
*   Goal amount <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>
*   Amount saved over time <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>
*   Amount left to save <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>
*   Contribution made over time (as a percentage) <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>
*   Targeted date for contribution <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>
*   Required monthly contribution <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>

## Databases for the Tracker
To build this sinking funds tracker, five [[setting_up_databases_in_notion | databases]] are required <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>:
1.  Sinking Funds Database <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>
2.  Sinking Funds Details Database <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>
3.  Sinking Funds Overview Database <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>
4.  Sinking Fund Summary Database <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>
5.  Total Sinking Funds Database <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>

### 1. Sinking Funds Database
This database holds all the information related to the [[types_of_sinking_funds_in_notion | sinking funds]] being created <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>. Its key properties include:
*   **Sinking Funds Details**: Categorized as Healthcare, Transportation, Utilities, Events, Family, and Education <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.
*   **Goal Amount**: The targeted savings amount <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.
*   **Starting Balance**: The initial savings at the start of the journey <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.
*   **Start Date**: The date when saving began for the fund <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.
*   **Goal Date**: The targeted end date by which the sinking fund must be built <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.
*   **Months**: The duration in months between the Start Date and Goal Date <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.
*   **Payment Breakdown**: The required monthly payment towards the sinking fund, calculated as `(Goal Amount - Starting Balance) / Months` <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.
*   **Account**: The account under which the sinking fund is created <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.
*   **Amount Saved**: A rollup from another database, showing total savings to date <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.
*   **Amount Left**: Calculated as `Goal Amount - Amount Saved`, indicating the balance still required <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.

### 2. Sinking Funds Details Database
This database stores information related to each sinking fund and its contributions <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>. Its properties include:
*   **Sinking Fund**: The specific sinking fund to which an amount is being contributed <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>, including the six categories of [[types_of_sinking_funds_in_notion | sinking funds]] <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.
*   **Category**: Helps in [[linking_databases_in_notion | linking different databases together]] <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.
*   **Contribution Date**: The date on which a contribution is made <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>.
*   **Starting Balance**: The opening balance when contributing on a specific date; it's the closing balance of the previous month (zero for the first month) <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.
*   **Contribution Amount**: The amount contributed to the sinking fund on a specific date <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.
*   **Closing Balance**: Calculated as `Opening Balance + Contribution Amount` <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>. The closing balance of one month is copied to the next month's opening balance <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>.
*   **Contribution Required per Month**: Rolled up from the Sinking Funds database <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.

### 3. Sinking Funds Overview Database
This database provides a complete overview of all created sinking funds <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>. Its properties include:
*   **Goal Amount**: The targeted sinking fund amount <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.
*   **Amount Saved**: The total contribution made so far across all sinking funds <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.
*   **Amount Left**: Indicates the further contribution required, calculated as `Goal Amount - Amount Saved` <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.
*   **Targeted Savings**: The minimum monthly contribution required, rolled up from other databases <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.
*   **Contribution in Percentage**: The total amount saved divided by the targeted amount <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>.
*   **Goal Date**: The date by which the sinking funds should be established <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.

### 4. Sinking Fund Summary Database
This database summarizes the targeted goal amount, amount saved, amount left, contribution percentage, targeted goal date, and required monthly contribution for each individual sinking fund <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>. All amounts are rolled up from earlier databases <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>. This database helps to create a summarized view of the entire tracker <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>.

### 5. Total Sinking Funds Database
This database calculates the total values for all sinking funds combined <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>. It sums up the targeted contribution, amount saved, amount left, and total contribution percentage for all funds <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>. The contribution percentage is calculated by dividing the total contribution by the total targeted amount <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>. These values are rolled up from the previous databases <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>.

## Primary Dashboard
The main dashboard integrates these databases to provide a comprehensive overview:
*   **Summary Section**: Displays the combined goal amount, amount saved, amount left, and contribution percentage from all sinking funds <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>. This section is linked to the Total Sinking Funds database in a gallery view <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>.
*   **Sinking Funds Overview**: Provides an overview of the six types of sinking funds, showing their goal amount, amount saved, amount left, contribution percentage, end goal date, and required monthly contribution <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>. This is linked to the Sinking Fund Summary database with a gallery layout <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>.
*   **Sinking Funds Progress**: Shows monthly payments made towards each sinking fund and the number of contributions <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>. A green tick indicates that the contribution for a month exceeds the minimum required, while a red cross signifies it does not meet the minimum <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>. This section is linked to the individual Sinking Funds Details database in a list format <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>.