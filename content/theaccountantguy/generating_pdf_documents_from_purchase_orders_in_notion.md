---
title: Generating PDF documents from purchase orders in Notion
videoId: zlLWtZdPvLk
---

From: [[theaccountantguy]] <br/> 

This article explains how to utilize a [[using_notion_for_managing_purchase_orders | Notion purchase order tracker template]] to manage purchase orders and [[generating_purchase_order_pdf_documents_using_notion | generate PDF documents]] for them using PDFOutput.com.

## Notion Purchase Order Tracker Template Overview

The [[using_notion_for_managing_purchase_orders | purchase order tracker template]] in Notion features a database designed to keep track of various aspects of purchase orders <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>.

### Database Structure
The database includes essential columns such as:
*   Purchase order number <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>
*   Order date <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>
*   Expected delivery date <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>
*   Terms and conditions <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>
*   Company name and address <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>
*   Supplier name <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>

For tracking individual items within a purchase order, the template provides:
*   Description columns <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>
*   Quantity columns <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>
*   Unit price columns <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>

Additional item entries can be added by duplicating existing description, quantity, and unit price columns <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.

### Automatic Calculations
The template automatically computes several values:
*   **Subtotal Amount**: Calculated as the summation of the unit price multiplied by the quantity for each item description <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>, <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>. If new item columns are added, the formula for the subtotal needs to be updated <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.
*   **Shipping Cost**: A dedicated field to include shipping expenses <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.
*   **Tax Rate**: A percentage field for tax calculation <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.
*   **Total Amount**: The final amount, computed from the subtotal, shipping cost, and tax <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.
*   **Notes**: A column for any additional remarks <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>.

### Summary Dashboards
At the top of the Notion page, a summary section provides key metrics:
*   **Purchase Order Summary**:
    *   **Total Purchases**: The sum of all purchase orders recorded in the database <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.
    *   **Units Ordered**: The total quantity of units ordered across all purchase orders, derived from the quantity columns <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>. This formula also needs to be updated if more quantity columns are added <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>.
    *   **Average Order Value**: Calculated by dividing total purchases by the units ordered <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.
*   **Client Summary**: This section provides a breakdown of purchase data by client. For example, it tracks total purchases, total quantities ordered, and average order value for clients like ABC Solutions, XYZ Manufacturing, and LMN Enterprises <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>.

For further customization of the Notion template, users can contact notionformyuse@gmail.com <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>.

## [[generating_pdf_documents_with_notion_and_pdfoutput | Generating PDF Documents with PDFOutput.com]]

The purchase order data tracked in Notion can be used to [[generating_purchase_order_pdfs_using_notion | generate PDF documents]] using PDFOutput.com <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.

### Single PDF Generation
To [[generating_pdf_documents_with_notion_and_pdfoutput | generate a single PDF]] from a purchase order:
1.  **Login to PDFOutput.com**: Access the platform through their website <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.
2.  **Select Template**: Choose the "Purchase Order" template from the dropdown menu <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>. Users can request new templates if needed <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>.
3.  **Choose Currency**: Select the desired currency (e.g., USD, EUR) from the available options. New currencies can be requested if not listed <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.
4.  **Input Data**: Manually fill in the purchase order details into the PDFOutput.com interface, mirroring the information from the Notion database <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.
5.  **Download PDF**: Once all information is entered and verified, click "Download PDF" to generate the document <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>. The generated PDF will be clean and precise, reflecting the chosen currency <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>, <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.

### Bulk PDF Generation
PDFOutput.com also supports [[bulk_pdf_generation_from_notion_databases | bulk PDF generation]]:
1.  **Switch to Bulk Export Mode**: Navigate to the "Bulk export mode" within the platform <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>.
2.  **Fill Details**: Input details for multiple purchase orders, adding new rows as needed <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>, <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.
3.  **Download Options**: Users can choose to download individual documents or [[generating_bulk_pdf_documents_using_google_docs_and_notion | download all PDFs]] at once <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.

### Future Notion Integration
An upcoming feature will allow direct integration with Notion databases. This will enable users to select a Notion database within PDFOutput.com and directly export or download PDFs, reading information automatically from Notion <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>. This will streamline the process for [[generating_payment_receipts_in_pdf_using_notion | generating payment receipts in PDF using Notion]] and other documents like [[generating_pdf_invoices_from_notion_data | PDF invoices from Notion data]].

For feedback or suggestions on PDFOutput.com, users can utilize the feedback window on the platform <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.