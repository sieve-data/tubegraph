---
title: Bills Distribution Categories and Periods
videoId: RqN1qUpTkSI
---

From: [[theaccountantguy]] <br/> 

The Notion Bills Tracker organizes expenses by various distributions, including categories and billing periods, providing detailed insights into spending habits <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.

## Distribution by Categories

Bills are classified into six distinct categories:
*   Entertainment <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>
*   Food and Groceries <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>
*   Utility Bills <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>
*   Travel and Transportation <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>
*   Loans and Debts <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>
*   Others <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>

For each category, the tracker displays the total amount paid and the percentage of bills paid <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>. In the [[notion_database_structure_for_bills_management | Bills Category Database]], three pieces of information are extracted: the number of bills paid, the actual expenses incurred, and the bills paid in percentage <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>.

## Distribution by Periods

Bills are also distributed based on their payment frequency or periods <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. These periods include:
*   Daily <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>
*   Weekly <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>
*   Monthly <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>
*   Quarterly <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>
*   Half-Yearly <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>
*   Annually <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>
*   One-Time <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>

For each period, the dashboard reflects several key metrics:
*   Budgeted Expenses <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>
*   Actual Expenses <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>
*   Change Observed (Budgeted less Actual) <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>
*   Upcoming Bill to be Paid <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>
*   Bills Paid (in numbers) <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>
*   Bills Paid in Percentage <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>

### Bills Frequency Database
The [[notion_database_structure_for_bills_management | Bills Frequency Database]] is specifically designed to manage [[managing_billing_periods_for_subscriptions | bills paid as per different periodicity of expense]] <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>. All values within this database are "rolled up" from the [[notion_database_structure_for_bills_management | Bills Database]], which includes a "type of expense" property for daily, weekly, monthly, or other specified types <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a> <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.

Key metrics in the [[notion_database_structure_for_bills_management | Bills Frequency Database]] include:
*   **Budgeted Expense**: Rolled up from the Bills Database <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.
*   **Actual Expense**: Also rolled up from the Bills Database <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.
*   **Change**: Calculated as budgeted expense less actual expense <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.
*   **Upcoming Bill**: Rolled up from the Bills Database, providing the earliest due date <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>.
*   **Bills Paid**: Rolled up from the Bills Database, counting bills marked as "checked" <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.
*   **Total Bills**: Rolled up from the description column of the Bills Database, counting all bills <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.
*   **Bills Paid in Percentage**: Calculated as (bills paid / total bills) <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>.
*   **Bills Paid (Text Format)**: A formula with an "if" condition calculates how many bills have been paid from the total, displayed as text <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.