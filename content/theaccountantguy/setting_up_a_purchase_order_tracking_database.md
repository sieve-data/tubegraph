---
title: Setting up a purchase order tracking database
videoId: zlLWtZdPvLk
---

From: [[theaccountantguy]] <br/> 

A [[using_notion_for_managing_purchase_orders | purchase order tracker]] template can be utilized to keep a record of your purchase orders <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>.

## Database Structure

The core of the tracker is a database that includes several key columns to capture all necessary information for each purchase order <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>:

*   **Purchase Order Number** <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>
*   **Order Date** <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>
*   **Expected Delivery Date** <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>
*   **Terms and Conditions** <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>
*   **Company Name** <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>
*   **Company Address** <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>
*   **Supplier Name** <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>
*   **Description** (for items) <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>
*   **Quantity** (for items) <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>
*   **Unit Price** (for items) <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>
*   **Shipping Cost Amount** <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>
*   **Tax Rate** (in percentage) <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>
*   **Notes** <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>

### Managing Items and [[calculating_subtotals_and_totals_in_purchase_orders | Calculations]]

The template includes columns for item descriptions, quantities, and unit prices <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>. To add more items, you can duplicate existing description, quantity, and unit price columns <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.

The subtotal amount is automatically computed as the summation of the unit price multiplied by the quantity for each description <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>, <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>. If you add more item columns, the subtotal formula needs to be updated to include the new items <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.

The **total amount** for a purchase order is derived by adding the shipping cost and applying the tax rate to the subtotal <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>, <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.

## Purchase Order Summary

At the top of the tracker, a summary provides an overview of your purchases <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>:

*   **Total Purchase**: This is the summation of all purchases recorded in the database <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>, <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.
*   **Units Ordered**: Calculated from the quantity columns of all items <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>, <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>. Remember to update the calculation formulas if you add more item quantity columns <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>.
*   **Average Order Value**: Computed by dividing the total purchases by the total units ordered <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>. This value is automatically updated <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>.

## Client Summary

The tracker also includes a client summary, which can display information for multiple clients (e.g., ABC Solutions, XYZ Manufacturing, LMN Enterprises) <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>, <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>:

*   **Total Purchases Value** per client <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>
*   **Total Quantities Ordered** from each client <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>
*   **Average Order Value** for each client <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>

## Generating PDF Documents

While the primary function is tracking, the data in the database can also be used to [[generating_purchase_order_pdfs_using_notion | generate PDF documents]] for individual or [[exporting_bulk_purchase_order_documents | bulk purchase orders]] using an external tool like PDF output.com <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>, <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>. This platform allows you to select a purchase order template, choose a currency, and input the database information to create a clean and precise PDF <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>, <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>, <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>. A future integration is planned to directly export from the Notion database <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.

The template offers a simple solution for [[automating_expenses_tracking_through_databases | tracking purchase order expenses]] <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>. For further customization or assistance, you can reach out via email <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>.