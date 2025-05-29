---
title: Managing income sources in Notion
videoId: 2MkChIwv0t0
---

From: [[theaccountantguy]] <br/> 

The "accountant guy" outlines a system for building an income tracker within Notion to [[managing_finances_with_notion | manage finances]] and stay on top of earnings <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>. This minimalistic Notion income tracker allows for a comprehensive overview of financial inflows <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.

## Sections of the Income Tracker

The Notion income tracker is structured with four primary sections <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>:

*   **Total Earnings** Displays the aggregate earnings for a specific period <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.
*   **Sources of Income** Itemizes total earnings from individual sources like salary, side hustles, or other income streams, including their percentage contribution to the total <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.
*   **Frequency of Income** Details the regularity of income, calculating total earnings and the number of sources for each frequency <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.
*   **Overview Section** Presents monthly income broken down into four quarters, along with the percentage of monthly earnings relative to total earnings <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.

## Required Databases for the Income Tracker

To build this income tracker, five interconnected databases are necessary <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>:

1.  **Income Details Database** <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>
2.  **Income Source Database** <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>
3.  **Frequency of Income Database** <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>
4.  **Total Earnings Database** <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>
5.  **Period Database** <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>

### 1. Income Details Database

This database serves as the input point for all income-related details <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>. It includes the following properties:

*   **Income Details (Title Property)** Specifies different income sources received throughout the year <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.
*   **Period of Income (Relation Property)** Links to the "Period Database" to reflect monthly incomes for each source <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>. This relationship is shown both ways <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>.
*   **Income Source (Relation Property)** Connects to the "Income Source Database" to categorize the source of income (e.g., salary, side hustle, other income) <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>. This is also a two-way relation <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>.
*   **Frequency of Income (Relation Property)** Relates to the "Frequency of Income Database" to indicate how often income is earned <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>. This property also has a two-way relation <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>.
*   **Amount (Number Property)** Records the amount of income earned for a specific period <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>. The sum of income earned during the period is displayed at the bottom <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>.

### 2. Income Source Database

This database is used to analyze various income sources <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>. Its properties include:

*   **Name (Title Property)** Defines distinct income sources such as salary, side hustle, and other income <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.
*   **Earnings Database (Relation Property)** Links to the "Total Earnings Database" <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>.
*   **Income Details Property (Relation Property)** Connects to the "Income Details Database," linking all associated incomes <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.
*   **Actual Income (Roll-up Property)** Derived from the "Income Details Database," this property rolls up the "Amount" property and calculates its sum <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.
*   **Total Earnings (Roll-up Property)** Derived from the "Earnings Database," this property rolls up the "Amount" from the earnings database, displaying its original value <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.
*   **Frequency (Roll-up Property)** Extracts the "Frequency of Income" property from the "Income Details Database," showing the original values <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.
*   **Earnings in Percentage (Formula Property)** Calculates the percentage of specific earnings relative to the total earnings, displayed with a percent format and a green bar <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>.

### 3. Frequency of Income Database

This database provides analysis on how frequently income is earned <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>. Key properties are:

*   **Frequency (Title Property)** Specifies income frequencies like monthly, annual, quarterly, half-yearly, or one-time income <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>.
*   **Earnings Associated (Roll-up Property)** Derived from the related property in the next column, this property calculates the sum of earnings associated with each frequency <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.
*   **Relation Property** Connects to the "Income Details Database" and automatically defines all income sources related to each frequency <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>.
*   **Sources of Income (Formula Property)** Calculates the number of income sources, displaying "one source," "two sources," "three sources," or "no source" based on the count <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>.

### 4. Total Earnings Database

This database aggregates total earnings from all specified income sources <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>. It contains:

*   **Total Earnings (Title Property)** Named for clarity <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>.
*   **Income Source (Relation Property)** Establishes a relation to the "Income Source Database," linking to the three specified income sources <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>.
*   **Total Earnings (Roll-up Property)** Rolls up values from the "Income Source" property, calculating the sum of total earnings from these sources <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>.

### 5. Period Database

The final database calculates periodical income for each month and provides further analysis <a class="yt-timestamp" data-t="00:07:46">[00:07:46]</a>. It also displays the percentage of each month's earnings to the yearly total <a class="yt-timestamp" data-t="00:07:57">[00:07:57]</a>. Its properties include:

*   **Month (Title Property)** Represents the month of income <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>.
*   **Income Details (Relation Property)** Links to the "Income Details Database," showing earned income <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>.
*   **Earnings (Roll-up Property)** Rolls up the "Amount" property from the "Income Details Database," presented as a sum <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>.
*   **Total Earnings (Roll-up Property)** Rolls up values from the "Total Earnings Database," representing the earnings amount with original values <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>. This property shows monthly earnings and the combined total earnings for all months <a class="yt-timestamp" data-t="00:08:38">[00:08:38]</a>.
*   **Proportion of Earnings (Formula Property)** Calculates the proportion of each month's earnings to the total earnings by dividing monthly earnings by total earnings <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>. This is formatted as a percentage with a green bar <a class="yt-timestamp" data-t="00:08:54">[00:08:54]</a>.

## Primary Dashboard Presentation

The primary dashboard serves as the central display for the income tracker <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>.

*   **Total Earnings**
    *   This section links to the "Total Earnings Database" and is presented in a list view <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>. It shows the overall income earned during the specified period <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.
*   **Sources of Income**
    *   This section uses a three-column layout, created by typing "/three columns" in Notion <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a>. Each column links to the "Income Source Database" and is displayed in a gallery format <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>. It visualizes the actual income and percentage contribution of each source <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>.
*   **Frequency**
    *   Derived from the "Frequency of Income Database," this section is also presented in a gallery layout <a class="yt-timestamp" data-t="00:09:53">[00:09:53]</a>. It shows total earnings and sources of earnings for each frequency <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>.
*   **Overview Section**
    *   This section links to the "Period Database" and is displayed in gallery mode <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>. Information is divided into four quarters, with individual months specified within each <a class="yt-timestamp" data-t="00:10:12">[00:10:12]</a>. It shows earnings for each month and their proportion to the total earnings, with filters applied for respective months in each quarter <a class="yt-timestamp" data-t="00:10:19">[00:10:19]</a>.

This comprehensive setup allows for effective [[tracking_expenses_and_income_in_notion | tracking of income]] and [[setting_up_income_and_expense_tracking_in_notion | setting up income tracking in Notion]] <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a>.