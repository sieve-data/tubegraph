---
title: Setting up a sales receipts database
videoId: p9M2n3vwLMs
---

From: [[theaccountantguy]] <br/> 

This article details how to utilize a sales receipts tracker template to manage and keep track of sales, as well as how to generate PDF documents for these receipts <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>.

## Sales Receipts Database Overview

The sales receipts database provides all the necessary information to track sales <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.

### Key Fields

The database includes the following key information:
*   **Receipt Number** <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>
*   **Receipt Date** <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>
*   **Payment Method**: This field allows selection from several payment clearing options <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>.
*   **Business Name** and **Address**: You can enter your own business details here <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.
*   **Customer Details**: This is a relational property linked to another database containing client information <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.
*   **Description**: Details what is being sold <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>.
*   **Quantity of Sales** <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>
*   **Unit Price** <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>

You can add multiple descriptions, quantities, and unit prices for a single sale, with each row representing a different item being sold <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.

### Financial Calculations

*   **Subtotal Column**: Sums up the total amount of individual items sold <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.
*   **Tax Rate**: Applied after the subtotal <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.
*   **Total Amount**: Automatically computed <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.
*   **Notes Column**: For any related notes needed to clear payments <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.

### Summary Sections

The database includes summary sections for quick insights:

#### Sales Receipt Summary
This section shows key performance indicators (KPIs) for the business <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.
*   **Total Sales**: Drawn from the sales value <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.
*   **Units Sold**: Reflects the quantity of sales <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.
*   **Average Sales Value**: Calculated as total sales divided by units sold <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.

> [!CAUTION] Formula Updates
> If additional columns are added for descriptions and quantities, ensure that the formulas for the subtotal amount, total amount, and quantity sold are updated accordingly for accurate computation <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.

#### Client Summary
This section provides a breakdown of sales per client:
*   Total sales for each client <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.
*   Total quantity of sales made to each client <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>.
*   Average sales price for every client <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>.

### Customization and Support
The template can be customized to meet specific requirements <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>. For further customization or assistance, you can reach out via notionformyuse@gmail.com <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.

## [[generating_pdf_documents_for_sales_receipts | Generating PDF Documents for Sales Receipts]]

Sales receipt PDF documents can be generated for businesses using a tool called PDF Output.com <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.

### Steps to Generate Individual PDF Sales Receipts
1.  **Navigate to PDF Output.com** <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.
2.  **Select a Template**: Click on the "template selection" dropdown at the top and search for the desired template, such as "sales receipts" <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.
3.  **Fill in Information**: Enter all required details, including receipt number, date, payment method, business name, address, customer details, item descriptions, quantities, unit prices, tax rate, and notes <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.
    *   The platform calculates the subtotal and total amount automatically <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>.
4.  **Select Currency**: Choose the desired currency (e.g., US dollars, Euro) which will update automatically <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.
5.  **Download PDF**: Click "Download PDF" to generate and download the sales receipt PDF document <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.

### Steps to [[generating_bulk_payment_receipts | Generate Bulk PDF Sales Receipts]]
For bulk generation of PDF documents:
1.  **Select Bulk Export Mode**: On PDF Output.com, choose the "bulk export mode document" option <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.
2.  **Add Database Information**: Input all sales receipt details into the provided database interface <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.
    *   Columns can be resized to improve readability <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.
    *   New rows can be added using the "add new row" button <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>.
    *   Rows or individual items can be deleted using the respective icons <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.
3.  **Download All PDFs**: Click "Download all PDF" to download all the generated PDFs in one go <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>.
    *   Alternatively, individual PDFs can be downloaded by clicking on specific rows <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>.
4.  **Currency Adjustments**: Changing the currency setting will automatically update the currency symbol in all generated PDFs <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>.

### Template Requests and Feedback
If a specific template is needed that is not available, you can click "request template" to send a direct request <a class="yt-timestamp" data-t="00:07:53">[00:07:53]</a>. Feedback can also be sent through the feedback window <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>. For queries, contact notionformyuse@gmail.com <a class="yt-timestamp" data-t="00:08:07">[00:08:07]</a>.