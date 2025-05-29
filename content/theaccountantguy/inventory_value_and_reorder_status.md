---
title: Inventory value and reorder status
videoId: V3PBconN8sE
---

From: [[theaccountantguy]] <br/> 

The inventory management template provides two key metrics for understanding inventory levels: the Inventory Value and the Reorder Status <a class="yt-timestamp" data-t="01:57:00">[01:57:00]</a>. These metrics are accessible within the Inventory Portfolio section of the template <a class="yt-timestamp" data-t="01:10:00">[01:10:00]</a>.

## Inventory Value

The inventory value represents the total value of inventory at the end of a transaction period <a class="yt-timestamp" data-t="01:59:00">[01:59:00]</a>. This value, along with the number of units available, is automatically populated after all purchase and sales transactions are made in the transactions view <a class="yt-timestamp" data-t="02:07:00">[02:07:00]</a>.

## Reorder Status

The reorder status indicates whether an inventory item needs to be reordered based on a predefined reorder level <a class="yt-timestamp" data-t="02:14:00">[02:14:00]</a>.

### Setting Reorder Levels
A reorder level is a specific number of units that triggers a need to reorder an inventory item <a class="yt-timestamp" data-t="00:51:00">[00:51:00]</a>, <a class="yt-timestamp" data-t="00:54:00">[00:54:00]</a>. This level is set in the [[inventory_setup_and_classifications | inventory setup]] section for each item <a class="yt-timestamp" data-t="00:51:00">[00:51:00]</a>.

### Status Indicators
The template provides messages to indicate the reorder status:
*   **Low Stock**: If the available units drop below the set reorder level, a "low stock" message appears, indicating the need to reorder <a class="yt-timestamp" data-t="02:25:00">[02:25:00]</a>, <a class="yt-timestamp" data-t="02:27:00">[02:27:00]</a>, <a class="yt-timestamp" data-t="02:29:00">[02:29:00]</a>.
*   **Surplus**: If available units are significantly above the reorder level, a message indicates that the item is "available in surplus" and does not need to be reordered <a class="yt-timestamp" data-t="02:57:00">[02:57:00]</a>, <a class="yt-timestamp" data-t="02:59:00">[02:59:00]</a>.

### Examples
*   **Wheat**: If the reorder level is set to 60 units <a class="yt-timestamp" data-t="00:59:00">[00:59:00]</a>, and current available units are 30 <a class="yt-timestamp" data-t="02:36:00">[02:36:00]</a>, the system indicates "low stock" because 30 units is below 60 <a class="yt-timestamp" data-t="02:41:00">[02:41:00]</a>, <a class="yt-timestamp" data-t="02:43:00">[02:43:00]</a>.
*   **Corn**: If the reorder level is set to 10 units <a class="yt-timestamp" data-t="01:01:00">[01:01:00]</a>, and current available units are 70 <a class="yt-timestamp" data-t="02:52:00">[02:52:00]</a>, the system indicates a "surplus" as 70 units is well above the 10-unit reorder level <a class="yt-timestamp" data-t="02:56:00">[02:56:00]</a>.

This feature allows users to quickly assess inventory levels and determine if more units are needed <a class="yt-timestamp" data-t="03:05:00">[03:05:00]</a>, <a class="yt-timestamp" data-t="03:08:00">[03:08:00]</a>.