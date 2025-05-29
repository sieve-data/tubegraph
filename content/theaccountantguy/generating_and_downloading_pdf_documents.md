---
title: Generating and downloading PDF documents
videoId: YbcxEBwvmKU
---

From: [[theaccountantguy]] <br/> 

[[utilizing_pdf_output_for_document_generation | PDF Output]] is a tool designed to [[automating_pdf_document_generation | generate PDF documents]] in bulk by leveraging a Notion page as a template and a Notion database to supply data for replacement elements <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This process facilitates [[generating_and_exporting_pdf_documents_for_business | generating and exporting PDF documents for various business needs]] <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>.

## How PDF Output Works

Once logged into [[utilizing_pdf_output_for_document_generation | PDF Output]], users will see sections for Notion database and Notion template. The Notion database defines the data source, and the Notion template defines the structure for PDF generation <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.

### Creating Notion Template and Database

Before using [[utilizing_pdf_output_for_document_generation | PDF Output]], a template and a database must be created in Notion <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.

1.  **Template Creation**:
    *   Create a new page in Notion (e.g., "Invitation Letter Template") <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.
    *   Define the content of the template <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.
    *   Crucially, any sections intended to be replaced by database elements (placeholders) must be enclosed in curly braces, such as `{title}` and `{customer name}` <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>. These placeholders will be replaced by data from the database <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.

2.  **Database Creation**:
    *   Create another new page and select "Table" as the format (e.g., "Invitation Letter Database") <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.
    *   Define columns in the database with the *exact same names* as the placeholders used in the template (e.g., "title" and "customer name") <a class="yt=timestamp" data-t="00:02:30">[00:02:30]</a>. Maintaining the exact naming convention is vital for automatic mapping <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.
    *   Populate the database with unique information for each row, as each row will generate a separate PDF document <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.

### Connecting Notion to PDF Output

1.  In [[utilizing_pdf_output_for_document_generation | PDF Output]], click "click here to add database" or "add template" <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.
2.  Select the specific Notion account and then the template and database pages created earlier <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
3.  Click "Allow Access" to initiate the authorization process, which will automatically fetch the selected database and template into [[utilizing_pdf_output_for_document_generation | PDF Output]] <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>.

### Mapping Properties

1.  Define a connection name (e.g., "Invitation Letter") <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>.
2.  The system will automatically load the template and database and attempt to map database properties (columns) to template elements (placeholders in curly braces) <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.
3.  If the database column names and template placeholder names are identical, the mapping will occur automatically <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.
4.  If names differ, manual mapping is required by selecting the correct elements from dropdowns <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.
5.  Sorting, searching, and filtration options are available for managing properties <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>.

### [[steps_for_downloading_and_exporting_pdfs | Generating and Downloading PDFs]]

Once mapping is complete, click "Create PDF" <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>.
*   The tool will generate PDF documents based on each row in the database, populating the template with the respective data <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>.
*   Users can [[previewing_and_downloading_generated_pdf_files | preview a sample]] document to verify the output (e.g., "Dear Dr. Harry") <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.
*   Clicking "Download All" will download all generated PDF documents as individual files <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>. Each document will reflect the unique information from its corresponding database row (e.g., PDFs for Dr. Harry, Miss Sophia, Mr. S) <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>.

### Key Considerations for PDF Generation

*   **Placeholder Format**: Always enclose placeholder text elements in the Notion template within curly braces (e.g., `{customer name}`) <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>.
*   **Naming Convention**: Use the exact same naming convention for placeholder text in the template and the corresponding column names in the Notion database <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>. If names differ, manual mapping will be required <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.

## Additional Features and Options

### Connections

The "Connections" sidebar option displays all previously created connections, allowing users to quickly load pre-defined database and template settings without re-creating a new connection each time <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>.

### Templates

The "Templates" section provides a list of pre-defined templates that users can utilize. Each template includes a database link and a template link. To use a pre-defined template, duplicate both the database and the template file from the provided links into your Notion workspace <a class="yt-timestamp" data-t="00:09:07">[00:09:07]</a>.

### Upgrade Option

Under the free plan, generated PDFs will include a "Made with [[utilizing_pdf_output_for_document_generation | PDF Output]]" watermark and may have certain limitations. Users can upgrade their subscription plan to remove the watermark and access additional features <a class="yt-timestamp" data-t="00:10:37">[00:10:37]</a>.

### Settings

The "Settings" tab allows users to:
*   Choose different page formats for the generated PDFs <a class="yt-timestamp" data-t="00:11:01">[00:11:01]</a>.
*   Add more templates and databases after the initial setup <a class="yt-timestamp" data-t="00:11:15">[00:11:15]</a>.

### Feedback and Help

*   **Feedback**: Users can provide feedback directly through the "Feedback" section, which sends messages to the developer's inbox for assistance <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>.
*   **Help**: The "Help" section typically contains a demonstration video or guide on using the tool <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>.