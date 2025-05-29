---
title: Setting up a sales receipts database
videoId: p9M2n3vwLMs
---

From: [[theaccountantguy]] <br/> 

A sales receipts tracker template can be utilized to keep track of sales data <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. This system, often implemented within a platform like [[using_notion_to_track_sales_receipts | Notion]], helps organize and analyze sales information for a business <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>.

## Sales Receipts Database Structure

The core of the sales receipts tracker is a database that contains comprehensive information for tracking sales <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. Key fields include:

*   **Receipt Number** <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>
*   **Receipt Date** <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>
*   **Payment Method** – This is a selectable field with various payment options <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>.
*   **Business Name** and **Address** – Users can enter their own business details <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.
*   **Customer Details** – A relational property linked to another database containing client information <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.
*   **Description** – Details about what is being sold <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>. Multiple descriptions can be added for different items sold in a single transaction <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.
*   **Quantity** <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>
*   **Unit Price** <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>
*   **Subtotal** – Automatically sums the total amount of individual items sold within a row <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.
*   **Tax Rate** <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>
*   **Total Amount** – Computed automatically based on the subtotal and tax rate <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.
*   **Notes** – For any relevant notes regarding the payment or sale <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.

Additional columns may be linked to other databases for further integration <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>.

## Sales Receipt Summary

A summary section provides key performance indicators related to sales <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>:

*   **Total Sales** – Derived from the sales value within the database <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.
*   **Units Sold** – Represents the total quantity of items sold <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>. If additional description and quantity columns are added, the formulas for subtotal, total amount, and units sold must be updated accordingly <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.
*   **Average Sales Value** – Calculated as Total Sales divided by Units Sold, providing key business insights <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.

## Client Summary

This section provides a breakdown of sales data specific to each client <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>:

*   **Total Sales for Each Client** <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>
*   **Total Quantity of Sales Made to Each Client** <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>
*   **Average Sales Price for Every Client** <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>

The client summary can be [[customizing_sales_receipt_templates | customized]] to fit specific reporting needs <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>.

## Customization and Support

The sales receipts template is designed for customization <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>. For further customization or assistance with the database, users can reach out via email <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.

## Generating Sales Receipts Documents

Beyond tracking, this system can be integrated with tools to [[generating_sales_receipts_pdf_documents | generate sales receipts PDF documents]] for business purposes <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>. An external tool like PDFoutput.com allows users to select a sales receipt template, input details (receipt number, date, payment method, business name, address, items, quantities, unit prices, tax rate, notes, and currency), and download individual PDF documents <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>.

### Bulk Export

The system also supports [[bulk_exporting_sales_receipts_as_pdf | bulk exporting sales receipts as PDF]] documents <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>. Users can input multiple sales receipt details into a database interface within the PDF generation tool and then download all corresponding PDFs in one go <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>. Column widths and row heights can be adjusted for data entry <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>. Users can add or delete rows and individual items as needed <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>. The currency can be changed, and the PDF output will automatically update <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>.