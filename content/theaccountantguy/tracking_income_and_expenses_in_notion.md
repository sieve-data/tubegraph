---
title: Tracking income and expenses in Notion
videoId: C9gr5yS8EPc
---

From: [[theaccountantguy]] <br/> 

This article details how to create and utilize a minimalistic budget planner in Notion to [[managing_finances_with_Notion | manage finances]] efficiently <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. This dashboard allows users to [[budgeting_and_tracking_expenses_in_Notion | keep track of their income and expenses]] in one central location <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>.

Key features include:
*   Fixing monthly income goals to assess overall performance <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>.
*   Categorizing expenses to identify areas for improvement <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.
*   Setting and monitoring monthly budgets for different categories <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.
*   Gaining access to the budget tracker from any device, anywhere <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.

The dashboard is composed of three main segments <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>:
1.  **Summary Segment:** Provides an overall view of income, expenses, and allocation of funds, including quarterly allocation <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.
2.  **Income Details:** Displays actual versus estimated income, quarterly income overview, and frequency of income <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.
3.  **Expense Details:** Shows actual versus budgeted expenses, quarterly expense overview, and types of expenses <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>.

To use this template, a Notion account is required <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.

## Setting Up Your Budget Tracker in Notion

The process involves three simple steps <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>:

### Step 1: Filling Out Income Details

The first step involves filling out the income details for each month <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>. This is done by [[creating_an_income_tracker_in_Notion | creating an income tracker]] in Notion using an inline database <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>. An inline database can be created by typing `/database` and selecting "database inline" <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.

The income details database includes the following columns <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>:
*   **Income Details:** The default title property, specifying each individual income earned <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
*   **Source of Income:** A relation property linked to another database, categorizing income (e.g., Salary, Side Hustle, Other Sources) <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.
*   **Month of Income:** A relation property specifying the month income is earned <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.
*   **Frequency of Income:** A relation property indicating how frequently income is earned (e.g., Recurring, One-time) <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.
*   **Expected Income:** A number property (e.g., US Dollars) for anticipated income <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.
*   **Actual Income:** A number property (e.g., US Dollars) for the income actually earned <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>.
*   **Difference:** A formula property calculating the difference between Actual Income and Expected Income <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>.

#### Utilizing Relation and Roll-up Properties for Income Analysis

To gain detailed insights, Notion's relation and roll-up properties are used to link the primary income database with other databases <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>.

1.  **Income Type Database:** This database helps calculate total actual and budgeted income, difference, and percentage change for each income source (e.g., Salary, Side Hustle) <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>. It uses roll-up properties to pull "Actual Income" and "Expected Income" values from the main income database and sum them <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>.

2.  **Month of Income Database:** This database provides monthly overviews, showing expected income, actual income, and the proportion of actual income to budgeted income for each month <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>. Roll-up properties are used to sum expected and actual incomes, and a formula calculates the percentage: `(Total Actual Income / Total Expected Income)` <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>.

3.  **Frequency of Income Database:** This database helps analyze income based on frequency (recurring vs. one-time), showing total actual and expected income for each mode <a class="yt-timestamp" data-t="00:11:42">[00:11:42]</a>. Roll-up properties sum the relevant income values, and a formula calculates the proportion of each income type to the total income <a class="yt-timestamp" data-t="00:12:37">[00:12:37]</a>.

On the main dashboard, these detailed analyses are displayed using linked databases <a class="yt-timestamp" data-t="00:14:47">[00:14:47]</a>. For example, the "Actual vs. Estimated Income" section links to the "Income Variance Distribution" database <a class="yt-timestamp" data-t="00:15:22">[00:15:22]</a>, while "Quarterly Income Overview" links to the "Month of Income" database, filtered by quarter <a class="yt-timestamp" data-t="00:15:38">[00:15:38]</a>.

### Step 2: Filling Out Expense Details

The second step involves filling out expense details for each individual month <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>. This forms the core of [[using_notion_as_an_expense_tracker | using Notion as an expense tracker]] <a class="yt-timestamp" data-t="00:17:14">[00:17:14]</a>.

The expense details database includes:
*   **Expense Source:** Specifies the expense details <a class="yt-timestamp" data-t="00:17:19">[00:17:19]</a>.
*   **Month of Expense:** A relation property indicating when an expense is incurred <a class="yt-timestamp" data-t="00:17:26">[00:17:26]</a>.
*   **Expense Classification:** A relation property categorizing expenses into heads like Utility and Bills, Loans and Debts, Food and Groceries, Entertainment, Travel, and Transportation <a class="yt-timestamp" data-t="00:17:36">[00:17:36]</a>.
*   **Expense Type:** A relation property classifying expenses as Variable or Fixed <a class="yt-timestamp" data-t="00:17:56">[00:17:56]</a>.
*   **Budgeted Expense:** A number property (e.g., US Dollars) for expected monthly expenses <a class="yt-timestamp" data-t="00:18:06">[00:18:06]</a>.
*   **Actual Expense:** A number property (e.g., US Dollars) for actual monthly expenses <a class="yt-timestamp" data-t="00:18:15">[00:18:15]</a>.
*   **Difference:** Calculates the difference between Actual and Budgeted Expense, indicating if actual spending was less (positive difference) or more (negative difference) than budgeted <a class="yt-timestamp" data-t="00:18:23">[00:18:23]</a>.

Similar to income details, [[budget_and_actual_expense_tracking_in_Notion | actual versus budgeted expense tracking in Notion]] is achieved by linking to other databases like "Expense Variance Analysis" to provide total budgeted expense, total actual expense, difference, and percentage change <a class="yt-timestamp" data-t="00:18:57">[00:18:57]</a>. "Quarterly Expense Overview" links to the "Month of Expense" database for monthly actual expenses and their proportion to budgeted expenses <a class="yt-timestamp" data-t="00:19:24">[00:19:24]</a>. "Type of Expenses" links to the "Type of Expense" database, differentiating between variable and fixed expenses <a class="yt-timestamp" data-t="00:19:45">[00:19:45]</a>.

### Step 3: Allocating Available Funds

The final step is to allocate the available funds, which are calculated as income minus expenses, to different allocation heads for each month <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.

The fund allocation process includes:
*   **Available Funds Calculation:** A formula property calculates `Total Income - Total Expenses` <a class="yt-timestamp" data-t="00:21:41">[00:21:41]</a>.
*   **Allocation Categories:** Users allocate funds to categories such as Investments, Savings, and Others <a class="yt-timestamp" data-t="00:21:51">[00:21:51]</a>. These are number properties, typically set to US Dollars <a class="yt-timestamp" data-t="00:22:09">[00:22:09]</a>.
*   **Total Allocation:** A formula property summing Investments, Savings, and Other allocations <a class="yt-timestamp" data-t="00:22:15">[00:22:15]</a>.
*   **Percentage of Allocation:** A formula property calculated as `Total Allocation / Total Available Funds`, displayed as a percentage and potentially a bar <a class="yt-timestamp" data-t="00:22:26">[00:22:26]</a>.

The main dashboard's "Fund Allocation Overview" and "Quarterly Allocation Overview" sections link to the "Allocation of Funds" and "Available Funds" databases, respectively, displaying allocated amounts and proportions for different categories and quarters <a class="yt-timestamp" data-t="00:23:14">[00:23:14]</a>.

This structured approach to [[tracking_personal_finances_in_notion | tracking personal finances in Notion]] provides a comprehensive overview of your financial performance <a class="yt-timestamp" data-t="00:24:01">[00:24:01]</a>.