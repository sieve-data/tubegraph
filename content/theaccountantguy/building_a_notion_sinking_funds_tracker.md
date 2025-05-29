---
title: Building a Notion sinking funds tracker
videoId: -V7ovjYG2vg
---

From: [[theaccountantguy]] <br/> 

A Notion sinking funds tracker helps monitor various aspects of your savings goals, including the overall savings needed, the amount saved over time, the remaining amount to save, and the percentage of contribution made <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. It also provides an overview of individual fund progress and monthly contributions <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.

## Types of Sinking Funds
Six common types of sinking funds include:
*   Education <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>
*   Events <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>
*   Family <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>
*   Healthcare <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>
*   Transportation <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>
*   Utilities <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>

For each sinking fund, the tracker monitors:
*   Goal amount <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>
*   Amount saved over time <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>
*   Amount left to save <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>
*   Contribution made over time (percentage) <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>
*   Targeted contribution date <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>
*   Required monthly contribution <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>

## Required Databases
To build a Notion sinking funds tracker, you will need five interconnected databases <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>:
1.  **Sinking Funds Database** <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>
2.  **Sinking Funds Details Database** <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>
3.  **Sinking Funds Overview Database** <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>
4.  **Sinking Fund Summary Database** <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>
5.  **Total Sinking Funds Database** <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>

### 1. Sinking Funds Database
This database holds the core information for each sinking fund <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>, <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.
It includes:
*   **Sinking Fund Details:** Categories such as Healthcare, Transportation, Utilities, Events, Family, and Education <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.
*   **Goal Amount:** The target savings amount <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.
*   **Starting Balance:** Initial savings at the beginning <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.
*   **Start Date:** When saving began <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.
*   **Goal Date:** The target end date for fund completion <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.
*   **Months:** Duration in months between the start and goal dates <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.
*   **Payment Breakdown:** Monthly payment required, calculated as `(Goal Amount - Starting Balance) / Months` <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.
*   **Account:** Where the fund is held <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.
*   **Amount Saved:** A rollup from another database, showing total savings to date <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.
*   **Amount Left:** The remaining balance needed, calculated as `Goal Amount - Amount Saved` <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.

### 2. Sinking Funds Details Database
This database stores information related to each sinking fund's contributions over time <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>, <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>.
It includes:
*   **Sinking Fund:** Links to the specific sinking fund to which a contribution is made <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.
*   **Category:** Links different databases together by mapping to the same sinking fund <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.
*   **Contribution Date:** The date of the contribution <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>.
*   **Starting Balance:** The balance at the beginning of the contribution period (closing balance of the previous month, or zero for the first month) <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.
*   **Contribution Amount:** The amount contributed on a specific date <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.
*   **Closing Balance:** `Opening Balance + Contribution Amount` <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>. (Note: The closing balance of one month must be manually copied as the opening balance for the next month <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>).
*   **Contribution Required Per Month:** Rolled up from the Sinking Funds Database <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.

### 3. Sinking Funds Overview Database
This database provides a complete overview of all created sinking funds <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.
It includes:
*   **Goal Amount:** The targeted sinking fund amount <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.
*   **Amount Saved:** Total contributions made across all sinking funds <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.
*   **Amount Left:** Remaining contribution needed, calculated as `Goal Amount - Amount Saved` <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.
*   **Targeted Savings:** Minimum monthly contribution required (rolled up) <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.
*   **Contribution in Percentage:** `Total Amount Saved / Targeted Amount` <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>.
*   **Goal Date:** The target date for fund completion <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.

### 4. Sinking Fund Summary Database
This database summarizes key metrics for each individual sinking fund, with values rolled up from earlier databases <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>.
It shows:
*   Targeted goal amount <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>
*   Amount saved so far <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>
*   Amount left to contribute <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>
*   Contribution made in percentage <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>
*   Targeted goal date <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>
*   Contribution required for each month <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>

### 5. Total Sinking Funds Database
This database calculates the combined total values across all sinking funds <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>.
It includes:
*   Total targeted sinking funds contribution <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>
*   Total amount saved <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>
*   Total amount left <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>
*   Total contribution in percentage (total contribution / targeted amount) <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>, <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>
All these values are rolled up from the previous databases <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>.

## Primary Dashboard
The primary dashboard serves as the central hub for your sinking funds tracker <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>:

### Summary Section
Displays the sum total of all sinking funds, including the goal amount, amount saved, amount left, and contribution in percentage <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>. This section is linked to the [[using_databases_for_notion_sinking_funds | Total Sinking Funds Database]] in a gallery view <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>.

### Sinking Funds Overview
Provides an overview of all six types of sinking funds, showing their individual goal amount, amount saved, amount left to save, contribution percentage, end goal date, and required monthly contribution <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>. This is linked to the [[using_databases_for_notion_sinking_funds | Sinking Fund Summary Database]] in a gallery mode layout <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>.

### Sinking Funds Progress
Shows monthly payments made towards each sinking fund and whether contributions meet the minimum required criteria <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>. A green tick indicates the minimum contribution was met or exceeded, while a red cross indicates it was not <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>. These are linked to the [[using_databases_for_notion_sinking_funds | individual Sinking Funds Details Database]] in a list format <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>.

This comprehensive setup allows for effective tracking and management of your sinking funds within Notion <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a>.