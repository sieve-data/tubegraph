---
title: Exporting Notion data to PDF
videoId: Uh1g7uXtr_4
---

From: [[theaccountantguy]] <br/> 

This article explains how to [[generating_pdf_documents_from_notion | generate PDF documents]] for each row in a [[using_notion_as_a_database_for_pdf_generation | Notion database]], eliminating the need for manual data entry and individual exports <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. The demonstration uses an application form database, tracking details like candidate profile and education requirements <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>.

## Setting Up Your Notion Database for PDF Generation

To [[creating_a_notion_database_for_pdfs | create a Notion database for PDFs]], follow these steps:

### 1. Structure Your Notion Database
The database columns should contain the information you wish to include in your PDFs <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>. For an application form, this might include "Full Name," "Date of Birth," "Gender," and "Phone Number" <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.

### 2. Create a Template Page
Design an application form template that mirrors the database structure <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. For dynamic fields that will be populated from your database, place the exact column names inside curly brackets (e.g., `{Full Name}`, `{Date of Birth}`, `{Gender}`, `{Phone Number}`) <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. These curly-bracketed fields act as placeholders that will be replaced with data from the corresponding database columns <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

### 3. Integrate the Template into Database Rows
For each row in your database, open it and paste the template content into the empty section at the bottom <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.

#### Automating Template Population
To avoid manual copying and pasting for new entries, you can set up a default template for your database:
1.  Click the drop-down menu next to the "New" button in your database <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.
2.  Select "New template" <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>.
3.  Give the template a name (e.g., "Applicant Name") <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.
4.  Paste your application form template content into this new template page <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.
5.  Click outside the template to save it <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.
6.  Click the three dots next to your newly created template in the drop-down menu and choose "Set as default" <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.
7.  Select "For all views" and specify your "Application Form Database" <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>.

Now, any new row added to the database will automatically include the template <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.

## [[generating_pdf_documents_with_notion_and_pdfoutput | Generating PDF documents with Notion and PDFOutput]]

This process utilizes a tool called PDFOutput <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>, which requires a Notion database to [[bulk_pdf_generation_from_notion_databases | generate documents in bulk]] <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>.

### 1. Connect Notion to PDFOutput
1.  Sign in to PDFOutput <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
2.  Copy your Notion database URL from the top of your Notion page <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.
3.  Paste the database URL into the designated field in PDFOutput <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.
4.  [[connecting_notion_database_with_pdf_output | Connect the Notion database with PDFOutput]] via an API key <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>:
    *   Click the link in PDFOutput to add an API key <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>.
    *   In Notion's API key settings, create a "New integration," add a name, choose your workspace, and save <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.
    *   Copy the "Internal Integration Secret" from the newly created key <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>.
    *   Paste this key into PDFOutput <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.
5.  Ensure the Notion database is connected to the API key you just created <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>:
    *   In Notion, click the three dots on your database page <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>.
    *   Go to "Connections" and select your API key (e.g., "new key") <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>.
6.  Publish the database <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>:
    *   Click "Share" on your Notion database page <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>.
    *   Click "Publish" <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>. This makes the database accessible to PDFOutput <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>.

### 2. Generate PDFs
1.  In PDFOutput, click "Load Database" <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.
2.  Select the Notion column you want to use for naming your PDF files (e.g., "Full Name") <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.
3.  Choose whether to generate PDFs for "All rows," a "range of rows," or "custom rows" <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.
4.  Click "Generate PDF" <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.
5.  A preview window will appear, showing the populated data from each row <a class="yt-timestamp" data-t="00:06:35">[00:06:35]</a>. You can adjust settings like paper size and layout on the right side <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>.
6.  Click "Save" to download each PDF file <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>. The files will be named according to the column you selected <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>.

> [!INFO] Template Requirement
> The template file **must** be available inside each row of the database for the files to generate successfully <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>.

## [[different_methods_for_pdf_generation_with_notion | Different Methods for PDF Generation with Notion]]

### Method 1: Database with Integrated Template (Demonstrated Above)
This method involves having a Notion database where each row contains the template content, either manually pasted or automatically populated via a default template <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>.

### Method 2: Separate Template URL with Database
Alternatively, you can use a Notion database without pre-filled templates in each row, and instead, directly link the main template page URL in PDFOutput <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>.
1.  Copy the URL of your main template page in Notion <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>.
2.  Paste this URL into the "Notion Page" field in PDFOutput <a class="yt-timestamp" data-t="00:10:44">[00:10:44]</a>.
3.  Click "Load Page" to load the document preview <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>.
4.  Then, load your database URL as usual <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>, select the column reference, and click "Generate PDF" <a class="yt-timestamp" data-t="00:10:58">[00:10:58]</a>. This approach will also work for [[using_notion_for_pdf_template_creation | PDF template creation]] <a class="yt-timestamp" data-t="00:11:04">[00:11:04]</a>.

## Flexibility of Template Content
It's not mandatory for your template's placeholder text elements to exactly match all the content or fields in the database <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>. PDFOutput will read the entire content of the page and generate the document <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>. You can include any information, notes, or lectures within the template pages, and it will still be included in the generated PDF <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>.

## Other Use Cases
This method can be applied to various document generation needs, such as [[generating_pdf_invoices_from_notion_data | generating PDF invoices from Notion data]] from an invoices database <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>.

## Additional Resources
*   PDFOutput provides a "Templates" section with predefined templates and associated "how-to-use" videos <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>.
*   For assistance, you can use the contact section at the bottom of the PDFOutput homepage <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a>.