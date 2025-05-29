---
title: Budget versus actual expense tracking
videoId: OV1faI8Z6yg
---

From: [[theaccountantguy]] <br/> 

An expense tracker can be built to monitor and manage spending effectively, allowing users to spend money as required <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>. This system provides a comprehensive [[overview_of_expenses_and_budget_tracking | overview of expenses]], including budgeted versus actual figures, differences, and percentage changes <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

## Expense Tracker Features

The expense tracker offers several key features for [[tracking_expenses_against_a_budget | tracking expenses against a budget]]:

*   **Total Expenses Overview** A summary showing total budgeted expenses, total actual expenses, the difference between them, and the percentage change <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.
*   **Categorized Expenses** Expenses are categorized as needs, desires, and wants <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.
*   **Top/Least/Recent Expenses Highlights** This section reflects the top 10 expenses, the least 10 expenses, and the most recent expenses incurred during a specific period <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.
*   **Actual vs. Budget Expenses** Expenses are divided into six distinct heads, showing total budgeted expenses, total actual expenses, the difference, and the percentage change <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.
*   **Expenses Overview by Period** Expenses are categorized by month and divided into four quarters. For each month, the total expenses incurred and their proportion to total expenses are shown <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>.
*   **Expenses Overview in Percentage** Expenses are categorized under six heads, displaying the total expenses and their proportion to the overall total <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.
*   **Frequency of Expenses** This feature indicates how frequently an expense is incurred, categorizing them as daily, one-time, weekly, monthly, quarterly, half-yearly, and annually. It also shows the total amount incurred and the sources of expenses for each frequency type <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.

## Building the Expense Tracker: Database Structure

To build this expense tracker, seven interconnected databases are required <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.

### 1. Expense Details Database
This database specifies the details of each individual expense <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>.
*   **Expense Details (Title Property)**: Shows individual expenses incurred <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.
*   **Period of Expense (Relation Property)**: Links to the Period Database, specifying the month for which an expense is incurred <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>.
*   **Expense Source (Relation Property)**: Links to the Expense Source database, specifying the source category of the expense <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.
*   **Frequency of Expense (Relation Property)**: Links to the Frequency of Expense database, indicating how frequently an expense occurs <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.
*   **Expense Categories (Relation Property)**: Links to the Expense Categories database, specifying the category (needs, wants, desires) for each expense source <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
*   **Actual Expense (Number Property)**: Specifies the actual amount incurred in US dollars <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.
*   **Budgeted Expense (Number Property)**: Specifies the estimated budgeted expense for each month in US dollars <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>.
*   **Sum of Actual and Budgeted Expenses**: Displayed at the bottom of the database <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>.

### 2. Expense Source Database
This database specifies the six different sources or heads under which expenses are incurred <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.
*   **Source of Expense (Title Property)**: Specifies one of the six expense heads <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>.
*   **Actual Expense (Roll-up Property)**: Rolled up from the Expense Details database, providing the sum of actual expenses for each source <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>.
*   **Budgeted Expense (Roll-up Property)**: Rolled up from the Expense Details database, providing the sum of budgeted expenses for each source <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>.
*   **Total Expenses (Roll-up Property)**: Derived from the Total Expenses database, extracting the total actual expenses amount as its original value <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>.
*   **Difference (Formula Property)**: Calculates the difference between actual expenses and budgeted expenses <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.
*   **Change in Percentage (Formula Property)**: Calculates the difference divided by the budgeted expense amount, represented as a percentage <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.

### 3. Frequency of Expenses Database
This database calculates how frequently expenses are incurred <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>.
*   **Frequency (Title Property)**: Specifies each individual mode of frequency (e.g., daily, monthly) <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>.
*   **Expense Details (Relation Property)**: Relates to the Expense Details database, linking different types of expenses to their frequency <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>.
*   **Sources of Expense (Formula Property)**: Calculates the unique sources of expenses for each frequency type <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>.

### 4. Total Expenses Database
This database reflects the total expenses incurred for all six heads, categorized by actual, budgeted, difference, and change in percentage for each <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>.
*   **Properties**: Includes Total Actual Expenses, Total Budgeted Expenses, Difference, and Change in Percentage <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>.
*   **Linking to Expense Heads**: All six expense heads are linked to each property <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>.
*   **Total Actual Expenses (Roll-up Property)**: Calculates total expenses from the Expense Source database, providing the sum value <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>.
*   **Total Budgeted Expense (Roll-up Property)**: Calculates total budgeted expenses from the Expense Source database, providing the sum value <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>.
*   **Amount (Formula Property)**: Derives values based on the "name" property:
    *   Actual expense value if the name property is "total actual expenses" <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>.
    *   Budgeted expense value if the name property is "total budgeted expenses" <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>.
    *   Difference if the name property is "difference" <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>.
    *   Change in percentage (difference divided by budgeted expense) if the name property is "changed in percentage" <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>.

### 5. Period of Expense Database
This database specifies monthly expenses for the entire year and helps categorize expenses with their proportion <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>.
*   **Month (Title Property)**: Specifies the month for each expense <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>.
*   **Expense Details (Relation Property)**: Relates to the Expense Details database, calculating expenses incurred each period <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>.
*   **Expenses for Each Month (Roll-up Property)**: Derived from the Expense Details database, calculating the sum of actual expense values <a class="yt-timestamp" data-t="00:09:58">[00:09:58]</a>.
*   **Total Expenses (Roll-up Property)**: Calculated from the Total Expense database, providing the total actual expense value <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>.
*   **Proportion of the Total Expense (Formula Property)**: Calculates expenses divided by total expenses, denoted as a percentage <a class="yt-timestamp" data-t="00:10:19">[00:10:19]</a>.
*   **Total Expenses (Relation Property)**: Linked to the Total Expenses database, deriving total expenses value <a class="yt-timestamp" data-t="00:10:36">[00:10:36]</a>.

### 6. Expense Budget Classification Database
This database classifies expenses under six heads and provides details on [[tracking_budgeted_vs_actual_expenses | total actual expenses]], [[budgeted_expenses_summary | total budgeted expenses]], differences, and percentage changes for each head <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>.
*   **Title Property**: Specifies required properties for use <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>.
*   **Relation Property**: Relates to the Expense Source database, specifying individual heads of expense <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>.
*   **Amount (Formula Property)**: Derives total actual expenses, total budgeted expenses, and the difference for specific categories like "travel and transportation" <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>.
*   **Change in Percentage (Formula Property)**: Calculates the difference divided by the budgeted expense <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>.
*   **Actual Expenses (Roll-up Property)**: Derives actual expense values from the Expense Source database, calculating their sum <a class="yt-timestamp" data-t="00:11:45">[00:11:45]</a>.
*   **Budgeted Expenses (Roll-up Property)**: Derives budgeted expense values from the Expense Source database, calculating their sum <a class="yt-timestamp" data-t="00:11:53">[00:11:53]</a>.
*   **Change in Percentage (Roll-up Property)**: Derived from the Expense Source database, showing the original value for the change in percentage <a class="yt-timestamp" data-t="00:12:11">[00:12:11]</a>.
*   **Difference Column (Roll-up Property)**: Provides the difference between budgeted and actual expenses <a class="yt-timestamp" data-t="00:12:21">[00:12:21]</a>.

### 7. Expense Categories Database
This database reflects expenses based on three types: needs, wants, and desires <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>.
*   **First Column (Title Property)**: Represents the categories (needs, wants, desires) <a class="yt-timestamp" data-t="00:12:44">[00:12:44]</a>.
*   **Relation Column**: Relates to the Expense Details database, capturing expenses related to needs, wants, and desires separately <a class="yt-timestamp" data-t="00:12:48">[00:12:48]</a>.
*   **Expenses Amount (Roll-up Property)**: Derived from the Expense Details database, providing the sum of actual expenses for each category <a class="yt-timestamp" data-t="00:12:57">[00:12:57]</a>.
*   **Total Expenses (Roll-up Property)**: Derived from the Total Expenses database, providing the sum of all combined expenses <a class="yt-timestamp" data-t="00:13:12">[00:13:12]</a>.

## Dashboard Presentation
The primary dashboard integrates these databases for a comprehensive [[tracking_income_and_expenses_effectively | overview of income and expenses]].
*   **Overview of Total Expenses**: Linked to the Total Expenses database and displayed in a gallery view <a class="yt-timestamp" data-t="00:13:32">[00:13:32]</a>.
*   **Three Categories of Expenses**: Linked to the Expense Categories database, presented in a gallery format within a three-column layout <a class="yt-timestamp" data-t="00:13:43">[00:13:43]</a>.
*   **Top 10 Highlights**: Linked to the Expense Details database and set out in a list format <a class="yt-timestamp" data-t="00:13:57">[00:13:57]</a>.
    *   Recent expenses are sorted by created time in descending order <a class="yt-timestamp" data-t="00:14:07">[00:14:07]</a>.
    *   Least 10 expenses are sorted by actual expenses in ascending order <a class="yt-timestamp" data-t="00:14:11">[00:14:11]</a>.
    *   Top 10 expenses are sorted in descending order <a class="yt-timestamp" data-t="00:14:16">[00:14:16]</a>.
*   **Actual vs. Budgeted Expenses**: Linked to the Expense Budget Classification database and set out in a gallery format <a class="yt-timestamp" data-t="00:14:25">[00:14:25]</a>.
*   **Expenses Overview**: Linked to the Period database and presented in a gallery format, with filters applied for each quarter <a class="yt-timestamp" data-t="00:14:36">[00:14:36]</a>.
*   **Expenses Overview Section (by Source)**: Linked to the Expense Source database, set out in a gallery format, and repeated for all six heads of expenses <a class="yt-timestamp" data-t="00:14:55">[00:14:55]</a>.
*   **Frequency of Expenses**: Linked to the Frequency of Expense database, displayed in a gallery format, with desired properties enabled <a class="yt-timestamp" data-t="00:15:05">[00:15:05]</a>.