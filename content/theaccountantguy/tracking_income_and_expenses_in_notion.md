---
title: Tracking Income and Expenses in Notion
videoId: C9gr5yS8EPc
---

From: [[theaccountantguy]] <br/> 

The Accountant Guy offers a guide on how to [[budgeting_and_tracking_expenses_in_notion | create a minimalistic budget planner]] using Notion <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>. This dashboard serves as a central location to [[how_to_track_income_and_expenses_using_notion | keep track of your income and expenses]] <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>.

## Benefits of the Notion Budget Planner
This Notion budget planner allows you to:
*   [[how_to_track_income_and_expenses_using_notion | Keep track of your income and expenses]] in one central location <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>.
*   Set monthly income goals to assess overall performance <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>.
*   [[expense_tracking_using_notion | Categorize expenses]] to identify areas for improvement <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.
*   Set and monitor monthly budgets for different categories <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.
*   Gain access to your [[expense_tracking_using_notion | budget tracker]] from any device, anywhere <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.

## Dashboard Segments
The budget planner dashboard is divided into three main segments:
1.  **Summary Segment**: Provides an overall view of income, expenses, and allocation of funds <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>, including quarterly allocation <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.
2.  **Income Details**: Shows details of actual versus estimated income, quarterly income overview, and frequency of income <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.
3.  **Expense Details**: Presents details of actual versus budgeted expenses, quarterly expense overview, and type of expenses <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>.

## Setting Up the Budget Tracker
To use this template, you need a Notion account <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>. The setup process involves three simple steps:
1.  **Filling out Income Details**: Input all income information for each month <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.
2.  **Filling out Expense Details**: Input all expense information for each individual month <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.
3.  **Allocating Available Funds**: Distribute the available funds (income minus expenses) for each month into different allocations <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.

### Step 1: Filling Up Income Details
To [[building_an_income_tracker_in_notion | build an income tracker]] within the budget planner, you start by [[creating_an_expense_tracker_with_notion | creating an inline database]] <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>. This can be done by typing `/database` and selecting `database inline` <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.

The inline database for income details includes the following columns:
*   **Income Details**: Specifies each individual income earned in a particular month <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>. This property is set as the default `title` type <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>.
*   **Source of Income**: Categorizes each income, such as salary, side hustle, or other sources <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>. This column has a `relation` property linked to an "income type" database for better analysis <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.
*   **Month of Income**: Specifies the month when income is earned <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>. This is also a `relation` property linked to a "month of income" database <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.
*   **Frequency of Income**: Indicates how frequently income is earned (e.g., recurring or one-time) <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>. This is another `relation` property <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.
*   **Expected Income**: The anticipated income for a month <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>. This is a `number` property, typically formatted as US dollars or your preferred currency <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>.
*   **Actual Income**: The actual income earned at the end of a month <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>. This is also a `number` property, set to US dollars <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.
*   **Difference**: The calculated difference between actual and expected income <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>. This uses a `formula` type property <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>.

#### Using Relation and Roll-Up Properties for Income Analysis
To provide comprehensive analysis, the income details section utilizes `relation` and `roll-up` properties linked to other databases <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>.

*   **Actual vs. Estimated Income**: Displays total actual income, total estimated income, the difference, and the percentage change for various income types (e.g., salary, side hustle, others) <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>. This is achieved by linking the main income database to an "income type" database and using `roll-up` properties to sum actual and expected income values based on their source <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>.
*   **Quarterly Income Overview**: Shows the total actual income and the proportion of actual income to budgeted income for each month, divided into four quarters <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>. This connects to a "month of income" database using `relation` and `roll-up` properties to calculate monthly expected and actual incomes, and a `formula` to determine the percentage of budgeted income <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>.
*   **Frequency of Income**: Illustrates how frequently income is earned (recurring or one-time) and the total actual income for each frequency type, along with its proportion and percentage <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>. This is linked to a "frequency of income" database, using `relation` and `roll-up` to sum actual and expected income, and a `formula` for the proportion <a class="yt-timestamp" data-t="00:11:35">[00:11:35]</a>.

#### Linking Databases on the Main Dashboard
The income details on the primary dashboard are created by linking different databases:
*   For "Actual versus Estimated Income," the `income variance distribution` database is linked <a class="yt-timestamp" data-t="00:15:22">[00:15:22]</a>.
*   For "Quarterly Income Overview," the `month of income` database is linked and set to a gallery view, filtered by quarter (e.g., Q1 for Jan, Feb, Mar) <a class="yt-timestamp" data-t="00:15:38">[00:15:38]</a>.
*   For "Frequency of Income," the `frequency of income` database is linked and displayed in a list view <a class="yt-timestamp" data-t="00:16:13">[00:16:13]</a>.

### Step 2: Filling Up Expense Details
The [[expense_tracking_using_notion | expense tracking]] section involves a similar database structure as income details <a class="yt-timestamp" data-t="00:17:14">[00:17:14]</a>. The expense details section on the dashboard has three subsections: "Actual versus Budgeted Expense," "Quarterly Expense Overview," and "Type of Expense" <a class="yt-timestamp" data-t="00:16:33">[00:16:33]</a>.

The main expense database includes:
*   **Expense Source**: Specifies the details of the expense <a class="yt-timestamp" data-t="00:17:19">[00:17:19]</a>.
*   **Month of Expense**: The month when an expense is incurred, linked via `relation` to another database <a class="yt-timestamp" data-t="00:17:26">[00:17:26]</a>.
*   **Expense Classification**: Segregated into six heads like utilities and bills, loans and debts, food and groceries, entertainment, travel and transportation, and others <a class="yt-timestamp" data-t="00:17:36">[00:17:36]</a>. This uses a `relation` property <a class="yt-timestamp" data-t="00:17:49">[00:17:49]</a>.
*   **Expense Type**: Categorized as variable or fixed expense, also linked via `relation` <a class="yt-timestamp" data-t="00:17:56">[00:17:56]</a>.
*   **Budgeted Expense**: The expected expense for a particular month, a `number` property set as US dollars <a class="yt-timestamp" data-t="00:18:06">[00:18:06]</a>.
*   **Actual Expense**: The actual expense for a particular month, a `number` property set as US dollars <a class="yt-timestamp" data-t="00:18:15">[00:18:15]</a>.
*   **Difference**: The difference between actual and budgeted expenses, indicating if actual was less (positive difference) or more (negative difference) <a class="yt-timestamp" data-t="00:18:23">[00:18:23]</a>.

#### Classifying Expense Information
Similar to income, `relation` and `roll-up` properties are extensively used to analyze expenses:
*   **Actual vs. Budgeted Expense**: Linked to an "expense variance analysis" database, showing total budgeted, total actual, difference, and percentage change <a class="yt-timestamp" data-t="00:18:51">[00:18:51]</a>.
*   **Quarterly Expense Overview**: For each month, it displays the actual expense and its proportion to the budgeted expense <a class="yt-timestamp" data-t="00:19:24">[00:19:24]</a>. This is a gallery view linked to the "month of expense" database <a class="yt-timestamp" data-t="00:19:34">[00:19:34]</a>.
*   **Type of Expenses**: Segregates expenses into variable and fixed types, showing total actual expenses for each and their proportion to total expenses <a class="yt-timestamp" data-t="00:19:45">[00:19:45]</a>. This is a list view linked to the "type of expense" database <a class="yt-timestamp" data-t="00:19:57">[00:19:57]</a>.

### Step 3: Allocation of Available Funds
After recording income and expenses, the final step is to allocate the available funds, which is calculated as income less expenses <a class="yt-timestamp" data-t="00:21:20">[00:21:20]</a>.

The fund allocation overview analyzes the remaining funds, categorized into:
*   **Investment Section** <a class="yt-timestamp" data-t="00:20:36">[00:20:36]</a>
*   **Savings Section** <a class="yt-timestamp" data-t="00:20:38">[00:20:38]</a>
*   **Others Section** <a class="yt-timestamp" data-t="00:20:38">[00:20:38]</a>

The planner calculates the total allocation amount and the proportion of allocated funds to the total available funds <a class="yt-timestamp" data-t="00:20:51">[00:20:51]</a>. A quarterly allocation overview also provides monthly allocation details <a class="yt-timestamp" data-t="00:20:59">[00:20:59]</a>.

Key calculations for fund allocation:
*   **Available Funds**: A `formula` property calculates `total income - total expenses` for each month <a class="yt-timestamp" data-t="00:21:41">[00:21:41]</a>.
*   **Individual Allocations**: Investments, savings, and other allocations are input as `number` properties (e.g., US dollars) <a class="yt-timestamp" data-t="00:22:09">[00:22:09]</a>.
*   **Total Allocation**: A `formula` property sums the investment, savings, and other allocations <a class="yt-timestamp" data-t="00:22:15">[00:22:15]</a>.
*   **Percentage of Allocation**: A `formula` property calculates `total allocation / total available funds` and is formatted as a percentage <a class="yt-timestamp" data-t="00:22:26">[00:22:26]</a>.

Similar to income and expenses, `roll-up` properties are used to pull actual income from the "month-of-income" database and actual expenses from the "month of expense" database <a class="yt-timestamp" data-t="00:22:53">[00:22:53]</a>. Individual fund allocations are linked to the "allocation of funds" database <a class="yt-timestamp" data-t="00:23:14">[00:23:14]</a>, and the quarterly allocation overview is linked to the "available funds" database <a class="yt-timestamp" data-t="00:23:38">[00:23:38]</a>.