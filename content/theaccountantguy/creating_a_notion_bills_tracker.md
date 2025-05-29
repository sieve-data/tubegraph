---
title: Creating a Notion bills tracker
videoId: RqN1qUpTkSI
---

From: [[theaccountantguy]] <br/> 

This article provides a guide on how to [[setting_up_a_personal_finance_tracker_in_notion | set up a personal finance tracker in Notion]], specifically focusing on [[using_notion_for_bill_tracking | using Notion for bill tracking]] to create a comprehensive bills tracker <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.

## Overview of the Notion Bills Tracker

The Notion bills tracker is designed to help manage and visualize various aspects of bill payments and expenses.

### Summary Section <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>
The [[summary_section_of_notion_bills_tracker | summary section of the Notion bills tracker]] contains three main subsections:
*   **Upcoming Bills** <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>: Displays all bills and their related details, including the amount, due date, days remaining to pay, and payment status <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>. Clicking on a bill updates its status to "paid," which then moves it to the "Bills Paid" section <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.
*   **Past Due Bills** <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>: Shows bills that have passed their due date, including the amount, original due date, days past due, and payment status <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>.
*   **Bills Paid** <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>: Lists all bills that have been paid on time, along with the amount, due date, and bill status <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>.

### Bills Distribution by Priority <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>
Bills are categorized by priority: low, medium, or high <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>. This section displays the amount associated with each priority level and the percentage of bills accounted for so far <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.

### Bills Distribution by Category <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>
Bills are classified into six categories:
*   Entertainment <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>
*   Food and Groceries <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>
*   Utility Bills <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>
*   Travel and Transportation <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>
*   Loans and Debts (useful for tracking alongside a [[creating_a_notion_debt_tracker | Notion Debt Tracker]] or [[using_notion_for_debt_tracking | using Notion for debt tracking]]) <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>
*   Others <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>

Each category shows the total amount paid and the percentage of bills paid within that category <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>.

### Bills Distribution by Period <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>
Bills are also divided by payment frequency: daily, weekly, monthly, quarterly, half-yearly, annually, and one-time <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>. Each period displays:
*   Budgeted expenses <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>
*   Actual expenses <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>
*   The observed change <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>
*   Upcoming bill to be paid <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>
*   Bills paid (count) <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>
*   Bills paid in percentage <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>

## Database Setup for Notion Bills Tracker <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>
To build the Notion bills tracker, one primary database (Bills database) and several supplemental databases are required <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.

### Bills Details Database <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>
This is the core database that stores all bill-related information. It includes the following columns:
*   **Description**: States the description related to any expense <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>.
*   **Category**: Specifies one of the six expense categories <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.
*   **Priorities**: Defines the expense priority as low, medium, or high <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.
*   **Type of Expense**: Classifies the expense as daily, weekly, monthly, or any other defined type <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.
*   **Bill Date**: The date of occurrence of the expense <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.
*   **Due Date**: The expected repayment date of the bill <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.
*   **Budgeted Expense**: States the allocated budget for the expense <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>.
*   **Actual Expense**: Records the actual expense incurred <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.
*   **Status of Payment**: A checkbox reflecting whether the amount is paid or not <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.

The Category, Priority, and Expense Type columns are linked to other databases for presentation in the [[primary_dashboard_of_notion_bills_tracker | primary dashboard of the Notion bills tracker]] <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.

### Bills Frequency Database <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>
This database shows how bills are paid according to different periodicities. It includes:
*   **Budgeted Expense**: Rolled up from the Bills database <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>.
*   **Actual Expense**: Also rolled up from the Bills database <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>.
*   **Change**: Calculated as Budgeted Expense minus Actual Expense <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.
*   **Upcoming Bill**: Rolled up from the Bills database, showing the earliest due date <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>.
*   **Bills Paid**: Rolls up the count of paid bills by specifying a "checked" condition in the roll-up values <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.
*   **Total Bills**: Rolled up from the "Description" column of the Bills database, counting all bills <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>. This helps calculate "Bills Paid in Percentage" <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.
*   **Bills Paid (Text Formula)**: Uses an `if` condition to show the number of bills paid out of total bills in text format <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>.

### Bills Category Database and Bills Priority Database <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>
These two databases divide bills by the six categories and three priorities (low, medium, high), respectively <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>. From these, three pieces of information are extracted using the previously discussed roll-up methods:
*   Number of bills paid <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>
*   Actual expenses incurred <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>
*   Bills paid in percentage <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>

### Individual Expense Type Database <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>
Another database is created to show:
*   Budgeted expenses <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>
*   Actual expenses <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>
*   Change in expenses <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>
*   Upcoming bill <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>
*   Bills paid <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>
*   Bills paid in percentage <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>

These values are pulled using a roll-up property from the Bills Details database for each individual type of expense (e.g., daily, weekly) <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>.

## Primary Dashboard of Notion Bills Tracker <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>
The [[primary_dashboard_of_notion_bills_tracker | primary dashboard of the Notion bills tracker]] integrates all the data from the databases into a centralized view:
*   **Summary Section**: Displays upcoming bills, past due bills, and bills paid with relevant details like amount, due date, days remaining/past due, and payment status <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>.
*   **Bills Distribution (Priority)**: Shows low, medium, and high priority bills with incurred expenses and the percentage of bills paid <a class="yt-timestamp" data-t="00:06:35">[00:06:35]</a>.
*   **Bills Distribution (Category)**: Presents bills divided by entertainment, food & groceries, utility bills, travel & transportation, loans & debts, and others, indicating total expenses incurred and payment percentage for each <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>.
*   **Bills Distribution (Period)**: Organizes bills based on daily, weekly, monthly, quarterly, half-yearly, annually, and one-time expenses. It reflects budgeted expenses, actual expenses, the change between them, upcoming bills, bills paid in numbers, and the percentage of bills paid <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>.

This template for [[setting_up_a_personal_finance_tracker_using_notion | setting up a personal finance tracker using Notion]] is often available for download <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>.