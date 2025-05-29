---
title: Creating a Bills Tracker in Notion
videoId: RqN1qUpTkSI
---

From: [[theaccountantguy]] <br/> 

This article explains how to [[tracking_subscriptions_and_bill_payments_using_notion | create a bills tracker in Notion]] <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>. It provides a detailed overview of the primary dashboard, the databases required, and how various financial metrics are calculated and displayed <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.

## Notion Bills Tracker Dashboard Overview

The primary dashboard for the [[notion_bills_tracker_dashboard_overview | Notion bills tracker]] is organized into several key sections:

### Summary Section
The [[bills_summary_section_in_notion_template | summary section]] contains three subsections:
*   **Upcoming Bills**: This section displays all bills with their details, including the amount due, due date, number of days remaining until payment, and payment status <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a> <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>. Clicking on a bill's status updates it to "bill paid" <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.
*   **Past Due Bills**: This area shows bills that have passed their due date, including the amount, original due date, number of days past due, and payment status <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>.
*   **Bills Paid**: This section lists all bills that have been paid on time, along with the amount, due date, and status <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a> <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>.

### Bills Distribution by Priority
Bills are categorized by priority (low, medium, or high), showing the amount associated with each priority level and the percentage of bills paid within each respective head <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a> <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>.

### Bills Distribution by Category
Bills are also distributed across six predefined categories:
*   Entertainment <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>
*   Food and groceries <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>
*   Utility bills <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>
*   Travel and transportation <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>
*   Loans and debts <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>
*   Others <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>

Each category displays the total amount paid and the percentage of bills paid within it <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a> <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>.

### Bills Distribution by Period
Bills are further categorized by frequency, including daily, weekly, monthly, quarterly, half-yearly, annually, and one-time payments <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a> <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>. For each period, the dashboard shows:
*   Budgeted expenses <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>
*   Actual expenses <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>
*   The observed change <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>
*   Upcoming bills to be paid <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>
*   Bills paid (numerical count) <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>
*   Bills paid (as a percentage) <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>

## Building the Bills Tracker in Notion

To build this [[setting_up_a_finance_tracker_in_notion | finance tracker]] for [[using_notion_for_financial_tracking | financial tracking]] in Notion, one primary database and several supplemental databases are needed <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a> <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>.

### 1. Bills Details Database
This is the primary database that stores all bill-related information <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>. It includes the following columns:
*   **Description**: Details related to any expense <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.
*   **Category**: States one of the six expense categories <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>.
*   **Priorities**: Specifies low, medium, or high priority for the expense <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>.
*   **Type of Expense**: Defines the frequency (e.g., daily, weekly, monthly) <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.
*   **Bill Date**: The date the expense occurred <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.
*   **Due Date**: The expected repayment date for the bill <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>.
*   **Budgeted Expense**: The allocated budget for the expense <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.
*   **Actual Expense**: The actual cost incurred <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.
*   **Status of Payment**: A checkbox that reflects if the amount is paid or not <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>.

> [!INFO] Relationships
> The 'Category', 'Priority', and 'Expense Type' columns are related to other databases for presentation in the primary dashboard <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.

### 2. Bills Frequency Database
This database shows how bills are paid based on different periodicities <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>. Key properties include:
*   **Budgeted Expense**: Rolled up from the Bills database <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.
*   **Actual Expense**: Also rolled up from the Bills database <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.
*   **Change**: Calculated as "budgeted expense less the actual expense" <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.
*   **Upcoming Bill**: Rolled up from the Bills database to show the earliest due date <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>.
*   **Bills Paid**: Rolls up the count of bills that have been paid, derived by specifying a "checked" condition in the roll-up values <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.
*   **Total Bills**: Rolled up from the 'description' column of the Bills database, counting all bills <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.
*   **Bills Paid in Percentage**: Calculated as "bills paid divided by the total bills" <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>.
*   **Textual Summary**: A formula uses an "if" condition to calculate and display how many bills have been paid from the total bills in text format <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.

### 3. Bills Category Database
This database divides bills into the six categories discussed earlier <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>. It extracts three pieces of information for each category using the roll-up method:
*   Number of bills paid <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>
*   Actual expenses incurred <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>
*   Bills paid in percentage <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>

### 4. Bills Priority Database
This database includes the three priorities of bills: low, medium, and high <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>. Similar to the category database, it finds the actual expense and the bills paid in percentage using established methods <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>.

### 5. Individual Expense Type Database
This database tracks budgeted expenses, actual expenses, change in expenses, upcoming bills, bills paid, and bills paid in percentage for each individual type of expense (daily, weekly, monthly, etc.) <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>. Respective values are pulled using a roll-up property from the Bills Details database <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>. These calculations can be repeated for all expense types <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.

This [[how_to_set_up_and_use_a_personal_finance_tracker_in_notion | personal finance tracker]] template is available for download as a link in the description <a class="yt-timestamp" data-t="00:07:19">[00:07:19]</a>.