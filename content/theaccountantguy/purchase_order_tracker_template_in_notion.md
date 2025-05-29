---
title: Purchase order tracker template in Notion
videoId: zlLWtZdPvLk
---

From: [[theaccountantguy]] <br/> 

This article details a [[notion_product_order_tracking_template | purchase order tracker template]] designed for Notion, which helps users manage and track their purchase orders and associated expenses <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. The template is presented as a straightforward tool that can also be integrated with a PDF generation service for creating official purchase order documents <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.

## Template Database Structure

The core of the template is a database featuring several key columns to capture comprehensive purchase order details <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>:

*   **Purchase Order Number** <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>
*   **Order Date** <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>
*   **Expected Delivery Date** <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>
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

### Item Tracking and Calculation

The template comes pre-configured with two description, quantity, and unit price columns <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>. Users can easily add more item fields by duplicating existing columns for description, quantity, and unit price <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.

A "Subtotal" column automatically computes the sum of the quantities multiplied by their respective unit prices for all listed items <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. When adding new item columns, it is essential to update the subtotal formula to include these new values for accurate calculation <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>. The template also calculates a "Total Amount" by incorporating shipping costs and a tax rate <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.

## Purchase Order Summary

At the top of the Notion page, a summary section provides a quick overview of purchase activity <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>:

*   **Total Purchase:** This is the sum of all purchase orders in the database <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.
*   **Units Ordered:** This calculates the total units ordered across all purchase orders, derived from the quantity columns <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>. Users must update the formula for this summary as more quantity columns are added <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>.
*   **Average Order Value:** This is computed by dividing the total purchases by the total units ordered <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.

## Client Summary

The template includes a client summary that tracks purchase data for different clients, such as ABC Solutions, XYZ Manufacturing, and LMN Enterprises <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>. For each client, the summary displays:

*   **Total Purchases Value** <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>
*   **Total Quantities Ordered** <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>
*   **Average Order Value** <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>

## Generating Purchase Order PDFs

The template offers a solution for [[generating_purchase_order_pdfs_with_notion | generating PDF documents]] for purchase orders using `PDFoutput.com` <a class="yt-timestamp" data-t="02:29:500">[00:02:29]</a>.

### Steps for Single PDF Generation

1.  **Login:** Access `PDFoutput.com` <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.
2.  **Select Template:** Choose the "Purchase Order" template from the dropdown menu <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.
3.  **Choose Currency:** Select the desired currency (e.g., USD, Euro) <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>. Users can request new currencies or templates if needed <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>.
4.  **Input Data:** Manually fill in the purchase order details from the Notion database into the template on `PDFoutput.com` <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.
5.  **Download PDF:** Click "Download PDF" to generate the document <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>. The generated PDF will reflect the chosen currency and details <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.

### Bulk PDF Export

For [[generating_purchase_order_pdfs_in_bulk_using_notion | exporting multiple documents]], users can switch to "bulk export mode" on `PDFoutput.com` <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>. In this mode, users fill in details for multiple purchase orders by adding new rows <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>. They can then download individual documents or all documents in one go <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.

### Future Notion Integration

A future update for `PDFoutput.com` will include direct integration with Notion databases. This will allow users to select their Notion database and directly export PDF documents without manual data entry <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>.

---
**See Also:**
*   [[notion_product_order_tracking_template | Notion Product Order Tracking Template]]
*   [[inventory_tracking_using_notion | Inventory Tracking Using Notion]]
*   [[how_to_use_a_sales_receipts_tracker_in_notion | How to Use a Sales Receipts Tracker in Notion]]
*   [[generating_purchase_order_pdfs_with_notion | Generating Purchase Order PDFs with Notion]]
*   [[setting_up_a_customer_payments_tracker_in_notion | Setting Up a Customer Payments Tracker in Notion]]
*   [[generating_purchase_order_pdfs_in_bulk_using_notion | Generating Purchase Order PDFs in Bulk Using Notion]]
*   [[creating_a_bills_tracker_in_notion | Creating a Bills Tracker in Notion]]
*   [[creating_an_income_tracker_in_notion | Creating an Income Tracker in Notion]]
*   [[invoicing_and_payment_tracking_through_notion | Invoicing and Payment Tracking Through Notion]]