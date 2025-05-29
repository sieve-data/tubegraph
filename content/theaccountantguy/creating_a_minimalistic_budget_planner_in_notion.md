---
title: Creating a minimalistic budget planner in Notion
videoId: C9gr5yS8EPc
---

From: [[theaccountantguy]] <br/> 

This article outlines how to create a minimalistic budget planner using Notion to [[managing_finances_with_notion | manage finances]] and track income and expenses <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>. This dashboard can be used to set monthly income goals, categorize expenses, monitor monthly budgets, and access the budget tracker from any device <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>. This template is designed for [[budgeting_and_expense_management_in_notion | budgeting and expense management in Notion]] <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.

## Accessing the Template

The template can be obtained by visiting the online store at `theaccountantguy.gumroad.com` <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>. To use the template, a Notion account is required <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.

## Dashboard Overview

The budget planner dashboard consists of three main segments <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>:

1.  **Summary Segment**: Provides an overall view of income, expenses, and allocation of funds, including quarterly allocation <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.
2.  **Income Details**: Shows actual versus estimated income, quarterly income overview, and frequency of income <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.
3.  **Expense Details**: Displays actual versus budgeted expenses, quarterly expense overview, and type of expenses <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>.

## Setting Up the Budget Planner

The budget planner is set up following three simple steps <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>:

1.  Filling out income details <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.
2.  Filling out expense details <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.
3.  Allocating available funds (income minus expenses) <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.

### Step 1: Filling Out Income Details

The first step involves creating an inline database for income details <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>. An inline database can be created by typing `/` followed by `database` and selecting `database inline` <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.

**Columns in the Income Database:**

*   **Income Details**: A title-type property specifying individual incomes <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
*   **Source of Income**: A relation property linked to another database, categorizing income (e.g., salary, side hustle, other sources) <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.
*   **Month of Income**: A relation property linked to a separate database for months <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.
*   **Frequency of Income**: A relation property linked to another database, indicating if income is recurring or one-time <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.
*   **Expected Income**: A number property, typically formatted as US Dollars or a currency of choice <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.
*   **Actual Income**: A number property, also formatted as US Dollars, for the income earned <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>.
*   **Difference**: A formula-type property calculating the difference between actual and expected income <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>.

The database title can be made visible and edited by clicking the three dots next to the database, selecting "layout options", and enabling "show database title" <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.

#### Linking Databases and Roll-Up Properties for Income Analysis

To gain detailed insights, the income details database uses 'Relation' and 'Roll-up' properties to link with other databases <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>.

*   **Source of Income Analysis**: The `Source of Income` column is related to an `income type database` <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>. This allows for calculating total actual income, total budgeted income, difference, and percentage change for each income type (e.g., salary, side hustle) using a roll-up property <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>.
*   **Monthly Income Analysis**: The `Month of Income` column is related to a `month of income database` <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>. This helps calculate total actual and expected income for each month, and the proportion of actual income to budgeted income, again using relation and roll-up properties <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>. The percentage is calculated by dividing total actual income by total expected income and formatted as a percent <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>.
*   **Frequency of Income Analysis**: The `Frequency of Income` column is related to a `frequency of income database` <a class="yt-timestamp" data-t="00:11:37">[00:11:37]</a>. This allows calculating total actual and expected income for recurring versus one-time income sources <a class="yt-timestamp" data-t="00:11:44">[00:11:44]</a>.

### Step 2: Filling Out Expense Details

The expense details section involves creating a database to track all expenses <a class="yt-timestamp" data-t="00:17:14">[00:17:14]</a>.

**Columns in the Expense Database:**

*   **Expense Source**: Specifies what the expense is for <a class="yt-timestamp" data-t="00:17:19">[00:17:19]</a>.
*   **Month of Expense**: A relation property linked to another database, similar to income details <a class="yt-timestamp" data-t="00:17:26">[00:17:26]</a>.
*   **Expense Classification**: A relation property linked to another database, segregating expenses into categories like utilities, loans, food, entertainment, travel <a class="yt-timestamp" data-t="00:17:36">[00:17:36]</a>.
*   **Expense Type**: A relation property linked to a `type of expense database`, classifying expenses as variable or fixed <a class="yt-timestamp" data-t="00:17:56">[00:17:56]</a>.
*   **Budgeted Expense**: A number property (e.g., US Dollars) for the expected expense <a class="yt-timestamp" data-t="00:18:06">[00:18:06]</a>.
*   **Actual Expense**: A number property (e.g., US Dollars) for the actual expense incurred <a class="yt-timestamp" data-t="00:18:15">[00:18:15]</a>.
*   **Difference**: Calculates the difference between actual and budgeted expenses <a class="yt-timestamp" data-t="00:18:23">[00:18:23]</a>.

#### Expense Analysis and Linked Databases

Similar to income details, expense data is linked to other databases for detailed analysis <a class="yt-timestamp" data-t="00:18:51">[00:18:51]</a>:

*   **Actual vs. Budgeted Expense**: Linked to an `expense variance analysis` database, it shows total budgeted expense, total actual expense, difference, and percentage change <a class="yt-timestamp" data-t="00:18:57">[00:18:57]</a>. This can be viewed in Gallery mode <a class="yt-timestamp" data-t="00:19:11">[00:19:11]</a>.
*   **Quarterly Expense Overview**: Linked to the `month of expense` database, displaying actual expense and proportion of actual to budgeted expense for each month, also in Gallery mode <a class="yt-timestamp" data-t="00:19:24">[00:19:24]</a>.
*   **Type of Expenses**: Linked to the `type of expense` database, showing actual expenses and their proportion to total expenses for variable and fixed categories, often in List mode <a class="yt-timestamp" data-t="00:19:47">[00:19:47]</a>.

### Step 3: Allocating Available Funds

This final step involves allocating the funds remaining after expenses are deducted from income <a class="yt-timestamp" data-t="00:21:25">[00:21:25]</a>.

**Fund Allocation Database:**

*   **Total Available Funds**: A formula property calculating `Total Income - Total Expenses` <a class="yt-timestamp" data-t="00:21:41">[00:21:41]</a>. Total income and expenses are pulled using roll-up properties from the `month-of-income` and `month-of-expense` databases, respectively <a class="yt-timestamp" data-t="00:22:53">[00:22:53]</a>.
*   **Investment, Savings, Others**: Number properties (e.g., US Dollars) for allocating funds to these categories <a class="yt-timestamp" data-t="00:21:51">[00:21:51]</a>.
*   **Total Allocation**: A formula summing Investments, Savings, and Other allocations <a class="yt-timestamp" data-t="00:22:01">[00:22:01]</a>.
*   **Percentage of Allocation**: A formula calculating `Total Allocation / Total Available Funds`, formatted as a percentage and represented by a bar <a class="yt-timestamp" data-t="00:22:26">[00:22:26]</a>.

#### Fund Allocation Overviews

*   **Fund Allocation Overview**: Provides an analysis of remaining funds allocated to different heads (Investment, Savings, Others), showing allocated amounts and their proportion to total available funds <a class="yt-timestamp" data-t="00:20:29">[00:20:29]</a>. This is linked to an `allocation of funds` database <a class="yt-timestamp" data-t="00:23:14">[00:23:14]</a>.
*   **Quarterly Allocation Overview**: Gives a monthly allocation overview showing total available funds and proportion of funds allocated for each month, divided into quarters <a class="yt-timestamp" data-t="00:20:59">[00:20:59]</a>. This is linked to an `available funds` database <a class="yt-timestamp" data-t="00:23:38">[00:23:38]</a>.

## Linking Databases on the Main Dashboard

To display these detailed analyses on the primary dashboard, linked databases are used <a class="yt-timestamp" data-t="00:14:45">[00:14:45]</a>. This is done by typing `/` and then `link database` <a class="yt-timestamp" data-t="00:15:02">[00:15:02]</a>.

*   **Actual vs. Estimated Income**: Links the `income variance distribution` database <a class="yt-timestamp" data-t="00:15:22">[00:15:22]</a>.
*   **Quarterly Income Overview**: Links the `month of income` database and sets it to a Gallery view, filtered by quarters (e.g., Jan, Feb, March for Q1) <a class="yt-timestamp" data-t="00:15:38">[00:15:38]</a>.
*   **Frequency of Income**: Links the `frequency of income` database and sets it to a List view <a class="yt-timestamp" data-t="00:16:13">[00:16:13]</a>.

> [!NOTE] Property Visibility
> In linked database views, specific properties can be toggled visible or hidden to simplify the display <a class="yt-timestamp" data-t="00:16:02">[00:16:02]</a>.