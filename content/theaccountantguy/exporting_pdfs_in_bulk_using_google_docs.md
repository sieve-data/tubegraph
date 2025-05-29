---
title: Exporting PDFs in bulk using Google Docs
videoId: 6PR3AESuBoA
---

From: [[theaccountantguy]] <br/> 

[[pdfoutput_for_bulk_document_generation | PDFOutput.com]] is a tool designed to [[generating_bulk_pdf_documents_using_google_docs_and_notion | generate PDF documents in bulk]] by utilizing Google Docs as a template and integrating with a Notion database <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>.

## Getting Started with PDFOutput

To begin, navigate to PDFOutput.com and select "Create PDF" <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. You will be prompted to sign in with your Google account <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>. After choosing your account, you must enable the checkbox to grant [[pdfoutput_for_bulk_document_generation | PDFOutput]] access to specific files <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. Once enabled, click "Continue" to be redirected to the homepage <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.

## Creating a Bulk PDF Export Workflow

### Selecting a Google Docs Template

Upon reaching the homepage, you may see pre-populated PDF templates <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>. For a custom demonstration, you would use a raw Google document <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. Click the link next to "Google document" to view documents from your Google Drive <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>. For instance, an "invitation letter PDF output invitation letter" document can be selected to send invitation letters personalized with user's first and last names <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.

### Setting Up a Notion Database

A Notion database is used to store the data, such as first and last names, that will populate the PDF documents <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.

1.  **Create a New Page:** In your Notion workspace, create a new page, for example, "PDF output database" <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>.
2.  **Add an Inline Database:** Type `/database` and select "Inline" to create a new database <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>. Name it, e.g., "database PDF output" <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.
3.  **Define Columns:** Rename default columns to "first name" and "last name" <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>.
4.  **Populate Data:** Add names like "Priya Sharma," "Miller Stark," and "John quotes" to the database <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.

### Connecting Notion to PDFOutput

To connect your Notion database to [[pdfoutput_for_bulk_document_generation | PDFOutput]], you need the database URL and an API key <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.

1.  **Copy Database URL:** After creating the database, ensure you are in the database view <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>. Click "Share," then "Copy link" to get the database URL <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>. Paste this URL into the designated field in [[pdfoutput_for_bulk_document_generation | PDFOutput]] <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.
2.  **Generate API Key:** Click "Add API key" in [[pdfoutput_for_bulk_document_generation | PDFOutput]] to create a new API key in Notion, naming it something like "notion [[pdfoutput_for_bulk_document_generation | PDFOutput]] connection" <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>. Select your account and save it <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>. Copy the key value from Notion and paste it into [[pdfoutput_for_bulk_document_generation | PDFOutput]] <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.
3.  **Connect Database to API Key:** In Notion, click the three dots on your database page, select "Connections," and choose the "PDF output connection" you just created <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>. Confirm the connection <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.

### Mapping Properties and Output Settings

After connecting, click "Load properties" in [[pdfoutput_for_bulk_document_generation | PDFOutput]] to fetch the database columns <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.

*   **Output File Name:** Select "first name" from the dropdown to use the first name as the generated file name <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
*   **Output Folder:** Choose to save the files to a Google Drive folder or your local downloads folder <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>. To save to Google Drive, create a new folder (e.g., "invitation documents") in your Drive <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>, then click "Add folder" in [[pdfoutput_for_bulk_document_generation | PDFOutput]] and select it <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.

### Customizing the Template

To personalize your Google Doc template, replace placeholders with the Notion database properties <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>. In the [[pdfoutput_for_bulk_document_generation | PDFOutput]] interface, copy the "first name" and "last name" properties and paste them into the corresponding sections of your Google Doc template within the [[pdfoutput_for_bulk_document_generation | PDFOutput]] tool <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.

## [[generating_bulk_pdf_documents_using_google_docs_and_notion | Generating Bulk PDF Documents]]

Once all settings are configured, click "Export PDF" <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>. [[pdfoutput_for_bulk_document_generation | PDFOutput]] will begin [[generating_bulk_pdfs_with_database_integration | generating the documents]] and saving them to your designated Google Drive folder <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>. The "PDF generated count" will increase as documents are created <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>.

### Viewing Generated Documents

After generation, click "View in Google Drive" to open the folder <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>. You can then open each document to verify that the names from your Notion database (e.g., Jonty roads, Mirror Stark, Priya Sharma) have successfully replaced the placeholders in the template <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>. This demonstrates how Notion can serve as a database for [[generating_bulk_pdfs_with_database_integration | bulk PDF document generation]] <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>.

## Additional Features of PDFOutput

*   **Templates:** Access predefined templates for various purposes <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>.
*   **History:** View a record of all previously generated documents <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.
*   **Upgrade:** Options to upgrade to a specific plan are available <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>.
*   **Contact Section:** For questions or queries, a contact section is available at the bottom of the interface <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>.