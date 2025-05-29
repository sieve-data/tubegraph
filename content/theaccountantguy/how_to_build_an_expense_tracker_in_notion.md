---
title: How to build an expense tracker in Notion
videoId: OV1faI8Z6yg
---

From: [[theaccountantguy]] <br/> 

This article details how to construct a comprehensive [[tracking_expenses_with_notion | Notion expense tracker]] that allows you to monitor spending effectively <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>. The tracker provides an overview of total expenses, including budgeted vs. actual amounts, differences, and percentage changes <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>. It categorizes expenses into "needs," "desires," and "wants" <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>, highlights top 10, least 10, and recent expenses <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>, and displays actual versus budgeted expenses across six predefined heads <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>. Additionally, it offers a monthly expense overview categorized into four quarters <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>, a percentage breakdown of expenses <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>, and an analysis of expense frequency (daily, weekly, monthly, etc.) <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.

## Database Setup

To build this [[notion_expense_tracker_setup | Notion expense tracker]], you will need to create seven interconnected databases <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>. This [[database_setup_for_tracking_expense_details_and_sources_in_notion | database setup]] is fundamental for [[using_notion_for_expense_management | expense management]] and detailed analysis.

1.  **Expense Details**: Showcases individual expense entries <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>.
2.  **Expense Source**: Categorizes expenses under six main heads and provides subsequent analysis <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.
3.  **Frequency of Expenses**: Tracks how frequently an expense is incurred <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>.
4.  **Total Expenses**: Reflects total actual, budgeted, difference, and change for all six expense heads <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>.
5.  **Period of Expense**: Specifies monthly expenses for the entire year and helps categorize expenses by proportion <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>.
6.  **Expense Budget Classification**: Classifies expenses into six heads, showing budgeted, actual, differences, and percentage changes <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>.
7.  **Expense Categories**: Reflects expenses categorized as "needs," "wants," and "desires" for further analysis <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>.

### Expense Details Database

This database specifies details related to each individual expense <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.

*   **Expense Details** (Title property): Shows individual expenses incurred <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.
*   **Period of Expense** (Relation property): Links to the *Period database*, specifying the month for which an expense is incurred <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>.
*   **Expense Source** (Relation property): Links to the *Expense Source database*, indicating the specific source category of the expense <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.
*   **Frequency of Expense** (Relation property): Links to the *Frequency of Expense database*, indicating how frequently an expense occurs <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.
*   **Expense Categories** (Relation property): Links to the *Expense Categories database*, defining the category (e.g., need, want, desire) for each expense source <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
*   **Actual Expense** (Number property): Specifies the actual amount incurred in US dollars <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.
*   **Budgeted Expense** (Number property): Specifies the estimated budgeted expense for each month in US dollars <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>.
    *   The sum of actual and budgeted expenses is visible at the bottom <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>.

### Expense Source Database

This database categorizes expenses under six different heads <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>.

*   **Source of Expense** (Title property): Specifies one of the six expense heads <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>.
*   **Actual Expense** (Roll-up property): Rolled up from the *Expense Details database* to sum the actual expense amounts <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>.
*   **Budgeted Expense** (Roll-up property): Rolled up from the *Expense Details database* to sum the budgeted expense amounts <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>.
*   **Total Expenses** (Roll-up property): Derived from the *Total Expenses database*, extracting the total actual expenses <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>.
*   **Difference** (Formula property): Calculates the difference between actual expenses and budgeted expenses <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.
*   **Change in Percentage** (Formula property): Calculates the difference divided by the budgeted expense amount, displayed as a percentage <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.

### Frequency of Expenses Database

This database calculates how frequently expenses are incurred and performs further analysis <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>.

*   **Frequency** (Title property): Specifies each mode of frequency (e.g., daily, weekly, monthly) <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>.
*   **Relation Property** (Relation property): Links to the *Expense Details database*, relating different types of expenses to each frequency <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>.
*   **Sources of Expense** (Formula property): Calculates the unique sources of expenses for each frequency <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>.
    *   For example, "Commutation Expenses" listed twice counts as one source <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>, while "House Rent" and "Netflix Subscription" count as two <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a>.

### Total Expenses Database

This database calculates the total expenses incurred during a period <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>, featuring four main properties.

*   **Total Actual Expenses** (Roll-up property): Calculates the sum of total expenses from the *Expense Source database* <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>.
*   **Total Budgeted Expense** (Roll-up property): Calculates the sum of total budgeted expenses from the *Expense Source database* <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>.
*   **Difference** (Roll-up property): Calculates the difference between actual and budgeted expenses from the *Expense Source database* <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>.
*   **Change in Percentage** (Roll-up property): Calculates the percentage change from the *Expense Source database* <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>.
*   **Amount** (Formula property): Derives necessary values based on the name property (e.g., if the name is "Total Actual Expenses," it gets the actual expense value) <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>.

### Period of Expense Database

This database specifies monthly expenses for the entire year and helps categorize expenses into different categories with proportions <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>.

*   **Month** (Title property): Specifies the month for each expense <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>.
*   **Expense Details** (Relation property): Links to the *Expense Details database* to calculate expenses incurred each period <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>.
*   **Expenses for Each Month** (Roll-up property): Derived from the *Expense Details database*, summing the actual expense value for each month <a class="yt-timestamp" data-t="00:09:58">[00:09:58]</a>.
*   **Total Expenses** (Roll-up property): Calculated from the *Total Expense database*, providing the total actual expense value <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>.
*   **Proportion of the Total Expense** (Formula property): Calculates the expenses divided by the total expenses, shown as a percentage bar <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>.

### Expense Budget Classification Database

This database classifies expenses under six heads and provides details on total actual expenses, total budgeted expenses, differences, and percentage changes for each <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>.

*   **Title Property**: Specifies required properties for use <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>.
*   **Relation Property**: Links to the *Expense Source database*, specifying individual expense heads <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>.
*   **Amount** (Formula property): Derives total actual expenses, total budgeted expenses, and the difference for specific heads like travel and transportation <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>.
*   **Change in Percentage** (Formula property): Calculates the difference divided by the budgeted expense <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>.
*   **Roll-up Properties**:
    *   **Actual Expenses**: Roll-up from *Expense Source database* summing expense values <a class="yt-timestamp" data-t="00:11:45">[00:11:45]</a>.
    *   **Budgeted Expenses**: Roll-up from *Expense Source database* summing expense values <a class="yt-timestamp" data-t="00:11:53">[00:11:53]</a>.
    *   **Change in Percentage**: Roll-up from *Expense Source database* showing the original percentage change value <a class="yt-timestamp" data-t="00:12:11">[00:12:11]</a>.
    *   **Difference**: Roll-up property showing the difference between budgeted and actual expenses <a class="yt-timestamp" data-t="00:12:21">[00:12:21]</a>.
    *   These columns are repeated for all six expense heads <a class="yt-timestamp" data-t="00:12:27">[00:12:27]</a>.

### Expense Categories Database

This database specifies expenses into the three categories: "needs," "wants," and "desires" <a class="yt-timestamp" data-t="00:12:35">[00:12:35]</a>.

*   **Title Property**: Defines the categories <a class="yt-timestamp" data-t="00:12:44">[00:12:44]</a>.
*   **Relation Column**: Links to the *Expense Details database* to capture all expenses related to needs, wants, and desires separately <a class="yt-timestamp" data-t="00:12:48">[00:12:48]</a>.
*   **Expenses Amount** (Roll-up property): Derived from the *Expense Details database*, summing the actual expense amount for each type of expense <a class="yt-timestamp" data-t="00:12:57">[00:12:57]</a>.
*   **Total Expenses** (Roll-up property): Derived from the *Total Expenses database*, summing all combined expenses <a class="yt-timestamp" data-t="00:13:12">[00:13:12]</a>.

## Primary Dashboard Presentation

The primary dashboard serves as the central hub for your [[tracking_personal_finances_in_notion | personal finance tracking]] and [[setting_up_a_travel_expense_tracker_in_notion | expense management]].

*   **Overview of Total Expenses**: Linked to the *Total Expenses database* and set out in a gallery view <a class="yt-timestamp" data-t="00:13:32">[00:13:32]</a>.
*   **Three Categories of Expenses**: Linked to the *Expense Categories database* and displayed in a gallery format <a class="yt-timestamp" data-t="00:13:43">[00:13:43]</a>.
    *   Arrange this section in a three-column layout by typing `/three column` <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a>.
*   **Top 10 Highlights**: Linked to the *Expense Details database* and set out in a list format <a class="yt-timestamp" data-t="00:14:03">[00:14:03]</a>.
    *   **Recent Expenses**: Sorted by creation time in descending order <a class="yt-timestamp" data-t="00:14:07">[00:14:07]</a>.
    *   **Least 10 Expenses**: Sorted by actual expenses in ascending order <a class="yt-timestamp" data-t="00:14:11">[00:14:11]</a>.
    *   **Top 10 Expenses**: Sorted by actual expenses in descending order <a class="yt-timestamp" data-t="00:14:16">[00:14:16]</a>.
*   **Actual Versus Budgeted Expenses**: Linked to the *Expense Budget Classification database* and displayed in a gallery format <a class="yt-timestamp" data-t="00:14:25">[00:14:25]</a>.
*   **Expenses Overview (Monthly)**: Linked to the *Period database* and displayed in a gallery format <a class="yt-timestamp" data-t="00:14:36">[00:14:36]</a>.
    *   Apply filters for each quarter to show necessary months <a class="yt-timestamp" data-t="00:14:42">[00:14:42]</a>.
*   **Expenses Overview (By Source)**: Linked to the *Expense Source database* and set out in a gallery format, repeated for all expense heads <a class="yt-timestamp" data-t="00:14:55">[00:14:55]</a>.
*   **Frequency of Expenses**: Linked to the *Frequency of Expense database* and given in a gallery format with desired properties enabled <a class="yt-timestamp" data-t="00:15:05">[00:15:05]</a>.

This comprehensive [[credit_card_expense_tracking_in_notion | Notion expense tracker]] can be used for various purposes, including [[tracking_construction_project_expenses_in_notion | tracking construction project expenses in Notion]] or as a general [[building_an_income_tracker_in_notion | personal finance management tool]]. A template for this tracker is often available for download <a class="yt-timestamp" data-t="00:15:16">[00:15:16]</a>.