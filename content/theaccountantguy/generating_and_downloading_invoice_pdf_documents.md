---
title: Generating and downloading invoice PDF documents
videoId: IK71-I_O7Vg
---

From: [[theaccountantguy]] <br/> 

This article details a system for tracking invoice payments in Notion and then [[exporting_and_downloading_generated_pdf_documents | generating and downloading invoice PDF documents]] using an external tool, PDF output.com <a class="yt-timestamp" data-t="03:04:11">[03:04:11]</a>.

## Invoice Tracking in Notion

A Notion template is available to track invoice payments <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>.

### Invoice Payment Summary (KPIs)
At the top of the template, a summary section provides key performance indicators (KPIs) for your business <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>:
*   Total expenses incurred through invoices <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.
*   Total units purchased across all invoices <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.
*   Average invoice price <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.
These KPIs can be updated or new ones added <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. The values are dynamically updated when inputs in the database are altered <a class="yt-timestamp" data-t="01:57:02">[01:57:02]</a>.

### Client Summary
Below the KPIs, a client summary shows <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>:
*   Purchases made against each client <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>.
*   Number of units purchased from each client <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.
*   Average purchase value from each client <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.

### Invoice Database Details
The core of the system is a database where all invoice details are entered <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.
Fields include:
*   Invoice number <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>
*   Invoice date <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>
*   Due date <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>
*   Company name (issuing the invoice) <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>
*   Bill to section and client address <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>
*   Description of items purchased (e.g., "item one," "item two") <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>
*   Quantity <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>
*   Unit price <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>
*   Subtotal (computed by multiplying unit price and quantity) <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>
*   Tax rate <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>
*   Total amount (computed automatically) <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>
*   Notes (e.g., payment receipt date, mode of payment) <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>

### Customization and Dynamic Updates
To add more items beyond the default two, duplicate the existing item columns (description, quantity, unit price) and update the subtotal formula to include the new columns <a class="yt-timestamp" data-t="01:36:08">[01:36:08]</a>. The system's KPIs automatically reflect these changes <a class="yt-timestamp" data-t="01:47:04">[01:47:04]</a>. Ensure to update the "total quantities purchased" formula as well when adding more quantity columns <a class="yt-timestamp" data-t="02:15:01">[02:15:01]</a>.

## [[using_pdf_output_for_invoice_generation | Generating and Exporting Invoice PDFs with PDF output.com]]

For [[generating_and_managing_pdf_invoices | generating professional invoice PDFs using Notion | generating professional invoice PDFs]], you can use PDF output.com <a class="yt-timestamp" data-t="03:04:11">[03:04:11]</a>.

### Accessing the Tool
1.  Go to PDF output.com <a class="yt-timestamp" data-t="03:11:11">[03:11:11]</a>.
2.  Log in <a class="yt-timestamp" data-t="03:15:05">[03:15:05]</a>.
3.  In the top left, find the template drop-down and search for "inv" to locate the invoice template <a class="yt-timestamp" data-t="03:23:09">[03:23:09]</a>.

### [[using_pdf_output_to_create_invoices | Generating a Single PDF Invoice]]
1.  Fill in the invoice details into the form (invoice number, company name, address, item details, quantities, prices) <a class="yt-timestamp" data-t="03:33:04">[03:33:04]</a>.
2.  Select your desired currency, which will update the entire invoice <a class="yt-timestamp" data-t="03:55:03">[03:55:03]</a>.
3.  Click "Download PDF" to generate and download the invoice <a class="yt-timestamp" data-t="04:16:08">[04:16:08]</a>.
    *   A message "PDF downloaded successfully" will appear <a class="yt-timestamp" data-t="04:20:00">[04:20:00]</a>.
    *   The downloaded PDF will display the quantities, unit prices, total computed values, and any added notes <a class="yt-timestamp" data-t="04:23:09">[04:23:09]</a>.

### [[generating_pdf_documents_in_bulk | Generating PDF Invoices in Bulk]]
The platform also supports [[generating_pdf_invoices_in_bulk_with_notion | generating PDF documents in bulk]] <a class="yt-timestamp" data-t="04:34:03">[04:34:03]</a>.
1.  Go to the "bulk PDF mode" <a class="yt-timestamp" data-t="04:34:03">[04:34:03]</a>.
2.  Fill in the details for multiple invoices by copying and pasting information into the rows <a class="yt-timestamp" data-t="04:47:04">[04:47:04]</a>.
    *   *Note: Direct Notion database integration is not yet supported but will be added in the future <a class="yt-timestamp" data-t="04:41:04">[04:41:04]</a>.*
3.  Options are available to expand column width and add new rows <a class="yt-timestamp" data-t="04:52:03">[04:52:03]</a>.
4.  Once all details are filled, click "Download all PDF" to generate all PDFs one by one <a class="yt-timestamp" data-t="04:56:06">[04:56:06]</a>.
5.  Alternatively, you can click "Download PDF" on a specific row to generate only that invoice's PDF <a class="yt-timestamp" data-t="05:13:00">[05:13:00]</a>.

## Support
For any questions or queries regarding the Notion invoice payments tracker or [[generating_pdf_documents_for_business_needs | using PDF output to create invoices | using PDF output to generate invoice documents]], you can reach out via email at notionformyuse@gmail.com <a class="yt-timestamp" data-t="05:36:09">[05:36:09]</a> or use the feedback window on the PDF output.com website <a class="yt-timestamp" data-t="05:43:05">[05:43:05]</a>.