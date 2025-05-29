---
title: Using PDFoutputcom to generate PDF documents in bulk
videoId: 6PR3AESuBoA
---

From: [[theaccountantguy]] <br/> 

[[introduction_to_pdfoutput_tool | PDFoutput.com]] is a tool designed to [[bulk_pdf_document_generation | generate PDF documents in bulk]] by utilizing Google Docs as templates and Notion databases for data management <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. This guide outlines the steps to [[generating_pdf_documents_in_bulk_using_notion_and_pdfoutput | generate PDF documents in bulk using Notion and PDFOutput]].

## Getting Started with PDFOutput

To begin using PDFOutput, follow these initial steps:
1.  Navigate to PDFoutput.com <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>.
2.  Click on "Create PDF" <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>.
3.  Sign in with your Google account <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>.
4.  Enable the checkbox to grant PDFOutput access to specific files <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.
5.  Click "Continue" to be redirected to the homepage <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.

## Setting Up Your Document Template

PDFOutput uses Google Docs as templates for generating PDFs.
1.  On the PDFOutput homepage, click the link next to "Google document" to select your template <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.
2.  Choose your desired Google Doc from your Google Drive <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>. For example, an "invitation letter" document might be used <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.
3.  Identify placeholders in your Google Doc template (e.g., `first name`, `last name`) that will be populated with data <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.

## Connecting to Notion as a Database

PDFOutput integrates with Notion to pull dynamic data for your PDFs.
1.  From the dropdown menu in PDFOutput, select "Notion" <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.
2.  PDFOutput will request a database URL and an API key <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>.

### Creating a Notion Database
1.  Click the provided link to open your Notion workspace <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.
2.  Create a new page (e.g., "PDF output database") <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>.
3.  Type `/database` and select "Inline" to create a new database <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>.
4.  Rename columns as needed (e.g., "first name", "last name") <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.
5.  Populate the database with your data (e.g., names like Priya Sharma, Miller Stark, John Roads) <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.
6.  Once the database view is active, click "Share" and then "Copy link" to get the database URL <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>. Paste this URL into PDFOutput <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.

### Creating and Connecting a Notion API Key
1.  In PDFOutput, click "Add API key" <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
2.  Create a new internal integration key in Notion (e.g., "notion PDF output connection") <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.
3.  Select the desired account and click "Save" <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.
4.  Go back to the newly created integration, click "Show", and copy the API key value <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>. Paste this key into PDFOutput <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>.
5.  **Crucially**, ensure your Notion database is connected to this API key. In Notion, click the three dots on your database, select "Connections", and type "PDF output connection" to confirm the link <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.

## Configuring Output and Mapping Data

### Loading Properties and Output Settings
1.  In PDFOutput, click "Load properties" <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>. This will fetch all available properties from your Notion database <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>.
2.  Select the "output file name" property from the dropdown (e.g., "first name") to name your generated PDFs <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
3.  Choose your "output folder":
    *   **Google Drive:** Select "Google drive" <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>. You can create a new folder (e.g., "invitation documents") in Google Drive and then select it in PDFOutput <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>.
    *   **Downloads Folder:** Choose this option to save files directly to your desktop's downloads folder <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>.

### Mapping Fields
1.  In your Google Doc template within PDFOutput, replace your placeholders (e.g., `first name`, `last name`) with the corresponding properties fetched from Notion <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>. Simply copy the property name from the list and paste it into the document <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>.
2.  Optionally, format the mapped fields (e.g., bold, red) for clarity <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.

## Generating and Exporting PDFs

Once all settings are configured, you can [[generating_and_downloading_pdf_documents_in_bulk | generate and download PDF documents in bulk]]:
1.  Click "Export PDF" <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.
2.  PDFOutput will start generating the documents and saving them to your designated output folder <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>.
3.  Monitor the "PDF generated count" as documents are created <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>.
4.  After generation, click "View in Google Drive" (or check your downloads) to verify the documents <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>. The generated PDFs will show the placeholders replaced with the data from your Notion database (e.g., "Jonty Roads", "Mirror Stark", "Priya Sharma") <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>.

## Additional Features

PDFOutput offers other useful features:
*   **Templates:** Access predefined templates for various purposes <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>.
*   **History:** View a record of all previously generated documents <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.
*   **Upgrade:** Options to upgrade your plan <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>.
*   **Contact:** Reach out for support or queries via the contact section <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>.