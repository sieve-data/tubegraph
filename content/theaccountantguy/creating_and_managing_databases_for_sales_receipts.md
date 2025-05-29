---
title: creating and managing databases for sales receipts
videoId: p9M2n3vwLMs
---

From: [[theaccountantguy]] <br/> 

This article explains how to utilize a sales receipts tracker template to keep track of sales and how to generate PDF documents for these receipts. It covers [[setting_up_databases_in_notion | database setup]] for sales information and external tools for document generation.

## Sales Receipts Tracker Template Overview

The sales receipts tracker template features a sales receipts [[setting_up_a_database_in_notion_for_financial_tracking | database]] designed to help businesses track sales. <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>

### Sales Receipts Database Structure

The main sales receipts [[creating_databases_for_an_expense_tracker_in_notion | database]] contains comprehensive information for tracking sales:
*   **Receipt Number** <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>
*   **Receipt Date** <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>
*   **Payment Method**: A dropdown list allows selection of various payment clearing methods. <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>
*   **Business Name and Address**: Fields to enter your business name and address. <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>
*   **Customer Details**: This is a relational property linked to another [[managing_customer_database_and_payments | database]] containing client information. <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>
*   **Description**: Details of what was sold. <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>
*   **Quantity of Sales** <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>
*   **Unit Price** <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>
    *   Multiple descriptions, quantities, and unit prices can be added for a single sale by adding more rows within the same receipt entry. <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>
*   **Subtotal**: This column sums up the total amount of individual items sold. <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>
*   **Tax Rate**: Applied to the subtotal. <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>
*   **Total Amount**: Automatically computed based on subtotal and tax rate. <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>
*   **Notes**: A column for any related notes regarding the payment. <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>
*   **Additional Columns**: Some columns are linked to other [[setting_up_a_database_in_notion_for_financial_tracking | databases]] to provide further context and understanding of the links. <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>

### Sales Receipt Summary

A summary section at the top provides key performance indicators (KPIs) for your sales:
*   **Total Sales**: Drawn directly from the sales value in the [[setting_up_a_database_in_notion_for_financial_tracking | database]]. <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>
*   **Units Sold**: Reflects the quantity of sales from the main [[setting_up_a_database_in_notion_for_financial_tracking | database]]. <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>
    *   If additional columns are added for descriptions and quantities, formulas for the subtotal and total amount must be updated accordingly. <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>
*   **Average Sales Value**: Calculated by dividing total sales by units sold, providing a key insight for [[managing_accounts_and_transactions_for_small_businesses | business tracking]]. <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>

### Client Summary

The client summary section breaks down sales information by individual client:
*   **Total Sales per Client**: Shows the aggregate sales made to each client. <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>
*   **Total Quantity of Sales per Client**: Displays the total units sold to each client. <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>
*   **Average Sales Price for Every Client**: Provides the average price for sales made to each client. <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>

This template can be [[setting_up_and_customizing_notion_database_for_invoices | customized]] to fit specific requirements. <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a> For further assistance, contact notionformyuse@gmail.com. <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>

## Generating Sales Receipt PDF Documents with PDF Output

Beyond tracking in Notion, tools like PDF Output.com can generate sales receipt PDF documents for business needs. <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>

### Generating a Single PDF Document

1.  **Visit PDF Output.com**: Navigate to the website. <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>
2.  **Select Template**: From the template selection dropdown, choose "Sales Receipts." <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>
3.  **Fill Information**: Input all necessary details, such as receipt number, date, payment method, business name, address, item descriptions, quantities, unit prices, and tax rates. <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>
    *   The system automatically calculates subtotals and totals based on the input. <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>
4.  **Select Currency**: Choose the desired currency (e.g., US Dollars, Euro). <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>
5.  **Download PDF**: Click "Download PDF" to generate and download the single sales receipt document. <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>

### Bulk Exporting PDF Documents

PDF Output.com also supports bulk export of PDF documents, useful for generating multiple receipts simultaneously. <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>

1.  **Choose Bulk Export Mode**: Select the "bulk export mode document" option. <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>
2.  **Input Data in Database Format**: Enter all sales receipt details into a table-like format within the tool. <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>
    *   Columns can be resized and row heights adjusted for readability. <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>
    *   New rows can be added, and individual items or rows can be deleted. <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>
3.  **Download All PDFs**: Click "Download all PDF" to generate and download all the receipts in one go. <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>
    *   Alternatively, individual rows can be selected to download specific PDFs. <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>
    *   The currency setting applies to all generated PDFs. <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>

### Customization and Support

For specific template requests or feedback, users can utilize the "Request Template" or "Feedback Window" features on PDF Output.com, which directly communicate with the support team. <a class="yt-timestamp" data-t="00:07:52">[00:07:52]</a> For general queries about the database or PDF output, contact notionformyuse@gmail.com. <a class="yt-timestamp" data-t="00:08:07">[00:08:07]</a>