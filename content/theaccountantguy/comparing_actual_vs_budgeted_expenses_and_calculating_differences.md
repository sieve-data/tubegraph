---
title: Comparing actual vs budgeted expenses and calculating differences
videoId: OV1faI8Z6yg
---

From: [[theaccountantguy]] <br/> 

An expense tracker provides a comprehensive overview of financial expenditures, comparing planned budgets against actual spending to highlight differences and percentage changes <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

## Key Overview Components

The expense tracker features several sections designed to offer a detailed financial picture:
*   **Total Expenses Overview** <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>: Displays total budgeted expenses, total actual expenses, the differences between them, and the percentage change <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.
*   **Categorized Expenses** <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>: Expenses are categorized into "needs," "desires," and "wants" <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>.
*   **Expense Highlights** <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>: Includes the top 10 expenses, the least 10 expenses, and recent expenses incurred during a specific period <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.
*   **[[understanding_and_tracking_budgeted_versus_actual_expenses | Actual Versus Budget Expenses]]** <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>: This section breaks down expenses into six main heads, showing the total budgeted expenses, total actual expenses, the difference, and the percentage change for each <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.
*   **Expenses Overview During the Period** <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>: Expenses are categorized by month and divided into four quarters, detailing total expenses incurred and their proportion to total expenses <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.
*   **Expenses Overview in Percentage** <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>: Presents expenses categorized by the six heads, showing total expenses and their proportion in percentage <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.
*   **Frequency of Expenses** <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>: Indicates how frequently an expense is incurred (daily, one-time, weekly, monthly, quarterly, half-yearly, annually), along with the total amount and sources for each frequency type <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>.

## Building the Expense Tracker Databases

To construct this expense tracker, seven specific databases are required <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>:

1.  **Expense Details Database** <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>
    *   **Title Property**: Shows individual expenses incurred <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>.
    *   **Period of Expense**: A relation property linked to the period database, specifying the month an expense was incurred <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>.
    *   **Expense Source**: A relation property linked to the expense source database, indicating the source category of an expense <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.
    *   **Frequency of Expense**: A relation property linked to the frequency of expense database, showing how frequently an expense is incurred <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.
    *   **Expense Categories**: A relation property linked to the expense categories database, specifying the category for each expense source <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
    *   **Actual Expense**: A number property for the actual amount spent (in US dollars) <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.
    *   **Budgeted Expense**: A number property for the estimated budgeted amount for each month (in US dollars) <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>.
    *   The sum of actual and budgeted expenses is shown at the bottom <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>.

2.  **Expense Source Database** <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>
    *   Specifies six different sources (heads) of expenses <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>.
    *   **Source of Expense**: A title property for each of the six expense heads <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>.
    *   **Actual Expense**: A roll-up property from the expense details database, giving the sum of actual expenses for each source <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>.
    *   **Budgeted Expense**: A roll-up property from the expense details database, giving the sum of budgeted expenses for each source <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>.
    *   **Total Expenses**: A roll-up property from the total expenses database, extracting total actual expenses <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>.
    *   **Difference**: A formula property showing the difference between actual and budgeted expenses <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.
    *   **Change in Percentage**: A formula property calculated as the difference divided by the budgeted expense amount, displayed as a percentage <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.

3.  **Frequency of Expenses Database** <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>
    *   Calculates how frequently expenses are incurred <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a>.
    *   **Frequency**: A title property specifying each mode of frequency (e.g., daily, weekly) <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>.
    *   **Expense Details**: A relation property linked to the expense details database, associating expenses with their frequency <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>.
    *   **Sources of Expense**: A formula property calculating the unique sources of expenses for each frequency <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>.

4.  **Total Expenses Database** <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>
    *   Reflects total expenses incurred across all six heads <a class="yt-timestamp" data-t="00:03:29">[00:03:29]</a>.
    *   Includes properties for total actual expenses, total budgeted expenses, difference, and change in percentage <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>.
    *   **Total Actual Expenses**: A roll-up property calculating the sum of total expenses from the expense source database <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>.
    *   **Total Budgeted Expense**: A roll-up property calculating the sum of total budgeted expenses from the expense source database <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>.
    *   **Amount**: A formula property deriving values (actual, budgeted, difference, or percentage change) based on the property's name <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>.

5.  **Period of Expense Database** <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>
    *   Specifies monthly expenses for the entire year and categorizes expenses with their proportion <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.
    *   **Month**: A title property for each expense month <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>.
    *   **Expense Details**: A relation property linked to the expense details database, capturing expenses incurred each period <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>.
    *   **Expenses for Each Month**: A roll-up property from the expense details database, calculating the sum of actual expenses for each month <a class="yt-timestamp" data-t="00:09:58">[00:09:58]</a>.
    *   **Total Expenses**: A roll-up property from the total expense database, giving the total actual expense value <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>.
    *   **Proportion of the Total Expense**: A formula property calculating monthly expenses divided by total expenses, displayed as a percentage <a class="yt-timestamp" data-t="00:10:18">[00:10:18]</a>.

6.  **Expense Budget Classification Database** <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>
    *   Classifies expenses under six heads, providing details on total actual expenses, total budgeted expenses, differences, and percentage change for each head <a class="yt-timestamp" data-t="00:10:48">[00:10:48]</a>.
    *   **Title Property**: For specifying required properties <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>.
    *   **Relation Property**: Linked to the expense source database, specifying individual heads of expense <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>.
    *   **Amount**: A formula property deriving total actual expenses, total budgeted expenses, and the difference for specific expense heads <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>.
    *   **Change in Percentage**: A formula calculated as the difference divided by the budgeted expense <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>.
    *   **Actual Expenses**: A roll-up property deriving values from the expense source database, calculating the sum <a class="yt-timestamp" data-t="00:11:45">[00:11:45]</a>.
    *   **Budgeted Expenses**: A roll-up property deriving values from the expense source database, calculating the sum <a class="yt-timestamp" data-t="00:11:53">[00:11:53]</a>.
    *   **Change in Percentage**: A roll-up value from the expense source database, showing the original percentage change <a class="yt-timestamp" data-t="00:12:11">[00:12:11]</a>.
    *   **Difference Column**: A roll-up property showing the difference between budgeted and actual expenses <a class="yt-timestamp" data-t="00:12:21">[00:12:21]</a>.

7.  **Expense Categories Database** <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>
    *   Reflects expenses categorized as needs, wants, and desires <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.
    *   **First Column**: A title property <a class="yt-timestamp" data-t="00:12:44">[00:12:44]</a>.
    *   **Relation Column**: Linked to the expense details database, capturing expenses for needs, wants, and desires separately <a class="yt-timestamp" data-t="00:12:48">[00:12:48]</a>.
    *   **Expenses Amount**: A roll-up property derived from the expense details database, showing the sum of actual expenses for each category type <a class="yt-timestamp" data-t="00:12:57">[00:12:57]</a>.
    *   **Total Expenses**: A roll-up property from the total expenses database, giving the sum of all combined expenses <a class="yt-timestamp" data-t="00:13:12">[00:13:12]</a>.

## Dashboard Presentation

The primary dashboard of the expense tracker is organized for easy viewing:
*   **Overview of Total Expenses**: Linked to the total expenses database and displayed in a gallery view <a class="yt-timestamp" data-t="00:13:32">[00:13:32]</a>.
*   **Three Categories of Expenses**: Linked to the expense categories database, presented in a three-column gallery format <a class="yt-timestamp" data-t="00:13:43">[00:13:43]</a>.
*   **Top 10 Highlights**: Linked to the expense details database and shown in a list format <a class="yt-timestamp" data-t="00:13:57">[00:13:57]</a>.
    *   Recent expenses are sorted by created time in descending order <a class="yt-timestamp" data-t="00:14:07">[00:14:07]</a>.
    *   The least 10 expenses are sorted by actual expenses in ascending order <a class="yt-timestamp" data-t="00:14:11">[00:14:11]</a>.
    *   The top 10 expenses are sorted in descending order <a class="yt-timestamp" data-t="00:14:13">[00:14:13]</a>.
*   **[[comparing_budgeted_vs_actual_expenses | Actual Versus Budgeted Expenses]]**: Linked to the expense budget classification database and set out in a gallery format <a class="yt-timestamp" data-t="00:14:25">[00:14:25]</a>.
*   **Expenses Overview**: Linked to the period database and displayed in a gallery format, with filters applied for each quarter <a class="yt-timestamp" data-t="00:14:36">[00:14:36]</a>.
*   **Expenses Overview Section**: Linked to the expense source database, displayed in a gallery format, and repeated for all six expense heads <a class="yt-timestamp" data-t="00:14:55">[00:14:55]</a>.
*   **Frequency of Expenses**: Linked to the frequency of expense database, presented in a gallery format with desired properties enabled <a class="yt-timestamp" data-t="00:15:05">[00:15:05]</a>.