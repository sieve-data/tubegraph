---
title: Exporting Notion Data to PDF
videoId: Uh1g7uXtr_4
---

From: [[theaccountantguy]] <br/> 

This article explains how to [[Generating PDF documents from Notion using PDFOutput | generate PDF documents]] for each row in a Notion database, using a tool called [[Using PDF Output Tool with Notion | PDF Output]]. The process allows for the creation of multiple PDFs without manually entering information or exporting documents one by one <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.

## Preparing Your Notion Database

To begin, you need a Notion database, such as an application form database tracking candidate profiles and educational requirements <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>.

### Creating a Template Page
An application form template should be created that matches the database structure <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.
Key fields from the database, like "Full Name", "Date of Birth", "Gender", and "Phone Number", should be placed inside curly brackets `{}` in the template <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. These curly-bracketed fields correspond exactly to the column names in your Notion database <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

### Populating Database Rows with the Template
For each row of data in your Notion database, open the row and paste the content of your prepared template into the empty page section at the bottom <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.

### Automating Template Population (Optional, but Recommended)
To avoid manually copying and pasting the template for new rows, you can set it as a default:
1.  Click the drop-down arrow next to the "New" button in your database <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.
2.  Select "New template" <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>.
3.  Give the template a name (e.g., "Applicant Name") <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.
4.  Paste the template content into this new template page <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.
5.  Click the three dots next to the template name, choose "Set as default", and then "For all views in [database name]" <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.
Now, whenever a new row is added, the template will automatically populate the page <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.

## Integrating Notion with [[PDF Output Tool with Notion | PDF Output]]

[[Integrating Notion with PDF Output for document creation | PDF Output]] is a tool designed to [[Bulk Generating PDF Documents from Notion Database | generate documents in bulk]] from a Notion database <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>.

### Connecting Notion Database to PDF Output
1.  **Sign In**: Access your [[Using PDF Output Tool with Notion | PDF Output]] dashboard <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.
2.  **Copy Database URL**: Copy the URL of your Notion database from the browser's address bar <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.
3.  **Paste URL in PDF Output**: Paste the copied URL into the designated field in [[Using PDF Output Tool with Notion | PDF Output]] <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.
4.  **Generate API Key**: Your Notion database must be connected to [[Using PDF Output Tool with Notion | PDF Output]] via an API key <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.
    *   In Notion, go to "Settings & members" > "Integrations".
    *   Click "Develop your own integrations" if you haven't already.
    *   Click "New integration," add a name, choose your workspace, and save.
    *   Copy the "Internal Integration Secret" key <a class="yt-timestamp" data-t="00:04:58">[00:04:58]</a>.
5.  **Paste API Key in PDF Output**: Paste the copied API key into [[Using PDF Output Tool with Notion | PDF Output]] <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.
6.  **Connect Database to Integration**:
    *   In your Notion database, click the three dots (`...`) in the top right corner <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>.
    *   Select "Connections" and choose the integration name you created (e.g., "new key") <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>.
    *   Click "Confirm" <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>.
7.  **Publish Database**: The database must be published to be accessible by [[Using PDF Output Tool with Notion | PDF Output]]:
    *   Click "Share" on your Notion database <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>.
    *   Toggle "Publish to web" on <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>.
    *   Click "Publish" <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>. This step is crucial for [[Using PDF Output Tool with Notion | PDF Output]] to fetch pages from the database <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>.

## Generating PDF Documents

With the Notion database prepared and connected to [[Using PDF Output Tool with Notion | PDF Output]], you can now [[Generating PDFs in bulk with Notion | generate PDFs in bulk]].

1.  **Load Database**: In [[Using PDF Output Tool with Notion | PDF Output]], click "Load database" <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.
2.  **Select Naming Column**: Choose a column from your database (e.g., "Full Name") to be used for naming the generated PDF files <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.
3.  **Select Rows**: Decide whether to generate PDFs for "all rows," a specific "range of rows," or "custom rows" <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.
4.  **Generate PDF**: Click "Generate PDF" <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.
    *   [[Using PDF Output Tool with Notion | PDF Output]] will display a preview of each PDF, automatically populating the template's placeholder fields with data from the corresponding Notion row <a class="yt-timestamp" data-t="00:06:35">[00:06:35]</a>.
    *   On the right side, you can adjust settings like paper size and layout <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>.
    *   Click "Save" for each PDF to download them <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>. The files will be named according to the column you selected <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>.

### Alternative Method: Using a Direct Notion Page URL

Instead of having the template inside each Notion database row, you can directly use a Notion page URL as the template:
1.  Copy the URL of your main template page <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>.
2.  In [[Using PDF Output Tool with Notion | PDF Output]], paste this URL into the "Notion Page URL" field <a class="yt-timestamp" data-t="00:10:44">[00:10:44]</a>.
3.  Click "Load page" to load the document preview <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>.
4.  Then, follow the steps for loading the database, selecting the naming column, and [[Generating PDF documents from Notion using PDFOutput | generating the PDFs]] <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>.

This method allows you to use a separate template page with a Notion database that doesn't necessarily contain the template within its rows <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>.

## Use Cases and Flexibility

This method of [[creating_pdf_documents_with_notion_templates | creating PDF documents with Notion templates]] is applicable to various document generation needs, including:
*   [[Exporting and managing PDF files from Notion database | Application forms]] <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>
*   Invoices from an invoice database <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>
*   Any form of document for business or personal use <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>

It's not mandatory for placeholder elements to match exact database fields; [[Using PDF Output Tool with Notion | PDF Output]] can still read and [[exporting_pdf_documents_from_notion | export PDF documents from Notion]] pages containing general notes, lectures, or any other content <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>.

For additional resources and help, [[Using PDF Output Tool with Notion | PDF Output]] provides a contact section and a library of predefined templates that can be directly copied and used <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>.