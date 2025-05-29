---
title: Analyzing top and least expenses in Notion
videoId: OV1faI8Z6yg
---

From: [[theaccountantguy]] <br/> 

Within a Notion expense tracker, a dedicated section allows users to analyze their spending patterns by highlighting top, least, and recent expenses incurred over a period <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>. This feature is part of a comprehensive system for [[using_notion_for_expense_management | managing finances using Notion]] <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>.

## Top 10 Highlights

The "Top 10 Highlights" section on the primary dashboard is designed to provide quick insights into spending behavior <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>, <a class="yt-timestamp" data-t="00:13:57">[00:13:57]</a>. It reflects:
*   The top 10 expenses incurred during a specific period <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.
*   The least 10 expenses incurred during the period <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.
*   The recent expenses incurred during the period <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>.

This section is linked to the `Expense Details` database and is presented in a list format <a class="yt-timestamp" data-t="00:14:03">[00:14:03]</a>, allowing for a focused view of individual expenses.

### Sorting Logic

To accurately display the "Top 10 Highlights," the data is sorted according to specific criteria:
*   **Recent Expenses**: Sorted by "created time" in descending order <a class="yt-timestamp" data-t="00:14:07">[00:14:07]</a>.
*   **Least 10 Expenses**: Sorted by "actual expenses" in ascending order <a class="yt-timestamp" data-t="00:14:11">[00:14:11]</a>.
*   **Top 10 Expenses**: Sorted in descending order <a class="yt-timestamp" data-t="00:14:16">[00:14:16]</a>.

## Underlying Database: Expense Details

The `Expense Details` database is fundamental to this analysis, as it captures individual expense records <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>, <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>. This database includes several key properties:
*   **Expense Details (Title Property)**: Shows individual expenses incurred <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.
*   **Actual Expense**: A number property specifying the actual amount of expense incurred for the period, indicated in US dollars <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.
*   **Budgeted Expense**: The estimated budgeted expense for each month, also specified in US dollars <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.

The sum of actual and budgeted expenses can be found at the bottom of this database <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>. The "actual expense" property is crucial for sorting the top and least expenses, while the "created time" is used for recent expenses.