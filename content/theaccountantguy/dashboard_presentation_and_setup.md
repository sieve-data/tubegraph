---
title: Dashboard Presentation and Setup
videoId: OV1faI8Z6yg
---

From: [[theaccountantguy]] <br/> 

This article outlines how to build an expense tracker and manage spending effectively within Notion, covering both the dashboard's presentation and the underlying database setup. This tracker provides a comprehensive [[overview_and_presentation_of_financial_data_in_notion | overview]] of financial data <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

## Expense Tracker Dashboard Overview

The expense tracker dashboard includes several key sections:

*   **Overview of Total Expenses** This section displays total budgeted expenses, total actual expenses, the difference, and the change in percentage <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>.
*   **Categorized Expenses** Expenses are categorized into needs, desires, and wants <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.
*   **Top 10 Expenses Highlights** This highlights the top 10 expenses, the least 10 expenses, and recent expenses incurred during a period <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.
*   **Actual vs. Budgeted Expenses** This part breaks down expenses into six categories, showing total budgeted expenses, total actual expenses, their difference, and the percentage change <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.
*   **Expenses Overview by Period** Expenses are categorized by month, divided into four quarters, indicating total expenses incurred and their proportion to overall total expenses <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>.
*   **Expenses Overview in Percentage** This section categorizes expenses into six heads, displaying total expenses and their proportion to total expenses for each <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.
*   **Frequency of Expenses** This indicates how frequently an expense is incurred (daily, one-time, weekly, monthly, quarterly, half-yearly, annually), along with the total amount and sources of expenses for each frequency <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.

## Database Setup for the Expense Tracker

To build this expense tracker, seven databases are required <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>:

1.  **Expense Details Database**
    *   **Purpose**: Showcases individual expense details <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>.
    *   **Properties**:
        *   `Expense Details` (Title property): Individual expenses incurred <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.
        *   `Period of Expense` (Relation property): Links to the Period database, specifying the month an expense was incurred <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>.
        *   `Expense Source` (Relation property): Links to the Expense Source database, specifying the category of expense <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.
        *   `Frequency of Expense` (Relation property): Links to the Frequency of Expense database, indicating how frequently an expense is incurred <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.
        *   `Expense Categories` (Relation property): Links to the Expense Categories database, specifying the category for each expense source <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
        *   `Actual Expense` (Number property): The actual amount of expense incurred in USD <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.
        *   `Budgeted Expense` (Number property): The budgeted expense estimated for each month in USD <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>.
    *   **Calculations**: Displays the sum of actual and budgeted expenses at the bottom <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>.

2.  **Expense Source Database**
    *   **Purpose**: Categorizes expenses under six heads with subsequent analysis <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.
    *   **Properties**:
        *   `Source of Expense` (Title property): One of the six heads of expenses <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>.
        *   `Actual Expense` (Roll-up property): Sum of actual expenses from the Expense Details database <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>.
        *   `Budgeted Expense` (Roll-up property): Sum of budgeted expenses from the Expense Details database <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>.
        *   `Total Expenses` (Roll-up property): Extracts total actual expenses from the Total Expenses database <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>.
        *   `Difference` (Formula property): `Actual Expenses - Budgeted Expenses` <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.
        *   `Change in Percentage` (Formula property): `Difference / Budgeted Expense` (formatted as a percentage) <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.

3.  **Frequency of Expenses Database**
    *   **Purpose**: Showcases how frequently expenses are incurred <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>.
    *   **Properties**:
        *   `Frequency` (Title property): Specifies each individual mode of frequency (e.g., daily, monthly) <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>.
        *   `Expense Details` (Relation property): Relates to the Expense Details database, linking expenses to their frequency <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>.
        *   `Sources of Expense` (Formula property): Calculates unique sources of expenses for each frequency (e.g., "Commutation expenses" appearing twice counts as one source) <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>.

4.  **Total Expenses Database**
    *   **Purpose**: Reflects total expenses incurred for all six heads, categorized as actual, budgeted, difference, and change <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>.# Dashboard Presentation and Setup

This article outlines how to build an expense tracker and manage spending effectively within Notion, covering both the dashboard's presentation and the underlying database setup. This tracker provides a comprehensive [[overview_and_presentation_of_financial_data_in_notion | overview]] of financial data <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

## Expense Tracker Dashboard Overview

The expense tracker dashboard includes several key sections:

*   **Overview of Total Expenses** This section displays total budgeted expenses, total actual expenses, the difference, and the change in percentage <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>.
*   **Categorized Expenses** Expenses are categorized into needs, desires, and wants <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.
*   **Top 10 Expenses Highlights** This highlights the top 10 expenses, the least 10 expenses, and recent expenses incurred during a period <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.
*   **Actual vs. Budgeted Expenses** This part breaks down expenses into six categories, showing total budgeted expenses, total actual expenses, their difference, and the percentage change <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.
*   **Expenses Overview by Period** Expenses are categorized by month, divided into four quarters, indicating total expenses incurred and their proportion to overall total expenses <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>.
*   **Expenses Overview in Percentage** This section categorizes expenses into six heads, displaying total expenses and their proportion to total expenses for each <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.
*   **Frequency of Expenses** This indicates how frequently an expense is incurred (daily, one-time, weekly, monthly, quarterly, half-yearly, annually), along with the total amount and sources of expenses for each frequency <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.

## Database Setup for the Expense Tracker

To build this expense tracker, seven databases are required <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>:

1.  **Expense Details Database**
    *   **Purpose**: Showcases individual expense details <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>.
    *   **Properties**:
        *   `Expense Details` (Title property): Individual expenses incurred <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.
        *   `Period of Expense` (Relation property): Links to the Period database, specifying the month an expense was incurred <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>.
        *   `Expense Source` (Relation property): Links to the Expense Source database, specifying the category of expense <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.
        *   `Frequency of Expense` (Relation property): Links to the Frequency of Expense database, indicating how frequently an expense is incurred <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.
        *   `Expense Categories` (Relation property): Links to the Expense Categories database, specifying the category for each expense source <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
        *   `Actual Expense` (Number property): The actual amount of expense incurred in USD <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.
        *   `Budgeted Expense` (Number property): The budgeted expense estimated for each month in USD <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>.
    *   **Calculations**: Displays the sum of actual and budgeted expenses at the bottom <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>.

2.  **Expense Source Database**
    *   **Purpose**: Categorizes expenses under six heads with subsequent analysis <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.
    *   **Properties**:
        *   `Source of Expense` (Title property): One of the six heads of expenses <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>.
        *   `Actual Expense` (Roll-up property): Sum of actual expenses from the Expense Details database <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>.
        *   `Budgeted Expense` (Roll-up property): Sum of budgeted expenses from the Expense Details database <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>.
        *   `Total Expenses` (Roll-up property): Extracts total actual expenses from the Total Expenses database <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>.
        *   `Difference` (Formula property): `Actual Expenses - Budgeted Expenses` <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.
        *   `Change in Percentage` (Formula property): `Difference / Budgeted Expense` (formatted as a percentage) <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.

3.  **Frequency of Expenses Database**
    *   **Purpose**: Showcases how frequently expenses are incurred <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>.
    *   **Properties**:
        *   `Frequency` (Title property): Specifies each individual mode of frequency (e.g., daily, monthly) <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>.
        *   `Expense Details` (Relation property): Relates to the Expense Details database, linking expenses to their frequency <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>.
        *   `Sources of Expense` (Formula property): Calculates unique sources of expenses for each frequency (e.g., "Commutation expenses" appearing twice counts as one source) <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>.

4.  **Total Expenses Database**
    *   **Purpose**: Reflects total expenses incurred for all six heads, categorized as actual, budgeted, difference, and change <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>.
    *   **Properties**:
        *   `Name` (Title property): Defines the property (e.g., "Total Actual Expenses", "Total Budgeted Expenses", "Difference", "Change in Percentage") <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>.
        *   `Total Actual Expenses` (Roll-up property): Calculates total expenses from the Expense Source database (sum value) <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>.
        *   `Total Budgeted Expense` (Roll-up property): Calculates total budgeted expenses from the Expense Source database (sum value) <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>.
        *   `Amount` (Formula property): Derives values based on the `Name` property (e.g., actual expense value if `Name` is "Total Actual Expenses", budgeted if "Total Budgeted Expenses", difference if "Difference", and percentage change if "Change in Percentage") <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>.

5.  **Period of Expense Database**
    *   **Purpose**: Specifies monthly expenses for the entire year and categorizes expenses with their proportion <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>.
    *   **Properties**:
        *   `Month` (Title property): The month for each expense <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>.
        *   `Expense Details` (Relation property): Links to the Expense Details database, calculating expenses incurred each period <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>.
        *   `Expenses for each month` (Roll-up property): Sum of actual expense values from the Expense Details database <a class="yt-timestamp" data-t="00:09:58">[00:09:58]</a>.
        *   `Total Expenses` (Roll-up property): Total actual expense value from the Total Expense database <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>.
        *   `Proportion of the total expense` (Formula property): `Expenses for each month / Total Expenses` (denoted as a percentage in a red bar) <a class="yt-timestamp" data-t="00:10:19">[00:10:19]</a>.

6.  **Expense Budget Classification Database**
    *   **Purpose**: Classifies expenses into six heads with budgeted expenses, actual expenses, differences, and change for each <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>.
    *   **Properties**:
        *   `Title Property`: Specifies required properties <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>.
        *   `Relation Property`: Links to the Expense Source database, specifying individual heads of expense <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>.
        *   `Amount` (Formula property): Derives total actual, total budgeted, and difference for specific expense heads (e.g., travel and transportation) <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>.
        *   `Change in Percentage` (Formula property): `Difference / Budgeted Expense` <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>.
        *   `Actual Expenses` (Roll-up property): Sum of expense values from the Expense Source database <a class="yt-timestamp" data-t="00:11:45">[00:11:45]</a>.
        *   `Budgeted Expenses` (Roll-up property): Sum of expense values from the Expense Source database <a class="yt-timestamp" data-t="00:11:53">[00:11:53]</a>.
        *   `Change in Percentage` (Roll-up property): Original value of change in percentage from Expense Source database <a class="yt-timestamp" data-t="00:12:11">[00:12:11]</a>.
        *   `Difference` (Roll-up property): Difference between budgeted and actual expenses <a class="yt-timestamp" data-t="00:12:21">[00:12:21]</a>.
    *   **Note**: These columns need to be repeated for all six heads of expenses <a class="yt-timestamp" data-t="00:12:27">[00:12:27]</a>.

7.  **Expense Categories Database**
    *   **Purpose**: Reflects expenses categorized as needs, wants, and desires, providing further analysis <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.
    *   **Properties**:
        *   `Title Property`: Specifies the categories (needs, wants, desires) <a class="yt-timestamp" data-t="00:12:44">[00:12:44]</a>.
        *   `Relation Column`: Links to the Expense Details database, capturing expenses related to each category separately <a class="yt-timestamp" data-t="00:12:48">[00:12:48]</a>.
        *   `Expenses Amount` (Roll-up property): Sum of actual expenses from the Expense Details database for each expense type <a class="yt-timestamp" data-t="00:12:57">[00:12:57]</a>.
        *   `Total Expenses` (Roll-up property): Sum of all combined expenses from the Total Expenses database <a class="yt-timestamp" data-t="00:13:12">[00:13:12]</a>.

## Dashboard Presentation

The primary dashboard for the expense tracker brings together all these databases for a comprehensive [[dashboard_analysis_for_personal_finance | financial overview]] and [[designing_a_dashboard_with_linked_databases_and_calendar_view_in_notion | dashboard presentation]] <a class="yt-timestamp" data-t="00:13:25">[00:13:25]</a>.

*   **Overview of Total Expenses**: Linked to the Total Expenses database, displayed in a gallery view <a class="yt-timestamp" data-t="00:13:32">[00:13:32]</a>.
*   **Three Categories of Expenses**: Linked to the Expense Categories database, presented in a gallery format within a three-column layout (achieved by typing `/three column`) <a class="yt-timestamp" data-t="00:13:43">[00:13:43]</a>.
*   **Top 10 Highlights**: Linked to the Expense Details database, set out in a list format <a class="yt-timestamp" data-t="00:13:57">[00:13:57]</a>.
    *   Recent expenses are sorted by `created time` in descending order <a class="yt-timestamp" data-t="00:14:07">[00:14:07]</a>.
    *   Least 10 expenses are sorted by `actual expenses` in ascending order <a class="yt-timestamp" data-t="00:14:11">[00:14:11]</a>.
    *   Top 10 expenses are sorted in descending order <a class="yt-timestamp" data-t="00:14:16">[00:14:16]</a>.
*   **Actual vs. Budgeted Expenses**: Linked to the Expense Budget Classification database, displayed in a gallery format <a class="yt-timestamp" data-t="00:14:25">[00:14:25]</a>.
*   **Expenses Overview (by Period)**: Linked to the Period database, presented in a gallery format. Filters are applied for each quarter to show relevant months <a class="yt-timestamp" data-t="00:14:36">[00:14:36]</a>.
*   **Expenses Overview (by Percentage)**: Linked to the Expense Source database, set out in a gallery format and repeated for all expense heads <a class="yt-timestamp" data-t="00:14:55">[00:14:55]</a>.
*   **Frequency of Expenses**: Linked to the Frequency of Expense database, shown in a gallery format with desired properties enabled <a class="yt-timestamp" data-t="00:15:05">[00:15:05]</a>.