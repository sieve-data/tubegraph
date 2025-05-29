---
title: Tracking total earnings using Notion
videoId: 2MkChIwv0t0
---

From: [[theaccountantguy]] <br/> 

This article details how to [[creating_an_income_tracker_in_notion | create an income tracker in Notion]] to stay on top of your finances, specifically focusing on tracking total earnings <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>. This minimalistic tracker is designed to provide a comprehensive overview of income, its sources, frequency, and periodical segregation <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.

## Key Sections of the Notion Income Tracker

The Notion income tracker is organized into four main sections:
*   **Total Earnings** Displays the cumulative income for a specified period <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.
*   **Sources of Income** Identifies different income streams like salary, side hustle, or other sources, showing total earnings for each and its percentage of the total income <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.
*   **Frequency of Income** Shows how often income is earned, along with total earnings and the number of sources for each frequency <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.
*   **Overview Section** Provides monthly income segregated into four quarters, including the percentage of monthly earnings relative to total earnings <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.

## Required Databases

To build this Notion income tracker, five interconnected databases are utilized <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>:

1.  **Income Details Database** Stores specific information about income earned <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.
2.  **Income Source Database** Organizes income based on its origin <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.
3.  **Frequency of Income Database** Offers an overview of how often income is received <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.
4.  **Total Earnings Database** Reflects the grand total of earnings for a given period <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.
5.  **Period Database** Tracks income earned periodically throughout a year <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.

### Income Details Database

This database is where the raw data related to income is entered <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>.
*   **Income Details Property (Title)** The default title property where different sources of income received during the year are specified <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.
*   **Period of Income (Relation)** A relation property linked to the Period database, showing monthly incomes per source <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>.
*   **Income Source (Relation)** Linked to the Income Source database, specifying the origin of income (e.g., salary, side hustle) <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>.
*   **Frequency of Income (Relation)** Linked to the Frequency of Income database, indicating how frequently income is earned <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.
*   **Amount (Number)** Shows the monetary value of income for a particular period <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>. The sum of income earned during the period is displayed at the bottom <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>.

### Income Source Database

This database analyzes different sources of income <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>.
*   **Name (Title)** Defines income sources like salary, side hustle, or other income <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.
*   **Earnings Database (Relation)** Related to the Total Earnings database <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>.
*   **Income Details Property (Relation)** Related to the Income Details database, linking all incomes <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.
*   **Actual Income (Roll-up)** Derived from the Income Details database, rolling up the 'Amount' property and calculating its sum <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.
*   **Total Earnings Property (Roll-up)** Derived from the Earnings database, it shows the original value of the total earnings <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.
*   **Frequency Property (Roll-up)** Extracts the 'Frequency of Income' property from the Income Details database, showing original values <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.
*   **Earnings in Percentage (Formula)** Calculates the percentage of earnings from a specific source to the total earnings, displayed as a green percentage bar <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>.

### Frequency of Income Database

This database analyzes how frequently income is earned <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.
*   **Frequency (Title)** Indicates income frequency (e.g., monthly, annual, quarterly, half-yearly, one-time) <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>.
*   **Earnings Associated (Roll-up)** Derived from a related property, it calculates the sum of earnings for each frequency mode <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.
*   **Relation Property (Relation)** Related to the Income Details database, defining all income sources tied to each frequency <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>.
*   **Sources of Income (Formula)** A formula property that calculates the number of sources, displaying "one source," "two sources," "three sources," or "no source" based on the count <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>.

### Total Earnings Database

This database links total earnings to all three sources of income <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.
*   **Total Earnings (Title)** The main title property <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>.
*   **Income Source (Relation)** A relation property established with the Income Source database, linking to the three specified income sources <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>.
*   **Total Earnings (Roll-up)** Rolls up values from the income sources and calculates the sum of total earnings associated with them <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>.

### Period Database

This database calculates periodical income for each month and performs further analysis <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>. It also shows the percentage of monthly earnings to the total earnings for the year <a class="yt-timestamp" data-t="00:07:57">[00:07:57]</a>.
*   **Month (Title)** A title property representing the month of income <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>.
*   **Income Details (Relation)** Related to the Income Details database, showing the income earned <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>.
*   **Earnings (Roll-up)** Rolled up from the Income Details database, calculating and presenting the sum of earnings <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>.
*   **Total Earnings (Roll-up)** Rolled up from the Total Earnings database, showing original values of earnings <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>.
*   **Proportion of Earnings (Formula)** Calculates the percentage of each month's earning relative to the total earnings for the year, displayed as a green percentage bar <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>.

## Primary Dashboard Presentation

The primary dashboard serves as the main interface for viewing the income tracker <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>.

*   **Total Earnings** This section represents the total income earned during the period <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>. It is a linked view to the Total Earnings database, presented in a list view <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>.
*   **Sources of Income** Presented in a three-column layout (created by typing `/three columns`) <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a>. Each column is linked to the Income Source database and displayed in a gallery format <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>. It shows the actual income and percentage of each source to the total income <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>.
*   **Frequency** Derived from the Frequency of Income database, displayed in a gallery layout <a class="yt-timestamp" data-t="00:09:53">[00:09:53]</a>. It shows the total earnings and sources of earnings for each frequency <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>.
*   **Overview Section** Linked to the Period database and displayed in gallery mode <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>. Information is divided into four quarters, with individual months specified for each <a class="yt-timestamp" data-t="00:10:12">[00:10:12]</a>. It displays earnings for each month and their proportion to total earnings <a class="yt-timestamp" data-t="00:10:19">[00:10:19]</a>. Filters are applied to specify respective months for each quarter <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>.

This comprehensive Notion income tracker helps in [[tracking_personal_finances_in_notion | tracking personal finances in Notion]] by providing detailed insights into income streams and patterns <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a>.