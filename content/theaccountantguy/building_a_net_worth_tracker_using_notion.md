---
title: Building a Net Worth Tracker using Notion
videoId: G2UuEnUUCos
---

From: [[theaccountantguy]] <br/> 

A net worth tracker built using [[setting_up_a_personal_finance_tracker_in_notion | Notion]] helps monitor financial progress towards specific goals <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>. This tracker provides a comprehensive overview of financial health by summarizing net worth, breaking down assets and liabilities, and tracking monthly changes <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.

## Tracker Overview

The net worth tracker in [[setting_up_a_personal_finance_tracker_using_notion | Notion]] consists of several key sections:

*   **Summary Section** This section displays the net worth goal amount, the current total net worth, the amount required to reach the net worth goal, the total growth achieved in net worth since January, and the percentage of net worth achieved relative to the targeted amount <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.
*   **Monthly Net Worth Overview** This section provides a monthly summary of total assets, total liabilities, the net worth for each month, and the change in net worth for that month <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.
*   **Breakdown of Assets** This part details individual assets, categorized into five types, showing the amount of each asset and its proportion to the total assets <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.
*   **Breakdown of Liabilities** Similar to the asset breakdown, this section specifies four types of liabilities, along with their corresponding amounts and proportions relative to the total liabilities <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.

## Databases Required

To construct this net worth tracker, five distinct databases are utilized, each serving a specific purpose <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>.

### Assets and Liabilities Database

This database is where all assets and liabilities are recorded for each specific month <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. It includes:
*   **Asset/Liability Description** Five types of assets are specified <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.
*   **Opening Balance** A number property representing the balance at the start of the month <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.
*   **Amount** Shows additions or deletions for the period <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.
*   **Closing Balance** Calculated as opening balance plus/minus the amount <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.

The closing balance for each month must be copied to the opening balance of the subsequent month for all assets and liabilities <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>. This ensures continuity in tracking <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.

### Assets Breakdown Database

This database provides a breakup of all assets and their individual proportions to the total <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>.
*   It lists the five asset types created earlier <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.
*   The total amount for each asset type is rolled up from the Assets and Liabilities Database <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
*   The total assets value is calculated and rolled up from another database using a formula <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>.
*   The percentage of each asset relative to the total value of all assets combined is calculated and represented by a green bar <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.

### Liabilities Breakdown Database

This database is similar to the Assets Breakdown Database but comprises four types of liabilities, showing their total amounts and proportions <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.

### Net Worth Database

This database calculates key financial figures monthly <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>.
*   **Total Assets** Uses the closing balance of assets from the Assets and Liabilities Database <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.
*   **Total Liabilities** Uses the closing balance of liabilities from the Assets and Liabilities Database <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.
*   **Net Worth** Calculated by deducting total liabilities from total assets for the month <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>.
*   **Change in Net Worth** Calculated by deducting the closing net worth from the opening net worth <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.
All amounts in this database are rolled over from the Assets and Liabilities Database <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.

### Net Worth Summary Database

This is the final database, summarizing all previously discussed information <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>. It calculates and displays five key metrics <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>:
*   Net Worth Goal
*   Total Net Worth
*   Amount to Goal
*   Total Growth in Net Worth
*   Percentage of Net Worth to Targeted Net Worth

All values are pulled from the other databases to provide a desired total <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>.

## Primary Dashboard

The primary dashboard of the net worth tracker provides an integrated view of all the financial data <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.

*   **Summary Section** Displays the calculated net worth goal, total net worth, amount to goal, total growth, and the percentage of the net worth goal achieved <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>. This is linked to the Net Worth Goal Database and set in a gallery layout <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.
*   **Monthly Net Worth Overview** Specifies total assets, total liabilities, net worth, and change in net worth <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>. It is linked to the Net Worth Database and displayed in a gallery layout <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>.
*   **Assets Breakdown and Liabilities Breakdown** These sections are linked to their respective databases and are also set out in a gallery layout <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.

This comprehensive setup allows for effective [[net_worth_tracking_and_goals_in_notion | net worth tracking and goals in Notion]] <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.