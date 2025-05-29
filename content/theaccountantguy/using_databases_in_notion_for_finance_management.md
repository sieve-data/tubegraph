---
title: Using databases in Notion for finance management
videoId: -V7ovjYG2vg
---

From: [[theaccountantguy]] <br/> 
A sinking funds tracker in Notion can be an effective tool for [[finance_management_using_notion | finance management]] and tracking specific savings goals over time <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>. This system allows users to monitor the total savings needed, the amount saved, the remaining balance, and the percentage of contribution made <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.

### Sinking Funds Categories
The tracker can be categorized into various types of sinking funds, such as:
*   Education <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>
*   Events <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>
*   Family <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>
*   Healthcare <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>
*   Transportation <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>
*   Utilities <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>

For each sinking fund, the system tracks:
*   The goal amount <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>
*   The amount saved over time <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>
*   The amount left to save <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>
*   The contribution made in percentage <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>
*   The targeted contribution date <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>
*   The required monthly contribution <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>

The tracker also visualizes the overall progress of each sinking fund, showing monthly contributions and indicating whether they meet the minimum criteria <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.

### [[setting_up_and_using_databases_in_notion | Databases]] Required for a Sinking Funds Tracker
To build a comprehensive sinking funds tracker in Notion, five distinct [[creating_a_database_in_notion | databases]] are utilized <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>:
1.  **Sinking Funds database:** Stores details of each sinking fund <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.
2.  **Sinking Funds Details database:** Holds information about contributions related to each sinking fund <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>.
3.  **Sinking Funds Overview database:** Provides a comprehensive overview of all created sinking funds <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.
4.  **Sinking Fund Summary database:** Offers a summarized view of key metrics for individual sinking funds <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.
5.  **Total Sinking Funds database:** Calculates combined totals for all sinking funds <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>.

#### Sinking Funds Database
This database contains all the foundational information for each sinking fund <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>. Key properties include:
*   **Sinking Fund Details:** Categories like Healthcare, Transportation, Utilities, Events, Family, and Education <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.
*   **Goal Amount:** The targeted savings amount <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.
*   **Starting Balance:** Initial savings at the journey's start <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.
*   **Start Date:** When saving began for the fund <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.
*   **Goal Date:** The target end date for building the fund <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.
*   **Months:** Duration between the start and goal dates, calculated in months <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.
*   **Payment Breakdown:** The required monthly contribution, calculated as (Goal Amount - Starting Balance) / Months <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.
*   **Account:** Specifies the financial account where the fund is held <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.
*   **Amount Saved:** The total amount saved to date, rolled up from another database <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.
*   **Amount Left:** The balance needed, calculated as Goal Amount - Amount Saved <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.

#### Sinking Funds Details Database
This database records specific contributions made to each sinking fund <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>. Its properties include:
*   **Sinking Fund:** Identifies the fund receiving the contribution (e.g., Education, Events, Family) <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.
*   **Category:** Helps in [[establishing_relationships_between_notion_databases | linking different databases together]] by holding the same sinking fund name <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.
*   **Contribution Date:** The date a contribution is made <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>.
*   **Starting Balance:** The opening balance when contributing on a specific date, often the closing balance of the previous month (zero for the first month) <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.
*   **Contribution Amount:** The amount added to the sinking fund on that date <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.
*   **Closing Balance:** Calculated as Starting Balance + Contribution Amount <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.
*   **Contribution Required per Month:** Rolled up from the Sinking Funds database <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.
    *   *Note: Closing balances from one month need to be manually copied to the next month's opening balance <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>.*

#### Sinking Funds Overview Database
This database provides a comprehensive overview of all sinking funds <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>. Key metrics include:
*   **Goal Amount:** The total targeted amount for all sinking funds <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.
*   **Amount Saved:** The cumulative contributions across all funds <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.
*   **Amount Left:** The remaining amount needed, calculated as Goal Amount - Amount Saved <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.
*   **Targeted Savings:** The minimum monthly contribution required, rolled up from other databases <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.
*   **Contribution in Percentage:** Total Amount Saved divided by the Targeted Amount <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>.
*   **Goal Date:** The combined target end date for all funds <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.

#### Sinking Fund Summary Database
This database summarizes key figures for *each individual sinking fund* <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>. Properties include:
*   Targeted Goal Amount <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>
*   Amount Saved So Far <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>
*   Amount Left to Contribute <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>
*   Contribution Made in Percentage <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>
*   Targeted Goal Date <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>
*   Contribution Required for Each Month <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>
All these values are rolled up from the previously discussed databases <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>.

#### Total Sinking Funds Database
This database calculates the combined total values across all sinking funds <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>. It tracks:
*   Targeted Sinking Funds Contribution <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>
*   Amount Saved <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>
*   Amount Left <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>
*   Contribution in Percentage (Total Contribution / Targeted Amount) <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>
These values are sum totals rolled up from the previous databases <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>.

### Primary Dashboard
The primary dashboard integrates these databases to provide a comprehensive view of the sinking funds <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>:

#### Summary Section
*   Displays the overall Goal Amount, Amount Saved, Amount Left, and Contribution in Percentage <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>.
*   This section is linked to the "Total Sinking Funds" database, typically displayed in a gallery view <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>.

#### Sinking Funds Overview
*   Shows an overview of all six types of sinking funds <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>.
*   Includes the Goal Amount, Amount Saved, Amount Left to Save, Contribution in Percentage, End Goal Date, and required monthly contribution for each <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>.
*   Linked to the "Sinking Fund Summary" database in a gallery layout <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>.

#### Sinking Funds Progress
*   Displays monthly payments made towards each sinking fund and the number of contributions <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.
*   Indicates progress with a green tick if contributions exceed the minimum required, or a red cross if they don't <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>.
*   Linked to the "Individual Sinking Funds Details" database in a list format <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>.