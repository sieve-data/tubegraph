---
title: Tracking Savings and Contributions for Sinking Funds
videoId: -V7ovjYG2vg
---

From: [[theaccountantguy]] <br/> 

This guide outlines how to build a [[creating_a_sinking_funds_tracker_in_notion | sinking funds tracker]] using Notion to monitor various savings goals. The tracker helps visualize the overall amount of savings needed, the amount saved over time, the remaining amount to save, and the percentage contribution made over a specific period <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.

## Key Metrics Tracked
The tracker monitors specific metrics for each [[types_of_sinking_funds_education_events_family_healthcare_transportation_utilities | sinking fund]]:
*   **Goal amount:** The total desired savings for the fund <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.
*   **Amount saved over time:** The cumulative contributions made <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.
*   **Amount left to save:** The remaining balance needed to reach the goal <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.
*   **Contribution made (percentage):** The progress towards the goal, expressed as a percentage <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.
*   **Targeted date:** The desired completion date for the fund <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.
*   **Required contribution each month:** The amount to save monthly to meet the target date <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.

The tracker also provides an overall progress view of each [[types_of_sinking_funds_education_events_family_healthcare_transportation_utilities | sinking fund]], showing month-wise contributions and indicating if they meet the minimum contribution criteria <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.

## Databases Required
Building this tracker in Notion requires five interconnected databases <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>:
1.  **Sinking Funds Database** <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>
2.  **Sinking Funds Details Database** <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>
3.  **Sinking Funds Overview Database** <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>
4.  **Sinking Fund Summary Database** <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>
5.  **Total Sinking Funds Database** <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>

### 1. Sinking Funds Database
This database holds all the core information for each [[types_of_sinking_funds_education_events_family_healthcare_transportation_utilities | sinking fund]] <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>. It includes:
*   **Details:** Categorized as [[types_of_sinking_funds_education_events_family_healthcare_transportation_utilities | Healthcare]], [[types_of_sinking_funds_education_events_family_healthcare_transportation_utilities | Transportation]], [[types_of_sinking_funds_education_events_family_healthcare_transportation_utilities | Utilities]], [[types_of_sinking_funds_education_events_family_healthcare_transportation_utilities | Events]], [[types_of_sinking_funds_education_events_family_healthcare_transportation_utilities | Family]], and [[types_of_sinking_funds_education_events_family_healthcare_transportation_utilities | Education]] <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.
*   **Goal Amount:** The targeted savings amount <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.
*   **Starting Balance:** The initial savings at the beginning of the saving journey <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.
*   **Start Date:** The date when saving began for the fund <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.
*   **Goal Date:** The targeted end date to build the fund <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.
*   **Months:** The duration in months between the start and goal dates <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.
*   **Payment Breakdown:** The required monthly payment towards the fund, calculated as `(Goal Amount - Starting Balance) / Months` <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.
*   **Account:** The account where the [[types_of_sinking_funds_education_events_family_healthcare_transportation_utilities | sinking fund]] is created <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.
*   **Amount Saved:** A rolled-up value from another database, showing total savings to date <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.
*   **Amount Left:** The necessary balance still required to contribute (`Goal Amount - Amount Saved`) <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.

### 2. Sinking Funds Details Database
This database stores information related to each [[types_of_sinking_funds_education_events_family_healthcare_transportation_utilities | sinking fund]] and its contributions <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>.
*   **Sinking Fund:** The specific [[types_of_sinking_funds_education_events_family_healthcare_transportation_utilities | sinking fund]] receiving the contribution <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.
*   **Category:** Used for linking different databases together, mirroring the [[types_of_sinking_funds_education_events_family_healthcare_transportation_utilities | sinking fund]] name <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.
*   **Contribution Date:** The date a contribution is made <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>.
*   **Starting Balance:** The opening balance when a contribution is made; for subsequent months, it's the previous month's closing balance <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.
*   **Contribution Amount:** The amount contributed on a specific date <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.
*   **Closing Balance:** The `Starting Balance + Contribution Amount` <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.
*   **Contribution Required Per Month:** Rolled over from the Sinking Funds Database <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.

### 3. Sinking Funds Overview Database
This database provides a comprehensive overview of all created [[types_of_sinking_funds_education_events_family_healthcare_transportation_utilities | sinking funds]] <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.
*   **Goal Amount:** The targeted amount for all [[types_of_sinking_funds_education_events_family_healthcare_transportation_utilities | sinking funds]] <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.
*   **Amount Saved:** Total contributions made across all [[types_of_sinking_funds_education_events_family_healthcare_transportation_utilities | sinking funds]] <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.
*   **Amount Left:** The remaining contribution needed (`Goal Amount - Amount Saved`) <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.
*   **Targeted Savings:** The minimum monthly contribution required, rolled up from other databases <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.
*   **Contribution and Percentage:** The `Total Amount Saved / Targeted Amount` <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>.
*   **Goal Date:** The target completion date for the combined funds <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.

### 4. Sinking Fund Summary Database
This database summarizes the targeted goal, amount saved, amount left, percentage contribution, targeted goal date, and required monthly contribution for each individual [[types_of_sinking_funds_education_events_family_healthcare_transportation_utilities | sinking fund]] <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>. All values are rolled up from the earlier databases, creating a concise summary <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>.

### 5. Total Sinking Funds Database
This database calculates the combined total values across all [[types_of_sinking_funds_education_events_family_healthcare_transportation_utilities | sinking funds]] <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>.
*   **Targeted Sinking Funds Contribution:** The total targeted amount <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>.
*   **Amount Saved:** The total amount saved across all funds <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.
*   **Amount Left:** The total remaining balance <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>.
*   **Contribution and Percentage:** Total contribution divided by the total targeted amount <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>.

These values are all calculated by rolling up respective data from the previously discussed databases <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>.

## Primary Dashboard
The primary dashboard, often referred to as the [[setting_up_a_savings_funds_dashboard_in_notion | savings funds dashboard]], integrates these databases to provide a comprehensive overview <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.

### Summary Section
This section displays the total goal amount, amount saved, amount left, and contribution in percentage, representing the sum of all [[types_of_sinking_funds_education_events_family_healthcare_transportation_utilities | sinking funds]] <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>. It is linked to the Total Sinking Funds Database, displayed in a gallery view <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>.

### Sinking Funds Overview
This section provides an overview of all six [[types_of_sinking_funds_education_events_family_healthcare_transportation_utilities | sinking funds]]. It shows the goal amount, amount saved, amount left to save, contribution percentage, end goal date, and required monthly contribution for each <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>. This view is linked to the Sinking Fund Summary Database and presented in a gallery mode layout <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>.

### Sinking Funds Progress
This section tracks the monthly payments for each [[types_of_sinking_funds_education_events_family_healthcare_transportation_utilities | sinking fund]] and indicates if contributions meet the minimum required amount <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.
*   A **green tick** indicates that the contribution for any month exceeds the minimum required <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>.
*   A **red cross** signifies that the contribution does not meet the minimum requirement <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>.
This section is linked to the Sinking Funds Details Database and is displayed in a list format <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>.

This comprehensive Notion setup enables effective [[tracking_transactions_and_progress_towards_savings_goals | tracking transactions and progress towards savings goals]] for various [[types_of_sinking_funds_education_events_family_healthcare_transportation_utilities | sinking funds]], supporting a robust [[budgeting_and_savings_strategy | budgeting and savings strategy]] by providing clear insights into contributions and remaining balances.