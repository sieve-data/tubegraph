---
title: Setting and monitoring monthly budgets
videoId: C9gr5yS8EPc
---

From: [[theaccountantguy]] <br/> 

This article outlines how to create a minimalistic budget planner using Notion to [[budgeting_and_expense_tracking | keep track of income and expenses]] in one central location <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.

## Key Features and Benefits
This Notion-based budget planner allows users to:
*   Fix monthly income goals to assess overall performance <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>.
*   Categorize expenses to identify areas for improvement <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.
*   [[setting_budgeted_amounts_for_expenses | Set and monitor monthly budgets]] for different categories <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.
*   Gain access to their budget tracker from any device, anywhere <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.

The template for this planner can be obtained by visiting accountantguy.gumroad.com <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>. To use the template, users need to sign up for a Notion account <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>.

## Dashboard Structure
The dashboard consists of three main segments <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>:

1.  **Summary Segment** <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>: Provides an overall view of income, expenses, and allocation of funds <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>. It includes summaries of income, expenses, fund allocation, and quarterly allocation of funds <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.
2.  **Income Details** <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>: Presents details of actual versus estimated income expectations, quarterly income overview, and frequency of income <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.
3.  **Expense Details** <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>: Shows details of actual versus budgeted expenses, quarterly expense overview, and type of expenses <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.

## Setting Up the Budget Tracker
[[notion_monthly_budget_planner_setup | Setting up this budget tracker]] involves three simple steps <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>:

1.  Filling out the income details for each month <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.
2.  Filling out the expense details for each individual month <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.
3.  Allocating available funds (income minus expenses) for each individual month onto different allocations <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.

### Step 1: Filling Out Income Details
The income details are captured in an inline database <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>, created by typing `/database` and selecting `database inline` <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.

The inline database for income details includes the following columns/properties:
*   **Income Details**: A title-type property specifying each individual income earned in a particular month <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
*   **Source of Income**: A relation property linked to another database, categorizing income (e.g., salary, side hustle, other) <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.
*   **Month of Income**: A relation property linked to another database, specifying the month income is earned <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.
*   **Frequency of Income**: A relation property linked to another database, indicating how frequently income is earned (e.g., recurring, one-time) <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.
*   **Expected Income**: A number property, formatted as currency (e.g., US dollars), representing the anticipated income for the month <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.
*   **Actual Income**: A number property, formatted as currency, indicating the income earned at the end of the month <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>.
*   **Difference**: A formula-type property calculating the difference between actual and expected income <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>.

#### Income Analysis Using Relations and Roll-ups
The income details section provides sub-sections for analysis:
*   **Actual Versus Estimated Income**: Shows total actual income, total estimated income, their difference, and percentage change for each income type <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>. This is achieved by linking the main income database with an "Income Type" database using a relation property, and then using roll-up properties to sum actual and expected income for each category <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>.
*   **Quarterly Income Overview**: Displays total actual income and the proportion of each income to budgeted income for each month, divided into four quarters <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>. This relies on establishing a relationship with a "Month of Income" database and using roll-up properties to calculate expected and actual income per month, and a formula for percentage of budgeted income <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>.
*   **Frequency of Income**: Shows how frequently income is earned (recurring or one-time) and the total actual income and proportion for each frequency type <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>. A relation to a "Frequency of Income" database and roll-up properties are used to sum actual and expected incomes for recurring vs. one-time types <a class="yt-timestamp" data-t="00:11:35">[00:11:35]</a>.

> [!INFO] Relations and Roll-ups
> Establishing a two-way relationship between databases allows for powerful analysis. A roll-up property pulls desired information from a related database (e.g., actual income from the original database) and can then perform calculations like summing values <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>.

### Step 2: Filling Out Expense Details
Similar to income, expenses are tracked in a dedicated database <a class="yt-timestamp" data-t="00:17:14">[00:17:14]</a>.

The expense database includes:
*   **Expense Source**: Specifies the details of the incurred expense <a class="yt-timestamp" data-t="00:17:19">[00:17:19]</a>.
*   **Month of Expense**: A relation property linked to another database, indicating when the expense was incurred <a class="yt-timestamp" data-t="00:17:26">[00:17:26]</a>.
*   **Expense Classification**: A relation property linked to another database, categorizing expenses into heads like utility/bills, loans/debts, food/groceries, entertainment, travel/transportation, and others <a class="yt-timestamp" data-t="00:17:36">[00:17:36]</a>.
*   **Expense Type**: A relation property linked to a "Type of Expense" database, specifying if it's a variable or fixed expense <a class="yt-timestamp" data-t="00:17:56">[00:17:56]</a>.
*   **Budgeted Expense**: A number property, formatted as currency, representing the expected expense <a class="yt-timestamp" data-t="00:18:06">[00:18:06]</a>.
*   **Actual Expense**: A number property, formatted as currency, representing the actual expense incurred <a class="yt-timestamp" data-t="00:18:15">[00:18:15]</a>.
*   **Difference**: Calculates the difference between actual and budgeted expenses. A positive difference means actual was less than budgeted, while a negative difference means actual was more <a class="yt-timestamp" data-t="00:18:23">[00:18:23]</a>.

#### Expense Analysis and Overview
The expense details section provides sub-sections for analysis, similar to income:
*   **Actual Versus Budgeted Expense**: Shows total budgeted expense, total actual expense, their difference, and percentage change <a class="yt-timestamp" data-t="00:16:38">[00:16:38]</a>. This information is linked from an "Expense Variance Analysis" database <a class="yt-timestamp" data-t="00:18:51">[00:18:51]</a>.
*   **Quarterly Expense Overview**: Displays actual expense incurred and the proportion of actual expense to budgeted expense for each month <a class="yt-timestamp" data-t="00:19:24">[00:19:24]</a>. This is linked to the "Month of Expense" database <a class="yt-timestamp" data-t="00:19:34">[00:19:34]</a>.
*   **Type of Expenses**: Segregates expenses into variable and fixed, showing total actual expenses for each type and their proportion to total expense <a class="yt-timestamp" data-t="00:19:45">[00:19:45]</a>. This is linked to the "Type of Expense" database <a class="yt-timestamp" data-t="00:19:57">[00:19:57]</a>.

### Step 3: Allocating Available Funds
This step focuses on allocating the "available funds" (income minus expenses) <a class="yt-timestamp" data-t="00:21:25">[00:21:25]</a>. A formula is used to calculate available funds for each month <a class="yt-timestamp" data-t="00:21:41">[00:21:41]</a>.

Available funds are then allocated to different heads:
*   **Investment Section** <a class="yt-timestamp" data-t="00:20:36">[00:20:36]</a>
*   **Savings Section** <a class="yt-timestamp" data-t="00:20:37">[00:20:37]</a>
*   **Others Section** <a class="yt-timestamp" data-t="00:20:38">[00:20:38]</a>

The "Total Allocation" is the summation of investment, savings, and other allocations, represented by a formula <a class="yt-timestamp" data-t="00:21:56">[00:21:56]</a>. The "Percentage of Allocation" is calculated by dividing the total allocation by the total available funds, also using a formula and displayed as a bar <a class="yt-timestamp" data-t="00:22:26">[00:22:26]</a>.

#### Fund Allocation Overview
The dashboard features:
*   **Fund Allocation Overview**: Provides an analysis of remaining funds allocated to different heads (investment, savings, others), showing the total allocated amount and its proportion to total available funds <a class="yt-timestamp" data-t="00:20:29">[00:20:29]</a>. Each individual allocation is linked to an "Allocation of Funds" database <a class="yt-timestamp" data-t="00:23:14">[00:23:14]</a>.
*   **Quarterly Allocation Overview**: Gives a monthly allocation overview, showing total available funds for each month and the proportion of funds allocated, detailed by quarters <a class="yt-timestamp" data-t="00:20:59">[00:20:59]</a>. This is linked to an "Available Funds" database <a class="yt-timestamp" data-t="00:23:38">[00:23:38]</a>.

> [!INFO] Linking Databases for Dashboard Display
> To create linked databases on the primary dashboard, type `/link database` and select the desired database to link <a class="yt-timestamp" data-t="00:15:02">[00:15:02]</a>. This allows for displaying summarized and filtered views of the underlying data, such as setting views to "Gallery mode" or "List mode" and filtering by quarters (e.g., Q1 for Jan, Feb, Mar) <a class="yt-timestamp" data-t="00:15:40">[00:15:40]</a>.