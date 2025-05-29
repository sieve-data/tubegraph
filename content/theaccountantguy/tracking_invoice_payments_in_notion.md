---
title: Tracking invoice payments in Notion
videoId: IK71-I_O7Vg
---

From: [[theaccountantguy]] <br/> 

This article details how to [[invoicing_and_payment_tracking_through_notion | track invoice payments]] using a dedicated [[notion | Notion]] template and how to generate PDF invoices.

## Notion Invoice Payment Tracker Template

The [[notion | Notion]] template provides a comprehensive system for managing invoices <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>.

### Invoice Payment Summary (KPIs)

At the top of the template, a quick summary displays key performance indicators (KPIs) <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>:
*   Total expenses incurred through invoices <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.
*   Total units purchased from all combined invoices <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.
*   Average invoice price <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

These KPIs can be customized or updated as needed for a business <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>.

### Client Summary

Below the KPIs, a client summary shows details for each client <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>:
*   Total purchases made <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.
*   Number of units purchased <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.
*   Average purchase value <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.

### Invoice Database

The core of the template is a database where all invoice details can be entered <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.
Details include:
*   Invoice number <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.
*   Invoice date <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.
*   Due date <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.
*   Company name (issuing the invoice) <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.
*   "Bill to" section and client address <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.
*   Description of items purchased (e.g., Item 1, Item 2) <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.
*   Quantity for each item <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.
*   Unit price for each item <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.

The subtotal is computed by multiplying the unit price and quantity for each item <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>. A tax rate can be added, and the total amount is automatically computed <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>. Notes, such as expected payment receipt or mode of payment, can also be included <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.

### Customization and Formulas

To add more items beyond the initial two, duplicate the existing item columns and update the formula for the subtotal to include the new columns <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>. This ensures that all calculations update automatically <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. The KPIs at the top, such as total expenses and units purchased, are derived from the database figures and automatically reflect any changes made to the inputs <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>. Similarly, the `total quantities purchased` property, which influences the top-level KPIs, needs to be updated with new quantity columns <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.

## Generating PDF Invoices

The invoice tracker can be complemented by a tool to generate PDF documents for each invoice.

### Using PDF Output.com

PDF Output.com is a website that allows users to create invoice PDF documents <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.
1.  **Log In**: Access the website and log in <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.
2.  **Select Template**: Use the drop-down menu on the top left to find and select the "invoice" template (search for "inv") <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>.
3.  **Fill Details**: Manually enter the invoice details, including invoice number, company name, address, and item specifics <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>. The values, including currency (which can be changed), will reflect on the invoice <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
4.  **Download PDF**: Click "Download PDF" to generate and download the invoice document <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>. The generated PDF will show quantity, unit price, computed total, and notes <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.

### Bulk PDF Generation

PDF Output.com also offers a "bulk PDF mode" <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.
*   Users can fill in multiple rows of invoice information, similar to how data is structured in the [[notion | Notion]] database, by copy-pasting <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>. While direct [[notion | Notion]] database support is not yet available, users can manually fill in details <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.
*   After filling in details for multiple invoices, click "Download All PDF" to generate all documents one by one <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.
*   Individual PDFs for specific rows can also be generated by clicking "Download PDF" on that particular row <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>.

## Support and Feedback

For any questions or queries regarding the use of the [[invoicing_and_payment_tracking_through_notion | invoice payments tracker]] or PDF Output.com, users can reach out via email at notionformyuse@gmail.com <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>. There is also a feedback window available for sending queries directly <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>.