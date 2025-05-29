---
title: Managing bill payments and priorities with Notion
videoId: RqN1qUpTkSI
---

From: [[theaccountantguy]] <br/> 

The Accountant Guy presents a method to create a comprehensive [[creating_a_bills_database_in_notion | bills tracker]] in Notion, designed to help users [[tracking_personal_finances_in_notion | track personal finances]] and manage bill payments effectively <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. This tracker, which can be part of a broader [[using_notion_for_personal_finance_management | personal finance management system]], allows for categorization, prioritization, and detailed oversight of expenses <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.

## Notion Bills Tracker Dashboard Overview

The primary dashboard for the Notion Bills Tracker is organized into several key sections <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>:

### Summary Section
This section provides an at-a-glance view of bill statuses <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.
*   **Upcoming Bills:** Displays bills with their amount, due date, remaining days until payment, and payment status <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>. Clicking on a bill updates its status to "paid," moving it to the "Bills Paid" section <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.
*   **Past Due Bills:** Lists bills that have exceeded their due date, showing the amount, original due date, and how many days past due they are <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>.
*   **Bills Paid:** Shows all bills that have been paid on time, including the amount and payment status <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.

### Bills Distribution by Priority
This section categorizes bills by their priority: low, medium, or high <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. It shows the amount in each priority level and the percentage of bills within that category <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.

### Bills Distribution by Category
Bills are classified into six distinct categories:
*   Entertainment <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>
*   Food and Groceries <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>
*   Utility Bills <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>
*   Travel and Transportation <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>
*   Loans and Debts <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>
*   Others <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>

Each category displays the total amount paid and the percentage of bills paid within it <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.

### Bills Distribution by Period
This section divides bills by their frequency of occurrence: daily, weekly, monthly, quarterly, half-yearly, annually, and one-time <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>. For each period, it displays budgeted expenses, actual expenses, the observed change, upcoming bills, bills paid in numbers, and the percentage of bills paid <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>. This allows for detailed [[creating_and_managing_budgets_in_notion | budget management with Notion]] related to bills.

## Building the Notion Bills Tracker

To build the Notion bills tracker, one primary database and several supplemental databases are required <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.

### 1. Bills Details Database
This is the core database for all bill-related information <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.
*   **Description:** A text field for details related to the expense <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.
*   **Category:** A relation to the "Bills Category" database, classifying the expense into one of six predefined categories <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>.
*   **Priorities:** A relation to the "Bills Priority" database, assigning a low, medium, or high priority to the expense <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>.
*   **Type of Expense:** A relation to another database (e.g., "Bills Frequency" or "Expense Type"), indicating if it's daily, weekly, monthly, etc. <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.
*   **Bill Date:** The date the expense occurred <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.
*   **Due Date:** The expected repayment date for the bill <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>.
*   **Budgeted Expense:** The planned budget for the expense <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.
*   **Actual Expense:** The actual amount incurred for the expense <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.
*   **Status of Payment:** A checkbox property indicating if the amount is paid or not <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.

### 2. Bills Frequency Database
This database shows how bills are paid across different periodicities <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>.
*   **Budgeted Expense:** A roll-up property from the Bills Details database, deriving the total budgeted expense value for each frequency <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.
*   **Actual Expense:** A roll-up property from the Bills Details database, deriving the total actual expense value for each frequency <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.
*   **Change:** A formula property calculating the budgeted expense minus the actual expense <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.
*   **Upcoming Bill:** A roll-up property from the Bills Details database, showing the earliest due date <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>.
*   **Bills Paid:** A roll-up property from the Bills Details database, counting the number of bills with the "Status of Payment" checkbox checked <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.
*   **Total Bills:** A roll-up property from the "Description" column of the Bills Details database, counting all bills <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.
*   **Bills Paid in Percentage:** A formula property (Bills Paid / Total Bills) to calculate the percentage <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.
*   **Bills Paid Text:** A formula property with an `if` condition, showing how many bills have been paid from the total in text format <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.

### 3. Bills Category Database
This database is used to categorize bills into the six predefined categories <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>. It extracts information such as the number of bills paid, actual expenses incurred, and bills paid in percentage using roll-up methods <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>. This database contributes to [[bills_summary_and_categories_in_notion | bills summary and categories in Notion]].

### 4. Bills Priority Database
This database is used to assign low, medium, or high priority to bills <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>. Similar to the Bills Category database, it calculates the actual expense and the bills paid in percentage for each priority level using roll-up methods <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>.

### 5. Additional Database for Expense Types
An additional database can be created to track budgeted expenses, actual expenses, changes, upcoming bills, bills paid, and bills paid in percentage for each individual type of expense (e.g., daily, weekly, monthly) <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>. Values are pulled using a roll-up property from the Bills Details database <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>. This contributes to effective [[using_notion_for_expense_management | expense management with Notion]].

This structured approach to creating and managing databases in Notion enables comprehensive [[tracking_invoice_payments_in_notion | tracking of invoice payments]] and effective management of all bill-related financial activities, including [[adding_and_managing_invoices_in_notion | adding and managing invoices]].