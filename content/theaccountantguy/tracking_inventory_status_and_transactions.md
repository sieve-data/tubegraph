---
title: Tracking inventory status and transactions
videoId: V3PBconN8sE
---

From: [[theaccountantguy]] <br/> 

This article describes a template designed to help small businesses [[monitoring_inventory_transactions | track inventory]]. The template is presented by Sanat Biswal, "the accountant guy" <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>.

## Inventory Portfolio Overview

The template's inventory portfolio consists of three main views <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>:
*   Inventory Setup <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>
*   Inventory Portfolio <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>
*   Inventory Status <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>

### Inventory Setup

The Inventory Setup section allows for classifying inventory into three categories <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>:
*   Raw Materials <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>
*   Work in Progress <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>
*   Finished Goods <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>

For each added inventory item, the following details are tracked <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>:
*   **Opening Balance**: The starting balance of the inventory at the beginning of the financial year <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>.
*   **Opening Number of Units**: The initial quantity of units <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.
*   **Evaluation Principle**: Options like FIFO (First-In, First-Out), LIFO (Last-In, First-Out), or WSC (Weighted Average Cost) are available, though they can be left as default without affecting reporting <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.
*   **Reorder Level**: The unit level at which new orders should be placed for the inventory item <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. For example, a reorder level of 60 units for wheat and 10 units for corn was demonstrated <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.
*   **Percentage**: Indicates the proportion of a particular inventory item relative to the total inventory <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.

New inventory items can be added by clicking the "add inventor" button, which places them in a "no classification" window <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>. From there, they can be dragged and dropped into their specific category (e.g., Work in Progress) <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.

### Inventory Portfolio View

This section provides an overview of the current [[monitoring_inventory_transactions | inventory]] status <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>:
*   **Inventory Value**: The total value of inventory at the end of the transaction period <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>.
*   **Number of Units Available**: The quantity of units remaining after all purchases and sales <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.
*   **Reorder Status Level**: This status indicates whether an item needs reordering based on the reorder level set in the Inventory Setup <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.
    *   If units drop below the reorder level (e.g., wheat at 30 units when the reorder level is 60), a "low stock" message appears, prompting reorder <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.
    *   If units are above the reorder level (e.g., corn at 70 units when the reorder level is 10), a "Surplus" message appears, indicating no reorder is currently needed <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.

This view provides a quick glance at [[monitoring_inventory_transactions | inventory]] levels across categories <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>.

### Inventory Status View

This section tracks the current physical status of inventory <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>. Predefined statuses include <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>:
*   In Transit <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>
*   In Progress <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>
*   Not Sent <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>
Users can also edit or add new statuses as needed <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>.

The view shows how many [[monitoring_inventory_transactions | inventory transactions]] are currently in each status (e.g., one item "in transit" or "not sent") <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>. Transactions can be moved between statuses by clicking on the three dots icon <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.

## Transaction Section

The transaction section manages the financial aspects of [[monitoring_inventory_transactions | inventory]] <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>:
*   Purchases <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>
*   Sales <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>
*   Profit and Loss <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>

### Purchases

Purchase [[monitoring_inventory_transactions | transactions]] are organized by date, with the latest month appearing at the top <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>.
Key fields for purchases include <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>:
*   **Date**: Transactions are automatically bifurcated into different months <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.
*   **Description**: A field to add details about the purchase <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>.
*   **Account**: Selection of the inventory item being purchased (e.g., wheat, corn, bread) <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>.
*   **Number of Units**: The quantity of units purchased <a class="yt-timestamp" data-t="00:05:33">[00:05:33]</a>.
*   **Purchase Price**: The cost per unit <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>.
*   **Inventory Status**: The current status of the purchase transaction, which can be assigned from the available options <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>.

A "buy inventory" quick action button can automatically add a new purchase entry for the current date <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.

### Sales

The sales section functions similarly to the purchases section, allowing users to record and track sales of [[monitoring_inventory_transactions | inventory]] <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>.

### Profit and Loss

For each sale, the profit and loss section requires inputting the purchase price or cost of manufacturing the item sold <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>. The template then automatically calculates the profit or loss <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>. For example, a bread sale of $40 with a manufacturing cost of $10 would yield a $30 profit per unit, totaling $900 for 30 units sold <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>.

This template helps businesses effectively [[monitoring_inventory_transactions | track their inventory]], manage [[monitoring_inventory_transactions | transactions]], and ascertain the current status of their stock <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>.