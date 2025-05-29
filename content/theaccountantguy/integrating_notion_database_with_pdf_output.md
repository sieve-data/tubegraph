---
title: Integrating Notion database with PDF output
videoId: zrr8DW4PWz0
---

From: [[theaccountantguy]] <br/> 

This article explains how to generate payment receipt PDF documents using a Notion database and template in conjunction with PDFoutput.com <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. The process involves setting up a template, connecting your Notion workspace, mapping database properties, and exporting the documents.

## Getting Started with PDFoutput.com

To begin, log in to PDFoutput.com <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. From the interface, navigate to the "Templates" section <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. Here, you'll find a list of available templates, including a "Payment Receipts PDF Generator" <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>. You can use search, filter, and sorting options to locate specific templates <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>, <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.

### Duplicating the Template to Notion

Once you've selected a template, click the "Download link" or "Duplicate" option <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>, <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>. This will prompt you to duplicate the template to your chosen Notion workspace <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>, <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>. The template needs to be in a Notion workspace to be usable with PDF output <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.

## Understanding the Notion Template and Database

After duplicating, you will have both a Notion template and a Notion database.

### Template Structure

The Notion template contains predefined elements for the PDF output <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. Key information, such as receipt numbers, dates, customer names, and amounts, is represented by placeholder text enclosed in curly braces (e.g., `{receipt number}`, `{customer name}`). These placeholders will be replaced by data from your Notion database <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>, <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.

### Database Requirements

The Notion database must contain columns with names that exactly match the placeholder text in the template <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>, <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>. For example, if your template has a `{customer name}` placeholder, your Notion database should have a column named "customer name" <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.

### Customization

The entire template is customizable to your requirements <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>. You can adjust formatting, such as making elements bold or adding spacing <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>. Just ensure that any placeholder elements intended for replacement from the database remain within curly braces <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.

## Connecting Notion to PDFoutput.com

1.  **Go to Settings:** In PDFoutput.com, navigate to the "Settings" section <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>.
2.  **Add Template:** Click on "Click here to add templates" <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.
3.  **Choose Notion Workspace:** Select the Notion workspace where you duplicated the template <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>, <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>.
4.  **Select Pages and Allow Access:** Choose the "Payment Receipts PDF Generator" file and click "Allow access" to enable PDFoutput to read your template and database elements <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>, <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>. Authentication should be successful <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>.

## Generating PDF Documents

### Mapping Database Properties

After connecting, refresh the PDFoutput.com screen <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>.

1.  **Select Database and Template:** From the drop-downs, select your "payment receipts database" and the corresponding "payment receipt template" <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>, <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.
2.  **Name the Connection:** Give the connection a name, for example, "payment receipt" <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.
3.  **Automatic Mapping:** PDFoutput.com will attempt to automatically map your Notion database properties (columns) to the template elements <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>, <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>. This works correctly if the naming conventions match exactly <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.
4.  **Manual Mapping:** If any elements are mismatched, you can manually select the correct corresponding element using the search, filter (including "unmapped properties"), and sorting options <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>, <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>.

### Exporting and Reviewing PDFs

1.  **Export:** Once all elements are correctly mapped, click "Export" <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>.
2.  **PDF Status Column:** PDFoutput.com will automatically add a "PDF status" column to your Notion database. This column will be ticked as each row's PDF is generated <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>, <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>.
3.  **Preview and Download:** After successful export, you can click "Preview sample" to view a generated PDF <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>. You can also "Download all" generated files, which will correspond to individual rows in your Notion database <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>, <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>.

## Additional Features and Support

*   **Connections Section:** The "Connections" section in PDFoutput.com displays your past connections, allowing you to quickly reload the database and template without re-adding them manually <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>, <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>.
*   **Multiple Templates:** You can select and manage multiple templates <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>.
*   **Watermark and Plans:** On the free plan, generated PDFs will include a PDFoutput.com watermark <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>. Upgrading to a paid plan removes this watermark <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>.
*   **Settings:** Under settings, you can change the page format of the PDFs <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>.
*   **Feedback:** A feedback option is available to send messages directly to support <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>.
*   **Help Section:** The help section provides a demonstration video to assist with setup <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.

For questions or assistance, you can reach out via email at notionformyuse@gmail.com <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>.

## Related Topics
*   [[using_notion_for_generating_pdf_documents | Using Notion for generating PDF documents]]
*   [[generating_pdf_documents_using_notion | Generating PDF documents using Notion]]
*   [[pdf_document_creation_with_notion_and_pdf_output | PDF document creation with Notion and PDF output]]
*   [[how_to_integrate_notion_with_pdf_generation_tools | How to integrate Notion with PDF generation tools]]
*   [[generating_pdf_documents_from_notion_database_rows | Generating PDF documents from Notion database rows]]
*   [[setting_up_and_connecting_notion_database_for_pdf_creation | Setting up and connecting Notion database for PDF creation]]
*   [[generating_pdf_documents_using_notion_databases | Generating PDF documents using Notion databases]]
*   [[setting_up_and_managing_notion_databases_for_pdf_generation | Setting up and managing Notion databases for PDF generation]]
*   [[connecting_notion_database_to_pdf_output_via_api_keys | Connecting Notion database to PDF output via API keys]]