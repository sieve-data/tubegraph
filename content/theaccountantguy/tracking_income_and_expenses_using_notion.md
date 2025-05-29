---
title: Tracking income and expenses using Notion
videoId: C9gr5yS8EPc
---

From: [[theaccountantguy]] <br/> 

This article explains how to create a minimalistic budget planner using [[tracking_personal_finances_using_notion | Notion]] to [[tracking_personal_finances_in_notion | track personal finances]]. This dashboard helps in keeping track of income and expenses in one central location <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>.

## Key Features <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>

*   Fix monthly income goals to assess overall performance <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>.
*   Categorize expenses to identify areas for improvement <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.
*   Set and monitor monthly budgets for different categories <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.
*   Gain access to your budget tracker from any device, anywhere <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.

## Template Acquisition <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>

The template for this budget planner can be obtained by visiting the online store at `theaccountantguy.gumroad.com` <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. To use this template, you need to sign up for a [[tracking_personal_finances_using_notion | Notion]] account <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.

## Dashboard Structure <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>

The dashboard consists of three main segments:

1.  **Summary Segment**: Provides an overall view of income, expenses, and allocation of funds <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>. It includes a summary of income, expenses, fund allocation, and quarterly allocation of funds <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.
2.  **Income Details**: Gives details of actual versus estimated income, quarterly income overview, and frequency of income <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.
3.  **Expense Details**: Provides details of actual versus budgeted expenses, quarterly expense overview, and type of expenses <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>.

## Setting Up the Budget Planner <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>

Setting up the budget planner involves three simple steps <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>:

1.  Filling out the income details for each month <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.
2.  Filling out the expense details for each individual month <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.
3.  Allocating the available funds (income minus expenses) for each month onto different allocations <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.

### Step 1: Filling Income Details <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>

To begin [[tracking_personal_finances_in_notion | tracking personal finances in Notion]], an inline database is created by typing `/` and then `database`, selecting `database inline` <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.

#### Income Database Columns <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>

The income details database has the following columns <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>:

*   **Income Details**: Specifies each individual income earned in a particular month (title type property) <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
*   **Source of Income**: A category for each income (e.g., salary, side hustle, other sources) <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>. This is a relation property linked to an "income type" database for better analysis <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.
*   **Month of Income**: Specifies the month when income is earned <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>. This also has a relation property with another database <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.
*   **Frequency of Income**: Indicates how frequently income is earned (e.g., recurring, one-time) <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>. This is another related database <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.
*   **Expected Income**: A number property (e.g., US dollars) for anticipated monthly income <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.
*   **Actual Income**: A number property (e.g., US dollars) for the income actually earned at month-end <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>.
*   **Difference**: A formula type property calculating `Actual Income - Expected Income` <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>.

#### Using Relation and Roll-Up Properties for Income Analysis <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>

To get detailed income analysis, relation and roll-up properties are used with other databases <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>.

*   **Actual vs. Estimated Income**: The "Source of Income" column is related to an "income type" database <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>. This related database provides total actual income, total budgeted income, difference, and percentage change for each income type (salary, side hustle, others) using roll-up properties <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>.
*   **Quarterly Income Overview**: The "Month of Income" column is related to a "month of income" database <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>. This database uses relation and roll-up properties to calculate expected income, actual income, and the proportion of actual income to budgeted income for each month <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a>. The percentage is calculated with a formula: `Total Actual Income / Total Expected Income` <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>.
*   **Frequency of Income**: The "Frequency of Income" column is related to a "frequency of income" database <a class="yt-timestamp" data-t="00:11:35">[00:11:35]</a>. This database uses relation and roll-up properties to find total actual income and total expected income for recurring or one-time incomes <a class="yt-timestamp" data-t="00:11:44">[00:11:44]</a>. It also calculates the total proportion of each income type to the total income using a formula <a class="yt-timestamp" data-t="00:12:37">[00:12:37]</a>.

### Step 2: Filling Expense Details <a class="yt-timestamp" data-t="00:17:14">[00:17:14]</a>

This step focuses on [[tracking_expenses_with_notion | tracking expenses with Notion]].

#### Expense Database Columns <a class="yt-timestamp" data-t="00:17:17">[00:17:17]</a>

The expense details database has the following columns <a class="yt-timestamp" data-t="00:17:17">[00:17:17]</a>:

*   **Expense Source**: Specifies the details of the expense to be incurred <a class="yt-timestamp" data-t="00:17:19">[00:17:19]</a>.
*   **Month of Expense**: The month when an expense is incurred, linked to another database via a relation property <a class="yt-timestamp" data-t="00:17:26">[00:17:26]</a>.
*   **Expense Classification**: Segregated into six different heads (e.g., utility and bills, loans and debts, food and groceries, entertainment, travel and transportation) <a class="yt-timestamp" data-t="00:17:36">[00:17:36]</a>. This is linked to another database through a relation <a class="yt-timestamp" data-t="00:17:49">[00:17:49]</a>.
*   **Expense Type**: Specified as variable or fixed expense, linked to the "type of expense" database via a relation property <a class="yt-timestamp" data-t="00:17:56">[00:17:56]</a>.
*   **Budgeted Expense**: A number property (US dollars) for the expected expense for a month <a class="yt-timestamp" data-t="00:18:06">[00:18:06]</a>.
*   **Actual Expense**: A number property (US dollars) for the actual expense incurred for a month <a class="yt-timestamp" data-t="00:18:15">[00:18:15]</a>.
*   **Difference**: The difference between actual and budgeted expenses. A positive difference means actual was less than budgeted, while negative means actual was more than budgeted <a class="yt-timestamp" data-t="00:18:23">[00:18:23]</a>.

#### Using Relation and Roll-Up Properties for Expense Analysis <a class="yt-timestamp" data-t="00:18:44">[00:18:44]</a>

Similar to income details, relation and roll-up properties are used for expense analysis:

*   **Actual vs. Budgeted Expense**: Linked to an "expense variance analysis" database, providing total budgeted expense, total actual expense, difference, and percentage change for each expense classification <a class="yt-timestamp" data-t="00:18:55">[00:18:55]</a>.
*   **Quarterly Expense Overview**: Linked to the "month of expense" database, showing actual expense and proportion of actual expense to budgeted expense for each month, divided into quarters <a class="yt-timestamp" data-t="00:19:24">[00:19:24]</a>.
*   **Type of Expenses**: Segregates expenses into variable and fixed types, showing total actual expenses for each type and their proportion to total expense <a class="yt-timestamp" data-t="00:19:45">[00:19:45]</a>.

### Step 3: Fund Allocation <a class="yt-timestamp" data-t="00:20:08">[00:20:08]</a>

This step in [[creating_and_tracking_budgets_and_savings_in_notion | creating and tracking budgets and savings in Notion]] involves allocating available funds.

#### Calculating Available Funds <a class="yt-timestamp" data-t="00:21:28">[00:21:28]</a>

Total available funds are calculated as `Total Income - Total Expenses` for each month <a class="yt-timestamp" data-t="00:21:31">[00:21:31]</a>. This is represented by a formula property <a class="yt-timestamp" data-t="00:21:41">[00:21:41]</a>.

#### Allocating Funds <a class="yt-timestamp" data-t="00:21:48">[00:21:48]</a>

Available funds are allocated to different heads such as:

*   **Investment Section** <a class="yt-timestamp" data-t="00:20:36">[00:20:36]</a>
*   **Savings Section** <a class="yt-timestamp" data-t="00:20:37">[00:20:37]</a>
*   **Others Section** <a class="yt-timestamp" data-t="00:20:38">[00:20:38]</a>

These allocations are number properties, typically in US dollars <a class="yt-timestamp" data-t="00:22:09">[00:22:09]</a>. The total allocation is the summation of investment, savings, and other allocations, represented by a formula <a class="yt-timestamp" data-t="00:22:15">[00:22:15]</a>.

#### Percentage of Allocation <a class="yt-timestamp" data-t="00:22:26">[00:22:26]</a>

The percentage of allocation is calculated as `Total Allocation / Total Available Funds` <a class="yt-timestamp" data-t="00:22:28">[00:22:28]</a>. This is set to a percentage format and can be represented by a bar <a class="yt-timestamp" data-t="00:22:39">[00:22:39]</a>.

## Linked Databases in the Dashboard <a class="yt-timestamp" data-t="00:14:45">[00:14:45]</a>

The primary dashboard links different databases to display the various overviews <a class="yt-timestamp" data-t="00:14:47">[00:14:47]</a>. To create a linked database, type `/` and `link database`, then select the desired database <a class="yt-timestamp" data-t="00:15:02">[00:15:02]</a>.

*   **Actual vs. Estimated Income**: Linked to the "income variance distribution" database <a class="yt-timestamp" data-t="00:15:22">[00:15:22]</a>.
*   **Quarterly Income Overview**: Linked to the "month of income" database and set to a gallery view, filtered by months for each quarter (e.g., Q1: Jan, Feb, Mar) <a class="yt-timestamp" data-t="00:15:38">[00:15:38]</a>.
*   **Frequency of Income**: Linked to the "frequency of income" database and set to a list view <a class="yt-timestamp" data-t="00:16:13">[00:16:13]</a>.
*   **Fund Allocation Overview**: Each individual fund (investment, savings, others) is linked to the "allocation of funds" database, with a gallery layout showing investment source, allocation amount, and percentage of allocation <a class="yt-timestamp" data-t="00:23:14">[00:23:14]</a>.
*   **Quarterly Allocation Overview**: Linked to the "available funds" database, set to a gallery view, displaying month, total available funds, and percentage of allocation for each month <a class="yt-timestamp" data-t="00:23:38">[00:23:38]</a>.

This comprehensive setup allows for effective [[using_notion_for_expense_management | using Notion for expense management]] and [[using_notion_for_expense_tracking | using Notion for expense tracking]], enabling users to [[how_to_build_an_expense_tracker_in_notion | build an expense tracker in Notion]] and manage their finances.