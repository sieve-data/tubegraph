---
title: Using API keys for connecting Notion to PDF generation tools
videoId: 6PR3AESuBoA
---

From: [[theaccountantguy]] <br/> 

[[using_pdf_output_tool_with_notion | PDFoutput.com]] is a tool designed to [[creating_pdf_documents_with_notion_templates | generate PDF documents in bulk]] by utilizing Google Docs as templates and a Notion database as the data source <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This article provides a [[stepbystep_guide_on_setting_up_api_keys_for_notion | step-by-step guide on setting up API keys for Notion]] to facilitate this process.

## Initial Setup of PDFoutput.com

1.  **Access and Sign-in**: Navigate to [[using_pdf_output_tool_with_notion | PDFoutput.com]] and click on "create PDF" <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. You will be prompted to sign in with a Google account <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>.
2.  **Grant Access**: Enable the checkbox to give [[using_pdf_output_tool_with_notion | PDF output]] access to specific files <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. Click "continue" to be redirected to the homepage <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.

### Selecting a Google Document Template

[[setting_up_pdfoutput_with_api_keys | PDFoutput.com]] allows the use of Google Docs as templates for PDF generation <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>.
1.  Click the link next to "Google document" on the [[using_pdf_output_tool_with_notion | PDF output]] homepage <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.
2.  Select the desired Google document from your Google Drive <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>. For example, an "invitation letter" where fields like "first name" and "last name" need to be populated <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.
3.  After selecting, the chosen document will load for use <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.

## [[connecting_notion_to_pdf_output_via_api_key | Connecting Notion to PDF Output via API Key]]

The next crucial step is [[integrating_notion_with_pdf_output_for_document_creation | integrating Notion with PDF Output for document creation]].

### Setting up the Notion Database

1.  From the dropdown in [[using_pdf_output_tool_with_notion | PDF output]], select "Notion" <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.
2.  [[setting_up_pdfoutput_with_api_keys | PDF output]] will request a database URL and an API key <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>.
3.  **Create a Notion Database**:
    *   Click the provided link to open your Notion workspace <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.
    *   Create a new page, e.g., "PDF output database" <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>.
    *   Type `/database` and select "inline" to create a new database <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.
    *   Name the database (e.g., "database PDF output") <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.
    *   Rename columns as needed, e.g., "first name" and "last name" <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.
    *   Populate the database with sample data <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.
4.  **Copy Database URL**:
    *   Ensure you are in the database view <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>.
    *   Click "Share" and then "Copy link" to get the database URL <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.
    *   Paste this URL into the "database URL" field in [[using_pdf_output_tool_with_notion | PDF output]] <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.

### [[steps_to_set_up_api_keys_for_pdf_generation | Steps to Set up API Keys for PDF Generation]]

An API key is required to connect your Notion database to [[using_pdf_output_tool_with_notion | PDF output]] <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.
1.  **Create API Key**:
    *   In [[using_pdf_output_tool_with_notion | PDF output]], click "add API key" <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
    *   This will prompt you to create a new key. Name it (e.g., "notion PDF output connection") <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>.
    *   Select your Notion account and click "save" <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.
2.  **Retrieve and Paste API Key**:
    *   Go to the newly created "PDF output connection" <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.
    *   Click "show" to reveal the key and "copy this value" <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.
    *   Paste the copied API key into the "API key" field in [[using_pdf_output_tool_with_notion | PDF output]] <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.
3.  **Connect Database to API Key**:
    *   In your Notion database, click the three dots (`...`) menu <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.
    *   Select "Connections" and search for "PDF output connection" <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
    *   Click "confirm" to connect the database to the API key <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.

## Mapping Properties and Generating PDFs

Once the Notion database is connected via the API key, you can map its properties to your Google Doc template.

1.  **Load Properties**: In [[using_pdf_output_tool_with_notion | PDF output]], click "load properties" <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>. This will fetch all available properties (columns) from your Notion database <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>.
2.  **Define Output File Name**: Select a property from the dropdown (e.g., "first name") to use for naming the generated PDF files <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
3.  **Choose Output Folder**:
    *   Select "Google drive" and create a new folder (e.g., "invitation documents") in your Google Drive <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.
    *   In [[using_pdf_output_tool_with_notion | PDF output]], click "add folder" and select the newly created Google Drive folder <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.
    *   Alternatively, you can choose the "downloads folder" to save files locally <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>.
4.  **Map Template Fields**: Replace the placeholder text in your Google Doc template (e.g., "first name", "last name") with the corresponding properties fetched from Notion <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>. Simply copy the property names from the loaded properties section and paste them into the template fields in [[using_pdf_output_tool_with_notion | PDF output]] <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>.
5.  **[[exporting_pdf_documents_from_notion | Exporting PDF Documents from Notion]]**: Click "export PDF" to begin generating the documents <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>. The count of generated PDFs will increase as the process completes <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.
6.  **Verify Generated PDFs**: Once complete, click "view in Google drive" to open the folder and verify that the PDFs have been generated with the correct data from your Notion database <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>.

## Additional Features

*   **Templates**: [[using_pdf_output_tool_with_notion | PDF output]] offers predefined templates for various purposes <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>.
*   **History**: The "history" option allows you to view all documents generated in the past <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.
*   **Upgrade**: Users can upgrade to specific plans for enhanced features <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>.
*   **Contact**: A "contact section" is available for queries and support <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>.