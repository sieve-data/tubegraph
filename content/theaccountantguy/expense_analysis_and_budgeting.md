---
title: Expense Analysis and Budgeting
videoId: OV1faI8Z6yg
---

From: [[theaccountantguy]] <br/> 

This article details how to build an expense tracker designed for [[budgeting_and_tracking_business_expenses | budgeting and tracking business expenses]], allowing users to manage and analyze their spending effectively <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>. The tracker provides a comprehensive overview of expenses, including budgeted versus actual amounts, and categorizes spending for in-depth analysis <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

## Expense Tracker Overview

The expense tracker includes several key sections for [[managing_budgeted_vs_actual_expenses | managing budgeted vs actual expenses]] and analysis:

*   **Total Expenses Overview**
    *   Displays total budgeted expenses <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.
    *   Shows total actual expenses <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.
    *   Calculates differences and percentage changes <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.
*   **Categorized Expenses**
    *   Expenses are categorized as needs, desires, and wants <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>.
*   **Top 10/Least 10/Recent Expenses Highlights**
    *   Reflects the top 10 expenses incurred <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.
    *   Identifies the least 10 expenses incurred <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.
    *   Lists recent expenses <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>.
*   **Actual vs. Budgeted Expenses**
    *   Expenses are divided into six predefined heads <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.
    *   Indicates total budgeted and actual expenses, differences, and percentage changes for each head <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>. This section helps with [[budget_and_actual_expenses_comparison | budget and actual expenses comparison]] and [[comparison_of_actual_vs_budgeted_expenses | comparison of actual vs budgeted expenses]].
*   **Expenses Overview by Period**
    *   Expenses are categorized by month and divided into four quarters <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.
    *   Shows total expenses incurred per month and their proportion to total expenses <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.
*   **Expenses Overview in Percentage**
    *   Expenses are categorized into six heads, showing total expenses and their proportion to the total <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.
*   **Frequency of Expenses**
    *   Indicates how frequently an expense is incurred (daily, one-time, weekly, monthly, quarterly, half-yearly, annually) <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.
    *   Shows the total amount incurred and sources for each frequency type <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.

## Building the Expense Tracker: Databases

To build this expense tracker, seven specific databases are required <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.

### Expense Details Database

This database stores individual expense details <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>.
*   **Expense Details (Title Property):** Shows individual expenses incurred <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.
*   **Period of Expense (Relation Property):** Links to a Period database, specifying the month an expense was incurred <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>.
*   **Expense Source (Relation Property):** Links to an Expense Source database, specifying the source or head under which an expense is incurred <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.
*   **Frequency of Expense (Relation Property):** Links to a Frequency of Expense database, indicating how frequently an expense occurs <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.
*   **Expense Categories (Relation Property):** Links to an Expense Categories database, classifying expenses as needs, wants, or desires <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
*   **Actual Expense (Number Property):** Specifies the actual amount of expense incurred, typically in US dollars <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.
*   **Budgeted Expense (Number Property):** Specifies the estimated budgeted expense for each month, also in US dollars <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>.
    *   The sum of actual and budgeted expenses can be found at the bottom <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>.

### Expense Source Database

This database categorizes expenses under six different heads and provides subsequent analysis <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>.
*   **Source of Expense (Title Property):** Identifies one of the six expense heads <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>.
*   **Actual Expense (Roll-up Property):** Rolls up the sum of actual expense values from the Expense Details database <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>.
*   **Budgeted Expense (Roll-up Property):** Rolls up the sum of budgeted expense values from the Expense Details database <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>. This is crucial for [[setting_budgeted_amounts_for_business_expenses | setting budgeted amounts for business expenses]].
*   **Total Expenses (Roll-up Property):** Derived from the Total Expenses database, extracting the total actual expenses <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>.
*   **Difference (Formula Property):** Calculates the difference between actual and budgeted expenses <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>. This aids in [[budgeted_vs_actual_expenses_tracking | budgeted vs actual expenses tracking]].
*   **Change in Percentage (Formula Property):** Calculates the difference divided by the budgeted expense amount, represented as a percentage <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.

### Frequency of Expenses Database

This database tracks how frequently expenses are incurred and provides further analysis <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>.
*   **Frequency (Title Property):** Specifies each individual mode of frequency (e.g., daily, monthly) <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>.
*   **Expense Details (Relation Property):** Relates to the Expense Details database, linking specific expenses to their frequency types <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>.
*   **Sources of Expense (Formula Property):** Calculates the unique sources of expenses for each frequency type <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>.

### Total Expenses Database

This database reflects the total expenses incurred for all six expense heads <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>.
*   **Properties:** Total actual expenses, total budgeted expenses, difference, and change in percentage <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>.
*   **Total Actual Expenses (Roll-up Property):** Calculates the sum of total expenses from the Expense Source database <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>.
*   **Total Budgeted Expense (Roll-up Property):** Calculates the sum of total budgeted expenses from the Expense Source database <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>.
*   **Amount (Formula Property):** Derives values based on the "Name" property:
    *   Gets actual expense value if "Name" is "Total Actual Expenses" <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>.
    *   Gets budgeted expense value if "Name" is "Total Budgeted Expenses" <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>.
    *   Gets difference if "Name" is "Difference" <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>.
    *   Calculates change in percentage (difference / budgeted expense value) if "Name" is "Change in Percentage" <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>.

### Period of Expense Database

This database specifies monthly expenses for the entire year and helps categorize expenses with their proportions <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>.
*   **Month (Title Property):** Specifies the month for each expense <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>.
*   **Expense Details (Relation Property):** Calculates expenses incurred each period from the Expense Details database <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>.
*   **Expenses for Each Month (Roll-up Property):** Derived from Expense Details, calculating the sum of actual expense values <a class="yt-timestamp" data-t="00:09:58">[00:10:00]</a>.
*   **Total Expenses (Roll-up Property):** Calculated from the Total Expense database, giving total actual expense value <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>.
*   **Proportion of the Total Expense (Formula Property):** Calculates expenses divided by total expenses, denoted as a percentage <a class="yt-timestamp" data-t="00:10:18">[00:10:20]</a>.
*   **Total Expenses (Relation Property):** Linked to the Total Expenses database to derive total expense values <a class="yt-timestamp" data-t="00:10:36">[00:10:36]</a>.

### Expense Budget Classification Database

This database classifies expenses under six heads, providing details on total actual expenses, total budgeted expenses, differences, and percentage changes for each <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>. This is useful for [[budget_vs_actual_expenses_tracking | budget vs actual expenses tracking]].
*   **Title Property:** Specifies required properties for use <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>.
*   **Relation Property:** Links to the Expense Source database, specifying individual expense heads <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>.
*   **Amount (Formula Property):** Derives total actual, total budgeted, and difference values for specific heads (e.g., travel and transportation) <a class="yt-timestamp" data-t="00:11:15">[00:11:17]</a>.
*   **Change in Percentage (Formula Property):** Calculates the difference divided by the budgeted expense <a class="yt-timestamp" data-t="00:11:38">[00:11:40]</a>.
*   **Roll-up Properties:**
    *   **Actual Expenses:** Derives values from the Expense Source database, summing expense values <a class="yt-timestamp" data-t="00:11:45">[00:11:47]</a>.
    *   **Budgeted Expenses:** Derives values from the Expense Source database, summing budgeted expense values <a class="yt-timestamp" data-t="00:11:53">[00:11:56]</a>.
    *   **Change in Percentage:** Derives the change in percentage from the Expense Source database <a class="yt-timestamp" data-t="00:12:11">[00:12:13]</a>.
    *   **Difference Column:** Derives the difference between budgeted and actual expenses <a class="yt-timestamp" data-t="00:12:21">[00:12:21]</a>.
*   These columns need to be repeated for all six heads of expenses <a class="yt-timestamp" data-t="00:12:27">[00:12:30]</a>.

### Expense Categories Database

This database reflects expenses based on needs, wants, and desires, enabling further analysis for each type <a class="yt-timestamp" data-t="00:04:04">[00:04:05]</a>. This provides insight into [[expense_categories_and_budget_updates | expense categories and budget updates]].
*   **Title Property:** Defines the category (needs, wants, desires) <a class="yt-timestamp" data-t="00:12:44">[00:12:44]</a>.
*   **Relation Column:** Links to the Expense Details database to capture expenses related to each category separately <a class="yt-timestamp" data-t="00:12:48">[00:12:50]</a>.
*   **Expenses Amount (Roll-up Property):** Derived from the Expense Details database, providing the sum of actual expenses for each category <a class="yt-timestamp" data-t="00:12:57">[00:13:00]</a>.
*   **Total Expenses (Roll-up Property):** Derived from the Total Expenses database, giving the sum of all combined expenses <a class="yt-timestamp" data-t="00:13:12">[00:13:15]</a>.

## Primary Dashboard Presentation

The primary dashboard of the expense tracker displays information from the databases in various formats:

*   **Overview of Total Expenses:** Linked to the Total Expenses database and set out in a gallery mode view <a class="yt-timestamp" data-t="00:13:32">[00:13:35]</a>.
*   **Three Categories of Expenses:** Linked to the Expense Categories database and presented in a gallery format, often set in a three-column layout <a class="yt-timestamp" data-t="00:13:43">[00:13:45]</a>.
*   **Top 10 Highlights:** Linked to the Expense Details database in a list format, sorted as follows:
    *   Recent expenses: sorted by creation time in descending order <a class="yt-timestamp" data-t="00:14:07">[00:14:09]</a>.
    *   Least 10 expenses: sorted by actual expenses in ascending order <a class="yt-timestamp" data-t="00:14:11">[00:14:11]</a>.
    *   Top 10 expenses: sorted in descending order <a class="yt-timestamp" data-t="00:14:16">[00:14:16]</a>.
*   **Actual vs. Budgeted Expenses:** Linked to the Expense Budget Classification database and presented in a gallery format <a class="yt-timestamp" data-t="00:14:25">[00:14:27]</a>. This facilitates [[viewing_and_analyzing_overall_travel_expense_summaries | viewing and analyzing overall travel expense summaries]] for various categories.
*   **Expenses Overview (by Period):** Linked to the Period database and given in a gallery format, with filters applied for each quarter to show necessary months <a class="yt-timestamp" data-t="00:14:36">[00:14:39]</a>.
*   **Expenses Overview (by Head):** Linked to the Expense Source database, set out in a gallery format, and repeated for all expense heads <a class="yt-timestamp" data-t="00:14:55">[00:14:56]</a>.
*   **Frequency of Expenses:** Linked to the Frequency of Expense database, given in a gallery format with desired properties enabled <a class="yt-timestamp" data-t="00:15:05">[00:15:07]</a>.