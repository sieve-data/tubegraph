---
title: Setting up and integrating a Google Document with Notion
videoId: oprL9NBoj8o
---

From: [[theaccountantguy]] <br/> 
This article describes how to set up and integrate a Google Document with Notion using the PDF Output tool to generate bulk PDF documents.

## Introduction to PDF Output
PDF Output is a tool designed to [[generating_bulk_pdf_documents_using_google_docs_and_notion|generate PDF documents in bulk]] by combining a Google Document as a template with a Notion database that holds the data for replacement <a class="yt-timestamp" data-t="00:00:01">[00:00:01]</a>.

## Accessing PDF Output
To begin, log in to PDFoutput.com <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>. Upon logging in, the interface provides options to add a Google Document, add a Notion database, and export PDFs <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>.

## Setting up Your Google Document Template
The first step is to add a Google Document <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. There are two primary methods:
1.  **Creating a Blank Document**: You can start a new, empty Google Document from scratch <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.
    *   Click "Create Document" and select the Google account to connect <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.
    *   A blank document will be created, often named "PDF output new document" <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>.
    *   Rename the document as needed (e.g., "Invitation Template") <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>.
    *   Paste your desired content into the Google Document. This content can include placeholders for data that will be pulled from Notion, such as `Dear Mr. [Customer Name]` <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.
2.  **Choosing an Existing Document**: Alternatively, you can select any existing Google Document from your Google Drive <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.
    *   You can search for specific documents using the search bar <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>.

### Identifying Dynamic Fields
Within your Google Document template, identify the fields that need to be dynamically populated from your Notion database. For example, if generating invitations, you might have placeholders for `salutation` and `customer name` <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.

## Connecting Your Notion Database
After setting up your Google Document template, the next step is to integrate a Notion database <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>.

### Creating a Notion Database
If you don't have one, [[setting_up_a_database_in_notion|create a new database in Notion]]:
1.  Open your Notion account on a separate tab <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.
2.  Click "New Page", select "Table", and rename it (e.g., "Invitation List") <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.
3.  Populate this database with the necessary columns (properties) and rows of data (e.g., "Salutation" and "Customer Name" columns with individual customer entries) <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>.

### Integrating with PDF Output
1.  In PDF Output, click "Add Notion Database" <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.
2.  Connect using your Notion credentials <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.
3.  Select the specific Notion database you want to use (e.g., "Invitation List") from your Notion account <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.
4.  Allow access to this database <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.
5.  **Refresh Properties**: If you add new columns to your Notion database after connecting, click "Refresh Properties" in PDF Output to fetch the newly added properties <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>. This ensures all your data fields are available for mapping <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>.
    *   Note: If your Notion database has connections to other databases, ensure you select all relevant connected databases when approving the database list <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.

## Mapping Fields and Exporting PDFs
Once both the Google Document and Notion database are connected:
1.  **Map Fields**: In PDF Output, click on a property from your Notion database (e.g., "Salutation"). This copies the property name <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>.
2.  Go to your Google Document template and paste the copied property name into the corresponding placeholder <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>. Repeat for all dynamic fields <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.
3.  **Export PDF**: With the template and database ready, click "Export PDF" <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.
4.  Complete any necessary Google authentication <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>.
5.  PDF Output will read each row from your Notion database and generate a separate PDF document, replacing the placeholders with the respective values <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>. The generated PDFs will automatically download <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>.

## Additional Features and Tips
*   **Live Editing**: Changes made to the Google Document template within the PDF Output interface are reflected live <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.
*   **Pre-made Templates**: PDF Output may offer pre-made templates (e.g., [[using_notion_for_invoice_template_creation|invoice templates]]) <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>. You can either make a copy of these templates to your Google Workspace or copy their content and paste it into a blank document you create <a class="yt-timestamp" data-t="00:07:46">[00:07:46]</a>.
*   **Search and Sorting**: You can search for specific properties and sort values within the PDF Output interface <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>.

For any questions or further assistance, you can reach out to notionforuse@gmail.com <a class="yt-timestamp" data-t="00:08:59">[00:08:59]</a>.