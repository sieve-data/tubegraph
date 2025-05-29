---
title: Using Notion templates for financial management
videoId: C9gr5yS8EPc
---

From: [[theaccountantguy]] <br/> 

This article outlines how to create a minimalistic budget planner using [[notion_finance_templates | Notion]] to manage personal finances. This dashboard allows users to track income and expenses, set monthly income goals, categorize expenses, monitor monthly budgets, and access their budget tracker from any device <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.

## Acquiring the Template
The described [[notion_finance_templates | template]] can be obtained by visiting the online store at accountantguy.gumroad.com <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.

## Dashboard Segments
The budget planner dashboard consists of three main segments <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>:

*   **Summary Segment**: Provides an overall view of income, expenses, and allocation of funds, including quarterly allocation <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a> <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.
*   **Income Details**: Offers specifics on actual versus estimated income, quarterly income overview, and frequency of income <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.
*   **Expense Details**: Presents information on actual versus budgeted [[using_notion_templates_for_expense_management | expenses]], quarterly [[using_notion_templates_for_expense_management | expense]] overview, and type of [[using_notion_templates_for_expense_management | expenses]] <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>.

## Setting Up the Budget Tracker
To use this [[notion_finance_templates | template]], users need to sign up for a Notion account <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>. Setting up the [[overview_of_notion_budget_tracker_template | budget tracker]] involves three simple steps <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>:

1.  Filling out the income details for each month <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.
2.  Filling out the [[using_notion_templates_for_expense_management | expense]] details for each individual month <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.
3.  Allocating available funds (income minus expenses) for each month onto different allocations <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.

### Step 1: Filling Out Income Details
The first step involves creating and populating an inline database for income details <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.

#### Creating an Inline Database
An inline database can be created by typing `/` and then `database`, selecting "database inline" <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>. This database can be named, for example, "expected income Source details" <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.

#### Columns in the Income Database
The inline database for income details includes the following columns:

*   **Income details**: Specifies each individual income earned in a particular month <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>. This is the default title property <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>.
*   **Source of income**: A category for each income, such as salary, side hustle, and other sources <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>. This column has a relation property linked to an "income type" database <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.
*   **Month of income**: Specifies the month when income is earned <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>. This also uses a relation property with a "month of income" database <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.
*   **Frequency of income**: Indicates how frequently income is earned (e.g., recurring, one-time) <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>. This column is related to a "frequency of income" database <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.
*   **Expected income**: A number property indicating expected income for a month, formatted as US dollars or chosen currency <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a> <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>.
*   **Actual income**: A number property for the actual income earned, also formatted as US dollars <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a> <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>.
*   **Difference**: A formula type property calculating the difference between actual and expected income <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a> <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.

#### Linking Databases and Using Roll-up Property
To provide a better analysis, individual columns are linked to different databases using "relation" and "roll-up" properties <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>.

*   **Income Type Database**: Linked to the "Source of income" column, it provides information like total actual income, total budgeted income, difference, and percentage change for various income types (e.g., salary, side hustle) <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>.
    *   The "roll-up" property is used to pull desired properties (e.g., actual income, expected income) from the original database and calculate sums <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a> <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>.
*   **Month of Income Database**: Linked to the "Month of income" column, it allows calculation of total actual income, expected income, and the proportion of actual to budgeted income for each month <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>.
    *   A formula calculates the percentage of budgeted income by dividing total actual income by total expected income, converted to a percentage and represented by a bar <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>.
*   **Frequency of Income Database**: Linked to the "Frequency of income" column, it calculates total actual and expected income for recurring or one-time income types <a class="yt-timestamp" data-t="00:11:35">[00:11:35]</a>.
    *   Total proportion of each form of income to the total income is calculated by dividing the total income of each mode by the total actual income and converting it to a percentage <a class="yt-timestamp" data-t="00:12:37">[00:12:37]</a>.
*   **Income Variance Distribution Database**: This linked database calculates total estimated income, total actual income, the difference, and the change in percentage for each income head <a class="yt-timestamp" data-t="00:13:08">[00:13:08]</a>.
    *   "Roll-up" properties and `if` formulas are used to display relevant values based on the specific field (e.g., total estimated income, actual income, difference, change in percentage) <a class="yt-timestamp" data-t="00:13:22">[00:13:22]</a>.

#### Dashboard Views for Income Details
The primary dashboard's income details section links these databases to provide sub-sections:

*   **Actual versus Estimated Income**: Links to the "Income variance distribution" database to show total actual income, estimated income, and percentage change per income head <a class="yt-timestamp" data-t="00:15:22">[00:15:22]</a>.
*   **Quarterly Income Overview**: Links to the "Month of income" database, displayed in a gallery view, filtered by quarters (e.g., Q1 for Jan, Feb, Mar) showing actual income and proportion to budgeted income <a class="yt-timestamp" data-t="00:15:38">[00:15:38]</a>.
*   **Frequency of Income**: Links to the "Frequency of income" database, set in a list view, displaying actual income, total income, and percentage for different income heads <a class="yt-timestamp" data-t="00:16:13">[00:16:13]</a>.

To create a linked database, type `/` and then `link database` and select the desired database <a class="yt-timestamp" data-t="00:15:02">[00:15:02]</a>.

### Step 2: Filling Out Expense Details
Similar to income details, Step 2 involves managing [[using_notion_templates_for_expense_management | expenses]] in a dedicated database <a class="yt-timestamp" data-t="00:17:14">[00:17:14]</a>.

#### Columns in the Expense Database
The expense database includes:

*   **Expense source**: Specifies the details of the [[using_notion_templates_for_expense_management | expense]] to be incurred <a class="yt-timestamp" data-t="00:17:19">[00:17:19]</a>.
*   **Month of expense**: The month when an [[using_notion_templates_for_expense_management | expense]] is incurred, with a relation property to another database (similar to income) <a class="yt-timestamp" data-t="00:17:26">[00:17:26]</a>.
*   **Expense classification**: Segregated into six heads like utility and bills, loans and debts, food and groceries, entertainment, travel, and transportation <a class="yt-timestamp" data-t="00:17:36">[00:17:36]</a>. This is linked to another database via a relation <a class="yt-timestamp" data-t="00:17:49">[00:17:49]</a>.
*   **Expense type**: Classified as variable and fixed [[using_notion_templates_for_expense_management | expense]], linked to a "type of [[using_notion_templates_for_expense_management | expense]]" database with a relation property <a class="yt-timestamp" data-t="00:17:56">[00:17:56]</a>.
*   **Budgeted expense**: A number property set as US dollars for the expected [[using_notion_templates_for_expense_management | expense]] in a month <a class="yt-timestamp" data-t="00:18:06">[00:18:06]</a>.
*   **Actual expense**: A number property set as US dollars for the actual [[using_notion_templates_for_expense_management | expense]] in a month <a class="yt-timestamp" data-t="00:18:15">[00:18:15]</a>.
*   **Difference**: Calculates the difference between actual and budgeted [[using_notion_templates_for_expense_management | expenses]] <a class="yt-timestamp" data-t="00:18:23">[00:18:23]</a>.

#### Dashboard Views for Expense Details
The expense details section also links to different databases for its subsections:

*   **Actual versus Budgeted Expense**: Linked to an "expense variance analysis" database, it provides total budgeted [[using_notion_templates_for_expense_management | expense]], total actual [[using_notion_templates_for_expense_management | expense]], difference, and percentage change <a class="yt-timestamp" data-t="00:18:51">[00:18:51]</a>. This is displayed in a gallery view <a class="yt-timestamp" data-t="00:19:11">[00:19:11]</a>.
*   **Quarterly Expense Overview**: Shows actual [[using_notion_templates_for_expense_management | expense]] incurred and its proportion to budgeted [[using_notion_templates_for_expense_management | expense]] for each month, linked to the "month of [[using_notion_templates_for_expense_management | expense]]" database in a gallery view <a class="yt-timestamp" data-t="00:19:24">[00:19:24]</a>.
*   **Type of Expense**: Segregates [[using_notion_templates_for_expense_management | expenses]] into variable and fixed types, showing total actual [[using_notion_templates_for_expense_management | expenses]] and their proportion to the total [[using_notion_templates_for_expense_management | expense]], linked to the "type of [[using_notion_templates_for_expense_management | expense]]" database in a list view <a class="yt-timestamp" data-t="00:19:45">[00:19:45]</a>.

### Step 3: Allocation of Available Funds
After income and [[using_notion_templates_for_expense_management | expense]] details, the final step involves allocating available funds (income minus expenses) <a class="yt-timestamp" data-t="00:21:20">[00:21:20]</a>.

#### Calculating Available Funds
A formula calculates the total available funds for each month by subtracting total expenses from total income <a class="yt-timestamp" data-t="00:21:28">[00:21:28]</a>.

#### Allocating Funds
Available funds are allocated to different heads:
*   Investment
*   Savings
*   Others
These are number properties set in US dollars <a class="yt-timestamp" data-t="00:21:52">[00:21:52]</a>.

#### Calculating Total Allocation and Percentage
The total allocation is the summation of investments, savings, and other allocations, represented by a formula <a class="yt-timestamp" data-t="00:22:01">[00:22:01]</a>. The percentage of allocation is calculated by dividing total allocation by total available funds, formatted as a percentage and visualized with a bar <a class="yt-timestamp" data-t="00:22:26">[00:22:26]</a>.

#### Dashboard Views for Fund Allocation
The primary dashboard includes:

*   **Fund Allocation Overview**: Provides an analysis of remaining funds allocated to different heads (investment, savings, others), showing the total allocation amount and its proportion to total available funds <a class="yt-timestamp" data-t="00:20:27">[00:20:27]</a>. Each individual allocation is linked to an "allocation of funds" database, displayed in a gallery layout <a class="yt-timestamp" data-t="00:23:14">[00:23:14]</a>.
*   **Quarterly Allocation Overview**: Gives a monthly allocation overview, detailing total available funds for each month and the proportion of funds allocated, specified for each quarter of the year <a class="yt-timestamp" data-t="00:20:58">[00:20:58]</a>. This is linked to an "available funds" database in gallery mode <a class="yt-timestamp" data-t="00:23:38">[00:23:38]</a>.