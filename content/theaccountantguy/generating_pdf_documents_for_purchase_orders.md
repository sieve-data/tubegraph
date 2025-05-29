---
title: Generating PDF documents for purchase orders
videoId: zlLWtZdPvLk
---

From: [[theaccountantguy]] <br/> 

This article details how to utilize a purchase order tracker template and then generate PDF documents for those purchase orders using PDFoutput.com.

## Purchase Order Tracker Template

A purchase order tracker template is available to help keep track of purchase orders <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. This template includes a database with various columns essential for managing purchase orders <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>.

### Database Columns

The database contains key information for each purchase order:
*   Purchase order number <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>
*   Order date <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>
*   Expected delivery date <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>
*   Terms and conditions <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>
*   Name of the company <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>
*   Company address <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>
*   Supplier name <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>
*   Description <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>
*   Quantity <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>
*   Unit price <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>

Additional item descriptions, quantities, and unit prices can be added by duplicating existing columns <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.

### Automatic Computations

The template automatically computes several values:
*   **Subtotal Amount** The subtotal is calculated as the summation of the unit price and quantity for each description <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. If new description columns are added, the formula for the subtotal needs to be updated <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.
*   **Shipping Cost** An amount for shipping costs can be added <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.
*   **Tax Rate and Total Amount** A tax rate (in percentage) is applied, leading to a calculated total amount <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.
*   **Notes** A section for additional notes is also available <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>.

### Summary Features

The template provides various summary insights:
*   **Purchase Order Summary**
    *   **Total Purchase** The total amount of all purchases made <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>.
    *   **Units Ordered** The total units ordered across all purchase orders <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>. This calculation is derived from the quantity columns <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>.
    *   **Average Order Value** Calculated by dividing total purchases by units ordered <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.
*   **Client Summary**
    *   **Total Purchases Value** for each client <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.
    *   **Total Quantities Ordered** from each client <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.
    *   **Average Order Value** for each client <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.
    *   Example clients listed include ABC Solutions, XYZ Manufacturing, and LMN Enterprises <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>.

This template is designed to be quick and easy to use <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>. For further customization, users can reach out to notionformyuse@gmail.com <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>.

## Generating PDF Documents Using PDFOutput.com

[[generating_purchase_order_pdfs_using_notion | Generating purchase order PDFs using Notion]] from the tracker database can be done using PDFoutput.com <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.

### Steps for Single PDF Generation

1.  **Login to PDFoutput.com** <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.
2.  **Select Template** Choose the "Purchase AO template" from the dropdown menu <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>. Users can request new currencies or templates if needed <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.
3.  **Choose Currency** Select the desired currency, which will instantly update the template <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.
4.  **Enter Information** Populate the template with details from the purchase order database, such as order date, expected delivery date, company information, and item descriptions <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.
5.  **Download PDF** Once all information is filled, click "Download PDF" to generate a clean and precise purchase order PDF <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>.

### Bulk PDF Generation

PDFoutput.com also supports [[generating_single_and_bulk_pdf_documents | generating single and bulk PDF documents]] <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>. For [[bulk_pdf_invoice_generation | bulk PDF invoice generation]]:

1.  **Switch to Bulk Export Mode** Navigate to the "bulk export mode" <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>.
2.  **Fill Details for Multiple Documents** Input the details for all desired purchase orders by adding multiple rows <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.
3.  **Download Options** Users can choose to download individual documents or "Download all PDF" to get all documents in one go <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.

### Future Notion Integration

Future updates for PDFoutput.com will include direct Notion database integration <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>. This will allow users to directly select a Notion database and export information to generate PDFs more seamlessly <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>.