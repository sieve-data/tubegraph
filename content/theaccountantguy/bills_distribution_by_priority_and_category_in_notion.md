---
title: Bills distribution by priority and category in Notion
videoId: RqN1qUpTkSI
---

From: [[theaccountantguy]] <br/> 

Within the [[creating_a_bills_tracker_in_notion | Notion bills tracker]], expenses are categorized and distributed by priority and specific categories, providing an organized overview of spending <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>. This feature is part of the [[primary_dashboard_features_of_notion_bills_tracker | primary dashboard]]'s comprehensive display <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>.

## Bills Distribution by Priority

This section classifies bills into three levels of importance: low, medium, or high priority <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.

**Features:**
*   Displays the amount associated with each priority level <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.
*   Shows the percentage of bills assigned to each priority <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>.
*   On the [[primary_dashboard_features_of_notion_bills_tracker | primary dashboard]], it shows the expenses incurred and the percentage of bills paid for each priority level <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a>.

**Underlying Database:**
The [[databases_used_in_notion_bills_tracker | Bill's Priority database]] specifically contains these three priority levels <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>, <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>. From this database, the actual expense incurred and the bills paid in percentage are extracted <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.

## Bills Distribution by Category

Bills are also distributed across six distinct categories <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.

**Categories:**
*   Entertainment <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>
*   Food and groceries <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>
*   Utility bills <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>
*   Travel and transportation <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>
*   Loans and debts <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>
*   Others <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>

**Features:**
*   Each category shows the total amount paid <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.
*   Displays the percentage of bills paid within that category <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>.
*   On the [[primary_dashboard_features_of_notion_bills_tracker | primary dashboard]], it reflects the total expense incurred and the percentage of payment for bills within each category <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>.

**Underlying Database:**
The [[databases_used_in_notion_bills_tracker | Bill's Category database]] specifically organizes bills according to these six categories <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>, <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>. From this database, information such as the number of bills paid, actual expenses incurred, and the bills paid in percentage are extracted <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.

Both the category and priority distributions are derived from the primary [[databases_used_in_notion_bills_tracker | Bills database]] using a roll-up property to pull respective values <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>, <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>, <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>, <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>, often specifying conditions like "checked" for paid bills <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>.