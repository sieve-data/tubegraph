---
title: Creating and using templates in Google Docs for bulk document generation
videoId: oprL9NBoj8o
---

From: [[theaccountantguy]] <br/> 

[[using_pdf_output_com_to_create_bulk_pdf_documents | PDF output]] is a tool designed to [[generating_bulk_pdf_documents_using_google_docs_and_notion | generate PDF documents in bulk]] <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. It achieves this by utilizing a [[creating_and_using_templates_for_document_generation | Google document as a template]] and a [[creating_notion_templates_and_databases_for_pdf_generation | Notion database]] to hold the [[using_templates_and_placeholders_for_document_creation | elements to replace]] within the Google Document <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.

## Getting Started with PDF Output

To begin, users need to log in to PDF output.com <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>. The interface allows for adding a Google Document and a Notion database, after which bulk PDF export can be initiated <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.

## Creating and Managing Google Docs Templates

There are two primary ways to add a Google Document to be used as a template:
1.  **Create a blank document from scratch** <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.
2.  **Choose an existing document** from your Google Drive <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

### Step-by-Step Document Creation/Selection

1.  Click the "create document" button <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.
2.  Select the Google account to connect <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>. A blank document, initially named "PDF output new document," will be created <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.
3.  Rename the document (e.g., "Invitation Template") <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>.
4.  Add content to the Google Document, incorporating [[using_templates_and_placeholders_for_document_creation | placeholders]] for dynamic data. For example, fields like `salutation` and `customer name` can be inserted <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>. These placeholders will later be replaced with data from the Notion database <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>.
    *   *Example:* `Dear {{salutation}} {{customer name}}` <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.

If you already have a document, you can search for it by name in your Google Drive and select it <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>.

## Integrating with Notion Database

To populate the Google Docs template, a Notion database is required. This process involves [[integrating_google_docs_with_notion_database_for_pdf_creation | integrating Google Docs with Notion database for PDF creation]].

### Setting up the Notion Database

1.  Click "add notion database" in PDF Output <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>. This will prompt a connection to your Notion credentials <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.
2.  In Notion, create a new page and select "Table" to create a database (e.g., "Invitation List") <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.
3.  Add columns (properties) to the Notion database that correspond to the placeholders in your Google Docs template (e.g., "salutation," "customer name") <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>.
4.  Populate the Notion database with data for each row <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.
5.  Back in PDF Output, select the newly created Notion database and allow access <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.
6.  If you add new columns in Notion after connecting, click "refresh properties" in PDF Output to fetch them <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.

## Mapping Placeholders and Generating PDFs

Once both the Google Document template and Notion database are connected:

1.  In PDF Output, click on a Notion property (e.g., "salutation") to copy its placeholder <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>.
2.  Paste this placeholder into the corresponding spot in your Google Docs template <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>. Repeat for all placeholders (e.g., "customer name") <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.
3.  Click "export PDF" to begin the [[generating_and_downloading_pdf_documents_in_bulk | bulk PDF generation]] process <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>. You may need to complete a Google authentication step <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>.
4.  The system will read each row from the Notion database and [[using_templates_to_generate_pdf_documents | generate a PDF document]] for each <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>. The generated PDFs will be automatically downloaded <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>.

### Example Output
If the Notion database contained entries for "Mr. Vikash," "Mr. Sanat," and "Mrs. Satabdi," the system would generate three distinct PDF invitation documents, each personalized <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.

## Advanced Features and Tips

*   **Live Editing**: Changes made to the Google Document template are reflected live within the PDF Output interface <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.
*   **Connected Databases**: If your Notion database has connections to other databases, ensure you choose all relevant databases during the Notion connection process to allow for proper data fetching <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.
*   **Pre-built Templates**: [[using_pdf_output_com_to_create_bulk_pdf_documents | PDF output]] provides various pre-built templates (e.g., invoice templates) <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>. You can make a copy of these templates in your Google Workspace or copy their content and paste it into a blank Google Document <a class="yt-timestamp" data-t="00:07:46">[00:07:46]</a>. This streamlines the [[creating_and_managing_pdf_templates_in_google_drive | creating and managing PDF templates in Google Drive]] process.
*   **Search and Sort Properties**: The interface includes search functionality to find specific Notion properties and a sorting window to organize values <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>.

For questions or assistance, you can contact notionforuse@gmail.com <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.