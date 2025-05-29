---
title: Categorizing expenses as needs desires and wants
videoId: OV1faI8Z6yg
---

From: [[theaccountantguy]] <br/> 

Within the expense tracker, expenses are [[expense_categorization | categorized]] into three main types: needs, desires, and wants <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>. This classification helps in further analysis of spending for each type of expense <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>.

## Expense Categories Database

To facilitate this categorization, an "Expense Categories" database is created <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>. This database is one of seven essential databases required to build the overall expense tracker <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.

### Database Properties

The "Expense Categories" database includes several key properties:

*   **Title Property**: This is the first column, specifying the individual categories of needs, desires, and wants <a class="yt-timestamp" data-t="00:12:44">[00:12:44]</a>.
*   **Relation to Expense Details**: A relation property links this database to the "Expense Details" database <a class="yt-timestamp" data-t="00:12:48">[00:12:48]</a>. This connection allows the system to capture and relate all individual expenses to their respective categories (needs, wants, or desires) <a class="yt-timestamp" data-t="00:12:50">[00:12:50]</a>.
*   **Expenses Amount**: This roll-up property derives the actual expenses incurred for each category from the "Expense Details" database, calculating their sum <a class="yt-timestamp" data-t="00:12:57">[00:12:57]</a>.
*   **Total Expenses**: Another roll-up property, this derives the sum of all combined expenses from the "Total Expenses" database <a class="yt-timestamp" data-t="00:13:12">[00:13:12]</a>.

### Dashboard Presentation

On the primary dashboard of the expense tracker, these three categories of expenses (needs, desires, and wants) are prominently displayed <a class="yt-timestamp" data-t="00:13:43">[00:13:43]</a>. They are linked to the "Expense Categories" database and presented in a gallery format <a class="yt-timestamp" data-t="00:13:45">[00:13:45]</a>. For visual organization, the database display can be set in a three-column format <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a>. This allows for a clear overview of spending distribution across these fundamental categories.