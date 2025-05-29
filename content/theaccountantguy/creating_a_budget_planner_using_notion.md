---
title: Creating a budget planner using Notion
videoId: C9gr5yS8EPc
---

From: [[theaccountantguy]] <br/> 

This guide details how to create a minimalistic budget planner using Notion to track income, expenses, and allocate funds in a central location <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. This dashboard allows users to fix monthly income goals, categorize expenses, and set and monitor monthly budgets for different categories <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>. The template is accessible from any device <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.

To begin, a Notion account is required <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>.

## [[notion_budget_planner_overview | Budget Planner Overview]]

The dashboard is composed of three main segments <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>:

*   **Summary Segment:** Provides an overall view of income, expenses, and fund allocation <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>, including quarterly allocation of funds <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.
*   **Income Details:** Shows actual versus estimated income, quarterly income overview, and income frequency <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.
*   **Expense Details:** Displays actual versus budgeted expenses, quarterly expense overview, and types of expenses <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>.

## [[setting_and_managing_budgets_in_notion | Setting Up the Budget Planner]]

Setting up the budget planner involves three steps <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>:

1.  Filling out income details for each month <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.
2.  Filling out expense details for each month <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.
3.  Allocating available funds (income minus expenses) to different categories for each month <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.

### Step 1: Filling Income Details

To track income, an inline database is created <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>. This database is named "expected income Source details" <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>.

The income details database includes the following columns and properties <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>:

*   **Income Details:** A title type property <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>, specifying individual income entries <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>.
*   **Source of Income:** A relation property linked to an "income type" database, categorizing income (e.g., salary, side hustle, other sources) <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>. This helps in specifying and analyzing different income sources <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.
*   **Month of Income:** A relation property linked to a "month of income" database, specifying the month when income is earned <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.
*   **Frequency of Income:** A relation property linked to a "frequency of income" database, indicating how frequently income is earned (e.g., recurring, one-time) <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.
*   **Expected Income:** A number property (e.g., US dollars) for anticipated monthly income <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.
*   **Actual Income:** A number property (e.g., US dollars) for the income earned at the end of the month <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>.
*   **Difference:** A formula type property calculating `Actual Income - Expected Income` <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>.

#### Analyzing Income Details with Linked Databases

To analyze income by source, month, or frequency, Notion's relation and roll-up properties are used with separate databases <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>.

*   **Actual vs. Estimated Income:**
    *   A linked database (e.g., "income type" database) is used to calculate the total actual and expected income for each source (salary, side hustle, others) <a class="yt-timestamp" data-t="00:08:07">[00:08:07]</a>.
    *   Roll-up properties sum the `Actual Income` and `Expected Income` from the primary income database based on their relation <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>.
    *   Formulas calculate the difference and percentage change between actual and expected income <a class="yt-timestamp" data-t="00:13:49">[00:13:49]</a>.

*   **Quarterly Income Overview:**
    *   A "month of income" database is linked to the primary income database <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>.
    *   Roll-up properties calculate the total expected and actual income for each month <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>.
    *   A formula calculates the percentage of actual income to budgeted income (`Total Actual Income / Total Expected Income`) <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>. This can be represented by a bar <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a>.
    *   In the main dashboard, this data is displayed in a gallery view, filtered by quarters (e.g., Q1 for Jan, Feb, Mar) <a class="yt-timestamp" data-t="00:15:40">[00:15:40]</a>.

*   **Frequency of Income:**
    *   A "frequency of income" database is linked to analyze total actual and expected income for recurring or one-time sources <a class="yt-timestamp" data-t="00:11:35">[00:11:35]</a>.
    *   Roll-up properties sum the actual and expected income values from the primary database based on frequency <a class="yt-timestamp" data-t="00:11:56">[00:11:56]</a>.
    *   A formula calculates the proportion of each income frequency type to the total income (`Total Income of each mode / Total Actual Income`) <a class="yt-timestamp" data-t="00:12:37">[00:12:37]</a>.
    *   In the main dashboard, this is shown in a list view <a class="yt-timestamp" data-t="00:16:13">[00:16:13]</a>.

### Step 2: Filling Expense Details

This step involves tracking all expenses in a dedicated database <a class="yt-timestamp" data-t="00:17:14">[00:17:14]</a>.

The expense details database includes the following columns <a class="yt-timestamp" data-t="00:17:19">[00:17:19]</a>:

*   **Expense Source:** Specifies the expense details <a class="yt-timestamp" data-t="00:17:21">[00:17:21]</a>.
*   **Month of Expense:** A relation property linked to another database, similar to income details <a class="yt-timestamp" data-t="00:17:26">[00:17:26]</a>.
*   **Expense Classification:** A relation property linked to another database, segregating expenses into categories like utilities, loans, food, entertainment, travel <a class="yt-timestamp" data-t="00:17:36">[00:17:36]</a>.
*   **Expense Type:** A relation property linked to a "type of expense" database, categorizing expenses as variable or fixed <a class="yt-timestamp" data-t="00:17:56">[00:17:56]</a>.
*   **Budgeted Expense:** A number property (e.g., US dollars) for the expected monthly expense <a class="yt-timestamp" data-t="00:18:06">[00:18:06]</a>.
*   **Actual Expense:** A number property (e.g., US dollars) for the actual monthly expense incurred <a class="yt-timestamp" data-t="00:18:15">[00:18:15]</a>.
*   **Difference:** Calculates the difference between budgeted and actual expenses. A positive difference means actual was less than budgeted, while negative means actual was more <a class="yt-timestamp" data-t="00:18:23">[00:18:23]</a>.

#### Analyzing Expense Details with Linked Databases

Similar to income, relation and roll-up properties are used to analyze expenses:

*   **Actual vs. Budgeted Expense:**
    *   Linked to an "expense variance analysis" database <a class="yt-timestamp" data-t="00:18:51">[00:18:51]</a>.
    *   Calculates total budgeted expense, total actual expense, difference, and percentage change <a class="yt-timestamp" data-t="00:19:04">[00:19:04]</a>.
    *   Displayed in a gallery view <a class="yt-timestamp" data-t="00:19:11">[00:19:11]</a>.

*   **Quarterly Expense Overview:**
    *   Linked to a "month of expense" database <a class="yt-timestamp" data-t="00:19:36">[00:19:36]</a>.
    *   Shows actual expense incurred and the proportion of actual expense to budgeted expense for each month <a class="yt-timestamp" data-t="00:19:26">[00:19:26]</a>.
    *   Presented in a gallery view <a class="yt-timestamp" data-t="00:19:34">[00:19:34]</a>.

*   **Type of Expenses:**
    *   Linked to a "type of expense" database <a class="yt-timestamp" data-t="00:20:00">[00:20:00]</a>.
    *   Segregates expenses into variable and fixed, showing total actual expenses for each type and their proportion to total expense <a class="yt-timestamp" data-t="00:19:48">[00:19:48]</a>.
    *   Displayed in a list view <a class="yt-timestamp" data-t="00:19:57">[00:19:57]</a>.

### Step 3: Allocating Available Funds

This step focuses on allocating the remaining funds after expenses <a class="yt-timestamp" data-t="00:21:25">[00:21:25]</a>.

*   **Calculating Available Funds:**
    *   A formula calculates `Total Income - Total Expenses` to determine available funds for each month <a class="yt-timestamp" data-t="00:21:31">[00:21:31]</a>.

*   **Allocating Funds to Heads:**
    *   Available funds are allocated to different categories like investment, savings, and others <a class="yt-timestamp" data-t="00:21:49">[00:21:49]</a>.
    *   These allocations are number properties (e.g., US dollars) <a class="yt-timestamp" data-t="00:22:09">[00:22:09]</a>.
    *   **Total Allocation:** A formula sums `Investments + Savings + Other Allocations` <a class="yt-timestamp" data-t="00:22:15">[00:22:15]</a>.
    *   **Percentage of Allocation:** A formula calculates `Total Allocation / Total Available Funds`, converted to a percentage and represented by a bar <a class="yt-timestamp" data-t="00:22:26">[00:22:26]</a>.

#### Fund Allocation Overview

The dashboard includes two key overviews for fund allocation <a class="yt-timestamp" data-t="00:20:27">[00:20:27]</a>:

*   **Fund Allocation Overview:** Provides an analysis of remaining funds allocated to investment, savings, and other sections <a class="yt-timestamp" data-t="00:20:29">[00:20:29]</a>. It shows the total allocation amount and the proportion of allocation to total available funds <a class="yt-timestamp" data-t="00:20:51">[00:20:51]</a>. Each individual allocation is linked to an "allocation of funds" database <a class="yt-timestamp" data-t="00:23:14">[00:23:14]</a>.

*   **Quarterly Allocation Overview:** Offers a monthly allocation overview, detailing total available funds for each month and the proportion of funds allocated <a class="yt-timestamp" data-t="00:20:59">[00:20:59]</a>. This is presented for each quarter of the year <a class="yt-timestamp" data-t="00:21:10">[00:21:10]</a>. It is linked to an "available funds" database <a class="yt-timestamp" data-t="00:23:38">[00:23:38]</a>.

### Linking Databases for Dashboard Display

To bring all the detailed analyses into the primary dashboard, linked databases are utilized <a class="yt-timestamp" data-t="00:15:02">[00:15:02]</a>. By typing `/link database` in Notion, users can select and link the various databases created (e.g., income variance distribution, month of income, frequency of income, expense variance analysis, available funds) to display the summarized information <a class="yt-timestamp" data-t="00:15:05">[00:15:05]</a>.

This comprehensive approach allows for detailed [[budgeting_and_tracking_expenses_in_notion | budgeting and tracking expenses in Notion]] and [[managing_finances_using_notion | managing finances using Notion]]. For those looking to [[customizing_budget_templates_in_notion | customize budget templates in Notion]] or get a ready-made solution, the template can be purchased online <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.