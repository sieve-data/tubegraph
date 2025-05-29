---
title: Creating databases for an expense tracker in Notion
videoId: OV1faI8Z6yg
---

From: [[theaccountantguy]] <br/> 

This article details how to build an [[using_notion_as_an_expense_tracker | expense tracker]] in Notion, focusing on the construction of its underlying [[setting_up_databases_in_notion | databases]] to effectively track and analyze spending <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>. The tracker provides an overview of total budgeted and actual expenses, differences, and percentage changes, with expenses categorized by needs, desires, and wants <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>. It also highlights top 10, least 10, and recent expenses <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>, and presents actual versus budget expenses divided into six heads <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>. Expense overviews are categorized by months within four quarters <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>, and by six heads in percentage <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>. Finally, it tracks expense frequency (daily, weekly, monthly, quarterly, half-yearly, annually) <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.

## Building the Expense Tracker: Required Databases

To build this comprehensive [[using_notion_as_an_expense_tracker | expense tracker]], seven distinct [[creating_a_database_in_notion | databases]] must be constructed <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>:

1.  Expense Details <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>
2.  Expense Source <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>
3.  Frequency of Expenses <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>
4.  Total Expenses <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>
5.  Period of Expense <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>
6.  Expense Budget Classification <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>
7.  Expense Categories <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>

### 1. Expense Details Database

This [[creating_a_database_in_notion | database]] specifies the details for each individual expense incurred <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.

*   **Expense Details** (Title Property): Shows individual expenses <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.
*   **Period of Expense** (Relation Property): Linked to the "Period Database," specifying the month for each expense <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>.
*   **Expense Source** (Relation Property): Linked to the "Expense Source Database," specifying the source head of the expense <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.
*   **Frequency of Expense** (Relation Property): Linked to the "Frequency of Expense Database," indicating how frequently an expense is incurred <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.
*   **Expense Categories** (Relation Property): Linked to the "Expense Categories Database," specifying the category (needs, wants, desires) for each expense source <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
*   **Actual Expense** (Number Property): Specifies the actual amount incurred in US dollars <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.
*   **Budgeted Expense** (Number Property): Specifies the estimated budgeted expense for each month in US dollars <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>.

The sum of actual and budgeted expenses is displayed at the bottom <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>.

### 2. Expense Source Database

This [[creating_a_database_in_notion | database]] specifies the six different sources (heads) under which expenses are incurred <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>.

*   **Source of Expense** (Title Property): Specifies one of the six expense heads <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>.
*   **Actual Expense** (Roll-up Property): Rolls up actual expense amounts from the "Expense Details Database," summed <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>.
*   **Budgeted Expense** (Roll-up Property): Rolls up budgeted expense amounts from the "Expense Details Database," summed <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>.
*   **Total Expenses** (Roll-up Property): Derived from the "Total Expenses Database," extracting the total actual expenses amount as its original value <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>.
*   **Difference** (Formula Property): Calculates the difference between actual expenses and budgeted expenses <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.
*   **Change in Percentage** (Formula Property): Calculates the difference divided by the budgeted expense amount, formatted as a percentage <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.

### 3. Frequency of Expenses Database

This [[creating_a_database_in_notion | database]] calculates how frequently an expense is incurred and provides further analysis <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>.

*   **Frequency** (Title Property): Specifies each individual mode of frequency (e.g., daily, weekly) <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>.
*   **Relation Property** (Relation Property): Linked to the "Expense Details Database," relating different types of expenses to each frequency type <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>.
*   **Sources of Expense** (Formula Property): Calculates the unique sources of expenses for each frequency <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>. For example, if "commutation expenses" appears twice for a frequency, it's counted as one unique source <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>.

### 4. Total Expenses Database

This [[creating_a_database_in_notion | database]] tracks the total expenses incurred during a period <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.*   **Name Property** (Title Property): Used to categorize entries as "Total Actual Expenses," "Total Budgeted Expenses," "Difference," and "Change in Percentage" <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>.
*   **Total Actual Expenses** (Roll-up Property): Calculates the total actual expenses from the "Expense Source Database," summed <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>.
*   **Total Budgeted Expense** (Roll-up Property): Calculates the total budgeted expenses from the "Expense Source Database," summed <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>.
*   **Amount** (Formula Property): Derives values based on the "Name Property" <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>.
    *   If "Name Property" is "Total Actual Expenses," it gets the actual expense value <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>.
    *   If "Name Property" is "Total Budgeted Expenses," it gets the budgeted expense value <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>.
    *   If "Name Property" is "Difference," it calculates the difference <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>.
    *   If "Name Property" is "Change in Percentage," it calculates this as the difference divided by the budgeted expense value <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>.

### 5. Period of Expense Database

This [[setting_up_a_database_in_notion | database]] specifies expenses for each month of the year and allows for further analysis <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a>.

*   **Month Column** (Title Property): Specifies the month for each expense <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>.
*   **Expense Details** (Relation Property): Linked to the "Expense Details Database," calculating expenses incurred per period <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>.
*   **Expenses for Each Month** (Roll-up Property): Derived from the "Expense Details Database," calculating the sum of actual expense values <a class="yt-timestamp" data-t="00:09:58">[00:09:58]</a>.
*   **Total Expenses** (Roll-up Property): Calculated from the "Total Expense Database," providing the original value of total actual expenses <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>.
*   **Proportion of the Total Expense** (Formula Property): Calculates the expenses divided by the total expenses, denoted as a percentage <a class="yt-timestamp" data-t="00:10:18">[00:10:18]</a>.

### 6. Expense Budget Classification Database

This [[creating_a_database_in_notion | database]] classifies expenses under six heads and provides details on total actual expenses, total budgeted expenses, differences, and percentage changes for each head <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>.

*   **Title Property**: Specifies the required properties for use <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>.
*   **Relation Property**: Linked to the "Expense Source Database," specifying individual heads of expense <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>.
*   **Amount** (Formula Property): Derives total actual expenses, total budgeted expenses, and the difference for specific expense heads like travel and transportation <a class="yt-timestamp" data-t="00:11:15">[00:11:15]</a>.
*   **Change in Percentage** (Formula Property): Calculates the difference divided by the budgeted expense <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>.
*   **Actual Expenses** (Roll-up Property): Derives actual expense values from the "Expense Source Database," summed <a class="yt-timestamp" data-t="00:11:45">[00:11:45]</a>.
*   **Budgeted Expenses** (Roll-up Property): Derives budgeted expense values from the "Expense Source Database," summed <a class="yt-timestamp" data-t="00:11:53">[00:11:53]</a>.
*   **Change in Percentage** (Roll-up Property): Derives the change in percentage from the "Expense Source Database," showing the original value <a class="yt-timestamp" data-t="00:12:11">[00:12:11]</a>.
*   **Difference** (Roll-up Property): Provides the difference between budgeted and actual expenses <a class="yt-timestamp" data-t="00:12:21">[00:12:21]</a>.

These columns are repeated for all six expense heads <a class="yt-timestamp" data-t="00:12:27">[00:12:27]</a>.

### 7. Expense Categories Database

This [[setting_up_a_database_in_notion | database]] specifies the three types of expenses: needs, wants, and desires <a class="yt-timestamp" data-t="00:12:35">[00:12:35]</a>.

*   **First Column** (Title Property): The initial title property <a class="yt-timestamp" data-t="00:12:44">[00:12:44]</a>.
*   **Relation Column** (Relation Property): Linked to the "Expense Details Database," capturing all expenses related to needs, wants, and desires separately <a class="yt-timestamp" data-t="00:12:48">[00:12:48]</a>.
*   **Expenses Amount** (Roll-up Property): Represents the actual expenses incurred, derived from the "Expense Details Database," calculating the sum for each individual expense type <a class="yt-timestamp" data-t="00:12:57">[00:12:57]</a>.
*   **Total Expenses** (Roll-up Property): Derived from the "Total Expenses Database," providing the sum of all combined expenses <a class="yt-timestamp" data-t="00:13:12">[00:13:12]</a>.

## Dashboard Presentation

The primary dashboard of the [[using_notion_as_an_expense_tracker | expense tracker]] presents these [[setting_up_databases_in_notion | databases]] effectively <a class="yt-timestamp" data-t="00:13:28">[00:13:28]</a>:

*   **Overview of Total Expenses**: Linked to the "Total Expenses Database" and displayed in a gallery view <a class="yt-timestamp" data-t="00:13:32">[00:13:32]</a>.
*   **Three Categories of Expenses**: Linked to the "Expense Categories Database" in a gallery format, arranged in a three-column layout <a class="yt-timestamp" data-t="00:13:43">[00:13:43]</a>.
*   **Top 10 Highlights**: Linked to the "Expense Details Database" in a list format <a class="yt-timestamp" data-t="00:13:57">[00:13:57]</a>.
    *   Recent expenses are sorted by created time in descending order <a class="yt-timestamp" data-t="00:14:07">[00:14:07]</a>.
    *   Least 10 expenses are sorted by actual expenses in ascending order <a class="yt-timestamp" data-t="00:14:11">[00:14:11]</a>.
    *   Top 10 expenses are sorted in descending order <a class="yt-timestamp" data-t="00:14:16">[00:14:16]</a>.
*   **Actual vs. Budgeted Expenses**: Linked to the "Expense Budget Classification Database" in a gallery format <a class="yt-timestamp" data-t="00:14:25">[00:14:25]</a>.
*   **Expenses Overview**: Linked to the "Period Database" in a gallery format, with filters applied for each quarter to show relevant months <a class="yt-timestamp" data-t="00:14:36">[00:14:36]</a>.
*   **Expenses Overview Section**: Linked to the "Expense Source Database" in a gallery format, repeated for all expense heads <a class="yt-timestamp" data-t="00:14:55">[00:14:55]</a>.
*   **Frequency of Expenses**: Linked to the "Frequency of Expense Database" in a gallery format with desired properties enabled <a class="yt-timestamp" data-t="00:15:05">[00:15:05]</a>.

This comprehensive setup allows for robust [[budgeting_and_tracking_expenses_in_notion | budgeting and tracking expenses in Notion]], aiding in [[setting_up_a_personal_finance_tracker_in_notion | personal finance tracking]] and providing detailed [[creating_a_database_in_notion_for_calculations | calculations]] for spending analysis.