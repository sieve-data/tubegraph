---
title: Generating PDF invoices from Notion
videoId: IK71-I_O7Vg
---

From: [[theaccountantguy]] <br/> 

This article details how to track invoice payments within Notion and subsequently generate PDF invoices, either individually or in bulk, using an external tool called PDFOutput.com <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.

## Notion Invoice Payment Tracker

A dedicated Notion template is available for tracking invoice payments <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>.

### Summary Sections

The template includes key performance indicators (KPIs) at the top for a quick overview:
*   **Invoice Payment Summary** <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>
    *   Total expenses incurred through invoices <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.
    *   Total units purchased across all invoices <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.
    *   Average invoice price <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.
    *   These KPIs are customizable and can be updated or new ones added <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>.
*   **Client Summary** <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>
    *   Shows total purchases, units purchased, and average purchase value for each client <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>. This summary is automatically computed based on the database entries <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.

### Invoice Database Structure

The core of the tracker is a database where you can input detailed invoice information <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.
Key fields include:
*   Invoice number <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>
*   Invoice date <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>
*   Due date <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>
*   Company name (issuer) <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>
*   Bill to section and client address <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>
*   Description of items being purchased (e.g., Item one, Item two) <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>
*   Quantity <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>
*   Unit price <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>

Calculated fields:
*   **Subtotal:** Automatically calculated as quantity multiplied by unit price <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.
*   **Tax rate:** Added to the subtotal <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>.
*   **Total amount:** Computed from the subtotal and tax <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.

Additional fields:
*   Notes, such as expected payment receipt time or mode of payment <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.

### Customization and Updates

*   To add more items beyond the default two, duplicate existing item description, quantity, and unit price columns <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.
*   When adding new item columns, update the subtotal formula to include these new columns <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.
*   Similarly, the "Total Quantities Purchased" property, which feeds into the top-level KPIs, needs to be updated with new quantity columns <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.
*   Changes made in the database (e.g., altering input values) automatically update the summary KPIs like "Total Expenses" and "Units Purchased" <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.

## [[pdf_document_creation_with_notion_and_pdf_output | Generating PDF Documents with Notion and PDF Output]]

To [[creating_professional_invoice_templates_in_notion | generate a PDF document]] for each invoice tracked in Notion, you can use PDFOutput.com <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.

### Single PDF Generation

1.  **Access PDFOutput.com**: Log in to the website <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.
2.  **Select Template**: Use the drop-down menu on the top left and search for "inv" to find the invoice template <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>.
3.  **Fill in Details**: Manually enter the invoice details into the template. These can be copied from your Notion database <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.
4.  **Currency Selection**: You can set the desired currency (e.g., Euro), and the entire invoice will update accordingly <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.
5.  **Download PDF**: Click "Download PDF" to generate and save the invoice <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>. The generated PDF will display quantities, unit prices, computed total values, and any added notes <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.

### [[generating_pdf_documents_in_bulk_with_notion | Generating PDF Documents in Bulk]]

PDFOutput.com also supports [[generating_pdf_documents_from_notion_database_rows | generating PDF documents from Notion database rows]] in bulk <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.

1.  **Bulk PDF Mode**: Navigate to the "bulk PDF mode" section <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.
2.  **Input Data**: Currently, you need to manually copy and paste rows of information from your Notion database into the interface <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>. (Note: Direct support for Notion database integration is planned for the future <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.)
    *   You can add new rows as needed <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.
    *   Column widths can be expanded for better viewing <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>.
3.  **Generate All PDFs**: After filling in all details, click "Download all PDF" to generate all PDFs one by one <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>.
4.  **Generate Single PDF from Bulk**: You can also generate a PDF for a specific row in the bulk mode by clicking "Download PDF" on that particular row <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>.

## Support and Feedback

For any questions or queries regarding the use of the invoice payments tracker or [[using_notion_for_invoice_generation | utilizing PDF Output to generate invoice documents]], you can reach out via email at notionformyuse@gmail.com <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>. A feedback window is also available on the platform for direct communication <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>.