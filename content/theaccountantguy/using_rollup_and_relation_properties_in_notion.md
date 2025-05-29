---
title: Using Rollup and Relation Properties in Notion
videoId: C9gr5yS8EPc
---

From: [[theaccountantguy]] <br/> 

This article details how to create a minimalistic budget planner in Notion by effectively utilizing [[managing_relational_properties_in_notion_databases | relation]] and [[using_rollup_and_formula_properties | rollup properties]], as well as [[using_formulas_in_notion | formulas]] to track income, expenses, and fund allocation in one central location <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.

## Budget Planner Overview
The budget planner dashboard comprises three main segments:
*   **Summary Segment** Provides an overall view of income, expenses, and allocation of funds <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.
*   **Income Details** Shows actual versus estimated income, quarterly income overview, and frequency of income <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.
*   **Expense Details** Presents actual versus budgeted expenses, quarterly expense overview, and type of expenses <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>.

To use this template, a Notion account is required <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>.

## Setting Up the Budget Tracker
The setup involves three steps:
1.  Filling out income details <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.
2.  Filling out expense details <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.
3.  Allocating available funds (income minus expenses) <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.

## Step 1: Filling Out Income Details
Begin by creating an inline database in Notion by typing `/database` and selecting `database inline` <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>.
The database can be named "Expected Income Source Details" <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.

### Income Details Database Columns
The income details database includes the following columns:
*   **Income Details:** This is the default title property, detailing each individual income earned in a specific month <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
*   **Source of Income:** A [[managing_relational_properties_in_notion_databases | relation property]] linking to another database, categorizing income (e.g., salary, side hustle, other) <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a><a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>.
*   **Month of Income:** A [[managing_relational_properties_in_notion_databases | relation property]] linking to another database to specify the month income is earned <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.
*   **Frequency of Income:** A [[managing_relational_properties_in_notion_databases | relation property]] indicating how often income is earned (e.g., recurring, one-time) <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.
*   **Expected Income:** A [[creating_number_properties_in_notion | number property]] set to US dollars to specify expected monthly income <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a><a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>.
*   **Actual Income:** A [[creating_number_properties_in_notion | number property]] set to US dollars to record actual income earned <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a><a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.
*   **Difference:** A [[using_rollup_and_formula_properties | formula type property]] calculating the difference between actual and expected income <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.

### Analyzing Income Details with Relation and Rollup Properties
To gain deeper insights from the income data, [[tracking_relationships_using_notion | relationships]] are established with other databases, and [[using_rollup_and_formula_properties | rollup properties]] are used to aggregate information <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>.

#### Actual vs. Estimated Income (by Source)
To calculate total actual or expected income for specific sources (e.g., salary, side hustle), a [[managing_relational_properties_in_notion_databases | relation property]] links the main database to an "Income Type" database <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>.
Once databases are linked both ways <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>, [[using_rollup_and_formula_properties | rollup properties]] are used:
*   Specify the relation column <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>.
*   Pull the desired property (e.g., `actual income` or `expected income`) from the original database <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>.
*   Use the "Sum" function in the calculate section to total the values <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>.
*   [[using_formulas_in_notion | Formulas]] are used to calculate the difference and percentage change between actual and estimated totals <a class="yt-timestamp" data-t="00:13:49">[00:13:49]</a>.

#### Quarterly Income Overview (by Month)
For monthly income analysis, a [[managing_relational_properties_in_notion_databases | relationship]] is established with a "Month of Income" database <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>.
[[using_rollup_and_formula_properties | Rollup properties]] then fetch and sum expected and actual income for each month <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>.
A [[using_formulas_in_notion | formula]] is used to calculate the percentage of budgeted income (`total actual income / total expected income`), which can be displayed as a percentage or a bar <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>.

#### Frequency of Income
To analyze income by frequency (recurring vs. one-time), a [[managing_relational_properties_in_notion_databases | relationship]] is set up with a "Frequency of Income" database <a class="yt-timestamp" data-t="00:11:35">[00:11:35]</a>.
[[using_rollup_and_formula_properties | Rollup properties]] are employed to find the total actual and expected income for each frequency type <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>.
A [[using_formulas_in_notion | formula]] calculates the proportion of each income form to the total income <a class="yt-timestamp" data-t="00:12:37">[00:12:37]</a>.

### Creating Linked Databases on the Dashboard
To display these summaries on the main dashboard, use the `/link database` command <a class="yt-timestamp" data-t="00:15:02">[00:15:02]</a>.
*   **Actual vs. Estimated Income:** Link to the "Income Variance Distribution" database <a class="yt-timestamp" data-t="00:15:22">[00:15:22]</a>.
*   **Quarterly Income Overview:** Link to the "Month of Income" database, set to gallery view, and filtered by quarter (e.g., Q1 for Jan, Feb, Mar) <a class="yt-timestamp" data-t="00:15:38">[00:15:38]</a>. Display actual income and proportion to budgeted income <a class="yt-timestamp" data-t="00:16:02">[00:16:02]</a>.
*   **Frequency of Income:** Link to the "Frequency of Income" database, set to list view, displaying actual income, total income, and percentage <a class="yt-timestamp" data-t="00:16:13">[00:16:13]</a>.

## Step 2: Filling Out Expense Details
Similar to income, create an expense database. This section calculates total budgeted expense, actual expense, difference, and percentage change <a class="yt-timestamp" data-t="00:16:45">[00:16:45]</a>.

### Expense Details Database Columns
*   **Expense Source:** Specifies what the expense was incurred on <a class="yt-timestamp" data-t="00:17:19">[00:17:19]</a>.
*   **Month of Expense:** A [[managing_relational_properties_in_notion_databases | relation property]] linked to a "Month of Expense" database <a class="yt-timestamp" data-t="00:17:26">[00:17:26]</a>.
*   **Expense Classification:** A [[managing_relational_properties_in_notion_databases | relation property]] linking to another database, segregating expenses into six categories (e.g., utility, loans, food) <a class="yt-timestamp" data-t="00:17:36">[00:17:36]</a>. This helps in [[organizing_property_classification_in_notion | organizing property classification]].
*   **Expense Type:** A [[managing_relational_properties_in_notion_databases | relation property]] linked to an "Expense Type" database, classifying expenses as variable or fixed <a class="yt-timestamp" data-t="00:17:56">[00:17:56]</a>.
*   **Budgeted Expense:** A [[creating_number_properties_in_notion | number property]] in US dollars for expected expenses <a class="yt-timestamp" data-t="00:18:06">[00:18:06]</a>.
*   **Actual Expense:** A [[creating_number_properties_in_notion | number property]] in US dollars for actual expenses <a class="yt-timestamp" data-t="00:18:15">[00:18:15]</a>.
*   **Difference:** A [[using_rollup_and_formula_properties | formula]] calculating the difference between actual and budgeted expenses <a class="yt-timestamp" data-t="00:18:23">[00:18:23]</a>.

### Analyzing Expense Details with Relation and Rollup Properties
Similar to income, [[tracking_relationships_using_notion | relationships]] and [[using_rollup_and_formula_properties | rollup properties]] are used for expense analysis.

#### Actual vs. Budgeted Expense
This section is linked to an "Expense Variance Analysis" database, providing total budgeted expense, actual expense, difference, and percentage change <a class="yt-timestamp" data-t="00:18:51">[00:18:51]</a>. It's often displayed in a gallery view <a class="yt-timestamp" data-t="00:19:11">[00:19:11]</a>.

#### Quarterly Expense Overview
Linked to the "Month of Expense" database, this overview shows actual expense incurred and its proportion to budgeted expense for each month, typically in a gallery view <a class="yt-timestamp" data-t="00:19:24">[00:19:24]</a>.

#### Type of Expenses
This section categorizes expenses as variable or fixed. It's linked to the "Type of Expense" database and displays actual expenses and their percentage of total expenses in a list view <a class="yt-timestamp" data-t="00:19:45">[00:19:45]</a>.

## Step 3: Allocation of Available Funds
After calculating income and expenses, the next step is to allocate the remaining funds (income minus expenses) <a class="yt-timestamp" data-t="00:21:19">[00:21:19]</a>.

### Available Funds Calculation
A [[using_formulas_in_notion | formula]] is used to determine `total available funds = total income - total expenses` for each month <a class="yt-timestamp" data-t="00:21:28">[00:21:28]</a>.
The total actual income is pulled from the "Month of Income" database using a [[using_rollup_and_formula_properties | rollup property]] set to "Sum" <a class="yt-timestamp" data-t="00:22:53">[00:22:53]</a>. Similarly, actual expenses are pulled from the "Month of Expense" database <a class="yt-timestamp" data-t="00:23:06">[00:23:06]</a>.

### Fund Allocation to Different Heads
Available funds are then allocated to categories like investments, savings, and others <a class="yt-timestamp" data-t="00:21:48">[00:21:48]</a>.
*   **Investment, Savings, Others:** These are [[creating_number_properties_in_notion | number properties]] set to US dollars <a class="yt-timestamp" data-t="00:22:09">[00:22:09]</a>.
*   **Total Allocation:** A [[using_formulas_in_notion | formula]] calculates the sum of investment, savings, and other allocations <a class="yt-timestamp" data-t="00:22:15">[00:22:15]</a>.
*   **Percentage of Allocation:** A [[using_formulas_in_notion | formula]] (`total allocation / total available funds`) calculates the percentage, which can be represented by a bar <a class="yt-timestamp" data-t="00:22:26">[00:22:26]</a>.

### Fund Allocation Overview
*   **Fund Allocation Overview:** This section is linked to the "Allocation of Funds" database, showing investment source, allocation amount, and percentage of allocation for each month, typically in a gallery layout <a class="yt-timestamp" data-t="00:23:14">[00:23:14]</a>.
*   **Quarterly Allocation Overview:** Linked to the "Available Funds" database, this displays monthly total available funds and their percentage of allocation in a gallery mode, organized by quarters <a class="yt-timestamp" data-t="00:23:38">[00:23:38]</a>.

By following these steps, a comprehensive Notion budget tracker can be established using [[managing_relational_properties_in_notion_databases | relation]] and [[using_rollup_and_formula_properties | rollup properties]] to [[calculating_custom_data_summaries_in_notion | calculate custom data summaries]] and track financial performance.