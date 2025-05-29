---
title: Generating bulk PDF documents using Google Docs and Notion
videoId: oprL9NBoj8o
---

From: [[theaccountantguy]] <br/> 

[[generating_pdf_documents_with_notion_and_pdfoutput | PDFOutput]] is a tool designed to help users [[bulk_pdf_generation_from_notion_databases | generate PDF documents in bulk]] <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. It utilizes a [[setting_up_and_integrating_a_google_document_with_notion | Google document]] as a template and a [[generating_pdf_documents_from_notion | Notion database]] to hold the dynamic data for replacement <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.

## How to Use PDFOutput

The general process involves three main steps: adding a [[setting_up_and_integrating_a_google_document_with_notion | Google Document]] template, adding a [[generating_pdf_documents_from_notion | Notion database]], and then clicking to [[exporting_pdfs_in_bulk_using_google_docs | export PDF]] documents <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.

### 1. Log In to PDFOutput

Begin by logging in to pdfoutput.com <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>. The interface will display options to add a Google Document and a Notion database <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>.

### 2. Add a Google Document Template

The Google Document serves as the template for the PDF generation <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.
You have two options for adding a document:
*   **Create a blank document from scratch** <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.
*   **Choose an existing document** from your Google Drive <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

After selecting or creating the document, you can rename it (e.g., "Invitation Template") <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>. Within this document, identify the specific fields that need to be replaced with data from your Notion database, such as "customer name" or "salutation" <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.

For pre-existing templates, like an [[generating_pdf_invoices_from_notion_data | invoice template]], if they are restricted for access, you can make a copy in your Google Workspace or copy all content (Ctrl+A, Ctrl+C) and paste it into a blank document created within PDFOutput <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>.

### 3. Add a Notion Database

Next, connect your [[generating_pdf_documents_from_notion | Notion database]] by clicking "add notion database" <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.
*   Authenticate and select the specific Notion workspace <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>.
*   If you haven't already, create a new database in Notion (e.g., "Invitation List") <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.
*   Select the desired database from your Notion account and allow access <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.

Once connected, PDFOutput will display the properties (columns) of your Notion database, starting with the default "name" property <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>. If you add more columns to your Notion database (e.g., "customer name," "salutation"), click "refresh properties" in PDFOutput to fetch the newly added columns <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.

If your main database has connections to other Notion databases, ensure you also choose all connected databases when approving the database list <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.

### 4. Map Notion Properties to the Google Document

With both the Google Document template and the Notion database connected, you can now map the dynamic fields.
*   In PDFOutput, click on a Notion property (e.g., "salutation" or "customer name") to copy its placeholder <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>.
*   Go to your Google Document template and paste the copied placeholder where you want the value to appear (e.g., replace "Mr." with the "salutation" placeholder) <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.
*   This mapping tells PDFOutput to replace that specific part of the template with the corresponding data from your Notion database <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.

### 5. Export PDF Documents

After setting up the template and database and mapping the fields, click "export PDF" <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>. You may need to complete a Google authentication step <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>. PDFOutput will then read each row in your Notion database and generate a separate PDF document for each entry, automatically downloading them <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>.

## Key Features and Considerations

*   **Live Editing**: Changes made to the Google Document template within [[generating_pdf_documents_with_notion_and_pdfoutput | PDFOutput]] are reflected live in the Google Document itself <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.
*   **Template Library**: PDFOutput includes a library of pre-made templates <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>.
*   **Search Properties**: You can search for specific Notion properties within the interface <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.
*   **Sorting**: The tool offers a sorting window to organize values <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>.

For any questions, you can reach out to notionforuse@gmail.com <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.