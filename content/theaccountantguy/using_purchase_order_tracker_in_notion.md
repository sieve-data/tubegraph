---
title: Using purchase order tracker in Notion
videoId: zlLWtZdPvLk
---

From: [[theaccountantguy]] <br/> 

This article details how to utilize a Notion template to track purchase orders and manage related expenses, as well as how to [[generating_purchase_order_pdfs_using_notion | generate PDF documents]] for these orders.

## Notion Purchase Order Tracker Template

The Notion purchase order tracker template is designed to help users keep track of their purchase orders effectively <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. This simple template can be used to monitor [[expense_tracking_using_notion | purchase order expenses]] <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.

### Database Structure
The core of the tracker is a database that includes several key columns <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>:
*   **Purchase Order Number** <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>
*   **Order Date** <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>
*   **Expected Delivery Date** <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>
*   **Terms and Conditions** <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>
*   **Company Name** <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>
*   **Company Address** <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>
*   **Supplier Name** <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>
*   **Notes** <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>

### Item Details and Calculations
For tracking individual items within a purchase order, the template includes:
*   **Description** <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>
*   **Quantity** <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>
*   **Unit Price** <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>

> [!NOTE] Adding More Items
> To add more item descriptions, quantities, and unit prices, simply duplicate the existing columns by clicking on them and selecting "duplicate" <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. Input the details for the new items, and the subtotal will automatically compute <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>.

The template automatically computes the **subtotal amount** for items, which is a summation of the unit price and quantity for all descriptions <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

Other calculated fields include:
*   **Shipping Cost** <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>
*   **Tax Rate (in percentage)** <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>
*   **Total Amount** <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>

> [!IMPORTANT] Formula Updates
> When adding more descriptions and quantities, ensure that the formulas for calculations (like subtotal) are updated to reflect the new columns; otherwise, the values in the database will not change accordingly <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>.

## Purchase Order Summary

At the top of the Notion page, a purchase order summary provides an overview of all orders <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>. This summary includes:
*   **Total Purchases:** The sum of all purchases made <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>.
*   **Units Ordered:** Calculated from the quantity columns of all descriptions <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.
*   **Average Order Value:** The total purchases divided by the units ordered, computed automatically <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.

### Client Summary

The template also features a client summary, providing insights into specific clients. For example, for clients like ABC Solutions, XYZ Manufacturing, and LMN Enterprises <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>, the summary displays:
*   Total purchases value <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>
*   Total quantities ordered from each client <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>
*   Average order value for each client <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>

## Generating Purchase Order PDFs

In addition to tracking, the template supports [[generating_purchase_order_pdfs_using_notion | generating PDF documents]] for purchase orders using PDFoutput.com <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.

### Single PDF Mode
1.  **Log in to PDFoutput.com**: This is the first step to access the interface for PDF generation <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.
2.  **Select Template**: Choose "Purchase Order" from the dropdown menu on the left <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>. You can also request a specific template if it's not available <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>.
3.  **Choose Currency**: Select the desired currency (e.g., USD, Euro) from the dropdown <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>. New currencies can be requested if needed <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.
4.  **Fill Details**: Input all necessary information into the template fields, such as order date, expected delivery date, descriptions, quantities, and unit prices <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.
5.  **Download PDF**: Once all details are filled, click "Download PDF" to generate the document <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>. The generated PDF will be clean and precise, reflecting the chosen currency <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.

### Bulk Export Mode
For generating multiple purchase order PDFs at once, switch to the bulk export mode <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>.
1.  **Fill Multiple Rows**: Input all the details for multiple purchase orders into the respective rows <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>. New rows can be added using the "add new row" button <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.
2.  **Download Options**: You can choose to download individual documents or download all documents in one go by clicking "Download all PDF" <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.

> [!INFO] Future Notion Integration
> An upcoming feature will allow direct integration with a Notion database, enabling users to select their Notion database and export PDF documents by reading information directly from it <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>.

For further customization of the template, reach out to notionformyuse@gmail.com <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>.