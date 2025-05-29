---
title: Bulk PDF document generation using Notion
videoId: YbcxEBwvmKU
---

From: [[theaccountantguy]] <br/> 

[[generating_pdf_documents_in_bulk_using_notion_and_pdf_output | PDF Output]] is a tool designed to help users [[creating_pdf_documents_from_a_notion_database | generate PDF documents in bulk]] <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. It utilizes a Notion page as a template and a Notion database to hold the elements that will replace placeholders within the template <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>.

## How it Works

Upon logging into [[generating_pdf_documents_in_bulk_using_notion_and_pdf_output | PDF Output]], users will find sections for Notion database and Notion template <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. The process involves defining a Notion database for PDF generation <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a> and selecting a specific template to [[using_notion_templates_for_pdf_generation | generate the PDF document]] <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>.

### Setting Up in Notion

Before capturing the database and template in [[generating_pdf_documents_in_bulk_using_notion_and_pdf_output | PDF Output]], a database and template must be created from scratch in Notion <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.

#### Creating the Notion Template

1.  Create a new blank page in Notion <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.
2.  Give it a name, such as "invitation letter template" <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>.
3.  Set the page to full width mode <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.
4.  Define the content for the template <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.
5.  **Crucially**, sections that need to be replaced by database content must be enclosed in curly braces, e.g., `{title}` and `{customer name}` <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>. These will serve as placeholder elements <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.

#### Creating the Notion Database

1.  Create another new page in Notion <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.
2.  Select the "Table" option to create a database <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.
3.  Name the database, e.g., "invitation letter database" <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.
4.  Define columns with **exact same naming conventions** as the placeholder text in the template (e.g., `title` and `customer name`) <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>. This ensures automatic mapping <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>.
5.  Populate the database with rows of unique information <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.

### Connecting Notion to PDF Output

1.  In [[generating_pdf_documents_in_bulk_using_notion_and_pdf_output | PDF Output]], click "click here to add database" or "add template" <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.
2.  This redirects to Notion where you select the specific Notion account and then the template page and database to be used <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.
3.  Click "Allow access" to authorize the connection <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>.
4.  [[generating_pdf_documents_in_bulk_using_notion_and_pdf_output | PDF Output]] will automatically fetch and display the selected database and template <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
5.  Define a connection name (e.g., "invitation letter") <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>.

### Mapping Properties

1.  After clicking "next", the system loads the template and database <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.
2.  On the left, all database properties (columns) are listed <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>. On the right, the corresponding elements from the template (those in curly braces) are shown <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>.
3.  If naming conventions match, the mapping will happen automatically <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>.
4.  If names differ, you will need to manually select the correct corresponding elements for mapping <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.
5.  Sorting, searching, and filtration options are available for managing properties <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.

### Generating and Downloading PDFs

1.  Once all properties are correctly mapped, click "create PDF" <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>.
2.  The tool will generate PDF documents based on each row of the database, replacing the placeholders in the template with the corresponding data <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>.
3.  A preview sample can be viewed <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.
4.  Click "download all" to save all generated PDF documents <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>. Each row from the database will result in a unique PDF document <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>.

## Key Considerations

*   **Placeholder Syntax**: Always put placeholder text elements inside curly braces in the Notion template (e.g., `{customer name}`) <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>.
*   **Naming Convention**: Use the exact same naming convention for placeholder elements in the template and column headers in the database for automatic mapping <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>.
*   **Watermark and Upgrades**: Free plans include a "made with [[generating_pdf_documents_in_bulk_using_notion_and_pdf_output | PDF Output]]" watermark and certain limitations <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>. Users can upgrade their subscription for more features <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>.
*   **Page Formats**: Different page formats are available under the settings tab <a class="yt-timestamp" data-t="00:11:01">[00:11:01]</a>.

## Additional Features

*   **Connections**: Once a connection is created, it can be saved and reloaded from the "Connections" sidebar <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>. This means you don't need to create a new connection every time <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>.
*   **Predefined Templates**: The "Templates" sidebar provides a list of predefined templates <a class="yt-timestamp" data-t="00:09:07">[00:09:07]</a>, such as a [[generating_boarding_pass_pdf_documents_using_notion | boarding pass template]] <a class="yt-timestamp" data-t="00:09:23">[00:09:23]</a>. Each template comes with a database link and a template link <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>. To use them, you need to duplicate both the database and the template file into your Notion workspace <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a>.
*   **Adding More Templates/Databases**: After initial setup, more templates and databases can be added via the settings tab <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>.
*   **Feedback and Help**: Users can send feedback through the "PDF Feedback" section <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>, and a help section provides demonstrations <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>.