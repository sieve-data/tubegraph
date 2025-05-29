---
title: Using PDFoutputcom for bulk PDF generation
videoId: 6PR3AESuBoA
---

From: [[theaccountantguy]] <br/> 

[[features_and_functionalities_of_pdfoutput_tool | PDFoutput.com]] is a tool designed to [[generating_single_and_bulk_pdf_documents | generate PDF documents in bulk]] by [[using_templates_to_create_pdf_documents_in_bulk | utilizing Google Docs as a template]] in conjunction with a Notion database <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. This enables [[automating_document_exports_using_pdf_output | automated document exports]] for various use cases, such as invitation letters <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.

## Getting Started with PDFoutput.com

To begin [[steps_to_set_up_and_export_pdfs_using_pdf_output | using PDFOutput for bulk document generation]]:

1.  Navigate to PDFoutput.com <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>.
2.  Click on "Create PDF" <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>.
3.  Sign in with your Google account and select your account <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>.
4.  Enable the checkbox to grant [[features_and_functionalities_of_pdfoutput_tool | PDFoutput.com]] access to specific files <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.
5.  Click "Continue" to be redirected to the homepage <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.

While predefined templates are available, you can also use a raw Google Document <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.

## Setting Up Your Google Document Template

The core of [[using_pdf_output_tool_for_efficient_document_creation | efficient document creation]] with [[features_and_functionalities_of_pdfoutput_tool | PDFoutput.com]] involves a Google Document template.

1.  Click the link next to "Google Document" to select a file from your Google Drive <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.
2.  Choose the desired document, for example, an "invitation letter" <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.
3.  Within your Google Doc, identify placeholders (e.g., `first name`, `last name`) that will be replaced by data from your Notion database <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.
4.  Once selected, the invitation letter will load in the interface <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.

## Integrating with Notion Database

[[generating_pdf_invoices_using_pdfoutput | Generating PDF invoices using PDFoutput]] or any bulk document requires a data source. [[features_and_functionalities_of_pdfoutput_tool | PDFoutput.com]] integrates with Notion.

### Creating and Populating the Notion Database

1.  In [[features_and_functionalities_of_pdfoutput_tool | PDFoutput.com]], select "Notion" from the dropdown <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.
2.  Click the provided link to open your Notion workspace <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.
3.  Create a new page (e.g., "PDF output database") <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>.
4.  Type `/database` and select "inline" to create an inline database <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>.
5.  Rename columns to match your Google Doc placeholders (e.g., "first name", "last name") <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.
6.  Add data entries (e.g., Priya Sharma, Miller Stark, John Quotes) to the database <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.

### Connecting Notion to PDFoutput.com

1.  In Notion, click "Share" on your database page and "Copy link" to get the database URL <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.
2.  Paste this URL into the "Database URL" field in [[features_and_functionalities_of_pdfoutput_tool | PDFoutput.com]] <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.
3.  For the API key, click "add API key" <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
4.  Create a new integration (e.g., "Notion PDF output connection"), select your account, and save <a class="yt-timestamp" data-t="00:02:54">[00:03:07]</a>.
5.  Copy the generated internal integration token <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.
6.  Paste the API key into the "API key" field in [[features_and_functionalities_of_pdfoutput_tool | PDFoutput.com]] <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>.
7.  Crucially, ensure your Notion database is connected to this API key:
    *   In Notion, click the three dots on your database page <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
    *   Go to "Connections" and select "PDF output connection" <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>.
    *   Click "Confirm" <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.
8.  Back in [[features_and_functionalities_of_pdfoutput_tool | PDFoutput.com]], click "Load properties" to fetch column headers from your Notion database <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.

## Configuring Output and Mapping Properties

Once the properties are loaded, you can configure the output:

1.  **Output File Name:** Select a property from the dropdown (e.g., "first name") to name the generated PDF files <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
2.  **Output Location:** Choose "Google Drive" or "downloads folder" <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.
    *   For Google Drive, create a new folder (e.g., "invitation documents") in your Drive <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>.
    *   In [[features_and_functionalities_of_pdfoutput_tool | PDFoutput.com]], click "add folder" and select the newly created Google Drive folder <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.
3.  **Mapping Placeholders:** In the Google Document preview, highlight the placeholders (e.g., `first name`, `last name`) and replace them by copying the corresponding properties from the loaded properties list and pasting them into the document <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>. These mapped properties will be dynamically replaced for each document generated <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.

## [[generating_single_and_bulk_pdf_documents | Generating Single and Bulk PDF Documents]]

With all settings configured, you can now [[using_pdfoutput_for_bulk_document_generation | use PDFOutput for bulk document generation]]:

1.  Click "Export PDF" <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.
2.  [[features_and_functionalities_of_pdfoutput_tool | PDFoutput.com]] will begin [[automating_document_exports_using_pdf_output | automating document exports]], and the "PDF generated" count will increase as documents are created <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>.
3.  Once completed, click "View in Google Drive" to inspect the generated documents <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>. Each document will have the placeholders replaced with data from the Notion database (e.g., "Jonty Roads", "Mirror Stark", "Priya Sharma") <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>.

## Additional [[features_and_functionalities_of_pdfoutput_tool | Features and Functionalities of PDFOutput Tool]]

*   **Templates:** [[features_and_functionalities_of_pdfoutput_tool | PDFoutput.com]] offers predefined templates for various purposes <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>.
*   **History:** The "History" section allows you to view all previously generated documents <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.
*   **Upgrade Options:** Users can upgrade to a specific plan for additional features <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>.

For any questions or queries, a contact section is available at the bottom of the page <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>.