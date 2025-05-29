---
title: Using Notion for inventory management
videoId: V3PBconN8sE
---

From: [[theaccountantguy]] <br/> 

This Notion template, demonstrated by Sanat Biswal ("the accountant guy"), helps small businesses track their inventory <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>.

## Inventory Portfolio

The inventory portfolio section offers three distinct views for managing inventory: Inventory Setup, Inventory Portfolio, and Inventory Status <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.

### Inventory Setup

This view allows for the initial classification and setup of inventory items <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. Inventory can be categorized into:
*   Raw Materials <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>
*   Work in Progress <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>
*   Finished Goods <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>

For each inventory item, the following details can be recorded:
*   **Opening Balance:** The starting balance of the inventory at the beginning of the financial year <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.
*   **Opening Number of Units** <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>
*   **Valuation Principle:** Options include FIFO, LIFO, and WSC (Weighted Average Cost) <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>. This field is optional and won't affect other reporting if left undefined <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.
*   **Reorder Level:** The unit threshold at which a reorder of the inventory item is triggered <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.
*   **Percentage:** Indicates the proportion of a specific inventory item relative to the total inventory <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.

New inventory items can be added by clicking the "Add Inventory" button, which initially places them in a "no classification" window <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>. From there, items can be moved to specific categories like "Work in Progress" <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>. Once categorized, values can be entered via a pencil icon <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>.

### Inventory Portfolio (View)

This section provides a summary of inventory values and statuses after all transactions <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.
*   **Inventory Value:** The value of inventory at the end of the transaction period <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.
*   **Number of Units Available:** The quantity of units remaining after all purchases and sales <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>.
*   **Reorder Status Level:** This indicates whether an item needs to be reordered based on its reorder level <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>. For example, if "Wheat" drops below its reorder level of 60 units (e.g., to 30 units), a "low stock" message appears, prompting a reorder <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>. Conversely, an item like "Corn" with 70 units available, well above its 10-unit reorder level, will show as "Surplus" <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>. This provides a quick overview of inventory sufficiency <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>.

### Inventory Status

This view tracks the current physical status of inventory items <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>. Statuses include:
*   In Transit <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>
*   In Progress <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>
*   Not Sent <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>
*   And others <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>

These statuses are customizable; new ones can be added, and existing ones edited <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>. The view shows a count of items under each status, e.g., "In Transit (1)" <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>. Clicking on a status reveals the specific transactions under that status, such as a "Corn purchase" currently in transit <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>. Items can be moved between statuses as needed <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.

## Transactions

The transaction section manages purchases, sales, and profit/loss calculations for inventory <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>.

### Purchases

Purchase transactions are organized by date, with the latest month appearing at the top <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>. Key fields for a purchase transaction include:
*   **Date:** Automatically categorizes transactions by month <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>.
*   **Description** <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>
*   **Account:** Allows selection of the specific inventory item (e.g., "Wheat," "Corn," "Bread") <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>.
*   **Number of Units** <a class="yt-timestamp" data-t="00:05:33">[00:05:33]</a>
*   **Purchase Price:** The total value automatically populates based on units and price <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>.
*   **Inventory Status:** Customizable status for the transaction <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>.

A "Buy Inventory" quick action button can be used to automatically add a new purchase transaction with the current date <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.

### Sales

Similar to purchases, the sales section tracks inventory sales <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>.

### Profit and Loss

For every sale made, the profit and loss section requires the input of the purchase price (cost) of the sold item <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>. For example, if "Bread" was sold for $40 and its manufacturing cost was $10, inputting $10 as the purchase price will automatically calculate the profit or loss <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>. This allows for tracking the profitability of inventory sales <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>.