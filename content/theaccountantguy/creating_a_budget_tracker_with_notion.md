---
title: Creating a budget tracker with Notion
videoId: C9gr5yS8EPc
---

From: [[theaccountantguy]] <br/> 

This article describes how to [[creating_a_monthly_budget_planner_in_notion | create a minimalistic budget planner]] using Notion to [[tracking_personal_finances_using_notion | track personal finances]] <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. This dashboard allows users to [[tracking_personal_finances_in_notion | track income and expenses]] in one central location <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>, set monthly income goals to assess performance <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>, categorize expenses for identifying improvement areas <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>, and monitor monthly budgets for different categories <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>. The budget tracker is accessible from any device <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.

> [!info] Obtaining the Template
> A template for this Notion budget tracker can be obtained by visiting the online store at accountantguy.gumroad.com <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. To use this template, a Notion account is required <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.

## Dashboard Segments

The Notion budget planner dashboard is comprised of three main segments <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>:

1.  **Summary Segment**: Provides an overall view of income, expenses, and fund allocation <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. This includes summaries of income, expenses, fund allocation, and quarterly fund allocation <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.
2.  **Income Details**: Shows details of actual versus estimated income, quarterly income overview, and frequency of income <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.
3.  **Expense Details**: Displays actual versus budgeted expenses, quarterly expense overview, and type of expenses <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>.

## Setting Up the Budget Planner

The process of setting up this budget tracker involves three simple steps <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>:

1.  **Filling out Income Details**: Inputting income information for each month <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.
2.  **Filling out Expense Details**: Entering expense information for each individual month <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.
3.  **Allocating Available Funds**: Distributing the remaining funds (income minus expenses) for each month across different allocations <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>.

### Step 1: Filling Out Income Details

To begin, an inline database is created <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>. This can be done by typing `/database` and selecting "database inline" <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>. This database is named "Expected Income Source details" <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.

The inline database includes the following columns (properties) <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>:

*   **Income Details**: The primary title property, detailing each individual income earned in a month <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.
*   **Source of Income**: A relation property linked to another database (Income Type Database), categorizing income (e.g., salary, side hustle, other sources) <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.
*   **Month of Income**: A relation property linked to another database (Month of Income Database), specifying the month income is earned <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>.
*   **Frequency of Income**: A relation property linked to another database (Frequency of Income Database), indicating how frequently income is earned (e.g., recurring, one-time) <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.
*   **Expected Income**: A number property set to a currency format (e.g., US dollars), representing anticipated monthly income <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.
*   **Actual Income**: A number property set to a currency format (e.g., US dollars), recording the actual income earned at the end of a month <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.
*   **Difference**: A formula property that calculates the difference between `Actual Income` and `Expected Income` <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>.

#### Using Relations and Roll-ups for Income Analysis

Relations and roll-up properties are used to gather and analyze income data effectively <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a>.

*   **Actual vs. Estimated Income**:
    *   The `Source of Income` column is related to an "Income Type Database" <a class="yt-timestamp" data-t="00:08:05">[00:08:05]</a>. This database uses roll-up properties to display the total actual income, total budgeted income, their difference, and the percentage change for each income type <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>. The roll-up property pulls the `Actual Income` and `Expected Income` values from the original database and sums them <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.

*   **Quarterly Income Overview**:
    *   The `Month of Income` column is linked to a "Month of Income Database" <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>. This database uses relation and roll-up properties to calculate expected income, actual income, and the proportion of actual to budgeted income for each month <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>. The percentage of budgeted income is calculated using a formula: `Total Actual Income / Total Expected Income`, formatted as a percentage <a class="yt-timestamp" data-t="00:11:04">[00:11:04]</a>.

*   **Frequency of Income**:
    *   The `Frequency of Income` column is related to a "Frequency of Income Database" <a class="yt-timestamp" data-t="00:11:40">[00:11:40]</a>. This database utilizes relation and roll-up properties to determine the total actual income and total expected income for each income frequency (e.g., recurring, one-time) <a class="yt-timestamp" data-t="00:11:50">[00:11:50]</a>. It also calculates the proportion of each income form to the total income using a formula <a class="yt-timestamp" data-t="00:12:40">[00:12:40]</a>.

### Step 2: Filling Out Expense Details

This step focuses on [[how_to_build_an_expense_tracker_in_notion | tracking expenses]] <a class="yt-timestamp" data-t="00:17:17">[00:17:17]</a>. A single database is used for all expenses <a class="yt-timestamp" data-t="00:17:17">[00:17:17]</a>.

The expense database includes the following columns (properties) <a class="yt-timestamp" data-t="00:17:19">[00:17:19]</a>:

*   **Expense Source**: The primary title property, detailing the expenses to be incurred <a class="yt-timestamp" data-t="00:17:24">[00:17:24]</a>.
*   **Month of Expense**: A relation property linked to another database (similar to income details), specifying when an expense is incurred <a class="yt-timestamp" data-t="00:17:34">[00:17:34]</a>.
*   **Expense Classification**: A relation property linked to another database, segregating expenses into categories like utilities, loans, food, entertainment, travel, etc. <a class="yt-timestamp" data-t="00:17:47">[00:17:47]</a>.
*   **Expense Type**: A relation property linked to the "Type of Expense database", categorizing expenses as variable or fixed <a class="yt-timestamp" data-t="00:18:02">[00:18:02]</a>.
*   **Budgeted Expense**: A number property set as US dollars, representing the expected expense for a month <a class="yt-timestamp" data-t="00:18:13">[00:18:13]</a>.
*   **Actual Expense**: A number property set as US dollars, recording the actual expense for a month <a class="yt-timestamp" data-t="00:18:21">[00:18:21]</a>.
*   **Difference**: Calculates the difference between `Actual Expense` and `Budgeted Expense` <a class="yt-timestamp" data-t="00:18:27">[00:18:27]</a>. A positive difference means actual was less than budgeted; a negative difference means actual was more than budgeted <a class="yt-timestamp" data-t="00:18:36">[00:18:36]</a>.

#### Using Relations and Roll-ups for Expense Analysis

Similar to income details, relations and roll-ups are used for expense analysis:

*   **Actual vs. Budgeted Expense**:
    *   Linked to an "Expense Variance Analysis" database, which provides total budgeted expense, total actual expense, their difference, and percentage change <a class="yt-timestamp" data-t="00:19:10">[00:19:10]</a>. This database is typically displayed in a Gallery view <a class="yt-timestamp" data-t="00:19:14">[00:19:14]</a>.

*   **Quarterly Expense Overview**:
    *   Linked to the "Month of Expense" database, this overview shows actual expense incurred and the proportion of actual to budgeted expense for each month <a class="yt-timestamp" data-t="00:19:32">[00:19:32]</a>. This is typically a Gallery view <a class="yt-timestamp" data-t="00:19:36">[00:19:36]</a>.

*   **Type of Expenses**:
    *   Linked to the "Type of Expense" database, it segregates expenses into variable and fixed types, showing the total actual expenses for each type and their proportion to total expenses <a class="yt-timestamp" data-t="00:19:57">[00:19:57]</a>. This is often a List view <a class="yt-timestamp" data-t="00:20:00">[00:20:00]</a>.

### Step 3: Allocating Available Funds

This step involves [[creating_a_savings_funds_tracker_in_notion | allocating available funds]] (income minus expenses) <a class="yt-timestamp" data-t="00:21:24">[00:21:24]</a>.

1.  **Calculating Available Funds**: A formula calculates the total income less total expenses to determine the available funds for each month <a class="yt-timestamp" data-t="00:21:45">[00:21:45]</a>.
2.  **Allocating Funds**: These available funds are then allocated to different heads, such as "Investment," "Savings," and "Others" <a class="yt-timestamp" data-t="00:21:54">[00:21:54]</a>. These are number properties in US dollars <a class="yt-timestamp" data-t="00:22:13">[00:22:13]</a>.
3.  **Total Allocation**: A formula sums the amounts allocated to Investments, Savings, and Other allocations <a class="yt-timestamp" data-t="00:22:22">[00:22:22]</a>.
4.  **Percentage of Allocation**: This is calculated using a formula: `Total Allocation / Total Available Funds`, formatted as a percentage <a class="yt-timestamp" data-t="00:22:32">[00:22:32]</a>.

#### Fund Allocation Overview and Quarterly Allocation Overview

*   **Fund Allocation Overview**: This section, often in a Gallery layout, provides an analysis of remaining funds allocated to different heads like Investments, Savings, and Others <a class="yt-timestamp" data-t="00:20:38">[00:20:38]</a>. Each individual fund is calculated by being linked to its respective database ("Allocation of Funds database") <a class="yt-timestamp" data-t="00:23:20">[00:23:20]</a>.
*   **Quarterly Allocation Overview**: This provides a monthly allocation overview, detailing total available funds for each month and the proportion of funds allocated <a class="yt-timestamp" data-t="00:21:08">[00:21:08]</a>. This is linked to an "Available Funds" database and is often presented in a Gallery view <a class="yt-timestamp" data-t="00:23:44">[00:23:44]</a>.

## Linking Databases to the Main Dashboard

The primary dashboard for this [[overview_of_notion_budget_tracker_template | Notion Budget Tracker Template]] links different databases to present the actual versus estimated income, quarterly income overview, and frequency of income sections <a class="yt-timestamp" data-t="00:14:55">[00:14:55]</a>. Linked databases are created by typing `/link database` and selecting the desired database <a class="yt-timestamp" data-t="00:15:08">[00:15:08]</a>.

*   For "Actual versus Estimated Income details," the "Income Variance Distribution" database is linked <a class="yt-timestamp" data-t="00:15:29">[00:15:29]</a>.
*   For "Quarterly Income Overview," the "Month of Income" database is linked and set to a Gallery view <a class="yt-timestamp" data-t="00:15:44">[00:15:44]</a>. Filters are applied for each quarter (e.g., Q1 for Jan, Feb, March) <a class="yt-timestamp" data-t="00:15:50">[00:15:50]</a>.
*   For "Frequency of Income," the "Frequency of Income" database is linked and set to a List view <a class="yt-timestamp" data-t="00:16:19">[00:16:19]</a>.

This comprehensive setup enables [[creating_and_tracking_budgets_and_savings_in_notion | creating and tracking budgets and savings in Notion]].