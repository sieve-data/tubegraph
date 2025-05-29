---
title: Using Notion for generating PDF documents
videoId: hfHjnNxqo4o
---

From: [[theaccountantguy]] <br/> 

PDF Output is a tool that allows users to [[generating_pdf_documents_in_bulk_with_notion | generate PDF documents in bulk]] by integrating with [[generating_pdf_documents_using_notion | Notion]] pages and databases <a class="yt-timestamp" data-t="00:00:01">[00:00:01]</a>. This process leverages predefined or custom templates to populate PDF documents with data directly from Notion databases <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>.

## Core Components: Templates and Databases

The system relies on two main components:
1.  **Notion Template Page**: This is a Notion page designed as a template for your PDF document <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. It contains static content along with placeholders for dynamic data.
    *   **Placeholders**: Dynamic data fields are indicated by text enclosed in curly braces, such as `{purchase order number}`, `{date field}`, `{supplier name}`, and `{buyer name}` <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. These placeholders will be replaced with information from your Notion database <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.
2.  **Notion Database**: This database holds the actual data that will populate the templates <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.
    *   **Naming Convention**: The column names in the Notion database must exactly match the placeholder names in the template (e.g., a database column named "purchase order number" corresponds to the `{purchase order number}` placeholder) <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.
    *   **Bulk Generation**: Each row in the database typically corresponds to a unique PDF document that will be generated <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>.

## Steps for PDF Generation

To [[pdf_document_creation_with_notion_and_pdf_output | create PDF documents using Notion and PDF Output]]:

1.  **Log In to PDF Output**: Access the platform via PDFoutput.com <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>.
2.  **Select/Duplicate Templates**:
    *   Navigate to the "Templates" section in the right sidebar <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.
    *   Search for a predefined template (e.g., "purchase order") <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.
    *   Click on both the database and template links provided <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.
    *   Click "Start with this template" to duplicate the database and template into your Notion workspace <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.
3.  **Connect Notion to PDF Output**:
    *   In the PDF Output interface, click "click here to add database" or "click here to add template" <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
    *   Select your Notion workspace and choose the duplicated database and template pages <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.
    *   Click "Allow access" to authorize the connection <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
    *   Once connected, the database and template names will appear on the screen <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>.
4.  **Define Output Name**: Provide a name for the generated PDF documents (e.g., "purchase order") <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>.
5.  **Map Fields**:
    *   The system will load the database properties and template placeholders <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.
    *   If naming conventions are followed, the system will automatically map the fields <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.
    *   If manual mapping is needed, click on the greyed-out fields and select the corresponding database property <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>.
6.  **Generate PDFs**: Click "Create PDF" to start the generation process <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.
7.  **Preview and Download**:
    *   After processing, you can "Preview sample" to review a generated PDF <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>.
    *   Click "Download all" to get all the generated PDF files <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>.

### [[creating_and_using_notion_templates_for_pdfs | Customizing Notion Templates for PDF Generation]]

Users can edit, modify, or make any changes to the duplicated Notion template page <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>. The key is to ensure that any data intended to be replaced from the database is enclosed in curly braces `{}` and that the naming convention matches the database properties exactly <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>.

### Managing Connections and Settings

*   **Connections**: Once a connection is created, it saves the paired database and template for future use <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>. This means you don't need to re-select them every time you want to [[generating_pdf_documents_from_notion_database_rows | generate PDF documents from Notion database rows]] using that specific setup <a class="yt-timestamp" data-t="00:07:24">[00:07:24]</a>.
*   **Upgrade Options**: Free plans include a "Made with PDF Output" watermark on documents <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>. Upgrading to a paid subscription removes the watermark and offers unlimited PDF generation <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>.
*   **Page Format**: The default page format for PDFs is A4 <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>.
*   **Adding More Templates/Databases**: Additional databases and templates can be added via the settings section <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>.
*   **Relation Properties**: If your Notion database uses relation properties, ensure that you also grant access to the related databases during the connection process so all elements reflect correctly in the PDF output <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>.

### Support and Feedback

Users can provide feedback, report difficulties, or ask questions through the feedback option within the application <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>. A help section also includes a video demonstrating how to [[using_predefined_templates_in_notion_for_pdf_generation | use a custom template from scratch]] <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>. For further assistance, you can reach out via email at notionformyuse@gmail.com <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>.