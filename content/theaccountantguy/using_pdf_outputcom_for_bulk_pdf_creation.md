---
title: Using PDF Outputcom for Bulk PDF Creation
videoId: W_j9W6XedqM
---

From: [[theaccountantguy]] <br/> 

[[using_pdf_output_com_for_bulk_pdf_generation | PDF Output.com]] is a tool designed to [[generating_pdf_documents_in_bulk | generate PDF documents in bulk]] by connecting Notion templates and Notion databases <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. This method allows for the automated creation of multiple personalized documents, such as payment receipts <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>.

## Key Components

The process of [[using_pdf_output_com_for_bulk_pdf_generation | bulk PDF generation]] relies on two main components within Notion:

*   **Notion Template**: This document contains placeholders, or elements, enclosed in curly braces (e.g., `{company_website}`) <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. These placeholders will be dynamically replaced with information from the database <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>. An example is a payment receipt template <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>.
*   **Notion Database**: This acts as the data source. Each column in the database should correspond to an element in the template, and each row represents a unique document to be generated <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>, <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. To ensure automatic mapping between the template and database, the column names in the database must exactly match the elements specified within the curly braces in the template, including spacing and capitalization <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>.

## How to [[using_pdf_output_com_for_bulk_pdf_generation | Generate PDFs in Bulk]] with PDF Output.com

The general workflow involves several steps to connect your Notion data with [[using_pdfoutput_com_for_document_generation | PDF Output.com]] and produce documents:

### Step 1: Accessing PDF Output.com and Templates

Navigate to [[using_pdf_output_com_for_bulk_pdf_generation | PDF Output.com]] <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a> and log in <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>. Once logged in, go to the "Template" section on the sidebar <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>. Here, you can search for and find pre-built templates, such as the "Payment Receipts" template <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>. Each template provides a database link and a template link <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.

### Step 2: Duplicating Notion Template and Database

Before proceeding, you need to duplicate both the template and its corresponding database from [[using_pdfoutput_com_for_document_generation | PDF Output.com]]'s template section into your local Notion workspace <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.
1.  Click the "Duplicate" button on the template page and select your Notion workspace <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>.
2.  Repeat the duplication process for the database, adding it to the same Notion workspace <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>.

### Step 3: Connecting Notion to PDF Output.com

Return to the [[using_pdfoutput_com_for_document_generation | PDF Output.com]] interface <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>.
1.  Click "Click here to add database" or "Add template" <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.
2.  You will be prompted to grant access to your Notion pages. Select the specific Notion workspace (e.g., "accountant guy") <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.
3.  Select both the duplicated template and database, then click "Allow access" <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
4.  Once authentication is successful, the connected database and template will be displayed <a class="yt-timestamp" data-t="00:05:33">[00:05:33]</a>.
5.  Give your connection a name (e.g., "payment receipts") and click "Next" <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>. If the database or template doesn't load immediately, click "Refresh" <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>.

### Step 4: Mapping Database Properties to Template Elements

[[using_pdfoutput_com_for_document_generation | PDF Output.com]] will load the database properties and attempt to automatically map them to the template elements <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>.
*   If your database column names perfectly match the template elements in curly braces, the mapping will be automatic <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>.
*   If there are mismatches, you will need to manually select the corresponding database property for each template element <a class="yt-timestamp" data-t="00:06:59">[00:06:59]</a>. You can use the search and filter options to assist with mapping <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>.

### Step 5: [[generating_pdf_documents_in_bulk | Generating and Downloading PDFs]]

Once all elements are correctly mapped, click "Create PDF" <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.
*   The system will process each row in your database, replacing template placeholders with the corresponding data, and generate a PDF document for each <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>.
*   After generation, you can preview a sample document to check the output quality <a class="yt-timestamp" data-t="00:07:46">[00:07:46]</a>.
*   Finally, click "Download all documents" to receive a bulk download of your generated PDFs <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>. The generated PDFs are clean and accurately populated with data from the Notion database <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>.

## Additional Features

[[exporting_and_managing_pdfs_in_pdfoutput | PDF Output.com]] offers several features beyond basic document generation:

*   **Connections**: This section displays a list of all previously created database and template connections <a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a>. Clicking on a saved connection will automatically load the database and template, allowing you to quickly regenerate PDFs without re-adding them manually <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a>.
*   **Templates Library**: Access a variety of pre-defined templates for different use cases, such as invoices, in addition to payment receipts <a class="yt-timestamp" data-t="00:10:06">[00:10:06]</a>.
*   **Upgrade Options**: The free plan includes a "Made with [[using_pdf_output_for_invoice_generation | PDF Output]]" watermark <a class="yt-timestamp" data-t="00:10:18">[00:10:18]</a>. Upgrading to a paid plan removes this watermark and typically provides higher usage limits <a class="yt-timestamp" data-t="00:10:22">[00:10:22]</a>.
*   **Settings**: Configure preferences such as the default page format (e.g., A4) <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>. You can also add more templates and databases from this section <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>.
*   **Feedback and Support**: A dedicated window allows users to provide feedback or ask questions directly <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a>. For general inquiries, you can also reach out via email at notionformyuse@gmail.com <a class="yt-timestamp" data-t="00:11:47">[00:11:47]</a>.
*   **Custom Templates**: If you wish to use a custom template that is not pre-defined, a "Help" section explains the steps for generating documents in a custom PDF format without relying on the provided template and database structure <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>.

## Conclusion

[[using_pdf_output_to_create_invoices | PDF Output.com]] streamlines the process of [[generating_pdf_documents_in_bulk | bulk PDF generation]] by leveraging Notion databases and templates, making it efficient to create numerous documents with personalized data <a class="yt-timestamp" data-t="00:08:55">[00:08:55]</a>.