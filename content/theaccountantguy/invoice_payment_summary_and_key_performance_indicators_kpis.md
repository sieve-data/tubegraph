---
title: Invoice payment summary and key performance indicators KPIs
videoId: IK71-I_O7Vg
---

From: [[theaccountantguy]] <br/> 

This article explores how to track invoice payments and related key performance indicators (KPIs) using a Notion template, along with methods for generating invoice documents.

## Invoice Payment Summary and Key Performance Indicators (KPIs)

A Notion template is presented for tracking invoice payments <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. The template features a quick invoice payment summary at the top <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>, which functions as a [[using_a_summary_section_to_track_payment_totals | summary section to track payment totals]]. This summary displays key metrics:
*   Total expenses incurred through invoices <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.
*   Total units purchased across all invoices <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.
*   Average invoice price <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

These are considered essential [[KPI information for hotel bookings | KPIs]] for a business <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>. The template allows for adding new [[KPI information for hotel bookings | KPIs]] or updating existing ones <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. The displayed total expenses and units purchased are derived from the underlying database <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.

### Client Summary

Below the main summary, there is a client summary section <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. This summary provides insights into purchases made from specific clients, detailing:
*   Total amount of purchases <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.
*   Number of units purchased <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.
*   Average purchase value from each client <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.

### Invoice Details Database

The core of the tracking system is a database where all invoice details are entered <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>. This database includes fields for:
*   Invoice number <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>
*   Invoice date <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>
*   Due date <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>
*   Company name (issuer) <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>
*   Bill-to section and client address <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>
*   Description of purchased items (e.g., "item one," "item two") <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>
*   Quantity <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>
*   Unit price <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>
*   Subtotal (calculated as quantity multiplied by unit price) <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>
*   Tax rate <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>
*   Total amount (computed after tax) <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>
*   Notes, including payment receipt speed or mode of payment <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>

### Adding More Items and Updating Formulas

To add more items beyond the default two, users can duplicate existing item columns <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>. When new item columns are added, it is crucial to update the formulas for the subtotal and total quantities purchased to include these new columns <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>, ensuring that the summary metrics at the top update automatically <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>, <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.

## Generating PDF Invoice Documents

The system also integrates with PDF output.com for generating invoice documents <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.

### Single PDF Generation

To generate a single invoice PDF:
1.  Log in to PDF output.com <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.
2.  Select the "invoice" template from the dropdown menu <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>.
3.  Fill in the invoice details such as invoice number, company name, address, and item specifics (quantity, unit price) <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.
4.  The desired currency can be set, which updates the entire invoice <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.
5.  Click "Download PDF" to generate the document <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.

### Bulk PDF Generation

PDF output.com also supports generating multiple invoices in bulk <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>. Users can add multiple rows of invoice information, either by manually filling in details or eventually by copying from the Notion database (support for this is planned) <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>. After entering all details, clicking "download all PDF" will generate each PDF document sequentially <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>. It's also possible to generate a PDF for a specific row by clicking "download PDF" on that row <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>.

## Support

For any questions or queries regarding the invoice payments tracker or utilizing PDF output for invoice generation, users can reach out via email at notionformyuse@gmail.com <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a> or use the feedback window available <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>.