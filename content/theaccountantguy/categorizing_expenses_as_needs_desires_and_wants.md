---
title: Categorizing expenses as needs desires and wants
videoId: OV1faI8Z6yg
---

From: [[theaccountantguy]] <br/> 

Within an expense tracker, expenses are categorized into three main types: needs, desires, and wants <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>. This classification allows for further analysis of spending based on these categories <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.

## Expense Categories Database

The "expense categories" database is one of seven databases used to build the overall expense tracker <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>, <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>. This database is specifically designed to reflect expenses as needs, wants, and desires <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.

The "expense categories" database includes the following properties:
*   **Title Property** The first column serves as a title property for the category <a class="yt-timestamp" data-t="00:12:44">[00:12:44]</a>.
*   **Relation Property** A relation column links to the [[expense_details_and_categorization_in_notion | expense details]] database, capturing all expenses related to needs, wants, and desires separately <a class="yt-timestamp" data-t="00:12:48">[00:12:48]</a>.
*   **Expenses Amount** This is a roll-up property derived from the [[expense_details_and_categorization_in_notion | expense details]] database, which calculates the sum of the actual expense amount for each individual type of expense <a class="yt-timestamp" data-t="00:12:57">[00:12:57]</a>.
*   **Total Expenses** This roll-up property is derived from the "total expenses" database, providing the sum of all combined expenses <a class="yt-timestamp" data-t="00:13:12">[00:13:12]</a>.

## Dashboard Presentation

On the primary dashboard of the expense tracker, the three categories of expenses are displayed <a class="yt-timestamp" data-t="00:13:43">[00:13:43]</a>. They are linked to the [[expense_categorization_in_notion | expense categories]] database and presented in a gallery format <a class="yt-timestamp" data-t="00:13:45">[00:13:45]</a>. For visual presentation, the database is often set up in a three-column format <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a>.