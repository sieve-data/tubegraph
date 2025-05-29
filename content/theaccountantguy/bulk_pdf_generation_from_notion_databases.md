---
title: Bulk PDF generation from Notion databases
videoId: Uh1g7uXtr_4
---

From: [[theaccountantguy]] <br/> 

This article details how to [[generating_pdf_documents_from_notion | generate PDF documents]] in bulk from data stored in Notion databases, primarily using the PDFOutput tool <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>. This process is useful for creating multiple documents like application forms or invoices from structured Notion data <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>.

## Preparing Your Notion Database

To begin, you need a Notion database containing the information you wish to convert into PDFs and a corresponding template that defines the structure of your desired PDF document.

### Setting up the Database

The database should contain all the necessary fields (columns) that will populate your PDF documents <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>. For example, an application form database might track candidate profiles, education requirements, and other relevant details <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

### Creating the Template

The template is a Notion page designed to look like your final PDF. Crucially, it uses curly brackets `{}` to define placeholders that correspond to the exact field names in your database <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.

For instance, if your database has a "Full Name" column, the template would include `{Full Name}` where the applicant's name should appear <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>. Other fields like `{Date of Birth}`, `{Gender}`, and `{Phone Number}` would also be placeholders <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>.

### Integrating the Template into Database Rows

There are two primary ways to ensure each database row can generate a PDF:

1.  **Manual Copy-Pasting (Initial Setup)**:
    *   For each existing row in your database, click to "Open" the page <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>.
    *   Scroll to the bottom where it prompts to "Add an empty page or create a template" <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.
    *   Copy the content of your pre-made template page <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.
    *   Paste this content into the empty page section of each database row <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.

2.  **Setting a Default Template (Automated)**:
    *   Click the dropdown arrow next to the "New" button on your database <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.
    *   Select "New template" <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>.
    *   Give the template a name (e.g., "Applicant Name") <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.
    *   Paste your template content (with curly bracket placeholders) into this new template <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>.
    *   Click outside the template to save it <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.
    *   Click the three dots next to the template name and select "Set as default" <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>. Choose "For all views in [Database Name]" <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>.
    *   Now, any new row added to the database will automatically include this template <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.

## Using PDFOutput for Bulk PDF Generation

PDFOutput is a tool designed to [[generating_pdf_documents_with_notion_and_pdfoutput | generate PDF documents with Notion and PDFOutput]] in bulk <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.

### Connecting Notion to PDFOutput

Before generating PDFs, you need to connect your Notion database to PDFOutput:

1.  **Sign in to PDFOutput**: Access the PDFOutput dashboard <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.
2.  **Copy Database URL**: From your Notion database, copy the URL from the browser's address bar <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.
3.  **Paste Database URL**: Paste this URL into the designated field on the PDFOutput interface <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.
4.  **Generate Notion API Key**:
    *   In Notion, go to "Settings & members" > "Integrations" > "Develop your own integrations" <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.
    *   Click "New integration," provide a name, select your workspace, and save <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.
    *   Once created, click on the integration name, then "Show" next to "Internal Integration Secret" to reveal the key <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>. Copy this key <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.
5.  **Paste API Key**: Return to PDFOutput and paste the copied API key into the respective field <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.
6.  **Connect Database to API Key**: In Notion, open your database, click the three dots (`...`) in the top right corner, select "Connections," and choose the integration you just created (e.g., "New Key") <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>. Confirm the connection <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>.
7.  **Publish Database**: In Notion, with your database open, click "Share," then "Publish," and finally "Publish" again <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>. This makes the database accessible to PDFOutput <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>.

### Generating the PDFs

With the connection established, you can now [[exporting_notion_data_to_pdf | export Notion data to PDF]]:

1.  **Load Database**: In PDFOutput, click "Load database" <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.
2.  **Select Naming Column**: Choose which column from your database (e.g., "Full Name") should be used to name the generated PDF files <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.
3.  **Choose Rows**: Select whether to generate PDFs for "All Rows," a specific "Range of Rows," or "Custom Rows" <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.
4.  **Generate PDF**: Click "Generate PDF" <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.
5.  **Review and Save**: A preview window will appear, showing the populated PDF for each row. You can adjust settings like paper size and layout <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>. Click "Save" for each document to download it <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>. The files will be named according to your selected naming column <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>.

## Alternative Method: Using a Separate Notion Page as the Template

Instead of embedding the template in each database row, you can reference a standalone Notion page as the template:

1.  **Copy Template Page URL**: Copy the URL of your dedicated Notion template page <a class="yt-timestamp" data-t="00:10:36">[00:10:36]</a>.
2.  **Paste Template URL**: In PDFOutput, paste this URL into the "Notion Page" field <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>.
3.  **Load Page**: Click "Load page" to load the template <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>.
4.  **Load Database**: Then, load your Notion database URL and proceed with selecting the naming column and rows as described above <a class="yt-timestamp" data-t="00:10:55">[00:10:55]</a>.
5.  **Generate PDF**: Click "Generate PDF" <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>.

This method works even if the content inside your database rows doesn't explicitly match the template's placeholder elements, as PDFOutput will read the entire content of the template page and populate the placeholders from the database <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>.

## Applications and Support

This method for [[different_methods_for_pdf_generation_with_notion | generating PDF documents from Notion]] is versatile and can be applied to various use cases, such as [[generating_pdf_invoices_from_notion_data | generating PDF invoices from Notion data]], reports, or any other document where you need to batch-process information from a database <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>.

PDFOutput also offers predefined templates and support sections for further assistance <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>.