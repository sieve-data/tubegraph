---
title: Exporting and managing purchase order data
videoId: zlLWtZdPvLk
---

From: [[theaccountantguy]] <br/> 

This article outlines how to utilize a purchase order tracker template to keep track of and [[import_export_management | export]] purchase orders. The template provides a database for managing order details and offers a solution for [[generating_pdf_documents_for_purchase_orders | generating PDF documents]] for these orders via an external service. <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>

## Purchase Order Tracker Database

The core of the system is a database designed to maintain purchase order information. <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>

### Database Columns
The database includes essential columns such as:
*   Purchase order number <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>
*   Order date <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>
*   Expected delivery date <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>
*   Terms and conditions <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>
*   Company name and address <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>
*   Supplier name <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>
*   Notes <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>

### Item Details and Calculations
Crucial columns for tracking items include:
*   Description <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>
*   Quantity <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>
*   Unit price <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>

The database automatically computes the subtotal amount based on the quantity and unit price of items. <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a> Additional item descriptions can be added by duplicating existing columns and updating the subtotal formula. <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>

### Cost Components
The system also accounts for:
*   Shipping cost <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>
*   Tax rate in percentage <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>
These are added to derive the total amount for each purchase order. <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>

### Summary Metrics
The tracker provides summary information at the top of the database:
*   **Total Purchase Summary:** Shows the cumulative value of all purchases made. <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>
*   **Units Ordered:** Calculates the total units ordered from the quantity columns. <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>
*   **Average Order Value:** Computed by dividing total purchases by total units ordered. <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>

### Client Summary
A client summary section displays:
*   Total purchases value for each client <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>
*   Total quantities ordered from each client <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>
*   Average order value for each client <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>
Example clients include ABC Solutions, XYZ Manufacturing, and LMN Enterprises. <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>

## Exporting Purchase Order Documents

The system supports [[generating_pdf_documents_for_purchase_orders | generating PDF documents]] for purchase orders using PDFoutput.com. <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a> <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>

### Using PDFoutput.com
To [[exporting_completed_pdf_invoices | export]] PDFs:
1.  Log in to PDFoutput.com. <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>
2.  Select the "purchase AO template" from the dropdown menu. <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>
3.  Choose the desired currency for the document. <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>
    *   Currencies can be requested if not available. <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>
    *   Templates can also be requested. <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>
4.  Ensure "single PDF mode" is selected for individual document generation. <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>

### Single PDF Generation
In single PDF mode, users fill in the required information for a specific purchase order on the screen. <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a> Once details are filled, clicking "Download PDF" generates a clean and precise PDF document. <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a> The currency can be changed, and the PDF will update instantly to reflect the new currency. <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>

### Bulk PDF Export
For [[generating_purchase_order_pdfs_in_bulk_using_notion | exporting multiple documents]] at once, switch to "bulk export mode". <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>
1.  Fill in the details for multiple purchase orders by adding new rows. <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>
2.  Users can download individual documents or click "Download all PDF" to generate all documents in one go. <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>

### Future Notion Integration
A future update will include [[notion_integration_for_purchase_order_management | Notion integration]], allowing users to select a Notion database directly within PDFoutput.com to export PDF documents, streamlining the process of [[generating_purchase_order_pdfs_with_notion | generating purchase order PDFs with Notion]]. <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a> <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>