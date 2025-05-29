---
title: Tracking inventory status and transactions
videoId: V3PBconN8sE
---

From: [[theaccountantguy]] <br/> 
This article describes how a Notion template can be utilized for [[inventory_tracking_using_notion | inventory tracking]] for a small business, focusing on managing inventory status and [[adding_and_managing_transactions | transactions]].

## Inventory Portfolio <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>

The template is organized with an "Inventory Portfolio" section at the top, featuring three distinct views:
1.  Inventory Setup <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>
2.  Inventory Portfolio (main view) <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>
3.  Inventory Status <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>

### Inventory Setup <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>

This section classifies inventory into three types: Raw Materials, Work in Progress, and Finished Goods <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>. For each added inventory item, the following details can be set:
*   **Opening Balance**: The starting monetary value of the inventory at the beginning of the financial year <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.
*   **Opening Number of Units**: The initial quantity of units <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>.
*   **Valuation Principle**: Options include FIFO, LIFO, or WSC, though this can be left as is without affecting other reporting <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.
*   **Reorder Level**: A specified unit level at which the inventory should be reordered <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. For example, wheat might have a reorder level of 60 units, and corn 10 units <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.
*   **Percentage**: Shows the proportion of a particular inventory item relative to the total inventory <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.

New inventory items can be quickly added using an "add inventory" button, initially appearing in a "no classification" window <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>. Users can then drag and drop the item into the desired category (e.g., Work in Progress) and fill in its values <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.

### Inventory Portfolio View <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>

This view displays the current state of the inventory:
*   **Inventory Value**: The value of the inventory at the end of the transaction period <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>.
*   **Number of Units Available**: The total units remaining after all purchases and sales are processed <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>.
*   **Reorder Status Level**: Indicates whether an item needs reordering based on the set reorder level <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>. If units drop below the reorder level (e.g., wheat at 30 units when the reorder level is 60), it displays a "low stock" message prompting a reorder <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>. Conversely, if units are well above the reorder level (e.g., corn at 70 units with a 10-unit reorder level), it indicates "item available in surplus" <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.

### Inventory Status <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>

This section tracks the current location or stage of inventory, categorizing it by statuses like "in transit," "in progress," or "not sent" <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>. Users can customize these statuses <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>. For instance, if one purchase is "in transit," this section will reflect it <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>. Items can be easily moved between statuses by dragging and dropping <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.

## Transaction Section <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>

This part of the template is dedicated to [[tracking_transactions_and_invoice_statuses | tracking transactions]] related to inventory, including purchases, sales, and calculating profit/loss.

### Purchases <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>

Purchase [[tracking_purchases_and_consumption | transactions]] are organized by month, with the latest month appearing at the top <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>. For each purchase, users can input:
*   **Date**: Transactions auto-populate and bifurcate into different months <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>.
*   **Description**: A field for details about the purchase <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>.
*   **Account**: Selection of the specific inventory item (e.g., wheat, corn, bread) <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>.
*   **Number of Units**: Quantity purchased <a class="yt-timestamp" data-t="00:05:33">[00:05:33]</a>.
*   **Purchase Price**: The cost per unit <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>.
*   **Inventory Status**: Assign the current status of the purchased item <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>. This can also be edited <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.

A "buy inventory" quick action button automatically adds a new purchase entry with the current date <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.

### Sales <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>

The sales section functions similarly to the purchases section, allowing users to record inventory sales <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>.

### Profit and Loss <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>

For each sale, users must input the purchase price or manufacturing cost of the item sold <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>. The template then automatically calculates the profit or loss per sale. For example, if bread was sold for $40 and its cost was $10, with 30 units sold, the profit would be ($40 - $10) * 30 units = $900 <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>.

This comprehensive approach allows for detailed [[inventory_tracking_using_notion | inventory tracking]], status assignment, and financial oversight within a single template <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>.