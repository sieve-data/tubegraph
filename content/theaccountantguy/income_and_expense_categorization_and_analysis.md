---
title: Income and expense categorization and analysis
videoId: C9gr5yS8EPc
---

From: [[theaccountantguy]] <br/> 

This article details how to utilize a minimalistic budget planner built in Notion to effectively [[managing_and_tracking_income_and_expenses | manage and track income and expenses]], providing in-depth categorization and analysis features <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>. The planner aims to keep track of financial data in one central location <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>, allow for setting monthly income goals <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>, [[expense_categorization | categorize expenses]] to identify areas for improvement <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>, and monitor monthly budgets across different categories <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.

To use this template, a Notion account is required <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>. The setup involves three main steps: filling out income details <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>, filling out expense details <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>, and allocating available funds (income minus expenses) <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.

## Dashboard Segments

The budget planner's dashboard is organized into three primary segments:

*   **Summary Segment**: Provides an overall view of income, expenses, and allocation of funds <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>, including quarterly fund allocation <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.
*   **Income Details**: Offers specifics on actual versus estimated income, quarterly income overview, and frequency of income <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.
*   **Expense Details**: Presents information on actual versus budgeted expenses, quarterly expense overview, and types of expenses <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>.

## Income Tracking and Analysis

The first step in using the planner is to set up the income details <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>. This is done by creating an inline database in Notion <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>.

### Setting Up Income Details Database

The income details database includes the following columns:

*   **Income Details**: Title property for each individual income earned in a month <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
*   **Source of Income**: A category of each income, using a relation property linked to another database <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>. Examples include "salary," "side hustle," and "other sources of income" <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.
*   **Month of Income**: Specifies the month of income, also a relation property <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.
*   **Frequency of Income**: Indicates how frequently income is earned (e.g., recurring or one-time), another relation property <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.
*   **Expected Income**: A number property (e.g., US dollars) for the anticipated income in a month <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.
*   **Actual Income**: A number property (e.g., US dollars) for the actual income earned at month-end <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>.
*   **Difference**: A formula property calculating the difference between actual and expected income <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>.

### Income Analysis Through Linked Databases

To derive deeper insights, the main income database is linked to other databases using Notion's "relation" and "roll-up" properties <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>.

*   **Actual vs. Estimated Income by Source**:
    *   This section links to an "Income Type" database that aggregates total actual and budgeted income for each source (e.g., salary, side hustle, others) <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>.
    *   Roll-up properties are used to sum the actual and expected income values from the primary income database for each source <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>.
    *   It also calculates the difference and percentage change between actual and estimated income <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>.

*   **Quarterly Income Overview**:
    *   Linked to a "Month of Income" database <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>.
    *   Roll-up properties calculate expected and actual income for each month <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>.
    *   A formula property calculates the proportion of actual income to budgeted income for each month <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>.
    *   Months are then filtered into quarters (Q1: Jan, Feb, Mar; Q2: Apr, May, Jun, etc.) <a class="yt-timestamp" data-t="00:15:46">[00:15:46]</a>.

*   **Frequency of Income Analysis**:
    *   Linked to a "Frequency of Income" database <a class="yt-timestamp" data-t="00:11:37">[00:11:37]</a>.
    *   Roll-up properties determine the total actual and expected income for "recurring" and "one-time" income types <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>.
    *   A formula calculates the proportion of each income frequency type to the total income <a class="yt-timestamp" data-t="00:12:37">[00:12:37]</a>.

## Expense Tracking and Analysis

The second step is to track expenses <a class="yt-timestamp" data-t="00:17:14">[00:17:14]</a>. Similar to income, this involves setting up a dedicated database.

### Setting Up Expense Details Database

The expense details database contains the following columns for [[adding_and_categorizing_expenses | adding and categorizing expenses]]:

*   **Expense Source**: Specifies details on what the expense was incurred <a class="yt-timestamp" data-t="00:17:19">[00:17:19]</a>.
*   **Month of Expense**: The month when the expense was incurred, linked via a relation property to another database <a class="yt-timestamp" data-t="00:17:26">[00:17:26]</a>.
*   **Expense Classification**: Segregated into six different heads, such as "utility and bills," "others," "loans and debts," "food and groceries," "entertainment," and "travel and transportation" <a class="yt-timestamp" data-t="00:17:36">[00:17:36]</a>. This is linked to another database through a relation <a class="yt-timestamp" data-t="00:17:49">[00:17:49]</a>.
*   **Expense Type**: Classified as "variable" or "fixed expense," also linked to a "type of expense" database via relation <a class="yt-timestamp" data-t="00:17:56">[00:17:56]</a>.
*   **Budgeted Expense**: A number property (e.g., US dollars) for the expected expense <a class="yt-timestamp" data-t="00:18:06">[00:18:06]</a>.
*   **Actual Expense**: A number property (e.g., US dollars) for the actual expense incurred <a class="yt-timestamp" data-t="00:18:15">[00:18:15]</a>.
*   **Difference**: Calculates the difference between actual and budgeted expenses, indicating if actual was less (positive difference) or more (negative difference) than budgeted <a class="yt-timestamp" data-t="00:18:23">[00:18:23]</a>.

### Expense Analysis Through Linked Databases

Expense analysis mirrors the income analysis structure, utilizing linked databases, relations, and roll-ups:

*   **Actual vs. Budgeted Expense**:
    *   Linked to an "Expense Variance Analysis" database <a class="yt-timestamp" data-t="00:18:51">[00:18:51]</a>.
    *   Provides total budgeted expense, total actual expense, the difference, and percentage change <a class="yt-timestamp" data-t="00:19:04">[00:19:04]</a>.

*   **Quarterly Expense Overview**:
    *   Displays actual expense incurred and the proportion of actual expense to budgeted expense for each month <a class="yt-timestamp" data-t="00:19:26">[00:19:26]</a>.
    *   Linked to the "Month of Expense" database and organized into quarters, similar to income <a class="yt-timestamp" data-t="00:19:36">[00:19:36]</a>.

*   **Type of Expense Overview**:
    *   Segments expenses into "variable" and "fixed expenses" <a class="yt-timestamp" data-t="00:19:48">[00:19:48]</a>.
    *   Shows total actual expenses for each type and their proportion to the total expense <a class="yt-timestamp" data-t="00:19:51">[00:19:51]</a>.
    *   Linked to a "type of expense" database <a class="yt-timestamp" data-t="00:20:01">[00:20:01]</a>.

## Fund Allocation

The final step involves [[organizing_funds_into_categories_for_financial_management | allocating the available funds]], which is the income minus expenses <a class="yt-timestamp" data-t="00:21:21">[00:21:21]</a>.

### Calculating Available Funds

A formula property calculates the total income less total expenses to determine the available funds for each month <a class="yt-timestamp" data-t="00:21:41">[00:21:41]</a>.

### Allocating Funds

Available funds are allocated to different heads like "investment," "savings," and "others" <a class="yt-timestamp" data-t="00:21:52">[00:21:52]</a>.

*   **Total Allocation**: Summation of investment, savings, and other allocations <a class="yt-timestamp" data-t="00:22:01">[00:22:01]</a>.
*   **Percentage of Allocation**: A formula calculates the total allocation divided by the total available funds, displayed as a percentage and represented by a bar <a class="yt-timestamp" data-t="00:22:26">[00:22:26]</a>.

### Allocation Overviews

*   **Fund Allocation Overview**: Provides an analysis of remaining funds allocated to investment, savings, and others, including the total allocated amount and its proportion to total available funds <a class="yt-timestamp" data-t="00:20:29">[00:20:29]</a>. This is linked to an "allocation of funds" database <a class="yt-timestamp" data-t="00:23:25">[00:23:25]</a>.
*   **Quarterly Allocation Overview**: Offers a monthly allocation overview, showing total available funds for each month and the proportion of funds allocated, broken down by quarter <a class="yt-timestamp" data-t="00:20:59">[00:20:59]</a>. This links to an "available funds" database <a class="yt-timestamp" data-t="00:23:41">[00:23:41]</a>.

This Notion budget planner provides a comprehensive system for [[managing_and_tracking_income_and_expenses | managing and tracking income and expenses]], offering detailed categorization and analytical tools for better financial oversight <a class="yt-timestamp" data-t="00:24:02">[00:24:02]</a>.