---
title: Using databases in Notion for expense tracking
videoId: OV1faI8Z6yg
---

From: [[theaccountantguy]] <br/> 

This article outlines how to build an expense tracker in Notion using seven interconnected databases to manage and analyze personal finances <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. The tracker provides an overview of total expenses, categorized spending, top expenses, and more <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

## Expense Tracker Overview
The Notion expense tracker offers several key features for [[using Notion for expense management|expense management]]:
*   **Total Expenses Overview** A summary of total budgeted expenses, total actual expenses, differences, and percentage change <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.
*   **Categorized Spending** Expenses are categorized as needs, desires, and wants <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.
*   **Top/Least/Recent Expenses** Highlights the top 10, least 10, and most recent expenses incurred during a period <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.
*   **Actual vs. Budgeted Expenses** Displays expenses divided into six heads, showing budgeted, actual, difference, and percentage change for each <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.
*   **Periodic Expenses Overview** Expenses categorized by months within four quarters, including total expenses incurred and their proportion to total expenses <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>.
*   **Percentage-Based Expenses Overview** Expenses categorized into six heads, showing total expenses and their proportion to the overall total <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.
*   **Frequency of Expenses** Indicates how frequently an expense is incurred (daily, one-time, weekly, monthly, quarterly, half-yearly, annually), along with the total amount and sources for each frequency type <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.

## Databases Required
To build this expense tracker, seven specific [[setting_up_and_using_databases_in_notion|databases are required]]:
1.  [[using_notions_expense_details_database|Expense Details]] <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>
2.  Expense Source <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>
3.  Frequency of Expenses <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>
4.  Total Expenses <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>
5.  Period of Expense <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>
6.  Expense Budget Classification <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>
7.  Expense Categories <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>

## Building the Databases

### 1. [[using_notions_expense_details_database|Expense Details Database]]
This database specifies details related to each individual expense <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.
*   **Expense Details** (Title property) Shows individual expenses incurred during a period <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.
*   **Period of Expense** (Relation property) Links to the "Period" database to specify the month of expense <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>.
*   **Expense Source** (Relation property) Links to the "Expense Source" database, specifying the source under which an expense is incurred <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.
*   **Frequency of Expense** (Relation property) Links to the "Frequency of Expense" database, indicating how frequently an expense occurs <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.
*   **Expense Categories** (Relation property) Links to the "Expense Categories" database, specifying the category for each individual source of expense <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
*   **Actual Expense** (Number property) Specifies the actual amount of expense incurred for the period, indicated in US dollars <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.
*   **Budgeted Expense** (Number property) The estimated budgeted expense for each month, specified in US dollars <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.
*   **Sum** The sum of actual and budgeted expenses can be found at the bottom of this database <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>.

### 2. Expense Source Database
This database specifies the six different sources of expenses <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>.
*   **Source of Expense** (Title property) Specifies one of the six heads of expenses <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>.
*   **Actual Expense** (Roll-up property) Rolled up from the [[using_notions_expense_details_database|Expense Details Database]], showing the sum of actual expense amounts <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>.
*   **Budgeted Expense** (Roll-up property) Rolled up from the [[using_notions_expense_details_database|Expense Details Database]], showing the sum of budgeted expense amounts <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>.
*   **Total Expenses** (Roll-up property) Derived from the "Total Expenses" database, extracting the total actual expenses amount as its original value <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>.
*   **Difference** (Formula property) Calculates the difference between actual expenses and budgeted expenses <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.
*   **Change in Percentage** (Formula property) Calculates the difference divided by the budgeted expense amount, represented as a percentage <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.

### 3. Frequency of Expenses Database
This database calculates how frequently expenses are incurred and provides further analysis <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>.
*   **Frequency** (Title property) Denotes each individual mode of frequency (e.g., daily, weekly) <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>.
*   **Relation Property** (Relation property) Related to the [[using_notions_expense_details_database|Expense Details Database]], linking different types of expenses to each frequency type <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>.
*   **Sources of Expense** (Formula property) Calculates the unique sources of expenses for each frequency type <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>.

### 4. Total Expenses Database
This database calculates the total expenses incurred during a period <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.
*   **Total Actual Expenses** (Roll-up property) Calculates total expenses from the "Expense Source" database, providing the sum value <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>.
*   **Total Budgeted Expense** (Roll-up property) Calculates total budgeted expenses from the "Expense Source" database, providing the sum value <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>.
*   **Amount** (Formula property) Derives values based on the name property:
    *   Gets actual expense value if the name property is "total actual expenses" <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>.
    *   Gets budgeted expense value if the name property is "total budgeted expenses" <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>.
    *   Gets the difference if the name property is "difference" <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>.
    *   Calculates the change in percentage (difference divided by budgeted expense value) if the name property is "change in percentage" <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>.

### 5. Period of Expense Database
This database specifies expenses for each month of the year and provides further analysis <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a>.
*   **Month Column** (Title property) Specifies the month for each expense <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>.
*   **Expense Details** (Relation property) Linked to the [[using_notions_expense_details_database|Expense Details Database]], calculating expenses incurred each period <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>.
*   **Expenses for Each Month** (Roll-up property) Derived from the [[using_notions_expense_details_database|Expense Details Database]], calculating the sum of actual expense values <a class="yt-timestamp" data-t="00:09:58">[00:09:58]</a>.
*   **Total Expenses** (Roll-up property) Calculated from the "Total Expenses" database, providing the total actual expense value <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>.
*   **Proportion of the Total Expense** (Formula property) Calculates expenses divided by total expenses, denoted as a percentage with a red bar <a class="yt-timestamp" data-t="00:10:18">[00:10:18]</a>.

### 6. Expense Budget Classification Database
This database classifies expenses under six heads and provides details on total actual expenses, total budgeted expenses, difference, and percentage change for each head <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>.
*   **Title Property** Specifies the required properties for use <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>.
*   **Relation Property** Links to the "Expense Source" database, where individual heads of expense are specified <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>.
*   **Amount** (Formula property) Derives the total actual expenses, total budgeted expenses, and the difference for specific expense heads (e.g., travel and transportation) <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>.
*   **Change in Percentage** (Formula property) Calculates the difference divided by the budgeted expense <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>.
*   **Actual Expenses** (Roll-up property) Derives values from the "Expense Source" database, calculating the sum of expense values <a class="yt-timestamp" data-t="00:11:45">[00:11:45]</a>.
*   **Budgeted Expenses** (Roll-up property) Derived from the "Expense Source" database, calculating the sum of expense values <a class="yt-timestamp" data-t="00:11:53">[00:11:53]</a>.
*   **Change in Percentage** (Roll-up property) Derived from the "Expense Source" database, showing the original value of the change in percentage <a class="yt-timestamp" data-t="00:12:11">[00:12:11]</a>.
*   **Difference Column** (Roll-up property) Provides the difference between budgeted and actual expenses <a class="yt-timestamp" data-t="00:12:21">[00:12:21]</a>.

### 7. Expense Categories Database
This database specifies the three types of expenses: needs, wants, and desires <a class="yt-timestamp" data-t="00:12:35">[00:12:35]</a>.
*   **First Column** (Title property) <a class="yt-timestamp" data-t="00:12:44">[00:12:44]</a>.
*   **Relation Column** (Relation property) Linked to the [[using_notions_expense_details_database|Expense Details Database]], capturing all expenses related to needs, wants, and desires separately <a class="yt-timestamp" data-t="00:12:48">[00:12:48]</a>.
*   **Expenses Amount** (Roll-up property) The actual expenses incurred, derived from the [[using_notions_expense_details_database|Expense Details Database]], calculating the sum for each individual type of expense <a class="yt-timestamp" data-t="00:12:57">[00:12:57]</a>.
*   **Total Expenses** (Roll-up property) Derived from the "Total Expenses" database, giving the sum of all combined expenses <a class="yt-timestamp" data-t="00:13:12">[00:13:12]</a>.

## Primary Dashboard and Presentation
The primary dashboard of the expense tracker integrates these databases for a comprehensive view <a class="yt-timestamp" data-t="00:13:27">[00:13:27]</a>:
*   **Overview of Total Expenses** Linked to the "Total Expenses" database, displayed in a gallery view <a class="yt-timestamp" data-t="00:13:32">[00:13:32]</a>.
*   **Three Categories of Expenses** Linked to the "Expense Categories" database, presented in a gallery format within a three-column layout <a class="yt-timestamp" data-t="00:13:43">[00:13:43]</a>.
*   **Top 10 Highlights** Linked to the [[using_notions_expense_details_database|Expense Details Database]], set out in a list format <a class="yt-timestamp" data-t="00:13:57">[00:13:57]</a>:
    *   Recent expenses are sorted by "created time" in descending order <a class="yt-timestamp" data-t="00:14:07">[00:14:07]</a>.
    *   Least 10 expenses are sorted by "actual expenses" in ascending order <a class="yt-timestamp" data-t="00:14:11">[00:14:11]</a>.
    *   Top 10 expenses are sorted in descending order <a class="yt-timestamp" data-t="00:14:15">[00:14:15]</a>.
*   **Actual versus Budgeted Expenses** Linked to the "Expense Budget Classification" database, displayed in a gallery format <a class="yt-timestamp" data-t="00:14:25">[00:14:25]</a>.
*   **Expenses Overview (Period-based)** Linked to the "Period" database, given in a gallery format. Filters are applied for each quarter to show necessary months <a class="yt-timestamp" data-t="00:14:36">[00:14:36]</a>.
*   **Expenses Overview (Source-based)** Linked to the "Expense Source" database, displayed in a gallery format and repeated for all expense heads <a class="yt-timestamp" data-t="00:14:55">[00:14:55]</a>.
*   **Frequency of Expenses** Linked to the "Frequency of Expense" database, given in a gallery format with desired properties enabled <a class="yt-timestamp" data-t="00:15:05">[00:15:05]</a>.