---
title: Understanding Notion Finance Templates for Personal Use
videoId: G2UuEnUUCos
---

From: [[theaccountantguy]] <br/> 

This guide details how to build a net worth tracker using [[notion_finance_templates | Notion finance templates]] for personal use, providing an overview of its structure and the underlying databases required <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

## Net Worth Tracker Overview

The net worth tracker built in Notion includes several key sections:

*   **Summary Section** <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>:
    *   Net worth goal amount <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.
    *   Total net worth at present <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.
    *   Amount required to reach the net worth goal <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.
    *   Total growth achieved in net worth since January <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.
    *   Percentage of net worth achieved in proportion to the targeted amount <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.
*   **Monthly Net Worth Overview** <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>:
    *   Total assets for each month <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.
    *   Total liabilities for each month <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.
    *   Net worth for the month <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.
    *   Change in net worth for the month <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>.
*   **Assets Breakdown** <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>:
    *   Individual assets classified into five categories <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.
    *   The amount of each asset <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.
    *   The proportion of each asset to total assets <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.
*   **Liabilities Breakdown** <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>:
    *   Four types of liabilities <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.
    *   Corresponding amount and proportion of each liability to the total amount <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.

## Database Structure for the Net Worth Tracker

To build this net worth tracker, five types of databases are required <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>. Each database serves a distinct purpose <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.

### 1. Assets and Liabilities Database

This database records all assets and liabilities for each specific month during the year <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.

*   **Asset Description**: Specifies five types of assets <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.
*   **Opening Balance**: A number property indicating the asset's balance at the start of the month <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.
*   **Amount**: Shows the addition or deletion of assets for the specific period <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.
*   **Closing Balance**: Calculated as the opening balance added to the amount during the month <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.
*   **Data Flow**: The closing balance of each month for all assets must be copied and pasted onto the opening balance of the subsequent month <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>. The same process is repeated for the liabilities database <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.

### 2. Assets Breakdown Database

This database provides a detailed breakup of all assets and their individual proportions to the total amount <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.

*   **Listed Assets**: The same five asset types created earlier are listed <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.
*   **Total Amount**: The total amount for each asset from all months combined is represented by a formula rolled up from the Assets and Liabilities database <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
*   **Total Assets Value**: Calculated and rolled up from another database using a formula <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>.
*   **Percentage Calculation**: The percentage of each asset relative to the total value of all assets combined is calculated and represented visually with a green bar <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.
*   **Liabilities Breakdown**: A similar setup is used for the liabilities breakdown, comprising four types of liabilities <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.

### 3. Net Worth Database

This database is responsible for calculating key financial figures on a monthly basis <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.

*   **Total Assets**: Calculated based on the closing balance of assets for each month <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.
*   **Total Liabilities**: Calculated based on the closing balance of liabilities for each month <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.
*   **Net Worth**: Determined by deducting liabilities from assets for the month <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
*   **Change in Net Worth**: Calculated by deducting the closing net worth from the opening net worth of assets and liabilities <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.
*   **Data Source**: All amounts in this database are rolled over from the Assets and Liabilities database <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.

### 4. Net Worth Summary Database

This database summarizes all the calculated figures, forming the core of the net worth tracker's summary section <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>.

*   **Calculated Values**: Includes net worth goal, total net worth amount, amount to goal, total growth in net worth, and the percentage of net worth to the targeted net worth <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.
*   **Data Aggregation**: All values are pulled from the previously discussed databases and totaled as desired <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>.

## Primary Dashboard of the Net Worth Tracker

The primary dashboard serves as the central hub for viewing all summarized financial data <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.

*   **Summary Section**: Displays the net worth goal, total net worth, amount needed to reach the goal, total growth, and the percentage of the net worth goal achieved <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>. This section is linked to the Net Worth Summary database and displayed in a gallery layout <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.
*   **Monthly Net Worth Overview**: Specifies total assets, total liabilities, net worth, and change in net worth <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>. It is linked to the Net Worth database and set in a gallery layout <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>.
*   **Assets Breakdown and Liabilities Breakdown**: These sections are linked to their respective Assets Breakdown and Liabilities Breakdown databases, also set out in a gallery layout <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.

This structured approach, leveraging multiple linked databases and views, allows for comprehensive [[using_notion_for_financial_management | financial management]] and tracking of net worth within Notion <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>.