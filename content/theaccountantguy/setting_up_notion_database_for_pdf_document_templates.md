---
title: Setting up Notion database for PDF document templates
videoId: 6PR3AESuBoA
---

From: [[theaccountantguy]] <br/> 

PDFoutput.com is a tool designed to [[using_notion_database_and_templates_for_pdf_generation | generate PDF documents in bulk]] by [[connecting_notion_database_and_templates_to_pdf_output | utilizing Google documents as templates]] with the help of a Notion database <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>.

## Initial Setup of PDFoutput.com

To begin, navigate to PDFoutput.com and click on "create PDF" <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. You will be prompted to sign in with your Google account <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>. After choosing your account, ensure the checkbox to grant access to specific files for PDF output is enabled <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. Once enabled, click "continue" to be redirected to the homepage <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.

You can select a Google Document to use as a template <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>. For example, an "invitation letter PDF output invitation letter" can be chosen to send invitations to users, incorporating references to their first and last names <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.

## [[creating_a_database_in_notion | Creating a Database in Notion]]

To create a Notion database for PDF generation:
1.  Open your Notion workspace through the provided link <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.
2.  Create a new page, for instance, named "PDF output database" <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>.
3.  On the new page, type `/database` and select "inline" to [[creating_a_database_in_notion | create a new database]] <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.
4.  Rename the database, for example, "database PDF output" <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.
5.  Rename default columns to relevant properties, such as "first name" and "last name" <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>.
6.  Populate the database with sample data, such as "Priya Sharma," "Miller Stark," and "John Quotes" <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.

## [[setting_up_notion_api_keys_for_pdf_generation | Setting Up Notion API Keys]] and Database Connection

To [[connecting_notion_database_and_templates_to_pdf_output | connect your Notion database]] to PDFoutput.com:
1.  **Obtain Database URL**:
    *   From the Notion database view, click "share" <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.
    *   Click "copy link" to copy the database URL <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.
    *   Paste this URL into the "database URL" field on PDFoutput.com <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.
2.  **Create API Key**:
    *   In PDFoutput.com, click "add API key" <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>. This will prompt you to create a new key <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>.
    *   Create a new key, for example, named "Notion PDF output connection" <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.
    *   Select your Notion account and save the key <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.
    *   Go back to the "PDF output connection" you just created, click "show," and copy the displayed API key value <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.
    *   Paste this API key into the "API key" field on PDFoutput.com <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>.
3.  **Connect Database to API Key**:
    *   In Notion, click the three dots (`...`) for your database <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
    *   Go to "connections" and search for "PDF output connection" <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>.
    *   Confirm the connection <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.

## [[setting_up_notion_templates_and_databases_for_pdf_generation | Setting Up Notion Templates and Databases for PDF Generation]]

After [[connecting_notion_database_and_templates_to_pdf_output | connecting the Notion database]] and API key, click "load properties" in PDFoutput.com <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>. This will fetch and display all properties (columns) from your Notion database <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>.

### [[customizing_pdf_documents_using_notion_database_elements | Customizing PDF Documents Using Notion Database Elements]]

1.  **Define Output File Name**: Select a Notion property, such as "first name," from the dropdown to be used as the output file name for generated PDFs <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
2.  **Choose Output Folder**:
    *   Select "Google Drive" as the save location <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.
    *   Create a new folder in Google Drive (e.g., "invitation documents") <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.
    *   In PDFoutput.com, click "add folder" and select the newly created Google Drive folder <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>. Alternatively, you can choose to save files directly to your desktop's downloads folder <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>.
3.  **Map Properties to Template**: Replace placeholders in your Google Document template with the Notion properties <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>. For example, copy the "first name" property from PDFoutput.com and paste it into the document where the first name should appear <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>. Do the same for "last name" <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>.

## Generating PDF Documents

Once all settings are configured, click "export PDF" <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>. The tool will begin [[using_notion_database_and_templates_for_pdf_generation | generating the PDF documents]] and saving them to your defined Google Drive folder <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>. The count of generated PDFs will increase as the process continues <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>.

Upon completion, you can click "view in Google Drive" to access the generated documents <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>. The documents will show the placeholders replaced with the data from your Notion database, such as "Jonty Roads," "Mirror Stark," and "Priya Sharma" <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>. This demonstrates how Notion can be used as a database to [[using_notion_templates_and_databases_for_pdf_creation | generate PDF documents in bulk]] <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>.

PDFoutput.com also offers predefined templates and a history feature to track generated documents <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>.