---
title: Creating and utilizing PDF templates
videoId: 6PR3AESuBoA
---

From: [[theaccountantguy]] <br/> 
PDFoutput.com is a tool designed to [[using_templates_to_automate_pdf_creation | generate PDF documents in bulk]] by utilizing Google Documents as templates, with the help of a Notion database <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>.

## Getting Started

To begin using PDFoutput.com, follow these steps:
1.  Navigate to PDFoutput.com <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>.
2.  Click "Create PDF" <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>.
3.  Sign in through a Google account <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>.
4.  Enable the checkbox to grant PDFoutput access to specific files <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.
5.  Click "Continue" to be redirected to the homepage <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.

## [[creating_and_using_templates_for_pdf_generation | Creating and Using Templates for PDF Generation]]

PDFoutput.com allows users to leverage existing Google Documents as templates or use predefined templates <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>.

### Using a Google Document as a Template

For a demonstration, a raw Google Document can be used <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.
1.  Click the link next to "Google document" to view documents listed in your Google Drive <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.
2.  Select the desired document, for instance, an "invitation letter PDF output invitation letter" <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>. This document needs placeholders (e.g., for first name and last name) that will be populated from a database <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.
3.  Back on PDFoutput, click to add the Google Document and select it <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.

### Connecting to a Notion Database

To populate the template, a Notion database is used <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. This process involves [[managing_connections_and_templates_in_pdf_output | managing connections and templates in PDF Output]].
1.  Select "Notion" from the dropdown <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.
2.  The system will request a database URL and an API key <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>.

#### Setting Up the Notion Database
1.  Click the link to open your Notion workspace <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.
2.  Create a new page, for example, "PDF output database" <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>.
3.  Type `/database` and select "inline" to create an inline database <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>.
4.  Name the database, e.g., "database PDF output" <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.
5.  Rename columns to match your template's placeholders, such as "first name" and "last name" <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>.
6.  Add data entries (e.g., names like "Priya Sharma," "Miller Stark," "John Quotes") <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.
7.  Once the database is set up, click "Share" and "Copy link" to get the database URL <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>. Paste this URL into PDFoutput <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.

#### Creating the Notion API Key
1.  Click "add API key" within PDFoutput <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
2.  Create a new key (e.g., "notion PDF output connection"), select the account, and save <a class="yt-timestamp" data-t="00:02:54">[00:03:07]</a>.
3.  Go back to the newly created connection in Notion, click "Show" to reveal the key, and copy its value <a class="yt-timestamp" data-t="00:03:09">[00:03:15]</a>.
4.  Paste the API key into PDFoutput <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.

#### Connecting Database and API Key
1.  In Notion, for the created database, click the three dots, then "Connections" <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
2.  Type and select "PDF output connection" and confirm <a class="yt-timestamp" data-t="00:03:27">[00:03:34]</a>.

## [[customizing_templates_for_pdf_document_generation | Customizing Templates for PDF Document Generation]]

### Loading Properties and Output Settings
1.  In PDFoutput, click "Load properties" <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>. This fetches all properties from the Notion database <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>.
2.  **Output File Name:** Select a property from the dropdown, such as "first name," to define the output file name <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
3.  **Output Folder:**
    *   Choose "Google drive" to save files to your Google Drive <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.
    *   Create a new folder in Google Drive (e.g., "invitation documents") <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>.
    *   In PDFoutput, click "add folder" and select the newly created Google Drive folder <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.
    *   Alternatively, select "downloads folder" to save files directly to your desktop's download folder <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>.

### Mapping Template Placeholders
To [[customizing_templates_for_pdf_document_generation | customize templates for PDF document generation]], replace the generic text in your Google Doc template with the fetched properties:
1.  Copy the property name (e.g., "first name") from PDFoutput <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.
2.  Paste it into the Google Doc template where the first name should appear <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>.
3.  Repeat for other properties, such as "last name" <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>.
4.  These mapped properties will pull data from the Notion database <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.

## Generating PDFs

Once all settings are configured, click "Export PDF" <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>. PDFoutput will begin generating documents to the defined Google Drive folder, with the PDF generated count increasing as files are created <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>.

Generated documents will show the replaced text from the database (e.g., "Jonty Roads," "Mirror Stark," "Priya Sharma") <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>. The more information added to the database, the more documents will be generated <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.

## Additional Features

PDFoutput offers several other features for [[managing_pdf_output_templates_and_settings | managing PDF Output templates and settings]]:
*   **Templates:** Access predefined templates that can be used for various purposes <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>. These are [[customizable_pdf_templates | customizable PDF templates]] to meet specific needs <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>.
*   **History:** View all documents that have been generated in the past <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.
*   **Upgrade:** Option to upgrade to a specific plan <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>.
*   **Contact:** A contact section is available for any questions or queries <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>.