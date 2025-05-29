---
title: Using PDF output for invoice generation
videoId: WfYK1BJd490
---

From: [[theaccountantguy]] <br/> 

[[introduction_to_pdfoutput_tool | PDF Output]] is a tool designed to [[generating_pdf_documents_from_invoices | generate professional invoices]] directly from a Notion database <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. It facilitates the process of [[creating_and_exporting_pdf_documents_for_business | creating and exporting PDF documents for business]], specifically for invoices <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>.

## How it Works

[[introduction_to_pdfoutput_tool | PDF Output]] automatically maps data from a Notion database to a Notion template to [[bulk_pdf_document_generation | generate PDF documents]] <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.

### Template Structure
An invoice template in Notion is used, containing "from" and "to" sections <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. Placeholder text, such as client name, company, address, city, state, and zip, is inserted within curly braces (`{}`) <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>. Any element in the template enclosed in curly braces will be replaced with data from the database <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

### Database Structure
The Notion database contains columns (e.g., client name, amount, bank name, client address, client company) that correspond to the placeholder elements in the template <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>. For each row of information in the database, a separate PDF will be generated <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.

> [!TIP] Naming Convention
> Ensure that the element names in the template placeholders (e.g., `{client name}`) exactly match the column names in the Notion database <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>. If there's a mismatch, the mapping will appear in gray, and it can be manually corrected by searching for the correct value <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.

## Steps for Invoice Generation

1.  **Log In to PDFOutput**: Access the [[introduction_to_pdfoutput_tool | PDF Output]] interface <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.
2.  **Enable API Keys**: Go to the "Help" section (by clicking "H") to complete steps required for enabling API keys, which are necessary for the setup <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.
3.  **Define Connection**:
    *   Type a name for the connection (e.g., "invoice generation") <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.
    *   Select the Notion database name (e.g., "professional invoice database") from the dropdown <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>.
    *   Select the Notion template name (e.g., "professional invoice template") <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>.
4.  **Map Elements**: Click "Next" <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>. [[introduction_to_pdfoutput_tool | PDF Output]] will automatically load and map all database elements to their corresponding template placeholders <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.
5.  **Export PDFs**: Click "Export" <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.
    *   A "PDF status" column in your Notion database will automatically tick as each PDF file is generated <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>.
6.  **Preview and Download**:
    *   Click "Preview sample" to view a generated PDF <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.
    *   Click "Download all" to download all generated PDF files <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>.

The output PDFs will be clean and accurately populated with data from the Notion database into the specified template <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>. This method can be used for [[using_pdfoutputcom_to_create_bulk_pdf_documents | creating bulk PDF documents]] for various business needs <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>.