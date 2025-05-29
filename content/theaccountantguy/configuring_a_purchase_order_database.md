---
title: Configuring a purchase order database
videoId: zlLWtZdPvLk
---

From: [[theaccountantguy]] <br/> 

A purchase order tracker template includes a database designed to keep track of purchase orders <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. This database is essential for maintaining and managing all purchase order information <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>.

## Database Structure

The database features various columns to capture comprehensive purchase order details <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>:

*   **Purchase Order Number** <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>
*   **Order Date** <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>
*   **Expected Delivery Date** <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>
*   **Terms and Conditions** <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>
*   **Company Name** <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>
*   **Company Address** <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>
*   **Supplier Name** <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>
*   **Notes** <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>

### Item Details

For individual items within a purchase order, the database includes:

*   **Description** <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>
*   **Quantity** <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>
*   **Unit Price** <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>

Initially, two sets of description, quantity, and unit price columns are provided <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>. To add more items, these columns can be duplicated <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>.

### Cost Calculations

The database automatically computes several financial values:

*   **Subtotal Amount** <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>: This is the summation of the unit price multiplied by quantity for all item descriptions <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>. If additional item columns are added, the subtotal formula must be updated to include the new values <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.
*   **Shipping Cost Amount** <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>: An additional field to include shipping expenses <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.
*   **Tax Rate (in percentage)** <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>: Applied to calculate the final total <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.
*   **Total Amount** <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>: The final computed cost of the purchase order <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

## Purchase Order Summaries

The template provides real-time summaries at the top, derived from the database entries:

*   **Total Purchase** <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>: The sum of all purchases recorded in the database <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.
*   **Units Ordered** <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>: Calculated from the quantities across all item description columns <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>. Ensure formulas are updated if more quantity columns are added <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>.
*   **Average Order Value** <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>: This is the total purchases divided by the units ordered <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.

### Client Summary

A dedicated section provides a summary for different clients, based on their purchase orders in the database <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>. Examples include ABC Solutions, XYZ Manufacturing, and LMN Enterprises <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>. For each client, the following metrics are displayed:

*   **Total Purchases Value** <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>
*   **Total Quantities Ordered** <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>
*   **Average Order Value** <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>

This [[using_purchase_order_tracker_in_notion | purchase order tracker template]] is designed to be a simple, easy-to-use tool for tracking purchase order expenses <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>. For further [[customizing_purchase_order_templates_in_notion | customization]], assistance can be requested via email <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>.

## Generating PDF Documents

The template supports [[generating_pdf_documents_for_purchase_orders | generating PDF documents]] for individual purchase orders <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>. This functionality is available through PDF output.com <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.

### Single PDF Generation

1.  **Log in to PDF output.com** <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.
2.  **Select the "Purchase AO template"** from the dropdown menu <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.
3.  **Choose the desired currency** (e.g., USD, Euro) <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>. New currencies can be requested if not available <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.
4.  **Ensure "Single PDF mode" is selected** <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.
5.  **Fill in all the required details** from the purchase order database into the template on the screen <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.
6.  **Click "Download PDF"** to generate the document <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>.

### Bulk PDF Generation

For [[generating_purchase_order_pdfs_in_bulk | exporting multiple purchase order documents]], use the "bulk export mode" <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>.

1.  **Select "bulk export mode"** <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.
2.  **Fill in details for multiple purchase orders** by adding new rows <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.
3.  **Click "Download all PDF"** to generate all documents in one go <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>. Individual documents can also be downloaded <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.

An upcoming Notion integration will allow for [[generating_purchase_order_pdfs_using_notion | direct PDF generation from a Notion database]] <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>.