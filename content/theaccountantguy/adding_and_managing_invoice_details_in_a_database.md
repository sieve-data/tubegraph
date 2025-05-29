---
title: Adding and managing invoice details in a database
videoId: IK71-I_O7Vg
---

From: [[theaccountantguy]] <br/> 

This article details how to track invoice payments and manage invoice details using a Notion template, along with methods for [[exporting_and_managing_invoice_documents | generating PDF documents]] from these details.

## Notion Invoice Payment Tracker Overview
The Notion template provides a system to track invoice payments, offering a quick summary of financial metrics <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>.

Key Performance Indicators (KPIs) displayed at the top include:
*   Total expenses incurred through invoices <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.
*   Total units purchased across all invoices <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.
*   Average invoice price <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.
These KPIs can be customized or updated as needed <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.

A client summary section shows:
*   Purchase value per client <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>.
*   Number of units purchased from each client <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.
*   Average purchase value from each client <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.

## Database Details
The core of the tracker is a database where all invoice details can be entered <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>. Fields available include:
*   Invoice number <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>
*   Invoice date <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>
*   Due date <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>
*   Company name (issuer of invoice) <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>
*   Bill to section and client address <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>
*   Description of purchased items (e.g., "item one," "item two") <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>
*   Quantity <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>
*   Unit price <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>
*   Subtotal (calculated as quantity multiplied by unit price) <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>
*   Tax rate <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>
*   Total amount (computed automatically) <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>
*   Notes (e.g., expected payment receipt, payment mode) <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>

### Customizing and Updating
To add more items beyond the default two, users can duplicate existing item columns (description, quantity, unit price) <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>. When duplicating columns, it's crucial to update the subtotal formula to include the new columns <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.

Changes to inputs in the database, such as quantity or price, automatically update the total expenses and units purchased displayed in the summary section <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>. The "total quantities purchased" property, which drives the overall units purchased, must also be updated with new quantities <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.

The client summary also updates automatically to reflect changes in purchases, units, and average values for each client <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.

This [[tracking_transactions_and_invoice_statuses | invoice payment tracker]] helps keep track of all invoices for a business <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.

## Generating PDF Documents for Invoices
For [[exporting_and_managing_invoice_documents | generating PDF documents]] for invoices, users can utilize PDF output.com <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.

### Single PDF Generation
1.  **Access the Website**: Navigate to PDF output.com and log in <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.
2.  **Select Template**: Use the drop-down menu on the top left to find and select the "invoice" template (search for "inv") <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>.
3.  **Fill Details**: Input invoice details such as invoice number, company name, address, item descriptions, quantities, and unit prices <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.
    *   The desired currency can be set, which will update the entire invoice accordingly <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.
4.  **Download PDF**: Click "Download PDF" to generate and download the invoice document <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.

### Bulk PDF Generation
PDF output.com also supports bulk PDF generation for multiple invoices <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.
1.  **Bulk Mode**: Switch to the "bulk PDF mode" <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.
2.  **Input Data**: Fill in details for multiple invoices by copying and pasting information into the rows provided <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.
    *   Currently, direct support for [[mapping_database_elements_to_invoice_templates | Notion database integration]] for bulk generation is not yet added but is planned <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>.
    *   Column width can be expanded for better visibility <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>.
    *   New rows can be added as needed <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.
3.  **Download Options**:
    *   "Download all PDF" generates all invoices one by one <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>.
    *   "Download PDF" on a specific row generates only that particular invoice <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.

## Support and Feedback
For any questions or queries regarding the [[tracking_transactions_and_invoice_statuses | invoice payments tracker]] or using PDF output.com for invoice generation, users can reach out via email at notionformyuse@gmail.com <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>. There is also a feedback window on the website for direct inquiries <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>.