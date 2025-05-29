---
title: Notion Database Structure for Bills Management
videoId: RqN1qUpTkSI
---

From: [[theaccountantguy]] <br/> 

To [[creating_a_bills_tracker_in_notion | create a bills tracker in Notion]], the system primarily utilizes one main database, the "Bills database," along with several supplemental databases that store and organize information related to bills, enabling the retrieval of desired insights <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.

## Core Database: Bills Details Database

The central component of the Notion Bills Tracker is the "Bills Details Database" <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>. This database holds all the specific information for each expense.

It includes the following columns:
*   **Description**
    *   States the description related to any expense <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.
*   **Category**
    *   Assigns one of six defined categories to the expense <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>.
    *   This column is related to other databases for presentation on the primary dashboard <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.
*   **Priorities**
    *   Assigns a priority level: low, medium, or high <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>.
    *   This column is related to other databases for presentation on the primary dashboard <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.
*   **Type of Expense**
    *   Classifies the expense as daily, weekly, monthly, or another relevant type <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.
    *   This column is related to other databases for presentation on the primary dashboard <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.
*   **Bill Date**
    *   Records the date of occurrence of the expense <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.
*   **Due Date**
    *   Specifies the expected repayment date for bills <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>.
*   **Budgeted Expense**
    *   States the budget allocated for the expense <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.
*   **Actual Expense**
    *   Records the actual expense incurred <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.
*   **Status of Payment**
    *   Reflects whether the amount has been paid by clicking or unclicking a checkbox <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>.

## Supplemental Databases

### Bills Frequency Database

This database organizes bills based on their periodicity (e.g., daily, weekly, monthly) <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>. It uses roll-up properties and formulas linked to the "Bills Details Database" <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.

Columns and their derivations:
*   **Budgeted Expense**
    *   Rolled up from the "Bills Details Database" to show the budgeted expense value <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.
*   **Actual Expense**
    *   Rolled up from the "Bills Details Database" to show the actual expense value <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.
*   **Change**
    *   Calculated as `budgeted expense` less `actual expense` <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.
*   **Upcoming Bill**
    *   Rolled up from the "Bills Details Database" to show the earliest due date <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>.
*   **Bills Paid**
    *   Rolls up the number of bills that have been paid by specifying a "checked" condition in the roll-up values from the "Status of Payment" column in the "Bills Details Database" <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.
*   **Total Bills**
    *   Rolls up the total count of bills from the "Description" column of the "Bills Details Database" <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.
*   **Bills Paid in Percentage**
    *   Calculated as `bills paid` divided by `total bills` <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>.
*   **Textual Summary of Bills Paid**
    *   A formula with an `if` condition calculates how many bills have been paid from the total bills in a text format <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.

### Bills Category Database

This database categorizes bills into six types: entertainment, food and groceries, utility bills, travel and transportation, loans and debts, and others <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>.

It extracts the following information:
*   Number of bills paid <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.
*   Actual expenses incurred <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>.
*   Bills paid in percentage <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.
    *   This information is derived using similar roll-up methods as discussed for the "Bills Frequency Database" <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>.

### Bills Priority Database

This database classifies bills by their priority levels: low, medium, and high <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>.

It provides:
*   Actual expense <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.
*   Bills paid in percentage <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.
    *   These are determined using methods similar to those previously discussed for other databases <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>.

### Individual Type of Expenses Database

This database consolidates key financial metrics for each individual type of expense (e.g., daily, weekly, monthly) <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>.

It includes:
*   Budgeted expenses <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>.
*   Actual expenses <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.
*   Change in expenses <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>.
*   Upcoming bills <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>.
*   Bills paid <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>.
*   Bills paid in percentage <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>.

These values are extracted using a "Roll-up" property from the "Bills Details Database" <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>. The values can be calculated for a specific type (e.g., daily expenses) and then replicated for all other expense types <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>.

## Primary Dashboard Overview

The structured data from these databases is presented in the [[notion_bills_tracker_dashboard_overview | primary dashboard of the Notion Bills Tracker]] <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>.

The dashboard includes a [[bills_summary_section_in_notion_template | summary section]] with three subsections <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>:
*   **Upcoming Bills**: Shows amount, due date, days left, and payment status <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>.
*   **Past Due Bills**: Shows bills past their due date, including amount, due date, days past due, and payment status <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>.
*   **Bills Paid**: Displays all bills paid on time, with amount, due date, and status <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>.

Additionally, the dashboard features sections for:
*   **Bills Distribution by Priority**: Displays low, medium, and high priority bills, showing incurred expenses and percentage paid <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>.
*   **Bills Distribution by Category**: Divides bills into categories like entertainment, food and groceries, utility bills, travel and transportation, [[building_databases_for_debt_management_in_notion | loans and debts]], and others, showing total incurred expense and payment percentage for each <a class="yt-timestamp" data-t="00:06:35">[00:06:35]</a>.
*   **Bills Distribution Based on Period**: Shows bills by period (daily, weekly, monthly, quarterly, half-yearly, annually, one-time expense), reflecting budgeted expenses, actual expenses, change, upcoming bills, bills paid in numbers, and bills paid in percentage <a class="yt-timestamp" data-t="00:06:52">[00:06:52]</a>.