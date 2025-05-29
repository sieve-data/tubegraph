---
title: Organizing income sources with Notion databases
videoId: 2MkChIwv0t0
---

From: [[theaccountantguy]] <br/> 

This guide details how to build an [[tracking_income_and_expenses_in_notion | income tracker in Notion]] to help stay on top of your [[managing_finances_with_notion | finances]] <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. The tracker is designed to be minimalistic and provides a comprehensive overview of income streams <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.

## Tracker Sections

The [[managing_finances_using_notion | Notion income tracker]] is divided into four main sections:

*   **Total Earnings** Displays the total amount of earnings for a specified period <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.
*   **Sources of Income** Breaks down earnings by source (e.g., salary, side hustle), showing total earnings per source and its percentage of the overall income <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.
*   **Frequency of Income** Illustrates how frequently income is earned, including the total earnings and number of sources for each frequency type <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.
*   **Overview Section** Presents monthly income, segmented into four quarters, along with each month's percentage of total earnings <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.

## Essential Databases

To construct this [[tracking_personal_finances_in_notion | Notion income tracker]], five [[setting_up_a_database_in_notion_for_financial_tracking | databases]] are required <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>:

1.  **Income Details Database** Stores specific details of income earned <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.
2.  **Income Source Database** Tracks income relative to each specific source <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.
3.  **Frequency of Income Database** Provides an overview of how often income is earned within a period <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.
4.  **Total Earnings Database** Reflects the cumulative earnings over a given period <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.
5.  **Period Database** Displays periodical income earned throughout a year <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.

### Income Details Database

This [[setting_up_a_database_in_notion_for_financial_tracking | database]] is where income details are recorded and analyzed <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>.

*   **Income Details Property** A title property used to specify different income sources received during the year <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.
*   **Period of Income** A relation property linked to the Period database, showing monthly incomes per source <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>.
*   **Income Source** A relation property linked to the Income Source database, indicating the source of income (e.g., salary, side hustle, other income) <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>.
*   **Frequency of Income** A relation property linked to the Frequency of Income database, specifying how frequently income is earned <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.
*   **Amount** Shows the amount of income earned for a particular period <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>.
*   **Sum of Income** At the bottom, displays the total sum of income earned during the period <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>.

### Income Source Database

This [[setting_up_a_database_in_notion_for_financial_tracking | database]] analyzes different income sources <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>.

*   **Name Property** Defines income sources like salary, side hustle, and other income <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.
*   **Earnings Database** A relation property linked to the Total Earnings database <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>.
*   **Income Details Property** A relation property linked to the Income Details database, relating all incomes to their sources <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.
*   **Actual Income** A roll-up property derived from the Income Details database, calculating the sum of the "Amount" property <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.
*   **Total Earnings Property** A roll-up property derived from the Earnings database, showing the original total earnings value <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.
*   **Frequency Property** A roll-up property from the Income Details database, extracting and displaying the "Frequency of Income" property's original values <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.
*   **Earnings in Percentage** A formula property that calculates the percentage of specific earnings relative to total earnings <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>. This is represented with a percent format and a green bar <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.

### Frequency of Income Database

This [[setting_up_a_database_in_notion_for_financial_tracking | database]] provides an analysis of income earning frequency <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.

*   **Frequency Column** A title column indicating how frequently income is earned (e.g., monthly, annual, quarterly, half-yearly, one-time) <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>.
*   **Earnings Associated to Each Frequency of Income** A roll-up property derived from a related property, calculating the sum of earnings for each frequency mode <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.
*   **Relation Property** Linked to the Income Details database, defining all income sources related to each frequency <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>.
*   **Sources of Income** A formula property that calculates and labels the number of sources for each frequency (e.g., "one source", "two sources", "no source") <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>.

### Total Earnings Database

This [[setting_up_a_database_in_notion_for_financial_tracking | database]] connects the total earnings to all three income sources <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>.

*   **Total Earnings (Title Property)** <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>.
*   **Income Source** A relation property established with the Income Source database <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>.
*   **Total Earnings (Roll-up Property)** A roll-up property that aggregates values from the income sources and calculates their sum to represent total earnings <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>.

### Period Database

This final [[setting_up_a_database_in_notion_for_financial_tracking | database]] calculates periodical income monthly and analyzes it, showing each month's earnings as a percentage of total annual earnings <a class="yt-timestamp" data-t="00:07:46">[00:07:46]</a>.

*   **Month Property** A title-type property representing the month of income <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>.
*   **Income Details** A relation property linked to the Income Details database, showing earned income <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>.
*   **Earnings Property** A roll-up property from the Income Details database, calculating the sum of earnings <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>.
*   **Total Earnings** A roll-up property from the Total Earnings database, displaying original earnings values <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>. This shows earnings per month and overall total earnings <a class="yt-timestamp" data-t="00:08:38">[00:08:38]</a>.
*   **Proportion of Earnings** A formula property that calculates each month's earnings divided by total earnings, displayed as a green percentage bar <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>.

## Primary Dashboard Presentation

The primary dashboard visually presents all the collected income data <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>.

### Total Earnings Display

The total earnings represent the overall income earned during a period <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>. This is a linked view of the Total Earnings database, presented in a list view format <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>.

### Sources of Income Display

This section uses a three-column layout, created by typing `/three columns` <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a>. Each column is linked to the Income Source database and displayed in a gallery format <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>. It shows the actual income and percentage for each income source relative to the total income <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>.

### Frequency Display

The frequency display is derived from the Frequency of Income database and is presented in a gallery layout <a class="yt-timestamp" data-t="00:09:53">[00:09:53]</a>. It showcases total earnings and sources of earnings for each frequency <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>.

### Overview Section

This section is linked to the Period database and uses a gallery mode presentation <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>. Information is divided into four quarters, with individual months specified within each <a class="yt-timestamp" data-t="00:10:12">[00:10:12]</a>. It displays earnings for each month and their proportion to total earnings <a class="yt-timestamp" data-t="00:10:19">[00:10:19]</a>. Filters are applied for each quarter to show respective months <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>.

This completes the [[using_notion_for_financial_management | Notion income tracker]] setup <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>. A template is available for direct use <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>.