---
title: Tracking invoice payments in Notion
videoId: IK71-I_O7Vg
---

From: [[theaccountantguy]] <br/> 

This article details how to track invoice payments using a dedicated Notion template and how to generate PDF invoices from the recorded data <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>.

## Notion Template Overview

The Notion template provides a comprehensive system for [[setting_up_notion_for_invoice_management | invoice management]] and tracking invoice payments <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>.

### Invoice Payment Summary (KPIs)
At the top of the template, a quick summary displays key performance indicators (KPIs) related to invoice payments <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>:
*   Total expenses incurred through invoices <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.
*   Total units purchased across all invoices <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.
*   Average invoice price <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.
These KPIs can be customized or new ones can be added <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.

### Client Summary
A client summary section shows purchase details against each client, including:
*   Total purchases <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>.
*   Number of units purchased <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.
*   Average purchase value from each client <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.

### Invoice Database Details
The core of the system is a database where all invoice details are recorded <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>. Key fields include:
*   Invoice number <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.
*   Invoice date <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.
*   Due date <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.
*   Company name (who issues the invoice) <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.
*   "Bill to" section and client address <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.
*   Description of purchased items (e.g., "item one," "item two") <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.
*   Quantity and unit price for each item <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.
*   Subtotal (calculated as quantity multiplied by unit price) <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.
*   Tax rate <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>.
*   Total amount (computed based on subtotal and tax) <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.
*   Notes, such as expected payment receipt or mode of payment <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.

### Customization and Formulas
To add more items beyond the default two, users can duplicate existing item columns (description, quantity, unit price) <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>. It's crucial to update the formulas for subtotal, total expenses, and total quantities purchased to include the new columns so that the KPIs update automatically <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>. For example, changing an input value in the database will automatically reflect in the "total expenses" and "units purchased" at the top of the template <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.

## Generating PDF Invoices

The system integrates with an external website, PDFoutput.com, to generate PDF documents for each invoice <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.

### Single PDF Generation
1.  **Access PDFoutput.com:** Log in to the website <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.
2.  **Select Template:** Use the dropdown menu on the top left to find the "invoice" template by searching for "inv" <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.
3.  **Fill in Details:** Input all the necessary invoice details, including invoice number, company name, address, and item specifics (quantity, unit price) <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>. The desired currency can be set, and the entire invoice will update accordingly <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.
4.  **Download PDF:** Click "Download PDF" to generate and save the invoice document <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.

### Bulk PDF Generation
PDFoutput.com also offers a "bulk PDF mode" <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>. While direct Notion database support for bulk generation is not yet available, users can manually fill in rows of information (or copy-paste) <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>. After filling in the details for multiple invoices, clicking "Download all PDF" will generate each PDF one by one <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>. Individual PDFs can also be generated from specific rows in bulk mode <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>.

## Support and Feedback

For any questions or queries regarding the use of the invoice payments tracker or PDF output for invoice generation, users can contact `notionformyuse@gmail.com` <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>. A feedback window is also available on the platform for direct communication <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>.