---
title: Customizing sales receipt templates
videoId: p9M2n3vwLMs
---

From: [[theaccountantguy]] <br/> 

This article details how to utilize a sales receipts tracker template and how to [[generating_sales_receipts_in_pdf_format | generate sales receipts in PDF format]] using a dedicated tool <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.

## Sales Receipts Tracker Template

The sales receipts tracker template features a sales receipts database designed to help track sales <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>.

### Database Fields
The database includes essential fields for tracking sales <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>:
*   **Receipt Number** <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>
*   **Receipt Date** <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>
*   **Payment Method**: Offers several options for clearing payments <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>.
*   **Business Name and Address**: Users can input their own business details <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.
*   **Customer Details**: This is a relational property, linking to another database containing client information <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.
*   **Description**: Details what is being sold <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>.
*   **Quantity of Sales** <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>
*   **Unit Price** <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>

Users can add multiple descriptions, quantities, and unit prices for various items within a single sale by utilizing multiple rows <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>. The subtotal column automatically sums the total amount for individual items sold <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.
*   **Tax Rate** <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>
*   **Total Amount**: Automatically computed <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.
*   **Notes**: For any relevant information regarding payments <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.

Some additional columns are linked to other databases <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.

### Sales Receipt Summary
A summary section at the top displays key metrics <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>:
*   **Total Sales**: Drawn from the sales value <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.
*   **Units Sold**: Based on the quantity of sales <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>.
*   **Average Sales Value**: Calculated as total sales divided by units sold, providing key performance indicator (KPI) information for the business <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.

If additional columns are added for descriptions and quantities, the formulas for the subtotal amount and total amount need to be updated accordingly to ensure accurate computation <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>. Similarly, for the "quantity sold" column, if more quantities are added for corresponding descriptions, these must also be added to the calculation <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.

### Client Summary
A client summary section provides specific insights per client <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>:
*   **Total Sales for Each Client** <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.
*   **Total Quantity of Sales** made to each client <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.
*   **Average Sales Price** for every client <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>.

This template can be [[customizing_pdf_templates_for_specific_needs | customized]] to specific requirements <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>. For further assistance with customization, users can reach out via notionformyuse@gmail.com <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.

## Generating PDF Sales Receipts

A separate tool, PDFOutput.com, can be used to [[generating_sales_receipts_in_pdf_format | generate sales receipts as PDF documents]] <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>.

### Process for Single PDF Generation
1.  **Navigate to PDFOutput.com** <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.
2.  **Select Template**: Use the "template selection" dropdown to find and open the "sales receipts" template <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.
3.  **Fill in Information**: Input details such as receipt number, receipt date, payment method, business name, address, and item specifics (description, quantity, unit price) <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.
4.  **Tax Rate and Notes**: Enter the tax rate and any relevant notes <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.
5.  **Select Currency**: Choose the desired currency (e.g., US Dollars, Euro), which automatically updates the template <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.
6.  **Download PDF**: Click "Download PDF" to generate the sales receipt document <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>.

### Bulk PDF Export
The tool also supports exporting PDF documents in bulk <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
1.  **Select Bulk Export Mode**: Choose "bulk export mode document" <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.
2.  **Add Data as a Database**: Input all sales receipt information into a database format within the tool <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>.
    *   Column widths and row heights can be resized for better readability <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.
    *   Rows can be added or deleted as needed <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>. Individual items within a row can also be deleted <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>.
3.  **Download All PDFs**: Click "Download all PDF" to generate all documents in one go <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>. Alternatively, specific PDFs can be downloaded by clicking on individual rows <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>.
4.  **Currency Update**: Changing the currency setting will automatically reflect in all generated PDFs <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>.

### Requesting Templates and Feedback
Users can request specific templates via the "request template" option, which sends a direct message to the developer <a class="yt-timestamp" data-t="00:07:52">[00:07:52]</a>. Feedback can also be provided through the "feedback window" <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>.

For any queries regarding the database or the PDF output tool, contact notionformyuse@gmail.com or use the feedback window <a class="yt-timestamp" data-t="00:08:07">[00:08:07]</a>.