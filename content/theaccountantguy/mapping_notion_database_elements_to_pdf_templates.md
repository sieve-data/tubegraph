---
title: Mapping Notion database elements to PDF templates
videoId: XPSQBVl9mKs
---

From: [[theaccountantguy]] <br/> 

PDF Output is a tool that enables users to [[using_notion_as_a_database_for_pdf_generation | generate PDF documents in bulk]] by [[mapping_notion_database_to_pdf_templates | mapping Notion database elements to PDF templates]]. This process involves replacing placeholder text within a Notion template with corresponding data from a Notion database <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>.

## How it Works

The core concept involves creating a Notion template with specific placeholder text, typically enclosed in curly braces (e.g., `{invoice number}`). This placeholder text is then automatically replaced with data from corresponding columns in a Notion database <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>.

### Setting Up the Template and Database

1.  **Prepare Your Notion Template**:
    *   Create a template (e.g., an invoice) in Notion <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>.
    *   Define areas within the template where information from the database will be inserted using placeholder elements enclosed in curly braces, such as `{invoice number}`, `{date field}`, `{due date}`, and `{terms}` <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.
    *   This template can be customized to your requirements by adding, deleting, or modifying elements <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.

2.  **Create Your Notion Database**:
    *   Set up a Notion database where each row contains the data for a single PDF document <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.
    *   Ensure that the column names in your Notion database exactly match the placeholder names used in curly braces within your template <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>. If names differ, manual mapping will be required <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>.
    *   The tool will fetch information from every row of this database to replace the placeholder text in the template <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.

### Using PDF Output

1.  **Access PDF Output**:
    *   Navigate to PDFoutput.com <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.
    *   Log in to access the interface <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.

2.  **Duplicate and Connect Notion**:
    *   From the "Templates" section in PDF Output, select the desired template (e.g., "Invoice Template") <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>. You can use search, sort, and filter options to find templates <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.
    *   Click the "Download" link next to the template to view it <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.
    *   Click "Start with this template" to duplicate both the template and its associated database into your own Notion workspace <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.
    *   In PDF Output settings, click "Click here to add templates" to redirect to your Notion workspace <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.
    *   Choose the Notion account where you duplicated the templates and select the specific pages (template and database) to grant access to PDF Output <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>. Click "Allow Access" <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>.

3.  **Map Database Elements to Template**:
    *   Once connected, select your Notion database (e.g., "Professional Invoice Database") and the corresponding Notion template (e.g., "Invoice Template") within PDF Output <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.
    *   Provide a short name for the generation (up to 20 characters) <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.
    *   The tool will load all Notion properties (database columns) on the left and automatically map them to the template elements on the right <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>.
    *   If any elements are unmapped, they will appear in gray <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>. You can manually map them using search, sort, or filter options <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.

4.  **Generate PDFs**:
    *   Before exporting, check the "PDF Status" column in your Notion database <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>.
    *   Rows with this column checked will *not* be generated. Ensure it is unchecked for all rows you wish to process <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>. This column is unchecked by default upon initial integration <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>.
    *   Click "Export" <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>.
    *   As documents are generated, the "PDF Status" column in Notion will automatically become checked for each processed row <a class="yt-timestamp" data-t="00:07:19">[00:07:19]</a>.
    *   Once successful, you can "Preview Sample" of a generated PDF or "Download All" documents as a ZIP file <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>.

### Managing Generated Documents and Connections

*   **PDF Status Column**: This column in your Notion database indicates whether a PDF has been generated for a specific row. If it's checked, the row will not be regenerated <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>.
*   **Connections**: Once an export process is set up, it creates a "connection" <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>. You can reuse this connection by going to the "Connections" window, selecting your named connection, and simply clicking "Next" to regenerate <a class="yt-timestamp" data-t="00:09:34">[00:09:34]</a>.

### Additional Features

*   **Upgrade Options**: Information about current plan, renewal date, and file downloads are visible <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>. Paid plans remove watermarks from generated PDFs <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>.
*   **Page Format**: Under settings, you can choose different page formats for your PDF documents (e.g., A4, Letter) <a class="yt-timestamp" data-t="00:10:37">[00:10:37]</a>.
*   **Feedback & Help**: Options are available to send feedback or rewatch the demonstration video <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>.