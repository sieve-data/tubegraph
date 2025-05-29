---
title: Utilizing API keys to connect Notion to PDF generation tools
videoId: Uh1g7uXtr_4
---

From: [[theaccountantguy]] <br/> 

This article outlines how to generate PDF documents in bulk from a Notion database using an external tool, specifically PDF Output, by leveraging Notion's API keys <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. This method allows for the automated creation of PDF files for each row of data in a Notion database, eliminating the need for manual data entry and individual exports <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.

## Setting up the Notion Database for PDF Generation

To begin, you need a Notion database containing the information you wish to convert into PDFs, such as an application form database tracking candidate profiles and education requirements <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.

### Creating a Template with Placeholders

A key step is to create an application form template that mirrors the fields in your Notion database <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.
*   This template includes placeholder elements enclosed in curly brackets, like `{Full Name}`, `{Date of Birth}`, `{Gender}`, and `{Phone Number}` <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. These placeholders must exactly match the column names in your Notion database <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.
*   This template content needs to be pasted into each row of your Notion database. Open each row, scroll to the bottom, and paste the template into the empty section <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.

### Setting a Default Template for New Rows

To automate the inclusion of the template in new database entries:
1.  Click the dropdown next to the "New" button in your Notion database <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.
2.  Select "New template" <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>.
3.  Give the template a name (e.g., "Applicant Name") <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.
4.  Paste your template content into this new template page <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.
5.  Click the three dots next to the newly created template and select "Set as default" for all views in your database <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.
    *   This ensures that any new row added to the database will automatically include the template <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.

## Connecting Notion with PDF Output Tool using API Keys

The tool used for this process is PDF Output, which requires a Notion database to [[generating_pdf_documents_from_notion | generate documents in bulk]] <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>. The connection is established using Notion's API key.

### [[connecting_notion_databases_with_external_tools_using_api_keys | Copying the Notion Database URL]]
First, copy the URL of your Notion database from your browser's address bar <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>. This URL will be pasted into the PDF Output tool <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.

### [[setting_up_api_keys_in_notion | Obtaining the Notion API Key]]
The database must be connected to PDF Output via an API key, which is confidential and private <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.
1.  In Notion, navigate to your Integrations settings. You can often find a direct link within the PDF Output tool itself, labeled "Click here to add API key" <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>.
2.  Click "New integration" <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>.
3.  Add a new name for your integration and choose your workspace <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.
4.  After creation, find the integration you just made. Click on it and then click "Show" next to "Internal Integration Secret" <a class="yt-timestamp" data-t="00:04:58">[00:04:58]</a>. This is the API key you need <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.
5.  Copy this key and paste it into the designated field in the PDF Output tool <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>.

### [[connecting_notion_database_to_pdf_generator | Linking the Notion Database to the API Key]]
Even after obtaining the API key, you must explicitly connect your specific Notion database to this key:
1.  In your Notion database, click the three dots menu (usually top right) <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>.
2.  Select "Connections" <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>.
3.  Search for and select the name of the integration (API key) you just created <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>.
4.  Click "Confirm" to establish the connection <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>.

### [[generating_pdf_documents_from_notion | Publishing the Notion Database]]
The final crucial step for the PDF output tool to access your database is to publish it:
1.  In your Notion database, click "Share" <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>.
2.  Click "Publish" <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>.
3.  Confirm by clicking "Publish" again <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>.
    *   This makes the database live and accessible to the PDF Output tool, enabling it to fetch pages within the database <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>.

## [[using_api_keys_to_connect_databases_for_pdf_generation | Generating PDFs with PDF Output]]

Once the Notion database URL and API key are entered into PDF Output, and the database is connected and published:
1.  Click "Load Database" in PDF Output <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.
2.  **Configure PDF Naming and Row Selection:**
    *   Select the Notion column to be used as a reference for naming the PDF files (e.g., "Full Name") <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.
    *   Choose which rows to generate PDFs for: all rows, a specific range, or custom rows <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.
3.  Click "Generate PDF" <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.
    *   The tool will then process each selected row. The placeholder elements in your template will be automatically populated with the corresponding data from each Notion row <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>.
    *   On the right side of the PDF Output interface, you can adjust settings such as paper size and layout <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>.
    *   Save each generated PDF file to your desired location <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>. The files will be named according to the selected naming column <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>.

## [[different_methods_for_pdf_generation_with_notion | Alternative Method: Using a Standalone Template Page]]

Another approach for [[using_notion_as_a_database_for_pdf_generation | generating PDF documents from Notion]] is to use a standalone template page URL directly in PDF Output, rather than embedding the template within each database row <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>.
1.  Copy the URL of your main template page (the one containing the curly bracket placeholders) <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>.
2.  Paste this template URL into the "Notion Page" field in PDF Output <a class="yt-timestamp" data-t="00:10:44">[00:10:44]</a>.
3.  Click "Load Page" to display the template <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>.
4.  Then, proceed by entering your Notion database URL and API key, and click "Load Database" as in the primary method <a class="yt-timestamp" data-t="00:10:56">[00:10:56]</a>.
    *   This method means you don't need to copy the template into each row of your database; the external tool uses the standalone template page to populate data from your database <a class="yt-timestamp" data-t="00:11:16">[00:11:16]</a>.

This process can be applied to any form of document, such as creating invoices from an invoices database, or generating notes and other documentation <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>. It's not mandatory for the placeholder elements to perfectly match content in the page; any information within the Notion page content can be read and generated into documents <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>.