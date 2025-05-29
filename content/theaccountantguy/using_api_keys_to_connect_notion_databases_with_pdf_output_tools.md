---
title: Using API keys to connect Notion databases with PDF output tools
videoId: 5lnQYIpvjnM
---

From: [[theaccountantguy]] <br/> 

This article explains how to [[connecting_notion_database_and_templates_to_pdf_output | generate PDF documents from Notion templates and databases]] using API keys with a tool like pdf4put.com <a class="yt-timestamp" data-t="00:13:15">[00:13:15]</a>. This process allows for bulk PDF generation by replacing placeholder information in a Notion template with data from a Notion database <a class="yt-timestamp" data-t="00:34:04">[00:34:04]</a>.

## Preparing the Notion Invoice Template

A Notion page is used as a professional invoice template <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>.
To prepare the template for dynamic data insertion:
*   Place information intended for replacement from the database inside curly brackets (e.g., `{Client Name}`, `{Invoice Number}`) <a class="yt-timestamp" data-t="00:30:32">[00:30:32]</a>.
*   Ensure these fields correspond to column names in the Notion database <a class="yt-timestamp" data-t="04:15:08">[04:15:08]</a>.

## Setting Up the Notion Database

A Notion database holds the specific invoice-related information for each record <a class="yt-timestamp" data-t="00:18:31">[00:18:31]</a>. Each record in the database will be used to generate a separate PDF document <a class="yt-timestamp" data-t="00:23:09">[00:23:09]</a>. The column headers in this database should match the names used within the curly brackets in the Notion template <a class="yt-timestamp" data-t="04:15:08">[04:15:08]</a>.

## Using PDF Output Tools (e.g., pdf4put.com)

A third-party service like pdf4put.com can be used to connect Notion and generate PDFs <a class="yt-timestamp" data-t="00:49:10">[00:49:10]</a>.

### Initial Setup and Authentication
1.  **Sign In**: Log in to pdf4put.com using a chosen account <a class="yt-timestamp" data-t="00:57:04">[00:57:04]</a>.
2.  **Make Notion Page Public**: Share the Notion template page to the web to make it publicly accessible <a class="yt-timestamp" data-t="01:21:24">[01:21:24]</a>.
3.  **Copy Notion Page URL**: Obtain the public URL of the Notion template page <a class="yt-timestamp" data-t="01:31:33">[01:31:33]</a>.
4.  **Input Page URL**: Paste the copied Notion page URL into the designated field on the PDF output tool <a class="yt-timestamp" data-t="01:40:41">[01:40:41]</a>. After loading the page, the template's content should be visible <a class="yt-timestamp" data-t="01:44:06">[01:44:06]</a>.

### [[Setting up Notion API keys for PDF generation | API Key and Database Connection]]
1.  **Generate Notion API Key**:
    *   Access Notion's integration settings (often via a link provided by the PDF tool) <a class="yt-timestamp" data-t="02:10:04">[02:10:04]</a>.
    *   Create a new integration, provide a name (e.g., "new key"), and choose the relevant Notion account <a class="yt-timestamp" data-t="02:17:28">[02:17:28]</a>.
    *   Save the integration, then reveal and copy the generated internal API token <a class="yt-timestamp" data-t="02:27:54">[02:27:54]</a>.
2.  **Input API Key**: Paste the copied Notion API key into the PDF output tool <a class="yt-timestamp" data-t="02:39:13">[02:39:13]</a>.
3.  **[[Connecting Notion databases with API Keys for data management | Connect Notion Database to API Key]]**:
    *   Go to the Notion database to be used <a class="yt-timestamp" data-t="02:47:04">[02:47:04]</a>.
    *   Click the three dots menu on the top right of the database <a class="yt-timestamp" data-t="02:51:24">[02:51:24]</a>.
    *   Select "Connections" and search for the API key created earlier (e.g., "new key") <a class="yt-timestamp" data-t="02:53:25">[02:53:25]</a>.
    *   Confirm the connection to link the database with the API key <a class="yt-timestamp" data-t="03:16:00">[03:16:00]</a>.
    *   If the database uses "relation properties" to other databases, those related databases must also be connected to the *same* API key <a class="yt-timestamp" data-t="07:51:28">[07:51:28]</a>.
4.  **Copy Notion Database URL**: Copy the URL of the Notion database from the browser's address bar <a class="yt-timestamp" data-t="03:24:25">[03:24:25]</a>.
5.  **Input Database URL**: Paste the database URL into the PDF output tool <a class="yt-timestamp" data-t="03:30:20">[03:30:20]</a>.

### [[Connecting and setting up PDF output with Notion | Configuring PDF Output]]
1.  **Load Database**: Click "Load database" within the PDF output tool to pull in the database information <a class="yt-timestamp" data-t="03:53:07">[03:53:07]</a>.
2.  **File Naming**: Choose a column from the database (e.g., "Invoice Number") to use for naming the generated PDF files <a class="yt-timestamp" data-t="03:57:38">[03:57:38]</a>.
3.  **Row Selection**: Decide whether to generate PDFs for all rows in the database, a custom range of rows, or specific individual rows <a class="yt-timestamp" data-t="04:54:06">[04:54:06]</a>.
4.  **Layout Settings**: Adjust PDF layout options such as paper size (e.g., A4), orientation (portrait or landscape), and pages to be printed (e.g., all pages) <a class="yt-timestamp" data-t="05:40:41">[05:40:41]</a>.

### Generating and Saving PDFs
1.  **Generate PDF**: Click the "Generate PDF" button <a class="yt-timestamp" data-t="05:12:01">[05:12:01]</a>. The tool will begin populating the template with data from the first record <a class="yt-timestamp" data-t="05:15:35">[05:15:35]</a>.
2.  **Save Document**: Save each generated PDF file to your desired location, noting that it will be named according to the chosen database column <a class="yt-timestamp" data-t="06:01:05">[06:01:05]</a>. The tool will then proceed to generate the next document until all selected rows are processed <a class="yt-timestamp" data-t="06:12:00">[06:12:00]</a>.

### Key Reminders
*   The Notion template page must be publicly shared <a class="yt-timestamp" data-t="07:35:08">[07:35:08]</a>.
*   The Notion database must be explicitly connected to the API key being used <a class="yt-timestamp" data-t="07:39:24">[07:39:24]</a>.
*   Any relational databases linked within the main database must also be connected to the *same* API key <a class="yt-timestamp" data-t="07:51:28">[07:51:28]</a>.

For queries or assistance, contact notionformyuse@gmail.com or use the contact window on the platform <a class="yt-timestamp" data-t="08:25:27">[08:25:27]</a>.