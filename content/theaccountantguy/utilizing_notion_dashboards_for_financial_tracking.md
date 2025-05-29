---
title: Utilizing Notion dashboards for financial tracking
videoId: RqN1qUpTkSI
---

From: [[theaccountantguy]] <br/> 

[[creating_a_financial_dashboard_in_notion | Creating a bills tracker in Notion]] allows users to monitor their financial obligations effectively <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>. This system, part of [[creating_dashboards_for_financial_overview_in_notion | creating dashboards for financial overview in Notion]], provides a comprehensive view of bills and their payment statuses, offering a structure for [[using_notion_for_personal_finance_management | personal finance management]] and [[using_notion_for_cash_flow_management | cash flow management]] within Notion.

## Key Sections of the Notion Bills Tracker

The Notion bills tracker dashboard is structured into several key sections to provide a clear financial overview <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>:

### Summary Section
This section offers an immediate overview of bill statuses <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.
*   **Upcoming Bills:** Displays bills with their amount, due date, days remaining to pay, and payment status <a class="yt-timestamp" data-t="00:00:57">[00:01:10]</a>. Clicking on a bill updates its status to "paid" and moves it to the "Bills Paid" section <a class="yt-timestamp" data-t="00:01:12">[00:01:16]</a>.
*   **Past Due Bills:** Shows bills that have exceeded their due date, including the amount, original due date, and number of days past due <a class="yt-timestamp" data-t="00:06:08">[00:06:14]</a>.
*   **Bills Paid:** Lists all bills that have been paid on time, showing the amount, due date, and status <a class="yt-timestamp" data-t="00:06:19">[00:06:23]</a>.

### Bills Distribution by Priority
This section classifies bills by their priority level: low, medium, or high <a class="yt-timestamp" data-t="00:01:22">[00:01:25]</a>. It indicates the amount associated with each priority and the percentage of bills paid within each category <a class="yt-timestamp" data-t="00:01:25">[00:01:28]</a>.

### Bills Distribution by Category
Bills are categorized into six types:
*   Entertainment <a class="yt-timestamp" data-t="00:01:35">[00:01:37]</a>
*   Food and Groceries <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>
*   Utility Bills <a class="yt-timestamp" data-t="00:01:37">[00:01:38]</a>
*   Travel and Transportation <a class="yt-timestamp" data-t="00:01:38">[00:01:39]</a>
*   Loans and Debts <a class="yt-timestamp" data-t="00:01:39">[00:01:42]</a>
*   Others <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>

Each category shows the total amount paid and the percentage of bills paid within that category <a class="yt-timestamp" data-t="00:01:42">[00:01:45]</a>.

### Bills Distribution by Period
Bills are further divided by payment frequency: daily, weekly, monthly, quarterly, half-yearly, annually, and one-time <a class="yt-timestamp" data-t="00:01:47">[00:01:53]</a>. For each period, the tracker displays:
*   Budgeted expenses <a class="yt-timestamp" data-t="00:01:55">[00:01:57]</a>
*   Actual expenses <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>
*   The change observed (difference between budgeted and actual) <a class="yt-timestamp" data-t="00:01:57">[00:01:59]</a>
*   Upcoming bills to be paid <a class="yt-timestamp" data-t="00:01:59">[00:02:00]</a>
*   Number of bills paid <a class="yt-timestamp" data-t="00:02:00">[00:02:02]</a>
*   Percentage of bills paid <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>

## Building the Notion Bills Tracker

To [[creating_a_financial_dashboard_in_notion | build the Notion bills tracker]], the primary requirement is a "Bills database" along with several supplemental databases to store and relate information <a class="yt-timestamp" data-t="00:02:12">[00:02:22]</a>. This approach is fundamental to [[using_databases_in_notion_for_financial_tracking | using databases in Notion for financial tracking]].

### Bills Details Database
This is the core database for [[tracking_income_and_expenses_with_a_notion_dashboard | tracking income and expenses with a Notion dashboard]]. It includes the following columns <a class="yt-timestamp" data-t="00:02:27">[00:02:29]</a>:
*   **Description:** Details about the expense <a class="yt-timestamp" data-t="00:02:29">[00:02:31]</a>.
*   **Category:** One of the six expense categories (e.g., Entertainment, Food) <a class="yt-timestamp" data-t="00:02:33">[00:02:35]</a>.
*   **Priorities:** Low, medium, or high priority for the expense <a class="yt-timestamp" data-t="00:02:38">[00:02:40]</a>.
*   **Type of Expense:** Daily, weekly, monthly, etc. <a class="yt-timestamp" data-t="00:02:43">[00:02:48]</a>.
*   **Bill Date:** Date of expense occurrence <a class="yt-timestamp" data-t="00:02:48">[00:02:51]</a>.
*   **Due Date:** Expected repayment date <a class="yt-timestamp" data-t="00:02:52">[00:02:54]</a>.
*   **Budgeted Expense:** The planned budget for the expense <a class="yt-timestamp" data-t="00:02:54">[00:02:58]</a>.
*   **Actual Expense:** The actual amount incurred <a class="yt-timestamp" data-t="00:03:01">[00:03:03]</a>.
*   **Status of Payment:** A checkbox to indicate if the amount has been paid <a class="yt-timestamp" data-t="00:03:03">[00:03:09]</a>.

Category, Priority, and Expense Type columns are linked to other databases for presentation within the primary dashboard <a class="yt-timestamp" data-t="00:03:16">[00:03:22]</a>.

### Bills Frequency Database
This database tracks bill payments based on their periodicity <a class="yt-timestamp" data-t="00:03:24">[00:03:31]</a>. It uses roll-up properties from the Bills Details Database for:
*   **Budgeted Expense:** Rolled up from the Bills database <a class="yt-timestamp" data-t="00:03:31">[00:03:35]</a>.
*   **Actual Expense:** Rolled up from the Bills database <a class="yt-timestamp" data-t="00:03:40">[00:03:45]</a>.
*   **Change:** Calculated as budgeted expense minus actual expense <a class="yt-timestamp" data-t="00:03:48">[00:03:52]</a>.
*   **Upcoming Bill:** Rolled up from the Bills database, showing the earliest due date <a class="yt-timestamp" data-t="00:03:54">[00:03:58]</a>.
*   **Bills Paid:** Counts the number of bills marked as paid (checked condition in roll-up) <a class="yt-timestamp" data-t="00:04:03">[00:04:09]</a>.
*   **Total Bills:** Counts all bills from the description column of the Bills database <a class="yt-timestamp" data-t="00:04:13">[00:04:20]</a>.
*   **Bills Paid in Percentage:** Calculated as bills paid divided by total bills <a class="yt-timestamp" data-t="00:04:20">[00:04:24]</a>.
*   **Formula for text summary:** An `if` condition calculates how many bills have been paid from total bills in a text format <a class="yt-timestamp" data-t="00:04:27">[00:04:34]</a>.

### Bills Category Database & Bills Priority Database
These two databases categorize bills based on the six categories and three priorities respectively <a class="yt-timestamp" data-t="00:04:44">[00:04:54]</a>. They extract information such as the number of bills paid, actual expenses incurred, and the percentage of bills paid for each category/priority <a class="yt-timestamp" data-t="00:04:55">[00:05:01]</a>.

### Expense Type Database
This database tracks budgeted expenses, actual expenses, change, upcoming bills, bills paid, and bills paid in percentage for each individual type of expense (e.g., daily, weekly, monthly) <a class="yt-timestamp" data-t="00:05:19">[00:05:29]</a>. Values are pulled using a roll-up property from the Bills Details Database <a class="yt-timestamp" data-t="00:05:30">[00:05:34]</a>. These calculations can be replicated for all expense types <a class="yt-timestamp" data-t="00:05:36">[00:05:41]</a>.

These [[components_of_a_notion_financial_dashboard | components of a Notion financial dashboard]] collectively provide a robust system for [[using_notion_for_business_tracking | business tracking]] or personal finance, demonstrating how [[using_notion_templates_for_financial_management | Notion templates for financial management]] can be constructed.