---
title: Analyzing Fund Allocation and Financial Performance
videoId: C9gr5yS8EPc
---

From: [[theaccountantguy]] <br/> 
## Analyzing Fund Allocation and Financial Performance

A minimalistic budget planner built in Notion can be used to track income and expenses in one central location, allowing users to fix monthly income goals to assess their overall performance <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>. This approach enables categorization of expenses to identify areas for improvement, setting and monitoring monthly budgets, and gaining access to the budget tracker from any device <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.

The dashboard within this planner consists of three main segments <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>:
*   **Summary Segment** – Offers an overall view of income, expenses, and allocation of funds, including quarterly allocation <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.
*   **Income Details** – Provides specifics on actual versus estimated income, quarterly income overview, and frequency of income <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.
*   **Expense Details** – Shows actual versus budgeted expenses, quarterly expense overview, and types of expenses <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>.

### Setting Up the Budget Tracker

To use this budget planner, a Notion account is required <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>. The setup involves three simple steps <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>:
1.  **Filling out Income Details** – For each month <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.
2.  **Filling out Expense Details** – For each individual month <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.
3.  **Allocating Available Funds** – Distributing income minus expenses for each month into different allocations <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.

#### Income Details Setup

To begin, an inline database is created within Notion <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>. This database includes several columns for [[analyzing_income_sources_and_earnings | income analysis]] <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>:
*   **Income Details** – Specifies each individual income earned in a month <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
*   **Source of Income** – Categorizes income (e.g., salary, side hustle, other sources) <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>. This column uses a relation property linking to an "income type" database for detailed analysis <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.
*   **Month of Income** – Indicates the month an income is earned <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>. This also uses a relation property linking to a "month of income" database <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.
*   **Frequency of Income** – Specifies how often income is earned (e.g., recurring, one-time) <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>. This is linked to a "frequency of income" database <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.
*   **Expected Income** – The anticipated income for a month, a number property set to a currency format like US dollars <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.
*   **Actual Income** – The income actually earned at the end of a month, also a number property <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>.
*   **Difference** – A formula property calculating the difference between actual and expected income <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.

#### Analyzing Income Data

For comprehensive [[analyzing_financial_data_through_notion_templates | financial analysis]] in Notion, the `relation` and `roll-up` properties are extensively used <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>.
*   **Actual vs. Estimated Income** – A linked database called "income variance distribution" provides total actual income, total estimated income, their difference, and percentage change for each income type <a class="yt-timestamp" data-t="00:15:25">[00:15:25]</a>. This involves using `roll-up` to pull actual and expected income from the original database and then summing them <a class="yt-timestamp" data-t="00:08:51">[00:08:51]</a>.
*   **Quarterly Income Overview** – The "month of income" database is linked and set to a gallery view, filtered by quarter (e.g., Q1 for Jan, Feb, Mar) <a class="yt-timestamp" data-t="00:15:40">[00:15:40]</a>. It displays total actual income and the proportion of actual to budgeted income for each month <a class="yt-timestamp" data-t="00:06:59">[00:06:59]</a>. A formula calculates the percentage of budgeted income by dividing total actual income by total expected income <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>.
*   **Frequency of Income** – The "frequency of income" database is linked and set to a list view <a class="yt-timestamp" data-t="00:16:15">[00:16:15]</a>. It shows total actual income for recurring or one-time incomes, and their proportion to total income <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>. A formula divides the total income of each mode by the total actual income to get the percentage <a class="yt-timestamp" data-t="00:12:50">[00:12:50]</a>.

#### Expense Details Setup

The expense details are calculated within a single database <a class="yt-timestamp" data-t="00:17:17">[00:17:17]</a>, similar to income, with the following columns <a class="yt-timestamp" data-t="00:17:19">[00:17:19]</a>:
*   **Expense Source** – Details what the expense is for <a class="yt-timestamp" data-t="00:17:21">[00:17:21]</a>.
*   **Month of Expense** – The month an expense is incurred, linked to another database <a class="yt-timestamp" data-t="00:17:26">[00:17:26]</a>.
*   **Expense Classification** – Segregates expenses into categories like utilities, loans, food, entertainment, etc., linked to another database <a class="yt-timestamp" data-t="00:17:36">[00:17:36]</a>.
*   **Expense Type** – Specifies if the expense is variable or fixed, linked to a "type of expense" database <a class="yt-timestamp" data-t="00:17:56">[00:17:56]</a>.
*   **Budgeted Expense** – The expected expense for a month <a class="yt-timestamp" data-t="00:18:06">[00:18:06]</a>.
*   **Actual Expense** – The actual expense for a month <a class="yt-timestamp" data-t="00:18:15">[00:18:15]</a>.
*   **Difference** – The difference between actual and budgeted expenses <a class="yt-timestamp" data-t="00:18:23">[00:18:23]</a>. A positive difference means actual was less than budgeted, while negative means actual was more <a class="yt-timestamp" data-t="00:18:27">[00:18:27]</a>.

#### Analyzing Expense Data

The expense details section provides similar analysis to the income section <a class="yt-timestamp" data-t="00:16:33">[00:16:33]</a>:
*   **Actual vs. Budgeted Expense** – Linked to an "expense variance analysis" database, providing total budgeted and actual expenses, their difference, and percentage change <a class="yt-timestamp" data-t="00:18:55">[00:18:55]</a>.
*   **Quarterly Expense Overview** – Linked to the "month of expense" database, displaying actual expenses and their proportion to budgeted expenses for each month within quarters <a class="yt-timestamp" data-t="00:19:26">[00:19:26]</a>.
*   **Type of Expenses** – Segregates expenses into variable and fixed, showing total actual expenses for each type and their proportion to the total expense <a class="yt-timestamp" data-t="00:19:48">[00:19:48]</a>.

### Analyzing Fund Allocation

Once income and expense details are complete, the next step is [[analyzing_income_and_expenses_with_the_dashboard | allocating available funds]] <a class="yt-timestamp" data-t="00:21:25">[00:21:25]</a>.
*   **Total Available Funds** – Calculated as income less expenses, showing the remaining amount for each month <a class="yt-timestamp" data-t="00:21:31">[00:21:31]</a>.
*   **Allocation of Funds** – The available funds are allocated to different heads like investments, savings, and others <a class="yt-timestamp" data-t="00:21:51">[00:21:51]</a>.
*   **Total Allocation** – The sum of investments, savings, and other allocations <a class="yt-timestamp" data-t="00:22:01">[00:22:01]</a>.
*   **Percentage of Allocation** – Calculated as the total allocation divided by the total available funds <a class="yt-timestamp" data-t="00:22:28">[00:22:28]</a>.

#### Fund Allocation Overviews

Two main overviews provide insights into fund distribution:
*   **Fund Allocation Overview** – Provides an analysis of remaining funds allocated to different heads (e.g., investments, savings, others) <a class="yt-timestamp" data-t="00:20:29">[00:20:29]</a>. This is linked to the "allocation of funds" database, showing the investment source, allocation amount, and percentage of allocation for each month <a class="yt-timestamp" data-t="00:23:22">[00:23:22]</a>.
*   **Quarterly Allocation Overview** – Shows a monthly allocation overview, detailing total available funds for each month and the proportion of funds allocated, broken down by quarters <a class="yt-timestamp" data-t="00:20:59">[00:20:59]</a>. This is linked to the "available funds" database, displaying the month, total available funds, and percentage of allocation for the individual month <a class="yt-timestamp" data-t="00:23:41">[00:23:41]</a>.

The use of `relation` and `roll-up` properties, along with formulas, allows for detailed analysis of income, expenses, and fund allocation within Notion <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>.