---
title: Setting Up Notion Databases for Income Tracking
videoId: 2MkChIwv0t0
---

From: [[theaccountantguy]] <br/> 

This article outlines how to build a minimalistic income tracker in Notion to [[tracking_personal_finances_using_notion | stay on top of finances]] <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. The tracker is organized into four main sections: total earnings, sources of income, frequency of income, and an overview section <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.

## Income Tracker Sections

The Notion income tracker includes the following sections:
*   **Total Earnings** <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>: Displays the total earnings for a specified period <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>.
*   **Sources of Income** <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>: Shows total earnings for each individual income source (e.g., salary, side hustle) and its percentage of the total income <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.
*   **Frequency of Income** <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>: Indicates how frequently income is earned, calculating total earnings and the number of sources for each frequency <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.
*   **Overview Section** <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>: Presents monthly income segregated into four quarters, along with the percentage of monthly earnings relative to total earnings <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>.

## Databases Required for Income Tracking

To build this income tracker, five interconnected [[setting_up_and_using_databases_in_notion | Notion databases]] are necessary <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>:
1.  **Income Details Database**: Stores specifics about income earned <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.
2.  **Income Source Database**: Organizes income by each source <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.
3.  **Frequency of Income Database**: Provides an overview of income earning frequency <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.
4.  **Total Earnings Database**: Reflects the total income earned over a period <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.
5.  **Period Database**: Shows periodical income earned throughout the year <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.

## Building the Databases

### 1. Income Details Database
This database is used for inputting and analyzing income details <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>.
*   **Income Details**: A default "title" [[setting_up_notion_database_properties | property]] where different sources of income received during the year are specified <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.
*   **Period of Income**: A "relation" [[setting_up_notion_database_properties | property]] linked to the "Period Database," reflecting monthly incomes per source <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>.
*   **Income Source**: A "relation" [[setting_up_notion_database_properties | property]] linked to the "Income Source Database," specifying the source of income (e.g., salary, side hustle, other) <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>.
*   **Frequency of Income**: A "relation" [[setting_up_notion_database_properties | property]] linked to the "Frequency of Income Database," indicating how frequently income is earned <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.
*   **Amount**: A "number" [[setting_up_notion_database_properties | property]] showing the income earned for a specific period, with the sum of income visible at the end <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>.

### 2. Income Source Database
This database analyzes different sources of income <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>.
*   **Name**: A "title" [[setting_up_notion_database_properties | property]] defining income sources (e.g., Salary, Side Hustle, Other Income) <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.
*   **Earnings**: A "relation" [[setting_up_notion_database_properties | property]] linked to the "Total Earnings Database" <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>.
*   **Income Details**: A "relation" [[setting_up_notion_database_properties | property]] linked to the "Income Details Database" <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.
*   **Actual Income**: A "roll-up" [[setting_up_notion_database_properties | property]] derived from the "Income Details Database" (specifically the "Amount" [[setting_up_notion_database_properties | property]]), calculating the sum of earnings for each source <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.
*   **Total Earnings**: A "roll-up" [[setting_up_notion_database_properties | property]] derived from the "Earnings Database" (specifically the "Amount" [[setting_up_notion_database_properties | property]]), showing the original value <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.
*   **Frequency**: A "roll-up" [[setting_up_notion_database_properties | property]] from the "Income Details Database," extracting the "Frequency of Income" [[setting_up_notion_database_properties | property]] values <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.
*   **Earnings in Percentage**: A "formula" [[setting_up_notion_database_properties | property]] that calculates the percentage of a source's earnings to the total earnings, formatted as a green percent bar <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>.

### 3. Frequency of Income Database
This database analyzes how frequently income is earned <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.
*   **Frequency**: A "title" column indicating earning frequency (e.g., Monthly, Annual, Quarterly, Half Yearly, One-time) <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>.
*   **Earnings Associated**: A "roll-up" [[setting_up_notion_database_properties | property]] derived from the "Income Details Database" (specifically the "Amount" [[setting_up_notion_database_properties | property]]), calculating the sum of earnings for each frequency <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.
*   **Relation to Income Details**: A "relation" [[setting_up_notion_database_properties | property]] linked to the "Income Details Database," defining income sources related to each frequency <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>.
*   **Sources of Income**: A "formula" [[setting_up_notion_database_properties | property]] calculating the number of sources. For example, "1 source" if the number is 1, "2 sources" for 2, "3 sources" for 3, and "No source" for 0 <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>.

### 4. Total Earnings Database
This database relates total earnings to income sources <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.
*   **Total Earnings**: A "title" [[setting_up_notion_database_properties | property]] describing the total earnings <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>.
*   **Income Source**: A "relation" [[setting_up_notion_database_properties | property]] linked to the "Income Source Database," specifying the three sources of income <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>.
*   **Total Earnings (Roll-up)**: A "roll-up" [[setting_up_notion_database_properties | property]] of values from the "Income Sources" relation, calculating the sum of earnings associated with these sources <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>.

### 5. Period Database
This database calculates periodical income for each month and provides further analysis <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>. It also shows the percentage of monthly earnings relative to the total earnings for the year <a class="yt-timestamp" data-t="00:07:57">[00:07:57]</a>.
*   **Month**: A "title" [[setting_up_notion_database_properties | property]] representing the month of income <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>.
*   **Income Details**: A "relation" [[setting_up_notion_database_properties | property]] linked to the "Income Details Database," showing earned income <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>.
*   **Earnings**: A "roll-up" [[setting_up_notion_database_properties | property]] from the "Income Details Database," calculating the sum of earnings <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>.
*   **Total Earnings**: A "roll-up" [[setting_up_notion_database_properties | property]] from the "Total Earnings Database," representing the total earnings amount with original values <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>.
*   **Proportion**: A "formula" [[setting_up_notion_database_properties | property]] that calculates the proportion of each month's earnings to the total earnings, formatted as a green percent bar <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>.

## Primary Dashboard Presentation

The primary dashboard visually presents the [[tracking_income_and_expenses_using_notion | income tracker]] <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>.
*   **Total Earnings Display**: A linked view of the "Total Earnings Database" displayed in a "list view" <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.
*   **Sources of Income Display**: Presented in a three-column layout (created using `/three columns`), linked to the "Income Source Database" with a "gallery format" <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a>. This section shows actual income and its percentage of the total income for each source <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>.
*   **Frequency Display**: Derived from the "Frequency of Income Database" and displayed in a "gallery format," showing total earnings and sources of earnings for each frequency <a class="yt-timestamp" data-t="00:09:53">[00:09:53]</a>.
*   **Overview Section**: Linked to the "Period Database" in "gallery mode" <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>. Information is divided into four quarters, with individual months specified for each <a class="yt-timestamp" data-t="00:10:13">[00:10:13]</a>. Filters are applied to specify respective months for each quarter <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>.