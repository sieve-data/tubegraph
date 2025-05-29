---
title: Expense categorization and analysis
videoId: OV1faI8Z6yg
---

From: [[theaccountantguy]] <br/> 

This article outlines how to build an expense tracker for managing and analyzing spending, categorizing expenses based on various criteria, and presenting financial data effectively <a class="yt-timestamp" data-t="01:08:00">[01:08:00]</a>.

## Expense Tracker Overview
An expense tracker provides a comprehensive overview of financial data, including total budgeted expenses, total actual expenses, differences, and percentage change <a class="yt-timestamp" data-t="01:13:00">[01:13:00]</a>. It [[using_categories_for_effective_expense_management | categorizes expenses]] into "needs," "desires," and "wants" <a class="yt-timestamp" data-t="01:22:00">[01:22:00]</a>. Key highlights include the top 10, least 10, and most recent expenses incurred during a specific period <a class="yt-timestamp" data-t="01:27:00">[01:27:00]</a>.

### Key Analytical Sections
The tracker breaks down expenses into several analytical views:
*   **Actual vs. Budgeted Expenses** Expenses are divided into six main "heads" <a class="yt-timestamp" data-t="01:41:00">[01:41:00]</a>. This section displays total budgeted expenses, total actual expenses, their difference, and percentage change <a class="yt-timestamp" data-t="01:48:00">[01:48:00]</a>.
*   **Expenses Overview by Period** Expenses are categorized by month, divided into four quarters, showing total expenses incurred and their proportion to total expenses <a class="yt-timestamp" data-t="01:58:00">[01:58:00]</a>.
*   **Expenses Overview in Percentage** This view categorizes expenses into the six main heads, showing total expenses and their proportion to the total <a class="yt-timestamp" data-t="02:17:00">[02:17:00]</a>.
*   **Frequency of Expenses** This section indicates how frequently an expense is incurred, categorizing them as daily, one-time, weekly, monthly, quarterly, half-yearly, or annually <a class="yt-timestamp" data-t="02:32:00">[02:32:00]</a>. It also displays the total amount and sources for each frequency type <a class="yt-timestamp" data-t="02:44:00">[02:44:00]</a>.

## Building the Expense Tracker: Databases
To build this expense tracker, seven specific databases are required <a class="yt-timestamp" data-t="02:54:00">[02:54:00]</a>:

1.  **Expense Details** <a class="yt-timestamp" data-t="02:58:00">[02:58:00]</a>: Showcases individual expense details.
2.  **Expense Source** <a class="yt-timestamp" data-t="03:08:00">[03:08:00]</a>: [[defining_expense_categories_in_notion | Categorizes expenses]] under six heads with analysis.
3.  **Frequency of Expenses** <a class="yt-timestamp" data-t="03:18:00">[03:18:00]</a>: Shows how frequently an expense is incurred.
4.  **Total Expenses** <a class="yt-timestamp" data-t="03:27:00">[03:27:00]</a>: Reflects total expenses for all six heads, with actual, budgeted, difference, and change [[expense_detail_and_overview_sections_in_notion | details]] <a class="yt-timestamp" data-t="03:31:00">[03:31:00]</a>.
5.  **Period of Expense** <a class="yt-timestamp" data-t="03:38:00">[03:38:00]</a>: Specifies monthly expenses for the entire year and helps [[classifying_and_managing_travel_expenses | categorize expenses]] into different categories with proportions <a class="yt-timestamp" data-t="03:40:00">[03:40:00]</a>.
6.  **Expense Budget Classification** <a class="yt-timestamp" data-t="03:49:00">[03:49:00]</a>: Helps [[managing_different_types_of_business_expenses | classify expenses]] into six heads, each with budgeted, actual, differences, and change values <a class="yt-timestamp" data-t="03:51:00">[03:51:00]</a>.
7.  **Expense Categories** <a class="yt-timestamp" data-t="04:04:00">[04:04:00]</a>: Reflects expenses based on "needs," "wants," and "desires" for further analysis <a class="yt-timestamp" data-t="04:07:00">[04:07:00]</a>.

### Database Details

#### Expense Details Database
This database specifies details related to each individual expense <a class="yt-timestamp" data-t="04:22:00">[04:22:00]</a>.
*   **Expense Details** (Title property): Shows individual expenses incurred <a class="yt-timestamp" data-t="04:27:00">[04:27:00]</a>.
*   **Period of Expense** (Relation property): Links to the Period database, specifying the month an expense was incurred <a class="yt-timestamp" data-t="04:36:00">[04:36:00]</a>.
*   **Expense Source** (Relation property): Links to the Expense Source database, specifying the source under which an expense was incurred <a class="yt-timestamp" data-t="04:46:00">[04:46:00]</a>.
*   **Frequency of Expense** (Relation property): Links to the Frequency of Expense database, indicating how frequently an expense is incurred <a class="yt-timestamp" data-t="04:57:00">[04:57:00]</a>.
*   **Expense Categories** (Relation property): Links to the Expense Categories database, specifying the [[categories_and_classifications_in_bookkeeping | category]] for each individual source of expense <a class="yt-timestamp" data-t="05:07:00">[05:07:00]</a>.
*   **Actual Expense** (Number property): Specifies the actual amount of expense incurred for the period in US dollars <a class="yt-timestamp" data-t="05:15:00">[05:15:00]</a>.
*   **Budgeted Expense** (Number property): The estimated budgeted expense for each month in US dollars <a class="yt-timestamp" data-t="05:28:00">[05:28:00]</a>.
    *   The sum of actual and budgeted expenses can be found at the bottom <a class="yt-timestamp" data-t="05:34:00">[05:34:00]</a>.

#### Expense Source Database
This database specifies the six different sources of expenses <a class="yt-timestamp" data-t="05:48:00">[05:48:00]</a>.
*   **Source of Expense** (Title property): Specifies one of the six heads of expenses <a class="yt-timestamp" data-t="05:54:00">[05:54:00]</a>.
*   **Actual Expense** (Roll-up property): Rolls up the actual expense amount from the Expense Details database (sum format) <a class="yt-timestamp" data-t="06:04:00">[06:04:00]</a>.
*   **Budgeted Expense** (Roll-up property): Rolls up the budgeted expense amount from the Expense Details database (sum format) <a class="yt-timestamp" data-t="06:14:00">[06:14:00]</a>.
*   **Total Expenses** (Roll-up property): Extracts the total actual expenses amount from the Total Expenses database <a class="yt-timestamp" data-t="06:25:00">[06:25:00]</a>.
*   **Difference** (Formula property): Calculates the difference between actual and budgeted expenses <a class="yt-timestamp" data-t="06:40:00">[06:40:00]</a>.
*   **Change in Percentage** (Formula property): Calculates the difference divided by the budgeted expense amount, represented as a percentage <a class="yt-timestamp" data-t="06:51:00">[06:51:00]</a>.

#### Frequency of Expenses Database
This database calculates how frequently an expense is incurred and performs further analysis <a class="yt-timestamp" data-t="07:12:00">[07:12:00]</a>.
*   **Frequency** (Title property): Specifies each individual mode of frequency (e.g., daily, weekly) <a class="yt-timestamp" data-t="07:20:00">[07:20:00]</a>.
*   **Expense Details** (Relation property): Relates to the Expense Details database, linking different types of expenses to each frequency type <a class="yt-timestamp" data-t="07:26:00">[07:26:00]</a>.*   **Sources of Expense** (Formula property): Calculates the unique sources of expenses for each frequency type <a class="yt-timestamp" data-t="07:35:00">[07:35:00]</a>. For example, if "commutation expenses" appears twice, it counts as one source <a class="yt-timestamp" data-t="07:41:00">[07:41:00]</a>.

#### Total Expenses Database
This database calculates the total expenses incurred during the period <a class="yt-timestamp" data-t="08:14:00">[08:14:00]</a>.
*   **Total Actual Expenses** (Roll-up property): Calculates total expenses from the Expense Source database (sum value) <a class="yt-timestamp" data-t="08:36:00">[08:36:00]</a>.
*   **Total Budgeted Expenses** (Roll-up property): Calculates total budgeted expenses from the Expense Source database (sum value) <a class="yt-timestamp" data-t="08:47:00">[08:47:00]</a>.
*   **Amount** (Formula property): Derives values based on the "Name" property (which specifies total actual, total budgeted, difference, or change in percentage) <a class="yt-timestamp" data-t="08:57:00">[08:57:00]</a>. For example, if "Name" is "total actual expenses," it retrieves the actual expense value <a class="yt-timestamp" data-t="09:03:00">[09:03:00]</a>. The change in percentage is calculated as difference divided by budgeted expense <a class="yt-timestamp" data-t="09:18:00">[09:18:00]</a>.

#### Period of Expense Database
This database specifies expenses for each month and performs further [[analyzing_expenses_by_type_and_period | analysis]] <a class="yt-timestamp" data-t="09:32:00">[09:32:00]</a>.
*   **Month** (Title property): Specifies the month for each expense <a class="yt-timestamp" data-t="09:42:00">[09:42:00]</a>.
*   **Expense Details** (Relation property): Links to the Expense Details database, calculating expenses incurred each period <a class="yt-timestamp" data-t="09:48:00">[09:48:00]</a>.
*   **Expenses for Each Month** (Roll-up property): Derived from Expense Details database, summing the actual expense value <a class="yt-timestamp" data-t="09:58:00">[09:58:00]</a>.
*   **Total Expenses** (Roll-up property): Derived from the Total Expense database, showing total actual expense value <a class="yt-timestamp" data-t="10:10:00">[10:10:00]</a>.
*   **Proportion of the Total Expense** (Formula property): Calculates expenses divided by total expenses, denoted as a percentage bar <a class="yt-timestamp" data-t="10:18:00">[10:18:00]</a>.

#### Expense Budget Classification Database
This database [[classifying_inventory_into_categories | classifies expenses]] under six heads and provides details on total actual expenses, total budgeted expenses, difference, and percentage change for each head <a class="yt-timestamp" data-t="10:46:00">[10:46:00]</a>.
*   **Title** (Title property): Specifies the required properties for use <a class="yt-timestamp" data-t="11:00:00">[11:00:00]</a>.
*   **Relation Property** (Relation property): Links to the Expense Source database, specifying individual heads of expense <a class="yt-timestamp" data-t="11:06:00">[11:06:00]</a>.
*   **Amount** (Formula property): Derives total actual, total budgeted, and difference values for specific expense heads (e.g., travel and transportation) <a class="yt-timestamp" data-t="11:13:00">[11:13:00]</a>.
*   **Change in Percentage** (Formula property): Calculates difference divided by budgeted expense <a class="yt-timestamp" data-t="11:38:00">[11:38:00]</a>.
*   **Actual Expenses** (Roll-up property): Derives actual expense values from the Expense Source database, calculating their sum <a class="yt-timestamp" data-t="11:45:00">[11:45:00]</a>.
*   **Budgeted Expenses** (Roll-up property): Derives budgeted expense values from the Expense Source database, calculating their sum <a class="yt-timestamp" data-t="11:53:00">[11:53:00]</a>.
*   **Change in Percentage** (Roll-up property): Derives the change in percentage from the Expense Source database, showing the original value <a class="yt-timestamp" data-t="12:11:00">[12:11:00]</a>.
*   **Difference Column** (Roll-up property): Gives the difference between budgeted and actual expenses <a class="yt-timestamp" data-t="12:21:00">[12:21:00]</a>.
    *   These columns need to be repeated for all six heads of expenses <a class="yt-timestamp" data-t="12:27:00">[12:27:00]</a>.

#### Expense Categories Database
This database specifies the three types of expenses: needs, wants, and desires <a class="yt-timestamp" data-t="12:35:00">[12:35:00]</a>.
*   **Title** (Title property): The main category name <a class="yt-timestamp" data-t="12:44:00">[12:44:00]</a>.
*   **Relation Column** (Relation property): Links to the Expense Details database, capturing all expenses related to needs, wants, and desires separately <a class="yt-timestamp" data-t="12:48:00">[12:48:00]</a>.
*   **Expenses Amount** (Roll-up property): Captures the actual expenses incurred, derived from the Expense Details database, summing the actual expense amount for each type of expense <a class="yt-timestamp" data-t="12:57:00">[12:57:00]</a>.
*   **Total Expenses** (Roll-up property): Derived from the Total Expenses database, showing the sum of all combined expenses <a class="yt-timestamp" data-t="13:12:00">[13:12:00]</a>.

## Primary Dashboard Presentation
The primary dashboard of the expense tracker integrates these databases for a comprehensive view <a class="yt-timestamp" data-t="13:25:00">[13:25:00]</a>.
*   **Overview of Total Expenses**: Linked to the Total Expenses database, displayed in a gallery view <a class="yt-timestamp" data-t="13:32:00">[13:32:00]</a>.
*   **Three Categories of Expenses**: Linked to the Expense Categories database, presented in a three-column gallery format <a class="yt-timestamp" data-t="13:43:00">[13:43:00]</a>.
*   **Top 10 Highlights**: Linked to the Expense Details database, displayed in a list format <a class="yt-timestamp" data-t="13:57:00">[13:57:00]</a>. Data is sorted as follows:
    *   Recent expenses: sorted by created time in descending order <a class="yt-timestamp" data-t="14:07:00">[14:07:00]</a>.
    *   Least 10 expenses: sorted by actual expenses in ascending order <a class="yt-timestamp" data-t="14:11:00">[14:11:00]</a>.
    *   Top 10 expenses: sorted by actual expenses in descending order <a class="yt-timestamp" data-t="14:13:00">[14:13:00]</a>.
*   **Actual vs. Budgeted Expenses**: Linked to the Expense Budget Classification database, set out in a gallery format <a class="yt-timestamp" data-t="14:25:00">[14:25:00]</a>.
*   **Expenses Overview (by Period)**: Linked to the Period database, displayed in a gallery format with filters applied for each quarter <a class="yt-timestamp" data-t="14:36:00">[14:36:00]</a>.
*   **Expenses Overview (by Percentage)**: Linked to the Expense Source database, presented in a gallery format and repeated for all expense heads <a class="yt-timestamp" data-t="14:55:00">[14:55:00]</a>.
*   **Frequency of Expenses**: Linked to the Frequency of Expense database, displayed in a gallery format with desired properties enabled <a class="yt-timestamp" data-t="15:05:00">[15:05:00]</a>.