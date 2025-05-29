---
title: Using Google Docs as a template for PDF generation
videoId: 6PR3AESuBoA
---

From: [[theaccountantguy]] <br/> 

[[using_pdfoutput_com_for_document_generation | PDFoutput.com]] is a tool designed to [[generating_pdf_documents_in_bulk | generate PDF documents in bulk]] by utilizing [[using_templates_and_databases_for_pdf_generation | Google document]] as a template, with the help of a [[using_templates_and_databases_for_pdf_generation | Notion database]] <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>.

## Getting Started with PDFoutput.com

To begin, navigate to [[using_pdfoutput_com_for_document_generation | PDFoutput.com]] <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>.
1.  Click on "create PDF" <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>.
2.  Sign in through a Google account <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>.
3.  Enable the checkbox to grant [[using_pdfoutput_com_for_document_generation | PDF output]] access to specific files <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.
4.  Click "continue" to be redirected to the homepage <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.

While [[using_pdfoutput_com_for_document_generation | PDFoutput.com]] offers certain pre-populated [[creating_and_using_templates_for_pdf_generation | PDF templates]], this process focuses on using a raw Google Doc <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>.

## Preparing the Google Doc Template

1.  Click the link next to the Google document option on the [[using_pdfoutput_com_for_document_generation | PDFoutput.com]] interface <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>. This will display documents from your [[organizing_generated_pdfs_in_google_drive | Google Drive]] <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.
2.  Select the desired Google Doc to use as a template (e.g., "PDF output invitation letter") <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.
3.  In your Google Doc template, identify placeholders for dynamic data (e.g., `first name`, `last name`) <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>. These placeholders will be replaced with data from your [[using_templates_and_databases_for_pdf_generation | Notion database]] <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.

## Connecting to a Notion Database

[[using_pdfoutput_com_for_document_generation | PDFoutput.com]] integrates with [[using_templates_and_databases_for_pdf_generation | Notion]] to pull data for document generation <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.

### Creating the Notion Database
1.  In [[using_templates_and_databases_for_pdf_generation | Notion]], create a new page (e.g., "PDF output database") <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>.
2.  Type `/database` and select "inline" to create a new database <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>.
3.  Name the database (e.g., "database PDF output") <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.
4.  Rename columns to match your Google Doc placeholders (e.g., "first name," "last name") <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.
5.  Populate the database with data (e.g., "Priya Sharma," "Miller Stark," "John Quotes") <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.

### Obtaining Database URL and API Key
1.  From your [[using_templates_and_databases_for_pdf_generation | Notion database]] view, click "share" and then "copy link" to get the database URL <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>. Paste this into the "database URL" field in [[using_pdfoutput_com_for_document_generation | PDFoutput.com]] <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.
2.  Click "add API key" in [[using_pdfoutput_com_for_document_generation | PDFoutput.com]] to create a new Notion API key <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>. Name the key (e.g., "notion PDF output connection") and select your Notion account <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.
3.  Copy the generated API key value <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a> and paste it into the API key field in [[using_pdfoutput_com_for_document_generation | PDFoutput.com]] <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>.
4.  Ensure your [[using_templates_and_databases_for_pdf_generation | Notion database]] is connected to the API key by clicking the three dots on the database, selecting "connections," and choosing your "PDF output connection" <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.

## Configuring PDF Generation

1.  In [[using_pdfoutput_com_for_document_generation | PDFoutput.com]], click "load properties." This will fetch and display all columns from your [[using_templates_and_databases_for_pdf_generation | Notion database]] <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.
2.  **Output File Name**: Select a property from the dropdown (e.g., "first name") to use for naming the generated PDF files <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
3.  **Output Folder**:
    *   Select "Google Drive" <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.
    *   Create a new folder in your [[organizing_generated_pdfs_in_google_drive | Google Drive]] (e.g., "invitation documents") <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>.
    *   Click "add folder" in [[using_pdfoutput_com_for_document_generation | PDFoutput.com]] and select the newly created [[organizing_generated_pdfs_in_google_drive | Google Drive]] folder <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.
    *   Alternatively, you can choose the "downloads folder" to save files to your desktop <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>.
4.  **Map Placeholders**: In the editor within [[using_pdfoutput_com_for_document_generation | PDFoutput.com]], replace the generic placeholders (like `first name`, `last name`) in your Google Doc template with the actual properties fetched from the [[using_templates_and_databases_for_pdf_generation | Notion database]] <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>. Simply copy the property name from the fetched list and paste it into the template area <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.

## Generating PDFs

1.  Once all settings are configured, click "export PDF" <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.
2.  [[using_pdfoutput_com_for_document_generation | PDFoutput.com]] will begin [[generating_pdf_documents_in_bulk | generating the documents]] and saving them to your designated [[organizing_generated_pdfs_in_google_drive | Google Drive]] folder <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>. The "PDF generated count" will increase as documents are created <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>.
3.  After completion, click "view in [[organizing_generated_pdfs_in_google_drive | Google Drive]]" to open the folder and verify the generated PDFs <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>. Each document will have the placeholders replaced with the corresponding data from the [[using_templates_and_databases_for_pdf_generation | Notion database]] <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>.

## Additional Features of PDFoutput.com

*   **[[creating_and_using_templates_for_pdf_generation | Templates]]**: [[using_pdfoutput_com_for_document_generation | PDFoutput.com]] provides predefined [[using_pdf_output_templates_in_notion | PDF templates]] that users can utilize for their purposes <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>.
*   **History**: The "history" option displays all documents that have been [[generating_pdf_documents_in_bulk | generated]] in the past <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.
*   **Upgrade**: Users can upgrade to a specific plan <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>.
*   **Contact**: A contact section is available for queries or questions <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>.