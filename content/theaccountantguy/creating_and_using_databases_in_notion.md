---
title: Creating and using databases in Notion
videoId: 2MkChIwv0t0
---

From: [[theaccountantguy]] <br/> 

This article outlines how to build a minimalistic income tracker in Notion to help stay on top of personal finances <a class="yt-timestamp" data-t="00:57:00">[00:57:00]</a>.

## Income Tracker Sections

The Notion income tracker consists of four main sections <a class="yt-timestamp" data-t="01:03:00">[01:03:00]</a>:
*   **Total Earnings** <a class="yt-timestamp" data-t="01:07:00">[01:07:00]</a>: Displays the total earnings for a specified period <a class="yt-timestamp" data-t="01:07:00">[01:07:00]</a>.
*   **Sources of Income** <a class="yt-timestamp" data-t="01:12:00">[01:12:00]</a>: Categorizes income by source (e.g., salary, side hustle) and shows total earnings and percentage of total income for each source <a class="yt-timestamp" data-t="01:12:00">[01:12:00]</a>.
*   **Frequency of Income** <a class="yt-timestamp" data-t="01:21:00">[01:21:00]</a>: Indicates how frequently income is earned, calculating total earnings and the number of sources for each frequency <a class="yt-timestamp" data-t="01:21:00">[01:21:00]</a>.
*   **Overview Section** <a class="yt-timestamp" data-t="01:34:00">[01:34:00]</a>: Presents monthly income segregated into four quarters, along with the percentage of monthly earnings relative to total earnings <a class="yt-timestamp" data-t="01:34:00">[01:34:00]</a>.

## Required Databases

To build this income tracker, five interconnected databases are necessary <a class="yt-timestamp" data-t="01:47:00">[01:47:00]</a>:
1.  **Income Details Database**: Stores specifics of income earned <a class="yt-timestamp" data-t="01:53:00">[01:53:00]</a>.
2.  **Income Source Database**: Tracks income earned per source <a class="yt-timestamp" data-t="02:02:00">[02:02:00]</a>.
3.  **Frequency of Income Database**: Provides an overview of how frequently income is earned during a period <a class="yt-timestamp" data-t="02:10:00">[02:10:00]</a>.
4.  **Total Earnings Database**: Reflects the total earnings over a given period <a class="yt-timestamp" data-t="02:19:00">[02:19:00]</a>.
5.  **Period Database**: Shows periodical income earned throughout a year <a class="yt-timestamp" data-t="02:27:00">[02:27:00]</a>.

## [[setting_up_databases_and_relationships_in_notion | Setting up Databases and Relationships in Notion]]

### 1. Income Details Database
This database is used to input details related to income for analysis <a class="yt-timestamp" data-t="02:38:00">[02:38:00]</a>.
*   **Income Details** (Title property): Specifies the different sources of income received during the year <a class="yt-timestamp" data-t="02:44:00">[02:44:00]</a>.
*   **Period of Income** (Relation property): Linked with the "Period database" to reflect monthly incomes for each income source <a class="yt-timestamp" data-t="02:58:00">[02:58:00]</a>. This relation is shown both ways <a class="yt-timestamp" data-t="03:05:00">[03:05:00]</a>.
*   **Income Source** (Relation property): Linked to the "Income Source database" to specify the source of income (e.g., salary, side hustle, other) <a class="yt-timestamp" data-t="03:18:00">[03:18:00]</a>. This relation is also reflected both ways <a class="yt-timestamp" data-t="03:24:00">[03:24:00]</a>.
*   **Frequency of Income** (Relation property): Linked to the "Frequency of Income database" to indicate how frequently income is earned <a class="yt-timestamp" data-t="03:31:00">[03:31:00]</a>. This is shown both ways <a class="yt-timestamp" data-t="03:35:00">[03:35:00]</a>.
*   **Amount** (Number property): Represents the amount of income earned for a particular period <a class="yt-timestamp" data-t="03:44:00">[03:44:00]</a>.
*   The sum of income earned during the period is displayed at the bottom of the column <a class="yt-timestamp" data-t="03:50:00">[03:50:00]</a>.

### 2. Income Source Database
This database analyzes different sources of income <a class="yt-timestamp" data-t="03:59:00">[03:59:00]</a>.
*   **Name** (Title property): Defines income sources such as "salary", "side hustle", and "other income" <a class="yt-timestamp" data-t="04:05:00">[04:05:00]</a>.
*   **Earnings Database** (Relation property): Linked to the "Total Earnings database" <a class="yt-timestamp" data-t="04:12:00">[04:12:00]</a>.
*   **Income Details Property** (Relation property): Linked to the "Income Details database" <a class="yt-timestamp" data-t="04:22:00">[04:22:00]</a>.
*   **Actual Income** (Roll-up property): Derived from the "Income Details database", rolling up the "Amount" property and calculating its sum <a class="yt-timestamp" data-t="04:31:00">[04:31:00]</a>.
*   **Total Earnings** (Roll-up property): Derived from the "Earnings database", showing the original value of the amount <a class="yt-timestamp" data-t="04:51:00">[04:51:00]</a>.
*   **Frequency** (Roll-up property): Derived from the "Income Details database", extracting the "Frequency of Income" property and showing original values <a class="yt-timestamp" data-t="05:04:00">[05:04:00]</a>.
*   **Earnings in Percentage** (Formula property): Calculates the percentage of specific earnings relative to total earnings <a class="yt-timestamp" data-t="05:19:00">[05:19:00]</a>. This is represented with a percent format and a green bar <a class="yt-timestamp" data-t="05:31:00">[05:31:00]</a>.

### 3. Frequency of Income Database
This database provides analysis related to how frequently income is earned <a class="yt-timestamp" data-t="05:40:00">[05:40:00]</a>.
*   **Frequency** (Title property): Indicates income frequencies like "monthly income", "annual income", "quarterly income", "half yearly income", and "one-time income" <a class="yt-timestamp" data-t="05:47:00">[05:47:00]</a>.
*   **Earnings Associated to Each Frequency of Income** (Roll-up property): Derived from a related property in the next column. It rolls up the "earnings amount" property and calculates its sum value <a class="yt-timestamp" data-t="06:00:00">[06:00:00]</a>.
*   **Relation property** (Relation property): Linked to the "Income Details database", defining all income sources related to each frequency <a class="yt-timestamp" data-t="06:23:00">[06:23:00]</a>. This is automatically generated from the earlier database <a class="yt-timestamp" data-t="06:32:00">[06:32:00]</a>.
*   **Sources of Income** (Formula property): Calculates the number of sources. If the number is 1, it defines it as "one source"; if 2, "two sources"; if 3, "three sources"; and if 0, "no source" <a class="yt-timestamp" data-t="06:37:00">[06:37:00]</a>.

### 4. Total Earnings Database
This database relates the total earnings to all three income sources and finds the associated earnings <a class="yt-timestamp" data-t="07:07:00">[07:07:00]</a>.
*   **Total Earnings** (Title property): Describes the name <a class="yt-timestamp" data-t="07:17:00">[07:17:00]</a>.
*   **Income Source** (Relation property): Linked to the "Income Source database" where the three income sources are specified <a class="yt-timestamp" data-t="07:23:00">[07:23:00]</a>.
*   **Total Earnings** (Roll-up property): Rolls up values from the income sources and calculates the sum of total earnings associated with these sources <a class="yt-timestamp" data-t="07:31:00">[07:31:00]</a>.

### 5. Period Database
This database calculates the periodical income for each month and allows for further analysis, showing the percentage of monthly earnings to the total annual earnings <a class="yt-timestamp" data-t="07:46:00">[07:46:00]</a>.
*   **Month** (Title property): Represents the month of income <a class="yt-timestamp" data-t="08:02:00">[08:02:00]</a>.
*   **Income Details** (Relation property): Linked to the "Income Details database" which shows the income earned <a class="yt-timestamp" data-t="08:08:00">[08:08:00]</a>.
*   **Earnings** (Roll-up property): Rolled up from the "Income Details database", calculating the sum of the earnings amount <a class="yt-timestamp" data-t="08:16:00">[08:16:00]</a>.
*   **Total Earnings** (Roll-up property): Rolled up from the "Total Earnings database", representing the earnings amount with original values <a class="yt-timestamp" data-t="08:29:00">[08:29:00]</a>. This shows earnings for each month and total earnings for all months combined <a class="yt-timestamp" data-t="08:38:00">[08:38:00]</a>.
*   **Proportion of Earnings** (Formula property): Calculates the proportion of each month's earning to the total earning by dividing monthly earnings by total earnings <a class="yt-timestamp" data-t="08:44:00">[08:44:00]</a>. This is displayed as a percentage with a green bar <a class="yt-timestamp" data-t="08:54:00">[08:54:00]</a>.

## Primary Dashboard Presentation

The primary dashboard presents the aggregated information from the databases <a class="yt-timestamp" data-t="09:02:00">[09:02:00]</a>.

*   **Total Earnings**: A linked view of the "Total Earnings database" presented in a list view, showing the total income earned during the period <a class="yt-timestamp" data-t="09:10:00">[09:10:00]</a>.
*   **Sources of Income**: Presented in a three-column layout (created by typing `/three columns`) <a class="yt-timestamp" data-t="09:32:00">[09:32:00]</a>. These columns are linked to the "Income Source database" and displayed in a gallery format <a class="yt-timestamp" data-t="09:41:00">[09:41:00]</a>. This section shows the actual income and percentage of each source relative to the total income <a class="yt-timestamp" data-t="09:47:00">[09:47:00]</a>.
*   **Frequency**: Derived from the "Frequency of Income database" and presented in a gallery layout <a class="yt-timestamp" data-t="09:53:00">[09:53:00]</a>. It shows total earnings and sources of earnings for each frequency <a class="yt-timestamp" data-t="10:01:00">[10:01:00]</a>.
*   **Overview Section**: Linked to the "Period database" and displayed in a gallery mode <a class="yt-timestamp" data-t="10:07:00">[10:07:00]</a>. Information is divided into four quarters, specifying individual months for each quarter <a class="yt-timestamp" data-t="10:12:00">[10:12:00]</a>. It displays earnings for each month and their proportion to total earnings <a class="yt-timestamp" data-t="10:19:00">[10:19:00]</a>. Filters are applied for each quarter to show respective months <a class="yt-timestamp" data-t="10:24:00">[10:24:00]</a>.