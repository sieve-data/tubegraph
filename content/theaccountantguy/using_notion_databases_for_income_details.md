---
title: Using Notion databases for income details
videoId: C9gr5yS8EPc
---

From: [[theaccountantguy]] <br/> 

[[using_notion_for_personal_finance | Notion]] can be used to create a minimalistic budget planner dashboard to [[using_notion_for_financial_tracking | keep track of income and expenses]] in one central location <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>. This dashboard allows users to fix monthly income goals, categorize expenses, and set and monitor monthly budgets <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>. The budget tracker is accessible from any device <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.

The dashboard consists of three main segments:
*   **Summary** – Provides an overall view of income, expenses, and fund allocation <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.
*   **Income Details** – Shows details of actual versus estimated income, quarterly income overview, and frequency of income <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.
*   **Expense Details** – Presents details of actual versus budgeted expenses, quarterly expense overview, and type of expenses <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>.

To begin, users need to sign up for a [[using_notion_for_personal_finance_management | Notion]] account <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>.

## Setting up the Income Details Database

The first step in setting up the budget tracker is filling out the income details <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.

### Creating an Inline Database
An inline database, named "Expected Income Source Details", is used to capture income information <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>. It can be created by typing `/` and then `database`, selecting "database inline" <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>. The database title can be made visible and edited by clicking the three dots (`...`), navigating to "Layout options," and selecting "Show database title" <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>.

### Columns in the Income Database
The inline database for income details includes the following columns:
*   **Income Details** – The default property for any inline database, specifying each individual income earned in a month <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
*   **Source of Income** – A relation property linked to another database (e.g., "Income Type" database) that categorizes income, such as "Salary," "Side Hustle," and "Other Sources of Income" <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.
*   **Month of Income** – A relation property linked to a "Month of Income" database, indicating the month when income is earned <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.
*   **Frequency of Income** – A relation property linked to a "Frequency of Income" database, specifying how often income is earned (e.g., "recurring" or "one-time") <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.
*   **Expected Income** – A number property (e.g., US dollars) for the anticipated income for a given month <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.
*   **Actual Income** – A number property (e.g., US dollars) for the income actually earned at the end of the month <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>.
*   **Difference** – A formula type property that calculates the difference between actual income and expected income <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>.

## Analyzing Income Data with Relation and Roll-Up Properties
[[creating_a_database_in_notion_for_calculations | Relation]] and [[notion_database_setup_for_calculations | roll-up properties]] are crucial for detailed analysis of income data <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>.

### Actual vs. Estimated Income by Source
The income details section provides an "Actual versus Estimated Income" overview <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>. This displays total actual income, total estimated income, the difference between them, and the percentage change for each income source (e.g., salary, side hustle, other sources) <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>.

To achieve this, the primary income database is related to an "Income Type" database <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>. This "Income Type" database contains roll-up properties that:
*   Pull the actual income from the original database and calculate the sum for each income type <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>.
*   Pull the expected income from the original database and calculate the sum for each income type <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>.
*   Calculate the difference and percentage change using formulas based on the rolled-up values <a class="yt-timestamp" data-t="00:13:49">[00:13:49]</a>.

### Quarterly Income Overview
This section displays total actual income and the proportion of actual income to budgeted income for each month, divided into four quarters <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>.

A relation is established with a "Month of Income" database <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>. This database uses roll-up properties to calculate:
*   Total expected income for each month <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a>.
*   Total actual income for each month <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a>.
*   The proportion of actual income to budgeted income (Actual Income / Expected Income) as a percentage <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>.

### Frequency of Income Analysis
This section shows how frequently income is earned (recurring or one-time) and the total actual income and its proportion for each frequency type <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>.

This analysis relies on a relation to a "Frequency of Income" database <a class="yt-timestamp" data-t="00:11:35">[00:11:35]</a>. This database uses roll-up properties to determine:
*   Total actual income for recurring and one-time income <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>.
*   Total expected income for each mode <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>.
*   The proportion of each form of income to the total actual income <a class="yt-timestamp" data-t="00:12:37">[00:12:37]</a>.

## Linking Databases for Dashboard Views
To display these analyses on the main dashboard, linked databases are used <a class="yt-timestamp" data-t="00:14:45">[00:14:45]</a>. A linked database can be created by typing `/` and then `link database` <a class="yt-timestamp" data-t="00:15:02">[00:15:02]</a>.

*   **Actual versus Estimated Income** – Links to the "Income Variance Distribution" database <a class="yt-timestamp" data-t="00:15:22">[00:15:22]</a>.
*   **Quarterly Income Overview** – Links to the "Month of Income" database and is set to a gallery view <a class="yt-timestamp" data-t="00:15:38">[00:15:38]</a>. Filters are applied for each quarter (e.g., Q1 for Jan, Feb, Mar) <a class="yt-timestamp" data-t="00:15:46">[00:15:46]</a>.
*   **Frequency of Income** – Links to the "Frequency of Income" database and is set to a list view <a class="yt-timestamp" data-t="00:16:13">[00:16:13]</a>.

These steps complete the [[notion_income_tracker_setup | income details setup]] in the primary dashboard <a class="yt-timestamp" data-t="00:16:28">[00:16:28]</a>.