---
title: Customizing and exporting purchase order templates
videoId: zlLWtZdPvLk
---

From: [[theaccountantguy]] <br/> 

This article details the use of a purchase order tracker template and how to [[generating_pdf_documents_for_purchase_orders | generate PDF documents for purchase orders]] from it.

## Purchase Order Tracker Template Overview

The template helps to keep track of purchase orders within a database structure <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>.

### Database Structure

The database includes several columns to organize purchase order information <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>:
*   Purchase order number <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>
*   Order date <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>
*   Expected delivery date <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>
*   Terms and conditions <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>
*   Company name <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>
*   Company address <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>
*   Supplier name <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>
*   Description (for items) <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>
*   Quantity (for items) <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>
*   Unit price (for items) <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>

To add more item descriptions, quantities, and unit prices, existing columns can be duplicated <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.

### Automatic Calculations

The template automatically computes several values:
*   **Subtotal Amount** The subtotal is calculated as the summation of the unit price and quantity for all listed descriptions <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. If additional description columns are added, their values must be included in the subtotal formula for accurate computation <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.
*   **Shipping Cost** A dedicated field is available to include shipping costs <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.
*   **Tax Rate** A tax rate in percentage can be added <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.
*   **Total Amount** This is automatically computed based on the subtotal, shipping cost, and tax rate <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.
*   **Notes** An optional notes section is available <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>.

### Summary Metrics

At the top of the database, a purchase order summary provides key metrics <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>:
*   **Total Purchases** The sum of all purchases recorded in the database <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>.
*   **Units Ordered** Calculated from the quantity columns of all descriptions <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>. Formulas need to be updated if more quantity columns are added <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>.
*   **Average Order Value** Computed by dividing total purchases by units ordered <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.

### Client Summary

The template includes a client summary section that tracks data for different clients (e.g., ABC Solutions, XYZ Manufacturing, LMN Enterprises) <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>. For each client, it shows:
*   Total purchases value <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>
*   Total quantities ordered <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>
*   Average order value <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>

### Template Customization

This is a simple template for tracking purchase order expenses <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>. For further customization, users can reach out via email <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>. This template supports the [[customizing_purchase_order_templates_in_notion | customizing purchase order templates in Notion]].

## Generating Purchase Order PDFs

PDF documents for purchase orders can be generated using PDF output.com <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.

### Using PDF Output.com

To generate PDFs, users need to log in to PDF output.com <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.
1.  **Select Template**: Choose "purchase PO template" from the dropdown menu <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>. Users can also request specific templates if not found <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>.
2.  **Select Currency**: Choose the desired currency (e.g., USD, Euro) <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>. Currencies not listed can be requested <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.

### Single PDF Generation

In "single PDF mode," one document can be generated at a time <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>.
1.  **Fill Details**: Populate the template fields with information from the Notion database, such as order date, expected delivery date, company details, item descriptions, quantities, and unit prices <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>.
2.  **Download PDF**: Click "Download PDF" to generate and obtain a clean and precise purchase order PDF <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>. The currency selection directly affects the generated PDF <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.

### Bulk PDF Export

For [[generating_purchase_order_pdfs_in_bulk | generating purchase order PDFs in bulk]], switch to "bulk export mode" <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>.
1.  **Fill Multiple Rows**: Input details for multiple purchase orders by adding new rows and filling in all necessary information <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.
2.  **Download Options**:
    *   Download individual documents by clicking on specific rows <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.
    *   Download all documents in one go by clicking "Download all PDF" <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>.

### Future Notion Integration

Future updates will include a direct Notion integration, allowing users to select their Notion database and export PDFs directly from it <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>.

Users are encouraged to provide feedback through the dedicated window to help improve the product <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.