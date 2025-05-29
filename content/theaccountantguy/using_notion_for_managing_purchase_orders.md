---
title: Using Notion for managing purchase orders
videoId: zlLWtZdPvLk
---

From: [[theaccountantguy]] <br/> 

This guide explains how to utilize a Notion template to manage and track purchase orders, including generating PDF documents. The template is designed to help maintain a clear record of purchase order expenses <a class="yt-timestamp" data-t="02:27:54">[02:27:54]</a>.

## Purchase Order Tracker Template Overview
The Notion purchase order tracker template provides a structured way to keep track of your purchase orders <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>.

### Database Fields
The template features a database with various columns essential for managing purchase orders <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>:
*   Purchase order number <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>
*   Order date <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>
*   Expected delivery date <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>
*   Terms and conditions <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>
*   Company name <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>
*   Company address <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>
*   Supplier name <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>
*   Description of items <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>
*   Quantity <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>
*   Unit price <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>
*   Shipping cost amount <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>
*   Tax rate (in percentage) <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>
*   Notes <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>

Additional item descriptions, quantities, and unit prices can be added by duplicating existing columns <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.

### Automated Calculations
The template automatically computes several values:
*   **Subtotal amount**: This is calculated as the summation of the unit price and quantity for each description <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. If new description columns are added, the formula for the subtotal needs to be updated manually <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.
*   **Total amount**: This is derived by including the shipping cost and applying the tax rate to the subtotal <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>.

### Summary Dashboards
The template provides an immediate overview of purchase order data through summary dashboards:
*   **Purchase Order Summary**:
    *   **Total purchase**: The sum of all purchases made <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.
    *   **Units ordered**: The total units calculated from all quantity columns <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>. Remember to update the formulas if new quantity columns are added <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.
    *   **Average order value**: Computed by dividing the total purchases by the units ordered <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.
*   **Client Summary**: Provides metrics for individual clients, such as ABC Solutions, XYZ Manufacturing, and LMN Enterprises <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>.
    *   Total purchases value per client <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.
    *   Total quantities ordered from each client <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.
    *   Average order value per client <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.

## [[generating_purchase_order_pdfs_using_notion | Generating Purchase Order PDFs]]

PDF documents for purchase orders can be generated using PDFoutput.com <a class="yt-timestamp" data-t="02:31:56">[02:31:56]</a>.

### PDFoutput.com Workflow
1.  **Login**: Access PDFoutput.com <a class="yt-timestamp" data-t="02:55:76">[02:55:76]</a>.
2.  **Select Template**: Choose the "Purchase Order" template from the dropdown menu <a class="yt-timestamp" data-t="03:01:05">[03:01:05]</a>.
3.  **Select Currency**: Choose the desired currency; additional currencies can be requested if not available <a class="yt-timestamp" data-t="03:11:58">[03:11:58]</a>.
4.  **Input Data**: Manually fill in all the details from the Notion database into the corresponding fields on the PDFoutput.com interface <a class="yt-timestamp" data-t="03:53:74">[03:53:74]</a>. The total amount displayed in PDFoutput.com should match the total amount in Notion <a class="yt-timestamp" data-t="04:02:72">[04:02:72]</a>.

### Single PDF Export
In "Single PDF mode," you can generate one PDF document at a time <a class="yt-timestamp" data-t="03:23:44">[03:23:44]</a>. After filling in the data, click "Download PDF" to generate and download the document <a class="yt-timestamp" data-t="04:14:00">[04:14:00]</a>. The generated PDF will be clean and precise, reflecting the chosen currency <a class="yt-timestamp" data-t="04:21:00">[04:21:00]</a>.

### Bulk PDF Export
For generating multiple purchase order PDFs at once, switch to "Bulk Export mode" <a class="yt-timestamp" data-t="04:55:92">[04:55:92]</a>.
1.  **Fill Details**: Input all the details for multiple purchase orders by adding new rows <a class="yt-timestamp" data-t="05:00:19">[05:00:19]</a>.
2.  **Download Options**: You can download individual documents or download all documents at once by clicking "Download All PDF" <a class="yt-timestamp" data-t="05:08:44">[05:08:44]</a>.

### Future Notion Integration
A future update for PDFoutput.com will include direct Notion database integration. This will allow users to select their Notion database and directly export information to generate PDFs without manual input <a class="yt-timestamp" data-t="05:22:98">[05:22:98]</a>.

## Customization and Support
This is a simple template designed for ease of use <a class="yt-timestamp" data-t="02:14:15">[02:14:15]</a>. For further customization or assistance, you can reach out via email at notionformyuse@gmail.com <a class="yt-timestamp" data-t="02:18:24">[02:18:24]</a>. Feedback for improving the product can also be submitted through the feedback window on PDFoutput.com <a class="yt-timestamp" data-t="05:59:74">[05:59:74]</a>.