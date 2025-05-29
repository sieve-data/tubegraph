---
title: Using the bills details database in Notion
videoId: RqN1qUpTkSI
---

From: [[theaccountantguy]] <br/> 

To [[creating_a_bills_tracker_in_notion | create a bills tracker in Notion]], the primary database needed is the Bills Details database <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>. This database, along with supplemental databases, stores information related to bills and helps generate desired insights <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>.

## Database Columns

The Bills Details database contains several key columns (properties) to manage bill information <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>:

*   **Description** <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>: States the description related to any expense <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>.
*   **Category** <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>: Assigns the expense to one of six predefined categories <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>:
    *   Entertainment <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>
    *   Food and Groceries <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>
    *   Utility Bills <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>
    *   Travel and Transportation <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>
    *   Loans and Debts <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>
    *   Others <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>
*   **Priorities** <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>: Classifies the expense as low, medium, or high priority <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.
*   **Type of Expense** <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>: Defines the payment frequency, such as daily, weekly, monthly, quarterly, half-yearly, annually, or one-time <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>, <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.
*   **Bill Date** <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>: The date the expense occurred <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
*   **Due Date** <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>: The expected date for bill repayment <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.
*   **Budgeted Expense** <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>: The budgeted amount for the expense <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.
*   **Actual Expense** <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>: The actual amount incurred for the expense <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.
*   **Status of Payment** <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>: A checkbox that reflects if the amount has been paid or not by clicking or unclicking it <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.

## Integration and Usage

The 'Category', 'Priority', and 'Type of Expense' properties within the Bills Details database are linked to other databases for presentation in the primary dashboard of the [[tracking_subscriptions_and_bills_using_notion | Notion bills tracker]] <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.

Information from the Bills Details database is used to power various sections of the tracker:

*   **Summary Section** <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>:
    *   **Upcoming Bills**: Shows bills, their amount, due date, days remaining, and payment status <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>, <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>. Clicking the status updates it to "paid" and moves the bill to the "Bills Paid" section <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.
    *   **Past Due Bills**: Displays bills that have exceeded their due date, including the amount, due date, and days past due <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>.
    *   **Bills Paid**: Lists all bills paid on time with their amount, due date, and status <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.
*   **Bills Distribution by Priority** <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>: Classifies bills as low, medium, or high priority, showing the amount and percentage of bills in each category <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>, <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>.
*   **Bills Distribution by Category** <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>: Organizes bills into the six categories (entertainment, food and groceries, utility bills, travel and transportation, loans and debts, others), displaying the total amount paid and percentage of bills paid for each <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>, <a class="yt-timestamp" data-t="00:06:35">[00:06:35]</a>.
*   **Bills Distribution by Period** <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>: Divides bills by frequency (daily, weekly, monthly, quarterly, half-yearly, annually, one-time), showing budgeted expenses, actual expenses, change, upcoming bills, bills paid (in numbers and percentage) for each period <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>, <a class="yt-timestamp" data-t="00:06:52">[00:06:52]</a>.
*   **Roll-up Properties**: Values from the Bills Details database, such as budgeted expense <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a> and actual expense <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>, are rolled up into other databases like the Bills Frequency database for further calculations and presentations <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>, <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>, <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>. The 'status of payment' checkbox is used to roll up the number of bills paid <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.
*   **Calculations**: The database's 'description' column is used to count all bills for calculations like "Bills Paid in Percentage" (bills paid divided by total bills) <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.