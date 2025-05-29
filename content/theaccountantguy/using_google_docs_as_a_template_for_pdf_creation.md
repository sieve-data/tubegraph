---
title: Using Google Docs as a template for PDF creation
videoId: 6PR3AESuBoA
---

From: [[theaccountantguy]] <br/> 

[[PDFoutput.com]] is a tool designed to [[automating_pdf_generation_with_userdefined_templates | generate PDF documents in bulk]] by [[using_google_documents_and_notion_for_pdf_generation | utilizing Google Documents as a template]] with the assistance of a [[using_notion_templates_for_pdf_generation | Notion database]] <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>.

## Getting Started with PDFoutput.com

To begin, navigate to [[PDFoutput.com]] <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>.
1.  Click on "create PDF" <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>.
2.  Sign in with your Google account <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>.
3.  Enable the checkbox to grant [[PDFoutput.com]] access to specific files <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.
4.  Click "continue" to be redirected to the homepage <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.

## Selecting a Google Document as a Template

While [[PDFoutput.com]] offers pre-populated PDF templates <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>, you can also use a raw document from your Google Drive for custom templates <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.
1.  Click the link next to "Google document" <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.
2.  Select the desired document from your Google Drive <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>. For example, an "invitation letter PDF output invitation letter" can be used for sending invitations to users <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.
3.  Identify placeholders within the document that will be dynamically populated, such as "first name" and "last name" <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.

## Connecting to a Notion Database

[[generating_pdf_documents_for_business_purposes | Generating PDF documents]] requires a data source. [[PDFoutput.com]] leverages Notion databases to supply this data <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.
1.  In [[PDFoutput.com]], select "Notion" from the dropdown <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. This will prompt for a database URL and an API key <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>.

### Setting Up the Notion Database
1.  Open your Notion workspace <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.
2.  Create a new page (e.g., "PDF output database") <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>.
3.  Type `/database` and select "inline" to create a new database <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.
4.  Rename columns to match your placeholders, such as "first name" and "last name" <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.
5.  Add the data you wish to use for your documents (e.g., "Priya Sharma," "Miller Stark," "John quotes") <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.
6.  Once the database is created, click "share" and "copy link" to get the database URL <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>. Paste this URL into [[PDFoutput.com]] <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.

### Creating and Connecting the Notion API Key
1.  In [[PDFoutput.com]], click "add API key" <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
2.  Create a new internal integration (e.g., "notion PDF output connection") <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.
3.  Select the specific account and click "save" <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.
4.  Copy the generated API key value <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a> and paste it into [[PDFoutput.com]] <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>.
5.  Crucially, connect your Notion database to this API key:
    *   In Notion, click the three dots on your database page <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
    *   Select "connections" and search for "PDF output connection" <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>.
    *   Click "confirm" to establish the connection <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.

## Configuring PDF Generation

1.  In [[PDFoutput.com]], click "load properties" to fetch all columns (properties) from your Notion database <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.
2.  **Define Output File Name**: Select a property from the dropdown (e.g., "first name") to use as the name for the generated PDF files <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
3.  **Choose Output Folder**:
    *   **Google Drive**: Select "Google drive" and then choose or create a new folder (e.g., "invitation documents") <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.
    *   **Downloads Folder**: Opt to save files directly to your desktop's downloads folder <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>.
4.  **Map Placeholders**: In your Google Document, replace the static placeholders (e.g., "first name," "last name") with the corresponding properties fetched from Notion. Click the property name in [[PDFoutput.com]] to copy it, then paste it into your Google Doc <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>. These mapped properties will be dynamically replaced during generation <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.

## Generating PDFs

Once all settings are configured, click "export PDF" <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>. [[PDFoutput.com]] will begin [[generating_pdf_documents_for_business_purposes | generating the documents]] and saving them to your designated Google Drive folder <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>. The "PDF generated count" will increase as documents are created <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>.

You can view the generated documents directly in Google Drive, where you'll see the placeholders replaced with the data from your Notion database (e.g., "Jonty Roads," "Mirror Stark," "Priya Sharma") <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>. This demonstrates how a Notion database can be used to [[automating_pdf_generation_with_userdefined_templates | generate PDF documents in bulk]] <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>.

## Additional Features

*   **Templates**: [[PDFoutput.com]] provides predefined templates that you can use for various purposes <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>.
*   **History**: A "history" section tracks all previously generated documents <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.
*   **Upgrade**: Options to upgrade to a specific plan are available <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>.
*   **Contact**: For questions or queries, a contact section is provided at the bottom of the page <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>.