---
title: Utilizing Notion databases for financial tracking
videoId: RqN1qUpTkSI
---

From: [[theaccountantguy]] <br/> 
The Accountant Guy demonstrates how to [[setting_up_notion_for_personal_finance_tracking | set up]] a bills tracker in [[Using Databases in Notion for Financial Tracking | Notion]] to manage financial obligations <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>. This system allows users to monitor upcoming, past due, and paid bills, providing a comprehensive overview of financial commitments <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.

## Overview of the Notion Bills Tracker

The bills tracker in Notion is designed with several key sections to provide a clear and organized view of expenses <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>:

*   **Summary Section**: Displays upcoming bills, past due bills, and bills that have been paid <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>. This section includes details such as the amount due, due date, days remaining until payment, and the current payment status <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. The status can be updated to "paid" by clicking a checkbox <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.
*   **Bills Distribution by Priority**: Categorizes bills as low, medium, or high priority, showing the amount and percentage for each <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.
*   **Bills Distribution by Category**: Divides bills into six categories: entertainment, food and groceries, utility bills, travel and transportation, loans and debts, and others <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>. For each category, it shows the total amount paid and the percentage of bills paid <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.
*   **Bills Distribution by Period**: Organizes bills by frequency, such as daily, weekly, monthly, quarterly, half-yearly, annually, and one-time expenses <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>. This section includes budgeted expenses, actual expenses, the observed change, upcoming bills, bills paid (in numbers), and bills paid as a percentage <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.

## [[notion_database_setup | Notion Database Setup]]

To create this bills tracker, one primary database, the Bills database, and several supplemental databases are required <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.

### Bills Details Database

This is the central database for tracking individual bills <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>. Key columns include:
*   **Description**: A detailed note about the expense <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.
*   **Category**: Links to one of the six expense categories <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>.
*   **Priorities**: Designates the expense as low, medium, or high priority <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>.
*   **Type of Expense**: Specifies the frequency, such as daily, weekly, or monthly <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.
*   **Bill Date**: The date the expense occurred <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.
*   **Due Date**: The expected repayment date for bills <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>.
*   **Budgeted Expense**: The allocated budget for the expense <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.
*   **Actual Expense**: The actual cost incurred <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.
*   **Status of Payment**: A checkbox to indicate if the amount has been paid <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>.

### Supplemental Databases

These databases support the primary dashboard by providing aggregated and categorized data <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>:

*   **Bill Frequency Database**: Shows how bills are paid across different periodicities <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>. It includes:
    *   **Budgeted Expense**: A rollup from the Bills database for budgeted values <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.
    *   **Actual Expense**: A rollup from the Bills database for actual values <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.
    *   **Change**: Calculated as budgeted expense minus actual expense <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.
    *   **Upcoming Bill**: A rollup of the earliest due date from the Bills database <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>.
    *   **Bills Paid**: A rollup counting bills marked as "checked" <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.
    *   **Total Bills**: A rollup counting all bills from the description column <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.
    *   **Bills Paid in Percentage**: Calculated as (Bills Paid / Total Bills) <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.
    *   A formula displays the number of bills paid out of total bills in text format <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.

*   **Bills Category Database**: Divides bills into the six predefined categories <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>. It extracts information on the number of bills paid, actual expenses incurred, and the percentage of bills paid <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.

*   **Bills Priority Database**: Manages bills by their low, medium, or high priority <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>. It tracks the actual expense and bills paid in percentage for each priority level <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.

*   **Individual Expense Type Database**: This database displays budgeted expenses, actual expenses, changes, upcoming bills, bills paid (numbers), and bills paid (percentage) for each individual type of expense (e.g., daily, weekly, monthly) <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>. Values are pulled using a rollup property from the Bills Details database <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>.

This [[Utilizing Notion for financial summaries and budgeting | Notion setup]] provides a comprehensive tool for [[using_notion_for_budgeting | budgeting]] and [[using_databases_in_notion_for_financial_tracking | tracking expenses]], helping users stay on top of their financial obligations <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.