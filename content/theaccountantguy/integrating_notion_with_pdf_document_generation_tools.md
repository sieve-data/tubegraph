---
title: Integrating Notion with PDF document generation tools
videoId: n1_fpSFcf3k
---

From: [[theaccountantguy]] <br/> 

This article demonstrates how to [[integrating_notion_pages_and_databases_with_pdfoutput | integrate Notion pages and databases with PDFOutput]] to [[generating_pdf_documents_from_notion_using_pdfoutput | generate PDF documents from Notion using PDFOutput]] using an invoice template as an example <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>.

## Getting Started with PDFOutput

To begin [[integrating_notion_databases_with_pdfoutput | integrating Notion databases with PDFOutput]], you need to log in to PDFoutput.com <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. The interface allows you to create documents for various use cases <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

### Accessing Templates

From the main interface, navigate to the "template" section <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>. Here, you'll find a list of pre-created templates compatible with PDFOutput <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>. For this demonstration, the invoice template is used, which can be downloaded via its dedicated link <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>. You can use search, sorting, or filter options to locate specific templates <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.

### Understanding Template and Database Structure

Upon downloading a template, you'll see both the template and a corresponding Notion database <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.

#### Template Structure
The template contains elements like client name, company address, invoice number, date, and terms <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>. These elements are enclosed in curly braces, indicating they are placeholder texts <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>. These placeholders will be dynamically replaced with data from your Notion database <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>.

#### Database Structure
The Notion database features columns that correspond directly to the placeholder elements in the template, such as invoice number, date, client name, client company, and client address <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>. Each row in the database provides the data for a specific invoice, replacing the respective placeholders in the template <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.

### Duplicating Template to Notion

To start [[using_pdf_output_tool_with_notion | using PDF Output Tool with Notion]], click the "Start with this template" option on the PDFOutput site <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>. This prompts you to duplicate the template to your personal Notion workspace <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>. Select your Notion workspace from the dropdown and click "Add to private" <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>. The template and its associated database will then appear in your Notion workspace <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.

## Integrating Notion Template with PDFOutput

After duplicating the template to Notion, go back to PDFOutput and click on "Settings" <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>. Here, you will add the specific template you just duplicated <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.

### Linking Your Notion Workspace
Select the Notion workspace where you duplicated the template <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>. Then, click "Select pages" and choose the "invoice generator template" from the list of available pages in your workspace <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>. Click "Allow access" to authenticate and add the template to your PDFOutput setup <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.

### Mapping Notion Properties
Once authenticated, PDFOutput will sync the database and template elements <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.
On the PDFOutput screen, select your database and the professional invoice template <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>. Give your project a name (e.g., "invoice general") <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>. Clicking "Next" will sync all database and template elements <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>.

All Notion properties (database column headers) will be listed on the left and automatically mapped to their corresponding elements in the template <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>. For example, "Client Name" from Notion is mapped to the "Client Name" placeholder in the template <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>. Unmapped properties will be visible and can be manually mapped by searching for the correct element <a class="yt-timestamp" data-t="00:06:32">[00:06:32]</a>.

## Generating and Exporting PDFs

Once mapping is complete, click "Export" to start processing the documents <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>. In your Notion database, a "PDF Status" column will appear, and it will automatically check off as each document is generated <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>.

After successful export, you can preview a sample of the generated PDF <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>. To [[exporting_pdf_documents_from_notion | export PDF documents from Notion]] in bulk, click "Download All" to get all generated PDF outputs <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>. Each invoice from the database will be generated as a separate PDF file <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.

## Customization and Best Practices

### Template and Database Customization
Both the Notion template and the database are fully customizable <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.
*   **Template:** You can add, delete, or modify values in the template <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>. Ensure that all placeholder texts remain within curly braces `{}` <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.
*   **Database:** The column names in your Notion database must exactly match the placeholder names in the template <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>. For instance, if your template uses `{Invoice Number}`, your database column must be named "Invoice Number" <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.

### PDF Status Column
Before [[generating_pdfs_in_bulk_with_notion | generating PDFs in bulk with Notion]], ensure the "PDF Status" row in your Notion database is unticked <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>. If a row is ticked, it will be ignored during generation <a class="yt-timestamp" data-t="00:08:51">[00:08:51]</a>.

## Additional Features and Support

### Other Templates
You can explore and utilize various other templates available in PDFOutput for different document types <a class="yt-timestamp" data-t="00:08:58">[00:08:58]</a>.

### Watermark
If you are on the free plan, generated PDFs will include a watermark <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>. To remove it, you need to upgrade to a paid subscription plan <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>.

### Saved Connections
Once you've configured an [[integrating_notion_with_pdf_output_for_document_creation | integrating Notion with PDF Output for document creation]] setup, your connections are saved <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>. You can quickly reload previous configurations, including the linked database and template, without needing to remap elements every time <a class="yt-timestamp" data-t="00:09:39">[00:09:39]</a>.

### Help and Feedback
A "Help" section provides a detailed demonstration on setting up the integration for the first time <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>. For questions or feedback, you can contact notionforuse@gmail.com <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>.