---
title: Building an income tracker in Notion
videoId: 2MkChIwv0t0
---

From: [[theaccountantguy]] <br/> 

This guide details how to build a minimalistic income tracker in Notion, allowing users to stay on top of their finances <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>. This tracker helps analyze income, track sources, and understand earning frequency.

## Key Sections of the Tracker

The Notion income tracker consists of four main sections <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>:

*   **Total Earnings** Displays the overall earnings for a specified period <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.
*   **Sources of Income** Breaks down earnings by source (e.g., salary, side hustle), showing individual totals and their percentage contribution to overall income <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.
*   **Frequency of Income** Illustrates how often income is earned, including total earnings and the number of sources for each frequency <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.
*   **Overview Section** Presents monthly income, organized into four quarters, along with the percentage of monthly earnings relative to total earnings <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.

## Required Databases

To construct this income tracker, five interconnected databases are necessary <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>:

1.  **Income Details Database** Records the specifics of income earned <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.
2.  **Income Source Database** Categorizes income based on its source <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.
3.  **Frequency of Income Database** Provides a comprehensive view of how often income is received over a period <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.
4.  **Total Earnings Database** Consolidates the total earnings for a given period <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.
5.  **Period Database** Tracks income earned periodically throughout the year <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.

## Database Structure and Properties

### Income Details Database

This database is where raw income data is entered for analysis <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>.

*   **Income Details (Title Property)** The default title property, used to specify different sources of income received throughout the year <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.
*   **Period of Income (Relation Property)** Linked to the Period Database, reflecting monthly incomes per income source <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>.
*   **Income Source (Relation Property)** Linked to the Income Source Database, specifying categories like salary, side hustle, or other income <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>.
*   **Frequency of Income (Relation Property)** Linked to the Frequency of Income Database, indicating how frequently income is earned <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.
*   **Amount (Number Property)** Shows the income amount for a particular period, with a sum calculation at the end <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>.

### Income Source Database

This database analyzes different income sources <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>.

*   **Name (Title Property)** Defines income sources like salary, side hustle, and other income <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.
*   **Earnings Database (Relation Property)** Linked to the Total Earnings Database <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>.
*   **Income Details (Relation Property)** Linked to the Income Details Database <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.
*   **Actual Income (Roll-up Property)** Derived from the Income Details Database, rolling up the 'Amount' property to calculate the sum of income for each source <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.
*   **Total Earnings (Roll-up Property)** Derived from the Earnings Database, showing the original value from the 'Amount' in that database <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.
*   **Frequency (Roll-up Property)** Extracts the 'Frequency of Income' property from the Income Details Database, showing original values <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.
*   **Earnings in Percentage (Formula Property)** Calculates the percentage of earnings from each source relative to the total earnings, formatted as a green percentage bar <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>.

### Frequency of Income Database

This database provides analysis related to the frequency of income earned <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.

*   **Frequency (Title Property)** Indicates how often income is received (e.g., monthly, annual, quarterly, half-yearly, one-time) <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>.
*   **Earnings Associated to Each Frequency of Income (Roll-up Property)** Derived from the related property in the next column, calculating the sum of earnings for each frequency mode <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.
*   **Relation to Income Details Database (Relation Property)** Defines all income sources related to each frequency <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>.
*   **Sources of Income (Formula Property)** Calculates the number of income sources: "one source" if 1, "two sources" if 2, "three sources" if 3, and "no source" if 0 <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>.

### Total Earnings Database

This database relates total earnings across all three income sources and calculates the total associated earnings <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.

*   **Total Earnings (Title Property)** Described by name <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>.
*   **Income Source (Relation Property)** Linked to the Income Source Database, specifying the three income sources <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>.
*   **Total Earnings (Roll-up Property)** Rolls up values from the Income Source Database to calculate the sum of total earnings associated with these sources <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>.

### Period Database

This database calculates periodical income for each month and performs further analysis <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>. It also shows the percentage of monthly earnings to the total annual earnings <a class="yt-timestamp" data-t="00:07:57">[00:07:57]</a>.

*   **Month (Title Property)** Represents the month of income <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>.
*   **Income Details (Relation Property)** Linked to the Income Details Database, showing earned income <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>.
*   **Earnings (Roll-up Property)** Derived from the Income Details Database, calculating the sum of the earnings amount <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>.
*   **Total Earnings (Roll-up Property)** Derived from the Total Earnings Database, representing the earnings amount with original values <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>. This displays earnings for each month and the combined total earnings for all months <a class="yt-timestamp" data-t="00:08:38">[00:08:38]</a>.
*   **Proportion of Earnings to Total Earnings (Formula Property)** Calculates each month's earnings divided by the total earnings, displayed as a green percentage bar <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>.

## Primary Dashboard Presentation

The databases are presented on a primary dashboard for a comprehensive view <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>.

*   **Total Earnings**
    *   Represents the total income earned over the period <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.
    *   This is a linked view to the Total Earnings Database, displayed in a list view <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>.

*   **Sources of Income**
    *   Presented using a three-column layout, created by typing `/three columns` <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a>.
    *   Each column is linked to the Income Source Database and displayed in a gallery format <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>.
    *   Shows the actual income and percentage contribution for each source relative to the total income <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>.

*   **Frequency**
    *   Derived from the Frequency of Income Database <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>.
    *   Displayed in a gallery format <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>.
    *   Shows total earnings and sources of earnings for each frequency <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>.

*   **Overview Section**
    *   Linked to the Period Database <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>.
    *   Presented in gallery mode <a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a>.
    *   Information is divided into four quarters, with individual months specified for each <a class="yt-timestamp" data-t="00:10:12">[00:10:12]</a>.
    *   Displays earnings for each month and the proportion of earnings towards the total earnings <a class="yt-timestamp" data-t="00:10:19">[00:10:19]</a>.
    *   Filters are applied for each quarter to show respective months <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>.

This structured approach allows for effective [[how_to_track_income_and_expenses_using_notion | income and expense tracking using Notion]] and comprehensive [[setting_up_a_personal_finance_tracker_using_notion | personal finance tracking in Notion]].