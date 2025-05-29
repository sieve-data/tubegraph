---
title: Using databases in Notion for invoice tracking
videoId: IK71-I_O7Vg
---

From: [[theaccountantguy]] <br/> 

Notion can be utilized to track invoice payments, providing a clear overview of financial transactions related to invoices <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. A typical Notion template for this purpose includes key performance indicators (KPIs) and detailed invoice information <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>.

## Invoice Payment Summary

At the top of the tracking template, a summary section provides quick insights into invoice-related financial data <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>:
*   **Total Expenses:** The cumulative cost incurred through all invoices <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. This figure automatically updates based on the database entries <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.
*   **Units Purchased:** The combined total of all units acquired across all invoices <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.
*   **Average Invoice Price:** The average cost per invoice <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

These KPIs can be customized or additional ones can be added as needed <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>.

## Client Summary

Below the main KPIs, a client summary provides a breakdown of purchases by client <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. This summary includes:
*   Total purchases made from each client <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>.
*   The number of units purchased from each client <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.
*   The average purchase value from each client <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.

For example, if "11 Enterprises" is listed, the summary would show its total purchase value and total quantity purchased <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.

## Invoice Tracking Database Structure

The core of the system is a [[creating_a_database_in_notion | database]] where all invoice details are recorded <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>. Key fields within this [[creating_and_using_databases_in_notion | database]] include:
*   Invoice number <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>
*   Invoice date <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>
*   Due date <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>
*   Company name (issuing the invoice) <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>
*   Bill to section and client address <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>
*   Description of items purchased (e.g., Item one, Item two) <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>
*   Quantity <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>
*   Unit price <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>
*   Subtotal (calculated by multiplying quantity and unit price) <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>
*   Tax rate <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>
*   Total amount (computed by adding tax to subtotal) <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>
*   Notes (e.g., payment receipt date, mode of payment) <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>

To add more items beyond the default two, users can duplicate existing item columns and update the formula for the subtotal calculation to include the new columns <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>. Similarly, the "total quantities purchased" formula needs to be updated if more quantity columns are added <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.

## Generating PDF Invoices

While Notion is excellent for tracking, generating PDF invoices requires an external tool like PDFoutput.com <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.

### Single PDF Generation
1.  **Access PDFoutput.com:** Log in to the website <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.
2.  **Select Template:** Use the drop-down menu on the top left and search for "inv" to find the invoice template <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>.
3.  **Fill Details:** Input all relevant invoice information such as invoice number, company name, address, and item specifics (quantity, unit price) <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>. The desired currency can also be selected, which updates the entire invoice <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>.
4.  **Download PDF:** Click "Download PDF" to generate the invoice document <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>. The generated PDF will show quantities, unit prices, computed total values, and notes <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.

### Bulk PDF Generation
PDFoutput.com also offers a "bulk PDF mode" to generate multiple invoices simultaneously <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.
1.  **Input Data:** Users can manually fill in rows of invoice information or copy-paste from another source <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>. Support for direct integration with the [[creating_and_using_databases_in_notion | Notion database]] is planned <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>.
2.  **Generate All:** Clicking "Download all PDF" will generate each PDF document one by one <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>.
3.  **Generate Specific Row:** A "Download PDF" option on each row allows generation of a PDF for only that particular invoice <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>.

## Support

For any questions or assistance regarding the invoice payments tracker in Notion or using PDFoutput.com, users can reach out via email at notionformyuse@gmail.com <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>. A feedback window is also available on PDFoutput.com for direct queries <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>.