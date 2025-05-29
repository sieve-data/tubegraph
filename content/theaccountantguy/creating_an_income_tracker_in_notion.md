---
title: Creating an income tracker in Notion
videoId: 2MkChIwv0t0
---

From: [[theaccountantguy]] <br/> 

This article details how to build an income tracker in Notion to help users stay on top of their finances <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.

## Key Sections of the Notion Income Tracker

The Notion income tracker is organized into four main sections:
*   **Total Earnings**: Displays the total amount of earnings for a specific period <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.
*   **Sources of Income**: Shows total earnings for each individual income source (e.g., salary, side hustle, other) and its percentage of the total income <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.
*   **Frequency of Income**: Indicates how frequently income is earned, calculating total earnings and the number of sources for each frequency <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.
*   **Overview Section**: Presents monthly income, segregated into four quarters, along with the percentage of monthly earnings relative to total earnings <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.

## Required Databases

To build this Notion income tracker, five databases are required <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>:
*   **Income Details Database**: Stores the specific details of income earned <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.
*   **Income Source Database**: Tracks income earned with respect to each source <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.
*   **Frequency of Income Database**: Provides an overview of how frequently income is earned during a period <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.
*   **Total Earnings Database**: Reflects the total earnings accumulated during a given period <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.
*   **Period Database**: Shows periodical income earned throughout a year <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.

## Database Details

### Income Details Database
This database is used to feed and analyze income-related details <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>.
*   **Income Details Property**: A default title property where different sources of income received during the year are specified <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.
*   **Period of Income**: A relation property linked to the Period database, reflecting monthly incomes per source <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>.
*   **Income Source**: A relation property linked to the Income Source database, specifying the income source (e.g., salary, side hustle, other) <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>.
*   **Frequency of Income**: A relation property linked to the Frequency of Income database, indicating how frequently income is earned <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.
*   **Amount**: Shows the amount of income earned for a particular period <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>. The sum of income earned during the period is displayed at the end <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>.

### Income Source Database
This database analyzes different sources of income <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>.
*   **Name Property**: Defines the different sources of income, such as salary, side hustle, and other income <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.
*   **Earnings Database**: A relation property linked to the Total Earnings database, applied to the three specified income sources <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>.
*   **Income Details Property**: A relation property linked to the Income Details database, relating all incomes <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.
*   **Actual Income Property**: A roll-up property derived from the Income Details database, summing the 'Amount' property to show actual income <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.
*   **Total Earnings Property**: A roll-up property derived from the Earnings database, defining and calculating the amount from the earnings database, showing the original value <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.
*   **Frequency Property**: A roll-up property from the Income Details database, extracting the 'Frequency of Income' property and displaying original values <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.
*   **Earnings in Percentage**: A formula property that calculates the percentage of earnings relative to total earnings <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>, formatted as a percent with a green bar <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.

### Frequency of Income Database
This database provides analysis on how frequently income is earned <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.
*   **Frequency Column**: A title column indicating income frequency (e.g., monthly, annual, quarterly, half-yearly, one-time income) <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>.
*   **Earnings Associated to each Frequency of Income**: A roll-up property derived from a related property, which calculates the sum of earnings amounts for each frequency mode <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.
*   **Relation Property**: Linked to the Income Details database, automatically defining all income sources related to each frequency <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>.
*   **Sources of Income**: A formula property that calculates the number of sources <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>. It defines the source count (e.g., "one source", "two sources", "three sources", "no source") based on the number of sources <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>.

### Total Earnings Database
This database relates total earnings to all three income sources and finds the associated earnings <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.
*   **Total Earnings**: A title property described by its name <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>.
*   **Income Source**: A relation property established with the Income Source database, specifying the three income sources <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>.
*   **Total Earnings (Roll-up)**: A roll-up property that extracts values from income sources and calculates the sum of total earnings associated with these sources <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>.

### Period Database
This database calculates periodical income for each month and performs further analysis <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>, also showing the percentage of monthly earnings to total annual earnings <a class="yt-timestamp" data-t="00:07:57">[00:07:57]</a>.
*   **Month Property**: A title type property representing the month of income <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>.
*   **Income Details**: A relation property linked to the Income Details database, showing earned income <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>.
*   **Earnings Property**: A roll-up property from the Income Details database, calculating and presenting the sum of earnings amounts <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>.
*   **Total Earnings**: A roll-up property from the Total Earnings database, representing the earnings amount with original values <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>. This displays earnings for each month and total earnings for all months combined <a class="yt-timestamp" data-t="00:08:38">[00:08:38]</a>.
*   **Proportion of Earnings**: A formula property that calculates the earnings of each month divided by the total earnings <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>, specified as a percentage in a green bar <a class="yt-timestamp" data-t="00:08:54">[00:08:54]</a>.

## Primary Dashboard Presentation

The primary dashboard presents the summarized income data <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>.

*   **Total Earnings**: Represents the total income earned during the period <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>. It is a linked view of the Total Earnings database, displayed in a list view <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>.
*   **Sources of Income**: Presented using a three-column layout <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a>. Each column is linked to the Income Source database and displayed in a gallery format <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>. This section shows the total actual income and the percentage of each income source relative to the total income <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>.
*   **Frequency**: Derived from the Frequency of Income database and displayed in a gallery layout <a class="yt-timestamp" data-t="00:09:53">[00:09:53]</a>. It shows the total earnings and sources of earnings for each frequency <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>.
*   **Overview Section**: Linked to the Period database and presented in gallery mode <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>. Information is divided into four quarters, with individual months specified for each <a class="yt-timestamp" data-t="00:10:12">[00:10:12]</a>. It displays earnings for each month and their proportion to total earnings <a class="yt-timestamp" data-t="00:10:19">[00:10:19]</a>. Filters are applied to specify respective months for each quarter <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>.

This comprehensive Notion income tracker helps in [[tracking_personal_finances_in_notion | tracking personal finances in Notion]] effectively <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a>.