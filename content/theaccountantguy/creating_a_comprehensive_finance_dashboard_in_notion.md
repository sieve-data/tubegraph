---
title: Creating a comprehensive finance dashboard in Notion
videoId: -V7ovjYG2vg
---

From: [[theaccountantguy]] <br/> 

A "sinking funds tracker" can be built using [[tracking_personal_finances_using_notion | Notion]] to manage specific savings goals <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>. This tracker helps monitor the overall savings needed, the amount already saved, the remaining balance, and the percentage of contribution made over time <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. The system also tracks the overall progress of each sinking fund, showing monthly contributions and indicating whether they meet minimum requirements <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.

## Sinking Fund Categories

Six types of sinking funds are typically created within this tracker <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>, <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>, <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>:
*   Education <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>
*   Events <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>
*   Family <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>
*   Healthcare <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>
*   Transportation <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>
*   Utilities <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>

For each sinking fund, the system tracks <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>:
*   Goal amount <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>
*   Amount saved over time <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>
*   Amount left to save <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>
*   Contribution made over time (as a percentage) <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>
*   Targeted date for contribution <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>
*   Required monthly contribution <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>

## Databases for the Sinking Funds Tracker

To build this [[finance_management_using_notion | finance management]] tracker, five distinct databases are required <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>:
1.  **Sinking Funds Database** <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>
2.  **Sinking Funds Details Database** <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>
3.  **Sinking Funds Overview Database** <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>
4.  **Sinking Fund Summary Database** <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>
5.  **Total Sinking Funds Database** <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>

### 1. Sinking Funds Database

This database stores all information related to the sinking funds being created <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>. It includes:
*   **Sinking Funds Details:** Categorized by type (e.g., Healthcare, Transportation, Utilities, Events, Family, Education) <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.
*   **Goal Amount:** The targeted savings amount <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.
*   **Starting Balance:** The initial savings at the start of the journey <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.
*   **Start Date:** The date when saving began for the fund <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.
*   **Goal Date:** The targeted end date to build the fund <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.
*   **Months:** The duration in months between the start and goal dates <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.
*   **Payment Breakdown:** The required monthly payment, calculated as the difference between the goal amount and starting balance, divided by the number of months <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.
*   **Account:** The account where the sinking fund is held <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.
*   **Amount Saved:** A rolled-up value from another database, showing total savings to date <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.
*   **Amount Left:** The goal amount minus the amount saved, indicating the remaining balance needed <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.

### 2. Sinking Funds Details Database

This database stores information about each sinking fund and its contributions <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>.
*   **Sinking Fund:** The specific sinking fund to which a contribution is made <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>, <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>.
*   **Category:** Used for linking different databases <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>. The sinking fund name is duplicated in this field <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
*   **Contribution Date:** The date a contribution is made <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>.
*   **Starting Balance:** The balance when contributing on a specific date, usually the closing balance of the previous month (zero for the first month) <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.
*   **Contribution Amount:** The amount added to the sinking fund on a specific date <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.
*   **Closing Balance:** The opening balance plus the contribution amount <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>. The closing balance of one month is manually copied to the next month's opening balance <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>.
*   **Contribution Required Per Month:** Rolled over from the Sinking Funds database <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.

### 3. Sinking Funds Overview Database

This database provides a complete overview of all sinking funds created <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.
*   **Goal Amount:** The targeted sinking fund amount <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.
*   **Amount Saved:** Total contributions made across all sinking funds <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.
*   **Amount Left:** The remaining contribution required (Goal Amount - Amount Saved) <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.
*   **Targeted Savings:** The minimum monthly contribution rolled up from other databases <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.
*   **Contribution Percentage:** Total amount saved divided by the targeted amount <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>.
*   **Goal Date:** The target date for having the sinking funds complete <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.

### 4. Sinking Fund Summary Database

This database summarizes key financial metrics for each individual sinking fund <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>. All amounts are rolled up from earlier databases <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.
*   Targeted goal amount <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>
*   Amount saved so far <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>
*   Amount left to contribute <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>
*   Contribution made in percentage <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>
*   Targeted goal date <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>
*   Contribution required for each month <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>

### 5. Total Sinking Funds Database

This database calculates the combined total values of all sinking funds <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>. All values are calculated by rolling up respective values from previous databases <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>.
*   Total targeted sinking funds contribution <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>
*   Total amount saved <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>
*   Total amount left <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>
*   Total contribution percentage (total contribution divided by the total targeted amount) <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>, <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>

## Primary Notion Dashboard Layout

The [[setting_up_a_primary_dashboard_in_Notion | primary dashboard in Notion]] integrates these databases to provide a comprehensive view <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.

### Summary Section
This section displays the aggregated financial goals, total saved amount, remaining amount, and overall contribution percentage <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>. It links to the "Total Sinking Funds" database and is presented in a gallery view <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>.

### Sinking Funds Overview Section
This section provides an overview of all six types of sinking funds, showing <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>:
*   Goal amount <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>
*   Amount saved <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a>
*   Amount left to save <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>
*   Contribution percentage <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>
*   End goal date <a class="yt-timestamp" data-t="00:07:19">[00:07:19]</a>
*   Required monthly contribution for each fund <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>

This section is linked to the "Sinking Fund Summary" database and displayed in a gallery layout <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>.

### Sinking Funds Progress Section
This section details monthly payments made towards each sinking fund, including the number of contributions <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.
*   A green tick appears if a monthly contribution exceeds the minimum required amount <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>.
*   A red cross appears if the contribution does not meet the minimum requirement <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>.

This section is linked to the "Sinking Funds Details" database and presented in a list format <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>.

This comprehensive setup allows for effective [[tracking_personal_finances_in_notion | tracking personal finances in Notion]] and [[analyzing_financial_data_using_notion | analyzing financial data using Notion]] related to specific savings goals, effectively [[how_to_set_financial_goals_in_notion | setting financial goals in Notion]], [[managing_asset_financials_in_notion | managing asset financials in Notion]], [[creating_a_budget_tracker_with_notion | creating a budget tracker with Notion]], and [[customizing_notion_dashboard_for_personal_finances | customizing a Notion dashboard for personal finances]].