---
title: Presentation of expense data in Notion
videoId: OV1faI8Z6yg
---

From: [[theaccountantguy]] <br/> 

A Notion-based expense tracker is designed to help users [[tracking_income_and_expenses_in_notion | track income and expenses]] and manage spending effectively <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>. This tracker provides a comprehensive overview of financial data through various organized sections <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

## Dashboard Overview

The primary dashboard of the expense tracker is structured to provide clear insights into financial activity <a class="yt-timestamp" data-t="00:13:30">[00:13:30]</a>.

### Total Expenses Overview
An initial section offers an overview of total expenses <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>. This includes:
*   Total budgeted expenses <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>
*   Total actual expenses <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>
*   The difference between actual and budgeted amounts <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>
*   Change in percentage <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>

This overview is linked to the "total expenses" database and is displayed in a gallery view <a class="yt-timestamp" data-t="00:13:35">[00:13:35]</a>.

### Categorized Expenses
Expenses are categorized into "needs," "desires," and "wants" <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>. These categories are linked to the "expense categories" database and presented in a three-column gallery format <a class="yt-timestamp" data-t="00:13:45">[00:13:45]</a>. This classification helps in further analysis of spending habits <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>.

### Expense Highlights
The tracker highlights specific expenses, including:
*   **Top 10 expenses:** Reflects the highest expenses incurred during a period <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>, sorted in descending order <a class="yt-timestamp" data-t="00:14:16">[00:14:16]</a>.
*   **Least 10 expenses:** Shows the lowest expenses incurred <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>, sorted by actual expenses in ascending order <a class="yt-timestamp" data-t="00:14:11">[00:14:11]</a>.
*   **Recent expenses:** Displays the most recently incurred expenses <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>, sorted by creation time in descending order <a class="yt-timestamp" data-t="00:14:07">[00:14:07]</a>.

These highlights are linked to the "expense details" database and presented in a list format <a class="yt-timestamp" data-t="00:14:04">[00:14:04]</a>.

## Detailed Expense Views

### Actual vs. Budgeted Expenses
This section displays expenses divided into six heads, showing budgeted, actual, difference, and percentage change for each <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>. This view is linked to the "expense budget classification" database and presented in a gallery format <a class="yt-timestamp" data-t="00:14:27">[00:14:27]</a>.

### Expenses Overview by Period
The tracker categorizes expenses by month, further divided into four quarters <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>. For each month and quarter, the total expenses incurred and their proportion to total expenses are shown <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>. This overview is linked to the "period database" and uses filters for each quarter <a class="yt-timestamp" data-t="00:14:38">[00:14:38]</a>.

### Expenses Overview in Percentage
This section categorizes expenses into six main heads <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>. For each head, the total expenses and their proportion to the overall total are presented <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>. This is linked to the "expense source" database and repeated for all expense heads in a gallery format <a class="yt-timestamp" data-t="00:14:56">[00:14:56]</a>.

### Frequency of Expenses
The tracker indicates how frequently expenses are incurred, categorized as:
*   Daily <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>
*   One-time <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>
*   Weekly <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>
*   Monthly <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>
*   Quarterly <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>
*   Half-yearly <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>
*   Annually <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>

Under each frequency type, the total amount incurred and the sources of expenses are displayed <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>. This section is linked to the "frequency of expense" database and shown in a gallery format <a class="yt-timestamp" data-t="00:15:07">[00:15:07]</a>.

## Underlying Database Structure for Presentation
To enable this presentation, the [[tracking_income_and_expenses_using_Notion | Notion expense tracker]] uses seven interlinked databases <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>. Key databases relevant to data presentation include:

*   **Expense Details:** Captures individual expense details like title, period, source, frequency, category, actual amount, and budgeted amount <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>, <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.
*   **Expense Source:** Categorizes expenses under six heads and includes roll-up properties for actual and budgeted amounts from the expense details, as well as calculated differences and percentage changes <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>, <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>.
*   **Frequency of Expenses:** Identifies how frequently expenses are incurred and calculates unique sources of expenses for each frequency <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>, <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a>.
*   **Total Expenses:** Reflects overall total actual and budgeted expenses, differences, and percentage changes across all six expense heads <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>, <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.
*   **Period of Expense:** Specifies monthly expenses for the entire year and helps categorize expenses by proportion <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>, <a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a>.
*   **Expense Budget Classification:** Classifies expenses into six heads, providing budgeted and actual expenses, differences, and percentage changes for each <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>, <a class="yt-timestamp" data-t="00:10:48">[00:10:48]</a>.
*   **Expense Categories:** Reflects expenses based on "needs," "wants," and "desires," with further analysis for each type <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>, <a class="yt-timestamp" data-t="00:13:10">[00:13:10]</a>.

Each database uses specific property types, including title, relation (linking to other databases), number (for amounts), roll-up (to aggregate data from related databases), and formula (for calculations like differences and percentages) <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>, <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>, <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>, <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>. For instance, the "change in percentage" is derived by dividing the difference by the budgeted expense amount <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.