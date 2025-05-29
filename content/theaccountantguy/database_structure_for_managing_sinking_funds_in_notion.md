---
title: Database structure for managing sinking funds in Notion
videoId: -V7ovjYG2vg
---

From: [[theaccountantguy]] <br/> 
This article details the database structure required to build a [[notion_sinking_funds_tracker_setup | Sinking Funds tracker]] using Notion. This tracker aims to monitor the overall savings needed, amount saved over time, remaining amount to save, and the percentage of contribution made over a period <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.

The tracker includes six types of [[Sinking Funds | sinking funds]]: Education, Events, Family, Healthcare, Transportation, and Utilities <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. For each fund, the tracker monitors the goal amount, amount saved, amount left to save, contribution percentage, targeted contribution date, and required monthly contribution <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. It also provides an overall progress view, reflecting if monthly contributions meet the minimum criteria <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.

## Core Databases

To build the [[Sinking Funds | sinking funds]] tracker, five databases are utilized <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>:
1.  Sinking Funds Database <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>
2.  Sinking Funds Details Database <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>
3.  Sinking Funds Overview Database <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>
4.  Sinking Fund Summary Database <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>
5.  Total Sinking Funds Database <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>

### Sinking Funds Database

This database stores all the detailed information for each [[Sinking Funds | sinking fund]] being tracked <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>.

Properties include:
*   **Sinking Funds Details**: Categories such as Healthcare, Transportation, Utilities, Events, Family, and Education <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.
*   **Goal Amount**: The targeted savings amount for each fund <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.
*   **Starting Balance**: The initial savings at the beginning of the journey <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.
*   **Start Date**: The date when saving money for the fund began <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.
*   **Goal Date**: The targeted end date by which the [[Sinking Funds | sinking fund]] should be built <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.
*   **Months**: The duration in months between the start and goal dates <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.
*   **Payment Breakdown**: The required monthly contribution towards the [[Sinking Funds | sinking fund]], calculated as (Goal Amount - Starting Balance) / Months <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.
*   **Account**: Specifies the account under which the [[Sinking Funds | sinking fund]] is created <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.
*   **Amount Saved**: A rolled-up property from another database, indicating the total savings accumulated so far <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.
*   **Amount Left**: Calculated as Goal Amount - Amount Saved, showing the remaining balance needed <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.

### Sinking Funds Details Database

This database stores information related to each [[Sinking Funds | sinking fund]] and its specific contributions <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>.

Properties include:
*   **Sinking Fund**: Specifies the [[Sinking Funds | sinking fund]] to which a contribution is made (e.g., Education, Events, Family, Healthcare, Transportation, Utilities) <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.
*   **Category**: A property used to link different databases together, typically matching the Sinking Fund name <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.
*   **Contribution Date**: The date when a contribution was made <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>.
*   **Starting Balance**: The balance at the beginning of contributing on a specific date, which is the closing balance of the previous month (zero for the first month) <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>.
*   **Contribution Amount**: The amount contributed towards the [[Sinking Funds | sinking fund]] on a specific date <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.
*   **Closing Balance**: Calculated as Starting Balance + Contribution Amount <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.
*   **Contribution Required Per Month**: Rolled over from the Sinking Funds Database <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.

### Sinking Funds Overview Database

This database provides a complete overview of all created [[Sinking Funds | sinking funds]] <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.

Properties include:
*   **Goal Amount**: The targeted [[Sinking Funds | sinking fund]] amount <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.
*   **Amount Saved**: Indicates the total contributions made across all [[Sinking Funds | sinking funds]] so far <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.
*   **Amount Left**: Indicates the further contribution needed, calculated as Goal Amount - Amount Saved <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.
*   **Targeted Savings**: The minimum monthly contribution required, rolled up from another database <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.
*   **Contribution Percentage**: The total amount saved divided by the targeted amount <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>.
*   **Goal Date**: The target date for having the [[Sinking Funds | sinking funds]] complete <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.

### Sinking Fund Summary Database

This database provides a summarized view for each individual [[Sinking Funds | sinking fund]] <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>. All amounts are rolled up from earlier databases <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.

Properties include:
*   **Targeted Goal Amount**: The specific goal amount for an individual fund <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>.
*   **Amount Saved So Far**: The amount contributed to that specific fund <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>.
*   **Amount Left to Contribute**: The remaining amount needed for that fund <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>.
*   **Contribution Made in Percentage**: The percentage of the goal achieved for that fund <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>.
*   **Targeted Goal Date**: The specific goal date for that fund <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>.
*   **Contribution Required for Each Month**: The calculated monthly contribution for that fund <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>.

### Total Sinking Funds Database

This database calculates the total values of all [[Sinking Funds | sinking funds]] combined <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>. All values are calculated by rolling up respective values from previous databases <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>.

Properties include:
*   **Targeted Sinking Funds Contribution**: The sum of all targeted goal amounts <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>.
*   **Amount Saved**: The total amount saved across all funds <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>.
*   **Amount Left**: The total remaining amount to save across all funds <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>.
*   **Contribution in Percentage**: Total contribution divided by the total targeted amount <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>.

## Dashboard Integration

The primary [[dashboard_and_summary_views_for_sinking_funds_in_notion | dashboard]] for the Notion [[Sinking Funds | sinking funds]] tracker displays these databases in organized sections <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.

### Summary Section

This section displays the aggregated goal amount, amount saved, amount left, and contribution in percentage, representing the sum total of all [[Sinking Funds | sinking funds]] <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>. It is linked to the Total Sinking Funds database in a gallery view <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>.

### Sinking Funds Overview

This section provides an overview of all six types of [[Sinking Funds | sinking funds]], showing their individual goal amounts, amounts saved, amounts left to save, contribution percentages, end goal dates, and required monthly contributions <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>. This view is linked to the Sinking Fund Summary database, also displayed in a gallery mode <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>.

### Sinking Funds Progress

This section tracks monthly payments made towards each [[Sinking Funds | sinking fund]] and indicates whether contributions meet the minimum required amount <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>. A green tick signifies that contributions exceed the minimum, while a red cross indicates they do not <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>. These are linked to the individual Sinking Funds Details database in a list format <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>.