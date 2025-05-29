---
title: How to integrate Notion with PDF generation tools
videoId: 5lnQYIpvjnM
---

From: [[theaccountantguy]] <br/> 

This article outlines a process for [[integrating_notion_database_with_pdf_output | integrating Notion databases]] with a PDF generation tool to create professional documents, such as invoices, in bulk <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. The method leverages a Notion page as a template and a Notion database to supply variable information, allowing for [[generating_pdf_documents_in_bulk_with_notion | bulk PDF document generation]] <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>. The specific tool demonstrated is pdf4put.com <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.

## Preparing Your Notion Template and Database

To begin [[pdf_document_creation_with_notion_and_pdf_output | PDF document creation with Notion and PDF output]], you need a Notion page designed as your document template and a Notion database containing the data for each document.

### Notion Template Setup
Your Notion page should function as the main template for your PDF documents <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.
*   **Placeholders**: Information that will change for each document (e.g., client name, invoice number, address) must be enclosed in curly brackets `{}` <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. For example, `{client name}` or `{invoice number}` <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>. These placeholders will be replaced by data from your database <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>.

### Notion Database Setup
Your Notion database will hold the specific data for each PDF <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.
*   **Column Names**: Ensure the column names in your database precisely match the placeholders used in your Notion page template (without the curly brackets) <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>. For instance, if your template has `{client name}`, you should have a database column named `client name` <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.
*   **Data Entry**: Populate the database with all the necessary information for each record you wish to convert into a PDF <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>.
*   **Relational Properties**: If your database uses relational properties that link to other Notion databases, ensure those related databases are also connected to the same Notion API key you will use for integration <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>.

## Integrating with PDFoutput.com
The following steps detail how to use pdf4put.com for [[generating_pdf_documents_using_notion | generating PDF documents using Notion]].

### 1. Sign In
*   Go to pdf4put.com <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.
*   Click on "Sign In" and choose your desired account <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.

### 2. Provide Notion Page URL
*   In Notion, open your template page.
*   Click "Share" -> "Publish" -> "Publish" again to make the page public <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.
*   Copy the public link to the Notion page <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.
*   Paste this link into the "Notion Page URL" field on pdf4put.com <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.
*   Click "Load Page" to preview the document <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>.

### 3. Generate Notion API Key and Connect Database
An API key connects your Notion database to the PDF generation tool <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.
*   On pdf4put.com, click the link to add a Notion API key <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>. This will open Notion's integration settings.
*   Click "New Integration" <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.
*   Give it a name (e.g., "new key") and choose your Notion account <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.
*   Click "Save" <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.
*   Copy the newly generated "Internal Integration Token" <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.
*   Paste this key back into the "Notion API Key" field on pdf4put.com <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>.

Next, you need to connect your Notion database to this API key <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.
*   Go back to your Notion database.
*   Click the three dots in the top right corner <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.
*   Go to "Connections" and search for the API key you just created (e.g., "new key") <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.
*   Select the key and click "Confirm" <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>. Your database is now connected <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.

### 4. Provide Notion Database URL
*   Copy the URL of your Notion database from the browser's address bar <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>.
*   Paste this URL into the "Notion Database URL" field on pdf4put.com <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.
*   Click "Load Database" <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>.

### 5. Configure PDF Generation
*   **File Naming**: Choose a database column to use for naming the generated PDF files (e.g., "Invoice Number") <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>.
*   **Rows for Generation**:
    *   "All Rows": Generates a PDF for every record in the database <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.
    *   "Custom Rows": Allows you to specify a range (e.g., 4th through 7th row) <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.
    *   "Custom Rows (Specific)": Generate for specific, non-contiguous rows <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>.

### 6. Generate and Save PDFs
*   Click "Generate PDF" <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.
*   The tool will process each record, populating the template with data <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>.
*   As each PDF is generated, you can adjust layout settings like paper size (e.g., A4, Letter), orientation (portrait or landscape), and pages to include (all or specific) <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.
*   Click "Save" for each document, choosing your desired save location <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>. The files will be named according to your chosen naming column <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>.

## Verification and Important Reminders
After [[generating_pdf_invoices_from_notion | generating PDF invoices from Notion]] or other documents, verify that the information in the PDFs matches the database records accurately <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.

*   **Page Sharing**: Ensure your Notion template page is explicitly shared and made public <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>.
*   **Database Connection**: Confirm that the Notion database is properly connected to the API key you created <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.
*   **Relational Databases**: If using relation properties, ensure all related databases are also connected to the *same* API key <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>. This is crucial for [[setting_up_and_managing_notion_databases_for_pdf_generation | setting up and managing Notion databases for PDF generation]] that rely on interconnected data.

For [[troubleshooting_and_support_for_pdf_generation_with_notion | troubleshooting and support]], you can reach out via email at notionformyuse@gmail.com or use the contact window on the pdf4put.com website <a class="yt-timestamp" data-t="00:08:23">[00:08:23]</a>. This process facilitates [[using_notion_for_generating_pdf_documents | using Notion for generating PDF documents]] efficiently.