---
title: Creating an expense categories system
videoId: OV1faI8Z6yg
---

From: [[theaccountantguy]] <br/> 

This article outlines how to build an expense tracker in Notion, focusing on the various databases and categorizations used to manage and analyze spending <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>. The tracker provides an overview of total expenses, categorized spending, top/least/recent expenses, and comparisons between actual and budgeted amounts <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

## Core Components: The Seven Databases

To create this expense tracking system, seven interconnected databases are built <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>. These databases help with [[setting_up_expense_categories_and_budgets | setting up expense categories and budgets]] and [[adding_and_categorizing_expenses | adding and categorizing expenses]].

### 1. Expense Details Database

This database specifies the details of each individual expense incurred <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>.
*   **Title Property**: Shows individual expenses <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.
*   **Period of Expense**: A relation property linked to the 'Period of Expense' database, indicating the month an expense was incurred <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>.
*   **Expense Source**: A relation property linked to the 'Expense Source' database, specifying the source or head under which an expense falls <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.
*   **Frequency of Expense**: A relation property linked to the 'Frequency of Expense' database, indicating how frequently an expense is incurred <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.
*   **Expense Categories**: A relation property linked to the 'Expense Categories' database, specifying the category (e.g., needs, wants, desires) for each expense source <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>. This is crucial for [[modifying_and_adding_new_expense_categories_in_notion | modifying and adding new expense categories in Notion]] and [[customizing_categories_in_notion_expense_tracker | customizing categories]].
*   **Actual Expense**: A number property showing the actual amount spent in US dollars <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.
*   **Budgeted Expense**: A number property for the estimated budgeted amount for each month in US dollars <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>.
    *   The sum of actual and budgeted expenses is shown at the bottom <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>.

### 2. Expense Source Database

This database specifies six different sources or "heads" of expenses <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>. This is vital for [[managing_and_editing_expense_sources_and_categories | managing and editing expense sources]].
*   **Source of Expense**: A title property for each of the six expense heads <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>.
*   **Actual Expense**: A roll-up property from the 'Expense Details' database, summing the actual expense amounts <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>.
*   **Budgeted Expense**: A roll-up property from the 'Expense Details' database, summing the budgeted expense amounts <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>.
*   **Total Expenses**: A roll-up property from the 'Total Expenses' database, extracting the total actual expenses <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>.
*   **Difference**: A formula property calculating the difference between actual and budgeted expenses <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.
*   **Change in Percentage**: A formula property calculating the difference divided by the budgeted expense, shown as a percentage <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.

### 3. Frequency of Expenses Database

This database calculates and analyzes how frequently an expense is incurred <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>.
*   **Frequency**: A title property specifying the mode of frequency (e.g., daily, one-time, weekly, monthly, quarterly, half-yearly, annually) <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.
*   **Relation Property**: Linked to the 'Expense Details' database, relating expenses to their frequency type <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>.
*   **Sources of Expense**: A formula property calculating the unique sources of expenses for each frequency type <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>.

### 4. Total Expenses Database

This database reflects the total expenses incurred for all six expense heads <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>, categorizing them as actual, budgeted, difference, and percentage change <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.
*   **Total Actual Expenses**: A roll-up property from the 'Expense Source' database, summing total expenses <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>.
*   **Total Budgeted Expenses**: A roll-up property from the 'Expense Source' database, summing total budgeted expenses <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>.
*   **Difference** and **Change in Percentage**: Values linked from the expense heads <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>.
*   **Amount Column**: A formula property deriving values based on the name property (e.g., actual expense, budgeted expense, difference, or change in percentage) <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>.

### 5. Period of Expense Database

This database specifies monthly expenses for the entire year and helps categorize expenses with their proportions <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>.
*   **Month**: A title property specifying the month for each expense <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>.
*   **Expense Details**: A relation property linked to the 'Expense Details' database, capturing expenses incurred each period <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>.
*   **Expenses for each month**: A roll-up property from the 'Expense Details' database, summing actual expense values <a class="yt-timestamp" data-t="00:09:58">[00:09:58]</a>.
*   **Total Expenses**: A roll-up property from the 'Total Expenses' database, giving total actual expense value <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>.
*   **Proportion of the Total Expense**: A formula property calculating monthly expenses divided by total expenses, shown as a percentage bar <a class="yt-timestamp" data-t="00:10:19">[00:10:19]</a>.

### 6. Expense Budget Classification Database

This database classifies expenses under the six main heads and provides details on total actual expenses, total budgeted expenses, differences, and percentage change for each head <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>. This is useful for [[setting_up_business_expense_categories | setting up business expense categories]] and [[customizing_expense_categories_in_Notion | customizing expense categories]].
*   **Title Property**: Specifies required properties for use <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>.
*   **Relation Property**: Links to the 'Expense Source' database, specifying individual heads of expense <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>.
*   **Amount**: A formula property deriving total actual expenses, total budgeted expenses, and differences for each head <a class="yt-timestamp" data-t="00:11:15">[00:11:15]</a>.
*   **Change in Percentage**: A formula property for the difference divided by the budgeted expense <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>.
*   **Roll-up Properties**: Derives actual expenses, budgeted expenses, and change in percentage values from the 'Expense Source' database, summing them <a class="yt-timestamp" data-t="00:11:45">[00:11:45]</a>.
*   **Difference Column**: A roll-up property showing the difference between budgeted and actual expenses <a class="yt-timestamp" data-t="00:12:21">[00:12:21]</a>. These columns are repeated for all six expense heads <a class="yt-timestamp" data-t="00:12:27">[00:12:27]</a>.

### 7. Expense Categories Database

This database categorizes expenses into three types: needs, wants, and desires <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>. This system allows for [[adding_or_deleting_categories_in_a_notion_expense_tracker | adding or deleting categories]] and [[adding_and_editing_expense_categories | editing expense categories]].
*   **Title Property**: Specifies the expense category (needs, wants, desires) <a class="yt-timestamp" data-t="00:12:35">[00:12:35]</a>.
*   **Relation Column**: Linked to the 'Expense Details' database, capturing all expenses related to needs, wants, and desires separately <a class="yt-timestamp" data-t="00:12:48">[00:12:48]</a>.
*   **Expenses Amount**: A roll-up property derived from the 'Expense Details' database, summing the actual expense amount for each individual type of expense <a class="yt-timestamp" data-t="00:12:57">[00:12:57]</a>.
*   **Total Expenses**: A roll-up property from the 'Total Expenses' database, giving the sum of all combined expenses <a class="yt-timestamp" data-t="00:13:12">[00:13:12]</a>.

## Primary Dashboard Presentation

The primary dashboard provides a visual overview of the expense tracker <a class="yt-timestamp" data-t="00:13:27">[00:13:27]</a>:

*   **Overview of Total Expenses**: Linked to the 'Total Expenses' database in a gallery view <a class="yt-timestamp" data-t="00:13:32">[00:13:32]</a>.
*   **Three Categories of Expenses**: Linked to the 'Expense Categories' database in a gallery format, displayed in a three-column layout <a class="yt-timestamp" data-t="00:13:43">[00:13:43]</a>.
*   **Top 10 Highlights**: Linked to the 'Expense Details' database in a list format, sorted as follows <a class="yt-timestamp" data-t="00:13:57">[00:13:57]</a>:
    *   **Recent expenses**: Sorted by 'created time' in descending order <a class="yt-timestamp" data-t="00:14:07">[00:14:07]</a>.
    *   **Least 10 expenses**: Sorted by 'actual expenses' in ascending order <a class="yt-timestamp" data-t="00:14:11">[00:14:11]</a>.
    *   **Top 10 expenses**: Sorted in descending order <a class="yt-timestamp" data-t="00:14:16">[00:14:16]</a>.
*   **Actual vs. Budgeted Expenses**: Linked to the 'Expense Budget Classification' database in a gallery format <a class="yt-timestamp" data-t="00:14:25">[00:14:25]</a>.
*   **Expenses Overview**: Linked to the 'Period' database in a gallery format, with filters applied for each quarter to show necessary months <a class="yt-timestamp" data-t="00:14:36">[00:14:36]</a>.
*   **Expenses Overview Section (by Source)**: Linked to the 'Expense Source' database in a gallery format, repeated for all six expense heads <a class="yt-timestamp" data-t="00:14:55">[00:14:55]</a>.
*   **Frequency of Expenses**: Linked to the 'Frequency of Expense' database in a gallery format <a class="yt-timestamp" data-t="00:15:05">[00:15:05]</a>.