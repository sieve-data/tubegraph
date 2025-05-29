---
title: Creating and managing PDF templates in Google Drive
videoId: 6PR3AESuBoA
---

From: [[theaccountantguy]] <br/> 

[[generating_pdf_documents_for_businesses | PDFoutput.com]] is a tool designed to [[generating_bulk_pdf_documents_using_google_docs_and_notion | generate PDF documents in bulk]] by utilizing Google Docs as a template and a Notion database for data input <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>.

## Getting Started

1.  Navigate to PDFoutput.com <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>.
2.  Click on "Create PDF" <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>.
3.  Sign in with your Google account <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>.
4.  Enable the checkbox to grant PDFoutput access to specific files <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.
5.  Click "Continue" to be redirected to the homepage <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.

## Setting Up Your Template and Data Source

PDFoutput allows you to use pre-populated PDF templates or add your own raw Google Document for [[creating_and_using_templates_for_document_generation | document generation]] <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.

### 1. Selecting a Google Document Template

1.  Click the link next to "Google document" to add your template <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.
2.  Choose your desired document from Google Drive (e.g., an "invitation letter" template used in the demonstration) <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.
3.  Ensure your Google Doc template contains placeholders (e.g., "first name", "last name") that will be replaced by data from your database <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.

### 2. Connecting a Notion Database

1.  From the dropdown menu, select "Notion" as your data source <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.
2.  You will need a database URL and an API key <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>.

#### Creating Your Notion Database

1.  Open your Notion workspace <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.
2.  Create a new page (e.g., "PDF output database") <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>.
3.  Type `/database` and select "inline" to create a new database <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>.
4.  Name your database (e.g., "database PDF output") <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.
5.  Rename default columns to match your template placeholders (e.g., "first name", "last name") <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.
6.  Populate the database with your data (e.g., names like Priya Sharma, Miller Stark, John Quotes) <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.

#### Obtaining Notion Database URL and API Key

1.  **Database URL**:
    *   In Notion, go to your database view <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>.
    *   Click "Share" and then "Copy link" to get the database URL <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.
    *   Paste this URL into the PDFoutput.com interface <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.
2.  **API Key**:
    *   Click on "Add API key" in PDFoutput.com <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
    *   You will be prompted to create a new API key in Notion (e.g., "notion PDF output connection") <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.
    *   Select the appropriate account and save <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.
    *   Go back to the Notion API key page, click "Show" on the newly created key, copy its value, and paste it into PDFoutput.com <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.
3.  **Connect Database to API Key**:
    *   In Notion, on your database page, click the three dots (`...`) <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
    *   Select "Connections" and search for your API key (e.g., "PDF output connection") <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>.
    *   Click "Confirm" to connect the database to the API key <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.

## Configuring Output and Mapping

1.  **Load Properties**: In PDFoutput.com, click "Load properties" to fetch all column names from your Notion database <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.
2.  **Output File Naming**: Select a database property (e.g., "first name") from the dropdown to be used for naming your generated PDF files <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
3.  **Output Folder**:
    *   Choose to save files to your Google Drive or desktop downloads folder <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.
    *   To use Google Drive, create a new folder (e.g., "invitation documents") in your Drive <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>.
    *   In PDFoutput.com, click "Add folder" and select the newly created Google Drive folder <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.
4.  **Map Placeholders**: Replace the static placeholder text in the PDFoutput.com interface with the fetched properties from your Notion database (e.g., copy and paste "first name" and "last name" properties into their respective template locations) <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>.

## Generating and Managing PDFs

Once everything is set up, click "Export PDF" <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>. The tool will begin [[using_templates_to_generate_pdf_documents | generating the PDF documents]] and saving them to your specified Google Drive folder <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>. The PDF generated count will increase as documents are created <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>.

After generation, you can view the created PDFs in your Google Drive by clicking "View in Google Drive" <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>. The demonstration shows the tool successfully replacing placeholders with data from the Notion database (e.g., "Jonty Roads", "Mirror Stark", "Priya Sharma") <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>. The more information added to the database, the more documents will be generated <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.

## Additional Features

*   **Templates**: Access predefined templates that can be used for various purposes <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>.
*   **History**: View a record of all previously generated documents <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.
*   **Upgrade**: Option to upgrade to a specific plan <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>.
*   **Contact**: A contact section is available for queries <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>.