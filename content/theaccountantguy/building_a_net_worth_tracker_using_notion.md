---
title: Building a net worth tracker using Notion
videoId: G2UuEnUUCos
---

From: [[theaccountantguy]] <br/> 

This article details how to build a [[net_worth_tracking_with_notion | net worth tracker]] using Notion, covering its structure and the required databases to [[tracking_personal_finances_in_notion | track personal finances]] effectively <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

## Tracker Overview

The [[net_worth_tracking_with_notion | net worth tracker]] in Notion includes several key sections to provide a comprehensive financial overview <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>:

### Summary Section

This section displays a high-level summary of your [[net_worth_tracking_with_notion | net worth]] <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>:
*   **Net Worth Goal Amount**: The target amount to achieve <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.
*   **Total Net Worth at Present**: Your current [[net_worth_tracking_with_notion | net worth]] <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.
*   **Amount Required to Reach Goal**: The remaining sum needed to achieve the target <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.
*   **Total Growth Achieved**: The growth in [[net_worth_tracking_with_notion | net worth]] since January <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.
*   **Percentage of Net Worth Achieved**: The proportion of the targeted [[net_worth_tracking_with_notion | net worth]] that has been reached <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.

### Monthly Net Worth Overview

This section provides a monthly breakdown <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>:
*   **Total Assets** for each month <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>.
*   **Total Liabilities** <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.
*   **Net Worth for the Month** <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>.
*   **Change in Net Worth** for the month <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>.

### Breakdown of Assets

This section classifies individual assets into five categories, showing the amount of each asset and its proportion to total assets <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.

### Liabilities Breakdown

This section specifies four types of liabilities, showing their corresponding amounts and proportions to the total liabilities <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.

## Databases Required

To build this [[net_worth_tracking_with_notion | net worth tracker]], five types of databases are required <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>. Each database has distinct requirements <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.

### 1. Assets and Liabilities Database

This database is used to record all assets and liabilities for each specific month during the year <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.
Properties in this database include <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>:
*   **Asset/Liability Description**: Specifies five types of assets <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.
*   **Opening Balance**: A number property indicating the balance at the start of the month <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.
*   **Amount**: Shows additions or deletions of assets/liabilities for the specific period <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.
*   **Closing Balance**: Calculated as the opening balance plus the amount during the month <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.

For ongoing tracking, the closing balance of each month must be copied and pasted onto the opening balance of the subsequent month for all assets and liabilities <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.

### 2. Assets Breakdown Database

This database provides a breakup of all assets and their individual proportions to the total amount <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.
*   It lists the same five assets created earlier <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.
*   The **Total Amount** for each asset is rolled up from the Assets and Liabilities database, combining all months <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.
*   The **Total Assets Value** is calculated and rolled up from another database using a formula <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>.
*   The **Percentage of Each Asset** to the total value of all assets combined is calculated <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.

### 3. Liabilities Breakdown Database

Similar to the Assets Breakdown Database, this database tracks liabilities <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.
*   It comprises four types of liabilities <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.
*   It calculates the proportion of each liability to the total <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.

### 4. Net Worth Database

This database calculates key financial metrics on a monthly basis <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>:
*   **Total Assets**: Considers the closing balance of assets from the Assets and Liabilities database for each month <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.
*   **Total Liabilities**: Uses the closing balance of liabilities from the Assets and Liabilities database for each month <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.
*   **Net Worth**: Calculated by deducting liabilities from assets for the month <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
*   **Change in Net Worth**: Calculated by deducting the opening [[net_worth_tracking_with_notion | net worth]] from the closing [[net_worth_tracking_with_notion | net worth]] of the assets and liabilities <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.

All amounts in this database are rolled over from the Assets and Liabilities database <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.

### 5. Net Worth Summary Database

This database summarizes all the information from the other databases <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>.
It calculates five key metrics <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>:
*   [[net_worth_tracking_with_notion | Net worth]] Goal <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.
*   Total [[net_worth_tracking_with_notion | Net worth]] <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.
*   Amount to Goal <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>.
*   Total Growth in [[net_worth_tracking_with_notion | Net worth]] <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.
*   Percentage of the [[net_worth_tracking_with_notion | net worth]] to the targeted [[net_worth_tracking_with_notion | net worth]] <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.

Values are pulled and totaled from the previously discussed databases <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>.

## Primary Dashboard

The primary dashboard of the [[net_worth_tracking_with_notion | net worth tracker]] integrates the views from the different databases <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>:
*   **Summary Section**: Displays the [[net_worth_tracking_with_notion | net worth]] goal, total [[net_worth_tracking_with_notion | net worth]], amount to goal, total growth, and percentage of [[net_worth_tracking_with_notion | net worth]] goal <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>. This section links to the Net Worth Goal database and is set in a gallery layout <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.
*   **Monthly Net Worth Overview**: Specifies total assets, total liabilities, [[net_worth_tracking_with_notion | net worth]], and change in [[net_worth_tracking_with_notion | net worth]] <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>. It is linked to the Net Worth database and displayed in a gallery layout <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>.
*   **Assets Breakdown and Liabilities Breakdown**: These sections are linked to their respective breakdown databases and are also set out in a gallery layout <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.