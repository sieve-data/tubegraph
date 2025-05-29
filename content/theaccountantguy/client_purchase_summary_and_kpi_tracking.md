---
title: Client purchase summary and KPI tracking
videoId: IK71-I_O7Vg
---

From: [[theaccountantguy]] <br/> 

This article details a Notion template designed to [[payments_tracker | track invoice payments]] and provide key insights into business performance, specifically focusing on client purchases and overall expenses <a class="yt-timestamp" data-t="00:00:01">[00:00:01]</a>.

## Invoice Payment Summary

The template provides an immediate overview of invoice data through several key performance indicators (KPIs) at the top of the dashboard <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. These KPIs offer a quick snapshot of financial health related to purchases:
*   **Total Expenses** The sum of all expenses incurred through invoices <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.
*   **Units Purchased** The total number of units bought across all invoices <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.
*   **Average Invoice Price** The average price of invoices over time <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

These KPIs are customizable, allowing users to modify existing ones or add new ones to suit specific business needs <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. Values update automatically when underlying data in the database changes <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>.

## Client Summary

Below the overall summary, a client summary provides detailed insights into purchases made against each client <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. This section shows:
*   Total purchases made from each client <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.
*   The number of units purchased from each client <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.
*   The average purchase value from each client <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.

For instance, if "11 Enterprises" is listed, the summary will show their total purchase amount and the quantity of items purchased from them <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.

## Database Structure

The core of the template is a database where all invoice details are entered <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>. Key fields include:
*   Invoice number <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>
*   Invoice date <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>
*   Due date <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>
*   Company name (from which items are ordered/invoice issued) <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>
*   "Bill to" section and client address <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>
*   Description of items purchased (e.g., "item one," "item two") <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>
*   Quantity of each item <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>
*   Unit price of each item <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>

Additional notes can be added, such as expected payment receipt time or mode of payment <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.

### Calculations and Customization

The database automatically computes several values:
*   **Subtotal** Calculated by multiplying the unit price by the quantity for each item <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.
*   **Total Amount** Computed by adding a specified tax rate to the subtotal <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>.

To add more items beyond the default two, users can duplicate existing item columns and update the corresponding formulas for subtotal and total quantities purchased to include the new columns <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>. This ensures all dashboard figures, like "Total Expenses" and "Units Purchased," remain accurate <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.

## Generating PDF Invoices

The template integrates with an external service, `PDFoutput.com`, for generating PDF documents of invoices <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.

### Steps to Generate a Single PDF Invoice:
1.  Navigate to `PDFoutput.com` and log in <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.
2.  From the template dropdown on the top left, search for "inv" to find and select the invoice template <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.
3.  Fill in the invoice details such as invoice number, company name, address, item descriptions, quantities, and unit prices <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.
4.  Select the desired currency, which will update the entire invoice <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.
5.  Click "Download PDF" to generate and download the invoice document <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>. The generated PDF will show quantities, unit prices, total computed values, and any added notes <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.

### Bulk PDF Generation

For multiple invoices, `PDFoutput.com` also offers a bulk PDF mode <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>. While direct Notion database support is planned, users can currently manually fill in or copy-paste rows of invoice information <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.
*   Click "Add new row" to add more invoice entries <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.
*   After filling all details, click "Download all PDF" to generate all documents one by one <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>.
*   Alternatively, to generate a PDF for a specific row, click "Download PDF" next to that particular row <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>.

## Support

For any questions or issues regarding the [[payments_tracker | invoice payments tracker]] or using PDFoutput.com, support can be reached via email at `notionformyuse@gmail.com` <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a> or through the feedback window on the PDFoutput.com website <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>.