---
title: Creating a bills database in Notion
videoId: RqN1qUpTkSI
---

From: [[theaccountantguy]] <br/> 

This article explains how to create a comprehensive [[notion_bills_tracker_tutorial | bills tracker in Notion]] to manage and monitor expenses. The tracker is designed with a primary dashboard that offers a summary, bills distribution by priority and category, and a breakdown by payment period <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.

## Overview of the Notion Bills Tracker

The bills tracker features a primary dashboard that organizes financial information into several key sections:

### Summary Section
This section provides an overview of bill statuses, categorized into:
*   **Upcoming Bills:** Displays the amount, due date, days remaining, and payment status <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>. The status updates to "paid" when clicked, moving the bill to the "Bills Paid" section <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.
*   **Past Due Bills:** Shows bills that have passed their due date, including the amount, original due date, days past due, and payment status <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>.
*   **Bills Paid:** Lists all bills paid on time, along with the amount, due date, and bill status <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>.

### Bills Distribution Sections
Bills are further categorized and presented for analytical insights:
*   **By Priority:** Bills are classified as low, medium, or high priority, showing the amount incurred and the percentage of bills paid within each priority level <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a><a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>.
*   **By Category:** Bills are grouped into six categories: Entertainment, Food and Groceries, Utility Bills, Travel and Transportation, Loans and Debts, and Others <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a><a class="yt-timestamp" data-t="00:06:35">[00:06:35]</a>. Each category displays the total amount paid and its percentage of overall bills <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.
*   **By Period:** Bills are distributed based on payment frequency: Daily, Weekly, Monthly, Quarterly, Half-Yearly, Annually, and One-Time <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a><a class="yt-timestamp" data-t="00:06:52">[00:06:52]</a>. For each period, the tracker shows budgeted expenses, actual expenses, the observed change, upcoming bills, bills paid in numbers, and bills paid in percentage <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a><a class="yt-timestamp" data-t="00:06:59">[00:06:59]</a>.

## Building the Bills Tracker in Notion

To [[creating_and_managing_a_database_in_notion | build the Notion bills tracker]], the core component is a primary "Bills Database" complemented by several supplemental databases that store related information and facilitate desired calculations <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.

### 1. Bills Details Database
This is the central [[creating_a_database_in_notion | database in Notion]] for all bill-related information <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>. It includes the following columns:
*   **Description:** A detailed explanation of the expense <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.
*   **Category:** Links to one of the six expense categories <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>.
*   **Priorities:** Designates the expense as low, medium, or high priority <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>.
*   **Type of Expense:** Specifies the payment frequency (e.g., daily, weekly, monthly) <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.
*   **Bill Date:** The date the expense occurred <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.
*   **Due Date:** The expected date for bill repayment <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>.
*   **Budgeted Expense:** The planned budget for the expense <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.
*   **Actual Expense:** The actual amount incurred <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.
*   **Status of Payment:** A checkbox to indicate if the amount has been paid <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.

### 2. Bills Frequency Database
This supplemental [[creating_database_in_notion | database in Notion]] tracks how bills are paid across different periodicities <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>. It uses "roll-up" properties from the Bills Details Database to derive values:
*   **Budgeted Expense:** Rolled up from the Bills Database <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.
*   **Actual Expense:** Rolled up from the Bills Database <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.
*   **Change:** Calculated as Budgeted Expense minus Actual Expense <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.
*   **Upcoming Bill:** Rolled up to show the earliest due date <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>.
*   **Bills Paid:** Rolled up by counting bills where the status checkbox is "checked" <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.
*   **Total Bills:** Rolled up from the description column of the Bills Database to count all bills <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.
*   **Bills Paid in Percentage:** Calculated as (Bills Paid / Total Bills) <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.
*   **Textual Status:** A formula that displays how many bills have been paid out of the total <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.

### 3. Bills Category Database and Bills Priority Database
These databases are designed for presentation in the primary dashboard and extract key information using similar roll-up methods:
*   **Bills Category Database:** Divides bills into the six discussed categories <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>.
*   **Bills Priority Database:** Contains three priorities: Low, Medium, and High <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>.

Both databases extract:
*   Number of bills paid <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.
*   Actual expenses incurred <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>.
*   Bills paid in percentage <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.

### 4. Expense Type Database
This additional database presents a detailed breakdown for each individual type of expense (e.g., daily, weekly). It pulls respective values like budgeted expenses, actual expenses, change, upcoming bills, bills paid, and percentage paid using a "roll-up" property from the Bills Details Database <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>. This process can be repeated for all expense types <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.

The completed [[notion_bills_tracker_tutorial | Notion bills tracker]] template is available for download via a link in the video description <a class="yt-timestamp" data-t="00:07:19">[00:07:19]</a>.