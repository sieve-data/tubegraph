---
title: Using Notion as a database for PDF generation
videoId: 6PR3AESuBoA
---

From: [[theaccountantguy]] <br/> 

PDFoutput.com is a tool that facilitates [[bulk_pdf_generation_from_notion_databases | bulk PDF generation]] by utilizing Google Docs as a template and a [[creating_a_notion_database_for_pdfs | Notion database]] for data sourcing <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>.

## Getting Started with PDFoutput.com

1.  **Sign In**: Navigate to PDFoutput.com and click "Create PDF". You will be prompted to sign in with a Google account <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>.
2.  **Grant Access**: Enable the checkbox to give PDFoutput access to specific files <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. After enabling, click "Continue" to be redirected to the homepage <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.

## Setting up Your Document Template (Google Docs)

PDFoutput.com allows you to use a raw Google Document as a template <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.
1.  **Select Google Document**: Click the link next to "Google document" to view documents from your Google Drive <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.
2.  **Choose Document**: Select the desired document, for example, an "invitation letter PDF output invitation letter" <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>. This document should contain placeholders (e.g., for first name, last name) that will be replaced by data from Notion <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.
3.  **Add Document to PDFoutput**: Back in PDFoutput, click to add the Google Document and select the chosen invitation letter <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.

## [[Connecting Notion database to PDF generator | Connecting Notion as a Database]]

To [[connecting_notion_database_to_pdf_generator | connect Notion]] as your data source, you will need a database URL and an API key <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>.

### [[Setting up a Notion database and template for PDF generation | Creating a Notion Database]]

1.  **Open Notion Workspace**: Click the provided link in PDFoutput to open your Notion workspace <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.
2.  **Create New Page**: Create a new page, for instance, named "PDF output database" <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>.
3.  **Add Inline Database**: Type `/database` and select "Inline" to create a new database <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. Name it (e.g., "database PDF output") <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.
4.  **Define Columns**: Rename default columns or add new ones needed for your PDF, such as "First Name" and "Last Name" <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.
5.  **Populate Data**: Add sample names like "Priya Sharma," "Miller Stark," and "John quotes" to the database <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.
6.  **Copy Database URL**: Go to the database view, click "Share," then "Copy link" to get the database URL <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>. Paste this URL into the PDFoutput application <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.

### Creating and Connecting a Notion API Key

1.  **Create API Key**: In PDFoutput, click "add API key" <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>. Create a new key (e.g., "notion PDF output connection") and select the appropriate account <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.
2.  **Copy API Key**: Go back to the "PDF output connection" you just created, click "Show," and copy the key's value <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>. Paste this key into PDFoutput <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.
3.  **Connect Database to API Key in Notion**: In your Notion database, click the three dots, then "Connections," and search for "PDF output connection" <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>. Click "Confirm" to establish the connection <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.

## Configuring PDF Generation Settings

With the Notion database connected via API key and URL <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>:

1.  **Load Properties**: Click "Load properties" in PDFoutput. This will fetch all column names (properties) from your Notion database <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.
2.  **Define Output File Name**: Select a Notion property (e.g., "First Name") from the dropdown to be used as the output PDF file name <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
3.  **Select Output Folder**:
    *   **Google Drive**: Choose "Google drive" and create a new folder (e.g., "invitation documents") in your Google Drive <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>. Add this folder in PDFoutput <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.
    *   **Downloads Folder**: Alternatively, select "Downloads folder" to save files directly to your desktop downloads <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.
4.  **Map Properties to Document Placeholders**:
    *   In the Google Document template view within PDFoutput, copy the fetched Notion properties (like `{{first name}}` and `{{last name}}`) <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.
    *   Paste these properties into your Google Doc template where you want the corresponding data to appear <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>. You can format these placeholders (e.g., bold, red) <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>.

## [[Generating PDF documents from Notion | Generating PDFs]]

1.  **Export PDF**: Once everything is set, click "Export PDF" <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.
2.  **Monitor Progress**: The PDF generated count will increase as documents are created <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.
3.  **View Generated Files**: After generation, click "view in Google drive" to open the folder containing your new PDFs <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>. You will see that the placeholders in the template have been replaced with the data from your Notion database (e.g., "Jonty Roads," "Mirror Stark," "Priya Sharma") <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>. The more information you add to the Notion database, the more documents can be generated <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.

## Additional Features of PDFoutput.com

*   **Templates**: Predefined PDF templates are available for use <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>.
*   **History**: A "History" option allows you to view all documents generated in the past <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.
*   **Upgrade**: You can upgrade to a specific plan by clicking the "Upgrade" option <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>.
*   **Contact**: A contact section is available for queries or assistance <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>.