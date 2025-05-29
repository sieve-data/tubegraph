---
title: Database setup for invoice details
videoId: IK71-I_O7Vg
---

From: [[theaccountantguy]] <br/> 

A Notion database can be utilized to track invoice payments and manage invoice details for a business <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. This setup allows for a comprehensive overview of financial transactions related to invoices.

## Invoice Payment Summary

The template includes a quick invoice payment summary at the top, providing key performance indicators (KPIs) for the business <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. These KPIs include:
*   Total expenses incurred through invoices <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.
*   Total units purchased across all invoices <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.
*   Average invoice price <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

These KPIs can be customized or updated as needed <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. The total expenses and units purchased automatically reflect changes made in the underlying database <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.

## Client Summary

Below the main summary, there is a client summary section <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. This section breaks down purchases by client, showing:
*   Total purchases made from each client <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>.
*   Number of units purchased from each client <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.
*   Average purchase value from each client <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.

## Invoice Details Database

The core of the system is a [[database_setup_for_purchase_orders | database]] where all invoice details are entered <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>. Key fields in this [[database_setup_for_purchase_orders | database]] include:
*   Invoice number <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>
*   Invoice date <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>
*   Due date <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>
*   Company name (from which the invoice is issued) <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>
*   Bill-to section and client address <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>

### Item Descriptions and Calculations
The [[database_setup_for_purchase_orders | database]] also includes sections for purchased items:
*   Description of items (e.g., "item one," "item two") <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>
*   Quantity <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>
*   Unit price <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>

To add more items, existing columns can be duplicated, and the formula for calculating totals must be updated to include the new columns <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>.

The subtotal for each item is automatically computed by multiplying the unit price and quantity <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>. A tax rate is applied, and the total amount is calculated accordingly <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>. Notes, such as expected payment receipt time or mode of payment, can also be added <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.

The "total quantities purchased" property is used to populate values in the summary sections <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>. If more quantity columns are added, this formula also needs to be updated <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.

## [[setting_up_and_using_pdf_output_for_invoices | Generating Professional Invoices from a Database]]

While the Notion database tracks invoice details, generating professional PDF documents for each invoice requires an external solution like [[setting_up_and_using_pdf_output_for_invoices | PDF output.com]] <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.

### Single PDF Generation
1.  Log in to [[setting_up_and_using_pdf_output_for_invoices | PDF output.com]] <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.
2.  Select the desired [[using_notion_database_for_invoice_templates | invoice template]] (e.g., search for "inv") <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>.
3.  Fill in invoice details such as invoice number, company name, address, and item values <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.
4.  The currency can be changed, which will update the entire invoice <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.
5.  Click "Download PDF" to generate the document <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.

### Bulk PDF Generation
[[setting_up_and_using_pdf_output_for_invoices | PDF output.com]] also supports bulk PDF generation <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.
1.  Switch to "bulk PDF mode" <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.
2.  Currently, details from the [[using_notion_database_as_an_invoice_source | Notion database]] need to be manually copied and pasted into rows within the bulk mode <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>. Support for direct [[using_notion_database_as_an_invoice_source | Notion database]] integration is planned <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.
3.  New rows can be added to input multiple invoices <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.
4.  Click "Download all PDF" to generate all invoices at once <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>, or "Download PDF" on a specific row to generate a single invoice <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>.

For any questions or queries regarding the invoice payments tracker or [[setting_up and using PDF Output for invoices | PDF output]], assistance can be sought by contacting notionformyuse@gmail.com <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>. A feedback window is also available on the platform <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>.