---
title: Setting up income and expense tracking in Notion
videoId: C9gr5yS8EPc
---

From: [[theaccountantguy]] <br/> 

This article details how to create a minimalistic budget planner using Notion to track income and expenses in one central location <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.

## Budget Planner Capabilities
The Notion budget planner allows users to:
*   Keep track of income and expenses <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>.
*   Fix monthly income goals <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>.
*   Categorize expenses to identify areas for improvement <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.
*   Set and monitor monthly budgets for different categories <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.
*   Access the budget tracker from any device, anywhere <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.

## Accessing the Template
This template can be obtained by visiting the online store: `theaccountantguy.gumroad.com` <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>. To use this template, a Notion account is required <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>.

## Dashboard Segments
The dashboard consists of three primary segments <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>:
1.  **Summary Segment**: Provides an overall view of income, expenses, and allocation of funds, including quarterly allocation <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a> <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.
2.  **Income Details**: Shows actual versus estimated income, quarterly income overview, and frequency of income <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.
3.  **Expense Details**: Displays actual versus budgeted expenses, quarterly expense overview, and type of expenses <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>.

## Setting Up the Budget Tracker
[[setting_up_notion_for_personal_finance_tracking | Setting up a finance tracker in Notion]] involves three simple steps <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>:

### Step 1: Filling Out Income Details
This step involves creating and populating an inline database for income <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.
*   **Creating an Inline Database**: Type `/` and then `database` to select `database inline` <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>.
*   **Database Title**: The database can be named (e.g., "Expected Income Source Details") by clicking on the three dots, selecting `layout options`, clicking `show database title`, and then editing the title <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.
*   **Columns in the Income Database**:
    *   **Income details**: This is the default `title` property for any inline database, specifying each individual income earned in a month <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a> <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>.
    *   **Source of income**: A `relation` property linking to another database, categorizing income (e.g., Salary, Side Hustle, Other Sources) <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a> <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.
    *   **Month of income**: A `relation` property linking to another database, specifying the month income is earned <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a> <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.
    *   **Frequency of income**: A `relation` property linking to another database, indicating how frequently income is earned (e.g., Recurring, One-time) <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a> <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.
    *   **Expected income**: A `number` property specifying the anticipated income for a month, formatted with a currency (e.g., US dollars) <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a> <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>.
    *   **Actual income**: A `number` property for the income earned at the end of the month, also formatted with a currency <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a> <a class="yt-timestamp" data-t="00:05:45">[00:05:45]</a>.
    *   **Difference**: A `formula` type property calculating the difference between actual income and expected income <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a> <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.

#### Income Details Subsections (Analysis using Relation and Roll-up Properties)
The income details section of the dashboard utilizes linked databases and `relation` and `roll-up` properties for deeper analysis <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>. To create a linked database, type `/` and then `link database` <a class="yt-timestamp" data-t="00:15:02">[00:15:02]</a>.

*   **Actual versus Estimated Income**:
    *   This section links to an `Income Variance Distribution` database <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a> <a class="yt-timestamp" data-t="00:15:22">[00:15:22]</a>.
    *   It displays total actual income, total estimated income, the difference between them, and the percentage change for various income types <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>.
    *   `Relation` property is used to link to an `Income Type Database` (e.g., Salary, Side Hustle, Other Sources) <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>.
    *   `Roll-up` property pulls the desired properties (e.g., Actual Income, Expected Income) from the original income database and calculates their sum <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>.
    *   `If` formulas are used to display relevant values (e.g., total estimated income, total actual income, difference) based on the field type <a class="yt-timestamp" data-t="00:13:49">[00:13:49]</a>.

*   **Quarterly Income Overview**:
    *   This section links to the `Month of Income` database <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a> <a class="yt-timestamp" data-t="00:15:38">[00:15:38]</a>.
    *   It shows the total actual income and the proportion of actual income to budgeted income for each month, divided into four quarters <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a> <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>.
    *   `Relation` and `Roll-up` properties are used to calculate expected and actual income for each month <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>.
    *   A `formula` calculates the percentage of budgeted income (Total Actual Income / Total Expected Income) and can be represented as a bar <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>.
    *   The view is set to `Gallery` mode, filtered by quarters (e.g., Q1: Jan, Feb, Mar) <a class="yt-timestamp" data-t="00:15:42">[00:15:42]</a>. Only actual income and its proportion are visible <a class="yt-timestamp" data-t="00:16:02">[00:16:02]</a>.

*   **Frequency of Income**:
    *   This section links to the `Frequency of Income` database <a class="yt-timestamp" data-t="00:11:20">[00:11:20]</a> <a class="yt-timestamp" data-t="00:16:13">[00:16:13]</a>.
    *   It displays how frequently income is earned (recurring or one-time) and the total actual income, total proportion, and percentage for each type <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>.
    *   `Relation` and `Roll-up` properties are used to find total actual income and total expected income for each mode <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>.
    *   A `formula` calculates the total proportion of each income form to the total income (Total Income of Each Mode / Total Actual Income) <a class="yt-timestamp" data-t="00:12:37">[00:12:37]</a>.
    *   The view is set to `List` mode <a class="yt-timestamp" data-t="00:16:19">[00:16:19]</a>, showing actual income, total income, and percentage <a class="yt-timestamp" data-t="00:16:21">[00:16:21]</a>.

### Step 2: Filling Out Expense Details
[[tracking_transactions_and_expenses_in_notion | Tracking expenses and income in Notion]] involves setting up a dedicated database for expenses <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>. This database is similar in structure to the income database <a class="yt-timestamp" data-t="00:17:14">[00:17:14]</a>.

*   **Columns in the Expense Database**:
    *   **Expense source**: Specifies the details of the expense <a class="yt-timestamp" data-t="00:17:19">[00:17:19]</a>.
    *   **Month of expense**: A `relation` property linking to another database, similar to income details <a class="yt-timestamp" data-t="00:17:26">[00:17:26]</a>.
    *   **Expense classification**: A `relation` property linking to another database, segregating expenses into six heads (e.g., Utility and Bills, Loans and Debts, Food and Groceries, Entertainment, Travel and Transportation, Others) <a class="yt-timestamp" data-t="00:17:36">[00:17:36]</a>.
    *   **Expense type**: A `relation` property linking to the `Type of Expense` database, specified as variable or fixed expense <a class="yt-timestamp" data-t="00:17:56">[00:17:56]</a>.
    *   **Budgeted expense**: A `number` property (US dollars) for the expected expense <a class="yt-timestamp" data-t="00:18:06">[00:18:06]</a>.
    *   **Actual expense**: A `number` property (US dollars) for the incurred expense <a class="yt-timestamp" data-t="00:18:15">[00:18:15]</a>.
    *   **Difference**: Calculates the difference between actual and budgeted expenses. A positive difference means actual was less than budgeted; a negative difference means actual was more than budgeted <a class="yt-timestamp" data-t="00:18:23">[00:18:23]</a>.

#### Expense Details Subsections
The expense details section also uses linked databases for analysis <a class="yt-timestamp" data-t="00:16:33">[00:16:33]</a>.

*   **Actual versus Budgeted Expense**:
    *   Links to an `Expense Variance Analysis` database <a class="yt-timestamp" data-t="00:18:51">[00:18:51]</a>.
    *   Provides total budgeted expense, total actual expense, difference, and percentage change <a class="yt-timestamp" data-t="00:19:04">[00:19:04]</a>.
    *   The database is set to `Gallery` mode <a class="yt-timestamp" data-t="00:19:11">[00:19:11]</a>.

*   **Quarterly Expense Overview**:
    *   Links to the `Month of Expense` database <a class="yt-timestamp" data-t="00:19:24">[00:19:24]</a>.
    *   Shows actual expense incurred and the proportion of actual expense to budgeted expense for each month <a class="yt-timestamp" data-t="00:19:26">[00:19:26]</a>.
    *   Presented in `Gallery` view mode <a class="yt-timestamp" data-t="00:19:34">[00:19:34]</a>.

*   **Type of Expenses**:
    *   Links to the `Type of Expense` database <a class="yt-timestamp" data-t="00:19:57">[00:19:57]</a>.
    *   Segregates expenses into variable and fixed, showing total actual expenses for each type and their proportion to the total expense <a class="yt-timestamp" data-t="00:16:59">[00:16:59]</a>.
    *   Presented in `Listicle` view mode <a class="yt-timestamp" data-t="00:19:57">[00:19:57]</a>.

### Step 3: Allocating Available Funds
This final step involves allocating the `available funds` (income minus expenses) to different categories <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a> <a class="yt-timestamp" data-t="00:20:20">[00:20:20]</a>.

*   **Calculating Available Funds**: A `formula` calculates `Total Income - Total Expenses` for each month <a class="yt-timestamp" data-t="00:21:28">[00:21:28]</a>.
    *   `Total Actual Income` is derived using a `roll-up` property from the `month-of-income` database <a class="yt-timestamp" data-t="00:22:53">[00:22:53]</a>.
    *   `Actual Expense` is linked to the `month of expense` database <a class="yt-timestamp" data-t="00:23:06">[00:23:06]</a>.

*   **Fund Allocation Overview**:
    *   This segment provides an analysis of remaining funds allocated to different heads like Investment, Savings, and Others <a class="yt-timestamp" data-t="00:20:27">[00:20:27]</a>.
    *   Investment, Savings, and Other allocations are number properties set as US dollars <a class="yt-timestamp" data-t="00:22:09">[00:22:09]</a>.
    *   **Total Allocation**: A `formula` sums Investments, Savings, and Other allocations <a class="yt-timestamp" data-t="00:22:01">[00:22:01]</a>.
    *   **Percentage of Allocation**: A `formula` calculates `Total Allocation / Total Available Funds`, set to a percentage format <a class="yt-timestamp" data-t="00:22:26">[00:22:26]</a>.
    *   Each individual allocation is linked to an `Allocation of Funds` database, displayed in `Gallery` layout, showing investment source, allocation amount, and percentage of allocation <a class="yt-timestamp" data-t="00:23:14">[00:23:14]</a>.

*   **Quarterly Allocation Overview**:
    *   Gives a monthly allocation overview, showing total available funds for each month and the proportion of funds allocated <a class="yt-timestamp" data-t="00:20:59">[00:20:59]</a>.
    *   This section links to an `Available Funds` database <a class="yt-timestamp" data-t="00:23:38">[00:23:38]</a>.
    *   Set to `Gallery` mode, displaying month, total available funds, and percentage of allocation for each individual month <a class="yt-timestamp" data-t="00:23:44">[00:23:44]</a>. This is also categorized by quarters <a class="yt-timestamp" data-t="00:23:53">[00:23:53]</a>.

This completes the setup of the budget tracker in Notion. [[tracking_income_expenses_assets_and_liabilities_in_notion | Using Notion for financial tracking]] streamlines personal finance management.