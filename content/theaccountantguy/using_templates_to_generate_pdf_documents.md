---
title: Using templates to generate PDF documents
videoId: n1_fpSFcf3k
---

From: [[theaccountantguy]] <br/> 

This article demonstrates how to use Notion pages and templates in conjunction with PDFOutput.com to [[generating_pdf_documents_for_businesses | generate PDF documents]] from a Notion database <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. The process is illustrated using an invoice template <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.

## Getting Started

1.  **Log In to PDFOutput**: Access the service by logging in at PDFOutput.com <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. The interface allows for document creation <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.
2.  **Access Templates**: Navigate to the "template" section within the PDFOutput interface <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. Here, a list of pre-existing templates compatible with PDFOutput is displayed <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.
3.  **Download a Template**: For this demonstration, the "invoices template" is used. It can be downloaded directly from the list <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>. Users can also utilize search, sort, or filter options to find specific templates <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.

## Understanding the Template and Database Structure

After downloading, the [[creating_and_using_templates_for_document_generation | template]] and its corresponding database will be displayed <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.

### Notion Template

The Notion [[creating_and_using_templates_for_document_generation | template]] is designed for generating PDF output <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>. It contains various elements like client name, company address, invoice number, date, and terms <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.

*   **Placeholders**: All these elements are placed inside curly braces, indicating they are placeholder text elements <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>. These placeholders will be automatically replaced with data from the connected database <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>.

### Notion Database

The database connected to the [[creating_and_using_templates_for_document_generation | template]] has columns that match the placeholder elements <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>. For example, columns like invoice number, date, client name, and client company are present <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>. Each row in the database represents a unique set of data that will populate a separate PDF document <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.

*   **Naming Convention**: It is crucial that the names of the database columns exactly match the placeholder text elements within the curly braces in the Notion [[creating_and_using_templates_for_document_generation | template]] <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>, <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>. This ensures correct data mapping during generation <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.

## Setting Up and Generating PDFs

1.  **Duplicate the Template**: In PDFOutput, click "Start with this template" <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>. This action prompts you to duplicate the [[creating_and_using_templates_in_google_docs_for_bulk_document_generation | template]] onto your personal Notion workspace <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>. Select your desired Notion workspace and add it to your private pages <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>.
2.  **Add Template to PDFOutput Settings**: Go back to PDFOutput and click on "Settings" <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>. Here, select the specific template you just duplicated to add it to PDFOutput <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>. Ensure you select the correct Notion workspace where the template resides <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>.
3.  **Authenticate and Sync**: After selecting the template, click "Allow access" to authenticate the template and add it to your PDFOutput setup <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>. PDFOutput will then sync the database and template elements <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.
4.  **Customize (Optional)**: The Notion [[creating_and_using_templates_for_document_generation | template]] is fully customizable. You can add, delete, or modify any content. However, ensure that all placeholder text elements remain within curly braces and their names correspond exactly to the column names in your Notion database <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.
5.  **Map Properties**: Once synced, PDFOutput will display Notion properties (database columns) and automatically map them to the corresponding template elements <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>. Mapped elements will show a green bar <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>. If any property is unmapped, you can manually select and map it <a class="yt-timestamp" data-t="00:06:32">[00:06:32]</a>. Search, sort, and filter options are available for managing properties <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>.
6.  **Export**: Click "Export" to begin processing the documents <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>. A "PDF status" column in your Notion database will automatically update (get checked) as each document is generated <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>.
7.  **Preview and Download**: After successful export, you can preview a sample document to verify the output <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>. Then, click "Download all" to receive all generated PDF documents <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>. Each row from your database will result in a separate PDF <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>.

### Important Notes for Generation

*   Before generating, ensure that the "PDF status" row in your database is unticked <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>. Ticked rows will be ignored <a class="yt-timestamp" data-t="00:08:51">[00:08:51]</a>.
*   On the free plan, generated PDFs will include a watermark <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>. Upgrading to a paid plan removes the watermark <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>.

## Managing Connections

Once a particular output is generated and exported, the connection details are saved. You can access previous connections under the "Connections" section <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>. This allows you to quickly load the same database and template without re-mapping <a class="yt-timestamp" data-t="00:09:39">[00:09:39]</a>.