---
title: Building a Net Worth Tracker with Notion
videoId: G2UuEnUUCos
---

From: [[theaccountantguy]] <br/> 

This guide explains how to [[tracking_net_worth_with_notion | build a net worth tracker using Notion]] <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. The tracker is designed to provide a comprehensive overview of financial health, including assets, liabilities, and progress towards a net worth goal <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.

## Tracker Overview

The Net Worth Tracker consists of several key sections:

*   **Summary Section** This section displays:
    *   The net worth goal amount <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.
    *   The total current net worth <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.
    *   The remaining amount needed to reach the net worth goal <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.
    *   The total growth in net worth achieved since January <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.
    *   A percentage indicating net worth achieved relative to the targeted amount <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.
*   **Monthly Net Worth Overview** This section provides monthly data for:
    *   Total assets <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.
    *   Total liabilities <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.
    *   Net worth for the month <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.
    *   Change in net worth for the month <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>.
*   **Breakdowns** These sections detail:
    *   **Assets Breakdown**: Individual assets are classified into five categories, showing their amount and proportion to total assets <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.
    *   **Liabilities Breakdown**: Four types of liabilities are specified, along with their corresponding amount and proportion to the total liabilities <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.

## Database Requirements

[[tracking_net_worth_in_notion | Building this net worth tracker in Notion]] requires the use of five distinct databases <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>.

### 1. Assets and Liabilities Database

This database is used to record all assets and liabilities for each specific month of the year <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.

*   **Asset Description**: Specifies five types of assets <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.
*   **Opening Balance**: A number property representing the asset balance at the start of the month <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.
*   **Amount**: Shows additions or deletions of assets for the period <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.
*   **Closing Balance**: Calculated by adding the "Opening Balance" to the "Amount" during the month <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.
*   The closing balance of each month for all assets must be copied and pasted as the opening balance for the subsequent month <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>. This process is repeated for the liabilities database as well <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.

### 2. Assets Breakdown Database

This database provides a detailed breakdown of all assets and their individual proportions to the total amount <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>.

*   It lists the same five asset types created previously <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.
*   The total amount of each asset per month is represented using a rollup formula from the Assets and Liabilities database <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
*   Total assets value is calculated and rolled up from another database using a formula <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>.
*   The percentage of each asset to the total value of all assets combined is calculated and represented visually with a green bar <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.

### 3. Liabilities Breakdown Database

Similar to the Assets Breakdown, this database provides a breakdown for liabilities <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>. It comprises four types of liabilities <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.

### 4. Net Worth Database

This database calculates the total assets, total liabilities, net worth, and the change in net worth for each subsequent month <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.

*   **Total Assets**: Considers the closing balance of assets for each month <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.
*   **Total Liabilities**: Considers the closing balance of liabilities for each month <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.
*   **Net Worth**: Calculated by deducting liabilities from assets for the month <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>.
*   **Change in Net Worth**: Calculated by deducting the closing net worth from the opening net worth of assets and liabilities <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.
*   All amounts in this database are rolled over from the Assets and Liabilities database <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.

### 5. Net Worth Summary Database

This database summarizes the key financial metrics <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>. It calculates five main items:

*   Net worth goal <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>.
*   Total net worth amount <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.
*   Amount required to reach the goal <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>.
*   Total growth in net worth <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.
*   Percentage of net worth achieved relative to the targeted net worth <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.

All values are pulled and totaled from the other databases <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>.

## Primary Dashboard

The primary dashboard serves as the central hub for the net worth tracker <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.

*   **Summary Section**: Displays the net worth goal, total net worth, amount to goal, total growth, and percentage of net worth goal <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>. This section is linked to the Net Worth Goal database and set in a gallery layout <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.
*   **Monthly Net Worth Overview**: Specifies total assets, total liabilities, net worth, and change in net worth <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>. It is linked to the Net Worth database and displayed in a gallery layout <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>.
*   **Assets and Liabilities Breakdowns**: These sections are linked to their respective breakdown databases and are also set out in a gallery layout <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.

This concludes the discussion on [[using_notion_for_financial_tracking | using Notion for financial tracking]] and specifically, [[setting_up_an_investment_portfolio_tracker_in_notion | building a Net Worth Tracker]] <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>.