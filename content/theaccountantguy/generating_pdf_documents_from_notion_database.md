---
title: Generating PDF documents from Notion database
videoId: 5lnQYIpvjnM
---

From: [[theaccountantguy]] <br/> 

This article details the process of [[generating_pdf_invoices_from_notion_database | generating PDF invoices from a Notion database]] using a professional invoice template and PDFOutput.com, facilitating [[bulk_pdf_document_generation_using_notion | bulk PDF document generation using Notion]]. <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>

## Overview
The process involves using a Notion page as a template, populating it with data from a Notion database, and then using PDFOutput.com to convert each database record into a separate PDF document. <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a> The template contains placeholders (fields in curly brackets) that are replaced by information from the database records. <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>

## Preparing Notion for PDF Generation

### Invoice Template Setup
A Notion page serves as the professional invoice template. <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a> This template should include all necessary invoice information. <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a> Crucially, dynamic information that will be pulled from the database must be placed inside curly brackets (e.g., `{Client Name}`, `{Client Company}`, `{Client Address}`). <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a> These fields will be replaced by the data from the database. <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>

### Notion Database Setup
A Notion database holds the invoice-related information for each record. <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a> Each column in the database should correspond to a placeholder (field in curly brackets) in the template. <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a> This ensures that the correct data is fetched for replacement. <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a> For example, if your template has `{Client Name}`, your database needs a column named "Client Name".

### Sharing the Notion Page
The Notion template page must be made public and accessible for PDFOutput.com to use it. <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>
1.  Go to the invoice template Notion page. <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>
2.  Click "Share". <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>
3.  Click "Publish". <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>
4.  Confirm "Publish". <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>
5.  Copy the public link. <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>

### Connecting the Notion Database to an API Key
To allow PDFOutput.com to access your Notion database, you need to connect the database to an API key. <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>
1.  Navigate to your database in Notion. <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>
2.  Click the three dots `...` on the top right of the database. <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>
3.  Click "Connections". <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>
4.  Search for the API key you will use (e.g., "new key"). <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>
5.  Select the API key and click "Confirm". <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>
6.  Copy the database URL from the browser's address bar. <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>

> [!important] Relational Properties
> If your Notion database uses [[setting_up_notion_databases_for_pdf_generation | relational properties]] connected to other databases, all related databases must also be connected to the *same* API key. <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>

## [[generating_pdf_documents_in_bulk_using_notion_and_pdf_output | Generating PDF Documents in Bulk using Notion and PDF Output]]

### Using PDFOutput.com
1.  Go to pdf4put.com. <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>
2.  Click "Sign in" and log in with your chosen account. <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>
3.  **Provide Notion Page URL:** Paste the public Notion page URL into the designated field and click "Load Page". <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a> The template document will appear on the right side. <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>
4.  **Add Notion API Key:**
    *   Click the link "click here to add notion API key". <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>
    *   Click "New integration". <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>
    *   Give it a name (e.g., "new key"), choose your account, and click "Save". <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>
    *   Go to "Integrations", click the key name, click "Show", and copy the API key. <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>
    *   Paste the API key into PDFOutput.com. <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>
5.  **Fetch Database URL:** Paste the copied Notion database URL into the designated field. <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>
6.  **Load Database:** Click "Load Database". <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>
7.  **Select Naming Column:** Choose a column from your database to name the generated PDF files (e.g., "Invoice Number"). <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>
8.  **Choose Rows:** You can select to generate PDFs for "All rows" or specify "Custom rows" (e.g., rows 4-7) or even a "Custom row" for a single document. <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>
9.  **Generate PDF:** Click "Generate PDF". <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>
    *   PDFOutput.com will start processing each record, populating the template with data from your database. <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>
    *   You can adjust layout settings like paper size (e.g., A4), orientation (portrait/landscape), and pages to print. <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>
    *   Click "Save" for each generated PDF. The files will be named according to your chosen naming column (e.g., "Invoice number 3.pdf"). <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>

## [[exporting_and_previewing_pdf_documents_generated_in_notion | Exporting and previewing PDF documents generated in Notion]]

After generation, the PDFs are saved to your chosen location. <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a> You can then open and review each document to ensure all data has been accurately fetched and replaced from the Notion database. <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a> The generated PDFs should perfectly mirror the data in your Notion database rows. <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>

## Important Reminders

*   The Notion page [[using_notion_templates_for_pdf_generation | used as a template]] must be publicly shared. <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>
*   The Notion database must be connected to the API key you created. <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>
*   Any fields in the Notion template that need to be dynamically replaced must be enclosed in curly brackets (e.g., `{Field Name}`) and correspond to a column in your Notion database. <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>
*   If using relational properties in your database, ensure all linked databases are connected to the same API key. <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>

For any queries or assistance, you can reach out via notionformyuse@gmail.com or use the contact window on the PDFOutput website. <a class="yt-timestamp" data-t="00:08:23">[00:08:23]</a>