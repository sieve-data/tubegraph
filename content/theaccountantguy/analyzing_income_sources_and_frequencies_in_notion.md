---
title: Analyzing Income Sources and Frequencies in Notion
videoId: 2MkChIwv0t0
---

From: [[theaccountantguy]] <br/> 

This guide details how to [[building_a_notion_income_tracker | build an income tracker in Notion]] to stay on top of personal finances, specifically focusing on analyzing income sources and their frequencies <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.

## Sections of the Notion Income Tracker

The Notion income tracker is designed with four main sections <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>:

1.  **Total Earnings** <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>: Displays the total amount earned for a specific period <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>.
2.  **Sources of Income** <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>: Categorizes earnings by sources like salary, side hustle, and other income, showing total earnings for each and their percentage of the total income <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.
3.  **Frequency of Income** <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>: Indicates how frequently income is earned, calculating total earnings and the number of sources for each frequency <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.
4.  **Overview Section** <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>: Presents monthly income segregated into four quarters, along with the percentage of monthly earnings relative to the total earnings <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>.

## Required Databases for Income Tracking

To build this minimalistic Notion income tracker, five distinct databases are necessary <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>:

1.  **Income Details Database** <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>: Stores the specifics of income earned <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>.
2.  **Income Source Database** <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>: Tracks income earned relative to each source <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.
3.  **Frequency of Income Database** <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>: Provides an overview of how frequently income is earned over a period <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>.
4.  **Total Earnings Database** <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>: Reflects the total income earned during a specific period <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>.
5.  **Period Database** <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>: Shows periodical income earned throughout a year <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.

### Setting Up Notion Databases for Income Tracking

This section describes how to [[setting_up_notion_databases_for_income_tracking | set up Notion databases for income tracking]].

#### Income Details Database

This database serves as the foundation for feeding income details and generating related analysis <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>.

*   **Income Details (Title Property)** <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>: A default title property where different sources of income received during the year are specified <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.
*   **Period of Income (Relation Property)** <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>: Establishes a two-way relationship with the Period Database, reflecting monthly incomes per source <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.
*   **Income Source (Relation Property)** <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>: Linked to the Income Source Database (two-way relation), specifying sources like salary, side hustle, and other income <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.
*   **Frequency of Income (Relation Property)** <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>: Connected to the Frequency of Income Database (two-way relation), indicating how often income is earned <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>.*   **Amount (Number Property)** <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>: Shows the monetary value of income earned for a specific period <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>. The sum of income earned during the period is also displayed <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>.

#### Income Source Database

This database is used to analyze different sources of income <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>.

*   **Name (Title Property)** <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>: Defines the different income sources, such as salary, side hustle, and other income <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>.
*   **Earnings (Relation Property)** <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>: Relates to the Total Earnings Database, linking to the three specified income sources <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>.
*   **Income Details (Relation Property)** <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>: Connects to the Income Details Database, linking all related incomes <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.
*   **Actual Income (Roll-up Property)** <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>: Derived from the Income Details Database, rolling up the "Amount" property and calculating its sum <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>.
*   **Total Earnings (Roll-up Property)** <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>: A roll-up property derived from the Earnings Database, showing the original value of the total earnings <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>.
*   **Frequency (Roll-up Property)** <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>: A roll-up property from the Income Details Database, extracting the "Frequency of Income" property and displaying its original values <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
*   **Earnings in Percentage (Formula Property)** <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>: Calculates the percentage of specific earnings relative to total earnings, formatted as a percentage with a green bar <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>.

#### Frequency of Income Database

This database provides analysis related to how frequently income is earned <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.

*   **Frequency (Title Property)** <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>: Indicates the frequency of income, such as monthly, annual, quarterly, half-yearly, or one-time income <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>.
*   **Earnings Associated (Roll-up Property)** <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>: A roll-up property derived from the related property in the next column, calculating the sum of the earnings amount for each frequency mode <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>.
*   **Relation Property (Relation Property)** <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>: Related to the Income Details Database, defining all income sources linked to each frequency, automatically generated from the Income Details Database <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>.
*   **Sources of Income (Formula Property)** <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>: Calculates the number of sources based on a formula: "one source," "two sources," "three sources," or "no source" if the number is zero <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>.

#### Total Earnings Database

This database relates total earnings to all three income sources and calculates the associated earnings <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.

*   **Total Earnings (Title Property)** <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>: The title property defining the total earnings <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>.
*   **Income Source (Relation Property)** <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>: A relation property established with the Income Source Database, specifying the three income sources <a class="yt-timestamp" data-t="00:07:25">[00:07:25]</a>.
*   **Total Earnings (Roll-up Property)** <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>: A roll-up property that aggregates values from the income sources and calculates the sum of total earnings associated with them <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>.

#### Period Database

This database calculates periodical income for each month and provides further analysis <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>. It also shows the percentage of monthly earnings relative to the total annual earnings <a class="yt-timestamp" data-t="00:07:57">[00:07:57]</a>.

*   **Month (Title Property)** <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>: A title type property representing the month of income <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>.
*   **Income Details (Relation Property)** <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>: Related to the Income Details Database, showing the income earned <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>.
*   **Earnings (Roll-up Property)** <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>: Rolled up from the Income Details Database, calculating and presenting the sum of the earnings amount <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>.
*   **Total Earnings (Roll-up Property)** <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>: Rolled up from the Total Earnings Database, representing the earnings amount with original values, showing monthly earnings and combined total earnings <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>.
*   **Proportion of Earnings (Formula Property)** <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>: Derived from a formula that calculates the earnings of each month divided by the total earnings <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>. This is specified as a percentage and displayed with a green bar <a class="yt-timestamp" data-t="00:08:54">[00:08:54]</a>.

## Dashboard Presentation

The primary dashboard consolidates the information from all databases for clear presentation <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>.

*   **Total Earnings Display** <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>: Represents the total income earned during the period <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>. This is a linked view of the Total Earnings Database, displayed in a list view <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>.
*   **Sources of Income Display** <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>: Utilizes a three-column layout, created by typing `/three columns` <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a>. Each column links to the Income Source Database and is presented in a gallery format <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>. This section shows the actual income and percentage of each source relative to total income <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>.
*   **Frequency Display** <a class="yt-timestamp" data-t="00:09:53">[00:09:53]</a>: Derived from the Frequency of Income Database and presented in a gallery format <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>. It shows total earnings and sources of earnings for each frequency <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>.
*   **Overview Section** <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a>: Linked to the Period Database and displayed in gallery mode <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>. Information is divided into four quarters, with individual months specified for each <a class="yt-timestamp" data-t="00:10:12">[00:10:12]</a>. It shows earnings per month and their proportion to total earnings <a class="yt-timestamp" data-t="00:10:19">[00:10:19]</a>. Filters are applied to specify respective months for each quarter <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>.

This comprehensive Notion income tracker helps in [[tracking_personal_finances_in_notion | tracking personal finances in Notion]] effectively <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a>.