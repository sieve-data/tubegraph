---
title: Creating a Notion expense tracker
videoId: OV1faI8Z6yg
---

From: [[theaccountantguy]] <br/> 

This article outlines how to build a comprehensive expense tracker in Notion, allowing users to [[Expense Tracking in Notion | track income and expenses using Notion]], analyze spending habits, and manage budgeted funds effectively <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>. The tracker offers an overview of total expenses, categorized spending, and detailed analysis by period and frequency <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

## Key Features of the Tracker

The Notion expense tracker provides several distinct sections for comprehensive financial oversight:
*   **Total Expenses Overview** This section displays total budgeted expenses, total actual expenses, the difference between them, and the percentage change <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.
*   **Categorized Expenses** Expenses are categorized into "needs," "desires," and "wants" <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.
*   **Top 10 Expenses Highlights** This feature reflects the top 10 expenses incurred, the least 10 expenses, and recent expenses within a specific period <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.
*   **Actual vs. Budgeted Expenses** Expenses are divided into six specific heads, showing total budgeted, total actual, differences, and percentage changes for each <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.
*   **Expenses Overview by Period** This section categorizes expenses by month, divided into four quarters, indicating total expenses incurred and their proportion to total expenses <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>.
*   **Expenses Overview in Percentage** Displays expenses categorized under six heads, detailing total expenses and their proportion to the overall total <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.
*   **Frequency of Expenses** This feature tracks how frequently expenses are incurred (daily, one-time, weekly, monthly, quarterly, half-yearly, annually), showing the total amount and sources for each frequency <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.

## Building the Notion Expense Tracker

To construct this expense tracker, seven interconnected databases are required <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.

### Required Databases
1.  **Expense Details Database** <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>
2.  **Expense Source Database** <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>
3.  **Frequency of Expenses Database** <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>
4.  **Total Expenses Database** <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>
5.  **Period of Expense Database** <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>
6.  **Expense Budget Classification Database** <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>
7.  **Expense Categories Database** <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>

### Database Structures and Properties

#### 1. Expense Details Database
This database specifies the details of each individual expense <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.
*   **Expense Details** (Title property): Shows individual expenses incurred <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.
*   **Period of Expense** (Relation property): Links to the `Period of Expense` database, specifying the month for each expense <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>.
*   **Expense Source** (Relation property): Links to the `Expense Source` database, specifying the source under which an expense is incurred <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.
*   **Frequency of Expense** (Relation property): Links to the `Frequency of Expenses` database, indicating how frequently an expense is incurred <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.
*   **Expense Categories** (Relation property): Links to the `Expense Categories` database, specifying the category for each individual source of expense <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
*   **Actual Expense** (Number property): Specifies the actual amount of expense incurred in US dollars <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.
*   **Budgeted Expense** (Number property): Specifies the budgeted expense estimated for each month in US dollars <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>.
    *   The sum of actual and budgeted expenses is displayed at the bottom <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>.

#### 2. Expense Source Database
This database specifies the six different sources of expenses under which an expense is incurred <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>.
*   **Source of Expense** (Title property): Specifies one of the six expense heads <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>.
*   **Actual Expense** (Roll-up property): Rolled up from the `Expense Details` database, showing the sum of actual expenses <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>.
*   **Budgeted Expense** (Roll-up property): Rolled up from the `Expense Details` database, showing the sum of budgeted expenses <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>.
*   **Total Expenses** (Roll-up property): Derived from the `Total Expenses` database, extracting the total actual expenses amount as its original value <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>.
*   **Difference** (Formula property): Calculates the difference between actual and budgeted expenses <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.
*   **Change in Percentage** (Formula property): Calculates the difference divided by the budgeted expense amount, displayed as a percentage <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.

#### 3. Frequency of Expenses Database
This database calculates how frequently an expense is incurred and performs further analysis <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>.
*   **Frequency** (Title property): Specifies each individual mode of frequency (e.g., daily, weekly) <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>.
*   **Expense Details** (Relation property): Relates to the `Expense Details` database, linking different types of expenses to their frequency <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>.
*   **Sources of Expense** (Formula property): Calculates the unique sources of expenses for each frequency mode <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>.

#### 4. Total Expenses Database
This database calculates the total expenses incurred during a period <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.
*   **Name Property**: Includes `Total Actual Expenses`, `Total Budgeted Expenses`, `Difference`, and `Change in Percentage` <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>.
*   **Total Actual Expenses** (Roll-up property): Calculates total expenses from the `Expense Source` database, showing the sum value <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>.
*   **Total Budgeted Expense** (Roll-up property): Calculates total budgeted expenses from the `Expense Source` database, showing the sum value <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>.
*   **Amount** (Formula property): Derives values based on the name property:
    *   Actual expense value if `Name` is "Total Actual Expenses" <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>.
    *   Budgeted expense value if `Name` is "Total Budgeted Expenses" <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>.
    *   Difference if `Name` is "Difference" <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>.
    *   Change in percentage if `Name` is "Change in Percentage" (calculated as difference divided by budgeted expense) <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>.

#### 5. Period of Expense Database
This database specifies expenses for each month and provides further analysis <a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a>.
*   **Month** (Title property): Specifies the month for each expense <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>.
*   **Expense Details** (Relation property): Relates to the `Expense Details` database, calculating expenses incurred each period <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>.
*   **Expenses for Each Month** (Roll-up property): Derived from `Expense Details` database, calculating the sum of actual expense values <a class="yt-timestamp" data-t="00:09:58">[00:10:00]</a>.
*   **Total Expenses** (Roll-up property): Calculated from the `Total Expenses` database, providing the total actual expense value <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>.
*   **Proportion of Total Expense** (Formula property): Calculates expenses divided by total expenses, displayed as a percentage <a class="yt-timestamp" data-t="00:10:18">[00:10:18]</a>.

#### 6. Expense Budget Classification Database
This database classifies expenses under six heads and provides details on total actual, total budgeted, difference, and percentage change for each <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>.
*   **Title Property**: Specifies required properties for use <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>.
*   **Relation Property**: Relates to the `Expense Source` database, specifying individual heads of expense <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>.
*   **Amount** (Formula property): Derives total actual, total budgeted, and difference values for each expense head <a class="yt-timestamp" data-t="00:11:13">[00:11:17]</a>.
*   **Change in Percentage** (Formula property): Calculates the difference divided by the budgeted expense <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>.
*   **Actual Expenses** (Roll-up property): Derived from the `Expense Source` database, calculating the sum of expense values <a class="yt-timestamp" data-t="00:11:45">[00:11:45]</a>.
*   **Budgeted Expenses** (Roll-up property): Also derived from the `Expense Source` database, calculating the sum of budgeted expense values <a class="yt-timestamp" data-t="00:11:53">[00:11:53]</a>.
*   **Change in Percentage** (Roll-up property): Derived from the `Expense Source` database, showing the original value of percentage change <a class="yt-timestamp" data-t="00:12:11">[00:12:11]</a>.
*   **Difference Column** (Roll-up property): Shows the difference between budgeted and actual expenses <a class="yt-timestamp" data-t="00:12:21">[00:12:21]</a>.
    *   These columns must be repeated for all six expense heads <a class="yt-timestamp" data-t="00:12:27">[00:12:27]</a>.

#### 7. Expense Categories Database
This database specifies the three types of expenses: needs, wants, and desires <a class="yt-timestamp" data-t="00:12:35">[00:12:35]</a>.
*   **Title Property** <a class="yt-timestamp" data-t="00:12:44">[00:12:44]</a>.
*   **Relation Column** (Relation property): Relates to the `Expense Details` database, capturing all expenses related to needs, wants, and desires separately <a class="yt-timestamp" data-t="00:12:48">[00:12:48]</a>.
*   **Expenses Amount** (Roll-up property): Shows actual expenses incurred, derived from the `Expense Details` database, calculating the sum for each type of expense <a class="yt-timestamp" data-t="00:12:57">[00:12:57]</a>.
*   **Total Expenses** (Roll-up property): Derived from the `Total Expenses` database, showing the sum of all combined expenses <a class="yt-timestamp" data-t="00:13:12">[00:13:12]</a>.

## Primary Dashboard Presentation

The primary dashboard of the expense tracker is organized using linked databases and various view formats to provide a clear and intuitive overview <a class="yt-timestamp" data-t="00:13:28">[00:13:28]</a>.

*   **Overview of Total Expenses**: Linked to the `Total Expenses` database and displayed in a gallery view <a class="yt-timestamp" data-t="00:13:32">[00:13:32]</a>.
*   **Categorized Expenses**: The three categories of expenses (needs, wants, desires) are linked to the `Expense Categories` database and presented in a gallery format <a class="yt-timestamp" data-t="00:13:43">[00:13:43]</a>. This section can be formatted into a three-column layout using `/three column` command <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a>.
*   **Top 10 Highlights**: Linked to the `Expense Details` database and set in a list format <a class="yt-timestamp" data-t="00:14:03">[00:14:03]</a>. Data is sorted as follows:
    *   Recent expenses by "created time" in descending order <a class="yt-timestamp" data-t="00:14:07">[00:14:07]</a>.
    *   Least 10 expenses by "actual expenses" in ascending order <a class="yt-timestamp" data-t="00:14:11">[00:14:11]</a>.
    *   Top 10 expenses sorted in descending order <a class="yt-timestamp" data-t="00:14:16">[00:14:16]</a>.
*   **Actual vs. Budgeted Expenses**: Linked to the `Expense Budget Classification` database and displayed in a gallery format <a class="yt-timestamp" data-t="00:14:25">[00:14:25]</a>.
*   **Expenses Overview by Period**: Linked to the `Period of Expense` database and presented in a gallery format <a class="yt-timestamp" data-t="00:14:36">[00:14:36]</a>. Filters are applied for each quarter to show relevant months <a class="yt-timestamp" data-t="00:14:42">[00:14:42]</a>.
*   **Expenses Overview by Source**: Linked to the `Expense Source` database and displayed in a gallery format, repeated for all expense heads <a class="yt-timestamp" data-t="00:14:55">[00:14:55]</a>.
*   **Frequency of Expenses**: Linked to the `Frequency of Expenses` database, displayed in a gallery format with desired properties enabled <a class="yt-timestamp" data-t="00:15:05">[00:15:05]</a>.

This comprehensive guide covers [[Creating a Notion Income Tracker | creating a Notion income tracker]] for robust financial management, combining personal and business expense tracking <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>.