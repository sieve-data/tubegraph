---
title: Budget vs actual expense tracking
videoId: OV1faI8Z6yg
---

From: [[theaccountantguy]] <br/> 

This article describes a system for [[budgeting_and_tracking_expenses_in_notion | budgeting and tracking expenses]] that provides an [[budget_summary_and_tracking | overview of budgeted versus actual expenses]], differences, and percentage changes <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>. The tracker also highlights top and least expenses, as well as recent expenses incurred <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.

## Core Components for Tracking

The expense tracker features an "actual versus the budget expenses part" <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>, where expenses are organized into six primary categories <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>. For each category, the system displays:
*   Total budgeted expenses <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>
*   Total actual expenses <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>
*   The difference between actual and budgeted amounts <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>
*   The change in percentage <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>

Additionally, expenses are categorized by needs, wants, and desires for further analysis <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.

## Database Structure for [[budget_versus_actual_expense_analysis | Budget Versus Actual Expense Analysis]]

To build this expense tracker, seven databases are required <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>. Key databases supporting [[tracking_expenses_against_budget | tracking expenses against budget]] include:

### Expense Details Database
This database specifies individual expense details <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>. It includes:
*   **Expense details (Title property):** Shows individual expenses <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.
*   **Period of expense (Relation property):** Links to a period database specifying the month an expense was incurred <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>.
*   **Expense source (Relation property):** Links to the Expense Source database, categorizing the source of expense <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.
*   **Frequency of expense (Relation property):** Links to the Frequency of Expense database, indicating how often an expense is incurred <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.
*   **Expense categories (Relation property):** Links to the Expense Categories database, assigning categories like needs, wants, or desires <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
*   **Actual expense (Number property):** Records the actual amount incurred in US dollars <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.
*   **Budgeted expense (Number property):** Records the estimated budgeted expense for each month in US dollars <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.
*   The sum of actual and budgeted expenses is displayed at the bottom <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>.

### Expense Source Database
This database specifies six different sources of expenses and their analysis <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>. It includes:
*   **Source of expense (Title property):** Identifies one of the six expense categories <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>.
*   **Actual expense (Roll-up property):** Rolls up the sum of actual expenses from the Expense Details database <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>.
*   **Budgeted expense (Roll-up property):** Rolls up the sum of budgeted expenses from the Expense Details database <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>.
*   **Total expenses (Roll-up property):** Extracts total actual expenses from the Total Expenses database <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>.
*   **Difference (Formula property):** Calculates the difference between actual and budgeted expenses <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.
*   **Change in percentage (Formula property):** Calculates the difference divided by the budgeted expense amount, displayed as a percentage <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.

### Total Expenses Database
This database reflects the total expenses incurred for all six heads <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>, categorized as actual, budgeted, difference, and change <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>. It includes:
*   **Total actual expenses (Roll-up property):** Calculates the total expenses from the Expense Source database <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>.
*   **Total budgeted expense (Roll-up property):** Calculates the total budgeted expenses from the Expense Source database <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>.
*   **Amount (Formula property):** Derives values based on the property name: actual expense value for "total actual expenses", budgeted expense value for "total budgeted expenses", and the difference for "difference" <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>. This also calculates the change in percentage by dividing the difference by the budgeted expense value <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>.

### Expense Budget Classification Database
This database classifies expenses under six heads, providing [[tracking_actual_vs_budgeted_travel_expenses | actual versus budgeted travel expenses]], differences, and percentage changes for each <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a> <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>.
*   **Amount (Formula property):** Derives total actual expenses, total budgeted expenses, and the difference for each head <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>.
*   **Change in percentage (Formula property):** Calculates the difference divided by the budgeted expense <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>.
*   **Roll-up properties:** Derive actual expenses, budgeted expenses, differences, and change in percentage values from the Expense Source database <a class="yt-timestamp" data-t="00:11:45">[00:11:45]</a> <a class="yt-timestamp" data-t="00:11:53">[00:11:53]</a> <a class="yt-timestamp" data-t="00:12:11">[00:12:11]</a> <a class="yt-timestamp" data-t="00:12:21">[00:12:21]</a>. These columns are repeated for all six heads of expenses <a class="yt-timestamp" data-t="00:12:27">[00:12:27]</a>.

## Dashboard Presentation

The primary dashboard for this [[budget_and_actual_expense_tracking_in_notion | budget and actual expense tracking in Notion]] includes:
*   **Overview of Total Expenses:** Linked to the Total Expenses database, displayed in a gallery view <a class="yt-timestamp" data-t="00:13:32">[00:13:32]</a>.
*   **Actual vs. Budgeted Expenses:** Linked to the Expense Budget Classification database, displayed in a gallery format <a class="yt-timestamp" data-t="00:14:25">[00:14:25]</a>.
*   **Expenses Overview:** Linked to the Period database, displayed in a gallery format, with filters applied for each quarter <a class="yt-timestamp" data-t="00:14:36">[00:14:36]</a>.
*   **Expenses Overview Section (Percentage):** Linked to the Expense Source database, displayed in a gallery format and repeated for all expense heads <a class="yt-timestamp" data-t="00:14:55">[00:14:55]</a>.
*   **Top 10 Highlights:** Linked to the Expense Details database in a list format, sorted by:
    *   Recent expenses (created time, descending) <a class="yt-timestamp" data-t="00:14:07">[00:14:07]</a>
    *   Least 10 expenses (actual expenses, ascending) <a class="yt-timestamp" data-t="00:14:11">[00:14:11]</a>
    *   Top 10 expenses (actual expenses, descending) <a class="yt-timestamp" data-t="00:14:13">[00:14:13]</a>
*   **Expense Categories:** Three categories of expenses (needs, wants, desires) linked to the Expense Categories database in a three-column gallery format <a class="yt-timestamp" data-t="00:13:43">[00:13:43]</a>.
*   **Frequency of Expenses:** Linked to the Frequency of Expense database, displayed in a gallery format with desired properties enabled <a class="yt-timestamp" data-t="00:15:05">[00:15:05]</a>.

This comprehensive [[overview_of_budgeting_tracker_template | budgeting tracker template]] allows for detailed [[dynamic_updates_of_budgeted_and_actual_expenses | dynamic updates of budgeted and actual expenses]] and [[income_and_expense_tracking_with_budget_targets | income and expense tracking with budget targets]] <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>.