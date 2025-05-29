---
title: Notion Budget Tracker Overview
videoId: C9gr5yS8EPc
---

From: [[theaccountantguy]] <br/> 

The Notion Budget Planner is a minimalistic dashboard designed to help users track their income and expenses in a central location <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. It allows users to fix monthly income goals, categorize expenses to identify areas for improvement, and set and monitor monthly budgets for different categories <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>. The tracker is accessible from any device, anywhere <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.

This template is available for purchase at accountantguy.gumroad.com <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.

## Dashboard Segments

The dashboard is comprised of three main segments:

*   **Summary Segment**
    *   Provides an overall view of income, expenses, and allocation of funds <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.
    *   Includes a summary of income, expenses, fund allocation, and quarterly allocation of funds <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.
*   **Income Details**
    *   Shows details of actual versus estimated income expectations <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.
    *   Provides a quarterly income overview <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.
    *   Indicates the frequency of income <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.
*   **Expense Details**
    *   Offers details of actual versus budgeted expenses <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>.
    *   Includes a quarterly expense overview <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.
    *   Breaks down expenses by type <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>.

## Setting Up the Budget Tracker

To use this template, users need to sign up for a Notion account <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>. The setup process involves three main steps:

1.  **Filling out Income Details** <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>
2.  **Filling out Expense Details** <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>
3.  **Allocating Available Funds** (Income minus Expenses) <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>

## Key Notion Features Utilized

The Notion budget planner leverages several Notion features for comprehensive financial tracking:

*   **Inline Databases**: Used to create structured tables for income and expense entries <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>. Databases can be named by clicking on the three dots, then layout options, and enabling "show database title" <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.
*   **Properties**:
    *   **Title Property**: Default property for database entries, used for income details <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>.
    *   **Number Property**: Used for expected income, actual income, budgeted expense, and actual expense, allowing currency formatting (e.g., US dollars) <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>.
    *   **Relation Property**: Essential for linking different databases (e.g., income details to source of income, month of income, and frequency of income databases) <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>. This allows for better analysis across categories <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.
    *   **Formula Property**: Calculates differences (e.g., actual income minus expected income) <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>, and percentages (e.g., actual income divided by expected income) <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>.
    *   **Roll-up Property**: Used in conjunction with relation properties to aggregate data from linked databases, such as calculating the total actual income for a specific source (e.g., salary) <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>. This property allows pulling specific information (e.g., `actual income`, `expected income`) and performing calculations like `sum` <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>.
*   **Linked Databases**: Used on the main dashboard to display filtered or summarized information from other databases (e.g., [[notion_budget_and_expenses_template | Income Variance Distribution]] for actual vs. estimated income) <a class="yt-timestamp" data-t="00:14:47">[00:14:47]</a>. They are created by typing `/link database` <a class="yt-timestamp" data-t="00:15:05">[00:15:05]</a>.
*   **Layouts**: Databases can be displayed in various layouts such as Gallery mode or List mode <a class="yt-timestamp" data-t="00:15:44">[00:15:44]</a>.

### Income Details Section

*   **Income Details Database**: Columns include Income Details (Title), Source of Income (Relation), Month of Income (Relation), Frequency of Income (Relation), Expected Income (Number, US dollars), Actual Income (Number, US dollars), and Difference (Formula) <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.
*   **Source of Income**: Categories like Salary, Side Hustle, and Other Sources of income are related to an "Income Type" database to calculate totals and variances for each type <a class="yt-timestamp" data-t="00:08:05">[00:08:05]</a>.
*   **Month of Income**: Related to a "Month of Income" database to track expected income, actual income, and the proportion of actual income to budgeted income for each month <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>.
*   **Frequency of Income**: Related to a "Frequency of Income" database to track recurring versus one-time incomes <a class="yt-timestamp" data-t="00:11:37">[00:11:37]</a>.

### Expense Details Section

The expense section mirrors the income section with similar database structures and linked properties:

*   **Expense Details Database**: Columns include Expense Source (Title), Month of Expense (Relation), Expense Classification (Relation), Expense Type (Relation), Budgeted Expense (Number, US dollars), Actual Expense (Number, US dollars), and Difference (Formula) <a class="yt-timestamp" data-t="00:17:17">[00:17:17]</a>.
*   **Expense Classification**: Segregated into categories such as utility and bills, loans and debts, food and groceries, entertainment, travel and transportation, and others <a class="yt-timestamp" data-t="00:17:36">[00:17:36]</a>. These are linked to an "Expense Variance Analysis" database <a class="yt-timestamp" data-t="00:18:57">[00:18:57]</a>.
*   **Expense Type**: Classified as variable and fixed expenses, linked to a "Type of Expense" database <a class="yt-timestamp" data-t="00:17:57">[00:17:57]</a>.

### Allocation of Funds

After tracking income and expenses, the next step is to allocate the available funds (income minus expenses) <a class="yt-timestamp" data-t="00:21:20">[00:21:20]</a>.

*   **Available Funds Database**: Calculates the total available funds for each month using a formula (total income less total expenses) <a class="yt-timestamp" data-t="00:21:41">[00:21:41]</a>.
*   **Fund Allocation Overview**: Funds are allocated to different heads such as Investment, Savings, and Others <a class="yt-timestamp" data-t="00:20:34">[00:20:34]</a>. The total allocated amount and its proportion to the total available funds are calculated <a class="yt-timestamp" data-t="00:20:51">[00:20:51]</a>.
*   **Quarterly Allocation Overview**: Provides a monthly allocation overview showing total available funds and the proportion of funds allocated for each month, broken down by quarters <a class="yt-timestamp" data-t="00:20:59">[00:20:59]</a>.