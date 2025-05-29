---
title: Bills summary and categories in Notion
videoId: RqN1qUpTkSI
---

From: [[theaccountantguy]] <br/> 

This article details how to create and manage a bills tracker in Notion, focusing on the summary and categorization features. The system is designed to provide a comprehensive overview of financial obligations and distributions <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.

## Overview of the Notion Bills Tracker

The [[notion_bills_tracker_tutorial | Notion bills tracker]] allows users to organize and monitor their bills efficiently. It provides a primary dashboard that displays key financial insights <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>.

### Summary Section

The summary section of the Notion bills tracker is divided into three subsections <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>:
*   **Upcoming Bills:** Shows bills that are approaching their due date, including the amount, due date, remaining days, and payment status <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a> <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>.
*   **Past Due Bills:** Displays bills that have exceeded their due date, showing the amount, original due date, number of days past due, and payment status <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a> <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>.
*   **Bills Paid:** Lists all bills that have been successfully paid on time, including the amount, due date, and status of payment <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a> <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>. Clicking on a bill's status updates it to "paid," moving it to this section <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a> <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.

### Bills Distribution

The system categorizes bills in several ways to provide a detailed financial overview:

*   **By Priority:** Bills are classified by [[managing_bill_payments_and_priorities_with_notion | priority]] as low, medium, or high <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. This section shows the amount associated with each priority level and the percentage of bills accounted for <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a> <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>.
*   **By Category:** Bills are divided into six predefined categories <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a> <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>:
    *   Entertainment <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>
    *   Food and Groceries <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>
    *   Utility Bills <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>
    *   Travel and Transportation <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>
    *   Loans and Debts <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>
    *   Others <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>
    Each category displays the total amount paid and the percentage of bills paid within that category <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a> <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>.
*   **By Period:** Bills are further categorized by their payment frequency <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a> <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>:
    *   Daily <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>
    *   Weekly <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>
    *   Monthly <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>
    *   Quarterly <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>
    *   Half Yearly <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>
    *   Annually <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>
    *   One Time <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>
    Each period head shows the budgeted expenses, actual expenses, the change observed, upcoming bills, bills paid (in numbers), and bills paid as a percentage <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a> <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.

## Building the Notion Bills Tracker

[[creating_a_bills_database_in_notion | Building the Notion bills tracker]] primarily requires one main database, the "Bills database," along with several supplemental databases to store and process information <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.

### Bills Details Database

The "Bills Details" database is central to tracking individual expenses <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>. It includes the following columns to capture [[expense_details_and_categorization_in_notion | expense details and categorization in Notion]]:
*   **Description:** A text field for the expense description <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.
*   **Category:** Links to one of the six expense categories <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>.
*   **Priorities:** Links to the expense priority (low, medium, or high) <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>.
*   **Type of Expense:** Specifies the periodicity (daily, weekly, monthly, etc.) <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.
*   **Bill Date:** The date the expense occurred <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.
*   **Due Date:** The expected repayment date for the bill <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>.
*   **Budgeted Expense:** The allocated budget for the expense <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.
*   **Actual Expense:** The actual cost incurred <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.
*   **Status of Payment:** A checkbox that reflects if the amount is paid <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>.

### Bills Frequency Database

This database shows how bills are managed according to their periodicity <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>. It features:
*   **Budgeted Expense:** A rollup from the Bills database, showing the budgeted value <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.
*   **Actual Expense:** A rollup from the Bills database, showing the actual expense value <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.
*   **Change:** Calculated as budgeted expense minus actual expense <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.
*   **Upcoming Bill:** A rollup from the Bills database, showing the earliest due date <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>.
*   **Bills Paid:** A rollup counting the number of bills marked as "checked" for payment <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.
*   **Total Bills:** A rollup from the description column of the Bills database, counting all bills <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.
*   **Bills Paid in Percentage:** Calculated as (Bills Paid / Total Bills) <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.
*   **Formula (Text):** An "if" condition formula that displays the total bills paid in text format <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.

### Bills Category Database and Bills Priority Database

These supplemental databases are used for presenting [[expense_categorization_in_notion | expense categorization in Notion]] and priority distributions <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>.
*   **Bills Category Database:** Divides bills into the six discussed categories <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.
*   **Bills Priority Database:** Holds the three priority levels: low, medium, and high <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>.
Both databases extract the number of bills paid, actual expenses incurred, and the bills paid in percentage using rollup methods from the Bills Details database <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a> <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>.

### Expense Type Database

This database calculates [[using_summary_and_financial_overview_features_in_notion | budgeted expenses]], actual expenses, change in expenses, upcoming bills, bills paid, and bills paid in percentage for each individual type of expense (e.g., daily, weekly, monthly) <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>. These values are pulled using a rollup property from the Bills Details database <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.