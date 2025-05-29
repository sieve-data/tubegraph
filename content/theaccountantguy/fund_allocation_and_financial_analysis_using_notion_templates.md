---
title: Fund allocation and financial analysis using Notion templates
videoId: C9gr5yS8EPc
---

From: [[theaccountantguy]] <br/> 

This article details how to create a minimalistic budget planner using Notion to track income, expenses, and allocate funds, providing a comprehensive financial overview <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. This [[notion_finance_templates | Notion finance template]] allows users to keep track of financial data in one central location from any device <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.

## Key Capabilities of the Notion Budget Planner
The Notion budget planner is designed to help users:
*   Keep track of income and expenses <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>.
*   Fix monthly income goals <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>.
*   Categorize expenses to identify areas for improvement <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.
*   Set and monitor monthly budgets for different categories <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.
*   Gain access to the budget tracker from any device, anywhere <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.

## Dashboard Segments
The dashboard of this budget planner consists of three main segments <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>:
1.  **Summary Segment:** Provides an overall view of income, expenses, and allocation of funds <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>. This includes a summary of income, expenses, fund allocation, and quarterly allocation <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.
2.  **Income Details:** Shows details of actual versus estimated income, quarterly income overview, and frequency of income <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.
3.  **Expense Details:** Presents details of actual versus budgeted expenses, quarterly expense overview, and types of expenses <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>.

To utilize this template, users need a Notion account <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>.

## Setting Up the Budget Planner
[[Using Notion for Financial Tracking | Setting up this budget tracker]] involves three simple steps <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>:

### Step 1: Filling Out Income Details
The first step is to fill out the income details for each month <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.

#### Creating the Income Database
An inline database is created by typing `/` followed by `database` and selecting `database inline` <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>. This database is typically named "Expected Income Source Details" <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.

The income database includes the following columns:
*   **Income Details:** A title property describing each individual income <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
*   **Source of Income:** A relation property linked to another database, categorizing income (e.g., Salary, Side Hustle, Other Sources) <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.
*   **Month of Income:** A relation property linked to a database specifying the month income is earned <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.
*   **Frequency of Income:** A relation property specifying how frequently income is earned (e.g., recurring, one-time) <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.
*   **Expected Income:** A number property (e.g., US dollars) for the anticipated income in a month <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.
*   **Actual Income:** A number property (e.g., US dollars) for the income actually earned <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>.
*   **Difference:** A formula property calculating the difference between Actual Income and Expected Income <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>.

#### Analyzing Income Details with Linked Databases and Roll-ups
To gain deeper insights, several linked databases are used in conjunction with "relation" and "roll-up" properties <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>:

*   **Actual vs. Estimated Income:** This view shows total actual income, total estimated income, their difference, and percentage change across income sources (e.g., Salary, Side Hustle) <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>. This is achieved by linking to an "Income Type" database and using roll-up properties to sum actual and expected income from the main income database <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>.
*   **Quarterly Income Overview:** Displays total actual income and the proportion of each income to budgeted income, divided into four quarters <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>. This links to a "Month of Income" database <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>. Roll-up properties calculate expected and actual income for each month, and a formula (`total actual income / total expected income`) derives the proportion, displayed as a percentage <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a>.
*   **Frequency of Income:** Illustrates actual income for recurring or one-time income types, along with total proportion and percentage <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>. This is linked to a "Frequency of Income" database <a class="yt-timestamp" data-t="00:11:35">[00:11:35]</a>, using roll-up properties to sum expected and actual income <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>, and a formula to calculate the proportion of each income mode to the total income <a class="yt-timestamp" data-t="00:12:37">[00:12:37]</a>.

The main dashboard's income details section links these various databases using the "linked database" function <a class="yt-timestamp" data-t="00:15:02">[00:15:02]</a>.

### Step 2: Filling Out Expense Details
The second step involves filling out expense details for each individual month <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.

#### Creating the Expense Database
Similar to income, a database is created with columns for expense tracking <a class="yt-timestamp" data-t="00:17:14">[00:17:14]</a>:
*   **Expense Source:** The title property detailing what the expense is for <a class="yt-timestamp" data-t="00:17:19">[00:17:19]</a>.
*   **Month of Expense:** A relation property linked to a database specifying when the expense was incurred <a class="yt-timestamp" data-t="00:17:26">[00:17:26]</a>.
*   **Expense Classification:** A relation property categorizing expenses into heads like utility and bills, loans and debts, food and groceries, entertainment, travel, and transportation <a class="yt-timestamp" data-t="00:17:36">[00:17:36]</a>.
*   **Expense Type:** A relation property categorizing expenses as variable or fixed <a class="yt-timestamp" data-t="00:17:56">[00:17:56]</a>.
*   **Budgeted Expense:** A number property (e.g., US dollars) for the expected expense <a class="yt-timestamp" data-t="00:18:06">[00:18:06]</a>.
*   **Actual Expense:** A number property (e.g., US dollars) for the actual expense incurred <a class="yt-timestamp" data-t="00:18:15">[00:18:15]</a>.
*   **Difference:** Calculates the difference between Actual and Budgeted expense, indicating if actual spending was less (positive difference) or more (negative difference) than budgeted <a class="yt-timestamp" data-t="00:18:23">[00:18:23]</a>.

#### Analyzing Expense Details
The expense details section in the dashboard also uses linked databases to provide overviews <a class="yt-timestamp" data-t="00:16:33">[00:16:33]</a>:
*   **Actual vs. Budgeted Expense:** Similar to income variance, this links to an "Expense Variance Analysis" database, showing total budgeted, actual, difference, and percentage change for expenses <a class="yt-timestamp" data-t="00:18:51">[00:18:51]</a>.
*   **Quarterly Expense Overview:** Displays actual expense and its proportion to budgeted expense for each month, grouped by quarter, linking to the "Month of Expense" database <a class="yt-timestamp" data-t="00:19:24">[00:19:24]</a>.
*   **Type of Expenses:** Shows actual expenses for variable and fixed categories, along with their proportion to total expenses <a class="yt-timestamp" data-t="00:19:45">[00:19:45]</a>. This links to a "Type of Expense" database <a class="yt-timestamp" data-t="00:19:57">[00:19:57]</a>.

### Step 3: Fund Allocation
The final step is to allocate the available funds (income minus expenses) for each month into different allocations <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>. This process is crucial for [[managing_finances_with_notion | managing finances with Notion]] and [[budgeting_and_saving_with_notion | budgeting and saving with Notion]].

#### Calculating Available Funds
The "Available Funds" are calculated using a formula: `Total Income - Total Expenses` <a class="yt-timestamp" data-t="00:21:28">[00:21:28]</a>. Total income and actual expense values are pulled using roll-up properties from their respective monthly databases <a class="yt-timestamp" data-t="00:22:53">[00:22:53]</a>.

#### Allocating Funds
Available funds are then allocated to categories like:
*   **Investment:** A number property for allocated investment amounts <a class="yt-timestamp" data-t="00:21:52">[00:21:52]</a>.
*   **Savings:** A number property for allocated savings amounts <a class="yt-timestamp" data-t="00:21:54">[00:21:54]</a>.
*   **Others:** A number property for other allocations <a class="yt-timestamp" data-t="00:21:54">[00:21:54]</a>.

A "Total Allocation" formula sums these allocated amounts (`Investment + Savings + Other Allocations`) <a class="yt-timestamp" data-t="00:22:01">[00:22:01]</a>. The "Percentage of Allocation" is calculated by `Total Allocation / Total Available Funds`, displayed as a percentage bar <a class="yt-timestamp" data-t="00:22:26">[00:22:26]</a>.

#### Fund Allocation Overviews
The dashboard presents these allocations through:
*   **Fund Allocation Overview:** Provides an analysis of remaining funds allocated to different heads (Investment, Savings, Others), showing the total allocated amount and proportion of allocation to total available funds <a class="yt-timestamp" data-t="00:20:27">[00:20:27]</a>. This view links to individual allocation databases <a class="yt-timestamp" data-t="00:23:14">[00:23:14]</a>.
*   **Quarterly Allocation Overview:** Offers a monthly allocation overview, detailing total available funds for each month and the proportion of funds allocated, broken down by quarters <a class="yt-timestamp" data-t="00:20:59">[00:20:59]</a>. This links to an "Available Funds" database <a class="yt-timestamp" data-t="00:23:38">[00:23:38]</a>.

By following these steps, users can complete the entire budget tracker in Notion, allowing for comprehensive [[using_notion_for_personal_finance_management | personal finance management]] and [[budgeting_and_saving_strategically_with_notion | strategic budgeting and saving]]. This systematic approach enables [[customizing_notion_templates_for_financial_tracking | customizing Notion templates for financial tracking]] and offers an [[overview_of_notion_budget_tracker_template | overview of Notion budget tracker template]] functionality, including [[using_notion_for_financial_planning_and_debt_overview | financial planning and debt overview]].