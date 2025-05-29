---
title: Configuring API keys and database connections
videoId: 6PR3AESuBoA
---

From: [[theaccountantguy]] <br/> 

PDFoutput.com is a tool designed to generate PDF documents in bulk by leveraging Google Documents as templates and a Notion database for data input <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>.

## Initial Setup and Google Document Selection

To begin, navigate to PDFoutput.com and click on "create PDF" <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. You will be prompted to sign in with a Google account <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>. Ensure you enable the checkbox to grant PDFoutput access to specific files <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. After signing in, you can select a Google Document to use as a template <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>. For example, an invitation letter can be selected, which requires placeholders for dynamic data like "first name" and "last name" <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.

## Setting Up the Notion Database

To supply data for your PDF documents, you'll need a Notion database.
1.  In your Notion workspace, create a new page, for instance, named "PDF output database" <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>.
2.  Inside this page, type `/database` and select "inline" to create a new database <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>. Name the database, for example, "database PDF output" <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.
3.  Rename the default columns to match the placeholders in your Google Document, such as "first name" and "last name" <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.
4.  Populate the database with your desired data, like "Priya Sharma" or "John Roads" <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.
5.  To connect this database, first copy its URL: click on the "share" button in Notion, then "copy link" <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>. This URL will be pasted into PDFoutput.com <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.

## [[setting_up_api_keys_for_notion | Setting up Notion API Keys]]

An [[setting_up_api_keys_for_notion | API key]] is essential to [[integrating_notion_with_an_api_key_for_database_access | connect your Notion database]] to PDFoutput.com <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.
1.  In PDFoutput.com, click "add API key" <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>. This will prompt you to create a new key.
2.  Create a new internal integration, naming it something descriptive like "notion PDF output connection" <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.
3.  Once created, go back to the "notion PDF output connection" integration, click "show" to reveal the [[defining_and_using_api_keys_for_ai_engines_like_gemini_and_gpt | API key]], and copy its value <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.
4.  Crucially, ensure your Notion database is connected to this new [[setting_up_api_keys_for_notion | API key]]. In your Notion database, click the three dots (`...`), go to "connections", and select the "PDF output connection" <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>. Confirm the connection <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.

## [[connecting_notion_databases_via_api | Connecting Notion Database with PDFoutput]]

With the database URL and [[setting_up_api_keys_for_notion | API key]] ready, you can [[connecting_notion_databases_via_api | connect your Notion database]] to PDFoutput.com <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.
1.  In PDFoutput.com, paste the copied database URL and [[setting_up_api_keys_for_notion | API key]] into their respective fields <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>.
2.  Click "load properties" to fetch all column headers (properties) from your Notion database <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.

## Configuring Output and Mapping Properties

Before generating PDFs, you need to define how the output files will be named and where they will be saved.
1.  **Output File Name**: Select a database property, like "first name", from the dropdown to automatically name each generated PDF document <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
2.  **Output Folder**: Choose between saving files to your "downloads folder" (desktop) or a "Google Drive" folder <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>. If using Google Drive, create a new folder (e.g., "invitation docs") and then select it within PDFoutput.com <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>.
3.  **Mapping Properties**: Replace the placeholder text in your Google Document template with the corresponding Notion database properties. For example, if your template has "first name" and "last name" placeholders, copy the "first name" property from PDFoutput.com and paste it into the Google Doc, and do the same for "last name" <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>. These mapped properties will dynamically populate the document with data from each row of your Notion database <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.

## Generating and Verifying PDFs

Once all configurations are complete, click "export PDF" <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>. PDFoutput.com will begin generating documents, and you'll see a count increase as each PDF is created <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.
After generation, click "view in Google drive" to open the output folder <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>. Open the generated PDFs to verify that the placeholders have been correctly replaced with the data from your Notion database, such as "Jonty Roads", "Mirror Stark", or "Priya Sharma" <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>. The system will [[connecting_notion_database_with_api_for_bulk_document_generation | generate as many documents as there are entries]] in your Notion database <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.

PDFoutput.com also offers predefined templates <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a> and a "history" section to view past generated documents <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.