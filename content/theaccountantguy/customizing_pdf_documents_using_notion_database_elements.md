---
title: Customizing PDF documents using Notion database elements
videoId: oprL9NBoj8o
---

From: [[theaccountantguy]] <br/> 

PDFOutput is a tool designed to generate PDF documents in bulk by combining a Google Document as a template with a Notion database containing the data elements for replacement <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. This process allows for efficient [[generating_pdfs_from_notion_using_pdfoutput | bulk PDF generation]] based on dynamic data.

## Getting Started with PDFOutput

To begin, users need to log in to PDFoutput.com <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>. The interface will then prompt for the integration of a Google Document and a Notion database before allowing the export of PDFs <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.

### Adding a Google Document Template

There are two primary ways to add a Google Document to PDFOutput:
1.  **Create a blank document from scratch** <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.
2.  **Choose an existing document** from your Google Drive <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

After creating or selecting a document, it can be renamed (e.g., "invitation template") <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>. This document will serve as the template for the PDF generation, where specific fields will be replaced with data from Notion <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>. For example, an invitation template might include placeholders like `customer name` and `salutation` <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.

### Connecting a Notion Database

The next step involves connecting a Notion database to PDFOutput. This requires authentication with Notion credentials <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.

If a database is not yet created, you will need to:
1.  Open your Notion account <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.
2.  Create a new page and select the "Table" option <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.
3.  Rename the table (e.g., "invitation list") <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>.
4.  Add necessary columns (properties) such as "Name", "Salutation", and "Customer Name" <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>.
5.  Populate the database with your data <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.

Once the database is set up in Notion, return to PDFOutput. The newly created database should appear, allowing you to select it and grant access <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>. If new columns are added to the Notion database later, click "refresh properties" in PDFOutput to sync them <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>. This process demonstrates [[setting_up_notion_database_for_pdf_document_templates | setting up a Notion database for PDF document templates]].

## Mapping Notion Properties to Google Doc Placeholders

This is the core of [[customizing_notion_templates | customizing Notion templates]] for PDF generation, specifically [[using_notion_database_and_templates_for_pdf_generation | using Notion database and templates for PDF generation]].

1.  In PDFOutput, click on a Notion database property (e.g., "Salutation") to copy its value <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>.
2.  Navigate to your Google Document template within PDFOutput.
3.  Highlight the corresponding placeholder text (e.g., "Mr") <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.
4.  Paste the copied Notion property value into the placeholder <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>.
5.  Repeat this for all dynamic fields, such as "customer name" <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.

The system will then replace these placeholders with the actual data from each row in your Notion database during PDF generation <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>. This highlights [[connecting_notion_database_and_templates_to_pdf_output | connecting Notion database and templates to PDF output]].

## Generating PDFs

Once the template is prepared and the database is connected, click the "Export PDF" button <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>. A Google authentication step may be required <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>. After authentication, PDFOutput will process each row of the Notion database and generate a separate PDF document for each entry, automatically downloading them <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>. This effectively demonstrates [[using_pdf_output_with_notion_templates | using PDF Output with Notion Templates]].

### Example Output

For a Notion database with entries for Mr. Vikash, Mr. Sanat, and Mrs. Satabdi, three distinct PDF invitation documents will be generated, each personalized with the correct salutation and name <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>.

## Advanced Considerations

*   **Connected Databases**: If your primary Notion database is linked to other databases, ensure you approve access to all connected databases when setting up the Notion integration <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.
*   **Pre-existing Templates**: PDFOutput offers a library of pre-made templates (e.g., invoice templates) <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>. Users can either:
    *   Make a copy of the template directly into their Google workspace <a class="yt-timestamp" data-t="00:07:46">[00:07:46]</a>.
    *   Copy all content from the template (Ctrl+A, Ctrl+C) and paste it into a new blank Google Document <a class="yt-timestamp" data-t="00:07:53">[00:07:53]</a>.
    This functionality is part of [[creating_notion_templates_and_databases_for_pdf_generation | creating Notion templates and databases for PDF generation]].
*   **Search and Sort Properties**: PDFOutput includes features to search for specific properties in your Notion database and to sort values for easier management <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>.

This detailed process outlines [[setting_up_notion_templates_and_databases_for_pdf_generation | setting up Notion templates and databases for PDF generation]] for efficient PDF customization.

If you have any questions, you can reach out to notionforuse@gmail.com <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.