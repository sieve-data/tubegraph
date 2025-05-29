---
title: Establishing Links and Relationships Between Databases in Notion
videoId: C9gr5yS8EPc
---

From: [[theaccountantguy]] <br/> 

[[Setting up databases and relationships in Notion | Setting up databases and relationships in Notion]] in Notion is crucial for creating comprehensive dashboards and gaining detailed insights from your data <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>. This process involves establishing connections between different databases and utilizing specific properties like "Relation" and "Roll-up" to pull and analyze related information <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>.

## Why Establish Database Relationships?
Establishing relationships between databases offers several benefits:
*   **Enhanced Analysis** <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>: It helps in specifying and analyzing various aspects of your data, such as calculating total actual income for a specific source <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a> or total expenses for a particular month <a class="yt-timestamp" data-t="00:19:26">[00:19:26]</a>.
*   **Centralized Tracking** <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>: You can keep track of various income and expenses in one central location <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>.
*   **Performance Assessment** <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>: Monitor monthly income goals to assess overall performance <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.
*   **Categorization for Improvement** <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>: Categorize expenses to identify areas for improvement <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.

## Basic Setup: [[Creating a database in Notion | Creating an Inline Database]]
To begin, you typically need to [[creating_a_database_in_notion | create a database]].
1.  Type `/` (forward slash) in Notion <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.
2.  Type `database` and select `Database - Inline` <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.
3.  Fill out the required details for your database columns <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>.
    *   The first column is typically a "Title" type property, which is the default for any inline database <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.
    *   You can name the database by clicking the three dots (`...`), then `Layout` options, and ensuring `Show database title` is enabled to edit the title <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>.

### Example Database Columns (Income Details)
For an income details database, typical columns might include:
*   **Income Details (Title property)**: Specifies individual income entries <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>.
*   **Source of Income**: A category of income, such as salary, side hustle, or other sources <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>. This often becomes a "Relation" property <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.
*   **Month of Income**: The specific month an income is earned <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>. This can also be a "Relation" property <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>.
*   **Frequency of Income**: How frequently income is earned (e.g., recurring, one-time) <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>. Another "Relation" property <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.
*   **Expected Income**: A "Number" property, formatted as currency (e.g., US dollars) <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.
*   **Actual Income**: A "Number" property, formatted as currency <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.
*   **Difference**: A "Formula" property that calculates the difference between actual and expected income <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>.

## Establishing Relations Between Databases
The "Relation" property is key to [[setting_up_databases_and_relationships_in_notion | setting up relationships]]. It allows you to link records from one database to records in another <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.

### How to Set a Relation Property
1.  Add a new property to your database <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.
2.  Select "Relation" as the property type <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.
3.  Choose the database you want to relate to (e.g., "Income Type" database for "Source of Income" column) <a class="yt-timestamp" data-t="00:08:05">[00:08:05]</a>.
4.  Ensure the databases are linked both ways for full functionality <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>.

## Using the Roll-up Property for Analysis
Once a relation is established, the "Roll-up" property allows you to pull and aggregate specific information from the related database <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>. This is part of [[creating_custom_formulas_and_linking_databases_in_notion | creating custom formulas and linking databases in Notion]].

### How to Set a Roll-up Property
1.  Add a new property to your database <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>.
2.  Select "Roll-up" as the property type <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>.
3.  **Relation**: Specify the relation property (e.g., "Source of Income") that links to the original database <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>.
4.  **Property**: Select the desired property from the *original* database that you want to pull (e.g., "Actual Income" or "Expected Income") <a class="yt-timestamp" data-t="00:08:45">[00:08:45]</a>.
5.  **Calculate**: Choose the aggregation method (e.g., "Sum" to get the total, "Average," "Count," etc.) <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>.

### Examples of Roll-up Use
*   **Total Actual Income by Source**: In an "Income Type" database, you can use a Roll-up to sum the "Actual Income" from the main "Income Details" database for each income source (e.g., Salary, Side Hustle) <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>.
*   **Expected Income by Month**: In a "Month of Income" database, a Roll-up can sum the "Expected Income" for each month from the main income database <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a>.
*   **Expense Analysis**: Similar roll-ups can be used for expense details to calculate total budgeted or actual expenses by category or month <a class="yt-timestamp" data-t="00:18:51">[00:18:51]</a>.

## Linking Existing Databases to a Dashboard
For a comprehensive overview, you can link existing databases to a main dashboard page. This provides summarized views without duplicating data <a class="yt-timestamp" data-t="00:14:47">[00:14:47]</a>.

### How to Create a Linked Database View
1.  Type `/` (forward slash) on your dashboard page <a class="yt-timestamp" data-t="00:15:05">[00:15:05]</a>.
2.  Type `link database` and select `Linked view of an existing database` <a class="yt-timestamp" data-t="00:15:07">[00:15:07]</a>.
3.  Choose the database you want to link (e.g., "Income Variance Distribution" for actual vs. estimated income) <a class="yt-timestamp" data-t="00:15:27">[00:15:27]</a>.
4.  You can then customize the view (e.g., "Gallery" mode <a class="yt-timestamp" data-t="00:15:44">[00:15:44]</a>, "List" mode <a class="yt-timestamp" data-t="00:16:19">[00:16:19]</a>) and filter properties to display only relevant information for your dashboard section <a class="yt-timestamp" data-t="00:16:02">[00:16:02]</a>.

### Dashboard Sections Using Linked Databases (Budget Planner Example)
*   **Summary Segment**: Gives an overall view of income, expenses, and fund allocation <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.
*   **Income Details**:
    *   **Actual vs. Estimated Income**: Linked to an "Income Variance Distribution" database to show total actual income, total estimated income, difference, and percentage change <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>.
    *   **Quarterly Income Overview**: Linked to a "Month of Income" database, filtered by quarters (e.g., Q1: Jan, Feb, Mar) <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>.
    *   **Frequency of Income**: Linked to a "Frequency of Income" database to show total actual income for recurring or one-time income <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>.
*   **Expense Details**: Similar to income, with sections for actual vs. budgeted expense, quarterly expense overview, and type of expenses (variable/fixed) <a class="yt-timestamp" data-t="00:16:33">[00:16:33]</a>.
*   **Fund Allocation**: Shows available funds (income minus expenses) allocated to different heads like investments, savings, and others <a class="yt-timestamp" data-t="00:20:22">[00:20:22]</a>.

By effectively [[creating_and_using_databases_in_notion | creating and using databases in Notion]] and linking them through relations and roll-ups, you can build a powerful and organized system for [[using_databases_for_financial_tracking_in_notion | financial tracking]] or any other data management need.