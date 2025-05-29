---
title: Creating a bills tracker in Notion
videoId: RqN1qUpTkSI
---

From: [[theaccountantguy]] <br/> 

This article outlines how to create a bills tracker within Notion, which helps in organizing and monitoring various expenses and payments <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. The tracker provides a comprehensive overview of your financial obligations, including upcoming bills, past due amounts, and paid bills <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.

## Overview of the Notion Bills Tracker

The Notion bills tracker is designed to provide detailed insights into your expenses through several key sections:

*   **Summary Section** <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>
    *   **Upcoming Bills:** Displays bills with their amount, due date, days left until payment, and payment status <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.
    *   **Past Due Bills:** Shows bills that have exceeded their due date, including the amount, original due date, and days past due <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>.
    *   **Bills Paid:** Lists all bills that have been successfully paid, along with their amount and due date <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>. The status of a bill can be updated to "paid" by simply clicking a checkbox <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.
*   **Bills Distribution by Priority** <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>
    *   Bills are categorized by priority: low, medium, or high <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.
    *   This section shows the amount within each priority level and the percentage of bills paid for each <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.
*   **Bills Distribution by Category** <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>
    *   Bills are classified into six categories: entertainment, food and groceries, utility bills, travel and transportation, loans and debts, and others <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>.
    *   Each category displays the total amount paid and the percentage of bills paid within that category <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.
*   **Bills Distribution by Period** <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>
    *   Bills are organized by payment frequency: daily, weekly, monthly, quarterly, half-yearly, annually, and one-time <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>.
    *   For each period, it shows budgeted expenses, actual expenses, the change observed (budgeted minus actual), upcoming bills, the number of bills paid, and the percentage of bills paid <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.

## Building the Bills Tracker in Notion

To [[creating_a_notion_expense_tracker | create this bills tracker]], you primarily need one main database, the "Bills Database," along with several supplemental databases to store and relate information <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.

### Core Databases

#### Bills Details Database

This is the central database where all individual bill details are entered <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>. Key columns include:
*   **Description:** A statement related to the expense <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.
*   **Category:** One of the six expense categories (e.g., Entertainment, Utility Bills) <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>.
*   **Priorities:** Low, medium, or high priority <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>.
*   **Type of Expense:** Such as daily, weekly, or monthly <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.
*   **Bill Date:** The date the expense occurred <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.
*   **Due Date:** The expected date for bill repayment <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>.
*   **Budgeted Expense:** The planned budget for the expense <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.
*   **Actual Expense:** The actual cost incurred <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.
*   **Status of Payment:** A checkbox that reflects if the amount has been paid or not <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>.

Category, priority, and expense type fields are linked to other databases for presentation in the primary dashboard <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.

#### Bills Frequency Database

This database shows how bills are paid across different periodicities <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>. It uses "roll-up" properties from the Bills Details database to derive values <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>:
*   **Budgeted Expense:** Rolled up from the Bills database <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.
*   **Actual Expense:** Rolled up from the Bills database <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.
*   **Change:** Calculated as budgeted expense less actual expense <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.
*   **Upcoming Bill:** Rolled up from the Bills database, showing the earliest due date <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>.
*   **Bills Paid:** Rolls up the number of bills marked as paid (checked condition) <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.
*   **Total Bills:** Rolls up the count of all bills from the description column <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.
*   **Bills Paid in Percentage:** Calculated as (Bills Paid / Total Bills) <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.
*   A formula uses an "if" condition to calculate how many bills have been paid from the total, displayed as text <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.

#### Bills Category Database & Bills Priority Database

These two databases categorize bills by the six predefined categories and three priority levels (low, medium, high) respectively <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>. From these, you can extract:
*   Number of bills paid <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.
*   Actual expenses incurred <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>.
*   Bills paid in percentage <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.
    These are achieved using methods similar to those discussed for the Bills Frequency database <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>.

#### Individual Type of Expenses Database

This database presents budgeted expenses, actual expenses, change in expenses, upcoming bills, bills paid, and bills paid in percentage for each individual type of expense (e.g., daily, weekly) <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>. These values are pulled using a "roll-up" property from the Bills Details database <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>. This process can be replicated for all expense types <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.

## Primary Dashboard

The primary dashboard integrates data from all databases to provide a comprehensive view of your bills <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>. It features:
*   **Summary Section:** As described above, with upcoming, past due, and paid bills <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>.
*   **Bills Distribution by Priority:** Shows expenses incurred and percentage paid for low, medium, and high priority bills <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>.
*   **Bills Distribution by Category:** Displays total expenses incurred and percentage of payment for categories like entertainment, food, utility, travel, loans, and others <a class="yt-timestamp" data-t="00:06:35">[00:06:35]</a>.
*   **Bills Distribution by Period:** Reflects budgeted expenses, actual expenses, change, upcoming bills, bills paid in numbers, and bills paid in percentage for daily, weekly, monthly, quarterly, half-yearly, annually, and one-time expenses <a class="yt-timestamp" data-t="00:06:52">[00:06:52]</a>.

This detailed Notion bills tracker template is often available for download via a link in the video description <a class="yt-timestamp" data-t="00:07:19">[00:07:19]</a>. This method can be generalized for [[tracking_income_and_expenses_using_notion | tracking income and expenses]], [[budgeting_and_tracking_in_notion | budgeting and tracking in Notion]], [[creating_a_notion_expense_tracker | creating a Notion expense tracker]], and other financial management needs.