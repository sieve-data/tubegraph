---
title: Integrating Google Docs with Notion Database
videoId: 6PR3AESuBoA
---

From: [[theaccountantguy]] <br/> 

PDFoutput.com is a tool designed to [[using_google_docs_and_notion_for_bulk_pdf_generation | generate PDF documents in bulk]] by utilizing a Google Document as a template and a [[using_notion_as_a_template_and_database_for_pdfs | Notion database]] as the data source <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>.

## Getting Started with PDFoutput.com

1.  **Accessing the Tool**: Navigate to PDFoutput.com and click "Create PDF" <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>.
2.  **Sign-In and Permissions**:
    *   Sign in using a Google account <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>.
    *   Enable the checkbox to grant PDFoutput access to specific files <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.
    *   Click "Continue" to be redirected to the homepage <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.

## Setting Up Your Template and Database

### 1. Selecting the Google Document Template

*   From the PDFoutput homepage, click the link next to "Google document" <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.
*   Choose the desired document from your Google Drive, such as an "invitation letter PDF output invitation letter" <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>. This document will serve as the template, containing placeholders for dynamic data like "first name" and "last name" <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.

### 2. Setting Up the Notion Database

To [[connecting_notion_database_and_template_for_pdfs | connect a Notion database]], you'll need its URL and an API key <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>.

#### Creating the Database in Notion

1.  **Create a New Page**: In your Notion workspace, create a new page (e.g., "PDF output database") <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>.
2.  **Add an Inline Database**:
    *   Type `/database` and select "Database - Inline" <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>.
    *   Name the database (e.g., "database PDF output") <a class="yt=" data-t="00:01:55">[00:01:55]</a>.
    *   Rename columns to match your template's placeholders, such as "First Name" and "Last Name" <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.
3.  **Populate with Data**: Add entries to your database, including the first and last names for each record (e.g., Priya Sharma, Miller Stark, John Quotes) <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.
4.  **Obtain Database URL**:
    *   Ensure you are viewing the database directly <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>.
    *   Click "Share", then "Copy link" to get the database URL <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.

#### Creating and Connecting the API Key

1.  **Create API Key**:
    *   In PDFoutput.com, click "add API key" <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.
    *   Create a new integration key (e.g., "Notion PDF output connection") <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.
    *   Copy the generated API key <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.
2.  **Connect Database to API Key**:
    *   In Notion, open the database you created <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.
    *   Click the three dots `...` (page menu), then "Connections" <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
    *   Search for and select your created API key (e.g., "PDF output connection") and click "Confirm" <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>.

## Configuring PDF Output

1.  **Load Properties**: Back in PDFoutput.com, paste the database URL and API key into their respective fields <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>. Click "Load Properties" to fetch all column names from your Notion database <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.
2.  **Define Output File Name**: Select a Notion property (e.g., "First Name") from the dropdown to name the generated PDF files <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
3.  **Choose Output Folder**:
    *   Select "Google Drive" as the destination <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.
    *   Create a new folder in your Google Drive (e.g., "invitation documents from invitation docs") <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>.
    *   In PDFoutput, click "add folder" and select the newly created Google Drive folder <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>. Alternatively, you can save files to your local downloads folder <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>.
4.  **Map Placeholders**: In your Google Document template preview, replace generic placeholders (e.g., "first name", "last name") with the corresponding Notion database properties by copying and pasting them directly from the fetched properties list in PDFoutput <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.

## Generating PDF Documents

1.  **Export PDF**: Once all settings are configured, click "Export PDF" <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.
2.  **Monitor Progress**: The "PDF generated" count will increase as documents are created <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>.
3.  **Verify Output**:
    *   After generation is complete, click "View in Google Drive" <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>.
    *   Open the generated PDFs to confirm that the Notion database values (e.g., Jonty Roads, Mirror Stark, Priya Sharma) have correctly replaced the placeholders in the Google Doc template <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>.

This process demonstrates how to [[generating_pdf_documents_from_a_notion_database | generate PDF documents from a Notion database]] in bulk using a Google Docs template <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>. The more information added to the database, the more documents can be generated <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.

## Additional Features

*   **Templates**: PDFoutput.com offers predefined templates for various purposes <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>.
*   **History**: Users can view a history of all previously generated documents <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.
*   **Upgrade**: Options are available to upgrade to different plans <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>.
*   **Contact**: A contact section is available for queries <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>.