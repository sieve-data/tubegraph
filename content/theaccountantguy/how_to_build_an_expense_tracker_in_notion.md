---
title: How to build an expense tracker in Notion
videoId: OV1faI8Z6yg
---

From: [[theaccountantguy]] <br/> 

This guide details how to [[using_notion_for_expense_tracking | build an expense tracker]] in Notion, allowing you to effectively [[tracking_expenses_with_notion | track expenses]] and manage your spending <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. The tracker provides a comprehensive overview of your financial data, including budgeted versus actual spending and expense categorization <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

## Expense Tracker Features Overview

The completed expense tracker includes several key sections:
*   **Overview of Total Expenses** Displays total budgeted expenses, total actual expenses, the difference, and the percentage change <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.
*   **Categorized Expenses** Divides expenses into "needs," "desires," and "wants" <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.
*   **Top 10 Expenses Highlights** Shows the top 10, least 10, and most recent expenses incurred during a specific period <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.
*   **Actual vs. Budget Expenses** Categorizes expenses into six heads, detailing total budgeted expenses, total actual expenses, the difference, and the percentage change for each <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.
*   **Expenses Overview During the Period** Organizes expenses by month, divided into four quarters, indicating total expenses and their proportion to total expenses <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>.
*   **Expenses Overview in Percentage** Presents expenses categorized into six heads, showing total expenses and their proportion to the total <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.
*   **Frequency of Expenses** Identifies how frequently an expense is incurred (daily, one-time, weekly, monthly, quarterly, half-yearly, annually), along with the total amount and sources for each frequency <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.

## Building the Expense Tracker: Database Setup

To [[creating_a_budget_tracker_with_notion | create this expense tracker]], you will need to [[using_notion_expense_tracker_for_personal_or_business_expenses | set up]] seven interlinked databases <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.

### 1. Expense Details Database
This database specifies the details of each individual expense <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>.
*   **Expense Details (Title Property):** For individual expenses incurred <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.
*   **Period of Expense (Relation Property):** Links to the Period Database, specifying the month an expense was incurred <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>.
*   **Expense Source (Relation Property):** Links to the Expense Source database, indicating the source of the expense <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.
*   **Frequency of Expense (Relation Property):** Links to the Frequency of Expense database, showing how often an expense is incurred <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.
*   **Expense Categories (Relation Property):** Links to the Expense Categories database, classifying each expense source <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
*   **Actual Expense (Number Property):** Specifies the actual amount incurred in US dollars <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.
*   **Budgeted Expense (Number Property):** The estimated budgeted expense for each month in US dollars <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>.
    > The sum of actual and budgeted expenses can be viewed at the bottom of this database <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>.

### 2. Expense Source Database
This database specifies the six different sources (heads) under which expenses are incurred and provides subsequent analysis <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.
*   **Source of Expense (Title Property):** Specifies one of the six expense heads <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>.
*   **Actual Expense (Roll-up Property):** Sums the actual expense amounts from the Expense Details database <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>.
*   **Budgeted Expense (Roll-up Property):** Sums the budgeted expense amounts from the Expense Details database <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>.
*   **Total Expenses (Roll-up Property):** Extracts the total actual expenses amount from the Total Expenses database <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>.
*   **Difference (Formula Property):** Calculates `Actual Expenses - Budgeted Expenses` <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.
*   **Change in Percentage (Formula Property):** Calculates `Difference / Budgeted Expense` and formats as a percentage <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.

### 3. Frequency of Expenses Database
This database helps calculate how frequently an expense is incurred and performs further analysis <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>.
*   **Frequency (Title Property):** Denotes each individual mode of frequency (e.g., daily, weekly) <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>.
*   **Expense Details (Relation Property):** Relates different types of expenses from the Expense Details database to each frequency type <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>.
*   **Sources of Expense (Formula Property):** Calculates unique sources of expenses for each frequency <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>.

### 4. Total Expenses Database
This database reflects the total expenses incurred for all six expense heads <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>.
*   **Name (Title Property):** Represents properties like total actual expenses, total budgeted expenses, difference, and percentage change <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>.
*   **Total Actual Expenses (Roll-up Property):** Calculates total expenses from the Expense Source database, summing the values <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>.
*   **Total Budgeted Expense (Roll-up Property):** Calculates total budgeted expenses from the Expense Source database, summing the values <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>.
*   **Amount (Formula Property):** Derives values based on the 'Name' property <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>:
    *   If `Name` is "total actual expenses," gets actual expense value <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>.
    *   If `Name` is "total budgeted expenses," gets budgeted expense value <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>.
    *   If `Name` is "difference," gets the difference <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>.
    *   If `Name` is "change in percentage," calculates `Difference / Budgeted Expense` <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>.

### 5. Period of Expense Database
This database specifies monthly expenses for the entire year and helps categorize expenses by proportion <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>.
*   **Month (Title Property):** Specifies the month for each expense <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>.
*   **Expense Details (Relation Property):** Links to the Expense Details database to calculate expenses incurred each period <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>.
*   **Expenses for Each Month (Roll-up Property):** Derives actual expense values from the Expense Details database, summing them <a class="yt-timestamp" data-t="00:09:58">[00:10:00]</a>.
*   **Total Expenses (Roll-up Property):** Calculates total actual expense value from the Total Expenses database <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>.
*   **Proportion of the Total Expense (Formula Property):** Calculates `Expenses / Total Expenses` and displays as a percentage bar <a class="yt-timestamp" data-t="00:10:18">[00:10:18]</a>.

### 6. Expense Budget Classification Database
This database classifies expenses under six heads, providing details on total actual expenses, total budgeted expenses, differences, and percentage changes for each <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>.
*   **Title (Title Property):** Specifies the required properties for use <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>.
*   **Expense Source (Relation Property):** Relates to the Expense Source database, specifying individual expense heads <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>.
*   **Amount (Formula Property):** Derives total actual expenses, total budgeted expenses, and differences for specific heads (e.g., travel and transportation) <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>.
*   **Change in Percentage (Formula Property):** Calculates `Difference / Budgeted Expense` <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>.
*   **Actual Expense (Roll-up Property):** Derives expense values from the Expense Source database, calculating their sum <a class="yt-timestamp" data-t="00:11:45">[00:11:45]</a>.
*   **Budgeted Expenses (Roll-up Property):** Derives expense values from the Expense Source database, calculating their sum <a class="yt-timestamp" data-t="00:11:53">[00:11:53]</a>.
*   **Change in Percentage (Roll-up Property):** Derives the change in percentage from the Expense Source database <a class="yt-timestamp" data-t="00:12:11">[00:12:11]</a>.
*   **Difference (Roll-up Property):** Provides the difference between budgeted and actual expenses <a class="yt-timestamp" data-t="00:12:21">[00:12:21]</a>.
    > These columns should be repeated for all six expense heads <a class="yt-timestamp" data-t="00:12:27">[00:12:27]</a>.

### 7. Expense Categories Database
This database reflects expenses based on "needs," "wants," and "desires," allowing for further analysis <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>.
*   **Title (Title Property):** Represents the category types <a class="yt-timestamp" data-t="00:12:44">[00:12:44]</a>.
*   **Expense Details (Relation Property):** Links to the Expense Details database to capture all expenses related to needs, wants, and desires separately <a class="yt-timestamp" data-t="00:12:48">[00:12:48]</a>.
*   **Expenses Amount (Roll-up Property):** Derives actual expense amounts from the Expense Details database, calculating the sum for each category <a class="yt-timestamp" data-t="00:12:57">[00:12:57]</a>.
*   **Total Expenses (Roll-up Property):** Derives the sum of all combined expenses from the Total Expenses database <a class="yt-timestamp" data-t="00:13:12">[00:13:12]</a>.

## Dashboard Presentation

The primary dashboard of your Notion expense tracker brings all these databases together for easy viewing and management <a class="yt-timestamp" data-t="00:13:28">[00:13:28]</a>.

*   **Overview of Total Expenses:** Linked to the [[tracking_income_and_expenses_using_notion | Total Expenses database]] and displayed in a gallery view <a class="yt-timestamp" data-t="00:13:32">[00:13:32]</a>.
*   **Three Categories of Expenses:** Linked to the Expense Categories database and presented in a gallery format <a class="yt-timestamp" data-t="00:13:43">[00:13:43]</a>. To achieve a three-column layout, use the `/three column` command <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a>.
*   **Top 10 Highlights:** Linked to the Expense Details database and set in a list format <a class="yt-timestamp" data-t="00:13:57">[00:13:57]</a>.
    *   Recent expenses are sorted by `created time` in descending order <a class="yt-timestamp" data-t="00:14:07">[00:14:07]</a>.
    *   Least 10 expenses are sorted by `actual expenses` in ascending order <a class="yt-timestamp" data-t="00:14:11">[00:14:11]</a>.
    *   Top 10 expenses are sorted in descending order <a class="yt-timestamp" data-t="00:14:16">[00:14:16]</a>.
*   **Actual vs. Budgeted Expenses:** Linked to the Expense Budget Classification database and displayed in a gallery format <a class="yt-timestamp" data-t="00:14:25">[00:14:25]</a>.
*   **Expenses Overview (by Period):** Linked to the Period database and shown in a gallery format <a class="yt-timestamp" data-t="00:14:36">[00:14:36]</a>. Filters are applied for each quarter to show relevant months <a class="yt-timestamp" data-t="00:14:42">[00:14:42]</a>.
*   **Expenses Overview (by Source):** Linked to the Expense Source database, set in a gallery format, and repeated for all expense heads <a class="yt-timestamp" data-t="00:14:55">[00:14:55]</a>.
*   **Frequency of Expenses:** Linked to the [[setting_up_a_travel_expense_tracker_using_notion | Frequency of Expense database]] and displayed in a gallery format, with desired properties enabled <a class="yt-timestamp" data-t="00:15:05">[00:15:05]</a>.

This structured approach allows for effective [[using_notion_for_expense_management | expense management]] and [[tracking_personal_finances_in_notion | tracking personal finances in Notion]].