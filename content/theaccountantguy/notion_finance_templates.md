---
title: Notion Finance Templates
videoId: 2MkChIwv0t0
---

From: [[theaccountantguy]] <br/> 

This guide details how to build a minimalistic income tracker in [[notion_application | Notion]] to help users stay on top of their [[finance_management_using_notion | finances]] <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>. This [[notion_template_and_database_integration | Notion template and database integration]] focuses specifically on tracking income <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.

## Key Sections of the Income Tracker <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>
The Notion Income Tracker is organized into four main sections:
*   **Total Earnings**: Displays the total amount of earnings for a specified period <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.
*   **Sources of Income**: Lists income sources like salary, side hustle, and other sources, showing total earnings for each and their percentage of the total income <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.
*   **Frequency of Income**: Illustrates how frequently income is earned, calculating total earnings and the number of sources for each frequency type <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.
*   **Overview Section**: Provides monthly income segregated into four quarters, along with the percentage of monthly earnings relative to total earnings <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.

## Required Databases <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>
To construct this income tracker, five interconnected databases are necessary <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>:
1.  **Income Details Database**: Stores specifics about income earned <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.
2.  **Income Source Database**: Tracks income per source <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.
3.  **Frequency of Income Database**: Offers a complete overview of income earning frequency <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.
4.  **Total Earnings Database**: Reflects the total earnings over a period <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.
5.  **Period Database**: Shows periodical income earned throughout a year <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.

## Building the Databases <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>
The process of [[creating_templates_and_databases_in_notion | creating templates and databases in Notion]] for this tracker involves setting up specific properties and relationships within each database.

### 1. Income Details Database <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>
This database is where income-related details are input for analysis <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>.
*   **Income Details (Title Property)**: Default property to specify different sources of income received during the year <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.
*   **Period of Income (Relation Property)**: Establishes a relation with the `Period Database`, showing monthly incomes for each source <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>.
*   **Income Source (Relation Property)**: Relates to the `Income Source Database`, defining specific sources like salary, side hustle, etc. <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>.
*   **Frequency of Income (Relation Property)**: Linked to the `Frequency of Income Database`, specifying how frequently income is earned <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.
*   **Amount (Number Property)**: Shows the income amount earned for a particular period, with a sum calculation at the end <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>.

### 2. Income Source Database <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>
This database analyzes different income sources <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>.
*   **Name (Title Property)**: Defines income sources such as salary, side hustle, and other income <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.
*   **Earnings Database (Relation Property)**: Related to the `Total Earnings Database` <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>.
*   **Income Details (Relation Property)**: Linked to the `Income Details Database` <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.
*   **Actual Income (Roll-up Property)**: Derived from the `Income Details Database` (using the `Amount` property), calculating the sum value <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.
*   **Total Earnings (Roll-up Property)**: Derived from the `Earnings Database`, showing the original total earnings amount <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.
*   **Frequency (Roll-up Property)**: Extracts the `Frequency of income` property from the `Income Details Database`, showing original values <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.
*   **Earnings in Percentage (Formula Property)**: Calculates the percentage of earnings from a specific source relative to the total earnings, displayed as a green percent bar <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>.

### 3. Frequency of Income Database <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>
This database provides analysis on how frequently income is earned <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>.
*   **Frequency (Title Property)**: Indicates income frequency (e.g., monthly, annual, quarterly, half-yearly, one-time) <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>.
*   **Earnings Associated to Each Frequency of Income (Roll-up Property)**: Derived from the related `Income Details Database` (using the `Amount` property), calculating the sum of earnings for each frequency <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.
*   **Relation Property (Relation Property)**: Linked to the `Income Details Database`, automatically populating all income sources related to each frequency <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>.
*   **Sources of Income (Formula Property)**: Calculates the number of income sources, displayed as "one source," "two sources," "three sources," or "no source" <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>.

### 4. Total Earnings Database <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>
This database consolidates total earnings across all income sources <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.
*   **Total Earnings (Title Property)**: The primary name property <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>.
*   **Income Source (Relation Property)**: Established with the `Income Source Database`, specifying the three income sources <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>.
*   **Total Earnings (Roll-up Property)**: Rolls up values from the `Income Source Database` to calculate the sum of total earnings associated with these sources <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>.

### 5. Period Database <a class="yt-timestamp" data-t="00:07:46">[00:07:46]</a>
This database calculates periodical income monthly and performs further analysis <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>. It also shows the percentage of monthly earnings relative to the total annual earnings <a class="yt-timestamp" data-t="00:07:57">[00:07:57]</a>.
*   **Month (Title Property)**: Represents the month of income <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>.
*   **Income Details (Relation Property)**: Linked to the `Income Details Database`, showing earned income <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>.
*   **Earnings (Roll-up Property)**: Rolled up from the `Income Details Database` (using the `Amount` property), presented as a sum <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>.
*   **Total Earnings (Roll-up Property)**: Rolled up from the `Total Earnings Database` (using the `Earnings Amount` property), showing original values <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>. This displays earnings for each month and the combined total earnings <a class="yt-timestamp" data-t="00:08:38">[00:08:38]</a>.
*   **Proportion of Each Month's Earning (Formula Property)**: Calculates monthly earnings divided by total earnings, displayed as a green percent bar <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>.

## Primary Dashboard Presentation <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>
The final dashboard consolidates all the information from the databases.

### Total Earnings Display <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>
*   This section links directly to the `Total Earnings Database` and is presented in a `List View` <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>. It shows the total income earned during the period <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.

### Sources of Income Display <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>
*   Presented using a three-column layout (created by typing `/three columns`) <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a>.
*   Each column links to the `Income Source Database` and uses a `Gallery format` <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>.
*   This displays the actual income and percentage for each income source relative to the total income <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>.

### Frequency Display <a class="yt-timestamp" data-t="00:09:53">[00:09:53]</a>
*   Derived from the `Frequency of Income Database` <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>.
*   Presented in a `Gallery format` <a class="yt-timestamp" data-t="09:57">[00:09:57]</a>.
*   Shows total earnings and sources of earnings for each frequency <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>.

### Overview Section <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a>
*   Linked to the `Period Database` and presented in `Gallery mode` <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>.
*   Information is divided into four quarters, with individual months specified for each <a class="yt-timestamp" data-t="00:10:12">[00:10:12]</a>.
*   Displays earnings for each month and their proportion to total earnings <a class="yt-timestamp" data-t="00:10:19">[00:10:19]</a>.
*   Filters are applied to each quarter to display the respective months <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>.

This comprehensive [[notion_template_and_database_integration | Notion template and database integration]] provides a detailed income tracker, leveraging [[notion_features_for_budgeting | Notion features for budgeting]] to keep [[finance_management_using_notion | finances]] organized <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.