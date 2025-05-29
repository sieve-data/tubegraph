---
title: Overview of total budgeted and actual expenses
videoId: OV1faI8Z6yg
---

From: [[theaccountantguy]] <br/> 

An expense tracker provides a comprehensive overview of financial outlays, highlighting the distinction between planned spending and actual expenditures <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>. This overview includes total budgeted expenses, total actual expenses, the differences between them, and the percentage change <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.

## Key Components

The system is designed to provide detailed insights into expenses, focusing on how actual spending aligns with budgeted figures.

### Total Expenses Overview
The primary dashboard prominently features an "overview of total expenses" linked to a dedicated database <a class="yt-timestamp" data-t="00:13:32">[00:13:32]</a>. This section presents:
*   Total budgeted expenses <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.
*   Total actual expenses <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.
*   Differences between actual and budgeted amounts <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.
*   Percentage change <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.

### Actual vs. Budgeted Expenses
A dedicated section focuses on [[calculating_budgeted_versus_actual_expenses | actual versus budgeted expenses]] broken down into six main categories or "heads" <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>. For each category, it displays:
*   Total budgeted expenses <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.
*   Total actual expenses <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>.
*   The difference <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.
*   The change in percentage <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.

## Database Structure for Calculation

The expense tracker utilizes several databases to support the calculation and display of budgeted vs. actual expenses:

### Total Expenses Database
This database reflects the [[managing_budget_and_actual_expenses | total expenses incurred]] across all six expense categories, categorized as actual, budgeted, difference, and change <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>.
*   **Total Actual Expenses:** A roll-up property from the Expense Source database, summing actual expense amounts <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>.
*   **Total Budgeted Expenses:** A roll-up property from the Expense Source database, summing budgeted expense amounts <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>.
*   **Amount Column:** A formula property that dynamically pulls the value based on the name property (e.g., actual expense value if the name is "total actual expenses", budgeted expense value if the name is "total budgeted expenses", etc.) <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>.
*   **Change in Percentage:** Calculated as the difference divided by the budgeted expense value <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>.

### Expense Details Database
This database specifies individual expense details <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>:
*   **Actual Expense:** A number property indicating the actual amount incurred in US dollars <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.
*   **Budgeted Expense:** A number property indicating the estimated budgeted expense for each month in US dollars <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.
*   The sum of actual and budgeted expenses is available at the bottom of this database <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>.

### Expense Source Database
This database specifies the six different sources of expenses <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>:
*   **Actual Expense:** A roll-up property from the Expense Details database, providing the sum of actual expenses for each source <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>.
*   **Budgeted Expense:** A roll-up property from the Expense Details database, providing the sum of budgeted expenses for each source <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>.
*   **Difference:** A formula property showing the difference between actual and budgeted expenses <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.
*   **Change in Percentage:** A formula property calculating the difference divided by the budgeted expense amount, displayed as a percentage <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.

### Expense Budget Classification Database
This database [[setting_and_tracking_budgeted_expenses | classifies expenses under six heads]] and provides detailed information on total actual expenses, total budgeted expenses, difference, and percentage change for each <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>.
*   **Amount:** A formula property deriving values like total actual expenses, total budgeted expenses, and the difference for each expense head <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>.
*   **Change in Percentage:** A formula property calculated as the difference divided by the budgeted expense <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>.
*   **Roll-up properties** are used to derive actual expenses, budgeted expenses, differences, and change in percentage from the Expense Source database <a class="yt-timestamp" data-t="00:11:45">[00:11:45]</a>.

This structured approach allows for detailed [[monitoring_budget_versus_actual_expenses | monitoring budget versus actual expenses]] and [[summary_of_expenses_and_budget_comparison | summary of expenses and budget comparison]].