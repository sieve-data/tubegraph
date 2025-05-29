---
title: Setting and understanding reorder levels
videoId: V3PBconN8sE
---

From: [[theaccountantguy]] <br/> 

The Notion template for [[inventory_management_using_notion | inventory management]] includes a feature to set and track reorder levels for different inventory items. This helps in understanding stock availability and managing replenishment.

## What is a Reorder Level?

A reorder level is the specific number of units of an inventory item at which you want to place a new order to replenish your stock <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.

## Setting Reorder Levels

Within the inventory setup section, each added inventory item allows for a "reorder level" to be set <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. For example:
*   Wheat may have a reorder level of 60 units <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.
*   Corn may have a reorder level of 10 units <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>.

## Understanding Reorder Status

The system uses the set reorder level to provide a "reorder status level" in the inventory portfolio view <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>. This status indicates whether an item needs to be reordered or if there is sufficient stock.

### Low Stock Status
If the available units of an inventory item drop below its set reorder level, the system will indicate "low stock" and signal that the item needs to be reordered <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>.
*   **Example**: If wheat has a reorder level of 60 units <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>, and after transactions, only 30 units are available <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>, the system will display a "low stock" message <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.

### Surplus Stock Status
If the available units are significantly above the reorder level, the system will indicate that the item is "available in Surplus" and does not need to be reordered at that time <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.
*   **Example**: If corn has a reorder level of 10 units <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>, and 70 units are available <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>, the system will show that the item is in surplus <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>.

This feature allows for a quick overview of all inventory items across different categories to determine if sufficient units are available <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>.