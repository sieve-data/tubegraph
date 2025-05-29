---
title: Tracking bill payments and due dates
videoId: RqN1qUpTkSI
---

From: [[theaccountantguy]] <br/> 

A bills tracker can be created in Notion to monitor and manage various payments <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>. This system allows for [[tracking_payment_amounts_and_due_payments | tracking payment amounts and due payments]], due dates, and payment statuses, offering a comprehensive overview of financial obligations.

## Overview of the Bills Tracker Dashboard

The primary dashboard of the Notion bills tracker provides several key sections:

### Summary Section
This section is divided into three subsections, offering a quick glance at the status of bills:
*   **Upcoming Bills** <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>: Displays bills that are approaching their due dates <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>. It shows the amount, due date, number of days left until payment, and the current status <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. The status can be updated to "paid" by clicking a checkbox <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.
*   **Past Due Bills** <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>: Lists bills that have exceeded their due dates <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>. This includes the expense amount, the original due date, and how many days past due it is <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>.
*   **Bills Paid** <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>: Shows all bills that have been paid on time, along with their amount, due date, and status <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.

### Bills Distribution
This section categorizes bills based on different criteria:
*   **By Priority** <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>: Bills are classified as low, medium, or high priority <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. It displays the amount for each priority level and the percentage of bills paid within that priority <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.
*   **By Category** <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>: Bills are grouped into six main categories: entertainment, food and groceries, utility bills, travel and transportation, [[debt_payment_tracking_and_reporting | loans and debts]], and others <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>. For each category, the total amount paid and the percentage of bills paid are shown <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.
*   **By Period** <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>: Bills are segmented by their payment frequency: daily, weekly, monthly, quarterly, half-yearly, annually, and one-time <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>. This view includes budgeted expenses, actual expenses, the observed change, upcoming bills, the number of bills paid, and the percentage of bills paid <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.

## Building the Bills Tracker in Notion

To construct this tracker, one primary "Bills Database" and several supplemental databases are required <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.

### Bills Details Database
This is the core database for tracking bills <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>. Key columns include:
*   **Description**: Details related to the expense <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.
*   **Category**: One of the six expense categories <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>.
*   **Priorities**: Low, medium, or high priority <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>.
*   **Type of Expense**: Such as daily, weekly, or monthly <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.
*   **Bill Date**: The date the expense occurred <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.
*   **Due Date**: The expected repayment date for the bill <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>.
*   **Budgeted Expense**: The allocated budget for the expense <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.
*   **Actual Expense**: The actual cost incurred <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.
*   **Status of Payment**: A checkbox indicating if the amount has been paid <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>.

Category, Priority, and Expense Type columns are linked to other databases for presentation <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.

### Bills Frequency Database
This database shows how bills are paid according to different periodicities <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>. It leverages "roll-up" properties from the Bills database:
*   **Budgeted Expense**: Rolled up from the Bills database to show budgeted values <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.
*   **Actual Expense**: Rolled up from the Bills database to show actual expense values <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>.
*   **Change**: Calculated as budgeted expense minus actual expense <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.
*   **Upcoming Bill**: Rolled up from the Bills database to show the earliest due date <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>.
*   **Bills Paid**: Rolls up the count of bills marked as "checked" (paid) <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.
*   **Total Bills**: Rolls up the count of all bills from the description column <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.
*   **Bills Paid in Percentage**: Calculated as bills paid divided by total bills <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.
*   A formula uses an "if" condition to display how many bills have been paid from the total <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.

### Bills Category Database & Bills Priority Database
These supplemental databases organize bills by the six categories and three priority levels <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>. They extract the number of bills paid, actual expenses incurred, and the percentage of bills paid using similar roll-up methods <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>.

### Individual Type of Expenses Database
This database holds budgeted expenses, actual expenses, change, upcoming bills, bills paid in numbers, and bills paid in percentage for each individual type of expense <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>. Values are pulled using a roll-up property from the Bills Details database <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>. This process is repeated for all expense types <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.

This Notion bills tracker template is designed to provide comprehensive [[tracking_invoice_payments_in_Notion | tracking of invoice payments]] and ensure timely management of all financial obligations.