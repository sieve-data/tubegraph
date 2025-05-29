---
title: Creating a professional invoice template in Notion
videoId: 5lnQYIpvjnM
---

From: [[theaccountantguy]] <br/> 

This article explains how to set up a professional invoice template within Notion and use it to [[generating_pdf_invoices_in_bulk_using_a_notion_database | generate PDF invoices in bulk]] from a Notion database <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.

## Template Overview
A [[creating_professional_invoice_templates | professional invoice template]] in Notion can include all necessary invoice information <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. The template is designed to have certain pieces of information enclosed in curly brackets (e.g., `{client name}`, `{invoice number}`), which act as placeholders <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. These placeholders will be dynamically replaced with data from a Notion database <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>.

## Tools Required
To [[generating_invoices_from_a_notion_database | generate PDF documents]] from your Notion invoice template using data from a database, you will use `pdf4notion.com` <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>. This tool facilitates the bulk PDF generation process <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.

## Step-by-Step Setup

### 1. Prepare Your Notion Invoice Template
Ensure your Notion page contains the desired invoice layout <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. All fields intended to be populated from your database should be enclosed in curly brackets (e.g., `{client name}`, `{client company}`, `{client address}`) <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. These curly-bracketed fields must correspond to column names in your Notion database <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.

### 2. Prepare Your Notion Database
Create a Notion database with records containing invoice-related information <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>. Each column in the database should correspond to a field in your invoice template <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.

### 3. Share Your Notion Page
To allow `pdf4notion.com` to access your template:
1.  Go to your Notion invoice template page <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>.
2.  Click on "Share" <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.
3.  Click on "Publish" <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.
4.  Confirm "Publish" again to make the page public <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.
5.  Copy the page link <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.

### 4. Connect Notion to `pdf4notion.com`
1.  Go to `pdf4notion.com` and sign in <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.
2.  Paste the copied Notion page URL into the designated field on `pdf4notion.com` <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.
3.  Click "Load Page" to preview your template <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>.

### 5. Create a Notion API Key
An API key is essential to connect your Notion database with `pdf4notion.com` <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.
1.  On `pdf4notion.com`, click the link to add a Notion API key <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.
2.  This will open a Notion integration window; click "New integration" <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.
3.  Give it a name (e.g., "new key") and choose your account <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.
4.  Click "Save" <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.
5.  Copy the generated API key <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.
6.  Paste the API key into the designated field on `pdf4notion.com` <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>.

### 6. Connect Your Notion Database
1.  In your Notion database, click the three dots on the top right <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.
2.  Go to "Connections" <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.
3.  Search for and select the API key you just created (e.g., "new key") <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.
4.  Click "Confirm" <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>. This connects the database to the API key <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.
5.  Copy the URL of your Notion database <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>.
6.  Paste this database URL into the field on `pdf4notion.com` <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.
7.  Click "Load Database" <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>.

### 7. Configure and Generate PDFs
1.  Choose a column from your database to name the generated PDF files (e.g., "Invoice Number") <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>.
2.  Select which rows to process (e.g., "All rows", "Custom rows", or "Specific row") <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.
3.  Click "Generate PDF" <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>. `pdf4notion.com` will begin populating the invoices <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>.
4.  You can adjust layout settings such as paper size (e.g., A4), orientation (portrait/landscape), and page range (all pages) <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>.
5.  Save each generated PDF document to your desired location <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>. The files will be saved using the chosen naming column (e.g., "Invoice Number 1", "Invoice Number 2") <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>.

## Important Reminders

*   **Page Sharing**: Your Notion template page must be publicly shared and accessible <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.
*   **Database Connection**: The Notion database must be connected to the API key you created <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.
*   **Template Fields**: Ensure all dynamic fields in your template are enclosed in curly brackets and match column names in your database <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>.
*   **Relational Properties**: If your database uses [[setting_up_notion_for_invoice_management | relation properties]] (linking to other Notion databases), those relational databases must also be connected with the same API key <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>. All linked databases must have the correct API key connection for seamless operation <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.

For further assistance, you can reach out via email to `notionformyuse@gmail.com` <a class="yt-timestamp" data-t="00:08:25">[00:08:25]</a>.