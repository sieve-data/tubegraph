---
title: Building a net worth tracker using Notion
videoId: G2UuEnUUCos
---

From: [[theaccountantguy]] <br/> 

This article details how to [[using_notion_to_track_net_worth | build a net worth tracker]] within Notion, encompassing a summary, monthly overview, and breakdowns of assets and liabilities <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. This tracker allows for the tracking of financial growth and progress towards a net worth goal <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.

## Tracker Overview

The Notion net worth tracker features several key sections:
*   **Summary Section** This displays:
    *   The net worth goal amount <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.
    *   Current total net worth <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.
    *   The amount still required to reach the net worth goal <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.
    *   Total net worth growth achieved since January <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.
    *   The percentage of the targeted net worth achieved <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.
*   **Monthly Net Worth Overview** This section provides monthly data, including total assets, total liabilities, net worth for the month, and the change in net worth for that period <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.
*   **Assets Breakdown** This categorizes individual assets into five types, showing their amount and their proportion to total assets <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.
*   **Liabilities Breakdown** Similar to assets, this specifies four types of liabilities, along with their corresponding amounts and proportions to the total liabilities <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.

## [[databases_required_for_a_net_worth_tracker_in_notion | Databases Required]]

To [[tracking_personal_finances_using_notion | build this net worth tracker]], five types of databases are required <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>. Each database has distinct requirements <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.

### 1. Assets and Liabilities Database
This database is used to record all assets and liabilities for each specific month of the year <a class="yt-timestamp" data-t="01:40:53">[01:40:53]</a>.
*   **Asset Description:** Specifies up to five types of assets <a class="yt-timestamp" data-t="01:50:09">[01:50:09]</a>.
*   **Opening Balance:** A number property representing the asset's balance at the start of the month <a class="yt-timestamp" data-t="01:55:04">[01:55:04]</a>.
*   **Amount:** Shows additions or deletions of assets during the period <a class="yt-timestamp" data-t="02:00:27">[02:00:27]</a>.
*   **Closing Balance:** Calculated as the opening balance plus the amount during the month <a class="yt-timestamp" data-t="02:06:06">[02:06:06]</a>.
*   **Important Note:** The closing balance of each month must be copied and pasted as the opening balance for the subsequent month for all assets and liabilities <a class="yt-timestamp" data-t="02:16:03">[02:16:03]</a>.

### 2. Assets Breakdown Database
This database breaks down all assets, showing their individual proportions to the total amount <a class="yt-timestamp" data-t="02:42:07">[02:42:07]</a>.
*   It lists the same five assets created previously <a class="yt-timestamp" data-t="02:48:38">[02:48:38]</a>.
*   **Total Amount:** Represents the total amount of each asset from all months combined, rolled up from the Assets and Liabilities Database <a class="yt-timestamp" data-t="02:50:03">[02:50:03]</a>.
*   **Total Assets Value:** Calculated and rolled up from another database using a formula <a class="yt-timestamp" data-t="03:02:41">[03:02:41]</a>.
*   **Percentage:** Calculates the percentage of each asset relative to the total value of all combined assets, displayed as a green bar <a class="yt-timestamp" data-t="03:13:00">[03:13:00]</a>.

### 3. Liabilities Breakdown Database
This database is structured similarly to the Assets Breakdown, but for liabilities, comprising four types of liabilities <a class="yt-timestamp" data-t="03:20:47">[03:20:47]</a>.

### 4. Net Worth Database
This database calculates key financial figures for each subsequent month <a class="yt-timestamp" data-t="03:31:40">[03:31:40]</a>.
*   **Total Assets:** Considers the closing balance of assets for each month, rolled over from the Assets and Liabilities Database <a class="yt-timestamp" data-t="03:42:02">[03:42:02]</a>.
*   **Total Liabilities:** Considers the closing balance of liabilities for each month, rolled over from the Assets and Liabilities Database <a class="yt-timestamp" data-t="03:47:04">[03:47:04]</a>.
*   **Net Worth:** Calculated by deducting total liabilities from total assets for the month <a class="yt-timestamp" data-t="03:51:30">[03:51:30]</a>.
*   **Change in Net Worth:** Calculated by deducting the closing net worth from the opening net worth of assets and liabilities <a class="yt-timestamp" data-t="03:56:06">[03:56:06]</a>.

### 5. Net Worth Goal Database
This database appears to be a smaller, distinct database specifically for setting and referencing the net worth goal, which is then used in the summary section of the dashboard <a class="yt-timestamp" data-t="04:57:48">[04:57:48]</a>.

## Primary Dashboard

The primary dashboard of the Notion [[tracking_personal_finances_in_notion | net worth tracker]] integrates information from all the databases <a class="yt-timestamp" data-t="04:46:16">[04:46:16]</a>.

*   **Summary Section:** This section calculates and displays the net worth goal, total net worth, amount to goal, total growth, and the percentage of the net worth goal achieved <a class="yt-timestamp" data-t="04:48:07">[04:48:07]</a>. It links to the Net Worth Goal Database and is typically set in a gallery layout <a class="yt-timestamp" data-t="04:57:48">[04:57:48]</a>.
*   **Monthly Net Worth Overview:** Specifies total assets, total liabilities, net worth, and change in net worth <a class="yt-timestamp" data-t="05:03:00">[05:03:00]</a>. This section links to the Net Worth Database and is also set in a gallery layout <a class="yt-timestamp" data-t="05:09:41">[05:09:41]</a>.
*   **Assets Breakdown and Liabilities Breakdown:** These sections are linked to their respective databases and are displayed in a gallery layout <a class="yt-timestamp" data-t="05:15:02">[05:15:02]</a>.

This comprehensive setup allows for detailed [[tracking_personal_finances_in_notion | personal finance tracking]] and visualization within Notion.