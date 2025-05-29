---
title: Databases required for tracking net worth in Notion
videoId: G2UuEnUUCos
---

From: [[theaccountantguy]] <br/> 

To build a [[building_a_net_worth_tracker_using_notion | net worth tracker using Notion]], five types of databases are required to complete the system <a class="yt-timestamp" data-t="01:27:18">[01:27:18]</a>. Each database serves a distinct purpose <a class="yt-timestamp" data-t="01:31:37">[01:31:37]</a>.

## Assets and Liabilities Database

This database is used to record all assets and liabilities for each specific month during the year <a class="yt-timestamp" data-t="01:41:07">[01:41:07]</a>.

Key properties include:
*   **Asset Description**: Specifies up to five types of assets <a class="yt-timestamp" data-t="01:50:52">[01:50:52]</a>.
*   **Opening Balance**: A number property representing the balance at the start of the month <a class="yt-timestamp" data-t="01:55:04">[01:55:04]</a>.
*   **Amount**: Shows additions or deletions of assets/liabilities for the period <a class="yt-timestamp" data-t="02:00:27">[02:00:27]</a>.
*   **Closing Balance**: Calculated as the opening balance plus or minus the amount during the month <a class="yt-timestamp" data-t="02:06:21">[02:06:21]</a>.
    *   The closing balance of each month for all assets and liabilities must be copied and pasted as the opening balance for the subsequent month <a class="yt-timestamp" data-t="02:16:32">[02:16:32]</a>.

## Assets Breakdown Database

This database provides a breakup of all assets and their individual proportions relative to the total amount <a class="yt-timestamp" data-t="02:42:07">[02:42:07]</a>.

Key properties and calculations include:
*   **Assets Listed**: The same five asset types created previously are listed <a class="yt-timestamp" data-t="02:48:47">[02:48:47]</a>.
*   **Total Amount**: Represents the combined total of each asset from all months, rolled up from the Assets and Liabilities database <a class="yt-timestamp" data-t="02:50:09">[02:50:09]</a>.
*   **Total Assets Value**: Calculated and rolled up from another database using a formula <a class="yt-timestamp" data-t="03:02:41">[03:02:41]</a>.
*   **Percentage of Each Asset**: Calculates the proportion of each asset to the total value of all assets combined, often represented by a green bar <a class="yt-timestamp" data-t="03:13:00">[03:13:00]</a>.

## Liabilities Breakdown Database

Similar to the assets breakdown, this database comprises four types of liabilities, with similar calculations for amounts and proportions <a class="yt-timestamp" data-t="03:20:96">[03:20:96]</a>.

## Net Worth Database

This database is used for [[creating_a_database_in_notion_for_calculations | calculations]] related to net worth <a class="yt-timestamp" data-t="03:32:00">[03:32:00]</a>.

It calculates:
*   **Total Assets**: Considers the closing balance of assets for each month <a class="yt-timestamp" data-t="03:42:25">[03:42:25]</a>.
*   **Total Liabilities**: Considers the closing balance of liabilities for each month <a class="yt-timestamp" data-t="03:46:95">[03:46:95]</a>.
*   **Net Worth**: Assets minus liabilities for the month <a class="yt-timestamp" data-t="03:50:90">[03:50:90]</a>.
*   **Change in Net Worth**: The closing net worth minus the opening net worth of assets and liabilities <a class="yt-timestamp" data-t="03:56:49">[03:56:49]</a>.
All amounts in this database are rolled over from the Assets and Liabilities database <a class="yt-timestamp" data-t="04:06:14">[04:06:14]</a>.

## Net Worth Goal Database (linked from Summary)

While not explicitly detailed as a separate creation step, a "net worth goal database" is mentioned as being linked to the summary section of the primary dashboard <a class="yt-timestamp" data-t="04:57:42">[04:57:42]</a>. This database likely stores the target net worth amount.

### Net Worth Summary

The net worth summary section, which pulls values from the other databases, displays five key metrics:
*   Net worth goal <a class="yt-timestamp" data-t="04:20:00">[04:20:00]</a>
*   Total net worth amount <a class="yt-timestamp" data-t="04:21:40">[04:21:40]</a>
*   Amount required to reach the goal <a class="yt-timestamp" data-t="00:43:08">[00:43:08]</a>, <a class="yt-timestamp" data-t="04:22:15">[04:22:15]</a>
*   Total growth in net worth since January <a class="yt-timestamp" data-t="00:47:00">[00:47:00]</a>, <a class="yt-timestamp" data-t="04:24:00">[04:24:00]</a>
*   Percentage of net worth achieved relative to the targeted net worth <a class="yt-timestamp" data-t="00:49:00">[00:49:00]</a>, <a class="yt-timestamp" data-t="04:26:00">[04:26:00]</a>

This comprehensive setup allows users to [[using_notion_to_monitor_financial_summaries_and_net_worth | monitor financial summaries and net worth]] effectively within Notion <a class="yt-timestamp" data-t="00:55:00">[00:55:00]</a>.