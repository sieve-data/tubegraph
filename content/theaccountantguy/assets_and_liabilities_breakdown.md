---
title: Assets and liabilities breakdown
videoId: G2UuEnUUCos
---

From: [[theaccountantguy]] <br/> 

This article details how assets and liabilities are tracked, broken down, and used to calculate net worth within a [[managing_asset_financials_in_notion | Notion]] net worth tracker <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. The system utilizes five distinct databases to achieve this <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>.

## Net Worth Tracker Overview

The net worth tracker provides a summary section that includes:
*   Total net worth at present <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.
*   Total growth achieved in net worth since January <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.
*   A percentage showing net worth achieved in proportion to the targeted amount <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.

A monthly net worth overview specifies total assets, total liabilities, net worth for the month, and the change in net worth for the month <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.

The tracker also includes:
*   A breakdown of assets, categorizing individual assets into five types, showing their amount and proportion to total assets <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.
*   A liabilities breakdown, specifying four types of liabilities, their corresponding amount, and proportion to the total amount <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.

## Core Databases for Assets and Liabilities

### Assets and Liabilities Database
This database is central to recording all assets and liabilities for each specific month during the year <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.
*   **Asset Description**: Specifies five types of assets <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>.
*   **Opening Balance**: A number property representing the balance at the start of the month <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.
*   **Amount**: Shows additions or deletions of assets/liabilities for the period <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.
*   **Closing Balance**: Calculated as the opening balance plus the amount during the month <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.

For continuity, the closing balance of each month must be copied and pasted as the opening balance for the subsequent month for all assets and liabilities <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.

### Assets Breakdown
This database provides a detailed breakup of all assets and their individual proportions to the total amount <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.
*   It lists the same five asset types established earlier <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.
*   The total amount for each asset from all months combined is rolled up from the primary assets database <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
*   The total assets value is calculated and rolled up from another database using a formula <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>.
*   The percentage of each asset relative to the total value of all assets combined is calculated and represented visually with a green bar <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.

### Liabilities Breakdown
Similar to the assets breakdown, this database details the breakdown of liabilities, comprising four types <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>. This provides insight into [[debt_overview_and_classification | debt overview]] and [[debt_overview_and_loan_categories | loan categories]] for tracking <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.

### Net Worth Database
This database calculates key financial metrics:
*   **Total Assets**: Considers the closing balance of assets for each month <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.
*   **Total Liabilities**: Considers the closing balance of liabilities for each month <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.
*   **Net Worth**: Calculated by deducting liabilities from assets for the month <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.
*   **Change in Net Worth**: Calculated by deducting the closing net worth from the opening net worth of the assets and liabilities <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.
*   All amounts in this database are rolled over from the initial assets and liabilities database <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.

## Net Worth Summary
The net worth summary section aggregates all discussed data to display five key figures:
*   Net worth goal <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.
*   Total net worth amount <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.
*   Amount required to reach the goal <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>.
*   Total growth in net worth <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.
*   Percentage of net worth achieved against the targeted net worth <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.
All values are pulled and totaled from the previously discussed databases <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>.

## Primary Dashboard Integration
The primary dashboard of the net worth tracker displays the integrated summary and breakdowns:
*   **Summary Section**: Shows the net worth goal, total net worth, amount to goal, total growth, and percentage of net worth goal, linked to the net worth goal database in a gallery layout <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.
*   **Monthly Net Worth Overview**: Specifies total assets, total liabilities, net worth, and change in net worth, linked to the net worth database in a gallery layout <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>.
*   **Assets Breakdown and Liabilities Breakdown**: Linked to their respective databases and displayed in a gallery layout <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.

This comprehensive setup allows for detailed [[tracking_finances_expenses_and_investments | financial tracking]] and analysis of an individual's financial position <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>.