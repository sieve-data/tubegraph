---
title: Classification of bills by priority and category
videoId: RqN1qUpTkSI
---

From: [[theaccountantguy]] <br/> 

In a Notion bills tracker, bills are organized and presented based on their priority and specific categories, providing users with a clear overview of their financial obligations and spending habits <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.

## Classification by Priority

Bills can be classified into three levels of priority: low, medium, or high <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. This classification helps in understanding the importance of each expense <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>. The tracker displays the amount associated with each priority level and the percentage of bills paid within that priority <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.

On the primary dashboard, the "Bills Distribution as per Priority" section visually represents expenses incurred and the percentage of bills paid for each priority level <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>.

## Classification by Category

Bills are also categorized into six distinct groups to provide a detailed breakdown of spending <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>. The categories include:
*   Entertainment <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>
*   Food and Groceries <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>
*   Utility Bills <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>
*   [[classifying_and_adding_travel_expenses_into_categories | Travel and Transportation]] <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>
*   [[debt_overview_and_categorization | Loans and Debts]] <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>
*   Others <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>

For each category, the tracker shows the total amount paid and the percentage of bills paid <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>. The primary dashboard includes a "Bills Distribution as per Category" section that displays the total expense incurred and the percentage of payments for each of these categories <a class="yt-timestamp" data-t="00:06:35">[00:06:35]</a>. This categorization is crucial for [[categorizing_expenses_in_notion | categorizing expenses in Notion]] effectively.

## Database Structure for Classification

The classification of bills by priority and category relies on several interlinked databases in Notion <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>:

*   **Bills Details Database**: This is the primary database where each expense entry includes columns for "Category" and "Priorities" <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>. These columns link to other supplemental databases for organization and presentation <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.
*   **Bills Category Database**: This database is dedicated to the six expense categories, storing information such as the number of bills paid, the actual expenses incurred, and the percentage of bills paid for each category <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>.
*   **Bills Priority Database**: Similar to the category database, this one manages the low, medium, and high priorities. It also extracts the actual expenses incurred and the percentage of bills paid for each priority level <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>.

Information like actual expenses and percentage of bills paid in these supplemental databases is typically derived using "rollup" properties from the main Bills Details Database <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.