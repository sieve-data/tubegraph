---
title: Tracking top and least expenses over a period
videoId: OV1faI8Z6yg
---

From: [[theaccountantguy]] <br/> 

An [[tracking_expenses|expense tracker]] can highlight top and least expenses incurred during a specific period <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>. This feature provides a quick overview of spending patterns <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.

## Components of the Feature

This feature typically reflects:
*   The top 10 expenses incurred <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>
*   The least 10 expenses incurred <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>
*   Recent expenses incurred <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>

## Data Source and Presentation

The data for tracking top and least expenses is primarily drawn from the **Expense Details database** <a class="yt-timestamp" data-t="00:14:03">[00:14:03]</a>. This database stores individual expense entries <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>, including the actual amount incurred <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.

The "Top 10 Highlights" section on the main dashboard is presented in a list format <a class="yt-timestamp" data-t="00:14:05">[00:14:05]</a>.

### Sorting Logic

To identify top, least, and recent expenses, specific sorting criteria are applied to the Expense Details database <a class="yt-timestamp" data-t="00:13:59">[00:13:59]</a>:

*   **Recent Expenses:** Sorted by `created time` in descending order <a class="yt-timestamp" data-t="00:14:07">[00:14:07]</a>.
*   **Least 10 Expenses:** Sorted by `actual expenses` in ascending order <a class="yt-timestamp" data-t="00:14:11">[00:14:11]</a>.
*   **Top 10 Expenses:** Sorted by `actual expenses` in descending order <a class="yt-timestamp" data-t="00:14:16">[00:14:16]</a>.