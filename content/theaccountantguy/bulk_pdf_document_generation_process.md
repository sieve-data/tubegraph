---
title: Bulk PDF document generation process
videoId: r6IYxPK0iz8
---

From: [[theaccountantguy]] <br/> 

The [[bulk_pdf_generation_process | bulk PDF document generation process]] enables the creation of professional PDF documents in bulk by utilizing a Notion template and a Notion database <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. This method is particularly useful for generating standardized documents like invoices <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>.

## Core Components

The process relies on two main components:

### Notion Template
A professional template defines the layout and structure of the document <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. Elements within curly braces `{{ }}` in the template act as placeholders that will be replaced by corresponding data from the Notion database <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. Examples include `{{client name}}`, `{{client company}}`, and `{{client address}}` <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.

### Notion Database
A Notion database holds the specific information for each document to be generated <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. Each row in the database typically represents one document <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>. The database properties (column headers) should ideally match the names of the placeholders in the template (e.g., "client name" in the database corresponds to `{{client name}}` in the template) <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>, <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>.

## Bulk Generation Steps

The following steps outline how to generate [[generating_bulk_pdfs_with_database_integration | bulk PDFs with database integration]] using [[pdfoutput_for_bulk_document_generation | PDF Output]]:

1.  **Access and Log In to PDF Output**
    Navigate to [[pdfoutput_for_bulk_document_generation | PDF Output]] at pdfoutput.com and log in to your account <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.

2.  **Duplicate Notion Template and Database**
    Before connecting, copy the desired Notion template and database (e.g., "Professional Invoices" template and its corresponding database) into your local Notion workspace <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>, <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. This is done by clicking the "Duplicate" option found at the top right of the Notion page for both the template and the database <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>. Select your Notion workspace to complete the duplication <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.

3.  **Connect Notion Workspace to PDF Output**
    In [[pdfoutput_for_bulk_document_generation | PDF Output]], on the connection details screen, click "Add Database" or "Add Template" <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>. Select your Notion workspace and then choose the duplicated template and database pages from your Notion workspace <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>, <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>. Grant access to connect them to [[pdfoutput_for_bulk_document_generation | PDF Output]] <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>. Assign a connection name (e.g., "invoice template") <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a> and click "Next" <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>.

4.  **Map Database Properties to Template Elements**
    [[pdfoutput_for_bulk_document_generation | PDF Output]] will automatically reflect all database properties on the left side and attempt to map them to corresponding elements in the template <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>. If the template placeholder names exactly match the database property names, mapping occurs automatically <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>. If names differ, you may need to manually map elements by clicking on the gray icon next to the unmapped property and searching for the correct template element <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>.

5.  **Generate PDFs**
    Once all elements are correctly mapped, click "Create PDF" <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>. The system will then begin [[bulk_exporting_pdf_documents | generating PDF documents]] for each row in your Notion database <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>.

6.  **Preview and Download**
    Upon successful export, you can preview a sample PDF file to ensure accuracy <a class="yt-timestamp" data-t="00:06:12">[00:06:12]</a> or download all generated documents <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>. The downloaded files will include separate PDFs for each entry in the database <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>.

## Customization and Best Practices

*   **Customizable Templates:** The template can be entirely customized to meet specific requirements <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>.
*   **Matching Names:** Ensure that any data you want to pull from the database is enclosed in curly braces in the template and uses the exact same name as the corresponding database property <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>. This enables automatic mapping <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>.
*   **Relational Properties:** If your database uses relational properties connected to other Notion databases, ensure those linked databases are also added and connected during the setup process <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>.

## Additional Features of PDF Output

[[pdfoutput_for_bulk_document_generation | PDF Output]] provides several features to streamline the [[bulk_pdf_generation_from_notion_databases | bulk PDF generation from Notion databases]]:

*   **Connections:** The "Connections" section allows you to view and re-use previously created connections between Notion databases and templates, eliminating the need to redefine them each time <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>.
*   **Templates Library:** A library of pre-added templates is available for various use cases <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>. You can search for specific templates (e.g., "invoice") and access their corresponding database and template links for duplication <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.
*   **Upgrade Options:** For higher tiers of document generation and to remove the "Made with PDF Output" watermark, users can upgrade their subscription <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.
*   **Settings:** The settings window allows defining specific page formats (e.g., A4 size) for the generated PDFs <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>. It also provides an option to add more databases and templates after the initial connection <a class="yt-timestamp" data-t="00:09:33">[00:09:33]</a>.
*   **Custom Templates/Databases:** For [[custom_pdf_document_solutions | custom PDF document solutions]] not found in the template library, detailed instructions are available on how to connect your own custom Notion template and database <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>.
*   **Feedback:** A feedback option is available for sending messages or queries to the support team <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>.