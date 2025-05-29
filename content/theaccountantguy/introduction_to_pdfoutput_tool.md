---
title: Introduction to PDFOutput tool
videoId: YbcxEBwvmKU
---

From: [[theaccountantguy]] <br/> 

[[introduction_to_pdf_output_tool | PDF Output]] is a tool designed to generate PDF documents in bulk <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. It functions by using a Notion page as a template and a Notion database to supply the elements that will replace placeholders in the template <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>.

## Core Functionality

The fundamental process involves:
1.  **Notion Template**: A Notion page acts as the document template <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>.
2.  **Notion Database**: A Notion database holds all the data elements that will be inserted into the template <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>.

## Setting Up PDF Output for Document Generation

Upon logging into [[setting_up_pdfoutput_for_document_generation | PDF Output]], you will see sections for selecting your Notion database and Notion template <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. Before making selections within the tool, you need to create these components in Notion <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.

### Creating a Notion Template

To create a template in Notion:
1.  Open your Notion dashboard and create a new page <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.
2.  Give the page a name (e.g., "Invitation Letter Template") and set it to full width mode <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.
3.  Define the content of your template. Crucially, any sections intended to be replaced by data from your database must be enclosed in curly braces, for example, `{Title}` or `{Customer Name}` <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>. These curly-braced sections are placeholder elements <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>.

### Creating a Notion Database

To create a database in Notion:
1.  Create a new page and select "Table" as the type <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.
2.  Name the database (e.g., "Invitation Letter Database") <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.
3.  Define columns in the database with the *exact same naming convention* as the placeholder elements in your template <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>. For example, if your template uses `{Title}` and `{Customer Name}`, your database should have columns named "Title" and "Customer Name" <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>.
4.  Populate the database with rows of unique information for each document you wish to generate <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.

### Connecting Notion to PDF Output

Once your template and database are ready in Notion:
1.  In [[utilizing_pdf_output_for_document_generation | PDF Output]], click to add your database or template <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.
2.  You will be redirected to Notion to select the specific pages (your template and database) you intend to use <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>. Ensure you select the correct Notion account/workspace <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
3.  After selecting your template and database, click "Allow access" to authorize [[using_pdf_output_for_document_generation | PDF Output]] to fetch them <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>.
4.  [[using_pdf_output_tool_for_bulk_pdf_generation | PDF Output]] will automatically sync the database and template <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
5.  Provide a connection name (e.g., "Invitation Letter") and click "Next" <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>.

### Mapping Properties

In the next section, you will map database properties to template placeholders <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>.
*   The left side displays your database properties (e.g., "Customer Name", "Title") <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.
*   The right side shows the corresponding elements from your template that were defined inside curly braces <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>.
*   If the naming conventions are exact, [[features_of_pdfoutput_tool | PDF Output]] will automatically map them <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>.
*   If there are any naming differences, you may need to manually select the correct mapping for each element <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.
*   Sorting, searching, and filtering options are available to help manage properties <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.

### Generating and Downloading PDFs

1.  Once mapping is complete, click "Create PDF" <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>.
2.  [[using_pdfoutput_tool_for_bulk_pdf_generation | PDF Output]] will process and generate the PDFs, one for each row in your database <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>.
3.  You can preview a sample document to ensure it's generated correctly <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.
4.  Click "Download All" to download all the generated PDF documents <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>. Each PDF will contain the template content with the unique data from each corresponding database row <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>.

### Important Notes for Setup

*   Always enclose placeholder text elements in your Notion template inside curly braces (e.g., `{Placeholder}`) <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>.
*   Use the exact same naming convention for your database column names as you use for the placeholder text in the template <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>. If names differ, manual mapping will be required <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.

## Additional Features and Settings

[[features_of_pdfoutput_tool | PDF Output]] includes several other features accessible via the sidebar:
*   **Connections**: View and re-use previously established connections between Notion databases and templates, allowing you to generate documents without setting up a new connection every time <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>.
*   **Templates**: Access pre-defined templates with associated database and template links. You can duplicate these directly into your Notion workspace to start using them <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>.
*   **Upgrade**: Information on subscription plans. The free plan includes a "Made with [[utilizing_pdf_output_for_document_generation | PDF Output]]" watermark and certain limitations <a class="yt-timestamp" data-t="00:10:39">[00:10:39]</a>.
*   **Settings**: Customize page format options (e.g., A4, Letter) <a class="yt-timestamp" data-t="00:11:01">[00:11:01]</a>. This section also allows you to add more templates and databases after your initial setup <a class="yt-timestamp" data-t="00:11:10">[00:11:10]</a>.
*   **Feedback**: Submit feedback directly to the developer <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>.
*   **Help**: Access the demonstration video for guidance <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>.