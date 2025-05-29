---
title: Notion bills tracker tutorial
videoId: RqN1qUpTkSI
---

From: [[theaccountantguy]] <br/> 

This article outlines how to create a bills tracker within [[notion_app | Notion]], detailing its structure, databases, and functionalities. The tracker aims to provide a comprehensive overview of bill payments, budgeting, and financial tracking <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.

## Tracker Overview

The [[creating_a_bills_database_in_notion | Notion bills tracker]] is designed with several key sections to manage expenses effectively:

*   **Summary Section** <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>
    *   **Upcoming Bills**: Displays bills with their amount, due date, days remaining to pay, and payment status <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.
    *   **Past Due Bills**: Shows bills that have passed their due date, including the amount, original due date, and days past due <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>.
    *   **Bills Paid**: Lists all bills that have been paid, along with the amount and due date <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>.
    *   Clicking a bill's status updates it to "paid" and moves it to the "Bills Paid" section <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.

*   **Bills Distribution by Priority** <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>
    *   Bills are classified into low, medium, or high priority <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.
    *   This section shows the amount and percentage of bills for each priority level <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.

*   **Bills Distribution by Category** <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>
    *   Bills are categorized into six types: entertainment, food and groceries, utility bills, travel and transportation, loans and debts, and others <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.
    *   For each category, the total amount paid and the percentage of bills paid are displayed <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>.

*   **Bills Distribution by Period** <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>
    *   Bills are divided by frequency: daily, weekly, monthly, quarterly, half-yearly, annually, and one-time <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.
    *   Each period shows budgeted expenses, actual expenses, the observed change, upcoming bills, bills paid in numbers, and bills paid as a percentage <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.

## Building the Bills Tracker

To build the [[creating_a_bills_database_in_notion | Notion bills tracker]], one primary database and several supplemental databases are required <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.

### Bills Details Database

This is the core database containing individual bill information <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>. Columns include:

*   **Description**: Details related to an expense <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>.
*   **Category**: One of the six expense categories <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.
*   **Priorities**: Low, medium, or high priority for the expense <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.
*   **Type of Expense**: Daily, weekly, monthly, etc. <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.
*   **Bill Date**: Date of expense occurrence <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.
*   **Due Date**: Expected repayment date <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.
*   **Budgeted Expense**: The allocated budget for the expense <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>.
*   **Actual Expense**: The actual cost incurred <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.
*   **Status of Payment**: A checkbox to indicate if the amount is paid <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.

Category, Priority, and Expense Type columns are linked to other databases for dashboard presentation <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.

### Bills Frequency Database

This database organizes bills based on their payment periodicity <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>. Key properties, often using roll-ups from the Bills Details database, include:

*   **Budgeted Expense**: Rolled up from the Bills database <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>.
*   **Actual Expense**: Also rolled up from the Bills database <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>.
*   **Change**: Calculated as `Budgeted Expense - Actual Expense` <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.
*   **Upcoming Bill**: Rolled up to show the earliest due date <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>.
*   **Bills Paid**: Rolls up the count of bills with a "checked" status <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.
*   **Total Bills**: Rolled up from the description column to count all bills <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>.
*   **Bills Paid in Percentage**: Calculated as `Bills Paid / Total Bills` <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.
*   A formula with an `if` condition calculates the number of bills paid from total bills in text format <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.

### Bills Category Database & Bills Priority Database

These databases divide bills by the six categories and three priorities, respectively <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>. They extract information such as:

*   Number of bills paid <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>.
*   Actual expenses incurred <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.
*   Bills paid in percentage <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>.
*   The same roll-up methods used in the Bills Frequency database are utilized here <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.

### Individual Expense Type Database

This database presents budgeted expenses, actual expenses, change in expenses, upcoming bills, bills paid, and bills paid in percentage for each individual expense type (e.g., daily, weekly) <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>. Values are pulled using a Rollup property from the Bills Details database <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>.

## Primary Dashboard

The primary dashboard integrates all the data from the databases into a centralized view, displaying:

*   **Summary Section**: Upcoming bills, past due bills, and bills paid <a class="yt-timestamp" data-t="00:05:59">[00:05:59]</a>.
*   **Bills Distribution by Priority**: Low, medium, and high priority bills with expenses incurred and percentage paid <a class="yt-timestamp" data-t="00:06:35">[00:06:35]</a>.
*   **Bills Distribution by Category**: Breakdown by the six categories, showing total expense incurred and payment percentage <a class="yt-timestamp" data-t="00:06:52">[00:06:52]</a>.
*   **Bills Distribution by Period**: Daily, weekly, monthly, quarterly, half-yearly, annually, and one-time expenses, reflecting budgeted expenses, actual expenses, change, upcoming bills, bills paid (numbers), and bills paid (percentage) <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>.

This [[creating_a_bills_database_in_notion | Notion bills tracker]] template is available for download <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>.