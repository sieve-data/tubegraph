---
title: Using API keys for database and PDF tool connections
videoId: 5lnQYIpvjnM
---

From: [[theaccountantguy]] <br/> 

This article outlines the process of generating multiple PDF documents from a Notion template and database using API keys, specifically with the tool PDF4PUT.com <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>. This method allows for bulk PDF creation by dynamically replacing placeholder information in a template with data from a Notion database <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

## Overview of the Process

The core idea is to leverage a professional template set up in Notion, combined with a database containing varying record information <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. For each record in the database, a unique PDF document will be generated <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>. The values in the Notion template that need to be replaced are identified by being placed inside curly brackets (e.g., `{Client Name}`) <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.

## Pre-requisites in Notion

Before using the PDF generation tool, certain preparations are needed in Notion:

### 1. Create a Notion Template

*   Design a professional template (e.g., an invoice document) in a Notion page <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>.
*   Insert placeholders within curly brackets `{}` for all the information you intend to replace with data from your database <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. These placeholders must exactly match the column names in your Notion database <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>.

### 2. Set Up a Notion Database

*   Create a database in Notion containing all the records and corresponding data that will populate the PDF documents <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.
*   Ensure the column names in the database match the placeholders (text within curly brackets) in your Notion template <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>.

### 3. Make the Notion Page Public

*   For the PDF generation tool to access your template, the Notion page hosting the template must be made public <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.
*   To do this, click "Share" on your Notion page, then "Publish", and confirm "Publish to web" <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.
*   Copy the generated public link <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.

### 4. [[setting_up_api_keys_in_notion | Setting up API keys in Notion]] and [[steps_to_integrate_databases_with_api_keys_in_notion | Connecting Databases]]

*   An API key is essential to [[connecting_notion_database_to_pdf_output_via_api_keys | connect your Notion database with the PDF output tool]] <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.
*   Create a new integration in Notion (e.g., naming it "new key") and save it <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.
*   Copy the generated internal integration token (API key) <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.
*   To link your database to the API key, go to the database in Notion, click the three dots (`...`) on the top right, select "Add connections", and search for the integration you just created (e.g., "new key") <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>. Confirm the connection <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>.
*   If your database uses [[connecting_notion_database_to_pdf_output_via_api_keys | relational properties]], ensure all related databases are also connected to the same API key <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>.

## [[setting_up_and_connecting_notion_database_for_pdf_creation | Setting up and Connecting Notion Database for PDF Creation]] (on PDF4PUT.com)

1.  **Login**: Access PDF4PUT.com and sign in <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.
2.  **Paste Notion Page URL**: Paste the previously copied public Notion page URL into the designated field on PDF4PUT.com <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>. Click "Load Page" to preview the document <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>.
3.  **Paste Notion API Key**: Paste the copied Notion API key into its respective field <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.
4.  **Paste Notion Database URL**: Copy the URL of your Notion database (from the browser's address bar) <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a> and paste it into the PDF4PUT.com field <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.
5.  **Load Database**: Click "Load Database" to allow the tool to fetch your database structure <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>.
6.  **Select File Naming Column**: Choose a column from your database (e.g., "Invoice Number") that will be used to name the generated PDF files <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>.
7.  **Select Rows for Generation**: You can choose to generate PDFs for all rows, specific rows by range (e.g., 4th through 7th), or custom individual rows <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.

## [[exporting_pdf_documents_using_a_database | Generating and Exporting PDF Documents]]

Once all settings are configured, click "Generate PDF" <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>. The tool will then iterate through your database records, populate the Notion template with the corresponding data, and generate each PDF <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>.

### Layout Settings

During the generation process, you can adjust various layout settings:
*   **Paper Size**: Select from various paper sizes (e.g., A4, Letter) <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>.
*   **Orientation**: Choose between portrait or landscape mode <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>.
*   **Pages**: Specify whether to print all pages of the Notion document or a selected range <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>.

After each PDF is generated, you will be prompted to save it to your desired location, with the file name automatically set according to your chosen column (e.g., invoice number) <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>.

## Important Reminders

*   Ensure your Notion template page is publicly shared <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>.
*   Confirm that your Notion database is connected to the API key you created <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>.
*   If using relational properties in your database, the related databases must also be connected to the *same* API key for seamless operation <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>.

This detailed process allows for efficient bulk PDF generation from Notion databases, making it ideal for tasks like creating multiple invoices, reports, or personalized documents.