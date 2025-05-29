---
title: Overview and presentation of financial data in Notion
videoId: 2MkChIwv0t0
---

From: [[theaccountantguy]] <br/> 

This article outlines how to build a minimalistic income tracker in [[Notion]] to [[Using Notion for financial planning and debt overview | stay on top of your finances]] <a class="yt-timestamp" data-t="01:01:01">[01:01:01]</a>. The system is designed to provide a clear overview of earnings, sources of income, frequency of income, and monthly breakdowns.

## Income Tracker Structure
The Notion income tracker is organized into four main sections on a primary dashboard <a class="yt-timestamp" data-t="01:06:00">[01:06:00]</a>:
*   **Total Earnings** <a class="yt-timestamp" data-t="01:07:07">[01:07:07]</a>: Shows the total amount of earnings for a specified period <a class="yt-timestamp" data-t="01:09:00">[01:09:00]</a>.
*   **Sources of Income** <a class="yt-timestamp" data-t="01:12:00">[01:12:00]</a>: Displays total earnings for each individual income source (e.g., salary, side hustle) and its percentage of the total income <a class="yt-timestamp" data-t="01:13:00">[01:13:00]</a>.
*   **Frequency of Income** <a class="yt-timestamp" data-t="01:21:00">[01:21:00]</a>: Indicates how frequently income is earned, along with total earnings and the number of sources for each frequency <a class="yt-timestamp" data-t="01:22:00">[01:22:00]</a>.
*   **Overview Section** <a class="yt-timestamp" data-t="01:34:00">[01:34:00]</a>: Presents monthly income segregated into four quarters, including the percentage of monthly earnings relative to total earnings <a class="yt-timestamp" data-t="01:36:00">[01:36:00]</a>.

## Databases for Financial Tracking
To build this income tracker, five interconnected databases are required <a class="yt-timestamp" data-t="01:49:00">[01:49:00]</a>:
1.  **Income Details Database** <a class="yt-timestamp" data-t="01:53:00">[01:53:00]</a>: Stores specific details of income earned <a class="yt-timestamp" data-t="01:54:00">[01:54:00]</a>.
2.  **Income Source Database** <a class="yt-timestamp" data-t="02:02:00">[02:02:00]</a>: Shows income earned relative to each source <a class="yt-timestamp" data-t="02:04:00">[02:04:00]</a>.
3.  **Frequency of Income Database** <a class="yt-timestamp" data-t="02:10:00">[02:10:00]</a>: Provides an overview of how frequently income is earned <a class="yt-timestamp" data-t="02:12:00">[02:12:00]</a>.
4.  **Total Earnings Database** <a class="yt-timestamp" data-t="02:19:00">[02:19:00]</a>: Reflects the grand total of earnings for a given period <a class="yt-timestamp" data-t="02:21:00">[02:21:00]</a>.
5.  **Period Database** <a class="yt-timestamp" data-t="02:27:00">[02:27:00]</a>: Displays periodical income earned throughout the year <a class="yt-timestamp" data-t="02:29:00">[02:29:00]</a>.

### 1. Income Details Database
This database is where the raw data of income is entered, forming the foundation for analysis <a class="yt-timestamp" data-t="02:38:00">[02:38:00]</a>.
*   **`Income Details`** (Title property): Specifies different income sources received during the year <a class="yt-timestamp" data-t="02:46:00">[02:46:00]</a>.
*   **`Period of Income`** (Relation property): Links to the `Period Database` and reflects monthly incomes per income source <a class="yt-timestamp" data-t="02:58:00">[02:58:00]</a>.
*   **`Income Source`** (Relation property): Links to the `Income Source Database`, specifying categories like salary, side hustle, or other income <a class="yt-timestamp" data-t="03:18:00">[03:18:00]</a>.
*   **`Frequency of Income`** (Relation property): Links to the `Frequency of Income Database`, indicating how frequently income is earned <a class="yt-timestamp" data-t="03:31:00">[03:31:00]</a>.
*   **`Amount`** (Number property): Records the income amount for a specific period <a class="yt-timestamp" data-t="03:44:00">[03:44:00]</a>.
*   The sum of income earned for the period is shown at the bottom <a class="yt-timestamp" data-t="03:50:00">[03:50:00]</a>.

### 2. Income Source Database
This database analyzes different sources of income <a class="yt-timestamp" data-t="03:59:00">[03:59:00]</a>.
*   **`Name`** (Title property): Defines income sources such as salary, side hustle, and other income <a class="yt-timestamp" data-t="04:05:00">[04:05:00]</a>.
*   **`Earnings`** (Relation property): Links to the `Total Earnings Database` <a class="yt-timestamp" data-t="04:12:00">[04:12:00]</a>.
*   **`Income Details`** (Relation property): Links to the `Income Details Database`, relating all recorded incomes <a class="yt-timestamp" data-t="04:22:00">[04:22:00]</a>.
*   **`Actual Income`** (Roll-up property): Derives the sum of the `Amount` property from the `Income Details Database` <a class="yt-timestamp" data-t="04:31:00">[04:31:00]</a>.
*   **`Total Earnings`** (Roll-up property): Derived from the `Earnings Database`, showing the total amount from the earnings database <a class="yt-timestamp" data-t="04:51:00">[04:51:00]</a>.
*   **`Frequency`** (Roll-up property): Extracts the `Frequency of Income` property from the `Income Details Database` <a class="yt-timestamp" data-t="05:04:00">[05:04:00]</a>.
*   **`Earnings in Percentage`** (Formula property): Calculates the percentage of specific earnings to the total earnings, formatted as a green percentage bar <a class="yt-timestamp" data-t="05:19:00">[05:19:00]</a>.

### 3. Frequency of Income Database
This database provides analysis related to how frequently income is earned <a class="yt-timestamp" data-t="05:40:00">[05:40:00]</a>.
*   **`Frequency`** (Title property): Indicates how frequently income is earned (e.g., monthly, annual, quarterly, half-yearly, one-time) <a class="yt-timestamp" data-t="05:49:00">[05:49:00]</a>.
*   **`Earnings Associated to each frequency of income`** (Roll-up property): Calculates the sum of earnings associated with each frequency from related properties <a class="yt-timestamp" data-t="06:00:00">[06:00:00]</a>.
*   **`Relation property`** (Relation property): Links to the `Income Details Database`, defining all income sources related to each frequency <a class="yt-timestamp" data-t="06:23:00">[06:23:00]</a>.
*   **`Sources of Income`** (Formula property): Calculates the number of sources, displaying "one source," "two sources," "three sources," or "no source" based on the count <a class="yt-timestamp" data-t="06:37:00">[06:37:00]</a>.

### 4. Total Earnings Database
This database relates and finds the total earnings associated with all income sources <a class="yt-timestamp" data-t="07:07:00">[07:07:00]</a>.
*   **`Total Earnings`** (Title property): Describes the name for the total earnings <a class="yt-timestamp" data-t="07:17:00">[07:17:00]</a>.
*   **`Income Source`** (Relation property): Links to the `Income Source Database` where the three income sources are specified <a class="yt-timestamp" data-t="07:23:00">[07:23:00]</a>.
*   **`Total Earnings`** (Roll-up property): Rolls up values from the `Income Source Database` to calculate the sum of total earnings associated with these sources <a class="yt-timestamp" data-t="07:31:00">[07:31:00]</a>.

### 5. Period Database
This database calculates periodical income for each month and provides further analysis <a class="yt-timestamp" data-t="07:49:00">[07:49:00]</a>. It also shows the percentage of monthly earnings relative to the total annual earnings <a class="yt-timestamp" data-t="07:57:00">[07:57:00]</a>.
*   **`Month`** (Title property): Represents the month of income <a class="yt-timestamp" data-t="08:02:00">[08:02:00]</a>.
*   **`Income Details`** (Relation property): Links to the `Income Details Database`, showing earned income <a class="yt-timestamp" data-t="08:08:00">[08:08:00]</a>.
*   **`Earnings`** (Roll-up property): Calculates the sum of earnings from the `Income Details Database` <a class="yt-timestamp" data-t="08:16:00">[08:16:00]</a>.
*   **`Total Earnings`** (Roll-up property): Rolls up values from the `Total Earnings Database`, showing the original total earnings amount <a class="yt-timestamp" data-t="08:29:00">[08:29:00]</a>.
*   **`Proportion of each month's earning to the total earning`** (Formula property): Divides the earnings of each month by the total earnings, formatted as a green percentage bar <a class="yt-timestamp" data-t="08:44:00">[08:44:00]</a>.

## Primary Dashboard Presentation
The primary dashboard serves as a central hub for visualizing financial data, [[organizing financial data in Notion | presenting information]] from the linked databases <a class="yt-timestamp" data-t="09:02:00">[09:02:00]</a>.

### Total Earnings Display
*   The total earnings are shown as a link to the `Total Earnings Database` <a class="yt-timestamp" data-t="09:12:00">[09:12:00]</a>.
*   Presented in a list view format <a class="yt-timestamp" data-t="09:17:00">[09:17:00]</a>.

### Sources of Income Display
*   Presented using a three-column layout, created by typing `/` followed by `three columns` <a class="yt-timestamp" data-t="09:32:00">[09:32:00]</a>.
*   Each column is linked to the `Income Source Database` <a class="yt-timestamp" data-t="09:41:00">[09:41:00]</a>.
*   Displayed in a gallery format <a class="yt-timestamp" data-t="09:44:00">[09:44:00]</a>.
*   Shows actual income and the percentage of each source relative to total income <a class="yt-timestamp" data-t="09:47:00">[09:47:00]</a>.

### Frequency Display
*   Derived from the `Frequency of Income Database` <a class="yt-timestamp" data-t="09:55:00">[09:55:00]</a>.
*   Presented in a gallery layout <a class="yt-timestamp" data-t="09:57:00">[09:57:00]</a>.
*   Displays total earnings and sources of earnings for each frequency <a class="yt-timestamp" data-t="10:01:00">[10:01:00]</a>.

### Overview Section
*   Linked to the `Period Database` <a class="yt-timestamp" data-t="10:07:00">[10:07:00]</a>.
*   Uses a gallery mode of presentation <a class="yt-timestamp" data-t="10:09:00">[10:09:00]</a>.
*   Information is divided into four quarters, with individual months specified for each <a class="yt-timestamp" data-t="10:12:00">[10:12:00]</a>.
*   Shows earnings for each month and the proportion of earnings towards the total <a class="yt-timestamp" data-t="10:19:00">[10:19:00]</a>.
*   Filters are applied for each quarter to display the respective months <a class="yt-timestamp" data-t="10:24:00">[10:24:00]</a>.