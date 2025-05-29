---
title: Databases used in Notion bills tracker
videoId: RqN1qUpTkSI
---

From: [[theaccountantguy]] <br/> 

To create a [[creating_a_bills_tracker_in_notion | bills tracker in Notion]], a primary database and several supplemental databases are required to store information, manage details, and derive desired insights <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.

## Bills Details Database

This is the primary database for the Notion bills tracker <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>. It contains the core information for each bill <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.

Properties within this database include:
*   **Description**: A statement related to the expense <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.
*   **Category**: States one of six expense categories <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>.
*   **Priorities**: Indicates low, medium, or high priority for the expense <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>.
*   **Type of Expense**: Classifies the expense as daily, weekly, monthly, or other types <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.
*   **Bill Date**: The date the expense occurred <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.
*   **Due Date**: The expected repayment date for the bill <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>.
*   **Budgeted Expense**: The allocated budget for the expense <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.
*   **Actual Expense**: The actual cost incurred for the expense <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.
*   **Status of Payment**: A checkbox reflecting whether the amount has been paid <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>.

The Category, Priority, and Expense Type properties are linked to other databases for presentation on the [[primary_dashboard_features_of_notion_bills_tracker | primary dashboard]] <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.

## Bills Frequency Database

This database shows how bills are paid according to different periodicities of expense <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>.

Properties within this database include:
*   **Budgeted Expense**: Rolled up from the Bills Details database to show the budgeted value <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.
*   **Actual Expense**: Rolled up from the Bills Details database to show the actual value <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.
*   **Change**: Calculated as budgeted expense less the actual expense <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.
*   **Upcoming Bill**: Rolled up from the Bills Details database, providing the earliest due date <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>.
*   **Bills Paid**: Rolls up the number of bills marked as paid, derived by specifying a "checked" condition in the roll-up values <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.
*   **Total Bills**: Rolled up from the description column of the Bills Details database, counting all bills <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.
*   **Bills Paid in Percentage**: Calculated as "Bills Paid" divided by "Total Bills" <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>.
*   **Formula for text representation**: Uses an `if` condition to show how many bills have been paid from the total bills in text format <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.

## Bills Category Database

This database divides bills into six categories: entertainment, food and groceries, utility bills, travel and transportation, loans and debts, and others <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>.

It extracts three key pieces of information for each category:
*   Number of bills paid <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.
*   Actual expenses incurred <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>.
*   Bills paid in percentage <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.

## Bills Priority Database

This database organizes bills into three priorities: low, medium, and high <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>.

It provides the following information for each priority:
*   Actual expense <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.
*   Bills paid in percentage <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.

## Database for Individual Expense Types

This database presents budgeted expenses, actual expenses, change in expenses, upcoming bills, bills paid, and bills paid in percentage for each individual type of expense (e.g., daily, weekly, monthly) <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>. The respective values are pulled up using a Rollup property from the Bills Details database <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>. This can be created for all other types of expenses once set up for one type, such as daily expenses <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>.