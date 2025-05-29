---
title: Connecting Notion databases with PDF generation tools
videoId: hfHjnNxqo4o
---

From: [[theaccountantguy]] <br/> 

[[setting_up_pdfoutput_for_notion_databases | PDFOutput]] allows users to generate PDF documents, such as purchase orders, in [[bulk_pdf_generation_from_notion_databases | bulk]] directly from a Notion page and database <a class="yt-timestamp" data-t="00:00:01">[00:00:01]</a>.

## Template and Database Structure

A typical template, such as a purchase order, includes fields like purchase order number, date, supplier, and buyer name <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. In these templates, items placed inside curly braces (e.g., `{purchase order number}`, `{date field}`, `{supplier name}`, `{buyer name}`) serve as placeholders that will be replaced with data from a Notion database <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>.

The Notion database used for generation must contain columns with the exact same naming convention as the curly-braced items in the template <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>. Each row in the database represents a distinct document to be generated, with values placed for each field <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>.

## [[setting_up_pdfoutput_for_notion_databases | Setting up PDFOutput for Notion Databases]]

To begin [[connecting_notion_database_to_pdf_generator | connecting Notion database to PDF generator]] for bulk PDF generation:
1.  **Log in to PDFOutput.com** <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>.
2.  **Access Templates:** Navigate to the "Template" section in the sidebar <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.
3.  **Search for Templates:** Search for desired predefined templates (e.g., "purchase order") <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.
4.  **Duplicate Templates and Databases:**
    *   Click on the database link and the template link provided for the chosen template <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.
    *   Select "Start with this template" to duplicate the database onto your Notion workspace <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.
    *   Choose your Notion workspace and click "Add to private" to complete the duplication <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.
    *   Repeat this duplication process for the template as well <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.
5.  **Connect Notion to PDFOutput:**
    *   Return to PDFOutput and click "Click here to add database" or "Click here to add template" <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.
    *   Select your Notion workspace, choose the duplicated database and template, and click "Allow access" to connect them <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>.
    *   If the database and template don't appear immediately, click the refresh button <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>. Multiple databases and templates can be selected or searched for using dropdown menus <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.
6.  **Define Output Name:** Provide a name for the PDF generation process (e.g., "purchase order") and click "Next" <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>.
7.  **Map Fields:**
    *   The system will automatically map database properties to template elements if the naming conventions are identical (e.g., `{purchase order number}` in the template maps to a database column named "purchase order number") <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>.
    *   If automatic mapping fails (indicated by a gray color), manual mapping is required by selecting the correct element from a dropdown <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.
8.  **Generate PDFs:** Click "Create PDF" to process the documents from the database <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.
9.  **Preview and Download:** Once export is successful, you can preview a sample document <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a> or download all generated PDF documents <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>.

## Customization and Advanced Features

*   **Template Customization:** Templates are customizable; users can edit or modify them after duplication. Ensure any data to be replaced from the database remains within curly braces and adheres to the exact naming convention used in the database <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>.
*   **Saved Connections:** Once a connection is created, it appears under the "Connections" option, allowing for quick reloading of the database and template for future exports without re-entering details <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>.
*   **Subscription Options:** Free plans include a "Made with PDFOutput" watermark. Upgrading to a paid subscription removes the watermark and usage limits <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>.
*   **Page Format:** The default page format for PDFs is A4 <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>.
*   **Adding More Databases/Templates:** Additional databases and templates can be added via the "Settings" section <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.
*   **Feedback and Help:** Feedback options are available for reporting issues or providing suggestions <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>. A help section provides guidance on [[creating_a_notion_database_for_pdfs | creating a custom template and database]] from scratch if predefined templates are not desired <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>.
*   **Relation Properties:** If a Notion database uses relation properties, ensure that any related databases are also granted access during the connection process for all elements to reflect correctly in the PDF output <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.