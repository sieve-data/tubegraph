---
title: Workflow for exporting and downloading PDF documents
videoId: oprL9NBoj8o
---

From: [[theaccountantguy]] <br/> 

[[managing_and_exporting_pdfs_with_pdfoutput | PDFOutput]] is a tool designed to [[bulk_exporting_pdf_documents | generate PDF documents in bulk]] by combining a Google Document template with data from a Notion database <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. This process streamlines the creation of multiple personalized documents, such as invitations, invoices, or sales receipts <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a> <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>.

## Getting Started

To begin [[using_pdf_output_for_document_export_and_preview | using PDFOutput]], first log in to PDFoutput.com <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>. The interface will then allow you to add a Google Document template and a Notion database <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.

## Steps for Document Generation

The overall workflow involves three primary steps: adding a Google Document, integrating a Notion database, and then [[exporting_pdfs_in_bulk_using_google_docs | exporting the PDFs]] <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.

### 1. Adding a Google Document Template

The Google Document serves as the template for your PDFs <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.
You have two options for adding a document:
*   **Create a blank document from scratch** <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.
*   **Choose an existing document** from your Google Drive <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

#### Process for Creating a Blank Document
1.  Click the "create document" button <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.
2.  Select the Google account you wish to connect <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.
3.  Once created, rename the document (e.g., "Invitation Template") <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>.
4.  Paste your desired content into the document <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.
5.  Identify specific fields within the template that need to be replaced by data from your Notion database (e.g., `customer name` and `salutation`) <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a> <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.

> [!NOTE]
> The template is editable live, meaning changes made will be reflected in the Google Document <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.

### 2. Integrating a Notion Database

The Notion database holds the specific data elements that will populate your Google Document template <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.

#### Process for Adding a Notion Database
1.  Click "add notion database" <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.
2.  Connect your Notion credentials <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.
3.  Select the specific Notion pages or database you want to connect <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>.
    *   If you haven't created one, you can do so in Notion (e.g., create a new page as a table and name it "Invitation List") <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.
4.  Once the database is connected, its properties (columns) will be displayed <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.
    *   If you add new columns to your Notion database, click "refresh properties" to fetch the new properties <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.

#### Mapping Database Fields to the Template
1.  Click on a property from your Notion database (e.g., "salutation") to copy its value <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>.
2.  Go to your Google Document template and paste the copied property value where you want it to be replaced (e.g., paste `salutation` where you want the salutation to appear) <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.
3.  Repeat this process for all fields you want to replace (e.g., "customer name") <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.

> [!INFO]
> For databases with connections to other databases, ensure you choose *all* connected databases while approving the list to ensure proper data extraction <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.

### 3. Exporting and Downloading PDFs

After connecting both the template and the database, you are ready for the [[bulk_pdf_document_generation_process | bulk PDF document generation process]] <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>.

1.  Click "export PDF" <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>.
2.  Complete the Google authentication process <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>.
3.  [[pdfoutput_for_bulk_document_generation | PDFOutput]] will then read each row (item) in your Notion database and generate a corresponding PDF document <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>.
4.  The generated PDFs will automatically start downloading to your device <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>.

The downloaded documents will reflect the data from each row of your Notion database, personalized according to your template <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>. For example, if you have three entries in your Notion database, three distinct PDFs will be generated <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a> <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>.

## Additional Features

*   **Pre-built Templates:** [[integration_with_pdf_output_tools | PDFOutput]] offers pre-built templates for various uses, such as [[using_pdf_output_to_generate_invoices | invoice templates]] <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a> <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>. You can make a copy of these templates to your Google Workspace or copy their content into a blank document <a class="yt-timestamp" data-t="00:07:46">[00:07:46]</a>.
*   **Search and Sort:** The tool includes search functionality for properties <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a> and a sorting window to organize values <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>.

This workflow simplifies the process of [[generating_pdf_documents_for_sales_receipts | generating PDF documents]] in bulk, saving time and effort <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>.