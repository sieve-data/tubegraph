---
title: Using pdf4put for bulk PDF creation
videoId: 5lnQYIpvjnM
---

From: [[theaccountantguy]] <br/> 

This article demonstrates how to use the `pdf4put.com` tool to generate bulk PDF documents from a Notion template and database, specifically focusing on [[creating_bulk_invoice_pdfs|creating bulk invoice PDFs]] <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This process allows for [[automating_pdf_document_generation|automating PDF document generation]] by replacing dynamic information in a Notion page with data from a Notion database <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

## Overview of the Process

The method involves using a professional invoice template created in Notion and a Notion database containing invoice-related information <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. The goal is to generate a separate PDF document for each record in the database using the template <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>.

The core tool for this is `pdf4put.com` <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>, which enables [[bulk_export_of_pdf_documents_using_pdf_output|bulk export of PDF documents]] <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.

## Preparing Notion for PDF Generation

### Notion Template Setup
The Notion template must include placeholders for dynamic information, enclosed within curly brackets (e.g., `{Client Name}`, `{Invoice Number}`) <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>. These placeholders correspond to column names in the Notion database <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.

### Notion Page Sharing
To allow `pdf4put.com` to access the template, the Notion page needs to be made public <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.
1.  Open the Notion invoice template page <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>.
2.  Click on "Share" <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.
3.  Click on "Publish" twice to make the page public <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.
4.  Copy the public link of the page <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.

### Notion Database Setup and API Key Connection
The Notion database contains the specific data that will populate the PDF documents <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>.

1.  **Generate a Notion API Key**:
    *   Navigate to Notion integrations settings (a direct link is provided by pdf4put.com) <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.
    *   Click on "New Integration" <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.
    *   Provide a name for the integration (e.g., "new key") and choose the associated Notion account <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.
    *   Save the integration and copy the generated internal API key <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.
2.  **Connect Database to API Key**:
    *   Go back to the Notion database page <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.
    *   Click on the three dots in the top right corner <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.
    *   Select "Connections" <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.
    *   Search for the API key created earlier (e.g., "new key") and confirm the connection <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.
    *   Copy the URL of the Notion database <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>.

    > [!WARNING] Relational Properties
    > If the database uses any relation properties connected to other databases, ensure that *all* related databases are also connected to the same API key <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>.

## Using PDFoutput for Document Generation

To start [[setting_up_pdfoutput_for_document_generation|setting up PDFOutput for document generation]]:

1.  **Access PDF Output**: Go to `pdf4put.com` <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.
2.  **Sign In**: Click "Sign In" and choose your desired account <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.
3.  **Provide Notion Page URL**: Paste the public Notion page URL into the designated field on `pdf4put.com` <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>. Click "Load Page" to preview the document <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>.
4.  **Provide Notion API Key**: Paste the copied Notion API key into the API key field <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.
5.  **Provide Notion Database URL**: Paste the copied Notion database URL into the database URL field <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.
6.  **Load Database**: Click "Load Database" <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>.
7.  **Choose Naming Column**: Select a column from your database to be used for naming the generated PDF files (e.g., "Invoice Number") <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.
8.  **Set Rows (Optional)**: You can choose to generate PDFs for "All Rows," a "Custom Range" of rows, or "Custom Rows" for specific entries <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.
9.  **Generate PDF**: Click "Generate PDF" <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>. The tool will begin populating and presenting each invoice for saving <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>.
10. **Layout Settings**: Before saving each PDF, you can adjust layout settings such as paper size, orientation (portrait/landscape), and pages to be printed <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.
11. **Save Documents**: Save each generated PDF to your desired location <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>. The files will be saved with the names chosen from the selected database column <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>.

## Verification of Generated Documents

After the generation process, the PDFs can be opened and verified against the Notion database entries. For example, an invoice named "Invoice Number One" will correctly display information for "Alice Johnson" and the corresponding dates from the database row <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a>. This confirms the successful replacement of curly-bracketed fields with database values <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>.

## Support

For any queries or issues related to [[using_pdf_output_for_document_generation|using PDF output for document generation]], contact `notionformyuse@gmail.com` or use the contact window on the `pdf4put.com` website <a class="yt-timestamp" data-t="00:08:23">[00:08:23]</a>.