---
title: Overview and Analysis of Expenses in Notion
videoId: OV1faI8Z6yg
---

From: [[theaccountantguy]] <br/> 

This article describes how to [[notion_expense_tracker_setup | build an expense tracker]] and [[how_to_track_income_and_expenses_using_notion | track income and expenses using Notion]], allowing users to [[budgeting_and_tracking_expenses_in_notion | budget and track expenses]] and [[using_notion_for_expense_management | manage finances effectively]] <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. The tracker provides a comprehensive [[overview_of_notion_budget_tracker_template | overview]] of financial data, including budgeted expenses, actual expenses, differences, and percentage changes <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

## Key Features and Analysis

The expense tracker offers several views for detailed analysis:
*   **Total Expenses Overview** A summary showing total budgeted expenses, total actual expenses, the difference, and change in percentage <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.
*   **Categorized Expenses** Expenses are [[categorizing_expenses_in_notion | categorized]] into "needs," "desires," and "wants" <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.
*   **Top, Least, and Recent Expenses** Highlights the top 10, least 10, and most recent expenses incurred over a period <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.
*   **Actual vs. Budget Expenses** Displays expenses divided into six predefined categories or "heads" <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>. This section shows the total budgeted expenses, total actual expenses, difference, and percentage change for each head <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.
*   **Expenses Overview by Period** Categorizes expenses by month, further divided into four quarters, showing total expenses and their proportion to overall total expenses <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>.
*   **Expenses Overview in Percentage** Presents expenses [[categorizing_expenses_in_notion | categorized]] into six heads, showing total expenses and their proportion in percentage <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.
*   **Frequency of Expenses** Indicates how often an expense is incurred, categorizing it as daily, one-time, weekly, monthly, quarterly, half-yearly, or annually <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>. This section also lists the total amount incurred and sources for each frequency <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.

## Database Structure for the Expense Tracker

To [[notion_expense_tracker_setup | build this expense tracker]], seven distinct databases are required <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.

### 1. Expense Details Database
This database specifies details related to each individual expense <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>:
*   **Expense Details (Title)**: Shows individual expenses <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.
*   **Period of Expense**: A relation property linking to the "Period Database," specifying the month an expense was incurred <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>.
*   **Expense Source**: A relation property linking to the "Expense Source Database," indicating the source or head of expense <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.
*   **Frequency of Expense**: A relation property linking to the "Frequency of Expense Database," indicating how frequently an expense is incurred <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.
*   **Expense Categories**: A relation property linking to the "Expense Categories Database," specifying the category (needs, wants, desires) for each source <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
*   **Actual Expense**: A number property indicating the actual amount incurred in USD <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.
*   **Budgeted Expense**: A number property indicating the estimated budgeted expense for each month in USD <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.
*   **Sum of Actual and Budgeted Expenses**: Displayed at the bottom of the database <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>.

### 2. Expense Source Database
This database specifies the six different sources or heads of expenses <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>:
*   **Source of Expense (Title)**: Specifies one of the six heads of expenses <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>.
*   **Actual Expense**: A roll-up property from the "Expense Details Database," summing actual expense amounts <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>.
*   **Budgeted Expense**: A roll-up property from the "Expense Details Database," summing budgeted expense amounts <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>.
*   **Total Expenses**: A roll-up property from the "Total Expenses Database," extracting total actual expenses <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>.
*   **Difference**: A formula calculating the difference between actual and budgeted expenses <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.
*   **Change in Percentage**: A formula calculating the difference divided by the budgeted expense, formatted as a percentage <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.

### 3. Frequency of Expenses Database
This database showcases how frequently an expense is incurred <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>:
*   **Frequency (Title)**: Specifies individual modes of frequency (e.g., daily, weekly) <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>.
*   **Expense Details**: A relation property linking to the "Expense Details Database," relating different expense types to their frequency <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>.
*   **Sources of Expense**: A formula calculating the unique sources of expenses for each frequency <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>.

### 4. Total Expenses Database
This database reflects the total expenses incurred for all six heads, categorizing them as actual, budgeted, difference, and change <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>:
*   **Name (Title)**: Specifies the property name (e.g., "Total Actual Expenses", "Total Budgeted Expenses", "Difference", "Change in Percentage") <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>.
*   **Total Actual Expenses**: A roll-up property from the "Expense Source Database," summing total actual expenses <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>.
*   **Total Budgeted Expense**: A roll-up property from the "Expense Source Database," summing total budgeted expenses <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>.
*   **Amount**: A formula property deriving values based on the "Name" property:
    *   Actual expense value if "Total Actual Expenses" <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>.
    *   Budgeted expense value if "Total Budgeted Expenses" <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>.
    *   Difference if "Difference" <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>.
    *   Calculates change in percentage (difference divided by budgeted expense) if "Change in Percentage" <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>.

### 5. Period of Expense Database
This database specifies monthly expenses for the entire year and helps [[categorizing_expenses_in_notion | categorize expenses]] with proportions <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>:
*   **Month (Title)**: Specifies the month for each expense <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>.
*   **Expense Details**: A relation property linking to the "Expense Details Database," calculating expenses incurred each period <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>.
*   **Expenses for Each Month**: A roll-up property from the "Expense Details Database," summing actual expense values <a class="yt-timestamp" data-t="00:09:58">[00:09:58]</a>.
*   **Total Expenses**: A roll-up property from the "Total Expenses Database," providing the total actual expense value <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>.
*   **Proportion of the Total Expense**: A formula calculating the expenses divided by the total expenses, shown as a percentage bar <a class="yt-timestamp" data-t="00:10:19">[00:10:19]</a>.

### 6. Expense Budget Classification Database
This database classifies expenses under the six heads, providing details on total actual, total budgeted expenses, differences, and percentage changes for each <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>:
*   **Title Property**: Specifies the required properties for use <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>.
*   **Relation to Expense Source Database**: Links to the "Expense Source Database," specifying individual heads of expense <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>.
*   **Amount**: A formula property deriving total actual expenses, total budgeted expenses, and the difference for specific expense heads <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>.
*   **Change in Percentage**: A formula calculating the difference divided by the budgeted expense <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>.
*   **Actual Expenses (Roll-up)**: A roll-up property deriving values from the "Expense Source Database," summing expense values <a class="yt-timestamp" data-t="00:11:45">[00:11:45]</a>.
*   **Budgeted Expenses (Roll-up)**: A roll-up property from the "Expense Source Database," summing budgeted expense values <a class="yt-timestamp" data-t="00:11:53">[00:11:53]</a>.
*   **Change in Percentage (Roll-up)**: A roll-up property from the "Expense Source Database," showing the original change in percentage <a class="yt-timestamp" data-t="00:12:11">[00:12:11]</a>.
*   **Difference (Roll-up)**: A roll-up property showing the difference between budgeted and actual expenses <a class="yt-timestamp" data-t="00:12:21">[00:12:21]</a>. These columns are repeated for all six heads of expenses <a class="yt-timestamp" data-t="00:12:27">[00:12:27]</a>.

### 7. Expense Categories Database
This database reflects expenses based on three types: needs, wants, and desires <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>:
*   **Title Property**: Defines the category (needs, wants, or desires) <a class="yt-timestamp" data-t="00:12:44">[00:12:44]</a>.
*   **Relation to Expense Details Database**: Captures all expenses related to needs, wants, and desires separately <a class="yt-timestamp" data-t="00:12:48">[00:12:48]</a>.
*   **Expenses Amount**: A roll-up property from the "Expense Details Database," summing the actual expense amount for each type <a class="yt-timestamp" data-t="00:12:57">[00:12:57]</a>.
*   **Total Expenses**: A roll-up property from the "Total Expenses Database," summing all combined expenses <a class="yt-timestamp" data-t="00:13:12">[00:13:12]</a>.

## Dashboard Presentation

The primary dashboard of the [[tracking_income_and_expenses_in_notion | Notion expense tracker]] organizes and presents the data for easy analysis:
*   **Overview of Total Expenses**: Linked to the "Total Expenses Database" and displayed in a gallery view <a class="yt-timestamp" data-t="00:13:32">[00:13:32]</a>.
*   **Expense Categories**: Displays the three expense categories (needs, wants, desires) linked to the "Expense Categories Database" in a three-column gallery format <a class="yt-timestamp" data-t="00:13:43">[00:13:43]</a>.
*   **Top 10 Highlights**: Linked to the "Expense Details Database" and displayed in a list format, sorted as follows:
    *   **Recent Expenses**: Sorted by creation time in descending order <a class="yt-timestamp" data-t="00:14:07">[00:14:07]</a>.
    *   **Least 10 Expenses**: Sorted by actual expenses in ascending order <a class="yt-timestamp" data-t="00:14:11">[00:14:11]</a>.
    *   **Top 10 Expenses**: Sorted in descending order <a class="yt-timestamp" data-t="00:14:16">[00:14:16]</a>.
*   **Actual vs. Budgeted Expenses**: Linked to the "Expense Budget Classification Database" and displayed in a gallery format <a class="yt-timestamp" data-t="00:14:25">[00:14:25]</a>.
*   **Expenses Overview**: Linked to the "Period Database" and presented in a gallery format, with filters applied for each quarter to show necessary months <a class="yt-timestamp" data-t="00:14:36">[00:14:36]</a>.
*   **Expenses Overview Section**: Linked to the "Expense Source Database," displayed in a gallery format and repeated for all six heads of expenses <a class="yt-timestamp" data-t="00:14:55">[00:14:55]</a>.
*   **Frequency of Expenses**: Linked to the "Frequency of Expense Database," displayed in a gallery format with desired properties enabled <a class="yt-timestamp" data-t="00:15:05">[00:15:05]</a>.

This detailed [[overview_of_notion_budget_tracker_template | overview]] demonstrates how to [[budgeting_business_expenses_using_notion | budget business expenses]] and [[managing_business_expenses_using_notion | manage business expenses using Notion]], or personal finances, through a structured and analytical approach.