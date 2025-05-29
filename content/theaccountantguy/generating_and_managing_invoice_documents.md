---
title: Generating and managing invoice documents
videoId: IK71-I_O7Vg
---

From: [[theaccountantguy]] <br/> 

This article describes how to track invoice payments and generate invoice documents using a Notion template and an online PDF generation tool called PDF Output.

## Tracking Invoice Payments in Notion

A dedicated Notion template allows users to track invoice payments <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. This template provides a quick invoice payment summary at the top <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.

The summary includes key performance indicators (KPIs) such as:
*   Total expenses incurred through invoices <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.
*   Total units purchased across all invoices <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.
*   Average invoice price <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

Additional KPIs can be added, or existing ones updated <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.

A client summary section displays purchase details per client, including total purchases, units purchased, and average purchase value <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>.

The core of the system is a database where users can input detailed invoice information <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.
Database fields include:
*   Invoice number <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>
*   Invoice date <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>
*   Due date <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>
*   Company name <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>
*   Bill-to section and client address <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>
*   Description of purchased items (e.g., "item one," "item two") <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>
*   Quantity <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>
*   Unit price <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>

The subtotal is automatically calculated as the multiplication of unit price and quantity <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>. The tax rate is added, and the total amount is computed <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>. Notes, such as payment receipt timing or mode, can also be added <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.

To add more items beyond the initial two, users can duplicate existing columns and update the formula to include the new column <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>. This ensures that all calculations, such as total expenses and units purchased, update automatically <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. The "total quantities purchased" property also needs to be updated if more quantities are added <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>. This [[generating_professional_invoices_from_notion_database | Notion database]] system helps to keep track of all invoices for a business <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>.

## [[using_pdf_output_for_invoice_generation | Generating Professional Invoices]]

To [[exporting_and_managing_generated_pdf_invoices | generate PDF documents for invoices]], users can utilize PDF output.com <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.

### Single PDF Generation
1.  Log in to PDF output.com <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>.
2.  Select the desired [[creating_and_customizing_invoice_templates_in_pdf | invoice template]] from the drop-down menu, typically by searching for "inv" <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>.
3.  Fill in the invoice details, including invoice number, company name, address, and all values <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.
    *   The desired currency can be set, and the entire invoice will update accordingly <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.
    *   All values, including item totals, are reflected <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
4.  Click "Download PDF" to generate the invoice <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>. The system will confirm "PDF downloaded successfully" <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>.
5.  The generated PDF will display the quantity, unit price, computed total value, and any added notes <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.

### [[creating_bulk_invoice_pdfs | Bulk Invoice PDF Generation]]
PDF Output also supports [[creating_bulk_invoice_pdfs | bulk PDF generation]] <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.
1.  Navigate to the "bulk PDF mode" <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.
2.  Input invoice details by copying and pasting rows of information <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>. While future support for direct Notion database integration is planned, it's not currently available <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.
3.  Users can expand column width for better viewing <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>.
4.  Click "Download all PDF" to generate all invoices one by one <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>.
5.  Individual PDFs for specific rows can also be generated by clicking "Download PDF" on that row <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>.

For any questions or support regarding the invoice payments tracker or [[using_pdf_output_for_invoice_generation | PDF Output]] for invoice generation, users can reach out via email to notionformyuse@gmail.com <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a> or use the feedback window on the platform <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>.