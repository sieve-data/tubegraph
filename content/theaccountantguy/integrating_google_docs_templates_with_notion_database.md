---
title: Integrating Google Docs templates with Notion database
videoId: 6PR3AESuBoA
---

From: [[theaccountantguy]] <br/> 

PDFoutput.com is a tool designed to generate PDF documents in bulk by utilizing Google Docs as a template in conjunction with a Notion database <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. This process allows for document automation, such as creating personalized invitation letters based on data stored in Notion <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>, <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.

## Getting Started with PDFoutput.com

To begin, navigate to PDFoutput.com and click on "create PDF" <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. You will be prompted to sign in with a Google account <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>. After choosing an account, enable the checkbox to grant PDFoutput specific file access <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. Once enabled, click "continue" to be redirected to the homepage <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.

## Selecting a Google Docs Template

While PDFoutput.com offers pre-populated PDF templates <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>, you can also use a raw Google Doc for custom purposes <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.

1.  Click the link next to "Google document" to view documents from your Google Drive <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.
2.  Select the desired document, such as an "invitation letter" <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>. This document should contain placeholders (e.g., `first name`, `last name`) that will be populated from your Notion database <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.
3.  Back on PDFoutput, select the chosen Google Doc from the list <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.

## Setting Up a Notion Database

[[connecting_notion_database_to_google_docs_for_document_automation | Connecting a Notion database to Google Docs]] requires a specific setup within Notion to enable the integration.

1.  From the PDFoutput interface, select "Notion" from the dropdown <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.
2.  Click the provided link to open your Notion workspace <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.
3.  **Create a New Notion Page and Database**:
    *   Click on "new page" <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>.
    *   Name the page, e.g., "PDF output database" <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.
    *   Type `/database` and select "inline" to create a new database <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>.
    *   Rename default columns to match your Google Doc placeholders, such as "first name" and "last name" <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.
    *   Populate the database with sample data (e.g., Priya Sharma, Miller Stark, John Coats) <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.

4.  **Obtain Database URL**:
    *   Ensure you are in the database view <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>.
    *   Click "share" and then "copy link" to get the database URL <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.
    *   Paste this URL into the corresponding field on PDFoutput <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.

5.  **Create and Connect an API Key**:
    *   Click "add API key" on PDFoutput <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
    *   Create a new integration key in Notion, naming it (e.g., "PDF output connection") and selecting the appropriate account <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.
    *   Copy the generated API key value <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.
    *   Paste the API key into the corresponding field on PDFoutput <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.

6.  **Connect Database to API Key**:
    *   In Notion, go to the three dots menu of your database <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.
    *   Click "connections" and search for the API key you just created (e.g., "PDF output connection") <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
    *   Click "confirm" to link the database to the API key <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.

## Configuring PDF Generation

1.  On PDFoutput, click "load properties" to fetch all column headers (properties) from your Notion database <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.
2.  **Define Output File Name**: Select a Notion property from the dropdown (e.g., "first name") to use for naming the generated PDF files <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
3.  **Select Output Destination**:
    *   Choose "Google Drive" to save documents to a specified folder <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.
    *   Create a new folder in Google Drive (e.g., "invitation documents") <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>.
    *   Click "add folder" on PDFoutput and select the newly created Google Drive folder <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.
    *   Alternatively, select the "downloads folder" to save files locally <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>.
4.  **Map Google Doc Placeholders**: In your Google Doc template, replace the placeholder text (e.g., `first name`, `last name`) with the corresponding Notion properties copied from PDFoutput <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>. Ensure accurate mapping for correct data population <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.

## Generating PDFs

With all settings configured, click "export PDF" <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>. PDFoutput will start generating documents and display a count of generated PDFs <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>. Once complete, click "view in Google Drive" to access the newly created personalized documents <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>. Each document will have its placeholders replaced with the data from the Notion database, e.g., "Jonty Roads", "Mirror Stark", "Priya Sharma" <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>.

## Additional Features

PDFoutput.com offers several other useful features:
*   **Templates**: Predefined templates that can be used for various purposes <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>. This is part of [[creating_and_using_templates_in_notion | Creating and using templates in Notion]] and [[creating_and_managing_templates_in_notion | Creating and managing templates in Notion]].
*   **History**: A log of all past generated documents <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.
*   **Upgrade Options**: Information on upgrading to a specific plan <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>.
*   **Contact Section**: A contact section for questions or queries <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>.

This integration provides a powerful way of [[integrating_databases_with_templates_in_notion | integrating databases with templates in Notion]] to streamline document creation, especially for [[creating_and_using_notion_templates_for_pdfs | creating and using Notion templates for PDFs]].