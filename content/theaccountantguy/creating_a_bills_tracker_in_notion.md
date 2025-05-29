---
title: Creating a bills tracker in Notion
videoId: RqN1qUpTkSI
---

From: [[theaccountantguy]] <br/> 

This article details how to build a comprehensive bills tracker within Notion, providing a structured system for managing and visualizing your financial obligations <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. The tracker includes sections for upcoming bills, past due bills, and bills that have been paid <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>. It also categorizes bills by priority, type, and period, offering a holistic view of expenses <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.

## Overview of the Notion Bills Tracker

The Notion Bills Tracker is designed to display all bills and their relevant details, such as the amount due, due date, days remaining until payment, and payment status <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. When a bill's status is updated to "paid," it automatically reflects in the "Bills Paid" section <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.

### Summary Section
The summary section provides an at-a-glance view of your bills, divided into three key areas <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>:
*   **Upcoming Bills:** Shows bills with their due dates, amount, and the number of days left until payment <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.
*   **Past Due Bills:** Highlights bills that have exceeded their due date, indicating the amount, original due date, and how many days past due <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.
*   **Bills Paid:** Lists all bills that have been successfully paid, along with their amount and due date <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.

### Bills Distribution
The tracker also visualizes bill distribution in several ways:
*   **By Priority:** Bills are classified as low, medium, or high priority, showing the amount and percentage for each <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.
*   **By Category:** Bills are grouped into six categories: entertainment, food and groceries, utility bills, travel and transportation, loans and debts, and others <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>. Each category displays the total amount paid and its percentage of overall bills <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.
*   **By Period:** Bills are categorized by frequency, including daily, weekly, monthly, quarterly, half-yearly, annually, and one-time payments <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. This section shows budgeted expenses, actual expenses, the observed change, upcoming bills, bills paid in numbers, and the percentage of bills paid for each period <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.

## Building the Bills Tracker in Notion

To [[tracking_personal_finances_in_Notion | track personal finances in Notion]] and create this bills tracker, the primary component is the **Bills Database**, complemented by several supplemental databases to manage and display information effectively <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.

### Bills Details Database
The core of the tracker is the [[using_the_bills_details_database_in_notion | Bills Details Database]] <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>. It includes the following properties:
*   **Description:** A detailed account of the expense <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.
*   **Category:** One of the six defined expense categories (e.g., entertainment, utility bills) <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>.
*   **Priorities:** Designates the expense as low, medium, or high priority <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>.
*   **Type of Expense:** Specifies the payment frequency (e.g., daily, weekly, monthly) <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.
*   **Bill Date:** The date the expense occurred <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.
*   **Due Date:** The expected date for bill repayment <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>.
*   **Budgeted Expense:** The planned budget for the expense <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.
*   **Actual Expense:** The actual cost incurred <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.
*   **Status of Payment:** A checkbox that, when clicked, marks the bill as paid <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.

The `Category`, `Priority`, and `Expense Type` properties are linked to other databases for presentation on the primary dashboard <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.

### Supplemental Databases

#### Bills Frequency Database
This database shows how bills are paid based on different periodicities <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>. It includes:
*   **Budgeted Expense:** Rolled up from the Bills database to derive the budgeted value <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.
*   **Actual Expense:** Rolled up from the Bills database to derive the actual expense value <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.
*   **Change:** Calculated as `Budgeted Expense` minus `Actual Expense` <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.
*   **Upcoming Bill:** Rolled up from the Bills database to show the earliest due date <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>.
*   **Bills Paid:** Rolls up the number of bills marked as "checked" in the Bills database <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.
*   **Total Bills:** Rolls up the count of all bills from the description column of the Bills database <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.
*   **Bills Paid in Percentage:** Calculated as `Bills Paid` divided by `Total Bills` <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>.
*   **Text Formula:** A formula with an `if` condition calculates and displays how many bills have been paid out of the total in text format <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.

#### Bills Category Database
This database categorizes bills into the six predefined categories <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>. It extracts information such as the number of bills paid, actual expenses incurred, and the percentage of bills paid for each category <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>.

#### Bills Priority Database
This database classifies bills into low, medium, and high priorities <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>. Similar to the category database, it finds the actual expense and the bills paid in percentage for each priority level <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>.

#### Expense Type Database
Another database pulls together budgeted expenses, actual expenses, changes in expenses, upcoming bills, bills paid, and the percentage of bills paid for each individual expense type (e.g., daily, weekly) <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>. These values are retrieved using a Rollup property from the Bills Details database <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.

## Primary Dashboard of the Notion Bills Tracker
The primary dashboard serves as the central hub for [[tracking_subscriptions_and_bills_using_Notion | tracking subscriptions and bills using Notion]] and [[creating_and_tracking_budgets_and_savings_in_Notion | creating and tracking budgets and savings in Notion]] with the Notion Bills Tracker <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>.

### Summary Section
The dashboard prominently features the summary section, displaying:
*   **Upcoming Bills:** Amount due, due date, days left, and payment status <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>.
*   **Past Due Bills:** Amount of expense, due date, days past due, and payment status <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>.
*   **Bills Paid:** Amount, due date, and status of paid bills <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>.

### Bills Distribution
The dashboard also provides a clear visual breakdown of bills:
*   **By Priority:** Shows low, medium, and high priority bills, including expenses incurred and the percentage paid <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>.
*   **By Category:** Divides bills into entertainment, food and groceries, utility bills, travel and transportation, loans and debts, and others, showing total expenses and payment percentages for each <a class="yt-timestamp" data-t="00:06:35">[00:06:35]</a>.
*   **By Period:** Displays bills by daily, weekly, monthly, quarterly, half-yearly, annually, and one-time expenses, reflecting budgeted expenses, actual expenses, change, upcoming bills, number of bills paid, and the percentage paid <a class="yt-timestamp" data-t="00:06:52">[00:06:52]</a>.

This comprehensive Notion Bills Tracker helps users effectively manage their financial obligations and track their spending habits. A template for this tracker is often available for download in the description of relevant videos <a class="yt-timestamp" data-t="00:07:19">[00:07:19]</a>.