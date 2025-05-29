---
title: Notion Bills Tracker Dashboard Overview
videoId: RqN1qUpTkSI
---

From: [[theaccountantguy]] <br/> 

The Notion Bills Tracker is designed to help users manage their expenses by tracking upcoming, past due, and paid bills, as well as providing various distribution insights <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.

## Primary Dashboard Sections

The primary dashboard of the [[creating_a_bills_tracker_in_notion | Notion bills tracker]] is organized into several key sections <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>.

### Summary Section

This section provides a quick overview of bill statuses <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.
It includes all bills and related details such as the amount, due date, days left to pay, and payment status <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. Clicking on a bill updates its status to "paid" <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.

The summary section is divided into three subsections <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>:

*   **Upcoming Bills**
    Shows expenses due, the due date of the bill, the number of days left, and the payment status <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>.
*   **Past Due Bills**
    Displays bills that have passed their due date, indicating the expense amount, the original due date, the number of days past due, and the payment status <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>.
*   **Bills Paid**
    Lists all bills that have been paid on time, showing the amount, due date, and status of the bill <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a>.

### Bills Distribution by Priority

Bills are classified by priority: low, medium, or high <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. This section shows the amount within each priority level and the percentage of bills accounted for so far <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>. It also displays the expenses incurred and the percentage of bills paid for each priority <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>.

### Bills Distribution by Category

This section categorizes bills under six heads <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>:
*   Entertainment <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>
*   Food and groceries <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>
*   Utility bills <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>
*   Travel and transportation <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>
*   Loans and debts <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>
*   Others <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>

Each category shows the total amount paid and the percentage of bills paid within that category <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.

### Bills Distribution by Period

Bills are divided into periods such as daily, weekly, monthly, quarterly, half-yearly, annually, and one-time expenses <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. For each period, the dashboard displays <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>:
*   Budgeted expenses <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>
*   Actual expenses <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>
*   The observed change (difference between budgeted and actual) <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>
*   Upcoming bills to be paid <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>
*   Bills paid (in numbers) <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>
*   Bills paid in percentage <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>

## Underlying Database Structure

To build the [[creating_a_bills_tracker_in_notion | Notion bills tracker]], one primary database, the Bills database, and some supplemental databases are needed to store and retrieve information <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.

*   **Bills Details Database**: Contains columns for description, category (one of six expense categories), priority (low, medium, high), type of expense (daily, weekly, monthly, etc.), bill date, due date, budgeted expense, actual expense, and a checkbox for payment status <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.
*   **Bills Frequency Database**: Shows how bills are paid across different periodicities of expense <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>. This database rolls up budgeted expense, actual expense, calculates the change, identifies upcoming bills, and counts bills paid and total bills to determine the percentage paid <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.
*   **Bills Category Database**: Divides bills according to the six categories discussed <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>, extracting the number of bills paid, actual expenses incurred, and the percentage of bills paid <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.
*   **Bills Priority Database**: Contains the three priorities of bills (low, medium, high) <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a> and similarly extracts actual expense and bills paid in percentage <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.

The values displayed in the dashboard sections are pulled from these databases using roll-up properties <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>.