---
title: Notion expense tracker setup
videoId: OV1faI8Z6yg
---

From: [[theaccountantguy]] <br/> 

This article details how to build an [[budgeting_and_tracking_expenses_in_notion | expense tracker]] in Notion, allowing users to monitor spending effectively <a class="yt-timestamp" data-t="01:08:00">[01:08:00]</a>.

## Expense Tracker Overview

The Notion expense tracker includes several key sections:

*   **Total Expenses Overview** A summary showing total budgeted expenses, total actual expenses, the difference, and the percentage change <a class="yt-timestamp" data-t="01:13:00">[01:13:00]</a>.
*   **Categorized Expenses** Expenses are categorized into needs, desires, and wants <a class="yt-timestamp" data-t="01:22:00">[01:22:00]</a>.
*   **Top/Least/Recent Expenses Highlights** Reflects the top 10, least 10, and most recent expenses incurred during a period <a class="yt-timestamp" data-t="01:27:00">[01:27:00]</a>.
*   **Actual vs. Budget Expenses** Displays expenses divided into six predefined heads, indicating total budgeted expenses, total actual expenses, difference, and percentage change for each <a class="yt-timestamp" data-t="01:41:00">[01:41:00]</a>.
*   **Expenses Overview by Period** Categorizes expenses into months, divided into four quarters, showing total expenses and their proportion to total expenses for each month <a class="yt-timestamp" data-t="01:58:00">[01:58:00]</a>.
*   **Expenses Overview in Percentage** Shows expenses categorized into six heads, detailing total expenses and their proportion to the total <a class="yt-timestamp" data-t="02:17:00">[02:17:00]</a>.
*   **Frequency of Expenses** Indicates how frequently an expense is incurred, categorized as daily, one-time, weekly, monthly, quarterly, half-yearly, and annually <a class="yt-timestamp" data-t="02:32:00">[02:32:00]</a>. This section also shows the total amount of expenses incurred and their sources for each frequency type <a class="yt-timestamp" data-t="02:44:00">[02:44:00]</a>.

## Building the Expense Tracker

To build this [[using_notion_for_expense_management | expense management]] tracker, seven databases are required <a class="yt-timestamp" data-t="02:52:00">[02:52:00]</a>:

1.  **Expense Details**: Showcases details related to individual expenses <a class="yt-timestamp" data-t="02:58:00">[02:58:00]</a>.
2.  **Expense Source**: Categorizes expenses under six heads with subsequent analysis <a class="yt-timestamp" data-t="03:08:00">[03:08:00]</a>.
3.  **Frequency of Expenses**: Showcases how frequently an expense is incurred <a class="yt-timestamp" data-t="03:18:00">[03:18:00]</a>.
4.  **Total Expenses**: Reflects total expenses incurred for all six heads, categorized by actual, budgeted, difference, and change <a class="yt-timestamp" data-t="03:27:00">[03:27:00]</a>.
5.  **Period of Expense**: Specifies monthly expenses for the entire year, categorizing expenses into different categories with their proportion <a class="yt-timestamp" data-t="03:38:00">[03:38:00]</a>.
6.  **Expense Budget Classification**: Classifies expenses into six heads, each with budgeted expenses, actual expenses, differences, and change <a class="yt-timestamp" data-t="03:49:00">[03:49:00]</a>.
7.  **Expense Categories**: Reflects expenses as per needs, wants, and desires, and provides further analysis for each type <a class="yt-timestamp" data-t="04:04:00">[04:04:00]</a>.

### Database: Expense Details

This database specifies details related to each individual expense <a class="yt-timestamp" data-t="04:22:00">[04:22:00]</a>.

*   **Expense Details** (Title property): Shows individual expenses <a class="yt-timestamp" data-t="04:27:00">[04:27:00]</a>.
*   **Period of Expense** (Relation property): Links to the 'Period of Expense' database, specifying the month for each expense <a class="yt-timestamp" data-t="04:36:00">[04:36:00]</a>.
*   **Expense Source** (Relation property): Links to the 'Expense Source' database, specifying the source category of the expense <a class="yt-timestamp" data-t="04:46:00">[04:46:00]</a>.
*   **Frequency of Expense** (Relation property): Links to the 'Frequency of Expense' database, indicating how frequently an expense is incurred <a class="yt-timestamp" data-t="04:57:00">[04:57:00]</a>.
*   **Expense Categories** (Relation property): Links to the 'Expense Categories' database, specifying the category for each individual source of expense <a class="yt-timestamp" data-t="05:07:00">[05:07:00]</a>.
*   **Actual Expense** (Number property): Specifies the actual amount of expense incurred for the period in US dollars <a class="yt-timestamp" data-t="05:15:00">[05:15:00]</a>.
*   **Budgeted Expense** (Number property): Specifies the budgeted expense estimated for each month in US dollars <a class="yt-timestamp" data-t="05:28:00">[05:28:00]</a>.
    *   The sum of actual and budgeted expenses can be found at the bottom <a class="yt-timestamp" data-t="05:34:00">[05:34:00]</a>.

### Database: Expense Source

This database specifies the six different sources of expenses <a class="yt-timestamp" data-t="05:48:00">[05:48:00]</a>.

*   **Source of Expense** (Title property): Specifies one of the six heads of expenses <a class="yt-timestamp" data-t="05:54:00">[05:54:00]</a>.
*   **Actual Expense** (Roll-up property): Rolled up from the 'Expense Details' database, showing the sum of actual expense amounts <a class="yt-timestamp" data-t="06:04:00">[06:04:00]</a>.
*   **Budgeted Expense** (Roll-up property): Rolled up from the 'Expense Details' database, showing the sum of budgeted expense amounts <a class="yt-timestamp" data-t="06:14:00">[06:14:00]</a>.*   **Total Expenses** (Roll-up property): Derived from the 'Total Expenses' database, extracting the total actual expenses amount as the original value <a class="yt-timestamp" data-t="06:25:00">[06:25:00]</a>.
*   **Difference** (Formula property): Shows the difference between actual and budgeted expenses <a class="yt-timestamp" data-t="06:40:00">[06:40:00]</a>.
*   **Change in Percentage** (Formula property): Calculates the difference divided by the budgeted expense amount, represented as a percentage <a class="yt-timestamp" data-t="06:51:00">[06:51:00]</a>.

### Database: Frequency of Expenses

This database calculates how frequently an expense is incurred <a class="yt-timestamp" data-t="07:12:00">[07:12:00]</a>.

*   **Frequency** (Title property): Specifies each individual mode of frequency (e.g., daily, weekly) <a class="yt-timestamp" data-t="07:20:00">[07:20:00]</a>.
*   **Expense Details** (Relation property): Relates different types of expenses from the 'Expense Details' database to each frequency type <a class="yt-timestamp" data-t="07:26:00">[07:26:00]</a>.
*   **Sources of Expense** (Formula property): Calculates the unique sources of expenses for each frequency <a class="yt-timestamp" data-t="07:35:00">[07:35:00]</a>.

### Database: Total Expenses

This database calculates total expenses incurred during a period <a class="yt-timestamp" data-t="08:14:00">[08:14:00]</a>. It links all six expense heads.

*   **Total Actual Expenses** (Roll-up property): Calculates the total expenses from the 'Expense Source' database, providing the sum value <a class="yt-timestamp" data-t="08:36:00">[08:36:00]</a>.
*   **Total Budgeted Expense** (Roll-up property): Calculates the total budgeted expenses from the 'Expense Source' database, providing the sum value <a class="yt-timestamp" data-t="08:47:00">[08:47:00]</a>.
*   **Amount** (Formula property): Derives values based on the 'Name' property (e.g., actual expense if 'Total Actual Expenses', budgeted expense if 'Total Budgeted Expenses', difference if 'Difference', and percentage change if 'Change in Percentage') <a class="yt-timestamp" data-t="08:57:00">[08:57:00]</a>. Percentage change is calculated as the difference divided by the budgeted expense value <a class="yt-timestamp" data-t="09:18:00">[09:18:00]</a>.

### Database: Period of Expense

This database specifies expenses for each month and provides further analysis <a class="yt-timestamp" data-t="09:36:00">[09:36:00]</a>.

*   **Month** (Title property): Specifies the month for each expense <a class="yt-timestamp" data-t="09:42:00">[09:42:00]</a>.
*   **Expense Details** (Relation property): Links to the 'Expense Details' database, calculating expenses incurred each period <a class="yt-timestamp" data-t="09:48:00">[09:48:00]</a>.
*   **Expenses for Each Month** (Roll-up property): Derived from 'Expense Details' database, calculating the sum of actual expense values <a class="yt-timestamp" data-t="09:58:00">[09:58:00]</a>.
*   **Total Expenses** (Roll-up property): Calculated from the 'Total Expense' database, giving the total actual expense value <a class="yt-timestamp" data-t="10:10:00">[10:10:00]</a>.
*   **Proportion of the Total Expense** (Formula property): Calculates the expenses divided by the total expenses, denoted as a percentage <a class="yt-timestamp" data-t="10:18:00">[10:18:00]</a>.
*   **Total Expenses** (Relation property): Links to the 'Total Expenses' database to derive total expense values <a class="yt-timestamp" data-t="10:36:00">[10:36:00]</a>.

### Database: Expense Budget Classification

This database classifies expenses under six heads and provides details on total actual expenses, total budgeted expenses, difference, and percentage change for each <a class="yt-timestamp" data-t="10:46:00">[10:46:00]</a>.

*   **Title** (Title property): Specifies required properties for use <a class="yt-timestamp" data-t="11:00:00">[11:00:00]</a>.
*   **Relation property** (Relation property): Relates to the 'Expense Source' database, specifying individual heads of expense <a class="yt-timestamp" data-t="11:06:00">[11:06:00]</a>.
*   **Amount** (Formula property): Derives total actual expenses, total budgeted expenses, and the difference for specific expense heads (e.g., travel and transportation) <a class="yt-timestamp" data-t="11:13:00">[11:13:00]</a>.
*   **Change in Percentage** (Formula property): Calculates the difference divided by the budgeted expense <a class="yt-timestamp" data-t="11:38:00">[11:38:00]</a>.
*   **Actual Expenses** (Roll-up property): Derives values from the 'Expense Source' database, summing expense values <a class="yt-timestamp" data-t="11:45:00">[11:45:00]</a>.
*   **Budgeted Expenses** (Roll-up property): Also a roll-up value from the 'Expense Source' database, summing expense values <a class="yt-timestamp" data-t="11:53:00">[11:53:00]</a>.
*   **Change in Percentage** (Roll-up property): Derived from the 'Expense Source' database, showing the original percentage change <a class="yt-timestamp" data-t="12:11:00">[12:11:00]</a>.
*   **Difference** (Roll-up property): Shows the difference between budgeted and actual expenses <a class="yt-timestamp" data-t="12:21:00">[12:21:00]</a>.
    *   These columns need to be repeated for all six heads of expenses <a class="yt-timestamp" data-t="12:27:00">[12:27:00]</a>.

### Database: Expense Categories

This database specifies the three types of expenses: needs, wants, and desires <a class="yt-timestamp" data-t="12:35:00">[12:35:00]</a>.

*   **Title** (Title property): The primary category title (needs, wants, desires) <a class="yt-timestamp" data-t="12:44:00">[12:44:00]</a>.
*   **Relation column** (Relation property): Links to the 'Expense Details' database, capturing all expenses related to needs, wants, and desires separately <a class="yt-timestamp" data-t="12:48:00">[12:48:00]</a>.
*   **Expenses Amount** (Roll-up property): The actual expenses incurred, derived from the 'Expense Details' database, calculating the sum for each individual type of expense <a class="yt-timestamp" data-t="12:57:00">[12:57:00]</a>.
*   **Total Expenses** (Roll-up property): Derived from the 'Total Expenses' database, providing the sum of all combined expenses <a class="yt-timestamp" data-t="13:12:00">[13:12:00]</a>.

## Primary Dashboard Presentation

The primary dashboard for the [[using_notion_as_an_expense_tracker | Notion expense tracker]] integrates these databases for an organized view <a class="yt-timestamp" data-t="13:25:00">[13:25:00]</a>.

*   **Overview of Total Expenses**: Linked to the 'Total Expenses' database and set out in a gallery view <a class="yt-timestamp" data-t="13:32:00">[13:32:00]</a>.
*   **Three Categories of Expenses**: Linked to the 'Expense Categories' database, given in a gallery format within a three-column layout (achieved by typing `/three column`) <a class="yt-timestamp" data-t="13:43:00">[13:43:00]</a>.
*   **Top 10 Highlights**: Linked to the 'Expense Details' database and set out in a list format, with data sorted as follows <a class="yt-timestamp" data-t="13:57:00">[13:57:00]</a>:
    *   Recent expenses: Sorted by creation time in descending order <a class="yt-timestamp" data-t="14:07:00">[14:07:00]</a>.
    *   Least 10 expenses: Sorted by actual expenses in ascending order <a class="yt-timestamp" data-t="14:11:00">[14:11:00]</a>.
    *   Top 10 expenses: Sorted in descending order <a class="yt-timestamp" data-t="14:13:00">[14:13:00]</a>.
*   **Actual vs. Budgeted Expenses**: Linked to the 'Expense Budget Classification' database and set out in a gallery format <a class="yt-timestamp" data-t="14:25:00">[14:25:00]</a>.
*   **Expenses Overview (by Period)**: Linked to the 'Period' database and given in a gallery format, with filters applied for each quarter to show necessary months <a class="yt-timestamp" data-t="14:36:00">[14:36:00]</a>.
*   **Expenses Overview (by Source)**: Linked to the 'Expense Source' database, set out in a gallery format, and repeated for all heads of expenses <a class="yt-timestamp" data-t="14:55:00">[14:55:00]</a>.
*   **Frequency of Expenses**: Linked to the 'Frequency of Expense' database, given in a gallery format with desired properties enabled <a class="yt-timestamp" data-t="15:05:00">[15:05:00]</a>.

This [[benefits_of_tracking_expenses_in_notion | Notion expense tracker]] can be used for [[using_notion_for_business_expense_tracking | business expense tracking]], [[using_notion_to_track_credit_card_expenses | credit card expense tracking]], and more. Other specialized trackers like a [[notion_tax_payment_tracker | Notion tax payment tracker]], [[notion_home_renovation_expense_tracker | home renovation expense tracker]], or [[setting_up_a_travel_expense_tracker_in_notion | travel expense tracker]] can also leverage similar database structures.