---
title: Creating a Minimalistic Budget Planner Using Notion
videoId: C9gr5yS8EPc
---

From: [[theaccountantguy]] <br/> 

This guide demonstrates how to create a [[building_a_minimalistic_finance_template_in_notion | minimalistic budget planner using Notion]] to track income and expenses efficiently <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>. This [[using_notion_templates_for_budget_management | template]] can be used as a [[setting_up_a_personal_finance_tracker_using_notion | personal finance tracker]] <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>.

The [[overview_of_notion_budget_tracker_template | budget tracker]] allows you to:
*   Keep track of your [[using_notion_for_financial_summary_and_budget_management | income and expenses]] in one central location <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>.
*   Fix your [[customizing_and_setting_budgets_in_notion | monthly income goals]] to assess overall performance <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>.
*   Categorize expenses to identify areas for improvement <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.
*   Set and monitor [[customizing_and_setting_budgets_in_notion | monthly budgets]] for different categories <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.
*   Access your [[overview_of_notion_budget_tracker_template | budget tracker]] from any device, anywhere <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.

You can obtain this [[using_notion_templates_for_budget_management | template]] by visiting the online store: theaccountantguy.gumroad.com <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.

## Dashboard Segments <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>

The [[using_notion_for_financial_summary_and_budget_management | dashboard]] is composed of three main segments:
1.  **Summary Segment:** Provides an overall view of [[using_notion_for_financial_summary_and_budget_management | income and expenses]] and allocation of funds <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>. This includes a [[using_notion_for_financial_summary_and_budget_management | financial summary]] of income, expenses, fund allocation, and quarterly allocation of funds <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.
2.  **Income Details:** Displays details of actual versus estimated income, quarterly income overview, and frequency of income <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.
3.  **Expense Details:** Shows details of actual versus budgeted expenses, quarterly expense overview, and types of expenses <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>.

## Setting Up the Budget Tracker <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>

To use this [[using_notion_templates_for_budget_management | template]], you need a Notion account <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>. The setup involves three simple steps <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>:

1.  Filling out the income details for each month <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.
2.  Filling out the expense details for each individual month <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.
3.  Allocating available funds (income minus expenses) for each month onto different allocations <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.

### Step 1: Filling Up Income Details <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>

First, create an inline database by typing `/database` and selecting "Database - Inline" <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>. This database is named "Expected Income Source details" <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.

#### Income Database Columns <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>

*   **Income Details:** This is the default title property, detailing each individual income earned <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
*   **Source of Income:** A relation property linked to another database (Income Type Database), categorizing income (e.g., salary, side hustle, other) <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>, <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>.
*   **Month of Income:** A relation property linked to another database (Month of Income Database), specifying the month income is earned <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>, <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.
*   **Frequency of Income:** A relation property linked to another database (Frequency of Income Database), indicating how frequently income is earned (e.g., recurring, one-time) <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>, <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.
*   **Expected Income:** A number property (e.g., US Dollars) for the anticipated income <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>, <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>.
*   **Actual Income:** A number property (e.g., US Dollars) for the income actually earned <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>, <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>.
*   **Difference:** A formula type property calculating `Actual Income - Expected Income` <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>, <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.

#### Analyzing Income Details with Linked Databases <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>

To get detailed analyses for "Actual vs. Estimated Income", "Quarterly Income Overview", and "Frequency of Income", Notion uses relation and roll-up properties with separate databases <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>.

*   **Actual vs. Estimated Income:**
    *   This section links to the "Income Type Database" <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>.
    *   It displays total actual income, total budgeted income, their difference, and percentage change for each income type (salary, side hustle, others) <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>.
    *   A roll-up property pulls the `Actual Income` and `Expected Income` values from the original database and calculates their sum <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>, <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>.
    *   The "Income Variance Distribution" database is linked to display these results <a class="yt-timestamp" data-t="00:15:24">[00:15:24]</a>.

*   **Quarterly Income Overview:**
    *   This section links to the "Month of Income Database" <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>, <a class="yt-timestamp" data-t="00:15:40">[00:15:40]</a>.
    *   It calculates expected income, actual income, and the proportion of actual income to budgeted income for each month <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a>.
    *   A roll-up property pulls `Expected Income` and `Actual Income` values, summing them up <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>.
    *   The percentage of budgeted income is calculated with the formula `Total Actual Income / Total Expected Income` <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>.
    *   The dashboard view is set to "Gallery mode" and filtered by quarters (Q1: Jan-Mar, Q2: Apr-Jun, etc.) <a class="yt-timestamp" data-t="00:15:42">[00:15:42]</a>. Only actual income and proportion of actual income to budgeted income are visible <a class="yt-timestamp" data-t="00:16:02">[00:16:02]</a>.

*   **Frequency of Income:**
    *   This section links to the "Frequency of Income Database" <a class="yt-timestamp" data-t="00:11:35">[00:11:35]</a>, <a class="yt-timestamp" data-t="00:16:15">[00:16:15]</a>.
    *   It calculates total actual income and total expected income for recurring and one-time income types <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>.
    *   Roll-up properties are used to sum `Expected Income` and `Actual Income` from the original database <a class="yt-timestamp" data-t="00:11:56">[00:11:56]</a>.
    *   The proportion of each form of income to the total income is calculated using a formula: `Total Income of each mode / Total Actual Income` <a class="yt-timestamp" data-t="00:12:37">[00:12:37]</a>.
    *   The dashboard view is set to "List mode" and displays actual income, total income, and percentage <a class="yt-timestamp" data-t="00:16:17">[00:16:17]</a>.

### Step 2: Filling Up Expense Details <a class="yt-timestamp" data-t="00:17:14">[00:17:14]</a>

This step involves a single database for tracking expenses <a class="yt-timestamp" data-t="00:17:17">[00:17:17]</a>.

#### Expense Database Columns <a class="yt-timestamp" data-t="00:17:19">[00:17:19]</a>

*   **Expense Source:** Specifies the details of the incurred expense <a class="yt-timestamp" data-t="00:17:19">[00:17:19]</a>.
*   **Month of Expense:** A relation property linked to another database, similar to income details <a class="yt-timestamp" data-t="00:17:26">[00:17:26]</a>.
*   **Expense Classification:** A relation property linked to another database, segregating expenses into categories like utility/bills, loans/debts, food/groceries, entertainment, travel/transportation <a class="yt-timestamp" data-t="00:17:36">[00:17:36]</a>.
*   **Expense Type:** A relation property linked to the "Type of Expense Database", categorizing expenses as variable or fixed <a class="yt-timestamp" data-t="00:17:56">[00:17:56]</a>.
*   **Budgeted Expense:** A number property (e.g., US Dollars) for the expected expense <a class="yt-timestamp" data-t="00:18:06">[00:18:06]</a>.
*   **Actual Expense:** A number property (e.g., US Dollars) for the actual incurred expense <a class="yt-timestamp" data-t="00:18:15">[00:18:15]</a>.
*   **Difference:** Calculates `Actual Expense - Budgeted Expense`. A positive difference means actual expense was less than budgeted, while negative means it was more <a class="yt-timestamp" data-t="00:18:23">[00:18:23]</a>.

#### Analyzing Expense Details with Linked Databases <a class="yt-timestamp" data-t="00:18:44">[00:18:44]</a>

Similar to income, expense details use linked databases and roll-up properties for analysis.

*   **Actual vs. Budgeted Expense:**
    *   This section links to the "Expense Variance Analysis" database <a class="yt-timestamp" data-t="00:18:51">[00:18:51]</a>.
    *   It provides total budgeted expense, total actual expense, their difference, and percentage change <a class="yt-timestamp" data-t="00:19:04">[00:19:04]</a>.
    *   The database is set to "Gallery mode" with specific properties visible <a class="yt-timestamp" data-t="00:19:11">[00:19:11]</a>.

*   **Quarterly Expense Overview:**
    *   Links to the "Month of Expense Database" <a class="yt-timestamp" data-t="00:19:24">[00:19:24]</a>.
    *   Shows actual expense and the proportion of actual expense to budgeted expense for each month <a class="yt-timestamp" data-t="00:19:28">[00:19:28]</a>.
    *   Displayed in "Gallery mode" with month, actual expense, and proportion of actual to budgeted expense visible <a class="yt-timestamp" data-t="00:19:34">[00:19:34]</a>.

*   **Type of Expenses:**
    *   Links to the "Type of Expense Database" <a class="yt-timestamp" data-t="00:19:57">[00:19:57]</a>.
    *   Segregates expenses into variable and fixed, showing total actual expenses for each type and their proportion to total expenses <a class="yt-timestamp" data-t="00:16:59">[00:16:59]</a>.
    *   Displayed in "List mode" with specific properties visible <a class="yt-timestamp" data-t="00:19:57">[00:19:57]</a>.

### Step 3: Fund Allocation <a class="yt-timestamp" data-t="00:20:08">[00:20:08]</a>

After completing income and expense details, the final step is to allocate available funds <a class="yt-timestamp" data-t="00:21:19">[00:21:19]</a>.

#### Fund Allocation Database Columns <a class="yt-timestamp" data-t="00:21:28">[00:21:28]</a>

*   **Total Available Funds:** Calculated using the formula `Total Income - Total Expenses` for each month <a class="yt-timestamp" data-t="00:21:31">[00:21:31]</a>, <a class="yt-timestamp" data-t="00:21:41">[00:21:41]</a>.
    *   `Total Actual Income` is drawn using a roll-up property from the "Month of Income" database <a class="yt-timestamp" data-t="00:22:53">[00:22:53]</a>.
    *   `Actual Expense` is drawn using a roll-up property from the "Month of Expense" database <a class="yt-timestamp" data-t="00:23:06">[00:23:06]</a>.
*   **Investments:** A number property (e.g., US Dollars) for allocated investment funds <a class="yt-timestamp" data-t="00:20:39">[00:20:39]</a>, <a class="yt-timestamp" data-t="00:22:09">[00:22:09]</a>.
*   **Savings:** A number property (e.g., US Dollars) for allocated savings <a class="yt-timestamp" data-t="00:20:42">[00:20:42]</a>, <a class="yt-timestamp" data-t="00:22:11">[00:22:11]</a>.
*   **Others:** A number property (e.g., US Dollars) for other allocations <a class="yt-timestamp" data-t="00:20:46">[00:20:46]</a>, <a class="yt-timestamp" data-t="00:22:13">[00:22:13]</a>.
*   **Total Allocation:** A formula property that sums `Investments + Savings + Other Allocations` <a class="yt-timestamp" data-t="00:22:00">[00:22:00]</a>, <a class="yt-timestamp" data-t="00:22:15">[00:22:15]</a>.
*   **Percentage of Allocation:** A formula property calculating `Total Allocation / Total Available Funds`, formatted as a percentage with a bar representation <a class="yt-timestamp" data-t="00:22:26">[00:22:26]</a>, <a class="yt-timestamp" data-t="00:22:37">[00:22:37]</a>.

#### Analyzing Fund Allocation with Linked Databases <a class="yt-timestamp" data-t="00:20:08">[00:20:08]</a>

The [[using_notion_for_financial_summary_and_budget_management | dashboard]] displays two main overviews for fund allocation:

*   **Fund Allocation Overview:**
    *   Links to the "Allocation of Funds" database <a class="yt-timestamp" data-t="00:23:22">[00:23:22]</a>.
    *   Provides an analysis of remaining funds allocated to investment, savings, and other sections <a class="yt-timestamp" data-t="00:20:29">[00:20:29]</a>.
    *   Shows the total allocation amount and the proportion of allocation to total available funds <a class="yt-timestamp" data-t="00:20:51">[00:20:51]</a>.
    *   Displayed in "Gallery mode" showing "Investment Source", "Allocation Amount", and "Percentage of Allocation" <a class="yt-timestamp" data-t="00:23:25">[00:23:25]</a>.

*   **Quarterly Allocation Overview:**
    *   Links to the "Available Funds" database <a class="yt-timestamp" data-t="00:23:38">[00:23:38]</a>.
    *   Provides a monthly allocation overview showing total available funds for each month and the proportion of funds allocated for each month, broken down by quarters <a class="yt-timestamp" data-t="00:20:59">[00:20:59]</a>.
    *   Displayed in "Gallery mode" with "Month", "Total Available Funds", and "Percentage of Allocation" visible <a class="yt-timestamp" data-t="00:23:41">[00:23:41]</a>.

This detailed setup creates a comprehensive and [[building_a_minimalistic_finance_template_in_notion | minimalistic budget planner]] within Notion, allowing for a thorough [[setting_up_a_personal_finance_tracker_in_notion | personal finance tracker]] and [[monthly_budget_planner_setup_using_notion | monthly budget planner setup]] <a class="yt-timestamp" data-t="00:24:00">[00:24:00]</a>.