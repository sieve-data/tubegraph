---
title: Setting up and connecting Notion database for PDF creation
videoId: 6PR3AESuBoA
---

From: [[theaccountantguy]] <br/> 

This article details how to [[pdf_document_creation_with_notion_and_pdf_output | create PDF documents]] in bulk using PDFoutput.com, a Google Document as a template, and a [[setting_up_and_managing_notion_databases_for_pdf_generation | Notion database]] for data.

## Getting Started with PDFoutput.com

PDFoutput.com is a tool designed to [[generating_pdf_documents_using_notion | generate PDF documents]] in bulk by leveraging Google Docs as templates and a Notion database for dynamic content <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>.

1.  **Access and Sign In**: Navigate to PDFoutput.com and click "Create PDF" <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. You will be prompted to sign in with a Google account <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>.
2.  **Grant Access**: Enable the checkbox to give PDFoutput access to specific files <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. After enabling, click "Continue" to be redirected to the homepage <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.

## Selecting a Google Document Template

PDFoutput.com allows you to use existing templates or a raw Google Document for your PDFs <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>.

1.  **Choose Document**: Click the link next to "Google document" to view documents from your Google Drive <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.
2.  **Select Template**: Choose your desired Google Doc (e.g., "Invitation Letter PDF Output Invitation Letter") <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>. This document will serve as the template, containing placeholders (e.g., `first name`, `last name`) that will be populated by the Notion database <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.

## [[setting_up_a_database_in_notion | Setting up a Notion Database]]

To [[generating_pdf_documents_from_notion_database_rows | generate PDF documents from Notion database rows]], you first need to [[setting_up_and_managing_notion_databases_for_pdf_generation | set up a Notion database]] with the required data.

1.  **Create New Notion Page**: Open your Notion workspace and create a new page, naming it appropriately (e.g., "PDF Output Database") <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.
2.  **Insert Inline Database**: Type `/database` and select "Database - Inline" to create a new inline database <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>. Name the database (e.g., "Database PDF Output") <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.
3.  **Define Columns**: Rename default columns to match your template placeholders, such as "first name" and "last name" <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.
4.  **Add Data**: Populate the database with entries, filling in the defined columns (e.g., Priya Sharma, Miller Stark, John Coates) <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.

## [[connecting_notion_database_to_pdf_output_via_api_keys | Connecting Notion Database to PDFoutput.com]]

Connecting your Notion database involves obtaining its URL and creating an API key. This process [[integrating_notion_database_with_pdf_output | integrates the Notion database with PDF output]].

### Obtaining the Database URL

1.  **Access Database View**: Ensure you are in the database view within Notion <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>.
2.  **Copy Link**: Click the "Share" button at the top right, then click "Copy link" to get the database URL <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.
3.  **Paste into PDFoutput**: Return to PDFoutput.com and paste the copied URL into the "Database URL" field <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.

### Creating and Connecting the API Key

1.  **Generate API Key**: In PDFoutput.com, click "Add API key" <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>. This will lead you to Notion's integration settings. Create a new integration key (e.g., "Notion PDF Output Connection") <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.
2.  **Copy API Key**: After creation, go back to the integration you just made, click "Show," and copy the API key value <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.
3.  **Paste into PDFoutput**: Paste this API key into the "API Key" field on PDFoutput.com <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.

    > [!WARNING] Ensure the Notion database is connected to the API key.
    > In Notion, click the three dots (`...`) menu for your database, select "Connections," and choose your API key (e.g., "PDF Output Connection") <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>. Confirm the connection <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.

## Mapping Properties and Setting Output

After connecting, you need to map your Notion database properties to the Google Doc template and define where the generated PDFs will be saved.

1.  **Load Properties**: Click "Load properties" in PDFoutput.com. This will fetch all column headers (properties) from your Notion database <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.
2.  **Define Output File Name**: Select a Notion property to use as the output file name (e.g., "first name") <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
3.  **Choose Output Folder**:
    *   **Google Drive**: Select "Google drive" and create a new folder (e.g., "Invitation documents from invitation docs") <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>. Add and select this folder in PDFoutput.com <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.
    *   **Downloads Folder**: Alternatively, choose "Downloads folder" to save files to your desktop downloads <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>.
4.  **Map Placeholders**: In your Google Doc template, replace generic placeholders (e.g., `first name`, `last name`) with the exact property names fetched from Notion <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>. Simply copy the property name from PDFoutput.com and paste it into the Google Doc <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.

## [[generating_pdf_documents_using_notion | Generating PDF Documents]]

Once all settings are configured, you can initiate the PDF generation process. This uses Notion for [[generating_pdf_documents_from_notion_database_rows | generating PDF documents from database rows]].

1.  **Export PDF**: Click "Export PDF" <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>. PDFoutput.com will begin [[using_notion_for_generating_pdf_documents | generating PDF documents]] based on each row in your Notion database <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>.
2.  **Monitor Progress**: The "PDF generated" count will increase as documents are created <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>.
3.  **View Output**: Once complete, click "View in Google drive" to open the folder containing your newly generated PDFs <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>. The generated documents will have replaced the placeholders with data from your Notion database (e.g., "Jonty Roads", "Miller Stark", "Priya Sharma") <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>.

The more information you add to your Notion database, the more documents PDFoutput.com will generate for your use case <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.

## Additional Features

*   **Templates**: PDFoutput.com provides predefined templates for various purposes <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>.
*   **History**: The "History" section displays all documents previously generated <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.
*   **Upgrade**: Options to upgrade to a specific plan are available <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>.
*   **Contact**: For questions or queries, a contact section is available at the bottom of the page <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>.