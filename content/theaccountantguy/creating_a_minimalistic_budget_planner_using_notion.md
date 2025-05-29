---
title: Creating a minimalistic budget planner using Notion
videoId: C9gr5yS8EPc
---

From: [[theaccountantguy]] <br/> 

This article outlines how to [[notion_monthly_budget_planner_setup | create a minimalistic budget planner]] within [[using_notion_for_personal_finance_management | Notion]] to [[tracking_personal_finances_in_notion | track income and expenses]] <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>. The planner aims to provide a central location for financial oversight <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>, help fix monthly income goals for performance assessment <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>, categorize expenses for improvement identification <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>, and set/monitor monthly budgets <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>. The [[overview_of_notion_budget_tracker_template | budget tracker]] is accessible from any device <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.

To begin, one needs to sign up for a [[using_notion_for_personal_finance_management | Notion]] account <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.

## Dashboard Segments

The [[overview_of_notion_budget_tracker_template | dashboard]] is composed of three main segments <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>:

*   **Summary Segment**: Provides an overall view of income, expenses, and allocation of funds <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>, including quarterly allocation <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.
*   **Income Details**: Shows actual versus estimated income, quarterly income overview, and income frequency <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.
*   **Expense Details**: Displays actual versus budgeted expenses, quarterly expense overview, and types of expenses <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>.

## Setting Up the Budget Planner

The [[notion_monthly_budget_planner_setup | budget planner setup]] involves three steps <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>:

1.  **Filling out Income Details**: Inputting income information for each month <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>.
2.  **Filling out Expense Details**: Entering expense data for each individual month <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.
3.  **Allocating Available Funds**: Distributing the remaining funds (income minus expenses) across different allocations for each month <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.

### Step 1: Filling Out Income Details

The first step involves [[tracking_personal_finances_in_notion | filling up the income details]] <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a> by [[creating_and_managing_budgets_in_notion | creating an inline database]] <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>.

#### Income Database Columns

The income inline database includes the following columns <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>:

*   **Income Details**: A title property, specifying each individual income earned in a month <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>. This database can be named "expected income Source details" <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>.
*   **Source of Income**: A relation property linked to another database, categorizing income (e.g., salary, side hustle, other sources) <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>. This provides better analysis for each source <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.
*   **Month of Income**: A relation property linked to another database, specifying the month income is earned <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.
*   **Frequency of Income**: A relation property linked to another database, indicating how frequently income is earned (e.g., recurring, one-time) <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
*   **Expected Income**: A number property (e.g., US dollars) for anticipated monthly income <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>.
*   **Actual Income**: A number property (e.g., US dollars) for the income actually earned <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>.
*   **Difference**: A formula property calculating the difference between actual and expected income <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>.

#### Linking Databases for Income Analysis (Relation & Roll-up Properties)

To get detailed income analysis, relation and roll-up properties are used to link the primary income database with other databases <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>:

*   **Income Type Database**: Used to calculate total actual and expected income for specific income sources (e.g., salary, side hustle) <a class="yt-timestamp" data-t="00:08:05">[00:08:05]</a>. The roll-up property pulls actual and expected income from the original database and calculates sums <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>.
*   **Month of Income Database**: Used to calculate total actual and expected income for specific months <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>. It also calculates the proportion of actual income to budgeted income for each month using a formula (Total Actual Income / Total Expected Income), displayed as a percentage and a bar <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>.
*   **Frequency of Income Database**: Used to calculate total actual and expected income for recurring or one-time income sources <a class="yt-timestamp" data-t="00:11:35">[00:11:35]</a>. It also determines the proportion of each income type to the total income using a formula <a class="yt-timestamp" data-t="00:12:37">[00:12:37]</a>.

#### Displaying Income Details on the Primary Dashboard

Linked databases are used to display aggregated income information on the main dashboard <a class="yt-timestamp" data-t="00:14:47">[00:14:47]</a>. A linked database can be created by typing `/link database` <a class="yt-timestamp" data-t="00:15:02">[00:15:02]</a>.

*   **Actual vs. Estimated Income**: Links the `Income Variance Distribution` database <a class="yt-timestamp" data-t="00:15:22">[00:15:22]</a>.
*   **Quarterly Income Overview**: Links the `Month of Income` database and displays it in a gallery view, filtered by quarter (e.g., Q1: Jan, Feb, Mar) <a class="yt-timestamp" data-t="00:15:38">[00:15:38]</a>. Only actual income and its proportion to budgeted income are visible <a class="yt-timestamp" data-t="00:16:04">[00:16:04]</a>.
*   **Frequency of Income**: Links the `Frequency of Income` database and displays it in a list view, showing actual income, total income, and percentage for different income heads <a class="yt-timestamp" data-t="00:16:13">[00:16:13]</a>.

### Step 2: Filling Out Expense Details

The expense details section is similar to the income details, providing subsections for actual vs. budgeted expense, quarterly expense overview, and type of expenses <a class="yt-timestamp" data-t="00:16:33">[00:16:33]</a>.

#### Expense Database Columns

The expense database includes <a class="yt-timestamp" data-t="00:17:17">[00:17:17]</a>:

*   **Expense Source**: Specifies the expense details <a class="yt-timestamp" data-t="00:17:19">[00:17:19]</a>.
*   **Month of Expense**: A relation property linked to another database, indicating when an expense is incurred <a class="yt-timestamp" data-t="00:17:26">[00:17:26]</a>.
*   **Expense Classification**: Segregated into six heads (e.g., utility/bills, loans/debts, food/groceries, entertainment, travel/transportation) <a class="yt-timestamp" data-t="00:17:36">[00:17:36]</a>, linked via a relation property <a class="yt-timestamp" data-t="00:17:49">[00:17:49]</a>.
*   **Expense Type**: Specified as variable or fixed expense <a class="yt-timestamp" data-t="00:17:56">[00:17:56]</a>, linked via a relation property to the `Type of Expense` database <a class="yt-timestamp" data-t="00:18:00">[00:18:00]</a>.
*   **Budgeted Expense**: A number property (e.g., US dollars) for expected monthly expenses <a class="yt-timestamp" data-t="00:18:06">[00:18:06]</a>.
*   **Actual Expense**: A number property (e.g., US dollars) for actual monthly expenses <a class="yt-timestamp" data-t="00:18:15">[00:18:15]</a>.
*   **Difference**: Calculates the difference between budgeted and actual expenses. A positive difference means actual was less than budgeted; a negative difference means budgeted was less than actual <a class="yt-timestamp" data-t="00:18:23">[00:18:23]</a>.

#### Displaying Expense Details on the Primary Dashboard

*   **Actual vs. Budgeted Expense**: Links the `Expense Variance Analysis` database, providing total budgeted and actual expenses, difference, and percentage change <a class="yt-timestamp" data-t="00:18:51">[00:18:51]</a>. This is displayed in a gallery view <a class="yt-timestamp" data-t="00:19:11">[00:19:11]</a>.
*   **Quarterly Expense Overview**: Links the `Month of Expense` database, showing actual expense and its proportion to budgeted expense for each month, also in a gallery view <a class="yt-timestamp" data-t="00:19:24">[00:19:24]</a>.
*   **Type of Expenses**: Links the `Type of Expense` database, categorizing expenses as variable or fixed, and displaying actual expenses and their proportion to total expenses in a list view <a class="yt-timestamp" data-t="00:19:45">[00:19:45]</a>.

### Step 3: Allocating Available Funds

This step involves [[creating_a_savings_funds_tracker_in_notion | allocating available funds]] (income minus expenses) to different heads <a class="yt-timestamp" data-t="00:20:20">[00:20:20]</a>.

#### Fund Allocation Database

*   **Available Funds**: Calculated using a formula: `Total Income - Total Expenses` <a class="yt-timestamp" data-t="00:21:28">[00:21:28]</a>. The total income is rolled up from the month-of-income database, and actual expenses are drawn from the month-of-expense database <a class="yt-timestamp" data-t="00:22:53">[00:22:53]</a>.
*   **Allocation Heads**: Funds are allocated to categories such as `Investment`, `Savings`, and `Others`, each represented by a number property in US dollars <a class="yt-timestamp" data-t="00:21:52">[00:21:52]</a>.
*   **Total Allocation**: Summation of investments, savings, and other allocations, calculated by a formula <a class="yt-timestamp" data-t="00:22:00">[00:22:00]</a>.
*   **Percentage of Allocation**: Calculated as `Total Allocation / Total Available Funds`, set to a percentage format and represented by a bar <a class="yt-timestamp" data-t="00:22:26">[00:22:26]</a>.

#### Fund Allocation Overview on Dashboard

*   **Fund Allocation Overview**: Provides analysis of remaining funds allocated to different heads (Investment, Savings, Others) <a class="yt-timestamp" data-t="00:20:27">[00:20:27]</a>. Each individual fund is calculated by being linked to the individual databases <a class="yt-timestamp" data-t="00:23:14">[00:23:14]</a>. This is displayed in a gallery view with three visible properties: investment source, allocation amount, and percentage of allocation <a class="yt-timestamp" data-t="00:23:22">[00:23:22]</a>.
*   **Quarterly Allocation Overview**: Gives a monthly allocation overview showing total available funds for each month and the proportion of funds allocated, broken down by quarters <a class="yt-timestamp" data-t="00:20:59">[00:20:59]</a>. This links to the `Available Funds` database and is set to gallery mode <a class="yt-timestamp" data-t="00:23:38">[00:23:38]</a>.

This [[budget_management_with_notion | comprehensive budget tracker]] in [[using_notion_for_personal_finance_management | Notion]] allows for detailed [[tracking_personal_finances_in_notion | financial tracking]] and analysis <a class="yt-timestamp" data-t="00:24:02">[00:24:02]</a>.
The template discussed can be obtained by visiting the online store at `theaccountantguy.gumroad.com` <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.