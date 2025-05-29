---
title: Using PDFOutput for bulk PDF generation
videoId: YbcxEBwvmKU
---

From: [[theaccountantguy]] <br/> 

[[using_pdf_output_for_invoice_generation | PDF Output]] is a tool designed to [[generating_pdf_documents_in_bulk | generate PDF documents in bulk]] <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. It utilizes a Notion page as a template and a Notion database to supply the data that replaces elements within the template <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>.

## Core Functionality

[[using_pdfoutput_for_document_generation | PDF Output]] allows users to define a Notion database for PDF generation and select a Notion template for the document's structure <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

## Setup and Configuration

Before using PDF Output, you need to set up your template and database in Notion <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.

### Creating a Template in Notion
1.  Create a new page in your Notion workspace <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.
2.  Add content for your template, such as an "invitation letter template" <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.
3.  Define placeholder sections within the template by enclosing them in curly braces, e.g., `{title}` and `{customer name}` <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>. These placeholders will be replaced with data from your database <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.

### Creating a Database in Notion
1.  Create a new page in Notion and select "Table" as the database type <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.
2.  Define columns in your database with the exact same naming convention as the placeholders in your template (e.g., "title" and "customer name") <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.
3.  Populate the database with rows containing unique information for each PDF you want to generate <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.

### Connecting Notion to PDF Output
1.  Log into [[using_pdf_output_com_for_bulk_pdf_generation | PDF Output]] <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.
2.  Click "click here to add database" or "add template" <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.
3.  Select your Notion account and then choose the specific template and database pages you created <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
4.  Allow access for [[setting_up_and_configuring_pdfoutput | PDF Output]] to sync with your Notion pages <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>.
5.  Once synced, you will see your selected database and template available in [[using_pdf_outputcom_for_bulk_pdf_creation | PDF Output]] <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.
6.  Define a connection name (e.g., "invitation letter") <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.

### Mapping Properties
After defining the connection, [[using_pdfoutput_com_for_document_generation | PDF Output]] automatically loads the template and database <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.
*   Database properties (columns) are displayed on the left <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.
*   Template elements (placeholders in curly braces) are displayed on the right <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.
*   If the naming convention is exact, elements will be automatically mapped <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>.
*   If there are any naming differences, you may need to manually select and map the elements <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.
*   Sorting, searching, and filtration options are available for properties <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.

## Generating PDFs

Once the mapping is complete, click "Create PDF" <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>.
*   [[generating_pdf_documents_in_bulk | PDF Output]] will generate a PDF document for each row in your Notion database, replacing the template's placeholders with the corresponding data <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a>.
*   You can preview a sample PDF <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.
*   You can then [[exporting_and_managing_pdfs_in_pdfoutput | download all the generated PDFs]] <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>. Each PDF will be an individual document based on one row of data <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>.

## Important Notes and Features

*   **Placeholder Consistency**: Always put placeholder text elements inside curly braces (`{}`) and use the exact same naming convention in your Notion database columns <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>.
*   **Reusing Connections**: Once a connection is created, you can access it via the "Connections" sidebar option to quickly load the predefined database and template for future generations <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>.
*   **Predefined Templates**: The "Templates" sidebar provides a list of predefined templates that can be used <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>. To use one, click "Start with this template" to duplicate both the database and template files to your Notion workspace <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>.
*   **Subscription Plans**: Under the free plan, generated PDFs will have a "made with [[using_pdf_outputcom_for_bulk_pdf_generation | PDF Output]]" watermark and certain limitations <a class="yt-timestamp" data-t="00:10:39">[00:10:39]</a>. You can upgrade your subscription to remove these <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>.
*   **Page Format**: In the "Settings" tab, you can choose different page formats for your PDFs <a class="yt-timestamp" data-t="00:11:01">[00:11:01]</a>.
*   **Adding More Templates**: If you want to add more databases or templates after the initial setup, you can do so through the "Settings" tab by clicking "click here to add more templates" <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>.
*   **Feedback and Help**: You can provide feedback or seek assistance directly from the "Feedback" or "Help" sections within the application <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>.