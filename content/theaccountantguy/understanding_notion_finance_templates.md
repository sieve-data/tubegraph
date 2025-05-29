---
title: Understanding Notion finance templates
videoId: 2MkChIwv0t0
---

From: [[theaccountantguy]] <br/> 

This article describes how to build a minimalistic income tracker in Notion to stay on top of personal finances <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>. This [[notion_finance_templates | Notion finance template]] is designed to provide comprehensive analysis of income <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>.

## Key Sections of the Income Tracker

The income tracker is organized into four main sections:
*   **Total Earnings** Displays the overall earnings for a specified period <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.
*   **Sources of Income** Details total earnings from various sources like salary, side hustles, and other income, including the percentage each contributes to the total <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.
*   **Frequency of Income** Shows how often income is earned, along with total earnings and the number of sources for each frequency <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.
*   **Overview Section** Presents monthly income broken down into four quarters, indicating the percentage of monthly earnings relative to total earnings <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.

## Required Databases for Building the Tracker

To build this [[building_a_minimalistic_finance_template_in_notion | minimalistic finance template in Notion]], five interlinked databases are essential <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>:

1.  **Income Details Database** Stores specific information about earned income <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.
2.  **Income Source Database** Categorizes income by its origin <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.
3.  **Frequency of Income Database** Provides an overview of how often income is received <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.
4.  **Total Earnings Database** Reflects the aggregate earnings over a period <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.
5.  **Period Database** Displays periodical income earned throughout a year <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.

### Building the Income Details Database

This database is used for inputting specific income transaction details <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>. Its properties include:
*   **Income Details** (Title property): Specifies different sources of income received during the year <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.
*   **Period of Income** (Relation property): Links to the Period Database, reflecting monthly incomes per source <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>.
*   **Income Source** (Relation property): Links to the Income Source Database, specifying the source (e.g., salary, side hustle, other) <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>.
*   **Frequency of Income** (Relation property): Links to the Frequency of Income Database, indicating how often income is earned <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.
*   **Amount** (Number property): Shows the income earned for a specific period, with a sum calculation at the end <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>.

### Building the Income Source Database

This database [[analyzing_financial_data_through_notion_templates | analyzes financial data through Notion templates]] based on different sources of income <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>. Its properties include:
*   **Name** (Title property): Defines income sources like "Salary," "Side Hustle," and "Other Income" <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.
*   **Earnings** (Relation property): Links to the Total Earnings Database <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>.
*   **Income Details** (Relation property): Links to the Income Details Database <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.
*   **Actual Income** (Roll-up property): Rolls up the 'Amount' from the Income Details Database and sums it <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.
*   **Total Earnings** (Roll-up property): Rolls up the 'Amount' from the Earnings Database, showing the original value <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.
*   **Frequency** (Roll-up property): Extracts the 'Frequency of Income' property from the Income Details Database <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.
*   **Earnings in Percentage** (Formula property): Calculates the percentage of earnings from each source relative to the total earnings, displayed as a green bar <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>.

### Building the Frequency of Income Database

This database provides analysis related to how frequently income is earned <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>. Its properties include:
*   **Frequency** (Title property): Indicates income frequencies such as "Monthly Income," "Annual Income," "Quarterly Income," "Half Yearly Income," and "One-Time Income" <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>.
*   **Earnings Associated** (Roll-up property): Calculates the sum of earnings amounts from the related property in the next column <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.
*   **Relation to Income Details** (Relation property): Links to the Income Details Database, defining income sources related to each frequency <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>.
*   **Sources of Income** (Formula property): Calculates the number of sources, displayed as "one source," "two sources," "three sources," or "no source" <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>.

### Building the Total Earnings Database

This database relates total earnings to all three income sources <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>. Its properties include:
*   **Total Earnings** (Title property): The name of the property <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>.
*   **Income Source** (Relation property): Links to the Income Source Database, specifying the three income sources <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>.
*   **Total Earnings** (Roll-up property): Rolls up values from the Income Sources and calculates the sum of total earnings <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>.

### Building the Period Database

This database calculates periodical income for each month and provides further analysis <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>, including the percentage of monthly earnings to the yearly total <a class="yt-timestamp" data-t="00:07:57">[00:07:57]</a>. Its properties include:
*   **Month** (Title property): Represents the month of income <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>.
*   **Income Details** (Relation property): Links to the Income Details Database, showing earned income <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>.
*   **Earnings** (Roll-up property): Rolls up the 'Amount' from the Income Details Database, presenting the sum <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>.
*   **Total Earnings** (Roll-up property): Rolls up from the Total Earnings Database, showing the original values <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>.
*   **Proportion of Earnings** (Formula property): Calculates the proportion of each month's earnings to the total earnings by dividing monthly earnings by total earnings, formatted as a percentage with a green bar <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>.

## Primary Dashboard Presentation

The primary dashboard provides a summarized view of the income tracker data <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>.

*   **Total Earnings** This section links to the Total Earnings Database and is displayed in a List View, representing the total income earned during the period <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>.
*   **Sources of Income** Presented in a three-column layout, this section links to the Income Source Database and uses a Gallery format. It displays the actual income and percentage for each source relative to the total income <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a>.
*   **Frequency** Derived from the Frequency of Income Database, this section is presented in a Gallery layout, showing total earnings and sources of earnings for each frequency <a class="yt-timestamp" data-t="00:09:53">[00:09:53]</a>.
*   **Overview Section** Linked to the Period Database and displayed in Gallery mode, this section divides information into four quarters. It shows earnings for each month and their proportion to total earnings, with filters applied for respective months in each quarter <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a>.

This detailed structure facilitates [[using_notion_for_finance_management | using Notion for finance management]] effectively <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.