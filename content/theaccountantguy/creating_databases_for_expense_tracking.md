---
title: Creating Databases for Expense Tracking
videoId: OV1faI8Z6yg
---

From: [[theaccountantguy]] <br/> 

This article outlines how to build an expense tracker, including how to categorize and analyze spending habits <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>. The tracker provides an [[overview_of_business_expense_tracker | overview of total expenses]], showing budgeted and actual amounts, differences, and percentage changes <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>. Expenses are categorized as needs, desires, and wants <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. It also highlights top 10, least 10, and recent expenses <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.

The tracker includes sections for actual versus budgeted expenses divided into six heads <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>, expenses overview categorized by months and quarters <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>, and expenses overview in percentage for each of the six heads <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>. Additionally, it tracks the frequency of expenses (daily, one-time, weekly, monthly, quarterly, half-yearly, annually) <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.

## Building the Expense Tracker

To build this [[using_notion_for_expense_tracking | expense tracker]], seven databases are required <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.

### 1. Expense Details Database

This database specifies details for each individual expense incurred <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>, such as:
*   **Expense Details** (Title property): Shows individual expenses incurred <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.
*   **Period of Expense** (Relation property): Links to the "period database" to specify the month for each expense <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>.
*   **Expense Source** (Relation property): Links to the "expense source database" to specify the source of expense <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.
*   **Frequency of Expense** (Relation property): Links to the "frequency of expense database" to indicate how frequently an expense is incurred <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.
*   **Expense Categories** (Relation property): Links to the "expense categories database" to specify the category for each expense source <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
*   **Actual Expense** (Number property): Specifies the actual amount incurred in US dollars <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.
*   **Budgeted Expense** (Number property): The estimated budgeted expense for each month in US dollars <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.
The sum of actual and budgeted expenses is shown at the bottom <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>.

### 2. Expense Source Database

This database specifies the six different sources under which an expense is incurred <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>, including:
*   **Source of Expense** (Title property): Specifies one of the six expense heads <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>.
*   **Actual Expense** (Roll-up property): Rolled up from the "expense details database" to give the sum of actual expenses <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>.
*   **Budgeted Expense** (Roll-up property): Rolled up from the "expense details database" to give the sum of budgeted expenses <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>.
*   **Total Expenses** (Roll-up property): Derived from the "total expenses database," extracting the total actual expenses amount <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>.
*   **Difference** (Formula property): Shows the difference between actual expenses and budgeted expenses <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.
*   **Change in Percentage** (Formula property): Calculated as the difference divided by the budgeted expense amount, represented as a percentage <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.

### 3. Frequency of Expenses Database

This database calculates how frequently an expense is incurred <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>, with properties like:
*   **Frequency** (Title property): Specifies each individual mode of frequency <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>.
*   **Expense Details** (Relation property): Relates to the "expense details database" to link different types of expenses to each frequency type <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>.
*   **Sources of Expense** (Formula property): Calculates the unique sources of expenses for each frequency <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>.

### 4. Total Expenses Database

This database calculates the total expenses incurred during a period <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>, with properties:
*   **Total Actual Expenses** (Roll-up property): Calculates total expenses from the "expense source database" as a sum <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>.
*   **Total Budgeted Expense** (Roll-up property): Calculates total budgeted expenses from the "expense source database" as a sum <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>.
*   **Amount** (Formula property): Derives values based on the name property: actual expense if "total actual expenses," budgeted expense if "total budgeted expenses," difference if "difference," and change in percentage if "change in percentage" (calculated as difference over budgeted expense) <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>.

### 5. Period of Expense Database

This database specifies expenses for each month and provides further analysis <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a>, including:
*   **Month** (Title property): Specifies the month for each expense <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>.
*   **Expense Details** (Relation property): Relates to the "expense details database" to calculate expenses incurred each period <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>.
*   **Expenses for Each Month** (Roll-up property): Derived from the "expense details database," calculating the sum of actual expense values <a class="yt-timestamp" data-t="00:09:58">[00:09:58]</a>.
*   **Total Expenses** (Roll-up property): Calculated from the "total expense database" to provide the total actual expense value <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>.
*   **Proportion of the Total Expense** (Formula property): Calculates expenses divided by total expenses, denoted as a percentage <a class="yt-timestamp" data-t="00:10:18">[00:10:18]</a>.

### 6. Expense Budget Classification Database

This database classifies expenses under six heads and provides details on total actual expenses, total budgeted expenses, differences, and change in percentage for each head <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>. Properties include:
*   **Title property**: Specifies required properties for use <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>.
*   **Relation property**: Links to the "expense source database" where individual heads of expense are specified <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>.
*   **Amount** (Formula property): Derives total actual, total budgeted, and difference amounts for specific expense heads (e.g., travel and transportation) <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>.
*   **Change in Percentage** (Formula property): Calculated as the difference divided by the budgeted expense <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>.
*   **Actual Expenses** (Roll-up property): Derives values from the "expense source database" and calculates their sum <a class="yt-timestamp" data-t="00:11:45">[00:11:45]</a>.
*   **Budgeted Expenses** (Roll-up property): Also a roll-up property related to the "expense source database," calculating the sum of budgeted expense values <a class="yt-timestamp" data-t="00:11:53">[00:11:53]</a>.
*   **Change in Percentage** (Roll-up property): Derived from the "expense source database," showing the original value for change in percentage <a class="yt-timestamp" data-t="00:12:11">[00:12:11]</a>.
*   **Difference** (Roll-up property): Shows the difference between budgeted and actual expenses <a class="yt-timestamp" data-t="00:12:21">[00:12:21]</a>. These columns are repeated for all six expense heads <a class="yt-timestamp" data-t="00:12:27">[00:12:27]</a>.

### 7. Expense Categories Database

This database specifies the three types of expenses: needs, wants, and desires <a class="yt-timestamp" data-t="00:12:35">[00:12:35]</a>.
*   **Title property**: Defines the category <a class="yt-timestamp" data-t="00:12:44">[00:12:44]</a>.
*   **Relation column**: Links to the "expense details database" to capture expenses related to needs, wants, and desires separately <a class="yt-timestamp" data-t="00:12:48">[00:12:48]</a>.
*   **Expenses Amount** (Roll-up property): Represents actual expenses incurred, derived from the "expense details database," calculating the sum for each type of expense <a class="yt-timestamp" data-t="00:12:57">[00:12:57]</a>.
*   **Total Expenses** (Roll-up property): Derived from the "total expenses database," showing the sum of all combined expenses <a class="yt-timestamp" data-t="00:13:12">[00:13:12]</a>.

## Primary Dashboard Presentation

The primary dashboard of the [[automating_expenses_tracking_through_databases | expense tracker]] presents these databases in various views for [[using_databases_for_financial_tracking_in_notion | financial tracking]] and [[budgeting_and_tracking_business_expenses | budgeting]]:
*   **Overview of Total Expenses**: Linked to the "total expenses database" and displayed in a gallery view <a class="yt-timestamp" data-t="00:13:32">[00:13:32]</a>.
*   **Expense Categories**: Three categories linked to the "expense categories database" in a gallery format, arranged in a three-column layout <a class="yt-timestamp" data-t="00:13:43">[00:13:43]</a>. This allows for [[customizing_expense_tracking_for_personal_needs | customizing expense tracking for personal needs]] by categorizing expenses.
*   **Top 10 Highlights**: Linked to the "expense details database" in a list format <a class="yt-timestamp" data-t="00:14:03">[00:14:03]</a>. Recent expenses are sorted by created time (descending), least 10 by actual expenses (ascending), and top 10 by actual expenses (descending) <a class="yt-timestamp" data-t="00:14:07">[00:14:07]</a>.
*   **Actual versus Budgeted Expenses**: Linked to the "expense budget classification database" in a gallery format <a class="yt-timestamp" data-t="00:14:25">[00:14:25]</a>.
*   **Expenses Overview**: Linked to the "period database" in a gallery format, with filters applied for each quarter <a class="yt-timestamp" data-t="00:14:36">[00:14:36]</a>.
*   **Expenses Overview (Percentage)**: Linked to the "expense source database" in a gallery format, repeated for all expense heads <a class="yt-timestamp" data-t="00:14:55">[00:14:55]</a>. This is part of [[creating_and_categorizing_expenses_in_notion | creating and categorizing expenses]].
*   **Frequency of Expenses**: Linked to the "frequency of expense database" in a gallery format <a class="yt-timestamp" data-t="00:15:05">[00:15:05]</a>.

This comprehensive setup allows for detailed [[automating_expenses_tracking_through_databases | automating expenses tracking through databases]] and analysis.