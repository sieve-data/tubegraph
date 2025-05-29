---
title: Automating document exports using PDF output
videoId: Uh1g7uXtr_4
---

From: [[theaccountantguy]] <br/> 

[[using_pdf_output_tool_for_efficient_document_creation | PDF Output]] is a tool designed to [[using_pdfoutputcom_for_bulk_pdf_generation | generate PDF documents in bulk]] from a Notion database <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. This process automates the creation of individual PDF files for each row of information in a database, eliminating the need for manual data entry and one-by-one exports <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

## Setting Up Your Notion Database and Template

The first step in [[utilizing_pdf_output_for_bulk_pdf_generation | generating PDF documents]] is preparing your Notion database and a corresponding template.

### Database Structure
The demonstration uses an "application form database" where each row tracks requirements from a candidate profile to education <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>.

### Creating the Template
A template is created to match the fields in your database <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. Data fields within this template are enclosed in curly brackets, e.g., `{Full Name}`, `{Date of Birth}`, `{Gender}`, `{Phone Number}` <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. These curly-bracketed fields directly correspond to the column names in your Notion database <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.

### Populating the Template in Database Rows
For [[generating_pdf_invoices_using_pdfoutput | PDF generation]], each row in your Notion database needs to have the template content <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.

There are two primary methods to ensure this:
1.  **Manual Copy-Paste**: For existing rows, open each database entry, scroll to the bottom, and paste the template content <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.
2.  **Setting a Default Template**: To automate for new rows, click the dropdown next to "New" in your database <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.
    *   Select "New template" <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>.
    *   Name the template (e.g., "Applicant Name") <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.
    *   Paste the template content into this new template <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.
    *   Click the three dots next to the template and select "Set as default" for all views in the database <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.
    *   Now, any new row added to the database will automatically include this template <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.

## Connecting Notion to PDF Output

To enable [[using_pdf_output_tool_for_efficient_document_creation | PDF Output]] to access your Notion database, you need to establish a connection.

### Steps for Connecting Notion to PDF Output
1.  **Sign in to PDF Output**: Access the [[using_pdf_output_tool_for_efficient_document_creation | PDF Output]] dashboard <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
2.  **Copy Database URL**: Get the URL of your Notion database from the browser's address bar <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>. Paste this URL into the designated field in [[using_pdf_output_tool_for_efficient_document_creation | PDF Output]] <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.
3.  **Generate and Add API Key**:
    *   An API key is required to connect your database to [[using_pdf_output_tool_for_efficient_document_creation | PDF Output]] <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.
    *   Click the provided link in [[using_pdf_output_tool_for_efficient_document_creation | PDF Output]] to go to Notion's API key settings <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>.
    *   Click "New integration," add a name, choose your workspace, and save <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.
    *   Copy the "Internal Integration Secret" key <a class="yt-timestamp" data-t="00:04:58">[00:04:58]</a> and paste it into [[using_pdf_output_tool_for_efficient_document_creation | PDF Output]] <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.
4.  **Connect Database with API Key**:
    *   In your Notion database, click the three dots (`...`) menu <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>.
    *   Go to "Connections" and select the name of the API key you just created (e.g., "New Key") <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>. Confirm the connection <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.
5.  **Publish the Database**:
    *   Click "Share" in your Notion database <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>.
    *   Click "Publish" <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>. This makes the database live and accessible to [[using_pdf_output_tool_for_efficient_document_creation | PDF Output]] <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>. It is crucial for fetching pages within the database <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>.

## [[steps_to_set_up_and_export_pdfs_using_pdf_output | Generating PDF Documents]]

Once connected, you can proceed with [[exporting_pdf_documents_using_a_database | exporting PDF documents]].

### Steps for [[steps_to_set_up_and_export_pdfs_using_pdf_output | PDF Generation]]
1.  **Load Database**: In [[using_pdf_output_tool_for_efficient_document_creation | PDF Output]], click "Load Database" <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.
2.  **Select Reference Column**: Choose a column from the dropdown (e.g., "Full Name") to use as the naming convention for your generated PDF files <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>.
3.  **Select Rows**: Decide whether to generate PDFs for "All rows," a "range of rows," or "custom rows" <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.
4.  **Generate PDF**: Click "Generate PDF" <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.
5.  **Review and Save**:
    *   A preview window will appear, showing the populated PDF document with data from each row replacing the placeholder elements <a class="yt-timestamp" data-t="00:06:35">[00:06:35]</a>.
    *   On the right side, you can adjust settings like paper size and layout <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>.
    *   Click "Save" to [[exporting_and_managing_generated_pdf_documents | download]] each generated PDF to your local system <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>. The files will be named according to the selected reference column <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>.

### Output Verification
The generated PDFs will have the same structure as your template, with the corresponding data from each Notion database row seamlessly integrated <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>. The output is professional-looking and clean <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>.

## Alternative Template Usage

While the primary method involves embedding the template within each Notion database page, [[using_pdf_output_tool_for_efficient_document_creation | PDF Output]] offers an alternative:
*   You can directly use the URL of a standalone Notion template page <a class="yt-timestamp" data-t="00:10:32">[00:10:32]</a>.
*   Copy the template URL and paste it into the "Notion Page" field in [[using_pdf_output_tool_for_efficient_document_creation | PDF Output]] <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>.
*   Click "Load Page" to preview the document <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>.
*   Then, click "Load Database" and proceed with the same steps as above for [[utilizing_pdf_output_for_bulk_pdf_generation | generating PDFs]] <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>. This method still works even if the database pages don't explicitly contain the template <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>.

## General Applications and Support
[[using_pdf_output_tool_for_efficient_document_creation | PDF Output]] can be applied to various document generation needs, such as [[generating_pdf_invoices_using_pdfoutput | creating invoices]] from an invoices database, or [[syncing_and_exporting_documents_using_pdf_output | generating]] notes, lectures, or any form of documentation <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>. It's not mandatory for placeholder elements to match database content; the tool can read entire page content and [[utilizing_pdf_output_for_bulk_pdf_generation | generate documents]] accordingly <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.

For assistance, a "Contact" section is available at the bottom of the [[using_pdf_output_tool_for_efficient_document_creation | PDF Output]] homepage <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>. Additionally, [[using_pdf_output_tool_for_efficient_document_creation | PDF Output]] offers a "Templates" section with predefined templates that users can copy directly to get started <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>.