---
title: Generating PDF invoices in bulk using a Notion database
videoId: 5lnQYIpvjnM
---

From: [[theaccountantguy]] <br/> 

This article outlines how to generate professional PDF invoices in bulk by leveraging a Notion page template and a Notion database with the help of PDFOutput.com <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This method allows for the automated creation of multiple PDF documents, such as invoices or payment receipts, from structured data in Notion <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.

## Overview of the Process

The core idea is to use a Notion page as a template, where specific fields are marked with curly brackets (e.g., `{client name}`). These bracketed fields will be automatically populated with data from a Notion database <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. PDFOutput.com then processes this setup to [[creating_invoices_in_bulk_using_notion | create invoices in bulk using Notion]] <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.

## Required Components

1.  **Notion Invoice Template Page**: A Notion page designed as an invoice, containing all necessary information <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. Dynamic fields that will be populated from the database must be enclosed in curly brackets (e.g., `{client name}`, `{invoice number}`, `{due date}`) <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.
2.  **Notion Database**: A database containing the invoice-related information, with columns matching the names of the curly-bracketed fields in your template (e.g., "Client Name", "Invoice Number", "Due Date") <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>.
3.  **PDFOutput.com Account**: A tool to connect Notion to the PDF generation process <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.

## Step-by-Step Guide

### 1. Prepare Your Notion Assets

*   **Create Your Invoice Template Page**: Set up a Notion page as your invoice template. Populate it with static content and placeholders in curly brackets for dynamic data <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.
*   **Create Your Invoice Database**: Set up a Notion database with records for each invoice you want to generate. Ensure column names in this database match the placeholder names in your template (without the curly brackets) <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>.
*   **Make the Notion Page Public**: For PDFOutput to access your template, the Notion page must be shared publicly.
    *   Go to your Notion invoice template page <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>.
    *   Click "Share" -> "Publish" -> "Publish" <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.
    *   Copy the public link <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.
*   **Connect Database to API Key**:
    *   Go to your Notion database <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.
    *   Click the three dots in the top right corner <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.
    *   Click "Connections" <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.
    *   Search for the API key you will create in the next step (e.g., "new key") and confirm the connection <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.
    *   Copy the database URL from your browser's address bar <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>.

### 2. Configure PDFOutput.com

*   **Sign In**: Go to pdf4put.com and sign in with your account <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.
*   **Provide Notion Page URL**: Paste the public Notion page URL you copied earlier into the designated field in PDFOutput <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>. Click "Load Page" to preview the document <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>.
*   **Generate and Provide Notion API Key**: An API key is essential to connect PDFOutput to your Notion database <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>.
    *   In PDFOutput, click the link to add a Notion API key <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.
    *   In the Notion window that opens, click "New Integration" <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.
    *   Give it a name (e.g., "new key"), select your account, and click "Save" <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.
    *   Click "Integrations", then "Show" next to your new key, and copy the API key <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>.
    *   Paste the copied API key back into PDFOutput <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>.
*   **Provide Notion Database URL**: Paste the Notion database URL you copied earlier into PDFOutput <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.
*   **Load Database**: Click "Load Database" <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>.
*   **Select Naming Column**: Choose a column from your database (e.g., "Invoice Number") to use for naming the generated PDF files <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>.
*   **Choose Rows for Generation**:
    *   **All Rows**: Generate a PDF for every record in the database <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.
    *   **Custom Range**: Specify a range of rows (e.g., 4th through 7th) <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.
    *   **Custom Rows**: Select specific individual rows <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>.
*   **Generate PDFs**: Click "Generate PDF" <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>. PDFOutput will process each record, populating the template fields and prompting you to save each generated PDF <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.
*   **Layout Settings (Optional)**: You can adjust paper size, orientation (portrait/landscape), and page range before saving each PDF <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.

## Verification

Once the PDFs are generated, open them to verify that the data from the Notion database has correctly populated the template fields. For example, check if the client name, invoice number, and dates are accurate <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>.

## Key Reminders

*   **Public Page Access**: Ensure your Notion template page is shared publicly for PDFOutput to access it <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>.
*   **API Key Connection**: The Notion database *must* be connected to the specific API key you created in Notion <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>.
*   **Relational Properties**: If your database uses any relational properties linked to other Notion databases, those related databases must also be connected to the *same* API key <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>. This ensures all necessary data can be fetched seamlessly <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.

This method allows you to efficiently [[generating_invoices_from_a_notion_database | generate invoices from a Notion database]] or [[generating_payment_receipt_pdfs_in_bulk_using_notion | generate payment receipt PDFs in bulk using Notion]] <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>, streamlining your document creation workflow.

## Support

For any queries or issues, you can reach out to notionformyuse@gmail.com or use the contact window available on the PDFOutput.com website <a class="yt-timestamp" data-t="00:08:23">[00:08:23]</a>.