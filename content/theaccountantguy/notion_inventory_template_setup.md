---
title: Notion inventory template setup
videoId: V3PBconN8sE
---

From: [[theaccountantguy]] <br/> 
This article outlines the setup and features of a [[notion_overview | Notion]] template designed for small business inventory tracking <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. This template utilizes a [[using_notion_templates_for_inventory_management | Notion templates for inventory management]] approach to streamline inventory management.

## Inventory Portfolio <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>

The main section of the template is the Inventory Portfolio, which is organized into three primary views: Inventory Setup, Inventory Portfolio, and Inventory Status <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>.

### Inventory Setup <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>

The Inventory Setup section allows for classification of inventory into three categories: raw materials, work in progress, and finished goods <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>.

For each inventory item, the following details can be tracked:
*   **Opening Balance** – The starting balance of the inventory at the beginning of the financial year <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.
*   **Opening Number of Units** <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.
*   **Valuation Principle** – Options include FIFO, LIFO, and WSC (if unfamiliar, this can be left as is without affecting reporting) <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.
*   **Reorder Level** – The unit threshold at which a reorder is triggered for the inventory <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>. For example, 60 units for wheat and 10 units for corn <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.
*   **Percentage** – Indicates the proportion of a particular inventory item relative to the total inventory <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.

#### Adding New Inventory <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>
New inventory items can be added by clicking the "add inventor" button <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>. This places the new item in a "no classification" window <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>, from where it can be dragged and dropped into the appropriate category (e.g., work in progress) <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. Once categorized, values can be entered by clicking the pencil icon <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.

### Inventory Portfolio View <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>

This view displays key metrics for inventory after all transactions (purchases and sales):
*   **Inventory Value** at the end of the transaction period <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.
*   **Number of Units** available <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>.
*   **Reorder Status Level** – Provides messages based on the set reorder levels <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.
    *   If units drop below the reorder level (e.g., 30 units of wheat when reorder level is 60), a "low stock" message appears, indicating a need to reorder <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>.
    *   If units are above the reorder level (e.g., 70 units of corn when reorder level is 10), a "Surplus" message appears, indicating no immediate reorder is needed <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>.

This view helps quickly assess if sufficient units of inventory are available <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.

### Inventory Status <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>

This section tracks the current location or state of inventory items <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.
*   Pre-defined statuses include: "intransit", "in progress", "not sent", and others <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
*   Statuses can be customized or new ones added <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>.
*   The view indicates how many inventory items fall under each status <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>. For example, if a corn purchase of 50 units is "in transit", it will be reflected here <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>. Items can be moved between statuses <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.

## Transaction Section <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>

The transaction section manages purchases, sales, and profit/loss tracking.

### Purchases <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>

*   Transactions are organized by date, with more recent months appearing at the top <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.
*   Details to add for purchases:
    *   **Description** <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>
    *   **Account** (selection from existing inventory items like wheat, corn, bread) <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>
    *   **Number of Units** <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>
    *   **Purchase Price** <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>
    *   **Inventory Status** for the transaction (customizable) <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>
*   A "buy inventory" quick action button automatically adds a purchase entry to the current date <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>.

### Sales <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>

This section operates similarly to purchases, allowing users to record sales of inventory <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>.

### Profit and Loss <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>

For each sale, the template calculates profit or loss:
*   Users input the sales price and the purchase price (or manufacturing cost for finished goods) of the item sold <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>.
*   The template automatically calculates the profit or loss based on the provided values <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>. For example, a $40 sale of bread with a $10 cost, for 30 units, results in a $900 profit <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>.

This [[notion_finance_templates | Notion Finance Templates]] based solution helps track inventory, assign statuses, and monitor its current location and financial performance <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>.