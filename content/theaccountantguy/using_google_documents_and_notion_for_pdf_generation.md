---
title: Using Google Documents and Notion for PDF Generation
videoId: oprL9NBoj8o
---

From: [[theaccountantguy]] <br/> 

The PDF Output tool simplifies the process of [[generating_pdf_documents_in_bulk_using_notion_and_pdf_output | generating PDF documents in bulk]] by leveraging Google Documents as templates and Notion databases to hold the dynamic data for replacement <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. This tool allows users to [[creating_pdf_documents_from_a_notion_database | create PDF documents from a Notion database]] by automatically replacing placeholders in a Google Document template with information from each row of a Notion database <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.

## How PDF Output Works

The general workflow involves three main steps:
1.  Log in to PDF Output <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>.
2.  Add a Google Document to serve as your template <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.
3.  Connect a Notion database to supply the data <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.
4.  Export the PDFs <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>.

### Adding a Google Document Template

Users have two options for adding a Google Document:
*   **Create a blank document**: Start a new Google Document from scratch through the PDF Output interface <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.
*   **Choose an existing document**: Select any document already present in your Google Drive <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

Once a document is created or selected, it can be renamed (e.g., "Invitation Template") <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>. The template should include placeholders, such as `salutation` and `customer name`, which will be replaced by data from the Notion database <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.

### Connecting a Notion Database

To connect a Notion database:
1.  Click "Add Notion Database" in PDF Output <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.
2.  Authenticate and select the specific pages or databases from your Notion account <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.
3.  If a database doesn't exist, you can create a new page in Notion, convert it to a table, and rename it (e.g., "Invitation List") <a class="yt-timestamp" data-t="00:02:53">[00:03:02]</a>.
4.  Once created, select the new Notion database to allow access <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>. The database's properties (columns) will be fetched by PDF Output <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>. If new columns are added in Notion, click "refresh properties" in PDF Output to update them <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.

#### Example Database Setup in Notion
For an invitation template, a Notion database might include columns like "Name" (default), "Customer Name", and "Salutation" <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>.

### Mapping Data and [[generating_pdf_documents_from_notion_database | Generating PDF Documents]]

After both the Google Document template and Notion database are connected:
1.  In the PDF Output interface, select a property (column name) from your Notion database (e.g., "salutation") <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.
2.  Copy the property name.
3.  In the Google Document preview, highlight the corresponding placeholder text (e.g., `Dear Mr. S`) and paste the Notion property. This will insert a tag like `{{salutation}}` <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>.
4.  Repeat for all placeholders (e.g., `{{customer name}}`) <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.

Once mapping is complete, click "Export PDF" <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>. The tool will read each row in the Notion database and [[bulk_pdf_document_generation_using_notion | generate a separate PDF document]] for each, replacing the placeholders with the specific data from that row <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>. The generated PDFs will then be downloaded <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>.

### Advanced Features and Tips

*   **Connected Databases**: If your primary Notion database is linked to other databases, ensure you grant PDF Output access to all connected databases when prompted <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.
*   **Pre-made Templates**: PDF Output provides various pre-made templates (e.g., invoice templates) that users can access <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>. These can be copied directly into your Google Drive or copied and pasted into a blank Google Document <a class="yt-timestamp" data-t="00:07:46">[00:07:46]</a>. This facilitates [[creating_and_using_templates_for_pdf_generation_in_notion | creating and using templates for PDF generation in Notion]].
*   **Search and Sort**: The interface includes search and sorting options for Notion database properties <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>.
*   **Live Editing**: Changes made in PDF Output are reflected in the connected Google Document <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.

For assistance, users can reach out to notionforuse@gmail.com <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.