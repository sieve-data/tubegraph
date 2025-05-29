---
title: Tracking income and expenses with a Notion dashboard
videoId: C9gr5yS8EPc
---

From: [[theaccountantguy]] <br/> 

This article details how to [[tracking_personal_finances_in_notion | track personal finances]] by creating a minimalistic budget planner using Notion. This dashboard allows users to centralize their financial data, set income goals, categorize expenses, and monitor monthly budgets from any device <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>, <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>, <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>, <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>, <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>, <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>, <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. To use this template, a Notion account is required <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>.

## Dashboard Segments

The Notion budget planner dashboard consists of three main segments <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>:

1.  **Summary Segment**: Provides an overall view of income, expenses, and allocation of funds, including quarterly allocation <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>, <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.
2.  **Income Details**: Shows actual versus estimated income, quarterly income overview, and income frequency <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.
3.  **Expense Details**: Displays actual versus budgeted expenses, quarterly expense overview, and types of expenses <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>.

## Setting Up the Budget Tracker

[[setting_up_income_and_expenses_in_notion | Setting up income and expenses in Notion]] is done in three simple steps <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>:

1.  Filling out income details <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.
2.  Filling out expense details <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.
3.  Allocating available funds (income minus expenses) to different categories <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.

### Step 1: Building an Income Tracker in Notion

To [[building_an_income_tracker_in_notion | build an income tracker in Notion]], an inline database is created using the `/database` command, then selecting `database inline` <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>, <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>. The database can be named by clicking the three dots, then `layout options`, and `show database title` <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.

#### Income Details Database Columns

The income database includes the following columns:

*   **Income Details**: A title property for each individual income item <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>, <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>.
*   **Source of Income**: A relation property linked to another database, categorizing income (e.g., salary, side hustle, other sources) <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>, <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>, <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.
*   **Month of Income**: A relation property specifying the month income is earned <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>, <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.
*   **Frequency of Income**: A relation property indicating how often income is earned (e.g., recurring, one-time) <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>, <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>, <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.
*   **Expected Income**: A number property set to a currency format (e.g., US Dollars) for anticipated income <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>, <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>, <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>.
*   **Actual Income**: A number property for the income actually earned, also in currency format <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>, <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>.
*   **Difference**: A formula property calculating the difference between actual and expected income <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>, <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.

#### Deeper Analysis with Related Databases

For comprehensive analysis, columns like "Source of Income," "Month of Income," and "Frequency of Income" use a **relation property** to link to separate databases <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>, <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>, <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>, <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.

*   **Income Type Database**: Used to calculate total actual income, budgeted income, difference, and percentage change for each income category (e.g., salary, side hustle) <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>, <a class="yt-timestamp" data-t="00:08:07">[00:08:07]</a>.
*   **Month of Income Database**: Tracks expected income, actual income, and the proportion of actual to budgeted income for each month <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>, <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>.
*   **Frequency of Income Database**: Determines total actual and expected income for recurring versus one-time income sources <a class="yt-timestamp" data-t="00:11:23">[00:11:23]</a>, <a class="yt-timestamp" data-t="00:11:37">[00:11:37]</a>.

These related databases leverage the **roll-up property** to pull relevant information (e.g., actual income, expected income) from the original income details database and apply calculations like "sum" <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>, <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>, <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>, <a class="yt-timestamp" data-t="00:10:13">[00:10:13]</a>, <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>. Formulas are used for calculations like percentage of budgeted income (Actual Income / Expected Income) <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>.

#### Income Details on the Main Dashboard

The main dashboard's income details section links to these specialized databases to display information like actual vs. estimated income, quarterly income overview, and frequency of income <a class="yt-timestamp" data-t="00:14:45">[00:14:45]</a>, <a class="yt-timestamp" data-t="00:15:22">[00:15:22]</a>. This is achieved using **linked databases**, created by typing `/link database` <a class="yt-timestamp" data-t="00:15:02">[00:15:02]</a>.

*   **Actual vs. Estimated Income**: Links to the "Income Variance Distribution" database <a class="yt-timestamp" data-t="00:15:22">[00:15:22]</a>.
*   **Quarterly Income Overview**: Links to the "Month of Income" database, displayed in a gallery view, filtered by quarters (Q1: Jan-Mar, Q2: Apr-Jun, etc.) <a class="yt-timestamp" data-t="00:15:38">[00:15:38]</a>. Only actual income and proportion to budgeted income are visible <a class="yt-timestamp" data-t="00:16:02">[00:16:02]</a>.
*   **Frequency of Income**: Links to the "Frequency of Income" database, displayed in a list view, showing actual income, total income, and percentage <a class="yt-timestamp" data-t="00:16:13">[00:16:13]</a>.

### Step 2: How to Build an Expense Tracker in Notion

[[how_to_build_an_expense_tracker_in_notion | Building an expense tracker in Notion]] follows a similar process to the income tracker <a class="yt-timestamp" data-t="00:17:14">[00:17:14]</a>.

#### Expense Details Database Columns

The expense database includes:

*   **Expense Source**: Title property for individual expenses <a class="yt-timestamp" data-t="00:17:19">[00:17:19]</a>.
*   **Month of Expense**: Relation property linked to a database of months <a class="yt-timestamp" data-t="00:17:26">[00:17:26]</a>.
*   **Expense Classification**: Relation property linked to a database with six expense categories (e.g., utility/bills, loans/debts, food/groceries, entertainment, travel/transportation, others) <a class="yt-timestamp" data-t="00:17:36">[00:17:36]</a>.
*   **Expense Type**: Relation property linked to a database classifying expenses as variable or fixed <a class="yt-timestamp" data-t="00:17:56">[00:17:56]</a>.
*   **Budgeted Expense**: Number property (US Dollars) for expected expenses <a class="yt-timestamp" data-t="00:18:06">[00:18:06]</a>.
*   **Actual Expense**: Number property (US Dollars) for actual expenses incurred <a class="yt-timestamp" data-t="00:18:15">[00:18:15]</a>.
*   **Difference**: Formula property to show the difference between actual and budgeted expenses. A positive difference means actual was less than budgeted, while negative means actual was greater <a class="yt-timestamp" data-t="00:18:23">[00:18:23]</a>.

#### Expense Details on the Main Dashboard

Similar to income details, the main dashboard's expense section uses linked databases for different views:

*   **Actual vs. Budgeted Expense**: Links to the "Expense Variance Analysis" database, displayed in gallery mode, showing total budgeted expense, total actual expense, difference, and change in percentage <a class="yt-timestamp" data-t="00:18:51">[00:18:51]</a>, <a class="yt-timestamp" data-t="00:19:11">[00:19:11]</a>.
*   **Quarterly Expense Overview**: Links to the "Month of Expense" database, in gallery view, showing actual expense and proportion to budgeted expense for each month, categorized by quarter <a class="yt-timestamp" data-t="00:19:24">[00:19:24]</a>.
*   **Type of Expense**: Links to the "Type of Expense" database, in list view, segregating expenses into variable and fixed, displaying actual expenses and their proportion to total expenses <a class="yt-timestamp" data-t="00:19:45">[00:19:45]</a>.

### Step 3: Allocation of Available Funds

This step involves calculating and allocating the available funds (income minus expenses) <a class="yt-timestamp" data-t="00:21:25">[00:21:25]</a>.

#### Fund Allocation Database Columns

*   **Available Funds**: A formula property calculates total income less total expenses for each month <a class="yt-timestamp" data-t="00:21:28">[00:21:28]</a>, <a class="yt-timestamp" data-t="00:21:41">[00:21:41]</a>.
*   **Investment, Savings, Others**: Number properties (US Dollars) where available funds are allocated <a class="yt-timestamp" data-t="00:21:51">[00:21:51]</a>, <a class="yt-timestamp" data-t="00:22:09">[00:22:09]</a>.
*   **Total Allocation**: A formula property summing investments, savings, and other allocations <a class="yt-timestamp" data-t="00:22:00">[00:22:00]</a>, <a class="yt-timestamp" data-t="00:22:15">[00:22:15]</a>.
*   **Percentage of Allocation**: A formula property calculating (Total Allocation / Total Available Funds), displayed as a percentage and a bar <a class="yt-timestamp" data-t="00:22:26">[00:22:26]</a>, <a class="yt-timestamp" data-t="00:22:37">[00:22:37]</a>.

#### Fund Allocation on the Main Dashboard

*   **Fund Allocation Overview**: Shows investments, savings, and other allocations, along with the total allocated amount and its proportion to total available funds <a class="yt-timestamp" data-t="00:20:27">[00:20:27]</a>, <a class="yt-timestamp" data-t="00:20:51">[00:20:51]</a>. Each allocation is linked to the "Allocation of Funds" database and displayed in gallery view, showing investment source, allocation amount, and percentage <a class="yt-timestamp" data-t="00:23:14">[00:23:14]</a>, <a class="yt-timestamp" data-t="00:23:22">[00:23:22]</a>.
*   **Quarterly Allocation Overview**: Provides a monthly allocation overview, showing total available funds for each month and the proportion of funds allocated. This is linked to the "Available Funds" database, displayed in gallery mode, filtered by quarter <a class="yt-timestamp" data-t="00:20:57">[00:20:57]</a>, <a class="yt-timestamp" data-t="00:21:10">[00:21:10]</a>, <a class="yt-timestamp" data-t="00:23:38">[00:23:38]</a>.

This Notion budget planner provides a comprehensive tool for [[utilizing_notion_dashboards_for_financial_tracking | utilizing Notion dashboards for financial tracking]] and management <a class="yt-timestamp" data-t="00:24:02">[00:24:02]</a>.