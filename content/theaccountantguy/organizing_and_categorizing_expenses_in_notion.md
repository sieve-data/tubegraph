---
title: Organizing and categorizing expenses in Notion
videoId: C9gr5yS8EPc
---

From: [[theaccountantguy]] <br/> 
[[organizing_financial_transactions_in_notion | Organizing and categorizing expenses in Notion]] is a key component of creating a minimalistic budget planner in Notion <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>. This dashboard allows users to [[tracking_expenses_and_income_in_notion | track expenses]] in one central location <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>, [[customizing_expense_categories_in_notion | categorize expenses]] to identify areas for improvement <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>, and set and monitor monthly budgets for different categories <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.

The budget planner includes an "Expense Details" segment <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>, which provides details on actual versus budgeted expenses <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>, a quarterly expense overview <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>, and types of expenses <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>.

### Setting Up Expense Tracking
To set up expense tracking, one of the three main steps for the budget planner is [[managing_business_expenses_in_notion | filling out the expense details]] for each individual month <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>. This is done within a central database <a class="yt-timestamp" data-t="00:17:17">[00:17:17]</a>.

#### Expense Database Columns
The expense database includes several columns to facilitate [[creating_and_categorizing_expenses_in_notion | organizing financial transactions in Notion]]:
*   **Expense Source** This column specifies the details of each expense incurred <a class="yt-timestamp" data-t="00:17:19">[00:17:19]</a>. It is set as a title type property <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>.
*   **Month of Expense** This specifies the month in which an expense is incurred <a class="yt-timestamp" data-t="00:17:26">[00:17:26]</a>. This column has a relation property linked to a separate "month of expense" database <a class="yt-timestamp" data-t="00:17:30">[00:17:30]</a>.
*   **Expense Classification** This categorizes expenses into six main heads <a class="yt-timestamp" data-t="00:17:36">[00:17:36]</a>:
    *   Utility and bills <a class="yt-timestamp" data-t="00:17:43">[00:17:43]</a>
    *   Others <a class="yt-timestamp" data-t="00:17:43">[00:17:43]</a>
    *   Loans and debts <a class="yt-timestamp" data-t="00:17:44">[00:17:44]</a>
    *   Food and groceries <a class="yt-timestamp" data-t="00:17:45">[00:17:45]</a>
    *   Entertainment <a class="yt-timestamp" data-t="00:17:46">[00:17:46]</a>
    *   Travel and transportation <a class="yt-timestamp" data-t="00:17:47">[00:17:47]</a>
    This column is linked to another database via a relation property <a class="yt-timestamp" data-t="00:17:49">[00:17:49]</a>.
*   **Expense Type** Expenses are further segregated as variable or fixed <a class="yt-timestamp" data-t="00:17:56">[00:17:56]</a>. This also uses a relation property linked to a "type of expense" database <a class="yt-timestamp" data-t="00:18:00">[00:18:00]</a>.
*   **Budgeted Expense** A number property that sets the expected expense for a particular month, typically in US dollars <a class="yt-timestamp" data-t="00:18:06">[00:18:06]</a>.
*   **Actual Expense** A number property that records the actual expense incurred for a particular month, also typically in US dollars <a class="yt-timestamp" data-t="00:18:15">[00:18:15]</a>.
*   **Difference** A formula type property that calculates the difference between actual and budgeted expenses <a class="yt-timestamp" data-t="00:18:23">[00:18:23]</a>. A positive difference means actual expenses were less than budgeted, while a negative difference means actual expenses exceeded the budget <a class="yt-timestamp" data-t="00:18:27">[00:18:27]</a>.

All three categorized columns (Month of Expense, Expense Classification, Expense Type) are linked to different databases to enable deeper analysis <a class="yt-timestamp" data-t="00:18:39">[00:18:39]</a>.

#### Analyzing Expense Data
Similar to income details, [[using_notion_for_expense_management | expense data]] is analyzed using linked databases, relation, and roll-up properties.

*   **Actual vs. Budgeted Expense Overview**: A linked database, "expense variance analysis," displays the total budgeted expense, total actual expense, the difference, and the percentage change for each expense classification <a class="yt-timestamp" data-t="00:18:51">[00:18:51]</a>. This is often presented in a gallery view with key properties visible <a class="yt-timestamp" data-t="00:19:11">[00:19:11]</a>.
*   **Quarterly Expense Overview**: For each individual month, the actual expense incurred and its proportion to the budgeted expense are tracked <a class="yt-timestamp" data-t="00:19:26">[00:19:26]</a>. This is typically a gallery view linked to the "month of expense" database, displaying the month, actual expense, and proportion of actual to budgeted expense <a class="yt-timestamp" data-t="00:19:34">[00:19:34]</a>. Filters are applied for each quarter (e.g., Q1 for Jan, Feb, March) <a class="yt-timestamp" data-t="00:15:46">[00:15:46]</a>.
*   **Type of Expenses (Fixed vs. Variable)**: This section shows the total actual expenses for variable and fixed types, along with their percentage of the total expense <a class="yt-timestamp" data-t="00:19:48">[00:19:48]</a>. It is presented in a list view, linked to the "type of expense" database <a class="yt-timestamp" data-t="00:19:57">[00:19:57]</a>.

This comprehensive approach to [[budgeting_and_expense_management_in_notion | tracking transactions and expenses in Notion]] allows for detailed financial analysis and identification of areas for improvement <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.