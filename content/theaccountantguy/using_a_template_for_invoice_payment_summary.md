---
title: Using a template for invoice payment summary
videoId: IK71-I_O7Vg
---

From: [[theaccountantguy]] <br/> 

This article details a Notion template designed to track invoice payments, providing a comprehensive summary of expenses, purchased units, and average invoice prices. It also covers the integration with PDFoutput.com for [[using_templates_to_generate_pdf_invoices | generating PDF invoices]].

## Invoice Payment Tracker Template Overview

The provided template offers a quick invoice payment summary at the top <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. Key Performance Indicators (KPIs) include:
*   Total expenses incurred through invoices <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.
*   Total units purchased across all invoices <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.
*   Average invoice price <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

These KPIs can be customized or updated as needed <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.

## Client Summary

A dedicated client summary section shows:
*   Purchase amounts per client <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>.
*   Units purchased per client <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.
*   Average purchase value from each client <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.

For example, for "11 Enterprises," the template reflects total purchases of $189 and a total of 44 units purchased, derived from summing quantities like 31 and 13 <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.

## Invoice Database Details

The core of the template is a database where all invoice details can be entered <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>. This includes:
*   Invoice number <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>
*   Invoice date <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>
*   Due date <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>
*   Company name (issuing the invoice) <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>
*   Bill-to section and client address <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>
*   Description of items purchased (e.g., "item one" and "item two") <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>
*   Quantity and unit price for each item <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>

The subtotal is calculated automatically by multiplying the unit price and quantity <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>. A tax rate is added, and the total amount is computed <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>. Notes, such as payment receipt timing or mode of payment, can also be added <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.

### Customizing Item Rows and Formulas

To add more items beyond the default two, users can duplicate existing columns <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>. When new columns are added, it is essential to update the formula for the subtotal calculation to include these new columns <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>. After updating, all linked summaries, such as total expenses and units purchased, will automatically reflect the changes <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. For example, altering inputs in the database instantly updates the total expenses and units purchased displayed at the top <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>. The "total quantities purchased" property, used for the top summary, also requires formula updates when more quantity columns are added <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.

## Generating PDF Invoices with PDFoutput.com

The template integrates with PDFoutput.com to [[using_templates_to_generate_pdf_invoices | generate PDF invoices]] from the data entered in Notion <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.

### Single PDF Generation
1.  Access PDFoutput.com and log in <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.
2.  Select the desired [[creating_and_using_an_invoice_template_in_notion | invoice template]] from the drop-down menu (search "inv") <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>.
3.  Fill in the invoice details, including invoice number, company name, address, and item specifics <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.
4.  The currency can be changed, which updates the entire invoice accordingly <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.
5.  Click "Download PDF" to generate the invoice <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>. The generated PDF will show quantity, unit price, total value, and any added notes <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.

### Bulk PDF Generation
PDFoutput.com also supports bulk PDF generation <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>. Users can fill in multiple rows of invoice information manually or copy-paste data <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>. While direct support for Notion database import is not yet implemented, it is planned <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.
*   To add new invoice rows, click "add new row" <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.
*   Click "Download all PDF" to generate all invoices at once <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>.
*   Alternatively, generate a single PDF for a specific row by clicking "Download PDF" on that row <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>.

## Support and Feedback

For any questions or assistance regarding the invoice payments tracker or utilizing PDFoutput.com to [[using_templates_to_generate_pdf_invoices | generate invoice documents]], users can contact notionformyuse@gmail.com <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>. A feedback window is also available on the platform for direct communication <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>.