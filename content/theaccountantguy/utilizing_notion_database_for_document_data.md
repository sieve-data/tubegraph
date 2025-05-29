---
title: Utilizing Notion database for document data
videoId: 6PR3AESuBoA
---

From: [[theaccountantguy]] <br/> 

PDFoutput.com is a tool designed to [[generating_pdf_documents_from_notion_database | generate PDF documents in bulk]] by leveraging Google Docs as a template and a [[notion_database | Notion database]] for data management <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>.

## Getting Started with PDFoutput.com

To begin, navigate to PDFoutput.com and click on "create PDF" <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. You will be prompted to sign in with a Google account <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>. After choosing your account, you must enable the checkbox that grants PDFoutput access to specific files <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. Once enabled, click "continue" to be redirected to the homepage <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.

## Preparing the Google Document Template

PDFoutput.com allows you to use existing PDF templates or a raw Google document for your bulk generation needs <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. To select a Google Doc, click the link next to "Google document" on the PDFoutput homepage <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>. This will display documents from your Google Drive <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.

For instance, an "invitation letter" document can be used as a template, requiring placeholders for dynamic information like the user's first name and last name <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>. Once selected, the document will load into PDFoutput.com <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.

## [[connecting_notion_database_with_api_for_bulk_document_generation | Connecting to a Notion Database]]

The next step is to select "Notion" from the dropdown menu in PDFoutput.com <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>. This requires a database URL and an API key <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>.

### [[creating_a_database_in_notion | Creating and Setting Up a Notion Database]]

1.  **Access Notion Workspace**: Click the provided link in PDFoutput.com to open your Notion workspace <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.
2.  **[[setting_up_a_database_in_notion | Create a New Page]]**: Go to "new page" and create a new page (e.g., "PDF output database") <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>.
3.  **Insert an Inline Database**: Type a forward slash (`/`) and select "database inline" to create an inline database <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>. Name the database (e.g., "database PDF output") <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>.
4.  **Define [[properties_in_notion_databases | Database Properties]]**: Rename default columns to match your required data, such as "first name" and "last name" <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.
5.  **Populate Data**: Add your desired data rows (e.g., names like "Priya Sharma," "Miller Stark," "John Coates") <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.
6.  **Copy Database URL**: With the database view open, click "share," then "copy link" to obtain the database URL <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>. Paste this URL into the corresponding field in PDFoutput.com <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.

### Obtaining and [[linking_databases_in_notion | Connecting the API Key]]

1.  **Create API Key**: Click on "add API key" in PDFoutput.com <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>. Create a new key (e.g., "notion PDF output connection") and select your account <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>. Save the key <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.
2.  **Copy API Key Value**: Go back to the "PDF output connection" you just created, click "show," and copy the key value <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>. Paste this value into PDFoutput.com <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>.
3.  **Connect Database to API Key**: In Notion, open the database you created, click the three dots, select "connections," and type "PDF output connection" <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>. Click "confirm" to establish the connection <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.

### Loading Properties and Mapping Fields

Once the Notion database is connected, click "load properties" in PDFoutput.com <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>. This will fetch all the properties (columns) from your Notion database <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>.

*   **Define Output File Name**: Select a Notion property (e.g., "first name") from the dropdown to be used as the output file name <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
*   **Choose Output Folder**: You can save the generated PDFs to a Google Drive folder or your local downloads folder <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>. To use Google Drive, create a new folder (e.g., "invitation docs") in your drive <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>, then click "add folder" in PDFoutput.com to select it <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.
*   **Map Google Doc Placeholders**: In your Google Doc template, remove the placeholder text <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>. From the fetched Notion properties in PDFoutput.com, click to copy the desired property (e.g., "first name," "last name") and paste it into the corresponding location in your Google Doc template <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>. This links the template fields to your [[notion_database | Notion database]] properties <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>.

## [[generating_pdf_documents_from_notion_database | Generating PDF Documents]]

After all settings are configured, click "export PDF" <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>. PDFoutput.com will begin [[using_notion_for_bulk_document_creation | generating PDF documents]] based on each row in your Notion database, saving them to your specified output folder <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>. The "PDF generated" count will update as documents are created <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>.

Once complete, you can click "view in Google Drive" to open the folder and verify the generated documents <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>. Each document will dynamically feature the data (e.g., names) from the corresponding Notion database entry <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>. This demonstrates how a [[notion_database | Notion database]] can be used for [[creating_pdf_documents_from_a_notion_database | bulk PDF document generation]] <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>.

## Additional Features

PDFoutput.com also offers:
*   **Templates**: Predefined templates for various purposes <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>.
*   **History**: A record of all previously generated documents <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.
*   **Upgrade Options**: For accessing more features or higher limits <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>.

For any questions, a "contact section" is available at the bottom of the page <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>.