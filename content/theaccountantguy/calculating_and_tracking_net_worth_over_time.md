---
title: Calculating and Tracking Net Worth over Time
videoId: G2UuEnUUCos
---

From: [[theaccountantguy]] <br/> 

This article outlines how to build a [[building_a_net_worth_tracker_using_notion | net worth tracker using Notion]], detailing its structure, components, and the underlying databases required to track personal finances effectively. <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>

## Net Worth Tracker Overview

A comprehensive net worth tracker in Notion includes several key sections:

*   **Summary Section** <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>: Displays the net worth goal, current total net worth, the amount still needed to reach the goal, total growth achieved since January, and the percentage of the net worth goal achieved. <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>
*   **Monthly Net Worth Overview** <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>: Provides a month-by-month breakdown of total assets, total liabilities, the net worth for the month, and the change in net worth for that month. <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>
*   **Assets Breakdown** <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>: Categorizes individual assets into five types, showing the amount of each asset and its proportion to total assets. <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>
*   **Liabilities Breakdown** <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>: Specifies four types of liabilities, along with their corresponding amounts and proportions relative to total liabilities. <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>

## Database Structure

Building this [[net_worth_tracker_layout_and_structure | net worth tracker]] requires the use of five distinct databases, each serving a specific purpose. <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>

### Assets and Liabilities Database

This database serves as the primary record for all assets and liabilities for each specific month during the year. <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>

*   **Asset Description**: Five types of assets are specified here. <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>
*   **Opening Balance**: A number property representing the asset's balance at the start of the month. <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>
*   **Amount**: Shows additions or deletions to assets for the specific period. <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>
*   **Closing Balance**: Calculated by adding the opening balance to the amount during the month. <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>
*   **Monthly Rollover**: The closing balance of each month for all assets must be copied and pasted as the opening balance for the subsequent month. <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a> The same process applies to the liabilities database. <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>

### Assets Breakdown Database

This database provides a detailed breakup of all assets and their individual proportions to the total asset amount. <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>

*   **Listed Assets**: The same five assets created in the Assets and Liabilities database are listed. <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>
*   **Total Amount**: The total amount of each asset from all months combined is rolled up from the earlier database. <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>
*   **Total Assets Value**: This value is calculated and rolled up from another database using a formula. <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>
*   **Percentage of Each Asset**: The percentage of each asset relative to the total value of all assets combined is calculated and represented. <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>

### Liabilities Breakdown Database

This database functions similarly to the Assets Breakdown, focusing on liabilities. <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a> It comprises four types of liabilities, showing their amounts and proportions. <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>

### Net Worth Database

This database is central to calculating the net worth over time. <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>

*   **Total Assets**: Calculated using the closing balance of assets for each month. <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>
*   **Total Liabilities**: Calculated using the closing balance of liabilities for each month. <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>
*   **Net Worth**: Derived by deducting total liabilities from total assets for the month. <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>
*   **Change in Net Worth**: Calculated by deducting the closing net worth from the opening net worth of assets and liabilities. <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>
*   All amounts in this database are rolled over from the Assets and Liabilities database. <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>

### Net Worth Summary Database

This database summarizes the key financial figures discussed, providing a high-level overview. <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>

*   It calculates five main figures: net worth goal, total net worth, amount needed to reach the goal, total growth in net worth, and the percentage of net worth achieved relative to the target. <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>
*   All values are pulled and totaled from the other databases. <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>

## Primary Dashboard

The primary dashboard of the [[net_worth_tracker_layout_and_structure | net worth tracker]] integrates all the databases to present a cohesive view. <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>

*   **Summary Section**: Displays the net worth goal, total net worth, amount to goal, total growth, and percentage of net worth goal achieved. <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a> This section is linked to the net worth goal database and displayed in a gallery layout. <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>
*   **Monthly Net Worth Overview**: Shows total assets, total liabilities, net worth, and change in net worth. <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a> This is linked to the net worth database and also set in a gallery layout. <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>
*   **Assets and Liabilities Breakdown**: These sections are directly linked to their respective breakdown databases and displayed in a gallery layout. <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>