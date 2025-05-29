---
title: Using Databases in Notion for Expense Tracking
videoId: OV1faI8Z6yg
---

From: [[theaccountantguy]] <br/> 

This article details how to build an [[expense_tracking_using_notion | expense tracker]] in Notion, allowing users to [[budgeting_and_tracking_expenses_in_notion | budget and track expenses]] as required <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. The tracker provides an [[using_notion_for_expense_management | overview of total expenses]], showing budgeted and actual amounts, differences, and percentage changes <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>. It also categorizes expenses as needs, desires, and wants <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.

## Key Features

The [[creating_an_expense_tracker_with_notion | Notion expense tracker]] includes:
*   **Top 10 Expenses Highlights** A reflection of the top 10 expenses incurred during a period, along with the least 10 and most recent expenses <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.
*   **Actual vs. Budget Expenses** Expenses are divided into six heads, indicating total budgeted expenses, total actual expenses, differences, and percentage changes <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.
*   **Expenses Overview During the Period** Expenses are categorized into months, divided into four quarters. For each month, it shows total expenses incurred and their proportion to total expenses <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>.
*   **Expenses Overview in Percentage** Displays expenses categorized into six heads, showing total expenses and their proportion <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.
*   **Frequency of Expenses** Indicates how frequently an expense is incurred, categorized as daily, one-time, weekly, monthly, quarterly, half-yearly, and annually. For each category, it shows the total amount and sources of expenses <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.

## Building the Expense Tracker: Databases

To build this [[how_to_use_notion_for_tracking_business_expenses | expense tracker]], seven databases are required <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>.

### 1. Expense Details Database
This database specifies details related to each individual expense <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>.
*   **Expense Details** (Title property): Shows individual expenses incurred <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.
*   **Period of Expense** (Relation property): Links to the Period database, specifying the month an expense is incurred <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>.
*   **Expense Source** (Relation property): Links to the Expense Source database, specifying the source under which an expense is incurred <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.
*   **Frequency of Expense** (Relation property): Links to the Frequency of Expense database, indicating how frequently an expense is incurred <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.
*   **Expense Categories** (Relation property): Links to the Expense Categories database, specifying the category for each expense source <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
*   **Actual Expense** (Number property): Specifies the actual amount of expense incurred in US dollars <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.
*   **Budgeted Expense** (Number property): The estimated budgeted expense for each month in US dollars <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.
    *   *Sum of actual and budgeted expenses is displayed at the bottom* <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>.

### 2. Expense Source Database
This database specifies six different sources of expenses <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.
*   **Source of Expense** (Title property): Specifies one of the six expense heads <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>.
*   **Actual Expense** (Roll-up property): Rolled up from the Expense Details database, providing the sum of actual expenses <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>.
*   **Budgeted Expense** (Roll-up property): Rolled up from the Expense Details database, providing the sum of budgeted expenses <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>.
*   **Total Expenses** (Roll-up property): Derived from the Total Expenses database, extracting the total actual expenses amount <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>.
*   **Difference** (Formula property): Shows the difference between actual and budgeted expenses <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.
*   **Change in Percentage** (Formula property): Calculated as (Difference / Budgeted Expense Amount) <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.

### 3. Frequency of Expenses Database
This database calculates how frequently expenses are incurred and performs further analysis <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>.
*   **Frequency** (Title property): Specifies each individual mode of frequency (e.g., daily, weekly) <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>.
*   **Expense Details** (Relation property): Relates different types of expenses from the Expense Details database to each frequency type <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>.
*   **Sources of Expense** (Formula property): Calculates the unique sources of expenses for each frequency <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>.

### 4. Total Expenses Database
This database calculates the total expenses incurred during a period <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>.
*   **Name** (Title property): Describes the property (e.g., total actual expenses, total budgeted expenses, difference, change in percentage) <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>.
*   **Total Actual Expenses** (Roll-up property): Calculates total expenses from the Expense Source database, providing the sum <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>.
*   **Total Budgeted Expense** (Roll-up property): Calculates total budgeted expenses from the Expense Source database, providing the sum <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>.
*   **Amount** (Formula property): Derives necessary values based on the "Name" property (e.g., actual expense, budgeted expense, difference, or change in percentage) <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>.

### 5. Period of Expense Database
This database specifies expenses for each month of the year and categorizes them, showing proportions <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>.
*   **Month** (Title property): Specifies the month for each expense <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>.
*   **Expense Details** (Relation property): Relates to the Expense Details database, calculating expenses incurred each period <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>.
*   **Expenses for Each Month** (Roll-up property): Derived from the Expense Details database, calculating the sum of actual expense values <a class="yt-timestamp" data-t="00:09:58">[00:09:58]</a>.
*   **Total Expenses** (Roll-up property): Calculated from the Total Expense database, providing the total actual expense value <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>.
*   **Proportion of the Total Expense** (Formula property): Calculates (Expenses / Total Expenses), denoted as a percentage bar <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>.

### 6. Expense Budget Classification Database
This database classifies expenses under six heads and provides details on total actual expenses, total budgeted expenses, differences, and percentage changes for each <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>.
*   **Title** (Title property): Specifies required properties for use <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>.
*   **Relation** (Relation property): Relates to the Expense Source database, specifying individual expense heads <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>.
*   **Amount** (Formula property): Derives total actual expenses, total budgeted expenses, and the difference for specific expense heads <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>.
*   **Change in Percentage** (Formula property): Calculated as (Difference / Budgeted Expense) <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>.
*   **Actual Expenses** (Roll-up property): Derives values from the Expense Source database, calculating the sum of expense values <a class="yt-timestamp" data-t="00:11:45">[00:11:45]</a>.
*   **Budgeted Expenses** (Roll-up property): Rolled up from the Expense Source database, calculating the sum of expense values <a class="yt-timestamp" data-t="00:11:53">[00:11:53]</a>.
*   **Change in Percentage** (Roll-up property): Derived from the Expense Source database, showing the original change in percentage value <a class="yt-timestamp" data-t="00:12:11">[00:12:11]</a>.
*   **Difference** (Roll-up property): Shows the difference between budgeted and actual expenses <a class="yt-timestamp" data-t="00:12:21">[00:12:21]</a>.
    *   *These columns are repeated for all six expense heads* <a class="yt-timestamp" data-t="00:12:27">[00:12:27]</a>.

### 7. Expense Categories Database
This database specifies the three types of expenses: needs, wants, and desires <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>.
*   **Title** (Title property): Specifies the category name <a class="yt-timestamp" data-t="00:12:44">[00:12:44]</a>.
*   **Relation** (Relation column): Relates to the Expense Details database, capturing all expenses related to needs, wants, and desires separately <a class="yt-timestamp" data-t="00:12:48">[00:12:48]</a>.
*   **Expenses Amount** (Roll-up property): The actual expenses incurred, derived from the Expense Details database, calculating the sum for each type of expense <a class="yt-timestamp" data-t="00:12:57">[0:12:57]</a>.
*   **Total Expenses** (Roll-up property): Derived from the Total Expenses database, providing the sum of all combined expenses <a class="yt-timestamp" data-t="00:13:12">[00:13:12]</a>.

## Primary Dashboard Presentation

The primary dashboard of the [[using_databases_for_financial_tracking_in_notion | Notion expense tracker]] is structured for clear presentation <a class="yt-timestamp" data-t="00:13:28">[00:13:28]</a>:

*   **Overview of Total Expenses**: Linked to the Total Expenses database and displayed in a gallery view <a class="yt-timestamp" data-t="00:13:32">[00:13:32]</a>.
*   **Expense Categories**: Three categories (needs, wants, desires) linked to the Expense Categories database, displayed in a gallery format within a three-column layout <a class="yt-timestamp" data-t="00:13:43">[00:13:43]</a>.
*   **Top 10 Highlights**: Linked to the Expense Details database and set out in a list format <a class="yt-timestamp" data-t="00:13:57">[00:13:57]</a>.
    *   Recent expenses are sorted by created time in descending order <a class="yt-timestamp" data-t="00:14:07">[00:14:07]</a>.
    *   Least 10 expenses are sorted by actual expenses in ascending order <a class="yt-timestamp" data-t="00:14:11">[00:14:11]</a>.
    *   Top 10 expenses are sorted in descending order <a class="yt-timestamp" data-t="00:14:16">[00:14:16]</a>.
*   **Actual vs. Budgeted Expenses**: Linked to the Expense Budget Classification database and displayed in a gallery format <a class="yt-timestamp" data-t="00:14:25">[00:14:25]</a>.
*   **Expenses Overview**: Linked to the Period database and presented in a gallery format, with filters applied for each quarter to show necessary months <a class="yt-timestamp" data-t="00:14:36">[00:14:36]</a>.
*   **Expenses Overview Section**: Linked to the Expense Source database, set out in a gallery format, and repeated for all six heads of expenses <a class="yt-timestamp" data-t="00:14:55">[00:14:55]</a>.
*   **Frequency of Expenses**: Linked to the Frequency of Expense database, displayed in a gallery format with desired properties enabled <a class="yt-timestamp" data-t="00:15:05">[00:15:05]</a>.

This comprehensive setup allows for detailed [[using_notion_for_personal_and_business_expense_tracking | personal and business expense tracking]] and analysis within Notion.