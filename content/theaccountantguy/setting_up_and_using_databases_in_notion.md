---
title: Setting up and using databases in Notion
videoId: C9gr5yS8EPc
---

From: [[theaccountantguy]] <br/> 

Notion can be used to create a minimalistic budget planner, allowing users to track income and expenses in one central location <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>. This dashboard helps fix monthly income goals, categorize expenses for improvement, set and monitor monthly budgets, and is accessible from any device <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>. The budget planner template can be acquired from theaccountantguy.gumroad.com <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.

To utilize this template, a Notion account is required <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>.

## Dashboard Segments <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>
The budget planner dashboard typically consists of three main segments:
*   **Summary Segment:** Provides an overall view of income, expenses, and allocation of funds <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>, including quarterly fund allocation <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.
*   **Income Details:** Shows actual versus estimated income, quarterly income overview, and income frequency <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.
*   **Expense Details:** Displays actual versus budgeted expenses, quarterly expense overview, and types of expenses <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>.

## Setting Up the Budget Planner

The process involves three steps:
1.  Filling out income details <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.
2.  Filling out expense details <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.
3.  Allocating available funds (income minus expenses) for each month <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.

### Step 1: [[setting_up_notion_databases_for_income_tracking | Filling Out Income Details]]

To begin, an inline database must be created <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>. This can be done by typing a forward slash (`/`) and then `database`, selecting the `database inline` option <a class="yt-timestamp" data-t="02:27:00">[02:27:00]</a>.

The database can be named by clicking on the three dots, selecting "layout options," then "show database title," and finally editing the title <a class="yt-timestamp" data-t="04:09:00">[04:09:00]</a>.

#### Income Details Database Columns (Properties) <a class="yt-timestamp" data-t="02:46:00">[02:46:00]</a>

The inline database for income details includes the following columns:

*   **Income Details:** This is the default title property, specifying each individual income earned in a month <a class="yt-timestamp" data-t="02:50:00">[02:50:00]</a>.
*   **Source of Income:** A relation property linked to another database (e.g., "Income Type" database) that categorizes income (e.g., salary, side hustle, other sources) <a class="yt-timestamp" data-t="03:00:00">[03:00:00]</a>. Establishing relationships helps with detailed analysis <a class="yt-timestamp" data-t="04:47:00">[04:47:00]</a>.
*   **Month of Income:** A relation property linked to a "Month of Income" database, indicating the month income is earned <a class="yt-timestamp" data-t="03:20:00">[03:20:00]</a>.
*   **Frequency of Income:** A relation property linked to a "Frequency of Income" database, specifying how often income is earned (e.g., recurring, one-time) <a class="yt-timestamp" data-t="03:25:00">[03:25:00]</a>.
*   **Expected Income:** A number property set as currency (e.g., US dollars), indicating the anticipated income for the month <a class="yt-timestamp" data-t="03:37:00">[03:37:00]</a>. Users can choose their preferred currency <a class="yt-timestamp" data-t="05:25:00">[05:25:00]</a>.
*   **Actual Income:** A number property set as currency (e.g., US dollars), indicating the actual income received <a class="yt-timestamp" data-t="03:46:00">[03:46:00]</a>.
*   **Difference:** A formula-type property that calculates the difference between actual income and expected income <a class="yt-timestamp" data-t="03:53:00">[03:53:00]</a>.

#### [[establishing_relationships_between_notion_databases | Connecting Databases]] for Income Analysis

For a comprehensive analysis of income, individual columns are linked to other Notion databases using "relation" and "roll-up" properties <a class="yt-timestamp" data-t="06:22:00">[06:22:00]</a>:

*   **Income Type Database:**
    *   Linked to the "Source of Income" property <a class="yt-timestamp" data-t="08:03:00">[08:03:00]</a>.
    *   Uses a roll-up property to aggregate the total actual income and total budgeted income for each income type (e.g., salary, side hustle, others) <a class="yt-timestamp" data-t="08:39:00">[08:39:00]</a>. The sum of the desired property (e.g., actual income, expected income) is calculated <a class="yt-timestamp" data-t="08:49:00">[08:49:00]</a>.
    *   Can also calculate the difference and percentage change between actual and budgeted amounts <a class="yt-timestamp" data-t="08:24:00">[08:24:00]</a>.

*   **Month of Income Database:**
    *   Linked to the "Month of Income" property <a class="yt-timestamp" data-t="09:51:00">[09:51:00]</a>.
    *   Utilizes relation and roll-up properties to calculate total expected income, total actual income, and the proportion of actual income to budgeted income for each month <a class="yt-timestamp" data-t="10:11:00">[10:11:00]</a>.
    *   Percentage of budgeted income is calculated using a formula: `(Total Actual Income) / (Total Expected Income)` and formatted as a percentage, which can also be represented visually with a bar <a class="yt-timestamp" data-t="10:54:00">[10:54:00]</a>.

*   **Frequency of Income Database:**
    *   Linked to the "Frequency of Income" property <a class="yt-timestamp" data-t="11:35:00">[11:35:00]</a>.
    *   Uses relation and roll-up properties to determine total actual income and total expected income for recurring and one-time income sources <a class="yt-timestamp" data-t="11:43:00">[11:43:00]</a>.
    *   Calculates the total proportion of each income form to the total income using a formula: `(Total Income of Each Mode) / (Total Actual Income)` <a class="yt-timestamp" data-t="12:37:00">[12:37:00]</a>.

*   **Income Variance Distribution Database:**
    *   Used to calculate total estimated income, total actual income, the difference, and percentage change related to each income head <a class="yt-timestamp" data-t="13:10:00">[13:10:00]</a>.
    *   Employs an `if` formula to display values based on specific field types (e.g., if field is "total estimated income," show estimated income from roll-up property) <a class="yt-timestamp" data-t="13:49:00">[13:49:00]</a>.

#### Displaying Income Details on the Dashboard

On the primary dashboard, linked databases are used to display income details such as actual versus estimated income, quarterly income overview, and frequency of income <a class="yt-timestamp" data-t="14:45:00">[14:45:00]</a>.

*   To create a linked database, type `/` and then `link database` <a class="yt-timestamp" data-t="15:02:00">[15:02:00]</a>.
*   **Actual versus Estimated Income:** Links to the "Income Variance Distribution" database <a class="yt-timestamp" data-t="15:22:00">[15:22:00]</a>.
*   **Quarterly Income Overview:** Links to the "Month of Income" database and is set to a gallery view <a class="yt-timestamp" data-t="15:38:00">[15:38:00]</a>. Filters are applied for each quarter (e.g., Q1 for Jan, Feb, Mar) <a class="yt-timestamp" data-t="15:46:00">[15:46:00]</a>. Only actual income and the proportion of actual income to budgeted income are kept visible <a class="yt-timestamp" data-t="16:02:00">[16:02:00]</a>.
*   **Frequency of Income:** Links to the "Frequency of Income" database and is set to a list view <a class="yt-timestamp" data-t="16:13:00">[16:13:00]</a>. Displays actual income, total income, and percentage <a class="yt-timestamp" data-t="16:21:00">[16:21:00]</a>.

### Step 2: [[using_databases_in_notion_for_expense_tracking | Filling Out Expense Details]]

Similar to income tracking, a database is created for expenses.

#### Expense Details Database Columns (Properties) <a class="yt-timestamp" data-t="17:14:00">[17:14:00]</a>

The database for expenses includes:

*   **Expense Source:** Specifies details of the expense <a class="yt-timestamp" data-t="17:19:00">[17:19:00]</a>.
*   **Month of Expense:** A relation property linked to another database, indicating when an expense is incurred <a class="yt-timestamp" data-t="17:26:00">[17:26:00]</a>.
*   **Expense Classification:** A relation property linked to another database, segregating expenses into categories like utility and bills, loans and debts, food and groceries, entertainment, travel, and transportation <a class="yt-timestamp" data-t="17:36:00">[17:36:00]</a>.
*   **Expense Type:** A relation property linked to a "Type of Expense" database, specifying variable or fixed expenses <a class="yt-timestamp" data-t="17:56:00">[17:56:00]</a>.
*   **Budgeted Expense:** A number property set as currency (e.g., US dollars), indicating the expected expense <a class="yt-timestamp" data-t="18:06:00">[18:06:00]</a>.
*   **Actual Expense:** A number property set as currency (e.g., US dollars), indicating the actual expense <a class="yt-timestamp" data-t="18:15:00">[18:15:00]</a>.
*   **Difference:** A formula property that calculates the difference between actual and budgeted expenses <a class="yt-timestamp" data-t="18:23:00">[18:23:00]</a>. A positive difference means actual expense was less than budgeted, while a negative difference means actual expense was more <a class="yt-timestamp" data-t="18:27:00">[18:27:00]</a>.

#### Displaying Expense Details on the Dashboard

The expense details section in the primary dashboard is similar to the income details:

*   **Actual versus Budgeted Expense:** Linked to an "Expense Variance Analysis" database, displaying total budgeted expense, total actual expense, difference, and change in percentage, often in a gallery view <a class="yt-timestamp" data-t="18:51:00">[18:51:00]</a>.
*   **Quarterly Expense Overview:** Linked to the "Month of Expense" database in a gallery view, showing actual expense and its proportion to budgeted expense for each month <a class="yt-timestamp" data-t="19:24:00">[19:24:00]</a>.
*   **Type of Expenses:** Linked to a "Type of Expense" database in a list view, showing actual expense and its percentage to total expense for variable and fixed expenses <a class="yt-timestamp" data-t="19:45:00">[19:45:00]</a>.

### Step 3: [[using_databases_in_notion_for_finance_management | Allocating Available Funds]]

This step involves calculating available funds (income minus expenses) and allocating them to different heads.

#### Funds Allocation Database Columns <a class="yt-timestamp" data-t="21:19:00">[21:19:00]</a>

*   **Total Available Funds:** A formula property to calculate `(Total Income) - (Total Expenses)` for each month <a class="yt-timestamp" data-t="21:41:00">[21:41:00]</a>. This value is derived using a roll-up property drawing values from the "month-of-income" and "month-of-expense" databases <a class="yt-timestamp" data-t="22:53:00">[22:53:00]</a>.
*   **Investment, Savings, Others:** Number properties set as currency (e.g., US dollars) for allocating funds to these categories <a class="yt-timestamp" data-t="21:56:00">[21:56:00]</a>.
*   **Total Allocation:** A formula property that sums `Investments + Savings + Other Allocations` <a class="yt-timestamp" data-t="22:15:00">[22:22:00]</a>.
*   **Percentage of Allocation:** A formula property calculating `(Total Allocation) / (Total Available Funds)`, formatted as a percentage and can be represented by a bar <a class="yt-timestamp" data-t="22:26:00">[22:26:00]</a>.

#### Displaying Funds Allocation on the Dashboard

*   **Fund Allocation Overview:** Provides an analysis of remaining funds allocated to different heads (e.g., investment, savings, others), showing the allocated amount and proportion to total available funds <a class="yt-timestamp" data-t="20:27:00">[20:27:00]</a>. Each individual allocation is linked to an "Allocation of Funds" database, displayed in a gallery layout with properties for investment source, allocation amount, and percentage of allocation <a class="yt-timestamp" data-t="23:14:00">[23:14:00]</a>.
*   **Quarterly Allocation Overview:** Shows a monthly allocation overview, detailing total available funds and the proportion of funds allocated for each month, categorized by quarter <a class="yt-timestamp" data-t="20:59:00">[20:59:00]</a>. This is linked to an "Available Funds" database, set to gallery mode, displaying month, total available funds, and percentage of allocation <a class="yt-timestamp" data-t="23:38:00">[23:38:00]</a>.