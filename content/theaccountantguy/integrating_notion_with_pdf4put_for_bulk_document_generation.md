---
title: Integrating Notion with PDF4put for bulk document generation
videoId: 5lnQYIpvjnM
---

From: [[theaccountantguy]] <br/> 

This article outlines the process of [[generating_pdf_documents_in_bulk_using_notion_and_pdfoutput | generating PDF documents in bulk]] from a Notion database using a Notion template and the PDF4put service <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>, <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. Specifically, it demonstrates how to generate multiple PDF invoices from a Notion database <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>, <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>.

## Preparing the Notion Template

The first step is to create a professional invoice template within a Notion page <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>.
This template should include all necessary invoice information <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>.

Key information that needs to be replaced from the database should be placed inside curly brackets, for example, `{Client Name}`, `{Client Company}`, `{Client Address}` <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>, <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>. These bracketed fields will be automatically populated from your Notion database during the PDF generation process <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>.

## Setting up PDF4put Integration

To [[connecting_and_setting_up_pdf_output_with_notion | connect and set up PDFOutput with Notion]], follow these steps:

### 1. Make Notion Page Public

Share your Notion invoice template page by clicking "Share," then "Publish," and again "Publish" to make the page public <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>, <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>. Copy the public link to this page <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.

### 2. Log in to PDF4put

Go to `pdf4put.com` and sign in using your desired account <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>, <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.

### 3. Add Notion Page URL to PDF4put

Paste the copied Notion page URL into the designated field on PDF4put <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>. Click "Load Page" to display the document on the right side of the interface <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>. You can view the full document or its input source <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>.

### 4. Create and Connect Notion API Key

An API key is required to connect your Notion database with PDF4put <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>.
*   Click the "click here to add Notion API key" link <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.
*   In the Notion integration window, click "New Integration," provide a name (e.g., "New Key"), choose your account, and save <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.
*   Copy the generated API key from the "Integrations" section <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>.
*   Paste this API key into the PDF4put interface <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.

### 5. Connect Notion Database to API Key and PDF4put

Your Notion database must be connected to the API key you just created <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.
*   In your Notion database, click the three dots on the top right <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.
*   Select "Connections" and search for the API key you created (e.g., "New Key") <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.
*   Select the key and click "Confirm" to connect the database <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>.
*   Copy the URL of your Notion database from the browser's address bar <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>.
*   Paste the database URL into the corresponding field in PDF4put <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.

## Generating PDF Documents

With the Notion page URL, API key, and database URL set up, you can now generate your PDFs <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.

### 1. Load Database

Click "Load Database" on PDF4put <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>.

### 2. Configure Output Options

*   **File Naming**: Choose a column from your database (e.g., "Invoice Number") to use as the file name for the generated PDFs <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.
*   **Row Selection**: Decide which rows from your database to use:
    *   **All Rows**: Generate a PDF for every record <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.
    *   **Custom Range**: Specify a range of rows (e.g., 4th through 7th) <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.
    *   **Specific Row**: Generate a PDF for a single, specific row <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>.
*   **Layout Settings**: Adjust paper size (e.g., A4, Letter), orientation (portrait or landscape), and select which pages to print if your template has multiple pages <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.

### 3. Generate and Save PDFs

Click "Generate PDF" <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>. PDF4put will start populating the invoices one by one, replacing the curly-bracketed fields with data from your database <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>. Each generated PDF will be named according to your chosen column (e.g., "Invoice Number 3") <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>. Save each document to your desired location <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>.

## Key Reminders for Seamless Operation

*   **Notion Page Sharing**: Ensure your Notion page is publicly shared and accessible <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>.
*   **Database Connection**: Confirm that your Notion database is connected to the correct API key you created <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>.
*   **Relational Properties**: If your database uses relation properties connecting to other databases, ensure that *all* related databases are also connected to the *same* API key. This ensures all relevant data is fetched <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>.

For any queries or assistance, you can reach out via email at `notionformyuse@gmail.com` or use the contact window available on the PDF4put website <a class="yt-timestamp" data-t="00:08:23">[00:08:23]</a>.