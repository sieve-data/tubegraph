---
title: Expense Tracking in Notion
videoId: C9gr5yS8EPc
---

From: [[theaccountantguy]] <br/> 

This article details how to create a minimalistic budget planner using Notion to keep track of income and expenses <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. This dashboard allows users to:
*   Keep track of income and expenses in a central location <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>.
*   Set monthly income goals for performance assessment <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>.
*   Categorize expenses to identify areas for improvement <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.
*   Set and monitor monthly budgets for different categories <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.
*   Access the budget tracker from any device <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.

This template is designed for [[using_notion_for_personal_and_business_expense_tracking | personal and business expense tracking]], and provides a comprehensive approach to [[budgeting_and_tracking_in_notion | budgeting and tracking]] finances <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>.

## Accessing the Template
The template can be obtained by visiting the online store at `theaccountantguy.gumroad.com` <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>. To use the template, a Notion account is required <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>.

## Dashboard Segments
The dashboard is composed of three main segments <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>:
1.  **Summary Segment** <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>: Provides an overall view of income, expenses, and allocation of funds, including quarterly allocation <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.
2.  **Income Details** <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>: Shows details of actual versus estimated income, quarterly income overview, and frequency of income <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.
3.  **Expense Details** <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>: Presents actual versus budgeted expenses, quarterly expense overview, and type of expenses <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.

## Setting Up the Budget Tracker
Setting up this budget tracker involves three simple steps <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>:

1.  **Filling out the income details** for each month <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.
2.  **Filling out the expense details** for each individual month <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.
3.  **Allocating the available funds** (income minus expenses) for each month into different allocations <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.

### Step 1: Filling Income Details
To begin [[tracking_income_and_expenses_in_notion | tracking your income and expenses in Notion]], the first step is to fill in the income details <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>. This is done by creating an inline database <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>.

#### Creating an Inline Database
An inline database can be created by typing `/` followed by `database` and selecting `database inline` <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>. The database can be named, for example, "Expected Income Source Details" by clicking on the three dots, selecting layout options, and enabling "show database title" <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.

#### Columns in the Income Database
The inline database for income details includes the following columns <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>:
*   **Income Details** <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>: A title property that describes each individual income earned in a month <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.
*   **Source of Income** <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>: A relation property linked to an "Income Type" database, categorizing income (e.g., Salary, Side Hustle, Other Sources) <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>. Linking to another database allows for better analysis <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.
*   **Month of Income** <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>: A relation property linked to a "Month of Income" database, specifying the month income is earned <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.
*   **Frequency of Income** <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>: A relation property linked to a "Frequency of Income" database, indicating how frequently income is earned (e.g., Recurring, One-time) <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>.
*   **Expected Income** <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>: A number property showing the expected income for a month, formatted as currency (e.g., US dollars) <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>.
*   **Actual Income** <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>: A number property showing the actual income earned at the end of a month, also formatted as currency <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>.
*   **Difference** <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>: A formula property calculating the difference between actual income and expected income <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.

#### Using Relation and Roll-up Properties for Analysis
To obtain detailed insights for [[tracking_income_and_expenses_using_notion | tracking your income and expenses using Notion]], the template uses relation and roll-up properties <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>.

*   **Actual vs. Estimated Income** <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>: This section provides total actual income, total estimated income, their difference, and percentage change for different income types <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>. This is achieved by linking the primary income database to an "Income Type" database, then using roll-up properties to sum actual and expected incomes for each category <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>. An "Income Variance Distribution" database is also linked to show estimated vs. actual income and percentage change <a class="yt-timestamp" data-t="00:13:08">[00:13:08]</a>.
*   **Quarterly Income Overview** <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>: Displays total actual income and the proportion of actual income to budgeted income for each month, divided into quarters <a class="yt-timestamp" data-t="00:06:59">[00:06:59]</a>. This links to the "Month of Income" database <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>. Roll-up properties calculate expected and actual income for each month <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>. A formula (total actual income / total expected income) calculates the percentage of budgeted income, which can be represented by a bar <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>. This section is filtered by quarters (Q1: Jan-Mar, Q2: Apr-Jun, etc.) <a class="yt-timestamp" data-t="00:15:46">[00:15:46]</a>.
*   **Frequency of Income** <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>: Shows how frequently income is earned (recurring or one-time), displaying total actual income and its proportion/percentage for each frequency type <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>. This links to a "Frequency of Income" database, where roll-up properties are used to sum expected and actual incomes for each frequency <a class="yt-timestamp" data-t="00:11:35">[00:11:35]</a>. The proportion of each income form to total income is calculated using a formula (total income of each mode / total actual income) <a class="yt-timestamp" data-t="00:12:37">[00:12:37]</a>.

#### Linking Databases in the Main Dashboard
To display these sections on the main dashboard, linked databases are used <a class="yt-timestamp" data-t="00:15:02">[00:15:02]</a>. This is done by typing `/` and then `link database` <a class="yt-timestamp" data-t="00:15:05">[00:15:05]</a>.
*   For "Actual versus Estimated Income details," the "Income Variance Distribution" database is linked <a class="yt-timestamp" data-t="00:15:22">[00:15:22]</a>.
*   For "Quarterly Income Overview," the "Month of Income" database is linked and set to a gallery view, filtered by quarters <a class="yt-timestamp" data-t="00:15:38">[00:15:38]</a>.
*   For "Frequency of Income," the "Frequency of Income" database is linked and set to a list view <a class="yt-timestamp" data-t="00:16:13">[00:16:13]</a>.

### Step 2: Filling Expense Details
The expense details section is similar to income details but with more categories <a class="yt-timestamp" data-t="00:16:33">[00:16:33]</a>. This section is crucial for effective [[business_expense_tracking_with_notion | business expense tracking with Notion]].

#### Columns in the Expense Database
The main expense database for [[creating_a_notion_expense_tracker | creating a Notion expense tracker]] includes <a class="yt-timestamp" data-t="00:17:14">[00:17:14]</a>:
*   **Expense Source** <a class="yt-timestamp" data-t="00:17:19">[00:17:19]</a>: Specifies the details of the expense <a class="yt-timestamp" data-t="00:17:21">[00:17:21]</a>.
*   **Month of Expense** <a class="yt-timestamp" data-t="00:17:26">[00:17:26]</a>: A relation property linked to a "Month of Expense" database <a class="yt-timestamp" data-t="00:17:30">[00:17:30]</a>.
*   **Expense Classification** <a class="yt-timestamp" data-t="00:17:36">[00:17:36]</a>: A relation property classifying expenses into six heads (e.g., utility and bills, loans and debts, food and groceries, entertainment, [[setting_up_a_travel_expense_tracker_in_notion | travel and transportation]], others) <a class="yt-timestamp" data-t="00:17:38">[00:17:38]</a>. This also allows for [[credit_card_expenses_tracking_in_notion | credit card expenses tracking in Notion]].
*   **Expense Type** <a class="yt-timestamp" data-t="00:17:56">[00:17:56]</a>: A relation property distinguishing between variable and fixed expenses <a class="yt-timestamp" data-t="00:17:58">[00:17:58]</a>.
*   **Budgeted Expense** <a class="yt-timestamp" data-t="00:18:06">[00:18:06]</a>: A number property (US dollars) for the expected expense <a class="yt-timestamp" data-t="00:18:09">[00:18:09]</a>.
*   **Actual Expense** <a class="yt-timestamp" data-t="00:18:15">[00:18:15]</a>: A number property (US dollars) for the actual expense incurred <a class="yt-timestamp" data-t="00:18:17">[00:18:17]</a>.
*   **Difference** <a class="yt-timestamp" data-t="00:18:23">[00:18:23]</a>: Shows the difference between actual and budgeted expenses. A positive difference means actual was less than budgeted; a negative difference means budgeted was less than actual <a class="yt-timestamp" data-t="00:18:25">[00:18:25]</a>.

#### Expense Analysis Sections
The expense details sections are linked to other databases for detailed analysis for [[using_notion_for_expense_management | expense management in Notion]] <a class="yt-timestamp" data-t="00:18:44">[00:18:44]</a>:
*   **Actual versus Budgeted Expense** <a class="yt-timestamp" data-t="00:18:55">[00:18:55]</a>: Linked to an "Expense Variance Analysis" database, displaying total budgeted expense, total actual expense, difference, and change in percentage. This is in a gallery view <a class="yt-timestamp" data-t="00:18:57">[00:18:57]</a>.
*   **Quarterly Expense Overview** <a class="yt-timestamp" data-t="00:19:24">[00:19:24]</a>: For each month, shows actual expense and its proportion to budgeted expense. This is a gallery view linked to the "Month of Expense" database <a class="yt-timestamp" data-t="00:19:26">[00:19:26]</a>.
*   **Type of Expenses** <a class="yt-timestamp" data-t="00:19:45">[00:19:45]</a>: Segregates expenses into variable and fixed types, showing total actual expenses and their proportion to total expenses <a class="yt-timestamp" data-t="00:19:48">[00:19:48]</a>. This is a list view linked to the "Type of Expense" database <a class="yt-timestamp" data-t="00:19:57">[00:19:57]</a>.

### Step 3: Allocating Funds
Once income and expense details are complete, the next step is to allocate available funds <a class="yt-timestamp" data-t="00:21:19">[00:21:19]</a>. Available funds are calculated as `income - expenses` for each month <a class="yt-timestamp" data-t="00:21:30">[00:21:30]</a>.

#### Fund Allocation Overview
This section provides an analysis of remaining funds allocated to different heads <a class="yt-timestamp" data-t="00:21:27">[00:21:27]</a>:
*   **Investment Section** <a class="yt-timestamp" data-t="00:20:34">[00:20:34]</a>
*   **Savings Section** <a class="yt-timestamp" data-t="00:20:37">[00:20:37]</a>
*   **Others Section** <a class="yt-timestamp" data-t="00:20:37">[00:20:37]</a>

The overview shows the total allocation amount and the proportion of allocation to the total available funds <a class="yt-timestamp" data-t="00:20:51">[00:20:51]</a>.

#### Quarterly Allocation Overview
A quarterly allocation overview provides monthly allocation details, showing total available funds for each month and the proportion of funds allocated for each month <a class="yt-timestamp" data-t="00:20:57">[00:20:57]</a>.

#### Columns in the Allocation Database
The allocation database includes:
*   **Available Funds** <a class="yt-timestamp" data-t="00:21:28">[00:21:28]</a>: Calculated using a formula (`total income - total expenses`) <a class="yt-timestamp" data-t="00:21:41">[00:21:41]</a>. The total actual income and actual expense values are drawn using roll-up properties from their respective databases <a class="yt-timestamp" data-t="00:22:53">[00:22:53]</a>.
*   **Investments**, **Savings**, and **Other Allocations**: Number properties (US dollars) where desired allocation amounts are entered <a class="yt-timestamp" data-t="00:21:56">[00:21:56]</a>.
*   **Total Allocation** <a class="yt-timestamp" data-t="00:22:01">[00:22:01]</a>: A formula that sums Investments, Savings, and Other Allocations <a class="yt-timestamp" data-t="00:22:15">[00:22:15]</a>.
*   **Percentage of Allocation** <a class="yt-timestamp" data-t="00:22:26">[00:22:26]</a>: A formula `total allocation / total available funds`, formatted as a percentage and represented by a bar <a class="yt-timestamp" data-t="00:22:28">[00:22:28]</a>.

#### Linking Allocation Databases
*   The "Fund Allocation Overview" links to an "Allocation of Funds" database, displayed in a gallery layout, showing investment source, allocation amount, and percentage of allocation <a class="yt-timestamp" data-t="00:23:14">[00:23:14]</a>.
*   The "Quarterly Allocation Overview" links to an "Available Funds" database, also in gallery mode, displaying the month, total available funds, and percentage of allocation for each month, categorized by quarter <a class="yt-timestamp" data-t="00:23:38">[00:23:38]</a>.