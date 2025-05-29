---
title: Tracking assets and liabilities in Notion
videoId: G2UuEnUUCos
---

From: [[theaccountantguy]] <br/> 

To effectively track assets and liabilities, particularly as part of a [[how_to_track_net_worth_using_notion | net worth tracker using Notion]], a structured approach involving several interlinked databases is required <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>. This system allows for detailed recording, calculation, and visualization of personal finances.

## Tracker Overview <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>

The [[how_to_track_net_worth_using_notion | net worth tracker]] typically includes several sections:

*   **Summary Section** <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>
    *   Net worth goal amount <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>
    *   Total net worth at present <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>
    *   Amount required to reach the net worth goal <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>
    *   Total growth achieved in net worth since January <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>
    *   Percentage of net worth achieved proportional to the targeted goal <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>
*   **Monthly Net Worth Overview** <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>
    *   Total assets for each month <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>
    *   Total liabilities for each month <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>
    *   Net worth for the month <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>
    *   Change in net worth for the month <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>
*   **Breakdown of Assets** <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>
    *   Individual assets classified into categories (e.g., five types) <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>
    *   Amount of each asset <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>
    *   Proportion of each asset to the total assets <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>
*   **Liabilities Breakdown** <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>
    *   Types of liabilities (e.g., four types) <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>
    *   Corresponding amount <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>
    *   Proportion of each liability to the total amount <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>

## Required Databases <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>

Building this [[how_to_track_net_worth_using_notion | net worth tracker]] requires five types of databases, each with specific requirements <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.

### 1. Assets and Liabilities Database <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>

This database is where all assets and liabilities are recorded for each specific month during the year <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.

*   **Asset Description**: Specifies five types of assets <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>.
*   **Opening Balance**: A number property representing the asset's balance at the start of the month <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.
*   **Amount**: Shows the addition or deletion of assets for the specific period <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.
*   **Closing Balance**: Calculated as the opening balance added to the amount during the month <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.
*   **Maintenance**: The closing balance of each month for all assets must be copied and pasted onto the opening balance of the subsequent month <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>. The same process is repeated for the liabilities database <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.

### 2. Assets Breakdown Database <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>

This database provides a breakup of all assets and their individual proportions to the total amount <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.

*   **Asset Types**: Lists the same five assets created in the Assets and Liabilities database <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.
*   **Total Amount**: Represents the total amount of each asset from all months combined, rolled up from the earlier database <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
*   **Total Assets Value**: Calculated and rolled up from another database using a formula <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>.
*   **Percentage**: Calculates the percentage of each asset to the total value of all assets combined <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.

### 3. Liabilities Breakdown Database <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>

Similar to the Assets Breakdown, this database tracks liabilities, comprising four types <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>. The same calculation logic for total value and percentage applies.

### 4. Net Worth Database <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>

This database calculates key financial metrics on a monthly basis <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.

*   **Total Assets**: Considers the closing balance of assets for each month <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.
*   **Total Liabilities**: Uses the closing balance of liabilities for each month <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.
*   **Net Worth**: Calculated by deducting liabilities from assets for the month <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>.
*   **Change in Net Worth**: Deducts the closing net worth from the opening net worth of the assets and liabilities <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.
*   **Data Source**: All amounts are rolled over from the Assets and Liabilities database <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.

### 5. Net Worth Summary Database <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>

This database summarizes the key financial targets and achievements <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>.

*   **Metrics**: Calculates the net worth goal, total net worth, amount to goal, total growth in net worth, and the percentage of the net worth to the targeted net worth <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.
*   **Data Source**: All values are pulled from the previously discussed databases <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>.

## Primary Dashboard <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>

The primary dashboard provides a centralized view of the [[how_to_track_net_worth_using_notion | net worth tracker]] and its components <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.

*   **Summary Section**: Displays the net worth goal, total net worth, amount to goal, total growth, and the percentage of the net worth goal. This section links to the Net Worth Goal database and is often set in a gallery layout <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>.
*   **Monthly Net Worth Overview**: Specifies total assets, total liabilities, net worth, and change in net worth. This links to the Net Worth database and is set in a gallery layout <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>.
*   **Assets Breakdown and Liabilities Breakdown**: These sections are linked to their respective databases and are also displayed in a gallery layout <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.