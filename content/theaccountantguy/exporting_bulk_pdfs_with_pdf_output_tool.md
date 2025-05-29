---
title: Exporting Bulk PDFs with PDF Output Tool
videoId: oprL9NBoj8o
---

From: [[theaccountantguy]] <br/> 

[[introduction_to_pdfoutput_tool | PDF Output]] is a tool designed to [[bulk_export_of_pdf_documents | generate PDF documents in bulk]] <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. It utilizes a Google Document as a template and a Notion database to hold the data elements that replace placeholders in the Google Document <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. This enables the [[bulk_pdf_document_export_process | bulk PDF document export process]] <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.

## Getting Started

To begin [[using_pdf_output_interface_for_exporting_documents | using the PDF Output interface for exporting documents]], navigate to PDFoutput.com and log in <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>. The interface will display options to add a Google Document and a Notion database, followed by an "Export PDF" button to initiate document generation <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.

## Step-by-Step Document Generation

### 1. Adding a Google Document Template

The first step in [[customizing_and_exporting_pdf_documents_with_pdf_output_tool | customizing and exporting PDF documents with PDF Output tool]] is to add a Google Document <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. You have two options:
*   **Create a blank document from scratch** <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.
*   **Choose an existing document** from your Google Drive <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

After creating or selecting a document, rename it as needed (e.g., "Invitation Template") <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>. Within this document, define placeholders (e.g., `{{salutation}}`, `{{customer name}}`) that will be replaced by data from your Notion database <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.

### 2. Connecting a Notion Database

Next, connect a Notion database by clicking "Add Notion Database" <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.
1.  Connect to your Notion account <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.
2.  Select the specific Notion page or database you want to use (e.g., "Invitation List") <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.
3.  Click "Allow access" to link the database to PDF Output <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.

Once connected, PDF Output will display the properties (columns) of your Notion database <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>. If you add new columns to your Notion database, click "Refresh properties" to fetch the updated list <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.

### 3. Mapping Data Fields and Exporting PDFs

With both the Google Document and Notion database connected:
1.  In the PDF Output interface, select a property from your Notion database (e.g., "salutation") <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>.
2.  Copy the property value <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>.
3.  In your Google Document, select the corresponding placeholder and paste the copied property value <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>. This maps the database column to the template placeholder <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.
4.  Repeat this for all dynamic fields in your template (e.g., "customer name") <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.

Once all fields are mapped, click "Export PDF" <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>. You may need to complete a Google authentication step <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>. The tool will then read each row in your Notion database and [[bulk_exporting_and_downloading_generated_pdf_files | generate and download individual PDF files]] for each entry <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>.

> [!Example] Invitation Template Demonstration
> For an invitation template, a Notion database with "salutation" and "customer name" columns was used. The template contained "Dear {{salutation}} {{customer name}}" <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>. Entries like "Mr. Vikash", "Mr. Sanat", and "Mrs. Satabdi" from the Notion database were used to generate personalized PDFs <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>. This demonstrates the process for [[setting_up_and_exporting_pdf_receipts_in_bulk | setting up and exporting PDF receipts in bulk]] or similar documents.

## Advanced Features and Tips

### Handling Connected Notion Databases
If your primary Notion database is connected to other databases, ensure you select all linked databases during the connection process to allow PDF Output to access all necessary data <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.

### Using Pre-made Templates
PDF Output provides pre-made templates, such as an [[exporting_completed_pdf_invoices | invoice template]] <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>. You can:
*   **Make a copy** of the template directly to your Google workspace <a class="yt-timestamp" data-t="00:07:46">[00:07:46]</a>.
*   **Copy and paste** the content into a blank Google Document that you create within PDF Output <a class="yt-timestamp" data-t="00:07:53">[00:07:53]</a>.

### Interface Utilities
The PDF Output interface includes features such as:
*   **Search properties**: To find specific database properties <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>.
*   **Sorting window**: To sort values for your use case <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>.
*   **Refresh properties**: To update the list of Notion database properties after changes <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.

This comprehensive approach allows for efficient [[exporting_bulk_pdf_documents_from_a_database | exporting bulk PDF documents from a database]], streamlining document generation for various needs.

If you have further questions, you can reach out to notionforuse@gmail.com <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.