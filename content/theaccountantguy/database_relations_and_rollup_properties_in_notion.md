---
title: Database relations and rollup properties in Notion
videoId: C9gr5yS8EPc
---

From: [[theaccountantguy]] <br/> 

This article details how to create a minimalistic budget planner in [[creating_and_managing_a_database_in_notion | Notion]] using its database features, specifically focusing on [[establishing_relationships_between_databases_in_notion | establishing relationships]] between databases and employing [[using_rollup_and_formula_properties_in_notion | rollup and formula properties]] for financial analysis and tracking. This dashboard allows users to manage income and expenses, set monthly goals, categorize spending, and monitor budgets from any device <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.

## Budget Planner Overview
The budget planner dashboard is divided into three main segments:
*   **Summary Segment**: Provides an overall view of income, expenses, and fund allocation <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>. This includes a summary of income, expenses, fund allocation, and quarterly allocation <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.
*   **Income Details**: Displays actual versus estimated income, quarterly income overview, and income frequency <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.
*   **Expense Details**: Shows actual versus budgeted expenses, quarterly expense overview, and type of expenses <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>.

To use this template, a [[creating_and_managing_a_database_in_notion | Notion]] account is required <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.

## Setting Up the Budget Tracker
The setup involves three primary steps:
1.  **Filling Income Details**: Inputting monthly income information <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.
2.  **Filling Expense Details**: Inputting individual monthly expense information <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.
3.  **Allocating Available Funds**: Distributing the remaining funds (income minus expenses) across different categories for each month <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.

### Creating an Inline Database
An inline [[creating_a_database_in_notion | database]] is the foundation for tracking. It can be created by typing `/` followed by `database` and selecting "database inline" <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>. The database title can be made visible and edited via the three dots menu in the layout options <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.

### Income Details Database Columns
The income details [[creating_a_database_in_notion | database]] includes the following columns, each with a specific [[understanding_and_setting_property_types_in_notion_databases | property type]]:
*   **Income Details**: Title property, used for each individual income <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
*   **Source of Income**: A [[establishing_relationships_between_databases_in_notion | relation property]] linked to another database, categorizing income (e.g., salary, side hustle, other sources) <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.
*   **Month of Income**: A [[establishing_relationships_between_databases_in_notion | relation property]] linked to a separate month [[creating_a_database_in_notion | database]] <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.
*   **Frequency of Income**: A [[establishing_relationships_between_databases_in_notion | relation property]] indicating how often income is earned (e.g., recurring, one-time) <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.
*   **Expected Income**: A number [[understanding_and_setting_property_types_in_notion_databases | property type]] with a currency format (e.g., US dollars) for anticipated income <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.
*   **Actual Income**: A number [[understanding_and_setting_property_types_in_notion_databases | property type]] with a currency format for actual income earned <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>.
*   **Difference**: A [[using_rollup_and_formula_properties_in_notion | formula property]] calculating the difference between actual and expected income <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>.

### Expense Details Database Columns
Similar to income, the expense [[creating_a_database_in_notion | database]] is set up with relevant columns:
*   **Expense Source**: Specifies expense details <a class="yt-timestamp" data-t="00:17:19">[00:17:19]</a>.
*   **Month of Expense**: A [[establishing_relationships_between_databases_in_notion | relation property]] linked to another [[creating_a_database_in_notion | database]] <a class="yt-timestamp" data-t="00:17:26">[00:17:26]</a>.
*   **Expense Classification**: A [[establishing_relationships_between_databases_in_notion | relation property]] segregating expenses into categories like utilities, loans, food, entertainment, and travel <a class="yt-timestamp" data-t="00:17:36">[00:17:36]</a>.
*   **Expense Type**: A [[establishing_relationships_between_databases_in_notion | relation property]] classifying expenses as variable or fixed <a class="yt-timestamp" data-t="00:17:56">[00:17:56]</a>.
*   **Budgeted Expense**: A number [[understanding_and_setting_property_types_in_notion_databases | property type]] (US dollars) for expected expenses <a class="yt-timestamp" data-t="00:18:06">[00:18:06]</a>.
*   **Actual Expense**: A number [[understanding_and_setting_property_types_in_notion_databases | property type]] (US dollars) for actual expenses <a class="yt-timestamp" data-t="00:18:15">[00:18:15]</a>.
*   **Difference**: A [[using_rollup_and_formula_properties_in_notion | formula property]] calculating the difference between actual and budgeted expenses <a class="yt-timestamp" data-t="00:18:23">[00:18:23]</a>.

## Database Relations and Rollup Properties

### Establishing Relations
[[establishing_relationships_between_databases_in_notion | Setting up a relationship]] with another [[creating_a_database_in_notion | database]] is crucial for detailed analysis <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>. For instance, the "Source of Income" column in the income [[creating_a_database_in_notion | database]] is related to an "Income Type" [[creating_a_database_in_notion | database]] <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>. This allows for calculations like total actual income for a specific source <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>. These relationships are often two-way <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>.

### Using Rollup Properties
Once [[establishing_relationships_between_databases_in_notion | databases are linked]], a [[using_rollup_and_formula_properties_in_notion | rollup property]] can be used to pull desired information from the original [[creating_a_database_in_notion | database]] and perform calculations <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>.

*   **Example 1 (Income Type Analysis)**: To calculate total actual income for a specific income head (e.g., salary), a [[using_rollup_and_formula_properties_in_notion | rollup property]] is used. It specifies the relation to the "Income Type" [[creating_a_database_in_notion | database]], pulls the "Actual Income" property, and calculates the sum <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>. This applies to both actual and budgeted income <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>.
*   **Example 2 (Monthly Income Analysis)**: To find the total actual income for a specific month (e.g., January), a [[establishing_relationships_between_databases_in_notion | relationship]] is established with a "Month of Income" [[creating_a_database_in_notion | database]]. A [[using_rollup_and_formula_properties_in_notion | rollup property]] then pulls the "Expected Income" and "Actual Income" values and sums them up for each month <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>.
*   **Example 3 (Income Frequency Analysis)**: Similarly, for "Frequency of Income," a [[establishing_relationships_between_databases_in_notion | relationship]] is set up with a "Frequency of Income" [[creating_a_database_in_notion | database]], and [[using_rollup_and_formula_properties_in_notion | rollup properties]] are used to calculate total actual and expected income for recurring or one-time income sources <a class="yt-timestamp" data-t="00:11:35">[00:11:35]</a>.

### Using Formula Properties
[[using_rollup_and_formula_properties_in_notion | Formula properties]] are used to derive new values from existing properties, often in conjunction with rollups.
*   **Difference Calculation**: The "Difference" column in both income and expense databases uses a [[using_rollup_and_formula_properties_in_notion | formula property]] to subtract expected/budgeted values from actual values <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>.
*   **Percentage Calculation**: The "Percentage of Budgeted Income" is a [[using_rollup_and_formula_properties_in_notion | formula property]] that divides total actual income by total expected income, formatted as a percentage, and can be represented by a progress bar <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>.
*   **Proportion of Income/Expense**: A [[using_rollup_and_formula_properties_in_notion | formula property]] divides the total income/expense of a specific mode by the total actual income/expense, converted to a percentage <a class="yt-timestamp" data-t="00:12:37">[00:12:37]</a>.
*   **Conditional Formulas**: An `if` formula can be used to display different rollup values based on specific conditions, such as showing total estimated income, total actual income, or difference based on a field's content <a class="yt-timestamp" data-t="00:14:49">[00:14:49]</a>.

## Displaying Data with Linked Databases
To present these analyses on the main dashboard, linked [[creating_a_database_in_notion | databases]] are used. These are created by typing `/` and selecting `link database` <a class="yt-timestamp" data-t="00:15:02">[00:15:02]</a>.
*   **Actual vs. Estimated Income**: Links to the "Income Variance Distribution" [[creating_a_database_in_notion | database]] <a class="yt-timestamp" data-t="00:15:22">[00:15:22]</a>.
*   **Quarterly Income Overview**: Links to the "Month of Income" [[creating_a_database_in_notion | database]], displayed in a gallery view, filtered by quarters (e.g., Q1 filters Jan, Feb, Mar) <a class="yt-timestamp" data-t="00:15:38">[00:15:38]</a>.
*   **Frequency of Income**: Links to the "Frequency of Income" [[creating_a_database_in_notion | database]], displayed in a list view, showing actual income, total income, and percentage <a class="yt-timestamp" data-t="00:16:13">[00:16:13]</a>.
*   **Quarterly Expense Overview**: Links to the "Month of Expense" [[creating_a_database_in_notion | database]], displayed in a gallery view <a class="yt-timestamp" data-t="00:19:24">[00:19:24]</a>.
*   **Type of Expenses**: Links to the "Type of Expense" [[creating_a_database_in_notion | database]], displayed in a list view <a class="yt-timestamp" data-t="00:19:57">[00:19:57]</a>.

These linked [[creating_a_database_in_notion | databases]] allow for dynamic and categorized views of financial data.

## Fund Allocation
The third step involves [[using_databases_in_notion_for_financial_tracking | tracking]] the allocation of available funds (income minus expenses) <a class="yt-timestamp" data-t="00:21:25">[00:21:25]</a>.
*   **Available Funds**: A [[using_rollup_and_formula_properties_in_notion | formula property]] calculating total income less total expenses for each month <a class="yt-timestamp" data-t="00:21:41">[00:21:41]</a>.
*   **Allocation Heads**: Funds are allocated to categories like investments, savings, and others, each with a number [[understanding_and_setting_property_types_in_notion_databases | property type]] <a class="yt-timestamp" data-t="00:21:49">[00:21:49]</a>.
*   **Total Allocation**: A [[using_rollup_and_formula_properties_in_notion | formula property]] summing investment, savings, and other allocations <a class="yt-timestamp" data-t="00:22:15">[00:22:15]</a>.
*   **Percentage of Allocation**: A [[using_rollup_and_formula_properties_in_notion | formula property]] dividing total allocation by total available funds, formatted as a percentage with a bar representation <a class="yt-timestamp" data-t="00:22:26">[00:22:26]</a>.

This [[using_databases_in_notion_for_financial_tracking | financial tracking]] setup leverages the power of Notion's [[establishing_relationships_between_databases_in_notion | relational databases]] and [[using_rollup_and_formula_properties_in_notion | rollup and formula properties]] to create a comprehensive and dynamic budget planner.