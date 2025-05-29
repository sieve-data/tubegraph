---
title: Tracking invoice payments in Notion
videoId: IK71-I_O7Vg
---

From: [[theaccountantguy]] <br/> 
This article details how to [[tracking_invoice_payments_in_notion | track invoice payments in Notion]] using a dedicated template and how to generate corresponding PDF documents.

## Invoice Payment Tracker Template in Notion
The Notion template for [[tracking_invoice_payments_in_notion | tracking invoice payments]] provides a comprehensive system for managing invoices <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>.

### Summary Sections
The template features two main summary sections at the top:
*   **Invoice Payment Summary** This section displays key performance indicators (KPIs) related to invoices, such as:
    *   Total expenses incurred through invoices <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>
    *   Total units purchased across all invoices <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>
    *   Average invoice price <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>
    *   These KPIs can be customized or updated <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>.
*   **Client Summary** This section provides insights per client, including:
    *   Total purchases made from each client <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>
    *   Number of units purchased from each client <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>
    *   Average purchase value from each client <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>

### Invoice Database
A central database forms the core of the template, allowing users to input and manage detailed invoice information <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.
*   **Core Fields** Each entry includes:
    *   Invoice number <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>
    *   Invoice date <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>
    *   Due date <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>
    *   Company name (issuing the invoice) <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>
    *   Bill-to section and client address <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>
*   **Itemized Details** For each invoice, details about purchased items can be added, including:
    *   Item description <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>
    *   Quantity <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>
    *   Unit price <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>
*   **Calculations**
    *   **Subtotal** is automatically calculated by multiplying the unit price and quantity for each item <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.
    *   **Total amount** is computed by adding the tax rate to the subtotal <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>.
*   **Additional Information** A "Notes" section is available for details such as payment receipt speed or mode of payment <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.
*   **Customization and Automation**
    *   More item columns can be added by duplicating existing ones <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>. When adding new columns, ensure to update the relevant formulas (e.g., for subtotal and total quantities purchased) to include the new columns <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a> <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.
    *   The total expenses and units purchased KPIs automatically update as data in the database changes <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.

## Generating PDF Invoices
The article also demonstrates how to generate PDF documents for invoices using a third-party tool, PDF output.com <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.

### Single PDF Generation
To generate a single invoice PDF:
1.  Log in to PDF output.com <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>.
2.  Select the "invoice" template from the dropdown menu <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a> <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.
3.  Fill in all the invoice details, such as invoice number, company name, address, item details, quantity, and unit price <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a> <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>.
4.  The desired currency can be set, which will update the entire invoice accordingly <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.
5.  Click "Download PDF" to generate the document <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.

### Bulk PDF Generation
PDF output.com also supports generating multiple invoice PDFs in bulk <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.
1.  Navigate to the "bulk PDF mode" <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.
2.  Input multiple rows of invoice information, which can be copied from the Notion database <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>. Support for direct integration with the Notion database is planned <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.
3.  The column width can be expanded for better viewing <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>.
4.  Click "Download all PDF" to generate all documents one by one <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>.
5.  Individual PDFs can also be generated from specific rows within the bulk mode <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>.