---
title: Using databases for financial tracking in Notion
videoId: 2MkChIwv0t0
---

From: [[theaccountantguy]] <br/> 

A minimalistic income tracker can be built in Notion to help users stay on top of their finances <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>. This [[setting_up_a_finance_tracker_in_notion | Notion income tracker]] is designed to provide a comprehensive overview of earnings.

## Structure of the Income Tracker

The Notion income tracker is divided into four main sections <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>:

*   **Total Earnings**
    *   Displays the total amount of earnings for a specified period <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.
*   **Sources of Income**
    *   Categorizes income by sources like salary, side hustle, and other sources <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.
    *   Shows the total earnings for each individual income source and its percentage of the total income <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.
*   **Frequency of Income**
    *   Indicates how frequently income is earned <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.
    *   Calculates the total earnings and the number of sources for each frequency of income <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>.
*   **Overview Section**
    *   Presents monthly income, segregated into four quarters <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.
    *   Includes the percentage of monthly earnings relative to the total earnings <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>.

## Essential Databases for the Tracker

To build this tracker, five distinct [[setting_up_a_database_in_notion | Notion databases]] are required <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>:

1.  **Income Details Database**: Stores specifics of income earned <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.
2.  **Income Source Database**: Organizes income based on its source <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.
3.  **Frequency of Income Database**: Provides an overview of how frequently income is earned <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.
4.  **Total Earnings Database**: Reflects the aggregated earnings over a given period <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.
5.  **Period Database**: Shows periodical income earned throughout a year <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.

### 1. Income Details Database

This database serves as the primary input for income data, allowing for subsequent analysis <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>.

*   **Income Details Property**: A title property where different sources of income received during the year are specified <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.
*   **Period of Income Property**: A relation property linked to the `Period Database`, reflecting monthly incomes per income source <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>.
*   **Income Source Property**: A relation property connected to the `Income Source Database`, specifying the income source (e.g., salary, side hustle) <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>.
*   **Frequency of Income Property**: A relation property linked to the `Frequency of Income Database`, indicating how frequently income is earned <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.
*   **Amount Property**: Shows the income amount earned for a specific period <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>.
*   **Sum of Income Earned**: Displays the sum of income earned during the period <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>.

### 2. Income Source Database

This database analyzes different income sources <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>.

*   **Name Property**: Defines income sources such as salary, side hustle, and other income <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.
*   **Earnings Database Property**: A relation property linked to the `Total Earnings Database` <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>.
*   **Income Details Property**: A relation property linked to the `Income Details Database` <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.
*   **Actual Income Property**: A roll-up property derived from the `Income Details Database`, calculating the sum of the "Amount" property <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.
*   **Total Earnings Property**: A roll-up property from the `Earnings Database`, showing the original value of the total earnings <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.
*   **Frequency Property**: A roll-up property from the `Income Details Database`, extracting and displaying the original values of the "Frequency of income" property <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.
*   **Earnings in Percentage Property**: A formula property that calculates the percentage of specific earnings relative to the total earnings, formatted as a green percent bar <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>.

### 3. Frequency of Income Database

This database provides analysis related to the frequency of income <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.

*   **Frequency Column**: A title column indicating how frequently income is earned (e.g., monthly, annual, quarterly, half-yearly, one-time) <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>.
*   **Earnings Associated Property**: A roll-up property derived from the related `Income Details Database`, calculating the sum of earnings for each frequency <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.
*   **Relation Property**: Linked to the `Income Details Database`, this property automatically defines all income sources related to each frequency <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>.
*   **Sources of Income Property**: A formula property that categorizes the number of sources (e.g., "one source", "two sources", "no source") <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>.

### 4. Total Earnings Database

This database links total earnings to all three income sources and calculates associated earnings <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.

*   **Total Earnings Property**: A title property <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>.
*   **Income Source Property**: A relation property established with the `Income Source Database`, specifying the three income sources <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>.
*   **Total Earnings (Roll-up) Property**: A roll-up property that aggregates values from the income sources and calculates the sum of total earnings <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>.

### 5. Period Database

This final database calculates periodical income for each month and provides further analysis <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>. It also shows the percentage of monthly earnings relative to the year's total earnings <a class="yt-timestamp" data-t="00:07:57">[00:07:57]</a>.

*   **Month Property**: A title-type property representing the month of income <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>.
*   **Income Details Property**: A relation to the `Income Details Database`, showing earned income <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>.
*   **Earnings Property**: A roll-up property from the `Income Details Database`, calculating the sum of the earnings amount <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>.
*   **Total Earnings Property**: A roll-up property from the `Total Earnings Database`, showing the original values of earnings <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>. This displays monthly earnings and the combined total earnings <a class="yt-timestamp" data-t="00:08:38">[00:08:38]</a>.
*   **Proportion of Earnings Property**: A formula property that calculates the percentage of each month's earning to the total earning <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>. It is formatted as a green percent bar <a class="yt-timestamp" data-t="00:08:54">[00:08:54]</a>.

## Primary Dashboard Presentation

The primary dashboard links to the databases and presents the financial data in an organized manner <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>.

*   **Total Earnings Section**:
    *   A linked view of the `Total Earnings Database`, displayed in a list view <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>.
    *   Represents the total income earned during the period <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.
*   **Sources of Income Section**:
    *   Presented in a three-column layout, created by typing `/` followed by "three columns" <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a>.
    *   Linked to the `Income Source Database` with a gallery format <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>.
    *   Shows the total actual income and the percentage of each income source relative to the total income <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>.
*   **Frequency Section**:
    *   Derived from the `Frequency of Income Database` and displayed in a gallery layout <a class="yt-timestamp" data-t="00:09:53">[00:09:53]</a>.
    *   Displays the total earnings and sources of earnings for each frequency <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>.
*   **Overview Section**:
    *   Linked to the `Period Database` and presented in a gallery mode <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>.
    *   Information is divided into four quarters, with individual months specified for each <a class="yt-timestamp" data-t="00:10:12">[00:10:12]</a>.
    *   Shows earnings for each month and their proportion to the total earnings <a class="yt-timestamp" data-t="00:10:19">[00:10:19]</a>.
    *   Filters are applied for each quarter to display the respective months <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>.

This structured approach to [[organizing_financial_data_in_notion | organizing financial data in Notion]] using multiple interlinked databases enables effective [[using_notion_for_financial_tracking | financial tracking in Notion]] by breaking down income into manageable and analyzable components. This allows for detailed [[using_notion_databases_for_income_details | income details tracking]] and insightful [[creating_a_database_in_notion_for_calculations | calculations directly within Notion]].