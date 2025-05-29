---
title: Notion net worth tracker tutorial
videoId: G2UuEnUUCos
---

From: [[theaccountantguy]] <br/> 

This article explains how to build a [[how_to_track_net_worth_using_notion | net worth tracker]] using [[utilizing_notion_databases_for_financial_tracking | Notion]] <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

## Tracker Overview

The [[how_to_track_net_worth_using_notion | Notion net worth tracker]] includes several key sections:

*   **Summary Section** <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>:
    *   Net worth goal amount <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>
    *   Total net worth at present <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>
    *   Amount required to reach the net worth goal <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>
    *   Total growth achieved in net worth since January <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>
    *   Percentage of net worth achieved proportional to the targeted amount <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>
*   **Monthly Net Worth Overview** <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>:
    *   Total assets for each month <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>
    *   Total liabilities <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>
    *   Net worth for the month <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>
    *   Change in net worth for the month <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>
*   **Assets Breakdown** <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>:
    *   Specifies individual assets classified into five categories <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>
    *   Amount of each asset <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>
    *   Proportion of each asset to the total assets <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>
*   **Liabilities Breakdown** <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>:
    *   Specifies four types of liabilities <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>
    *   Corresponding amount and proportion of each liability to the total amount <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>

## Building the Tracker: Required Databases

Building this [[how_to_track_net_worth_using_notion | net worth tracker]] requires the use of five types of [[utilizing_notion_databases_for_financial_tracking | Notion databases]] <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>.

### 1. Assets and Liabilities Database

This database is used to record all assets and liabilities for each specific month during the year <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.

*   **Asset Description**: Specifies five types of assets <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>.
*   **Opening Balance**: A number property indicating the asset's value at the start of the month <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.
*   **Amount**: Shows additions or deletions of assets for the specific period <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.
*   **Closing Balance**: Calculated as the opening balance added to the 'amount' during the month <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.

For each month, the closing balance of an asset must be copied and pasted to the opening balance of the subsequent month <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>. This process is repeated for the liabilities database as well <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.

### 2. Assets Breakdown Database

This database provides a breakup of all assets and their individual proportions to the total amount <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.

*   Lists the five asset types created earlier <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.
*   **Total Amount**: Shows the total amount of each asset rolled up from the 'Assets and Liabilities Database' <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
*   **Total Assets Value**: Calculated and rolled up from another database using a formula <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>.
*   **Percentage**: Calculates the percentage of each asset to the total value of all assets combined, represented in a green bar <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.

### 3. Liabilities Breakdown Database

Similar to the Assets Breakdown, this database repeats the same process for liabilities, comprising four types <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.

### 4. Net Worth Database

This database calculates the total assets, total liabilities, net worth, and the change in net worth for each subsequent month <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.

*   **Total Assets**: Considers the closing balance of assets of each month from the 'Assets and Liabilities Database' <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.
*   **Total Liabilities**: Considers the closing balance of liabilities of each month from the 'Assets and Liabilities Database' <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.
*   **Net Worth**: Calculated by deducting liabilities from the assets for the month <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
*   **Change in Net Worth**: Calculated by deducting the closing net worth from the opening net worth of the assets and liabilities <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.
*   All amounts are rolled over from the 'Assets and Liabilities Database' <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.

### 5. Net Worth Summary Database

This database summarizes all the calculated figures <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>.

*   Calculates five key figures: net worth goal, total net worth amount, amount to goal, total growth in net worth, and the percentage of net worth to the targeted net worth <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.
*   All values are pulled from the previously discussed databases <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>.

## Primary Dashboard

The primary dashboard of the [[how_to_track_net_worth_using_notion | net worth tracker]] organizes the information from the databases <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.

*   **Summary Section**: Displays the net worth goal, total net worth, amount to goal, total growth, and percentage of net worth goal <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>. This section is linked to the 'Net Worth Goal' database and set in a gallery layout <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.
*   **Monthly Net Worth Overview**: Specifies total assets, total liabilities, net worth, and change in net worth <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>. It is linked to the 'Net Worth Database' and displayed in a gallery layout <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>.
*   **Assets Breakdown** and **Liabilities Breakdown**: These sections are linked to their respective breakdown databases and are also set out in a gallery layout <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.

This structured approach allows for comprehensive [[how_to_track_net_worth_using_notion | net worth tracking]] within [[utilizing_notion_databases_for_financial_tracking | Notion]].