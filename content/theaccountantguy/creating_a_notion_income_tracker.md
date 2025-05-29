---
title: Creating a Notion Income Tracker
videoId: 2MkChIwv0t0
---

From: [[theaccountantguy]] <br/> 

This article details how to build a Notion income tracker to help stay on top of personal finances <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.

## Components of the Notion Income Tracker

The Notion income tracker is designed with four main sections <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>:
*   **Total Earnings**: Displays the total amount earned for a specific period <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.
*   **Sources of Income**: Shows total earnings for individual income sources (e.g., salary, side hustle) and their percentage of the total income <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.
*   **Frequency of Income**: Indicates how frequently income is earned, along with the total earnings and number of sources for each frequency <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.
*   **Overview Section**: Presents monthly income segregated into four quarters, including the percentage of monthly earnings relative to total earnings <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.

## Required Databases

To build this Notion income tracker, five databases are necessary <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>:
1.  **[[setting_up_income_details_in_notion | Income Details database]]**: Used to record the specifics of income earned <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.
2.  **Income Source database**: Tracks income earned by each source <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.
3.  **Frequency of Income database**: Provides an overview of how often income is earned over a period <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.
4.  **Total Earnings database**: Reflects the cumulative earnings within a specified period <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.
5.  **Period database**: Shows periodical income earned throughout a year <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.

## Database Construction

### Income Details Database

This database is where the specific details of income are input and analyzed <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>.

*   **Income Details Property**: A title property, which is the default, used to specify different income sources received during the year <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.
*   **Period of Income**: A relation property linked to the Period database, reflecting monthly incomes per source <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>. This relationship is shown both ways <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>.
*   **Income Source**: A relation property linked to the Income Source database, specifying the three predefined income sources (salary, side hustle, other) <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>. This is reflected both ways <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>.
*   **Frequency of Income**: A relation property linked to the Frequency of Income database, indicating how frequently income is earned <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>. This is shown both ways <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>.
*   **Amount**: A number property showing the income earned for a specific period <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>. The sum of income earned during the period is displayed at the bottom <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>.

### Income Source Database

This database analyzes different income sources <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>.

*   **Name Property**: Defines different income sources such as salary, side hustle, and other income <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.
*   **Earnings Database**: A relation property linked to the Total Earnings database, added to the three specified income sources <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>.
*   **Income Details Property**: A relation property linked to the [[setting_up_income_details_in_notion | Income Details database]], relating all incomes <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.
*   **Actual Income**: A roll-up property derived from the [[setting_up_income_details_in_notion | Income Details database]], specifically the `Amount` property, calculating its sum value <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.
*   **Total Earnings Property**: A roll-up property derived from the `Earnings` database, defining and calculating the amount, showing the original value <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.
*   **Frequency Property**: A roll-up property from the [[setting_up_income_details_in_notion | Income Details database]], extracting the `Frequency of Income` property and showing original values <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.
*   **Earnings in Percentage**: A formula property that calculates the percentage of earnings relative to total earnings, displayed as a green bar percentage <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>.

### Frequency of Income Database

This database contains analysis related to how frequently income is earned <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.

*   **Frequency Column**: A title column indicating income frequency (e.g., monthly, annual, quarterly, half-yearly, one-time) <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>.
*   **Earnings Associated to Each Frequency of Income**: A roll-up property derived from a related property in the next column, calculating the sum value of the `Earnings amount` property <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>. It represents earnings related to all forms of income for each frequency mode <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>.
*   **Relation Property**: A relation property linked to the [[setting_up_income_details_in_notion | Income Details database]], defining all income sources related to each frequency <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>. This is automatically generated from the earlier database <a class="yt-timestamp" data-t="00:06:32">[00:06:32]</a>.
*   **Sources of Income**: A formula property that calculates the number of sources. If the number is 1, it's defined as "one source"; if 2, "two sources"; if 3, "three sources"; and if 0, "no source" <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>.

### Total Earnings Database

This database relates total earnings to all three income sources <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.

*   **Total Earnings**: A title property <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>.
*   **Income Source**: A relation property established with the Income Source database, where the three income sources are specified <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>.
*   **Total Earnings (Roll-up)**: A roll-up property that extracts values from the income sources and calculates their sum to determine the total earnings <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>.

### Period Database

This final database calculates periodical income for each month and conducts further analysis, including the percentage of monthly earnings to total annual earnings <a class="yt-timestamp" data-t="00:07:46">[00:07:46]</a>.

*   **Month Property**: A title type property representing the month of income <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>.
*   **Income Details**: A relation property linked to the [[setting_up_income_details_in_notion | Income Details database]], showing earned income <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>.
*   **Earnings Property**: A roll-up property from the [[setting_up_income_details_in_notion | Income Details database]], calculating and presenting the sum of the `Earnings amount` <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>.
*   **Total Earnings**: A roll-up property from the Total Earnings database, representing the `Earnings amount` with original values <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>. This shows earnings for each month and total earnings combined <a class="yt-timestamp" data-t="00:08:38">[00:08:38]</a>.
*   **Proportion of Earnings**: A formula property that calculates the earnings of each month divided by the total earnings <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>. This is specified in percentage format and given in a green bar <a class="yt-timestamp" data-t="00:08:54">[00:08:54]</a>.

## Primary Dashboard Presentation

The primary dashboard serves as the main display for the tracked income data <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>.

### Total Earnings

This section presents the total income earned during the period <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>. It is a linked view of the Total Earnings database, displayed in a list view <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>.

### Sources of Income

This section uses a three-column layout, created by typing `/three columns` <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a>. The columns are linked to the Income Source database and displayed in a gallery format <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>. It shows the actual total income and the percentage of each income source relative to the total income <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>.

### Frequency

This section is derived from the Frequency of Income database, presented in a gallery layout <a class="yt-timestamp" data-t="00:09:53">[00:09:53]</a>. It displays the total earnings and sources of earnings for each frequency <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>.

### Overview Section

Linked to the Period database and displayed in gallery mode, this section divides information into four quarters <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>. Individual months are specified for each quarter <a class="yt-timestamp" data-t="00:10:12">[00:10:12]</a>. It shows monthly earnings and their proportion to total earnings <a class="yt-timestamp" data-t="00:10:19">[00:10:19]</a>. Filters are applied for each quarter to display the respective months <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>.

This concludes the setup of the Notion income tracker <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>.