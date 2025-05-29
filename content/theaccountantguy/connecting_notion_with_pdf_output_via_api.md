---
title: Connecting Notion with PDF Output via API
videoId: Uh1g7uXtr_4
---

From: [[theaccountantguy]] <br/> 

This article outlines how to [[generating_pdf_documents_with_notion | generate PDF documents]] for each row in a Notion database using the [[using_pdfoutput_tool_for_notion | PDF Output]] tool, by connecting Notion via its API <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. This process allows for bulk document creation without manual entry and individual exports <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.

## Prerequisites: Notion Database and Template Setup

To begin, you need a Notion database and a corresponding template page <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.

### Designing the Application Form Template
An application form database is used as an example, tracking details like candidate profiles and education requirements <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>. A matching template is created where data fields from the database are represented by placeholders enclosed in curly brackets (e.g., `{Full Name}`, `{Date of Birth}`) <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. These curly bracket fields must exactly match the column names in your Notion database <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

### Integrating the Template into Database Rows
Initially, you can manually copy and paste the template content into each database row's page <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.

For automated template insertion:
1.  Click the drop-down menu next to the "New" button in your Notion database <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.
2.  Select "New template" <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>.
3.  Name the template (e.g., "Applicant Name") <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.
4.  Paste the template content (with curly brackets) into this new template page <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.
5.  Click outside the template editor to save <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.
6.  Click the three dots next to your newly created template in the dropdown <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.
7.  Select "Set as default" and choose "For all views" for your specific database <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
Once set, any new row added to the database will automatically include this template <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.

## Connecting Notion to PDF Output

The [[using_pdfoutput_tool_for_notion | PDF Output]] tool is used to [[generating_pdf_documents_from_a_notion_database | generate PDF documents]] in bulk from a Notion database <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.

### Steps for API Connection

To connect your Notion database to [[using_pdfoutput_tool_for_notion | PDF Output]], follow these steps:

1.  **Copy the Notion Database URL**: From your Notion database, copy the URL from your browser's address bar <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>. Paste this URL into the designated field in the [[using_pdfoutput_tool_for_notion | PDF Output]] tool <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.

2.  **Generate a Notion API Key**:
    *   The database must be connected to [[using_pdfoutput_tool_for_notion | PDF Output]] via an API key, which is confidential <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.
    *   In Notion, go to "Settings & members" -> "Integrations" -> "Develop your own integrations" <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>.
    *   Click "New integration," add a name, choose your workspace, and save <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.
    *   Locate your new integration, click on it, and copy the "Internal Integration Secret" key <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>.
    *   Paste this key into the [[using_pdfoutput_tool_for_notion | PDF Output]] tool <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.

3.  **Connect Database to API Key**:
    *   In your Notion database, click the three dots in the top right corner <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>.
    *   Select "Add connections" <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>.
    *   Search for and select the name of the integration (API key) you just created <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>.
    *   Confirm the connection <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>.

4.  **Publish the Notion Database**:
    *   For [[using_pdfoutput_tool_for_notion | PDF Output]] to fetch pages, the database must be publicly accessible <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>.
    *   In your Notion database, click "Share" -> "Publish" -> "Publish" <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.
    *   This step is crucial for [[notion_database_integration_with_pdf_generation | PDF generation]] to work <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>.

## [[generating_pdf_documents_with_notion | Generating PDF Documents]]

Once Notion is properly connected to [[using_pdfoutput_tool_for_notion | PDF Output]]:

1.  **Load Database**: In [[using_pdfoutput_tool_for_notion | PDF Output]], click "Load Database" <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.
2.  **Select Naming Reference**: Choose a column from your database (e.g., "Full Name") to use for naming the generated PDF files <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.
3.  **Choose Rows**: Select whether to [[process_of_exporting_pdfs_from_notion | generate PDFs]] for all rows, a specific range, or custom selected rows <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.
4.  **Generate PDF**: Click "Generate PDF" <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.

<div class="callout callout-info">
<div class="callout-title">
Info
</div>
The tool will display each generated PDF, allowing you to verify that the data from the Notion row has correctly populated the template placeholders <a class="yt-timestamp" data-t="00:06:35">[00:06:35]</a>. You can adjust paper size and layout settings as needed <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>.
</div>

The generated files will be named according to your selected reference column (e.g., "Carol Davis.pdf") and will contain all the relevant data from the corresponding Notion database row <a class="yt-timestamp" data-t="00:07:59">[00:07:59]</a>.

## Flexible Template Usage

While the demonstration uses a template with matching placeholder elements, [[using_pdfoutput_tool_for_notion | PDF Output]] can also [[using_notion_with_pdf_output | generate documents]] from any Notion page content <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>. It's not mandatory for placeholder text elements to match page content; the tool reads the entire page content to [[creating_pdf_documents_from_notion_database | generate the documents]] <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>. This allows [[using_notion_as_a_template_and_database_for_pdfs | Notion to be used as a template and database for PDFs]] for notes, lectures, or any general documentation <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.

## Alternative Connection Method

Instead of ensuring each database row has the template embedded, you can directly use the main template page's URL <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>.
1.  Copy the URL of your dedicated template Notion page <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>.
2.  Paste this URL into the "Notion Page" section of [[using_pdfoutput_tool_for_notion | PDF Output]] <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>.
3.  Click "Load page" to load the template <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>.
4.  Then, proceed to load your Notion database URL as described above, and [[connecting_notion_database_and_template_for_pdfs | generate the PDFs]] <a class="yt-timestamp" data-t="00:10:55">[00:10:55]</a>.

This method allows you to have a database without embedded templates, referencing an external template page instead <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>.