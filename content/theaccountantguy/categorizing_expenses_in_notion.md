---
title: Categorizing Expenses in Notion
videoId: OV1faI8Z6yg
---

From: [[theaccountantguy]] <br/> 

A Notion-based expense tracker allows users to [[Using Notion for expense management | categorize]] and manage their spending effectively [00:01:09]. This system provides an overview of total budgeted and actual expenses, including differences and percentage changes [00:01:15].

## Key Expense Categories

Expenses within this Notion tracker are categorized in several ways for comprehensive analysis:

### Needs, Desires, and Wants
Expenses are primarily categorized into "needs," "desires," and "wants" [00:01:24], [00:04:07]. This classification helps in understanding spending patterns across essential, discretionary, and aspirational categories [00:12:37], [00:12:39].

### Six Heads of Expenses
The tracker also divides expenses into six specific "heads" or sources [00:01:44], [00:02:21], [00:03:12], [00:05:50]. These heads allow for detailed tracking and analysis of different types of expenditures [00:03:52].

### Frequency of Expenses
Expenses are further categorized by how frequently they are incurred [00:02:33], such as:
*   Daily expense [00:02:37]
*   One-time expense [00:02:37]
*   Weekly expense [00:02:39]
*   Monthly expense [00:02:40]
*   Quarterly expense [00:02:41]
*   Half-yearly expense [00:02:41]
*   Annually [00:02:42]

## Databases for Categorization

To enable expense categorization and tracking, the Notion system utilizes several interconnected databases [00:02:54]:

### 1. Expense Details Database
This database serves as the foundation, capturing individual expense details [00:02:58], [00:04:22].
*   **Expense Details** (Title property): Shows individual expenses incurred [00:04:27], [00:04:31].
*   **Period of Expense** (Relation property): Links to the `Period of Expense` database, specifying the month an expense was incurred [00:04:36], [00:04:40].
*   **Expense Source** (Relation property): Connects to the `Expense Source` database, indicating under which of the six heads an expense falls [00:04:46], [00:04:48].
*   **Frequency of Expense** (Relation property): Relates to the `Frequency of Expense` database, indicating how often an expense occurs [00:04:57], [00:05:01].
*   **Expense Categories** (Relation property): Links to the `Expense Categories` database, assigning each expense to a "needs," "wants," or "desires" category [00:05:07], [00:05:09].
*   **Actual Expense** (Number property): Records the actual amount incurred in USD [00:05:15], [00:05:17], [00:05:24].
*   **Budgeted Expense** (Number property): Records the estimated budgeted amount for each month in USD [00:05:27], [00:05:31].

### 2. Expense Categories Database
This database reflects the "needs," "wants," and "desires" classifications [00:04:04], [00:04:07], [00:12:35].
*   **Title Property**: Specifies the category (needs, wants, desires) [00:12:44], [00:12:46].
*   **Relation to Expense Details**: Captures all expenses linked to specific categories [00:12:48], [00:12:50].
*   **Expenses Amount** (Roll-up property): Calculates the sum of actual expenses for each category from the `Expense Details` database [00:12:57], [00:13:00].
*   **Total Expenses** (Roll-up property): Derives the sum of all combined expenses from the `Total Expenses` database [00:13:12], [00:13:15].

### 3. Expense Source Database
This database specifies the six different sources or heads of expenses [00:03:08], [00:05:48], [00:05:50].
*   **Source of Expense** (Title property): Identifies one of the six expense heads [00:05:54], [00:05:57].
*   **Actual Expense** (Roll-up property): Sums actual expense amounts from the `Expense Details` database for each source [00:06:04], [00:06:07].
*   **Budgeted Expense** (Roll-up property): Sums budgeted expense amounts from the `Expense Details` database for each source [00:06:14], [00:06:17].
*   **Total Expenses** (Roll-up property): Extracts total actual expenses from the `Total Expenses` database [00:06:25], [00:06:27].
*   **Difference** (Formula property): Shows the difference between actual and budgeted expenses [00:06:40], [00:06:42].
*   **Change in Percentage** (Formula property): Calculates the difference divided by the budgeted expense, displayed as a percentage [00:06:51], [00:06:53], [00:07:01].

### 4. Frequency of Expenses Database
This database tracks how often an expense is incurred [00:03:18], [00:07:12].
*   **Frequency** (Title property): Denotes the mode of frequency (e.g., daily, weekly) [00:07:20], [00:07:22].
*   **Relation to Expense Details**: Relates different types of expenses from the `Expense Details` database to their frequency [00:07:26], [00:07:27].
*   **Sources of Expense** (Formula property): Calculates the unique sources of expenses for each frequency type [00:07:35], [00:07:37].

### 5. Expense Budget Classification Database
This database classifies expenses under the six heads and provides details on actual, budgeted, difference, and percentage change for each [00:03:51], [00:10:47].
*   **Title property**: Specifies the required properties [00:11:00], [00:11:02].
*   **Relation to Expense Source**: Links to the `Expense Source` database for individual expense heads [00:11:06], [00:11:08].
*   **Amount** (Formula property): Derives total actual expenses, total budgeted expenses, and the difference for each head [00:11:13], [00:11:17].
*   **Change in Percentage** (Formula property): Calculates the difference divided by the budgeted expense for each head [00:11:38], [00:11:40].
*   **Roll-up properties**: Derived from the `Expense Source` database to show actual expenses, budgeted expenses, difference, and change in percentage [00:11:45], [00:11:53], [00:12:11], [00:12:21].

## Overview and Analysis

The main dashboard of the expense tracker integrates these databases to present a comprehensive financial overview [00:01:13], [00:13:28]:
*   **Overview of Total Expenses**: Linked to the `Total Expenses` database and displayed in a gallery view, showing total budgeted, actual, differences, and percentage changes [00:01:15], [00:13:32], [00:13:35].
*   **Three Categories of Expenses**: Displays the "needs, wants, and desires" categories, linked to the `Expense Categories` database in a three-column gallery format [00:01:24], [00:13:43], [00:13:45], [00:13:52].
*   **Top 10 Highlights**: Linked to the `Expense Details` database in a list format, sorted to reflect top 10 expenses (descending actual expense), least 10 expenses (ascending actual expense), and recent expenses (descending created time) [00:01:27], [00:13:57], [00:14:03], [00:14:07].
*   **Actual vs. Budgeted Expenses**: Linked to the `Expense Budget Classification` database in a gallery format, showcasing performance against budget for each expense head [00:01:41], [00:14:25], [00:14:27].
*   **Expenses Overview (Monthly)**: Linked to the `Period` database in a gallery format, showing monthly expenses categorized into four quarters [00:01:58], [00:14:36], [00:14:42].
*   **Expenses Overview (Percentage by Head)**: Linked to the `Expense Source` database in a gallery format, providing a percentage breakdown for the six heads of expenses [00:02:17], [0:14:55], [0:14:56].
*   **Frequency of Expenses**: Linked to the `Frequency of Expense` database in a gallery format, displaying expenses based on their recurrence (daily, weekly, etc.) [00:02:32], [00:15:05], [00:15:07].

This structured approach to [[Setting and managing expense categories in Notion | setting and managing expense categories in Notion]] allows for effective [[Budgeting and tracking expenses in Notion | budgeting and tracking expenses in Notion]], providing clear insights into spending habits and financial performance [00:01:09], [00:01:13].