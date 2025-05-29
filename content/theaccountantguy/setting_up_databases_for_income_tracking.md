---
title: Setting up Databases for Income Tracking
videoId: 2MkChIwv0t0
---

From: [[theaccountantguy]] <br/> 

## Introduction
To stay on top of your finances, you can build an income tracker in Notion <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>. This [[utilizing_notion_databases_for_financial_tracking | Notion income tracker]] will include four main sections:
*   **Total Earnings**: Displays the overall earnings for a specified period <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.
*   **Sources of Income**: Lists income sources like salary, side hustle, and others, showing total earnings for each and its percentage of the total income <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.
*   **Frequency of Income**: Indicates how frequently income is earned, calculating total earnings and the number of sources for each frequency <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.
*   **Overview**: Presents monthly income categorized into four quarters, along with the percentage of monthly earnings relative to total earnings <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.

## Required Databases
To build this minimalistic Notion income tracker, five databases are required <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>:
1.  **Income Details Database**: Stores the specific details of income earned <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.
2.  **Income Source Database**: Tracks income earned for each source <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.
3.  **Frequency of Income Database**: Provides a comprehensive overview of how frequently income is received <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.
4.  **Total Earnings Database**: Reflects the cumulative earnings over a specific period <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.
5.  **Period Database**: Displays periodical income earned throughout the year <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.

## Database Setup Details

### Income Details Database
This database is central for feeding and analyzing income details <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>.
*   **Income Details Property**: A default "Title" property where different sources of income received during the year are specified <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.
*   **Period of Income**: A relation property linked to the `Period Database`, reflecting monthly incomes for each income source <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>. This relation is shown both ways in both databases <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>.
*   **Income Source**: A relation property linked to the `Income Source Database`, specifying the source of income (e.g., salary, side hustle, other) <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>. This relation is also reflected both ways <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>.
*   **Frequency of Income**: A relation property linked to the `Frequency of Income Database`, defining how frequently income is earned <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>. This relation is shown both ways <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>.
*   **Amount**: A number property showing the amount of income earned for a particular period <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>. The sum of the income earned for the period is displayed at the end <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>.

### Income Source Database
This database analyzes different sources of income <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>.
*   **Name Property**: Defines the different sources of income (e.g., salary, side hustle, other income) <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.
*   **Earnings Database**: A relation property linked to the `Total Earnings Database`, associating total earnings with the three income sources <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>.
*   **Income Details Property**: A relation property linked to the `Income Details Database`, relating all incomes <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.
*   **Actual Income**: A roll-up property derived from the `Income Details Database`. It uses the 'Amount' property and calculates its sum value <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.
*   **Total Earnings Property**: A roll-up property derived from the `Earnings Database`. It defines the 'Amount' property from the `Earnings Database` and shows its original value <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.
*   **Frequency Property**: A roll-up property from the `Income Details Database` that extracts the 'Frequency of Income' property and shows its original values <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.
*   **Earnings in Percentage**: A formula property that calculates the percentage of individual source earnings to the total earnings <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>. This is represented with a percent format and a green bar <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.

### Frequency of Income Database
This database provides analysis related to how frequently income is earned <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.
*   **Frequency Column**: A "Title" column indicating frequencies such as monthly, annual, quarterly, half-yearly, or one-time income <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>.
*   **Earnings Associated to Each Frequency of Income**: A roll-up property derived from a related property in the next column. It calculates the sum value of the 'Earnings' amount, representing earnings for all forms of income for each frequency mode <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.
*   **Relation Property**: Linked to the `Income Details Database`, this property defines all income sources related to each frequency <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>. It is automatically generated from the `Income Details Database` <a class="yt-timestamp" data-t="00:06:32">[00:06:32]</a>.
*   **Sources of Income**: A formula property that calculates the number of sources. If the number is 1, it's defined as "one source"; if 2, "two sources"; if 3, "three sources"; and if 0, "no source" <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>.

### Total Earnings Database
This database relates and finds the total earnings associated with all three income sources <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>.
*   **Total Earnings**: A "Title" property described by name <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>.
*   **Income Source**: A relation property established with the `Income Source Database`, specifying the three income sources <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>.
*   **Total Earnings (Roll-up)**: A roll-up property that aggregates values from the income sources and calculates the sum of total earnings associated with them <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>.

### Period Database
This final database calculates periodical income for each month and allows further analysis <a class="yt-timestamp" data-t="00:07:46">[00:07:46]</a>. It also shows the percentage of monthly earnings relative to the total annual earnings <a class="yt-timestamp" data-t="00:07:57">[00:07:57]</a>.
*   **Month Property**: A "Title" property representing the month of income <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>.
*   **Income Details**: A relation property linked to the `Income Details Database`, showing the income earned <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>.
*   **Earnings Property**: A roll-up property derived from the `Income Details Database`, calculating and presenting the sum of the earnings amount <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>.
*   **Total Earnings**: A roll-up property from the `Total Earnings Database`, representing the earnings amount with original values <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>. This shows earnings for each month and the combined total earnings for all months <a class="yt-timestamp" data-t="00:08:38">[00:08:38]</a>.
*   **Proportion of Earnings**: A formula derived by calculating each month's earnings and dividing it by the total earnings <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>. This is displayed as a percentage with a green bar <a class="yt-timestamp" data-t="00:08:54">[00:08:54]</a>.

## Primary Dashboard Presentation
Once all databases are set up, the information is presented on a primary dashboard <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>.
*   **Total Earnings**: This section represents the total income earned during the period <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>. It is a linked view of the `Total Earnings Database` presented in a list view <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>.
*   **Sources of Income**: This is displayed using a three-column layout, created by typing `/three columns` <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a>. These columns are linked to the `Income Source Database` and presented in a gallery format <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>. It shows the actual total income and the percentage of each income source relative to the total income <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>.
*   **Frequency**: Derived from the `Frequency of Income Database`, this section is displayed in a gallery format <a class="yt-timestamp" data-t="00:09:53">[00:09:53]</a>. It presents the total earnings and the sources of earnings for each frequency <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>.
*   **Overview Section**: Linked to the `Period Database` with a gallery mode presentation <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>. Information is divided into four quarters, with individual months specified for each <a class="yt-timestamp" data-t="00:10:12">[00:10:12]</a>. It shows earnings for each month and the proportion of earnings towards the total earnings <a class="yt-timestamp" data-t="00:10:19">[00:10:19]</a>. Filters are applied to specify respective months for each quarter <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>.

This comprehensive setup allows for effective [[tracking_income_and_expenses_effectively | tracking income and expenses effectively]] using Notion databases <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a>.