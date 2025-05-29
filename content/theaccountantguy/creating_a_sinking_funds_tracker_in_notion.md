---
title: Creating a Sinking Funds Tracker in Notion
videoId: -V7ovjYG2vg
---

From: [[theaccountantguy]] <br/> 

This article details how to build a comprehensive sinking funds tracker using Notion, covering the setup of various databases and the dashboard layout. The tracker helps manage specific savings goals over time <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.

## What is a Sinking Funds Tracker?
A sinking fund tracker in Notion allows users to monitor various aspects of their savings goals <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>. It tracks:
*   The total amount of savings needed <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>
*   The amount saved over time <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>
*   The remaining amount to save <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>
*   The percentage of the total contribution made <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>

## Types of Sinking Funds
The tracker includes six predefined categories for sinking funds <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>:
*   Education <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>
*   Events <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>
*   Family <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>
*   Healthcare <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>
*   Transportation <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>
*   Utilities <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>

For each sinking fund, the tracker monitors the goal amount, amount saved, amount left, contribution percentage, targeted date, and required monthly contribution <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. It also provides an overview of the overall progress, including month-wise contributions and whether they meet the minimum criteria <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.

## Databases Required
Building this [[setting_up_a_savings_funds_dashboard_in_notion | Notion]] sinking funds tracker requires five distinct databases <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>:
1.  Sinking Funds Database <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>
2.  Sinking Funds Details Database <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>
3.  Sinking Funds Overview Database <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>
4.  Sinking Fund Summary Database <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>
5.  Total Sinking Funds Database <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>

### 1. Sinking Funds Database
This database holds all the primary details for each sinking fund <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>.
*   **Sinking Funds Details**: Categorized as Healthcare, Transportation, Utilities, Events, Family, and Education <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.
*   **Goal Amount**: The target savings amount <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.
*   **Starting Balance**: The initial savings at the start of the journey <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.
*   **Start Date**: When saving began for the fund <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.
*   **Goal Date**: The targeted end date for building the fund <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.
*   **Months**: The duration between the start and goal dates, calculated in months <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.
*   **Payment Breakdown**: The required monthly payment towards the fund, calculated as `(Goal Amount - Starting Balance) / Months` <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.
*   **Account**: The account where the fund is created <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.
*   **Amount Saved**: A rolled-up value from another database, showing total savings to date <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.
*   **Amount Left**: The remaining balance needed, calculated as `Goal Amount - Amount Saved` <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.

### 2. Sinking Funds Details Database
This database stores information about individual contributions to each sinking fund <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>.
*   **Sinking Fund**: The specific fund to which the contribution is made (e.g., Education, Events, Family, Healthcare, Transportation, Utilities) <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.
*   **Category**: Links different databases together; contains the same sinking fund name as the primary column <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.
*   **Contribution Date**: The date of the contribution <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>.
*   **Starting Balance**: The balance at the beginning of the contribution date, typically the closing balance of the previous month (zero for the first month) <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>.
*   **Contribution Amount**: The amount contributed on a specific date <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.
*   **Closing Balance**: Calculated as `Opening Balance + Contribution Amount` <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>. The closing balance of one month should be copied to the next month's opening balance <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>.
*   **Contribution Required Per Month**: Rolled over from the Sinking Funds Database <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.

### 3. Sinking Funds Overview Database
This database provides a comprehensive overview of all sinking funds <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.
*   **Goal Amount**: The targeted sinking fund amount <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.
*   **Amount Saved**: Total contributions made across all fund types <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.
*   **Amount Left**: Remaining contributions needed, calculated as `Goal Amount - Amount Saved` <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.
*   **Targeted Savings**: Minimum monthly contribution required, rolled up from another database <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.
*   **Contribution in Percentage**: Total amount saved divided by the targeted amount <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>.
*   **Goal Date**: The target date for having the funds <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.

### 4. Sinking Fund Summary Database
This database summarizes the details for each individual sinking fund <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>.
*   **Targeted Goal Amount** <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>
*   **Amount Saved So Far** <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>
*   **Amount Left to Contribute** <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>
*   **Contribution Made in Percentage** <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>
*   **Targeted Goal Date** <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>
*   **Contribution Required for Each Month** <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>

All these values are rolled up from earlier databases to create a summarized view <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>.

### 5. Total Sinking Funds Database
This database calculates the combined total values across all sinking funds <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>.
*   **Targeted Sinking Funds Contribution** <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>
*   **Amount Saved** <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>
*   **Amount Left** <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>
*   **Contribution in Percentage**: Total contribution divided by the targeted amount <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>.

These values are obtained by rolling up respective values from the preceding databases <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>.

## Primary Dashboard Layout
The primary dashboard integrates the information from all databases to provide a clear overview <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>:

### Summary Section
This section displays the total goal amount, amount saved, amount left, and contribution percentage for all sinking funds combined <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>. It is linked to the Total Sinking Funds database and displayed in a gallery view <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>.

### Sinking Funds Overview
This section provides an overview of all six sinking fund types <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>. It shows:
*   Goal amount <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>
*   Amount saved <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a>
*   Amount left to save <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>
*   Contribution in percentage <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>
*   End goal date <a class="yt-timestamp" data-t="00:07:19">[00:07:19]</a>
*   Contribution required per month <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>

This section is linked to the Sinking Fund Summary database with a gallery layout <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>.

### Sinking Funds Progress
This section shows monthly payments made towards each sinking fund and the number of contributions <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.
*   A green tick indicates if the contribution for any month exceeds the minimum required <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>.
*   A red cross indicates if it does not meet the minimum contribution <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>.

This section is linked to the individual Sinking Funds Details database and is set out in a list format <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>.

The template for this Notion sinking funds tracker is available for download via a link in the video description <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>.