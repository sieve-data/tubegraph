---
title: Using databases in Notion for financial tracking
videoId: -V7ovjYG2vg
---

From: [[theaccountantguy]] <br/> 

[[using_notion_for_templates_and_databases | Notion]] can be utilized to build a "sinking funds tracker" for [[tracking_personal_finances_in_notion | tracking personal finances]] <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>. This tracker helps monitor the total savings required over a period, the amount saved to date, the remaining amount to save, and the percentage of contributions made over time <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.

The tracker includes six categories of sinking funds: Education, Events, Family, Healthcare, Transportation, and Utilities <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. For each sinking fund, the system tracks:
*   Goal amount <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>
*   Amount saved over time <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>
*   Amount left to save <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>
*   Contribution made over time (as a percentage) <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>
*   Targeted date for contribution <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>
*   Required monthly contribution <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>

The tracker also provides an overall progress view for each sinking fund, showing month-wise contributions and indicating if they meet the minimum criteria <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.

## Required Databases

To build this sinking funds tracker, five distinct databases are needed <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>:
1.  Sinking Funds database <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>
2.  Sinking Funds Details database <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>
3.  Sinking Funds Overview database <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>
4.  Sinking Fund Summary database <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>
5.  Total Sinking Funds database <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>

### Sinking Funds Database

This database holds the core information for each sinking fund being tracked <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>. Its properties include:
*   **Sinking Funds Details**: Categorized as Healthcare, Transportation, Utilities, Events, Family, and Education <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.
*   **Goal Amount**: The target savings amount <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.
*   **Starting Balance**: The initial savings at the start of the journey <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.
*   **Start Date**: When saving began for the fund <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.
*   **Goal Date**: The target end date for building the fund <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.
*   **Months**: The duration in months between the start and end dates <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.
*   **Payment Breakdown**: The required monthly payment towards the fund, calculated as `(Goal Amount - Starting Balance) / Months` <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.
*   **Account**: Specifies the account where the fund is created <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.
*   **Amount Saved**: A rollup from another database (Sinking Funds Details) showing the total savings to date <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.
*   **Amount Left**: The remaining balance needed, calculated as `Goal Amount - Amount Saved` <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.

### Sinking Funds Details Database

This database stores information about individual contributions to each sinking fund <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>. It includes:
*   **Sinking Fund**: The specific sinking fund to which a contribution is made <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.
*   **Category**: Helps in [[establishing_relationships_between_databases_in_notion | linking different databases]] <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.
*   **Contribution Date**: The date when the contribution is made <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>.
*   **Starting Balance**: The opening balance on the contribution date, which is the closing balance of the previous month (excluding the first month which is zero) <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.
*   **Contribution Amount**: The amount contributed on a specific date <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.
*   **Closing Balance**: Calculated as `Opening Balance + Contribution Amount` <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>. Closing balances are copied to become the next month's opening balance <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>.
*   **Contribution Required Per Month**: A rollup from the Sinking Funds database <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.

### Sinking Funds Overview Database

This database provides an aggregated overview of all sinking funds <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>. It displays:
*   **Goal Amount**: The total targeted sinking fund amount <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.
*   **Amount Saved**: The total contributions made across all fund types <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.
*   **Amount Left**: The remaining contribution needed for all funds <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>, calculated as `Goal Amount - Amount Saved` <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>.
*   **Targeted Savings**: The minimum total monthly contribution required <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.
*   **Contribution in Percentage**: The total amount saved divided by the targeted amount <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>.
*   **Goal Date**: The target completion date for the funds <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.

### Sinking Fund Summary Database

This database provides a summarized view for each individual sinking fund, pulling relevant data from earlier databases <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>. It shows for each fund:
*   Targeted goal amount <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>
*   Amount saved so far <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>
*   Amount left to contribute <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>
*   Contribution made in percentage <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>
*   Targeted goal date <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>
*   Contribution required for each month <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>

### Total Sinking Funds Database

This database calculates the combined total values for all sinking funds <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>. It sums up:
*   Targeted sinking funds contribution <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>
*   Amount saved <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>
*   Amount left <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>
*   Contribution in percentage (total contribution divided by the targeted amount) <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>

All values in this database are rolled up from the previously discussed databases <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>.

## Primary Dashboard

The primary dashboard provides a comprehensive view of the sinking funds tracker, integrating the various databases <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>. It includes:
*   **Summary Section**: Displays the total goal amount, amount saved, amount left, and contribution in percentage, linked to the Total Sinking Funds database in a gallery view <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>.
*   **Sinking Funds Overview**: Shows an overview of all six fund types, indicating goal amount, amount saved, amount left to save, contribution percentage, end goal date, and monthly required contribution <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>. This is linked to the Sinking Fund Summary database in a gallery layout <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>.
*   **Sinking Funds Progress**: Details monthly payments for each fund, along with the number of contributions made <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>. It uses a visual indicator: a green tick if contributions exceed the minimum required, and a red cross if they do not <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>. This section is linked to the individual Sinking Funds Details database in a list format <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>.

This [[setting_up_databases_and_dashboards_in_notion | dashboard structure]] enables effective [[using_notion_for_personal_finance_management | personal finance management]] within Notion.