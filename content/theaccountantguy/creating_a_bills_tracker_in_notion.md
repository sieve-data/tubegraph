---
title: Creating a bills tracker in Notion
videoId: RqN1qUpTkSI
---

From: [[theaccountantguy]] <br/> 

This article details how to create a [[creating_a_bills_tracker_in_notion | bills tracker in Notion]], designed to manage and track expenses effectively <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.

## Overview of the Notion Bills Tracker

The Notion bills tracker provides a comprehensive overview of financial commitments, organized into several key sections:

*   **[[summary_section_of_notion_bills_tracker | Summary Section]]** <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>: This section is divided into three subsections:
    *   **Upcoming Bills**: Displays all pending bills with details such as amount due, due date, days remaining until payment, and payment status <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. Clicking on a bill's status updates it to "paid" and moves it to the "Bills Paid" section <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.
    *   **Past Due Bills**: Shows bills that have exceeded their due date <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>.
    *   **Bills Paid**: Lists all bills that have been paid on time <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.

*   **Bills Distribution by Priority**: Bills are categorized by priority (low, medium, or high), showing the amount and percentage for each category <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.

*   **Bills Distribution by Category**: Expenses are classified into six categories: entertainment, food and groceries, utility bills, travel and transportation, loans and debts, and others <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>. Each category displays the total amount paid and the percentage of bills paid within that category <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.

*   **Bills Distribution by Period**: Bills are also distributed by payment frequency: daily, weekly, monthly, quarterly, half-yearly, annually, and one-time <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. For each period, the tracker shows budgeted expenses, actual expenses, the observed change, upcoming bills, bills paid (in numbers), and bills paid as a percentage <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.

## Building the Bills Tracker: Required Databases

To construct the Notion bills tracker, one primary database and several supplemental [[databases_used_in_notion_bills_tracker | databases]] are needed to store and retrieve bill-related information <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.

### Bills Details Database

This is the primary database for recording all bill information <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>. It includes the following columns:

*   **Description**: A brief description of the expense <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.
*   **Category**: Assigns the expense to one of six predefined categories <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>.
*   **Priorities**: Designates the expense as low, medium, or high priority <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>.
*   **Type of Expense**: Specifies the expense frequency, such as daily, weekly, or monthly <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.
*   **Bill Date**: The date when the expense occurred <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.
*   **Due Date**: The expected date for bill repayment <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>.
*   **Budgeted Expense**: The allocated budget for the expense <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.
*   **Actual Expense**: The actual amount incurred for the expense <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.
*   **Status of Payment**: A checkbox to indicate if the bill has been paid <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.

The Category, Priority, and Expense Type columns are linked to other [[databases_used_in_notion_bills_tracker | databases]] for presentation on the [[primary_dashboard_features_of_notion_bills_tracker | primary dashboard]] <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.

### Bills Frequency Database

This database tracks bills based on their periodicity <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>. It uses "roll-up" properties from the Bills Details database to gather information:

*   **Budgeted Expense**: Rolled up from the Bills database to show budgeted values <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.
*   **Actual Expense**: Rolled up from the Bills database to show actual expense values <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.
*   **Change**: Calculated as `Budgeted Expense` minus `Actual Expense` <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.
*   **Upcoming Bill**: Rolled up from the Bills database, showing the earliest due date <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>.
*   **Bills Paid**: Rolls up the count of bills marked as "checked" (paid) in the Bills database <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.
*   **Total Bills**: Rolls up the count of all bills from the description column of the Bills database <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.
*   **Bills Paid in Percentage**: Calculated as `Bills Paid` divided by `Total Bills` <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>.
*   **Formula (Text)**: Uses an "if" condition to display how many bills have been paid out of the total in text format <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.

### Bills Category Database

This database organizes bills into the six discussed categories <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>. It extracts information such as the number of bills paid, actual expenses incurred, and the percentage of bills paid, using similar roll-up methods <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>.

### Bills Priority Database

This database categorizes bills by low, medium, and high priority <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>. It similarly tracks actual expenses and the percentage of bills paid using established roll-up techniques <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>.

### Expense Type Database

This database provides a detailed breakdown of budgeted expenses, actual expenses, the change, upcoming bills, bills paid, and bills paid in percentage for each individual type of expense (e.g., daily, weekly) <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>. Values are pulled using roll-up properties from the Bills Details database <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.

## Primary Dashboard Features of the Notion Bills Tracker

The [[primary_dashboard_features_of_notion_bills_tracker | primary dashboard]] serves as the central hub for the [[creating_a_bills_tracker_in_notion | Notion bills tracker]] <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>.

*   **[[summary_section_of_notion_bills_tracker | Summary Section]]**:
    *   **Upcoming Bills**: Shows amount, due date, days left, and payment status <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>.
    *   **Past Due Bills**: Displays bills that are overdue, including amount, due date, days past due, and payment status <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>.
    *   **Bills Paid**: Lists all paid bills with amount, due date, and status <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>.

*   **Bills Distribution (Priority)**: Categorizes bills by low, medium, and high priority, showing expenses incurred and the percentage of bills paid for each <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>.

*   **Bills Distribution (Category)**: Presents bills divided into entertainment, food and groceries, utility bills, travel and transportation, loans and debts, and others <a class="yt-timestamp" data-t="00:06:35">[00:06:35]</a>. Each category includes the total expense incurred and payment percentage <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>.

*   **Bills Distribution (Period)**: Shows bills based on periodicity (daily, weekly, monthly, quarterly, half-yearly, annually, one-time expense) <a class="yt-timestamp" data-t="00:06:52">[00:06:52]</a>. For each, it reflects budgeted expenses, actual expenses, change, upcoming bills, bills paid (in numbers), and the percentage of bills paid <a class="yt-timestamp" data-t="00:06:59">[00:06:59]</a>.