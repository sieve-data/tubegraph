---
title: Setting and Monitoring Monthly Budgets
videoId: C9gr5yS8EPc
---

From: [[theaccountantguy]] <br/> 

This article describes how to [[creating_and_monitoring_budgets | create and monitor a minimalistic budget planner]] using Notion, designed to help users [[setting_and_managing_budgets_for_expenses | set and monitor monthly budgets]] for various categories <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>. The planner functions as a dashboard to keep track of income and expenses in one central location <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>, allowing users to fix monthly income goals to assess overall performance <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a> and categorize expenses to identify areas for improvement <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. The template is accessible from any device <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.

To utilize this template, a Notion account is required <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>. The template is available for purchase at accountantguy.gumroad.com <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.

## Budget Planner Dashboard Structure

The Notion budget planner dashboard comprises three main segments <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>:

*   **Summary Segment**: Provides an overall view of income, expenses, and allocation of funds, including a quarterly allocation overview <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.
*   **Income Details**: Offers details on actual versus estimated income, a quarterly income overview, and frequency of income <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.
*   **Expense Details**: Presents details on actual versus budgeted expenses, a quarterly expense overview, and the type of expenses <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>.

## Setting up the Budget Tracker

[[setting_up_a_monthly_budget_in_google_sheets | Setting up this budget tracker]] involves three simple steps <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>:

1.  **Filling out Income Details**: Inputting income information for each month <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.
2.  **Filling out Expense Details**: Inputting expense information for each individual month <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.
3.  **Allocating Available Funds**: Distributing the remaining funds (income minus expenses) for each month across different allocations <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.

## Income Details

The income details are captured in an inline database <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>, with the following columns:

*   **Income Details**: Specifies each individual income earned in a particular month <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
*   **Source of Income**: A category for each income (e.g., salary, side hustle, other sources) <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>. This column has a relation property linked to an "income type" database for detailed analysis <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.
*   **Month of Income**: Specifies the month when income is earned <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>. This is linked to a "month of income" database <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.
*   **Frequency of Income**: Indicates how frequently income is earned (e.g., recurring, one-time) <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>. This is linked to a "frequency of income" database <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.
*   **Expected Income**: The anticipated income for a month, set as a number property in US dollars (or preferred currency) <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.
*   **Actual Income**: The real income earned at the end of the month, also a number property in US dollars <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>.
*   **Difference**: A formula property calculating the difference between actual and expected income <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>.

### Analyzing Income Details

The income details section offers three subsections for analysis <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>:

*   **Actual vs. Estimated Income**: Provides total actual income, total estimated income, their difference, and percentage change for each income type <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>.
*   **Quarterly Income Overview**: Shows total actual income and the proportion of each income to the budgeted income for each month, divided into four quarters <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>.
*   **Frequency of Income**: Illustrates how frequently income is earned (recurring vs. one-time), representing total actual income and its proportion for each frequency type <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>.

These analyses are achieved using Notion's relation and roll-up properties, linking the main income database to secondary databases like "income type", "month of income", and "frequency of income" <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>. Formulas are used to calculate percentages and differences <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>.

## Expense Details

The expense details are managed in a separate database, tracking various aspects of spending <a class="yt-timestamp" data-t="00:17:14">[00:17:14]</a>. The columns include:

*   **Expense Source**: Specifies details about the incurred expense <a class="yt-timestamp" data-t="00:17:19">[00:17:19]</a>.
*   **Month of Expense**: The month when an expense is incurred, linked to a "month of expense" database <a class="yt-timestamp" data-t="00:17:26">[00:17:26]</a>.
*   **Expense Classification**: Categorizes expenses into heads like utility and bills, loans and debts, food and groceries, entertainment, travel, and transportation <a class="yt-timestamp" data-t="00:17:36">[00:17:36]</a>. This is linked to another database through a relation <a class="yt-timestamp" data-t="00:17:49">[00:17:49]</a>.
*   **Expense Type**: Specifies if an expense is variable or fixed, linked to a "type of expense" database <a class="yt-timestamp" data-t="00:17:56">[00:17:56]</a>.
*   **Budgeted Expense**: The expected expense for a month, a number property in US dollars <a class="yt-timestamp" data-t="00:18:06">[00:18:06]</a>.
*   **Actual Expense**: The actual expense incurred for a month, a number property in US dollars <a class="yt-timestamp" data-t="00:18:15">[00:18:15]</a>.
*   **Difference**: Calculates the difference between actual and budgeted expenses. A positive difference means actual expense was less than budgeted, while a negative difference means it was more <a class="yt-timestamp" data-t="00:18:23">[00:18:23]</a>.

### Analyzing Expense Details

Similar to income details, the expense section includes three subsections for analysis <a class="yt-timestamp" data-t="00:16:33">[00:16:33]</a>:

*   **Actual vs. Budgeted Expense**: Calculates total budgeted expense, total actual expense, their difference, and percentage change <a class="yt-timestamp" data-t="00:16:45">[00:16:45]</a>. This is linked to an "expense variance analysis" database <a class="yt-timestamp" data-t="00:18:57">[00:18:57]</a>.
*   **Quarterly Expense Overview**: Shows actual expense incurred for each month and its proportion to the budgeted expense <a class="yt-timestamp" data-t="00:16:51">[00:16:51]</a>. This is linked to the "month of expense" database <a class="yt-timestamp" data-t="00:19:26">[00:19:26]</a>.
*   **Type of Expense**: Segregates expenses into variable and fixed, showing total actual expenses for each type and their proportion to total expenses <a class="yt-timestamp" data-t="00:16:59">[00:16:59]</a>. This is linked to the "type of expense" database <a class="yt-timestamp" data-t="00:19:45">[00:19:45]</a>.

## Fund Allocation

After calculating income and expenses, the remaining funds are allocated <a class="yt-timestamp" data-t="00:21:20">[00:21:20]</a>. The total available funds are calculated as income less expenses <a class="yt-timestamp" data-t="00:21:31">[00:21:31]</a>. These funds are then allocated to different heads such as:

*   **Investment Section** <a class="yt-timestamp" data-t="00:20:34">[00:20:34]</a>
*   **Savings Section** <a class="yt-timestamp" data-t="00:20:36">[00:20:36]</a>
*   **Others Section** <a class="yt-timestamp" data-t="00:20:38">[00:20:38]</a>

The dashboard provides a "fund allocation overview" showing the remaining funds allocated to these different heads <a class="yt-timestamp" data-t="00:20:29">[00:20:29]</a>. The "total allocation" is the summation of these categories <a class="yt-timestamp" data-t="00:22:01">[00:22:01]</a>. A "percentage of allocation" is also calculated (total allocation divided by total available funds) <a class="yt-timestamp" data-t="00:22:26">[00:22:26]</a>.

A "quarterly allocation overview" gives a monthly allocation overview, detailing total available funds for each month and the proportion of funds allocated <a class="yt-timestamp" data-t="00:20:59">[00:20:59]</a>. Each individual allocation is linked to the "allocation of funds" database <a class="yt-timestamp" data-t="00:23:22">[00:23:22]</a>, while the quarterly overview links to the "available funds" database <a class="yt-timestamp" data-t="00:23:41">[00:23:41]</a>.

This comprehensive Notion template helps in [[introduction_to_paycheck_budget_tracker | tracking budgeted and actual expenses]] <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>, [[tracking_and_analyzing_actual_versus_budgeted_expenses | analyzing financial performance]], and [[setting_budget_goals_and_tracking_progress | setting budget goals and tracking progress]] effectively using its interconnected databases and roll-up properties. This provides a robust set of [[budgeting_tools | budgeting tools]] for [[managing_monthly_transactions_and_categories | managing monthly transactions and categories]].