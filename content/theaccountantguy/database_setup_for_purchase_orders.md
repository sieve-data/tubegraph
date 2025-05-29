---
title: Database setup for purchase orders
videoId: zlLWtZdPvLk
---

From: [[theaccountantguy]] <br/> 

A database setup for purchase orders is used to [[tracking_purchase_order_expenses | keep track of your purchase orders]] <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. This template helps manage and summarize all relevant purchase order information <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>.

## Essential Database Columns

The purchase order tracker database includes several key columns to manage order details:
*   **Purchase Order Number** <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>
*   **Order Date** <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>
*   **Expected Delivery Date** <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>
*   **Terms and Conditions** <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>
*   **Company Name** <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>
*   **Company Address** <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>
*   **Supplier Name** <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>
*   **Description** (of items) <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>
*   **Quantity** <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>
*   **Unit Price** <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>

### Item Details and Calculations

The database automatically computes financial aspects of your purchase orders:
*   **Subtotal Amount** is automatically computed based on the quantity and unit price of items <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. It calculates the summation of each item's unit price multiplied by its quantity <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.
*   **Shipping Cost Amount** can be added to the purchase order <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.
*   **Tax Rate (percentage)** is included <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.
*   **Total Amount** is automatically calculated from the subtotal, shipping, and tax <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.
*   **Notes** can be added for additional information <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>.

### Customizing Item Columns

If you need to add more items to a purchase order than the default number of description, quantity, and unit price columns, you can duplicate these columns <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. After duplicating, ensure you update the subtotal formula to include the new columns' values for accurate calculation <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.

## Purchase Order Summaries

The database provides summary views for quick insights into your purchase activities:

### Overall Summary
*   **Total Purchases**: The sum of all purchase orders <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>.
*   **Units Ordered**: The total quantity of all items ordered across all purchase orders <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.
*   **Average Order Value**: Calculated by dividing the total purchases by the units ordered <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.

### Client Summary
A client summary section details purchase information per client, including:
*   Total purchases value for each client <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.
*   Total quantities ordered from each client <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.
*   Average order value per client <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.

### Notion Integration
Currently, the database is a standalone template. However, there are plans for [[setting_up_a_purchase_order_template_in_notion | Notion integration]] that will allow direct export of data from a Notion database to generate PDF documents <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.

For generating PDF documents from your purchase orders, you can use PDFoutput.com <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>. This tool allows you to [[generating_pdf_documents_for_purchase_orders | generate PDF documents for purchase orders]] either individually or in bulk <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.