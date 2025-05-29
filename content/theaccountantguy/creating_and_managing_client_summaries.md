---
title: Creating and managing client summaries
videoId: IK71-I_O7Vg
---

From: [[theaccountantguy]] <br/> 

A "client summary" feature within a Notion template allows businesses to track detailed purchasing information for each client <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. This summary is part of a broader [[setting_up_an_invoice_payment_summary | invoice payment summary]] system designed to monitor invoice payments in Notion <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>.

## Client Summary Metrics

The client summary provides key insights into client purchasing behavior <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>. For each client, it shows:
*   Total amount of purchases <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>
*   Total units purchased <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>
*   Average purchase value <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>

These metrics are automatically computed and displayed for all clients based on the data entered <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.

## Data Source: Invoice Database

The information for the client summary is drawn from a detailed invoice database at the bottom of the template <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>. This database includes fields such as:
*   Invoice number <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>
*   Invoice date <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>
*   Due date <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>
*   Company name <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>
*   "Bill to" section <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>
*   Client address <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>
*   Description of purchased items (e.g., "item one," "item two") <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>
*   Quantity of each item <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>
*   Unit price of each item <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>

The subtotal value for each item is calculated by multiplying the unit price and quantity <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>. The tax rate is then added, and the total amount is computed <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>. Notes regarding payment receipt or mode can also be added <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.

### Customization
To add more items beyond the default two, users can duplicate existing columns for description, quantity, and unit price <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>. It's crucial to update the relevant formulas by adding the new columns to ensure all calculations reflect the changes <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. Specifically, the "total quantities purchased" property, used to pull values to the summary, must also be updated <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.

## Example of Client Summary Data

For a client like "11 Enterprises," the summary could show:
*   Total purchases: $189 <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>
*   Total quantity purchased: 44 (e.g., 31 units + 13 units) <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>
*   Average purchase price <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>

This structured approach helps keep track of all invoices generated for a business <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>.