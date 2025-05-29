---
title: PDF document creation with Notion and PDF output
videoId: n1_fpSFcf3k
---

From: [[theaccountantguy]] <br/> 

This article provides a demonstration of [[generating_pdf_documents_using_notion | how to generate PDF documents]] utilizing a Notion page and template through the PDF Output platform <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. The example focuses on [[generating_pdf_invoices_from_notion | generating PDF invoices]] using a Notion database <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.

## Getting Started with PDF Output

To begin [[how_to_integrate_notion_with_pdf_generation_tools | integrating Notion with PDF generation tools]], users must log in to PDFoutput.com <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. After logging in, the interface displays options, and users should navigate to the "template" section <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.

### Exploring Templates

The template section presents a list of pre-created templates compatible with PDF Output <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. For this demonstration, the "invoices template" is used, downloaded via a specific link <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>. Users can search, sort, or filter for specific templates if needed <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.

### Understanding Template and Database Structure

When a template is opened, it displays both the template itself and a corresponding Notion database <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.

*   **Template**: The template contains placeholder text elements, such as `client name` or `invoice number`, enclosed in curly braces (e.g., `{Client Name}`) <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>. These placeholders will be replaced with data from the connected database <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.
*   **Database**: The connected Notion database contains columns with the exact same names as the placeholder text elements in the template (e.g., "Invoice Number", "Date", "Client Name") <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>. Each row in the database represents a set of data that will populate a unique PDF document <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.

## Setting Up Notion Integration

### Duplicating the Template

To begin [[creating_and_using_notion_templates_for_pdfs | creating and using Notion templates for PDFs]], click "Start with this template" on PDF Output, which prompts you to duplicate the template to your Notion workspace <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>. After selecting your workspace, the template and its associated database will be added to your Notion account <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>.

### Connecting to PDF Output

1.  Return to PDF Output and go to "Settings" <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.
2.  Select the option to "Add template" <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.
3.  Choose the Notion workspace where you duplicated the template <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.
4.  Select the specific template (e.g., "Invoice Generator Template") from the list of available Notion pages <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
5.  Click "Allow access" to authenticate and add the template to your PDF Output setup <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>. The system will then sync the database and template elements <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>.

### Customizing Templates and Databases

Both the Notion template and database are fully customizable <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>. Users can add, delete, or modify elements within the template <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>. It is crucial to ensure that all placeholder text elements within curly braces in the template exactly match the corresponding column names in the Notion database <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>. This precise naming convention is essential for successful PDF generation <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.

## [[generating_pdf_documents_using_notion_databases | Generating PDF Documents]]

1.  In PDF Output, select the Notion database and the corresponding Notion template <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>.
2.  Provide a name for the generation process <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>.
3.  Click "Next" to initiate the syncing of database elements and template <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>.
4.  The system will display the Notion properties (database columns) on the left, automatically mapped to the corresponding template elements (placeholders) <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>. Mapped elements appear in green <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>. If an element is unmapped, you can manually search and map it <a class="yt-timestamp" data-t="00:06:32">[00:06:32]</a>.
5.  Click "Export" to start the document processing <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>.

### Tracking and Output

*   **PDF Status Column**: In your Notion database, a "PDF Status" column will appear <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>. As each document is generated, the corresponding row in Notion will be checked <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a>.
*   **Preview and Download**: Once the export is successful, you can preview a sample PDF or "Download all" generated documents <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>. Each downloaded file will correspond to a row in your Notion database, effectively [[generating_pdf_documents_from_notion_database_rows | generating PDF documents from Notion database rows]] <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>.
*   **Regeneration**: Before generating new PDFs, ensure the "PDF Status" column for the desired rows in your Notion database is *unticked* <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>. Ticked rows will be ignored <a class="yt-timestamp" data-t="00:08:51">[00:08:51]</a>.

## Additional Features and Support

*   **Other Templates**: Users can explore and utilize various other templates available in PDF Output <a class="yt-timestamp" data-t="00:08:58">[00:08:58]</a>.
*   **Watermarks**: The free plan generates documents with a "PDF Output" watermark <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>. To remove the watermark, users must upgrade to a paid plan <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>.
*   **Feedback**: A feedback option is available for users to send messages or suggestions <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>.
*   **Connections**: After an initial export, the connection details (database and template selections) are saved under the "Connections" section, allowing for quick reloading of settings for future generations without remapping <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.
*   **Help Section**: The help section provides a full demonstration on how to set up the system for the first time <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>.
*   For [[troubleshooting_and_support_for_pdf_generation_with_notion | any questions or feedback]], users can reach out via email at notionforuse@gmail.com <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>.