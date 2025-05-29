---
title: Generating PDF invoices from Notion data
videoId: IK71-I_O7Vg
---

From: [[theaccountantguy]] <br/> 

This article explores how to track invoice payments in Notion and subsequently [[generating_pdf_documents_from_notion | generate PDF documents]] for those invoices using an external tool called [[generating_pdf_documents_with_notion_and_pdfoutput | PDFOutput]].

## Tracking Invoice Payments in Notion

A dedicated Notion template allows for comprehensive tracking of invoice payments <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>.

### Key Performance Indicators (KPIs) <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>
The template provides a quick invoice payment summary at the top <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>, including:
*   Total expenses incurred through invoices <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.
*   Total units purchased from all combined invoices <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.
*   Average invoice price <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.
These KPIs can be customized or additional ones can be added <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>.

### Client Summary <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>
A client summary section displays:
*   Purchase amounts per client <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>.
*   Units purchased per client <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.
*   Average purchase value from each client <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.

### Database Structure <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>
The core of the system is a database where you can input detailed invoice information <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>:
*   Invoice number, invoice date, and due date <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.
*   Company name (who issues the invoice) <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.
*   Bill-to section and client address <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.
*   Description of purchased items (e.g., "item one," "item two") <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.
*   Quantity and unit price for each item <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.
*   Subtotal calculated from unit price and quantity <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.
*   Tax rate and computed total amount <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>.
*   Notes such as payment receipt time or mode of payment <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.

### Managing Items and Formulas
To add more items beyond the default two, you can duplicate existing columns for description, quantity, and unit price <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>. Remember to update the subtotal formula to include the new columns <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. Similarly, the "total quantities purchased" property needs its formula updated when new quantity columns are added <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.

### Automatic Updates
The template is designed to automatically update KPIs like total expenses and units purchased when underlying data in the database changes <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. For example, altering an input value in the database will reflect immediately in the total expenses summary <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.

## [[generating_pdf_documents_from_notion | Generating PDF Invoices]] with [[generating_pdf_documents_with_notion_and_pdfoutput | PDFOutput.com]]

For [[generating_pdf_documents_from_notion | generating PDF documents]] for each invoice, a solution like [[generating_pdf_documents_with_notion_and_pdfoutput | PDFOutput.com]] can be used <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.

### Generating a Single PDF Invoice
1.  **Access PDFOutput.com**: Log in to PDFOutput.com <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.
2.  **Select Template**: Use the drop-down menu on the top left to search for and select the "invoice" [[using_notion_templates_for_invoice_pdfs | template]] <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>.
3.  **Fill Details**: Manually fill in the invoice details, including invoice number, company name, address, and item specifics (quantity, unit price) <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.
4.  **Set Currency**: You can set your desired currency (e.g., Euro), and the entire invoice will update accordingly <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.
5.  **[[exporting_notion_data_to_pdf | Download PDF]]**: Click "Download PDF" to [[generating_professional_invoices_from_notion_database | generate the invoice document]] <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>. A message "PDF downloaded successfully" will confirm the action <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>. The [[creating_professional_invoices_using_notion | invoice document]] will display quantities, unit prices, computed totals, and any added notes <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.

### Generating Bulk PDF Invoices
The platform also supports a "bulk PDF mode" <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.
*   In this mode, you can [[generating_professional_invoices_from_notion_database | add details from your Notion database]] by copying and pasting information into rows <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>.
*   Once all details are filled across multiple rows, click "Download all PDF" to [[generating_pdf_documents_from_notion | generate all PDF documents]] one by one <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.
*   Alternatively, you can choose to [[generating_pdf_documents_from_notion | generate a particular PDF]] for a specific row by clicking "Download PDF" on that row <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>.

> [!NOTE]
> Currently, direct support for [[using_a_notion_database_and_templates_to_create_pdf_invoices | Notion database]] integration in the bulk PDF mode is not yet available, requiring manual copy-pasting of data <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>.

## Support and Feedback
For any questions regarding the Notion invoice payments tracker or using [[generating_pdf_documents_with_notion_and_pdfoutput | PDFOutput]] to generate [[creating_professional_invoices_using_notion | invoice documents]], you can reach out via email at notionformyuse@gmail.com <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>. A feedback window is also available directly on the platform for sending queries <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>.