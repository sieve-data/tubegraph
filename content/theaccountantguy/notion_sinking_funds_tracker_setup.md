---
title: Notion sinking funds tracker setup
videoId: -V7ovjYG2vg
---

From: [[theaccountantguy]] <br/> 

This article details how to build a [[sinking_funds_tracker | sinking funds tracker]] using Notion to manage savings effectively <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>. The tracker helps monitor the overall savings needed, the amount saved over time, the remaining amount to save, and the percentage of contribution made during a period <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.

## Key Tracking Metrics

For each individual sinking fund, the system tracks:
*   The goal amount <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.
*   The amount saved over time <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.
*   The amount left to save <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.
*   The contribution made over time, reflected as a percentage <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.
*   The targeted date for making contributions <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.
*   The required monthly contribution <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.

The tracker also shows the overall progress of each sinking fund, including month-wise contributions and whether they meet the minimum contribution criteria <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.

## Sinking Fund Categories
Six types of sinking funds are typically created within this tracker:
*   Education <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>
*   Events <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>
*   Family <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>
*   Healthcare <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>
*   Transportation <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>
*   Utilities <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>

## Database Structure
To build the [[sinking_funds_tracker | sinking funds tracker]], five databases are utilized <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>. This [[database_structure_for_managing_sinking_funds_in_notion | database structure]] is central to the [[using_notion_for_financial_tracking | financial tracking]].

### 1. Sinking Funds Database
This database holds all the details for each sinking fund being created <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>:
*   **Sinking Fund Details**: Categorized as Healthcare, Transportation, Utilities, Events, Family, and Education <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.
*   **Goal Amount**: The targeted savings amount <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.
*   **Starting Balance**: The initial savings at the beginning of the journey <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.
*   **Start Date**: The date when saving for the sinking fund began <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.
*   **Goal Date**: The targeted end date by which the sinking fund should be built <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.
*   **Months**: The duration in months between the start and goal dates <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.
*   **Payment Breakdown**: The required monthly payment towards the sinking fund, calculated as `(Goal Amount - Starting Balance) / Months` <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.
*   **Account**: The account under which the sinking fund is created <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.
*   **Amount Saved**: Rolled up from another database, showing the total savings to date <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.
*   **Amount Left**: The remaining balance needed, calculated as `Goal Amount - Amount Saved` <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.

### 2. Sinking Funds Details Database
This database stores information related to each sinking fund and its contributions <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>:
*   **Sinking Fund**: The specific sinking fund to which a contribution is being made <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.
*   **Category**: Helps link different databases together, mirroring the sinking fund name <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.
*   **Contribution Date**: The date when a contribution is made <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>.
*   **Starting Balance**: The balance at the beginning of the contribution period, which is the closing balance of the previous month (zero for the first month) <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.
*   **Contribution Amount**: The amount contributed on a specific date <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.
*   **Closing Balance**: Calculated as `Opening Balance + Contribution Amount` <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>. The closing balance of one month needs to be copied to the next month's opening balance <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>.
*   **Contribution Required Per Month**: Rolled over from the Sinking Funds Database <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.

### 3. Sinking Funds Overview Database
This database provides a complete overview of all created sinking funds <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>:
*   **Goal Amount**: The targeted total for all sinking funds <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.
*   **Amount Saved**: Total contributions made across all sinking funds so far <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.
*   **Amount Left**: Remaining contributions needed, calculated as `Goal Amount - Amount Saved` <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.
*   **Targeted Savings**: The minimum required monthly contribution, rolled up from other databases <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.
*   **Contribution in Percentage**: Total amount saved divided by the targeted amount <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>.
*   **Goal Date**: The target date for the sinking funds to be fully saved <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.

### 4. Sinking Fund Summary Database
This database offers a summarized view of each individual sinking fund, with values rolled up from earlier databases <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>:
*   Targeted goal amount <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>.
*   Amount saved <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>.
*   Amount left to contribute <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>.
*   Contribution made in percentage <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>.
*   Targeted goal date <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>.
*   Contribution required for each month <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>.

### 5. Total Sinking Funds Database
This database calculates the combined total values across all sinking funds <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>:
*   Total targeted sinking funds contribution <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>.
*   Total amount saved <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.
*   Total amount left <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>.
*   Overall contribution in percentage (total contribution / targeted amount) <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>.
All values are rolled up from previous databases <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>.

## Primary Dashboard
The [[dashboard_and_summary_views_for_sinking_funds_in_notion | dashboard and summary views for sinking funds in Notion]] integrates these databases for a comprehensive overview. This is similar to a [[notion_monthly_budget_planner_setup | Notion monthly budget planner setup]] or [[notion_income_tracker_setup | Notion income tracker setup]] dashboard.

### Summary Section
This section displays the aggregated totals from the Total Sinking Funds Database, presented in a gallery view <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>:
*   Goal amount <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>.
*   Amount saved <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>.
*   Amount left <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>.
*   Contribution in percentage <a class="yt-timestamp" data-t="00:06:59">[00:06:59]</a>.

### Sinking Funds Overview
This section provides an overview of all six types of sinking funds, linked to the Sinking Fund Summary Database and displayed in a gallery mode layout <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>:
*   Goal amount <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>.
*   Amount saved <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a>.
*   Amount left to save <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>.
*   Contribution and percentage <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>.
*   End goal date <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>.
*   Contribution required for each month <a class="yt-timestamp" data-t="00:07:19">[00:07:19]</a>.

### Sinking Funds Progress
This section shows monthly payments made towards each sinking fund, linked to the individual Sinking Funds Details Database in a listical format <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>:
*   Indicates the number of contributions made <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>.
*   A green tick appears if a contribution for any month exceeds the minimum required <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>.
*   A red cross appears if the contribution does not meet the minimum requirement <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>.

This complete setup constitutes the [[creating_a_savings_funds_tracker_in_notion | creating a savings funds tracker in Notion]] and helps with the [[notion_expense_tracker_overview | Notion expense tracker overview]] and [[creating_a_notion_debt_tracker | creating a Notion debt tracker]].