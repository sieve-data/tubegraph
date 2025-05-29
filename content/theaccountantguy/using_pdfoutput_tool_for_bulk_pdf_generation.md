---
title: Using PDFoutput tool for bulk PDF generation
videoId: 6PR3AESuBoA
---

From: [[theaccountantguy]] <br/> 

[[Introduction to PDFOutput tool | PDFoutput.com]] is a tool designed to [[bulk_export_of_pdf_documents_using_pdf_output | generate PDF documents in bulk]] <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. It leverages Google Documents as templates <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a> and Notion databases for data input <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>.

## Getting Started

1.  **Access the Tool**: Navigate to [[Introduction to PDFOutput tool | PDF output.com]] <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>.
2.  **Create PDF**: Click on "create PDF" <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>.
3.  **Sign In**: Sign in using a Google account <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>.
4.  **Grant Access**: Enable the checkbox to provide [[Introduction to PDFOutput tool | PDF output]] access to specific files <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>, then click "continue" <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>. This redirects to the homepage <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.

## Step-by-Step Document Generation

### 1. Select a Google Document Template

The homepage displays pre-populated PDF templates <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. For custom documents, click the link next to "Google document" <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a> to view documents from your Google Drive <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>. Select your desired document, such as an "invitation letter PDF output invitation letter" <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.

The template should include placeholders for dynamic data, such as `first name` and `last name` <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>. These placeholders will be replaced with data from your Notion database.

### 2. Set Up Notion Database

[[Utilizing PDF output for document generation | PDF output]] integrates with Notion as a data source <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.

1.  **Create a Notion Database**:
    *   In Notion, create a new page, for example, "PDF output database" <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>.
    *   Type `/database` and select "inline" to create a new database <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.
    *   Rename columns to match your template placeholders, e.g., "first name" <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a> and "last name" <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.
    *   Populate the database with your desired data (e.g., Priya Sharma, Miller Stark, John Quotes) <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.
2.  **Obtain Database URL**:
    *   Ensure you are in the database view <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>.
    *   Click "share" <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>, then "copy link" <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a> to get the database URL <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.
    *   Paste this URL into the "database URL" field in [[Utilizing PDF output for document generation | PDF output]] <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.
3.  **Generate API Key**:
    *   Click on "add API key" <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a> in [[Utilizing PDF output for document generation | PDF output]], which will prompt you to create one in Notion <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.
    *   Create a new API key, naming it (e.g., "notion PDF output connection") <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a> and saving it <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.
    *   Copy the generated API key value <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a> and paste it into the "API key" field in [[Utilizing PDF output for document generation | PDF output]] <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>.
4.  **Connect Database to API Key**:
    *   In Notion, go to your database page, click the three dots (`...`) <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>, then "connections" <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>.
    *   Search for and select your "PDF output connection" <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a> and click "confirm" <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a> to link the database to the API key.

### 3. Map Data Fields and Define Output

1.  **Load Properties**: In [[Utilizing PDF output for document generation | PDF output]], click "load properties" <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>. This fetches all columns (properties) from your Notion database <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>.
2.  **Define Output File Name**: Select a property from the dropdown, such as "first name," to name the generated PDF files <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>.
3.  **Choose Output Folder**:
    *   Select "Google Drive" <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.
    *   Create a new folder in your Google Drive (e.g., "invitation documents") <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.
    *   In [[Utilizing PDF output for document generation | PDF output]], click "add folder" <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a> and select the newly created folder <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>.
    *   Alternatively, you can choose the "downloads folder" to save files directly to your desktop's download location <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>.
4.  **Map Placeholders**: Replace the static text in your Google Document template with the fetched properties. Copy the property names (e.g., `first name`, `last name`) from the [[Utilizing PDF output for document generation | PDF output]] interface and paste them into the corresponding locations in your Google Document template <a class="yt-timestamp" data-t="00:04:58">[00:04:58]</a>.

### 4. Export PDFs

Once all settings are configured, click "export PDF" <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>. [[Using PDF Output tool for invoice generation | PDF output]] will begin generating documents into your specified Google Drive folder <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>, updating the "PDF generated count" as it progresses <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>.

### 5. Verify Generated Documents

After generation is complete, click "view in Google Drive" <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a> to open the output folder. Open the generated PDFs to confirm that the placeholders have been correctly replaced with data from your Notion database (e.g., "Jonty Roads," "Mirror Stark," "Priya Sharma") <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>.

This process demonstrates how to [[using_pdf4put_for_bulk_pdf_creation | use Notion as a database]] to [[bulk_export_of_pdf_documents_using_pdf_output | generate PDF documents in bulk]] <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a>. The more information added to the Notion database, the more documents will be generated <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>.

## Additional Features

*   **Templates**: [[Features of PDFOutput tool | PDF output]] provides predefined templates for various purposes <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>.
*   **History**: The "history" option displays all previously generated documents <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>.
*   **Upgrade**: Users can upgrade to a specific plan by clicking the "upgrade" button <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>.
*   **Contact**: For questions or queries, a "contact section" is available at the bottom of the page <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>.