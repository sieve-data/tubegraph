---
title: Database setup for Notion bills tracker
videoId: RqN1qUpTkSI
---

From: [[theaccountantguy]] <br/> 

To [[Setting up a personal finance tracker using Notion | set up a personal finance tracker using Notion]] and [[Using Notion for bill tracking | track bills]] efficiently, the Notion bills tracker primarily uses one main database and several supplemental databases <a class="yt-timestamp" data-t="02:12:35">[02:12:35]</a>. These databases store information related to bills and generate desired financial insights <a class="yt-timestamp" data-t="02:18:20">[02:18:20]</a>.

## Bills Details Database

This is the primary database for the tracker <a class="yt-timestamp" data-t="02:14:55">[02:14:55]</a>. It contains detailed information for each expense:

*   **Description:** States the description related to any expense <a class="yt-timestamp" data-t="02:29:26">[02:29:26]</a>.
*   **Category:** Classifies the expense into one of six categories <a class="yt-timestamp" data-t="02:33:14">[02:33:14]</a>.
*   **Priorities:** Assigns a priority level (low, medium, or high) to the expense <a class="yt-timestamp" data-t="02:38:15">[02:38:15]</a>.
*   **Type of Expense:** Specifies the payment frequency (daily, weekly, monthly, etc.) <a class="yt-timestamp" data-t="02:43:24">[02:43:24]</a>.
*   **Bill Date:** The date of occurrence of the expense <a class="yt-timestamp" data-t="02:49:17">[02:49:17]</a>.
*   **Due Date:** The expected repayment date for bills <a class="yt-timestamp" data-t="02:52:58">[02:52:58]</a>.
*   **Budgeted Expense:** States the allocated budget for the expense <a class="yt-timestamp" data-t="02:55:53">[02:55:53]</a>.
*   **Actual Expense:** Reflects the actual amount incurred <a class="yt-timestamp" data-t="03:01:23">[03:01:23]</a>.
*   **Status of Payment:** A checkbox that, when clicked, updates the status to 'paid' <a class="yt-timestamp" data-t="03:04:33">[03:04:33]</a>.

The Category, Priority, and Expense Type properties are linked to other databases for presentation in the [[primary_dashboard_of_notion_bills_tracker | primary dashboard]] <a class="yt-timestamp" data-t="03:16:11">[03:16:11]</a>.

## Bills Frequency Database

This database organizes bills based on their payment periodicity <a class="yt-timestamp" data-t="03:24:48">[03:24:48]</a>. It includes:

*   **Budgeted Expense:** A roll-up property from the Bills Details Database, deriving the budgeted expense value <a class="yt-timestamp" data-t="03:31:39">[03:31:39]</a>.
*   **Actual Expense:** Another roll-up property from the Bills Details Database, deriving the actual expense value <a class="yt-timestamp" data-t="03:40:53">[03:40:53]</a>.
*   **Change:** A formula property calculating the difference between budgeted expense and actual expense <a class="yt-timestamp" data-t="03:48:42">[03:48:42]</a>.
*   **Upcoming Bill:** A roll-up property from the Bills Details Database, showing the earliest due date <a class="yt-timestamp" data-t="03:54:20">[03:54:20]</a>.
*   **Bills Paid:** A roll-up property that counts the number of bills marked as paid (checked condition) <a class="yt-timestamp" data-t="04:03:34">[04:03:34]</a>.
*   **Total Bills:** A roll-up property from the 'Description' column of the Bills Details Database, counting all bills <a class="yt-timestamp" data-t="04:13:58">[04:13:58]</a>.
*   **Bills Paid in Percentage:** A formula calculating 'bills paid' divided by 'total bills' <a class="yt-timestamp" data-t="04:21:40">[04:21:40]</a>.
*   **Text Formula:** A formula with an `if` condition to show how many bills have been paid from the total, in text format <a class="yt-timestamp" data-t="04:27:54">[04:27:54]</a>.

## Bills Category Database and Bills Priority Database

These two supplemental databases help categorize and prioritize bills <a class="yt-timestamp" data-t="04:43:26">[04:43:26]</a>:

*   **Bills Category Database:** Divides bills into six categories: entertainment, food and groceries, utility bills, travel and transportation, loans and debts, and others <a class="yt-timestamp" data-t="01:33:23">[01:33:23]</a>, <a class="yt-timestamp" data-t="04:45:10">[04:45:10]</a>.
*   **Bills Priority Database:** Classifies bills into three priorities: low, medium, and high <a class="yt-timestamp" data-t="01:21:05">[01:21:05]</a>, <a class="yt-timestamp" data-t="04:50:54">[04:50:54]</a>.

Both databases extract three key pieces of information using methods similar to those used in the Bills Frequency Database <a class="yt-timestamp" data-t="04:55:54">[04:55:54]</a>:

*   Number of bills paid <a class="yt-timestamp" data-t="04:57:38">[04:57:38]</a>
*   Actual expenses incurred <a class="yt-timestamp" data-t="04:59:45">[04:59:45]</a>
*   Bills paid in percentage <a class="yt-timestamp" data-t="05:01:27">[05:01:27]</a>

## Integration for the [[Primary dashboard of Notion bills tracker | Primary Dashboard]]

These databases are fundamental for building the [[Primary dashboard of Notion bills tracker | primary dashboard]] of the [[Setting up Notion for Invoice Management | Notion bills tracker]] <a class="yt-timestamp" data-t="05:44:03">[05:44:03]</a>. They feed data to sections such as:

*   **[[Summary section of Notion bills tracker | Summary Section]]:** Displays upcoming bills, past due bills, and bills paid, along with amounts, due dates, days left/past due, and payment status <a class="yt-timestamp" data-t="00:55:10">[00:55:10]</a>, <a class="yt-timestamp" data-t="05:53:14">[05:53:14]</a>.
*   **Bills Distribution by Priority:** Shows low, medium, and high priority bills with incurred expenses and percentage paid <a class="yt-timestamp" data-t="06:27:32">[06:27:32]</a>.
*   **Bills Distribution by Category:** Breaks down bills by categories like entertainment or utilities, showing total expense and percentage paid <a class="yt-timestamp" data-t="06:35:46">[06:35:46]</a>.
*   **Bills Distribution by Period:** Divides bills by daily, weekly, monthly, quarterly, half-yearly, annually, and one-time expenses, reflecting budgeted vs. actual expenses, change, upcoming bills, bills paid, and bills paid in percentage <a class="yt-timestamp" data-t="01:47:34">[01:47:34]</a>, <a class="yt-timestamp" data-t="06:52:50">[06:52:50]</a>.

[[Using databases for financial tracking in Notion | Using databases in Notion for invoice tracking]] allows for a comprehensive [[Monthly budget planner setup using Notion | monthly budget planner setup using Notion]] and detailed financial oversight <a class="yt-timestamp" data-t="02:18:20">[02:18:20]</a>.