---
title: Using PDF output for invoice document generation
videoId: IK71-I_O7Vg
---

From: [[theaccountantguy]] <br/> 

This article explains how to generate PDF documents for invoices using a dedicated PDF output tool, building upon a Notion-based invoice payment tracker.

## Invoice Payment Tracker in Notion
A Notion template can be used to track invoice payments <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. This template includes:
*   **Invoice Payment Summary** <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>: Displays key performance indicators (KPIs) such as total expenses incurred through invoices, total units purchased across all invoices, and the average invoice price <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. These KPIs can be customized <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>.
*   **Client Summary** <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>: Shows purchase details per client, including the amount purchased, units bought, and average purchase value <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>.
*   **Invoice Database** <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>: A database to record detailed invoice information <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>, including:
    *   Invoice number <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>
    *   Invoice date and due date <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>
    *   Company name <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>
    *   Bill-to section and client address <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>
    *   Descriptions of purchased items, quantities, and unit prices <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>
    *   Subtotal (calculated from quantity and unit price) <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>
    *   Tax rate and total amount <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>
    *   Notes, such as expected payment receipt time or mode of payment <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>

### Customizing the Notion Tracker
To add more items beyond the default two, users can duplicate existing item columns and update the associated formulas to include the new columns <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>. Similarly, formulas for "total quantities purchased" should be updated when adding more quantities to ensure accurate reflection in the summary <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.

## [[integration_with_pdf_output_tools | Generating PDFs for Business Invoices]]

While the Notion tracker helps manage invoices, a separate solution is available for [[generating_pdfs_for_business_invoices | generating PDF documents for each invoice]] <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>. This involves using a tool like PDF Output.com <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.

### Process for [[using_pdf_output_to_generate_invoices | Generating a Single PDF Invoice]]
1.  **Access PDF Output**: Log in to PDF Output.com <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.
2.  **Select Template**: Use the drop-down menu on the top left to search for and select an "invoice template" (e.g., by typing "inv") <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>.
3.  **Fill in Details**: Populate the template with invoice details such as invoice number, company name, address, and item specifics (quantity, unit price) <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.
4.  **Set Currency**: The desired currency can be set, and the entire invoice will update accordingly <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.
5.  **Generate PDF**: Click the "Download PDF" button to [[using_pdf_output_for_document_export_and_preview | generate and download]] the invoice as a PDF <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.

### [[pdfoutput_for_bulk_document_generation | Bulk PDF Document Generation]]
PDF Output also supports [[bulk_pdf_document_generation_process | generating multiple PDF documents]] simultaneously <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.
*   **Bulk PDF Mode**: Switch to the "Bulk PDF mode" within PDF Output <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.
*   **Input Data**: Fill in details for multiple invoices by copying and pasting information into rows <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>. While Notion database support is planned, it is not yet available <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.
*   **Download All**: Click "Download All PDF" to [[pdfoutput_for_bulk_document_generation | generate all PDFs one by one]] <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>.
*   **Individual Row Download**: Users can also download a PDF for a specific row by clicking "Download PDF" on that particular row <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>.

### [[using_templates_in_pdf_output_for_generating_receipts | Setting up PDF Output for Invoice Generation]]
The system uses templates, such as the invoice template, to structure the PDF output <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>. When [[setting_up_pdf_output_for_invoice_generation | generating PDF documents for sales receipts]] or invoices, these templates ensure consistent formatting.

## Support
For any questions or queries regarding the invoice payments tracker or [[using_pdf_output_to_generate_invoices | using PDF Output to generate invoice documents]], support is available via email at notionformyuse@gmail.com <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>. A feedback window is also available for direct communication <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>.