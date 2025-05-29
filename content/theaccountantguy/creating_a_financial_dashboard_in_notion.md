---
title: Creating a financial dashboard in Notion
videoId: -V7ovjYG2vg
---

From: [[theaccountantguy]] <br/> 

A [[utilizing_notion_dashboards_for_financial_tracking | Sinking Funds Tracker]] can be built using [[using_notion_for_personal_finance_management | Notion]] to manage savings for specific goals <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>. This tracker helps monitor the overall savings needed, the amount saved over time, the remaining amount to save, and the percentage of contributions made <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.

## Sinking Fund Categories
Six types of sinking funds are typically created within this tracker:
*   Education <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>
*   Events <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>
*   Family <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>
*   Healthcare <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>
*   Transportation <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>
*   Utilities <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>

## Key Metrics Tracked
For each individual sinking fund, the tracker monitors:
*   Goal amount <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>
*   Amount saved over time <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>
*   Amount left to save <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>
*   Contribution made over time (reflected as a percentage) <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>
*   Targeted date for contribution <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>
*   Required monthly contribution <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>

## Overall Progress Monitoring
The dashboard also visualizes the overall progress of each sinking fund, showing month-wise contributions and indicating if they meet the minimum required contribution <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. A green tick signifies meeting the minimum contribution, while a red cross indicates it was not met <a class="yt-timestamp" data-t="00:07:38">[00:07:38]</a>.

## Database Structure
[[components_of_a_notion_financial_dashboard | Building this Notion financial dashboard]] requires five distinct databases <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>:

### 1. Sinking Funds Database
This database holds all the detailed information for each sinking fund being tracked <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>:
*   **Sinking Funds Details** (e.g., Healthcare, Transportation, Utilities, Events, Family, Education) <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>
*   **Goal Amount**: The targeted savings amount <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.
*   **Starting Balance**: Initial savings at the start of the journey <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.
*   **Start Date**: The date saving began for the fund <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.
*   **Goal Date**: The targeted end date for building the fund <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.
*   **Months**: Duration in months between the start and goal dates <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.
*   **Payment Breakdown**: The required monthly payment towards the fund, calculated as `(Goal Amount - Starting Balance) / Months` <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.
*   **Account**: The financial account where the sinking fund is held <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.
*   **Amount Saved**: Total savings accumulated to date, rolled up from another database <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.
*   **Amount Left**: The remaining balance needed (`Goal Amount - Amount Saved`) <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.

### 2. Sinking Funds Details Database
This database stores information about each sinking fund's contributions <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>:
*   **Sinking Fund**: The specific fund being contributed to (e.g., Education, Events, Family, Healthcare, Transportation, Utilities) <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.
*   **Category**: Links different databases together by matching the sinking fund name <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.
*   **Contribution Date**: Date of the contribution <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>.
*   **Starting Balance**: The opening balance on the specific contribution date, typically the previous month's closing balance (zero for the first month) <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.
*   **Contribution Amount**: The amount contributed on that date <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.
*   **Closing Balance**: Calculated as `Opening Balance + Contribution Amount` <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.
*   **Contribution Required Per Month**: Rolled over from the Sinking Funds Database <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.

### 3. Sinking Funds Overview Database
This database provides a complete overview of all created sinking funds <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>:
*   **Goal Amount**: The targeted total for all sinking funds <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.
*   **Amount Saved**: Total contributions made across all funds <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.
*   **Amount Left**: Further contributions required (`Goal Amount - Amount Saved`) <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.
*   **Targeted Savings**: Minimum monthly contribution required, rolled up from other databases <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.
*   **Contribution in Percentage**: Total amount saved divided by the targeted amount <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>.
*   **Goal Date**: The target date for completing all sinking funds <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.

### 4. Sinking Fund Summary Database
This database summarizes key metrics for *each individual* sinking fund <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>:
*   Targeted goal amount <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>
*   Amount saved <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>
*   Amount left to contribute <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>
*   Contribution made in percentage <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>
*   Targeted goal date <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>
*   Contribution required for each month <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>
All these values are rolled up from earlier databases <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.

### 5. Total Sinking Funds Database
This database calculates the combined total values across all sinking funds <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>:
*   Targeted sinking funds contribution (total) <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>
*   Total amount saved <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>
*   Total amount left <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>
*   Contribution in percentage for all funds combined <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>. This is calculated as `Total Contribution / Targeted Amount` <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.

## Primary Dashboard Components
The primary [[creating_dashboards_for_financial_overview_in_notion | Notion financial dashboard]] integrates these databases to provide a comprehensive overview:

### Summary Section
This section displays the overall financial progress <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>:
*   Goal amount <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>
*   Amount saved <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>
*   Amount left <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>
*   Contribution in percentage <a class="yt-timestamp" data-t="00:06:59">[00:06:59]</a>
This section is linked to the "Total Sinking Funds" database, displayed in a gallery view <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>.

### Sinking Funds Overview
This section provides an overview of all six types of sinking funds <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>:
*   Goal amount <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>
*   Amount saved <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a>
*   Amount left to save <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>
*   Contribution in percentage <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>
*   End goal date <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>
*   Contribution required for each month <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>
These details are linked to the "Sinking Fund Summary" database in a gallery view <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>.

### Sinking Funds Progress
This section tracks monthly payments for each sinking fund <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>:
*   Shows monthly payments and the number of contributions made <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>.
*   Visually indicates if monthly contributions exceed the minimum required amount with a green tick, or if they do not meet it with a red cross <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>.
This section is linked to the "Sinking Funds Details" database in a list format <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>.

This structured approach allows for detailed [[tracking_personal_finances_in_notion | tracking of personal finances]] and progress towards [[setting_financial_goals_in_notion | setting financial goals]] within [[Notion]] <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a>. [[Using Notion templates for financial management | Templates]] for this tracker may be available for download <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>.