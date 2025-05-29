---
title: Components of an Income Tracker in Notion
videoId: 2MkChIwv0t0
---

From: [[theaccountantguy]] <br/> 
The Notion Income Tracker is a minimalistic system designed to help users stay on top of their finances <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. This tracker provides a comprehensive overview of earnings, their sources, frequency, and a monthly breakdown segregated into quarters <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>. [[tracking_income_and_expenses_in_notion | Tracking income and expenses in Notion]] is facilitated through this setup.

## Main Sections of the Income Tracker Dashboard

The main dashboard of the Notion Income Tracker is organized into four key sections:
*   **Total Earnings** <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>: Displays the cumulative amount of earnings for a specified period <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>.
*   **Sources of Income** <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>: Categorizes earnings by source (e.g., salary, side hustle) and shows the total earnings for each, along with its percentage of the total income <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.
*   **Frequency of Income** <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>: Illustrates how frequently income is earned, calculating the total earnings and the number of sources for each frequency <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.
*   **Overview Section** <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>: Presents monthly income data, divided into four quarters, and shows the percentage of monthly earnings relative to total earnings <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>.

## Databases Required for Setup

To construct this income tracker, five interconnected databases are necessary <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>:
1.  **Income Details Database** <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>
2.  **Income Source Database** <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>
3.  **Frequency of Income Database** <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>
4.  **Total Earnings Database** <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>
5.  **Period Database** <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>

## Database Structure and Properties

Each database plays a specific role in [[creating_a_notion_income_tracker | creating a Notion Income Tracker]] and [[tracking_income_and_expenses_using_notion | tracking income and expenses using Notion]].

### 1. Income Details Database

This database serves as the primary input point for income-related data, providing analysis related to recorded income <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>. [[Setting Up Income Details in Notion | Setting up Income Details in Notion]] is crucial here.

*   **`Income Details`** (Title property): Specifies different sources of income received throughout the year <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.
*   **`Period of Income`** (Relation property): Links to the `Period Database`, reflecting monthly incomes per income source <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>. This relationship is shown both ways in both databases <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>.
*   **`Income Source`** (Relation property): Connects to the `Income Source Database`, defining the specific source of income <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>. This relationship is also reflected both ways <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>.
*   **`Frequency of Income`** (Relation property): Links to the `Frequency of Income Database`, specifying how frequently income is earned <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>. This relationship is shown both ways <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>.
*   **`Amount`** (Number property): Records the income amount earned for a particular period <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>. The sum of income earned during the period is displayed at the end <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>.

### 2. Income Source Database

This database analyzes different income sources <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>.

*   **`Name`** (Title property): Defines the different sources of income such as "salary," "side hustle," and "other income" <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.
*   **`Earnings Database`** (Relation property): Linked to the `Total Earnings Database` <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>.
*   **`Income Details`** (Relation property): Connected to the `Income Details Database` <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.
*   **`Actual Income`** (Roll-up property): Derived from the `Income Details Database`, rolling up the `Amount` property and calculating its sum <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.
*   **`Total Earnings`** (Roll-up property): Derived from the `Earnings Database`, pulling the `Amount` property and showing its original value <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.
*   **`Frequency`** (Roll-up property): Extracts the `Frequency of Income` property from the `Income Details Database`, showing original values <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.
*   **`Earnings in Percentage`** (Formula property): Calculates the percentage of earnings relative to the total earnings <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>, displayed as a percent format with a green bar <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.

### 3. Frequency of Income Database

This database provides analysis related to how frequently income is earned <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.

*   **`Frequency`** (Title property): Indicates how often income is earned, e.g., "monthly income," "annual income," "quarterly income," "half-yearly income," or "one-time income" <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>.
*   **`Earnings Associated`** (Roll-up property): Derived from a related property, it calculates the sum value of earnings amount associated with each frequency mode <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.
*   **`Relation property`** (Relation property): Links to the `Income Details Database`, defining all sources of income related to each frequency, automatically generated <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>.
*   **`Sources of Income`** (Formula property): Calculates the number of income sources using conditional logic: "one source" if 1, "two sources" if 2, "three sources" if 3, and "no source" if 0 <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>.

### 4. Total Earnings Database

This database aggregates total earnings from all three income sources <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.

*   **`Total Earnings`** (Title property): Describes the name of the total earnings <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>.
*   **`Income Source`** (Relation property): Established with the `Income Source Database`, specifying the three income sources <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>.
*   **`Total Earnings`** (Roll-up property): Rolls up values from the `Income Sources`, calculating the sum of total earnings associated with these sources <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>.

### 5. Period Database

This database is used to calculate periodical income for each month and perform further analysis <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>. It also shows the percentage of monthly earnings to the total earnings for the year <a class="yt-timestamp" data-t="00:07:57">[00:07:57]</a>.

*   **`Month`** (Title property): Represents the specific month of income <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>.
*   **`Income Details`** (Relation property): Linked to the `Income Details Database`, showing the income earned <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>.
*   **`Earnings`** (Roll-up property): Rolled up from the `Income Details Database`, calculating the sum of the earnings amount <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>.
*   **`Total Earnings`** (Roll-up property): Rolled up from the `Total Earnings Database`, representing the earnings amount with original values <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>.
*   **`Proportion`** (Formula property): Calculates the proportion of each month's earnings to the total earnings by dividing monthly earnings by total earnings <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>. This is formatted as a percentage with a green bar <a class="yt-timestamp" data-t="00:08:54">[00:08:54]</a>.

## Primary Dashboard Presentation

The primary dashboard provides a visual [[Presentation of Income Tracking Data in Notion | presentation of income tracking data in Notion]] using linked databases.

*   **Total Earnings**: Presented as a linked view of the `Total Earnings Database` in a list view <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.
*   **Sources of Income**: Displayed using a three-column layout in a gallery format, linked to the `Income Source Database` <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a>. It shows actual income and the percentage of each source to the total income <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>.
*   **Frequency**: Derived from the `Frequency of Income Database` and presented in a gallery layout <a class="yt-timestamp" data-t="00:09:53">[00:09:53]</a>, showing total earnings and sources of earnings for each frequency <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>.
*   **Overview Section**: Linked to the `Period Database` with a gallery mode presentation <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>. This section divides information into four quarters, specifying individual months for each <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>. Filters are applied for each quarter to show respective months <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>. It displays earnings for each month and the proportion of earnings to total earnings <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>.

This structured setup allows for [[setting_up_a_personal_finance_tracker_in_notion | setting up a personal finance tracker in Notion]] and [[tracking_income_and_expenses in Notion | tracking income and expenses in Notion]] efficiently.