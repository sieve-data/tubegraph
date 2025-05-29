---
title: Databases setup in Notion for tracking expenses
videoId: OV1faI8Z6yg
---

From: [[theaccountantguy]] <br/> 

This article explains how to build an expense tracker in Notion, focusing on the seven necessary databases required for its functionality <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>. The tracker provides an overview of total expenses, including budgeted, actual, differences, and percentage changes <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>. It also categorizes expenses as needs, desires, and wants <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. Key highlights include top 10, least 10, and recent expenses <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.

The tracker further details actual versus budgeted expenses across six heads <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>, provides a monthly overview categorized into quarters <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>, and shows expense proportions in percentages <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>. Lastly, it tracks the frequency of expenses (daily, weekly, monthly, etc.) and their sources <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.

To build this [[creating_a_notion_expense_tracker | expense tracker]], seven distinct databases are necessary <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.

## Database Components for Tracking Expenses

The seven databases crucial for [[setting_up_notion_for_personal_finance_tracking | setting up Notion for personal finance tracking]] are:
1.  Expense Details <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>
2.  Expense Source <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>
3.  Frequency of Expenses <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>
4.  Total Expenses <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>
5.  Period of Expense <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>
6.  Expense Budget Classification <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>
7.  Expense Categories <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>

These databases are used to [[tracking_income_and_expenses_in_notion | track income and expenses in Notion]] and provide a comprehensive overview.

### 1. Expense Details Database

This database specifies the details for each individual expense incurred <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.

*   **Expense Details (Title Property):** Shows individual expenses <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.
*   **Period of Expense (Relation Property):** Links to the "Period Database," specifying the month an expense was incurred <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>.
*   **Expense Source (Relation Property):** Links to the "Expense Source Database," specifying the source category of the expense <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.
*   **Frequency of Expense (Relation Property):** Links to the "Frequency of Expense Database," indicating how frequently an expense occurs <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.
*   **Expense Categories (Relation Property):** Links to the "Expense Categories Database," specifying the category (needs, wants, desires) for each expense source <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
*   **Actual Expense (Number Property):** Records the actual amount of expense incurred in US dollars <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>. The sum of actual expenses is displayed at the bottom <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>.
*   **Budgeted Expense (Number Property):** Records the estimated budgeted expense for each month in US dollars <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>. The sum of budgeted expenses is displayed at the bottom <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>.

### 2. Expense Source Database

This database categorizes expenses under six different sources <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>.

*   **Source of Expense (Title Property):** Specifies one of the six expense categories <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>.
*   **Actual Expense (Roll-up Property):** Rolls up the sum of actual expense values from the "Expense Details" database <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>.
*   **Budgeted Expense (Roll-up Property):** Rolls up the sum of budgeted expense values from the "Expense Details" database <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>.
*   **Total Expenses (Roll-up Property):** Extracts the total actual expenses amount from the "Total Expenses" database <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>.
*   **Difference (Formula Property):** Calculates the difference between actual and budgeted expenses <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.
*   **Change in Percentage (Formula Property):** Calculates the difference divided by the budgeted expense, displayed as a percentage <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.

### 3. Frequency of Expenses Database

This database calculates how frequently expenses are incurred and performs further analysis <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>.

*   **Frequency (Title Property):** Specifies individual modes of frequency (e.g., daily, weekly) <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>.
*   **Relation Property:** Links to the "Expense Details" database, relating different types of expenses to each frequency <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>.
*   **Sources of Expense (Formula Property):** Calculates the unique sources of expenses for each frequency <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>.

### 4. Total Expenses Database

This database calculates the total expenses incurred during a period <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.

*   **Total Actual Expenses (Roll-up Property):** Calculates the sum of total expenses from the "Expense Source" database <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>.
*   **Total Budgeted Expense (Roll-up Property):** Calculates the sum of total budgeted expenses from the "Expense Source" database <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>.
*   **Amount (Formula Property):** Derives values based on the "Name" property (e.g., actual expense if "Total Actual Expenses," budgeted expense if "Total Budgeted Expenses," difference if "Difference," and change in percentage if "Change in Percentage") <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>. The change in percentage is calculated by dividing the difference by the budgeted expense value <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>.

### 5. Period of Expense Database

This database specifies expenses for each month and provides further analysis <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a>.

*   **Month (Title Property):** Specifies the month for each expense <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>.
*   **Expense Details (Relation Property):** Links to the "Expense Details" database, calculating expenses incurred each period <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>.
*   **Expenses for Each Month (Roll-up Property):** Derives the sum of actual expense values from the "Expense Details" database <a class="yt-timestamp" data-t="00:09:58">[00:09:58]</a>.
*   **Total Expenses (Roll-up Property):** Calculates the total actual expense value from the "Total Expenses" database <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>.
*   **Proportion of the Total Expense (Formula Property):** Calculates the expenses divided by the total expenses, displayed as a percentage in a red bar <a class="yt-timestamp" data-t="00:10:18">[00:10:18]</a>.
*   **Total Expenses (Relation Property):** Links to the "Total Expenses" database, deriving total expenses values <a class="yt-timestamp" data-t="00:10:36">[00:10:36]</a>.

### 6. Expense Budget Classification Database

This database classifies expenses under six heads and provides details on total actual expenses, total budgeted expenses, differences, and percentage changes for each head <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>. This is useful for [[using_notion_for_personal_and_business_expense_tracking | personal and business expense tracking]].

*   **Title Property:** Specifies the required properties for use <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>.
*   **Relation Property:** Links to the "Expense Source" database, where individual expense heads are specified <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>.
*   **Amount (Formula Property):** Derives total actual, total budgeted, and difference amounts for categories like travel and transportation <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>.
*   **Change in Percentage (Formula Property):** Calculates the difference divided by the budgeted expense <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>.
*   **Roll-up Properties:** Derives actual expense values, budgeted expense values, change in percentage, and difference from the "Expense Source" database, summing them where applicable <a class="yt-timestamp" data-t="00:11:45">[00:11:45]</a>. These columns need to be repeated for all six expense heads <a class="yt-timestamp" data-t="00:12:27">[00:12:27]</a>.

### 7. Expense Categories Database

This database specifies three types of expenses: needs, wants, and desires <a class="yt-timestamp" data-t="00:12:35">[00:12:35]</a>.

*   **Title Property:** The primary column for the categories <a class="yt-timestamp" data-t="00:12:44">[00:12:44]</a>.
*   **Relation Column:** Links to the "Expense Details" database, capturing expenses related to needs, wants, and desires separately <a class="yt-timestamp" data-t="00:12:48">[00:12:48]</a>.
*   **Expenses Amount (Roll-up Property):** Derives the sum of actual expense amounts from the "Expense Details" database for each expense type <a class="yt-timestamp" data-t="00:12:57">[00:12:57]</a>.
*   **Total Expenses (Roll-up Property):** Derives the sum of all combined expenses from the "Total Expenses" database <a class="yt-timestamp" data-t="00:13:12">[00:13:12]</a>.

## Dashboard Presentation

The primary dashboard for this [[using_notion_for_expense_management | expense management]] tracker integrates these databases to provide a comprehensive view <a class="yt-timestamp" data-t="00:13:25">[00:13:25]</a>.

*   **Overview of Total Expenses:** Linked to the "Total Expenses" database, displayed in a gallery view <a class="yt-timestamp" data-t="00:13:32">[00:13:32]</a>.
*   **Three Categories of Expenses:** Linked to the "Expense Categories" database, displayed in a gallery format within a three-column layout <a class="yt-timestamp" data-t="00:13:43">[00:13:43]</a>.
*   **Top 10 Highlights:** Linked to the "Expense Details" database, presented in a list format <a class="yt-timestamp" data-t="00:13:57">[00:13:57]</a>.
    *   Recent expenses are sorted by created time in descending order <a class="yt-timestamp" data-t="00:14:07">[00:14:07]</a>.
    *   Least 10 expenses are sorted by actual expenses in ascending order <a class="yt-timestamp" data-t="00:14:11">[00:14:11]</a>.
    *   Top 10 expenses are sorted in descending order <a class="yt-timestamp" data-t="00:14:16">[00:14:16]</a>.
*   **Actual vs. Budgeted Expenses:** Linked to the "Expense Budget Classification" database, displayed in a gallery format <a class="yt-timestamp" data-t="00:14:25">[00:14:25]</a>.
*   **Expenses Overview:** Linked to the "Period" database, displayed in a gallery format <a class="yt-timestamp" data-t="00:14:36">[00:14:36]</a>. Filters are applied for each quarter to show relevant months <a class="yt-timestamp" data-t="00:14:42">[00:14:42]</a>.
*   **Expenses Overview Section (by Source):** Linked to the "Expense Source" database, displayed in a gallery format and repeated for all expense heads <a class="yt-timestamp" data-t="00:14:55">[00:14:55]</a>.
*   **Frequency of Expenses:** Linked to the "Frequency of Expense" database, displayed in a gallery format with desired properties enabled <a class="yt-timestamp" data-t="00:15:05">[00:15:05]</a>.

This comprehensive [[using_databases_in_notion_for_financial_tracking | use of databases in Notion for financial tracking]] allows for detailed [[tracking_income_and_expenses_using_notion | tracking income and expenses using Notion]] and [[business_expense_tracking_with_notion | business expense tracking with Notion]].