---
title: Setting up a database in Notion for financial tracking
videoId: C9gr5yS8EPc
---

From: [[theaccountantguy]] <br/> 

This guide explains how to create a minimalistic budget planner using Notion to track income and expenses in one central location <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. This dashboard allows users to fix monthly income goals, assess performance, categorize expenses for improvement, and monitor monthly budgets for different categories <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>. The budget tracker is accessible from any device <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. To use this template, a Notion account is required <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.

## Budget Planner Dashboard Segments

The dashboard consists of three main segments <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>:

1.  **Summary Segment**: Provides an overall view of income, expenses, and fund allocation <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. It includes summaries of income, expenses, fund allocation, and quarterly allocation of funds <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.
2.  **Income Details**: Shows details of actual versus estimated income, quarterly income overview, and frequency of income <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.
3.  **Expense Details**: Presents details of actual versus budgeted expenses, quarterly expense overview, and types of expenses <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>.

## Setting Up the Budget Planner

[[setting_up_a_personal_finance_tracker_in_notion | Setting up this budget tracker]] involves three simple steps <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>:

1.  Filling out the income details for each month <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.
2.  Filling out the expense details for each individual month <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.
3.  Allocating available funds (income minus expenses) for each month into different allocations <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.

### Step 1: Filling Out Income Details

The first step is to [[creating_a_database_in_notion | create a database in Notion]] for income details <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.

#### [[setting_up_a_database_in_notion | Setting up a Database in Notion]] for Income

To create an inline database:
*   Type `/` and then `database` <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.
*   Select `Database - Inline` <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>.

The income details database, named "Expected Income Source Details" <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>, includes the following columns (properties):

*   **Income Details**: This is the default `Title` property, describing each individual income earned in a month <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
*   **Source of Income**: A `Relation` property linked to another database, categorizing income (e.g., salary, side hustle, other sources) <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>. This provides better analysis for each income source <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.
*   **Month of Income**: A `Relation` property specifying the month income is earned, linked to another database <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.
*   **Frequency of Income**: A `Relation` property indicating how frequently income is earned (e.g., recurring, one-time), linked to another database <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.
*   **Expected Income**: A `Number` property (e.g., US dollars) for the anticipated income in a month <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.
*   **Actual Income**: A `Number` property (e.g., US dollars) for the income earned at the end of the month <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>.
*   **Difference**: A `Formula` property calculating the difference between `Actual Income` and `Expected Income` <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>.

To make the database title visible, click the three dots, then layout options, and enable "Show database title" <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>. The title can then be edited <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>.

#### Analyzing Income Details with Related Databases

To gain deeper insights, several databases are linked to the primary income database using `Relation` and `Roll-up` properties <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>.

*   **Income Type Database**: Used to calculate total actual income, total budgeted income, their difference, and percentage change for various income sources (salary, side hustle, others) <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>. This is achieved by creating a `Relation` to this database and then using `Roll-up` properties to sum `Actual Income` and `Expected Income` from the original income database <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>.

*   **Month of Income Database**: Allows calculation of total actual income, total expected income, and the proportion of actual to budgeted income for each month <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>. `Relation` and `Roll-up` properties are again used to pull values from the original income database <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>. A formula (`Total Actual Income` / `Total Expected Income`) is used to calculate the percentage of budgeted income, which can be visualized with a bar <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>.

*   **Frequency of Income Database**: Helps calculate total actual and expected income for recurring versus one-time income sources <a class="yt-timestamp" data-t="00:11:22">[00:11:22]</a>. Similar `Relation` and `Roll-up` properties are applied <a class="yt-timestamp" data-t="00:11:35">[00:11:35]</a>. The proportion of each income form to the total income is calculated using a formula <a class="yt-timestamp" data-t="00:12:37">[00:12:37]</a>.

*   **Income Variance Distribution Database**: Calculates total estimated income, total actual income, their difference, and percentage change for each income head <a class="yt-timestamp" data-t="00:13:08">[00:13:08]</a>. This also uses `Relation` and `Roll-up` properties, along with `if` formulas to display specific values based on the field type (e.g., total estimated, total actual, difference, change in percentage) <a class="yt-timestamp" data-t="00:13:22">[00:13:22]</a>.

#### Displaying Income Details on the Dashboard

On the primary dashboard, the income details sections (actual versus estimated income, quarterly income overview, frequency of income) are created by linking these different databases <a class="yt-timestamp" data-t="00:14:45">[00:14:45]</a>.

To create a linked database:
*   Type `/` and then `link database` <a class="yt-timestamp" data-t="00:15:02">[00:15:02]</a>.
*   Select the desired database to link <a class="yt-timestamp" data-t="00:15:10">[00:15:10]</a>.

*   **Actual vs. Estimated Income**: Links the `Income Variance Distribution` database <a class="yt-timestamp" data-t="00:15:22">[00:15:22]</a>.
*   **Quarterly Income Overview**: Links the `Month of Income` database and is set to a `Gallery` view. Filters are applied for each quarter (e.g., Q1 for Jan, Feb, Mar) <a class="yt-timestamp" data-t="00:15:38">[00:15:38]</a>. Only actual income and the proportion of actual income to budgeted income are made visible <a class="yt-timestamp" data-t="00:16:02">[00:16:02]</a>.
*   **Frequency of Income**: Links the `Frequency of Income` database and is set to a `List` view, displaying actual income, total income, and percentage <a class="yt-timestamp" data-t="00:16:13">[00:16:13]</a>.

### Step 2: Filling Out Expense Details

[[creating_databases_for_an_expense_tracker_in_notion | Creating databases for an expense tracker in Notion]] involves setting up an expense database with similar principles to the income database <a class="yt-timestamp" data-t="00:17:14">[00:17:14]</a>.

#### [[databases_used_in_notion_bills_tracker | Databases Used in Notion Bills Tracker]] for Expenses

The main expense database includes:

*   **Expense Source**: `Title` property specifying expense details <a class="yt-timestamp" data-t="00:17:19">[00:17:19]</a>.
*   **Month of Expense**: `Relation` property linked to another database, similar to income <a class="yt-timestamp" data-t="00:17:26">[00:17:26]</a>.
*   **Expense Classification**: `Relation` property categorizing expenses into heads like utility and bills, loans and debts, food and groceries, entertainment, travel, and transportation <a class="yt-timestamp" data-t="00:17:36">[00:17:36]</a>.
*   **Expense Type**: `Relation` property specifying expenses as `Variable` or `Fixed`, linked to the `Type of Expense` database <a class="yt-timestamp" data-t="00:17:56">[00:17:56]</a>.
*   **Budgeted Expense**: `Number` property (e.g., US dollars) for expected expenses <a class="yt-timestamp" data-t="00:18:06">[00:18:06]</a>.
*   **Actual Expense**: `Number` property (e.g., US dollars) for actual expenses incurred <a class="yt-timestamp" data-t="00:18:15">[00:18:15]</a>.
*   **Difference**: Formula calculating the difference between `Actual Expense` and `Budgeted Expense`. A positive difference means actual was less than budgeted, while negative means actual exceeded budgeted <a class="yt-timestamp" data-t="00:18:23">[00:18:23]</a>.

#### Analyzing and Displaying Expense Details

Similar to income, expense details are categorized and displayed using linked databases:

*   **Actual vs. Budgeted Expense**: This section is linked to the `Expense Variance Analysis` database. It provides total budgeted expense, total actual expense, their difference, and percentage change <a class="yt-timestamp" data-t="00:18:51">[00:18:51]</a>. This is typically set to a `Gallery` view <a class="yt-timestamp" data-t="00:19:11">[00:19:11]</a>.
*   **Quarterly Expense Overview**: Linked to the `Month of Expense` database, displayed in a `Gallery` view. It shows actual expense and the proportion of actual to budgeted expense for each month, filtered by quarter <a class="yt-timestamp" data-t="00:19:24">[00:19:24]</a>.
*   **Type of Expenses**: Linked to the `Type of Expense` database and set to a `List` view. It segregates expenses into `Variable` and `Fixed`, showing total actual expenses for each type and their proportion to total expense <a class="yt-timestamp" data-t="00:19:45">[00:19:45]</a>.

### Step 3: Allocating Available Funds

[[databases_required_for_tracking_net_worth_in_notion | Databases required for tracking net worth in Notion]] often include fund allocation. This step involves calculating available funds (income minus expenses) and allocating them to different heads <a class="yt-timestamp" data-t="00:21:19">[00:21:19]</a>.

#### [[creating_a_database_in_notion_for_calculations | Creating a Database in Notion for Calculations]] for Fund Allocation

An `Available Funds` database calculates the `Total Income` minus `Total Expenses` for each month using a formula <a class="yt-timestamp" data-t="00:21:41">[00:21:41]</a>.

Once available funds are calculated, they are allocated to specific heads:

*   **Investment**: A `Number` property (e.g., US dollars) for allocated investment amounts <a class="yt-timestamp" data-t="00:22:09">[00:22:09]</a>.
*   **Savings**: A `Number` property (e.g., US dollars) for allocated savings <a class="yt-timestamp" data-t="00:22:11">[00:22:11]</a>.
*   **Others**: A `Number` property (e.g., US dollars) for other allocations <a class="yt-timestamp" data-t="00:22:12">[00:22:12]</a>.
*   **Total Allocation**: A `Formula` property summing `Investment`, `Savings`, and `Other` allocations <a class="yt-timestamp" data-t="00:22:15">[00:22:15]</a>.
*   **Percentage of Allocation**: A `Formula` property (`Total Allocation` / `Total Available Funds`), formatted as a percentage and potentially represented by a bar <a class="yt-timestamp" data-t="00:22:26">[00:22:26]</a>.

The `Total Actual Income` and `Actual Expense` values within the fund allocation overview are derived using `Roll-up` properties from the `Month of Income` and `Month of Expense` databases, respectively <a class="yt-timestamp" data-t="00:22:53">[00:22:53]</a>.

#### Displaying Fund Allocation

*   **Fund Allocation Overview**: Each individual fund (investment, savings, others) is calculated by linking to the `Allocation of Funds` database <a class="yt-timestamp" data-t="00:23:14">[00:23:14]</a>. This is typically displayed in a `Gallery` view showing the `Investment Source`, `Allocation Amount`, and `Percentage of Allocation` <a class="yt-timestamp" data-t="00:23:22">[00:23:22]</a>.
*   **Quarterly Allocation Overview**: Linked to the `Available Funds` database and set to a `Gallery` view. It displays the month, total available funds, and the percentage of allocation for each month, also segmented by quarters <a class="yt-timestamp" data-t="00:23:38">[00:23:38]</a>.

This comprehensive setup enables effective [[tracking_personal_finances_in_notion | tracking personal finances in Notion]] through a well-structured budget planner.