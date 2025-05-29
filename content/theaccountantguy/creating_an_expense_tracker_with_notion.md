---
title: Creating an Expense Tracker with Notion
videoId: OV1faI8Z6yg
---

From: [[theaccountantguy]] <br/> 

This article outlines how to build a comprehensive [[notion_expense_tracker_setup | Notion expense tracker]] to manage and analyze spending <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>. This tracker provides an overview of total expenses, categorized spending, top/least/recent expenses, and detailed comparisons between actual and budgeted amounts <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

## Key Features of the Expense Tracker

The Notion expense tracker includes several key sections for detailed [[expense_tracking_using_notion | expense tracking]] and analysis:

*   **Overview of Total Expenses** Displays total budgeted expenses, total actual expenses, the difference, and the percentage change <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>.
*   **Categorized Expenses** Expenses are categorized into needs, desires, and wants <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.
*   **Top 10 Expenses Highlights** Reflects the top 10 expenses, the least 10 expenses, and the most recent expenses incurred during a period <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.
*   **Actual vs. Budgeted Expenses** Presents expenses divided into six heads, showing total budgeted expenses, total actual expenses, difference, and percentage change for each <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.
*   **Expenses Overview During the Period** Categorizes expenses by month, divided into four quarters, showing total expenses incurred and their proportion to total expenses <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>.
*   **Expenses Overview in Percentage** Shows expenses categorized into six heads, with total expenses and their proportion to the total for each head <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.
*   **Frequency of Expenses** Indicates how frequently an expense is incurred, categorized as daily, one-time, weekly, monthly, quarterly, half-yearly, and annually <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>. For each frequency, it shows the total amount incurred and the sources of expenses <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.

## Required Databases for the Expense Tracker

To build this [[notion_expense_tracker_setup | Notion expense tracker]], seven databases are necessary <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>:

1.  **Expense Details** Showcases details related to individual expenses <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>.
2.  **Expense Source** Categorizes expenses under six heads with subsequent analysis <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.
3.  **Frequency of Expenses** Shows how frequently an expense is incurred <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>.
4.  **Total Expenses** Reflects the total expenses incurred for all six heads, categorized as actual, budgeted, difference, and change <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>.
5.  **Period of Expense** Specifies monthly expenses for the entire year and helps categorize expenses with their proportion <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>.
6.  **Expense Budget Classification** Classifies expenses into six heads, showing budgeted, actual, differences, and changes for each <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>.
7.  **Expense Categories** Reflects expenses based on needs, wants, and desires, providing further analysis <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>.

## Building Each Database

### Expense Details Database

This database specifies details related to each individual expense <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.

*   **Expense Details** (Title property) Shows individual expenses incurred <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.
*   **Period of Expense** (Relation property) Links to the Period database, specifying the month for each expense <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>.
*   **Expense Source** (Relation property) Links to the Expense Source database, specifying the source of expense <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.
*   **Frequency of Expense** (Relation property) Links to the Frequency of Expense database, indicating how frequently an expense is incurred <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.
*   **Expense Categories** (Relation property) Links to the Expense Categories database, specifying the category for each source of expense <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
*   **Actual Expense** (Number property) Specifies the actual amount of expense incurred for the period in US dollars <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.
*   **Budgeted Expense** (Number property) The budgeted expense estimated for each month in US dollars <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>.

The sum of actual and budgeted expenses can be found at the bottom of this database <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>.

### Expense Source Database

This database specifies the six different sources of expenses <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>.

*   **Source of Expense** (Title property) Specifies one of the six heads of expenses <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>.
*   **Actual Expense** (Roll-up property) Rolled up from the Expense Details database, summing actual expense amounts <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>.
*   **Budgeted Expense** (Roll-up property) Rolled up from the Expense Details database, summing budgeted expense amounts <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>.
*   **Total Expenses** (Roll-up property) Derived from the Total Expenses database, extracting the total actual expenses amount <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>.
*   **Difference** (Formula property) Calculates the difference between actual expenses and budgeted expenses <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.
*   **Change in Percentage** (Formula property) Calculates the difference divided by the budgeted expense amount, displayed as a percentage <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.

### Frequency of Expenses Database

This database calculates how frequently expenses are incurred and performs further analysis <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>.

*   **Frequency** (Title property) Specifies each individual mode of frequency (e.g., daily, weekly) <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>.
*   **Relation property** Relates to the Expense Details database, linking different types of expenses to each frequency type <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>.
*   **Sources of Expense** (Formula property) Calculates the unique sources of expenses for each frequency <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>. For example, "commutation expenses" written twice is counted as one source <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>.

### Total Expenses Database

This database calculates the total expenses incurred during the period <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>. It contains four properties: Total Actual Expenses, Total Budgeted Expenses, Difference, and Change in Percentage <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>.

*   **Total Actual Expenses** (Roll-up property) Calculates the total expenses from the Expense Source database, summing values <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>.
*   **Total Budgeted Expense** (Roll-up property) Calculates the total budgeted expenses from the Expense Source database, summing values <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>.
*   **Amount** (Formula property) Derives values based on the "name" property:
    *   Gets actual expense value if the name is "total actual expenses" <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>.
    *   Gets budgeted expense value if the name is "total budgeted expenses" <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>.
    *   Gets the difference if the name is "difference" <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>.
    *   Calculates the change in percentage (difference divided by budgeted expense) if the name is "change in percentage" <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>.

### Period of Expense Database

This database specifies expenses for each month and provides further analysis <a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a>.

*   **Month** (Title property) Specifies the month for each expense <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>.
*   **Expense Details** (Relation property) Relates to the Expense Details database, calculating expenses incurred each period <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>.
*   **Expenses for each month** (Roll-up property) Derived from the Expense Details database, calculating the sum of actual expense values <a class="yt-timestamp" data-t="00:09:58">[00:09:58]</a>.
*   **Total Expenses** (Roll-up property) Calculated from the Total Expense database, providing the total actual expense value <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>.
*   **Proportion of the total expense** (Formula property) Calculates expenses divided by total expenses, displayed as a percentage with a red bar <a class="yt-timestamp" data-t="00:10:19">[00:10:19]</a>.
*   **Total expenses** (Relation property) Linked to the Total Expenses database to derive total expenses value <a class="yt-timestamp" data-t="00:10:36">[00:10:36]</a>.

### Expense Budget Classification Database

This database classifies expenses under six heads and provides details on total actual expenses, total budgeted expenses, difference, and change in percentage for each head <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>.

*   **Title property** Specifies the required properties for use <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>.
*   **Relation property** Relates to the Expense Source database, specifying individual heads of expense <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>.
*   **Amount** (Formula property) Derives total actual expenses, total budgeted expenses, and the difference for specific expense heads like travel and transportation <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>.
*   **Change in percentage** (Formula property) Calculates the difference divided by the budgeted expense <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>.
*   **Actual Expenses** (Roll-up property) Derives values from the Expense Source database, summing expense values <a class="yt-timestamp" data-t="00:11:45">[00:11:45]</a>.
*   **Budgeted Expenses** (Roll-up property) Derives values from the Expense Source database, summing expense values <a class="yt-timestamp" data-t="00:11:53">[00:11:53]</a>.
*   **Change in percentage** (Roll-up property) Derived from the Expense Source database, showing the original change in percentage value <a class="yt-timestamp" data-t="00:12:11">[00:12:11]</a>.
*   **Difference** (Roll-up property) Shows the difference between budgeted and actual expenses <a class="yt-timestamp" data-t="00:12:21">[00:12:21]</a>.
    *   These columns need to be repeated for all six heads of expenses <a class="yt-timestamp" data-t="00:12:27">[00:12:27]</a>.

### Expense Categories Database

This database specifies the three types of expenses: needs, wants, and desires <a class="yt-timestamp" data-t="00:12:35">[00:12:35]</a>.

*   **Title property** (First column) <a class="yt-timestamp" data-t="00:12:44">[00:12:44]</a>.
*   **Relation column** Related to the Expense Details database, capturing all expenses related to needs, wants, and desires separately <a class="yt-timestamp" data-t="00:12:48">[00:12:48]</a>.
*   **Expenses amount** (Roll-up property) Represents actual expenses incurred, derived from the Expense Details database, summing the actual expense amount for each individual type of expense <a class="yt-timestamp" data-t="00:12:57">[00:12:57]</a>.
*   **Total expenses** (Roll-up property) Derived from the Total Expenses database, summing all combined expenses <a class="yt-timestamp" data-t="00:13:12">[00:13:12]</a>.

## Primary Dashboard Presentation

The primary dashboard for the [[using_notion_for_expense_management | Notion expense management]] tracker is set up as follows <a class="yt-timestamp" data-t="00:13:28">[00:13:28]</a>:

*   **Overview of Total Expenses** Linked to the Total Expenses database, displayed in a gallery mode view <a class="yt-timestamp" data-t="00:13:32">[00:13:32]</a>.
*   **Three Categories of Expenses** Linked to the Expense Categories database, displayed in a gallery format <a class="yt-timestamp" data-t="00:13:43">[00:13:43]</a>. The database needs to be put into a three-column format using `/three column` command <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a>.
*   **Top 10 Highlights** Linked to the Expense Details database, displayed in a list format <a class="yt-timestamp" data-t="00:14:03">[00:14:03]</a>.
    *   Recent expenses are sorted by created time in descending order <a class="yt-timestamp" data-t="00:14:07">[00:14:07]</a>.
    *   Least 10 expenses are sorted by actual expenses in ascending order <a class="yt-timestamp" data-t="00:14:11">[00:14:11]</a>.
    *   Top 10 expenses are sorted in descending order <a class="yt-timestamp" data-t="00:14:14">[00:14:14]</a>.
*   **Actual versus Budgeted Expenses** Linked to the Expense Budget Classification database, displayed in a gallery format <a class="yt-timestamp" data-t="00:14:25">[00:14:25]</a>.
*   **Expenses Overview** Linked to the Period database, displayed in a gallery format <a class="yt-timestamp" data-t="00:14:36">[00:14:36]</a>. Filters are applied for each quarter to show necessary months <a class="yt-timestamp" data-t="00:14:42">[00:14:42]</a>.
*   **Expenses Overview Section** Linked to the Expense Source database, displayed in a gallery format and repeated for all expense heads <a class="yt-timestamp" data-t="00:14:55">[00:14:55]</a>.
*   **Frequency of Expenses** Linked to the Frequency of Expense database, displayed in a gallery format with desired properties enabled <a class="yt-timestamp" data-t="00:15:05">[00:15:05]</a>.

A template for this [[budgeting_and_tracking_expenses_in_notion | budgeting and tracking expenses in Notion]] system can be downloaded via a link in the video description <a class="yt-timestamp" data-t="00:15:16">[00:15:16]</a>.