---
title: Expense Categorization Needs Desires and Wants
videoId: OV1faI8Z6yg
---

From: [[theaccountantguy]] <br/> 

An expense tracker can categorize expenses into three main types: needs, desires, and wants <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>. This classification aids in further [[Expense Analysis and Budgeting | analysis]] of expenses <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>.

## The Expense Categories Database

To build this functionality, an "Expense Categories" database is created <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>. This database is one of seven databases required to build the overall expense tracker <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.

Properties within this database include:
*   **Title Property**: Denotes the specific category, such as "Needs," "Wants," or "Desires" <a class="yt-timestamp" data-t="00:12:37">[00:12:37]</a>, <a class="yt-timestamp" data-t="00:12:44">[00:12:44]</a>.
*   **Relation Property**: Linked to the "Expense Details" database, capturing all individual expenses associated with each category (needs, wants, or desires) <a class="yt-timestamp" data-t="00:12:48">[00:12:48]</a>. The "Expense Details" database itself includes an "Expense Categories" relation property to specify the category for each individual source of expense <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
*   **Expenses Amount**: A roll-up property derived from the "Expense Details" database <a class="yt-timestamp" data-t="00:12:57">[00:12:57]</a>. It calculates the sum of actual expenses incurred for each individual type of expense (needs, wants, desires) <a class="yt-timestamp" data-t="00:13:03">[00:13:03]</a>.
*   **Total Expenses**: A roll-up property from the "Total Expenses" database, providing the sum of all combined expenses <a class="yt-timestamp" data-t="00:13:12">[00:13:12]</a>.

This database completes the process of [[Creating and categorizing expenses in Notion | creating and categorizing expenses]] based on needs, wants, and desires <a class="yt-timestamp" data-t="00:13:21">[00:13:21]</a>.

## Dashboard Presentation

On the primary dashboard of the expense tracker, these three categories of expenses are displayed <a class="yt-timestamp" data-t="00:13:43">[00:13:43]</a>. They are linked to the "Expense Categories" database and presented in a gallery format <a class="yt-timestamp" data-t="00:13:47">[00:13:47]</a>. For optimal presentation, the database view can be set in a three-column format <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a>. This visual representation helps in [[Organizing and categorizing expenses in Notion | organizing and categorizing expenses]] effectively.