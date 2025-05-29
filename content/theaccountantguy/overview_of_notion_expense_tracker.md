---
title: Overview of Notion Expense Tracker
videoId: OV1faI8Z6yg
---

From: [[theaccountantguy]] <br/> 

This wiki article provides an [[overview_of_notion_budget_tracker_template | overview]] of a Notion expense tracker, detailing its features, underlying databases, and dashboard presentation <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>. The tracker helps users manage their spending and track financial data <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.

## Tracker Features and Sections

The Notion expense tracker includes several key sections for comprehensive financial tracking <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>:

*   **Overview of Total Expenses**
    *   Displays total budgeted expenses <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>.
    *   Shows total actual expenses <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.
    *   Calculates differences and change in percentage <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.
*   **Categorized Expenses**
    *   Expenses are categorized as "needs," "desires," and "wants" <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.
*   **Top 10 Expenses Highlights**
    *   Reflects the top 10 expenses incurred during a period <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.
    *   Highlights the least 10 expenses incurred <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.
    *   Shows recent expenses <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>.
*   **Actual vs. Budget Expenses**
    *   Expenses are divided into six predefined heads <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>.
    *   Indicates total budgeted expenses <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.
    *   Shows total actual expenses <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>.
    *   Calculates the difference and change in percentage <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.
*   **Expenses Overview During the Period**
    *   Expenses are categorized by month, divided into four quarters <a class="yt-timestamp" data-t="00:01:58">[00:02:02]</a>.
    *   For each month, it displays the total expenses incurred and their proportion to total expenses <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.
*   **Expenses Overview in Percentage**
    *   Expenses are categorized into six heads <a class="yt-timestamp" data-t="00:02:19">[00:02:21]</a>.
    *   Under each head, it shows total expenses and their proportion to total expenses <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>.
*   **Frequency of Expenses**
    *   Indicates how frequently an expense is incurred, categorized as daily, one-time, weekly, monthly, quarterly, half-yearly, and annually <a class="yt-timestamp" data-t="00:02:32">[00:02:37]</a>.
    *   Under each frequency, it shows the total amount of expenses and their sources <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.

## Building the Expense Tracker: Required Databases

To build this Notion expense tracker, seven specific databases are required <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>:

1.  **Expense Details** <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>
    *   Showcases details related to individual expenses <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.
    *   **Properties:**
        *   `Expense Details` (Title property): Shows individual expenses incurred <a class="yt-timestamp" data-t="00:04:27">[00:04:31]</a>.
        *   `Period of Expense` (Relation property): Links to the `Period of Expense` database, specifying the month an expense was incurred <a class="yt-timestamp" data-t="00:04:36">[00:04:38]</a>.
        *   `Expense Source` (Relation property): Links to the `Expense Source` database, specifying the category under which an expense is incurred <a class="yt-timestamp" data-t="00:04:46">[00:04:48]</a>.
        *   `Frequency of Expense` (Relation property): Links to the `Frequency of Expense` database, indicating how frequently an expense occurs <a class="yt-timestamp" data-t="00:04:57">[00:04:59]</a>.
        *   `Expense Categories` (Relation property): Links to the `Expense Categories` database, specifying the category (needs, wants, desires) for each expense source <a class="yt-timestamp" data-t="00:05:07">[00:05:09]</a>.
        *   `Actual Expense` (Number property): Specifies the actual amount incurred in US dollars <a class="yt-timestamp" data-t="00:05:15">[00:05:17]</a>.
        *   `Budgeted Expense` (Number property): Specifies the estimated budgeted expense for each month in US dollars <a class="yt-timestamp" data-t="00:05:27">[00:05:31]</a>.
    *   The sum of actual and budgeted expenses can be found at the bottom <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>.

2.  **Expense Source** <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>
    *   Categorizes expenses under six heads with subsequent analysis <a class="yt-timestamp" data-t="00:03:10">[00:03:12]</a>.
    *   **Properties:**
        *   `Source of Expense` (Title property): Specifies one of the six expense heads <a class="yt-timestamp" data-t="00:05:54">[00:05:57]</a>.
        *   `Actual Expense` (Roll-up property): Rolled up from `Expense Details`, showing the sum of actual expenses <a class="yt-timestamp" data-t="00:06:04">[00:06:07]</a>.
        *   `Budgeted Expense` (Roll-up property): Rolled up from `Expense Details`, showing the sum of budgeted expenses <a class="yt-timestamp" data-t="00:06:14">[00:06:17]</a>.
        *   `Total Expenses` (Roll-up property): Derived from the `Total Expenses` database, extracting the total actual expenses <a class="yt-timestamp" data-t="00:06:25">[00:06:27]</a>.
        *   `Difference` (Formula property): Calculates the difference between actual and budgeted expenses <a class="yt-timestamp" data-t="00:06:40">[00:06:42]</a>.
        *   `Change in Percentage` (Formula property): Calculates `Difference` divided by `Budgeted Expense`, represented as a percentage <a class="yt-timestamp" data-t="00:06:51">[00:06:53]</a>.

3.  **Frequency of Expenses** <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>
    *   Showcases how frequently expenses are incurred <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.
    *   **Properties:**
        *   `Frequency` (Title property): Specifies each mode of frequency (e.g., daily, weekly) <a class="yt-timestamp" data-t="00:07:20">[00:07:22]</a>.
        *   `Expense Details` (Relation property): Links to the `Expense Details` database, relating expenses to their frequency type <a class="yt-timestamp" data-t="00:07:26">[00:07:27]</a>.
        *   `Sources of Expense` (Formula property): Calculates the unique sources of expenses for each frequency <a class="yt-timestamp" data-t="00:07:35">[00:07:37]</a>.

4.  **Total Expenses** <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>
    *   Reflects total expenses incurred for all six heads, categorized as actual, budgeted, difference, and change <a class="yt-timestamp" data-t="00:03:29">[00:03:29]</a>.
    *   **Properties:**
        *   `Total Actual Expenses` (Roll-up property): Calculates total expenses from the `Expense Source` database <a class="yt-timestamp" data-t="00:08:36">[00:08:39]</a>.
        *   `Total Budgeted Expense` (Roll-up property): Calculates total budgeted expenses from the `Expense Source` database <a class="yt-timestamp" data-t="00:08:47">[00:08:49]</a>.
        *   `Amount` (Formula property): Derives values based on the name property: actual expense if "total actual expenses," budgeted if "total budgeted expenses," difference if "difference," and change in percentage if "change in percentage" (calculated as difference/budgeted expense) <a class="yt-timestamp" data-t="00:08:57">[00:08:59]</a>.

5.  **Period of Expense** <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>
    *   Specifies monthly expenses for the entire year and helps categorize expenses with proportions <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.
    *   **Properties:**
        *   `Month` (Title property): Specifies the month for each expense <a class="yt-timestamp" data-t="00:09:42">[00:09:45]</a>.
        *   `Expense Details` (Relation property): Links to `Expense Details` database, calculating expenses incurred each period <a class="yt-timestamp" data-t="00:09:48">[00:09:50]</a>.
        *   `Expenses for each month` (Roll-up property): Derived from `Expense Details`, summing actual expense values <a class="yt-timestamp" data-t="00:09:58">[00:10:00]</a>.
        *   `Total Expenses` (Roll-up property): Derived from `Total Expense` database, giving total actual expense value <a class="yt-timestamp" data-t="00:10:10">[00:10:12]</a>.
        *   `Proportion of the Total Expense` (Formula property): Calculates `Expenses divided by Total Expenses`, denoted in percentage <a class="yt-timestamp" data-t="00:10:18">[00:10:20]</a>.

6.  **Expense Budget Classification** <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>
    *   Classifies expenses under six heads, providing details on total actual, total budgeted, difference, and percentage change for each <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
    *   **Properties:**
        *   Title property: Specifies required properties for use <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>.
        *   Relation property: Links to the `Expense Source` database, specifying individual heads of expense <a class="yt-timestamp" data-t="00:11:06">[00:11:08]</a>.
        *   `Amount` (Formula property): Derives total actual/budgeted expenses or the difference for each head <a class="yt-timestamp" data-t="00:11:13">[00:11:17]</a>.
        *   `Change in Percentage` (Formula property): Calculates `Difference` divided by `Budgeted Expense` <a class="yt-timestamp" data-t="00:11:38">[00:11:40]</a>.
        *   `Actual Expenses` (Roll-up property): Derives summed actual expense values from `Expense Source` database <a class="yt-timestamp" data-t="00:11:45">[00:11:47]</a>.
        *   `Budgeted Expenses` (Roll-up property): Derives summed budgeted expense values from `Expense Source` database <a class="yt-timestamp" data-t="00:11:53">[00:11:56]</a>.
        *   `Change in Percentage` (Roll-up property): Derived from `Expense Source`, showing original percentage change <a class="yt-timestamp" data-t="00:12:11">[00:12:13]</a>.
        *   `Difference` (Roll-up property): Shows the difference between budgeted and actual expenses <a class="yt-timestamp" data-t="00:12:21">[00:12:22]</a>.
    *   These columns need to be repeated for all six expense heads <a class="yt-timestamp" data-t="00:12:27">[00:12:27]</a>.

7.  **Expense Categories** <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>
    *   Reflects expenses as per "needs," "wants," and "desires," performing further analysis for each type <a class="yt-timestamp" data-t="00:04:05">[00:04:07]</a>.
    *   **Properties:**
        *   Title property: Identifies the category <a class="yt-timestamp" data-t="00:12:44">[00:12:46]</a>.
        *   Relation column: Links to `Expense Details`, capturing expenses related to needs, wants, and desires separately <a class="yt-timestamp" data-t="00:12:48">[00:12:50]</a>.
        *   `Expenses Amount` (Roll-up property): Derived from `Expense Details`, summing actual expense amounts for each category <a class="yt-timestamp" data-t="00:12:57">[00:13:00]</a>.
        *   `Total Expenses` (Roll-up property): Derived from `Total Expenses` database, summing all combined expenses <a class="yt-timestamp" data-t="00:13:12">[00:13:15]</a>.

## Primary Dashboard Presentation

The primary dashboard of the Notion expense tracker organizes these databases for an [[using_notion_for_expense_tracking | easy-to-use experience]] <a class="yt-timestamp" data-t="00:13:28">[00:13:30]</a>:

*   **Overview of Total Expenses:** Linked to the `Total Expenses` database, displayed in a gallery view <a class="yt-timestamp" data-t="00:13:32">[00:13:35]</a>.
*   **Three Categories of Expenses:** Linked to the `Expense Categories` database, presented in a three-column gallery format <a class="yt-timestamp" data-t="00:13:43">[00:13:45]</a>.
*   **Top 10 Highlights:** Linked to the `Expense Details` database, set out in a list format <a class="yt-timestamp" data-t="00:14:03">[00:14:05]</a>.
    *   Recent expenses are sorted by created time in descending order <a class="yt-timestamp" data-t="00:14:07">[00:14:09]</a>.
    *   Least 10 expenses are sorted by actual expenses in ascending order <a class="yt-timestamp" data-t="00:14:11">[00:14:11]</a>.
    *   Top 10 expenses are sorted by actual expenses in descending order <a class="yt-timestamp" data-t="00:14:13">[00:14:16]</a>.
*   **Actual vs. Budgeted Expenses:** Linked to the `Expense Budget Classification` database, displayed in a gallery format <a class="yt-timestamp" data-t="00:14:25">[00:14:27]</a>.
*   **Expenses Overview:** Linked to the `Period` database, presented in a gallery format <a class="yt-timestamp" data-t="00:14:36">[00:14:39]</a>. Filters are applied for each quarter to show necessary months <a class="yt-timestamp" data-t="00:14:42">[00:14:42]</a>.
*   **Expenses Overview Section:** Linked to the `Expense Source` database, set out in a gallery format and repeated for all expense heads <a class="yt-timestamp" data-t="00:14:55">[00:14:56]</a>.
*   **Frequency of Expenses:** Linked to the `Frequency of Expense` database, displayed in a gallery format with desired properties enabled <a class="yt-timestamp" data-t="00:15:05">[00:15:07]</a>.

This detailed [[notion_expense_tracker_overview | Notion expense tracker overview]] demonstrates how to build and [[using_notion_for_expense_management | use Notion for expense management]] effectively <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>. For more on [[budgeting_and_expense_management_in_notion | budgeting and expense management in Notion]], consider exploring the template further.