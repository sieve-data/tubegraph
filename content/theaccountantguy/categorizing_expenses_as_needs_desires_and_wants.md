---
title: Categorizing expenses as needs desires and wants
videoId: OV1faI8Z6yg
---

From: [[theaccountantguy]] <br/> 
An expense tracker can categorize expenses into three main types: needs, desires, and wants <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>. This classification aids in further [[Expense categorization and tracking in Notion | analysis of expenses]] for each type <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.

### Expense Categories Database Setup

To implement this categorization, an "Expense Categories" database is created <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>. This database reflects expenses based on needs, wants, and desires <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>, and specifies the three types of expenses <a class="yt-timestamp" data-t="00:12:37">[00:12:37]</a>.

Key properties within this database include:
*   **Title Property** The first column of the database <a class="yt-timestamp" data-t="00:12:44">[00:12:44]</a>.
*   **Relation Property to Expense Details Database** This column links to the "Expense Details" database, capturing all expenses related to needs, wants, and desires separately <a class="yt-timestamp" data-t="00:12:48">[00:12:48]</a>.
*   **Expenses Amount** This is a roll-up property that shows the actual expenses incurred <a class="yt-timestamp" data-t="00:12:57">[00:12:57]</a>. It is derived from the "Expense Details" database, summing the actual expense amount for each individual type of expense <a class="yt-timestamp" data-t="00:13:03">[00:13:03]</a>.
*   **Total Expenses** A roll-up property derived from the "Total Expenses" database, providing the sum of all combined expenses <a class="yt-timestamp" data-t="00:13:12">[00:13:12]</a>.

### Dashboard Presentation

On the primary dashboard of the expense tracker, these three categories of expenses are displayed <a class="yt-timestamp" data-t="00:13:43">[00:13:43]</a>. They are linked to the "Expense Categories" database and presented in a gallery format <a class="yt-timestamp" data-t="00:13:45">[00:13:45]</a>. For visual organization, the database can be arranged into a three-column format <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a>.