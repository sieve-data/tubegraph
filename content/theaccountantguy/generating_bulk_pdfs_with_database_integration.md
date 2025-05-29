---
title: Generating bulk PDFs with database integration
videoId: 5lnQYIpvjnM
---

From: [[theaccountantguy]] <br/> 

This article outlines a process for [[generating_pdfs_for_business_invoices | generating professional invoice documents]] in bulk using a Notion template and a database, with the help of [[pdfoutput_for_bulk_document_generation | PDFOutput]]. The method allows for the dynamic replacement of information from database records into a Notion page, enabling [[bulk_exporting_pdf_documents | bulk export]] of customized PDF documents <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.

## Overview of the Process

The [[bulk_pdf_document_generation_process | bulk PDF document generation process]] involves three primary components:
1.  A professional invoice template created as a Notion page <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>.
2.  A Notion database containing varying invoice-related information <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.
3.  The [[pdfoutput_for_bulk_document_generation | PDFOutput]] service (pdf4put.com) to facilitate the connection and generation <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.

The goal is to create a separate PDF document for each record in the Notion database, replacing placeholder text in the template with data from the corresponding database entry <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>.

## Preparing the Notion Template and Database

### Template Setup
A Notion page serves as the professional invoice template <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>.
*   **Placeholders**: Information that needs to be dynamically replaced from the database must be enclosed within curly brackets (e.g., `{Client Name}`, `{Client Company}`, `{Client Address}`) <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.
*   **Public Access**: The Notion template page must be made public to be accessible by [[pdfoutput_for_bulk_document_generation | PDFOutput]] <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>. This is achieved by clicking "Share," then "Publish," and again "Publish" in Notion <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>. The page link can then be copied <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.

### Database Setup
A Notion database holds the specific data for each invoice <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.
*   **Matching Fields**: The column headers in the database must correspond to the placeholder names used in the Notion template (e.g., a column named "Client Name" for the `{Client Name}` placeholder) <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.
*   **API Key Connection**: The Notion database must be connected to a Notion API key <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.
    1.  Go to Notion's integrations page (via a link provided by [[pdfoutput_for_bulk_document_generation | PDFOutput]]) <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.
    2.  Create a new integration, provide a name, and choose the associated Notion account <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.
    3.  Copy the generated API key <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.
    4.  In the Notion database, click the three dots (`...`) on the top right, then "Connections," and search for the newly created integration (API key name) to connect it <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.
*   **Database URL**: Copy the URL of the Notion database page from the browser's address bar <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.

## Generating PDFs with [[pdfoutput_for_bulk_document_generation | PDFOutput]]

### Steps on pdf4put.com
1.  **Login**: Sign in to pdf4put.com using a chosen account <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.
2.  **Paste Notion Page URL**: Paste the public URL of the Notion invoice template page into the designated field <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>. Click "Load Page" to verify the template appears <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>.
3.  **Paste API Key**: Paste the Notion API key obtained earlier into its field <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.
4.  **Paste Database URL**: Paste the URL of the Notion database into its field <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.
5.  **Load Database**: Click "Load Database" <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>.
6.  **Choose Naming Column**: Select a column from the database (e.g., "invoice number") to be used for naming the generated PDF files <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.
7.  **Select Rows (Optional)**: Users can choose to [[bulk_pdf_document_generation_process | generate documents]] for all rows, specific custom rows, or a range of rows <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.
8.  **Generate PDF**: Click "Generate PDF" to begin the [[bulk_pdf_generation_process | bulk PDF generation process]] <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.

### Output and Customization
*   [[pdfoutput_for_bulk_document_generation | PDFOutput]] will sequentially populate each invoice, replacing the curly-bracketed fields with data from each database record <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>.
*   Users can adjust layout settings such as paper size (e.g., A4) and orientation (portrait/landscape) before saving each PDF <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>.
*   The generated PDFs are named according to the selected column (e.g., "invoice number") <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>.

## Key Reminders

*   **Page Sharing**: The Notion page used as a template *must* be shared publicly <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>.
*   **Database Connection**: The Notion database *must* be connected to the API key created for the integration <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>.
*   **Relational Properties**: If the database utilizes any relation properties (linking to other databases), those linked databases *must also* be connected to the same API key to ensure seamless data fetching <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>.

For any queries, contact `notionformyuse@gmail.com` or use the contact window on the [[pdfoutput_for_bulk_document_generation | PDFOutput]] platform <a class="yt-timestamp" data-t="00:08:23">[00:08:23]</a>.