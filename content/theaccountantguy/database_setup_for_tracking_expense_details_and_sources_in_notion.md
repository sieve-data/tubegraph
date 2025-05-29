---
title: Database setup for tracking expense details and sources in Notion
videoId: OV1faI8Z6yg
---

From: [[theaccountantguy]] <br/> 

To [[how_to_build_an_expense_tracker_in_notion | build an expense tracker]] in Notion, seven databases are required <a class="yt-timestamp" data-t="02:54:02">[02:54:02]</a>. This article focuses on the setup of the "Expense Details" and "Expense Source" databases.

## Expense Details Database

This database is used to specify details related to each individual expense incurred during a period <a class="yt-timestamp" data-t="02:59:58">[02:59:58]</a>.

### Properties

*   **Expense Details** (Title Property): Shows individual expenses <a class="yt-timestamp" data-t="04:27:54">[04:27:54]</a>.
*   **Period of Expense** (Relation Property): Links to the "Period Database," specifying the individual month for which an expense is incurred <a class="yt-timestamp" data-t="04:36:47">[04:36:47]</a>.
*   **Expense Source** (Relation Property): Links to the "Expense Source Database," specifying the source category under which an expense is incurred <a class="yt-timestamp" data-t="04:46:16">[04:46:16]</a>.
*   **Frequency of Expense** (Relation Property): Links to the "Frequency of Expense Database," indicating how frequently an expense is incurred <a class="yt-timestamp" data-t="04:57:43">[04:57:43]</a>.
*   **Expense Categories** (Relation Property): Links to the "Expense Categories Database," specifying the category (needs, wants, or desires) for each individual source of expense <a class="yt-timestamp" data-t="05:07:37">[05:07:37]</a>.
*   **Actual Expense** (Number Property): Specifies the actual amount of expense incurred for the period, indicated in US dollars <a class="yt-timestamp" data-t="05:15:32">[05:15:32]</a>.
*   **Budgeted Expense** (Number Property): Represents the budgeted expense estimated for each month, specified in US dollars <a class="yt-timestamp" data-t="05:27:46">[05:27:46]</a>.

At the bottom of this database, the sum of actual and budgeted expenses can be found <a class="yt-timestamp" data-t="05:34:04">[05:34:04]</a>.

## Expense Source Database

This database specifies the six different sources under which an expense is incurred <a class="yt-timestamp" data-t="05:48:19">[05:48:19]</a>.

### Properties

*   **Source of Expense** (Title Property): Specifies one of the six heads of expenses <a class="yt-timestamp" data-t="05:54:33">[05:54:33]</a>.
*   **Actual Expense** (Roll-up Property): Derived from the "Expense Details" database, providing the sum of actual expense amounts <a class="yt-timestamp" data-t="06:04:49">[06:04:49]</a>.
*   **Budgeted Expense** (Roll-up Property): Derived from the "Expense Details" database, providing the sum of budgeted expense amounts <a class="yt-timestamp" data-t="06:14:02">[06:14:02]</a>.
*   **Total Expenses** (Roll-up Property): Derived from the "Total Expenses" database, extracting the total actual expenses amount as its original value <a class="yt-timestamp" data-t="06:25:29">[06:25:29]</a>.
*   **Difference** (Formula Property): Calculates the difference between actual expenses and budgeted expenses <a class="yt-timestamp" data-t="06:40:53">[06:40:53]</a>.
*   **Change in Percentage** (Formula Property): Calculates the difference divided by the budgeted expense amount, represented in percentage format <a class="yt-timestamp" data-t="06:51:24">[06:51:24]</a>.