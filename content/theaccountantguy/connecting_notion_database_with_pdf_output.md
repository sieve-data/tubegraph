---
title: Connecting Notion database with PDF output
videoId: 6PR3AESuBoA
---

From: [[theaccountantguy]] <br/> 

[[setting_up_pdfoutput_for_notion_databases | PDFoutput.com]] is a tool designed to [[generating_pdf_documents_from_notion | generate PDF documents in bulk]] by leveraging Google Docs as templates and a Notion database for data [00:00:02] [00:00:08]. This guide details how to [[using_notion_as_a_database_for_pdf_generation | use Notion as a database for PDF generation]] using PDFoutput.com.

## Getting Started with PDFoutput.com

To begin, navigate to [[setting_up_pdfoutput_for_notion_databases | PDFoutput.com]] and click "create PDF" <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>. You will be prompted to sign in with a Google account <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>. After choosing your account and clicking "continue," enable the checkbox to grant PDFoutput specific file access <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. Click "continue" again to be redirected to the homepage <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.

## Selecting a Google Document Template

The homepage may display pre-populated PDF templates <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>. For a new setup, click the link next to the Google document icon to select a document from your Google Drive <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.

For instance, an "invitation letter PDF output invitation letter" can be selected <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>. This letter might require placeholders for user's first and last names <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.

## [[creating_a_notion_database_for_pdfs | Setting Up a Notion Database]]

To [[setting_up_a_notion_database_and_template_for_pdf_generation | set up a Notion database]] for this process:

1.  Open your Notion workspace <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.
2.  Create a new page, for example, "PDF output database" <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>.
3.  Type `/database` and select "inline" to create a new database <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>.
4.  Rename the database (e.g., "database PDF output") <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.
5.  Rename columns to match your template placeholders, such as "First Name" and "Last Name" <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.
6.  Populate the database with desired entries (e.g., Priya Sharma, Miller Stark, John Roads) <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.

## [[connecting_notion_database_to_pdf_generator | Connecting Notion to PDFoutput.com]]

To [[connecting_notion_databases_with_pdf_generation_tools | connect your Notion database with PDF generation tools]]:

1.  **Obtain Database URL:** From the Notion database view, click "Share," then "Copy link" to get the database URL <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>. Paste this URL into the "database URL" field in PDFoutput.com <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.
2.  **Generate API Key:** In PDFoutput.com, click "add API key" <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>. Create a new key, naming it (e.g., "notion PDF output connection") and selecting the relevant account <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>. Copy the generated key value <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>. Paste this key into the "API key" field in PDFoutput.com <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>.
3.  **Connect Database to API Key:** In Notion, click the three dots on your database page, select "Connections," and type "PDF output connection" to link the database to the API key <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>. Confirm the connection <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.
4.  **Load Properties:** In PDFoutput.com, click "Load properties" to fetch all column headers from your Notion database <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.

## Configuring PDF Output Settings

1.  **Output File Name:** Select a Notion property (e.g., "First Name") from the dropdown to define the output PDF file names <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
2.  **Output Location:** Choose "Google Drive" as the output folder <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>. Create a new folder in your Google Drive (e.g., "invitation documents") <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>. Then, in PDFoutput.com, click "add folder" and select the newly created Google Drive folder <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>. Alternatively, you can select the "downloads folder" to save files to your desktop <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>.

## Mapping Placeholders and Generating PDFs

1.  **Map Properties:** In your Google Doc template, replace placeholders (e.g., "[First Name]", "[Last Name]") with the corresponding properties fetched from Notion <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>. Click to copy the property name from PDFoutput.com and paste it into the Google Doc <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>.
2.  **Export PDFs:** Once all settings are configured, click "Export PDF" to start [[exporting_notion_data_to_pdf | exporting Notion data to PDF]] documents <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>. The "PDF generated count" will increase as documents are created <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>.
3.  **Verify Output:** After completion, click "view in Google drive" to open the folder and verify the generated PDFs <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>. The documents will show the Notion data replacing the placeholders, for example, "Jonty Roads," "Mirror Stark," and "Priya Sharma" <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>. This demonstrates [[using_notion_templates_and_databases_for_pdf_generation | using Notion templates and databases for PDF generation]] to bulk-generate documents <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>. The more information added to the Notion database, the more documents will be generated <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.

## Additional Features

*   **Templates:** PDFoutput.com provides predefined templates that can be used for various purposes <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>.
*   **History:** The "history" option allows you to view all documents generated in the past <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.
*   **Upgrade:** Users can upgrade to different plans <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>.
*   **Contact:** A contact section is available for queries or questions <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>.