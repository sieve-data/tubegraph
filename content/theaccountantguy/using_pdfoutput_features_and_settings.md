---
title: Using PDFOutput features and settings
videoId: YbcxEBwvmKU
---

From: [[theaccountantguy]] <br/> 
The [[introduction_to_pdfoutput_tool | PDFOutput]] tool enables users to generate PDF documents in bulk by utilizing a Notion page as a template and a Notion database to supply data for replacement elements within that template <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>.

### Connecting Notion to PDFOutput
To begin using [[introduction_to_pdfoutput_tool | PDFOutput]], users must first define their Notion database and template within the application's interface <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.

#### Creating Notion Templates and Databases
Before connecting, users need to create a Notion database and template page from scratch <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.
1.  **Template Creation**:
    *   Create a new page in Notion <a class="yt-timestamp" data-t="01:01:02">[01:01:02]</a>.
    *   Define content for the template (e.g., an invitation letter) <a class="yt-timestamp" data-t="01:01:20">[01:01:20]</a>.
    *   Crucially, any sections intended to be replaced by data from the database must be enclosed within curly braces (e.g., `{{title}}`, `{{customer name}}`) <a class="yt-timestamp" data-t="01:01:34">[01:01:34]</a>. These placeholders will be dynamically replaced during PDF generation <a class="yt-timestamp" data-t="01:01:51">[01:01:51]</a>. This step is key for [[customizing_document_settings_and_layout_in_pdf_generation | customizing document settings and layout]].
2.  **Database Creation**:
    *   Create another new page in Notion and convert it into a table <a class="yt-timestamp" data-t="02:05:00">[02:05:00]</a>.
    *   Define columns in the database with the *exact same naming convention* as the curly-braced placeholders in the template (e.g., "title", "customer name") <a class="yt-timestamp" data-t="02:12:00">[02:12:00]</a>.
    *   Populate the database with rows of unique information that will be used to generate individual PDFs <a class="yt-timestamp" data-t="02:51:00">[02:51:00]</a>.

#### Authorizing and Selecting Pages in PDFOutput
Once the Notion template and database are ready:
1.  In [[introduction_to_pdfoutput_tool | PDFOutput]], click on "click here to add database" or "add template" <a class="yt-timestamp" data-t="03:11:00">[03:11:00]</a>.
2.  This redirects to a Notion authorization screen where the user selects their Notion account/workspace <a class="yt-timestamp" data-t="03:22:00">[03:22:00]</a>.
3.  Select the specific template and database pages created in Notion <a class="yt-timestamp" data-t="03:31:00">[03:31:00]</a>.
4.  Click "Allow access" to authorize [[introduction_to_pdfoutput_tool | PDFOutput]] to fetch the selected Notion pages <a class="yt-timestamp" data-t="03:46:00">[03:46:00]</a>.

### Mapping Properties and Generating PDFs
After authorization, the selected database and template will be available in the [[using_pdf_output_interface_for_exporting_documents | PDFOutput]] interface <a class="yt-timestamp" data-t="04:07:00">[04:07:00]</a>.
1.  **Connection Naming**: Provide a connection name (e.g., "invitation letter") <a class="yt-timestamp" data-t="04:25:00">[04:25:00]</a>.
2.  **Property Mapping**: The system automatically maps database properties (left side) to the corresponding template elements (right side) based on exact naming conventions <a class="yt-timestamp" data-t="04:36:00">[04:36:00]</a>.
    *   If names do not match exactly, manual mapping is required by selecting the correct element from a dropdown <a class="yt-timestamp" data-t="05:12:00">[05:12:00]</a>.
    *   Options for sorting, searching, and filtering mapped/unmapped properties are available <a class="yt-timestamp" data-t="05:31:00">[05:31:00]</a>.
3.  **PDF Creation**: Click "Create PDF" to initiate the document generation process <a class="yt-timestamp" data-t="05:56:00">[05:56:00]</a>.
4.  **Preview and Download**: Once generated, users can preview a sample PDF <a class="yt-timestamp" data-t="06:30:00">[06:30:00]</a> and then download all generated documents <a class="yt-timestamp" data-t="06:50:00">[06:50:00]</a>. Each row in the database corresponds to a unique PDF document <a class="yt-timestamp" data-t="06:56:00">[06:56:00]</a>. This process outlines [[using_pdf_output_interface_for_exporting_documents | using the PDF Output interface for exporting documents]].

### Additional Features and Settings
The [[introduction_to_pdfoutput_tool | PDFOutput]] sidebar provides access to various features and settings:

*   **Connections**: View and reuse previously created connections <a class="yt-timestamp" data-t="08:22:00">[08:22:00]</a>. Selecting an existing connection automatically loads the predefined database and template, allowing for quick re-generation without needing to create a new connection each time <a class="yt-timestamp" data-t="08:42:00">[08:42:00]</a>.
*   **Templates**: Access a list of predefined templates provided by [[introduction_to_pdfoutput_tool | PDFOutput]] <a class="yt-timestamp" data-t="08:57:00">[08:57:00]</a>. For each template, a database link and template link are provided. Users can duplicate these templates and databases to their own Notion workspace by clicking "Start with this template" <a class="yt-timestamp" data-t="09:15:00">[09:15:00]</a>. This allows users to leverage existing structures to [[customizing_and_exporting_pdf_documents_with_pdf_output_tool | customize and export PDF documents]].
*   **Upgrade**: Information regarding [[understanding_pdfoutput_subscription_plans_and_features | PDFOutput subscription plans]] and features is available here <a class="yt-timestamp" data-t="10:37:00">[10:37:00]</a>. The free plan includes a "Made with [[introduction_to_pdfoutput_tool | PDFOutput]]" watermark and certain limitations <a class="yt-timestamp" data-t="10:39:00">[10:39:00]</a>. Users can upgrade their subscription and activate their plan <a class="yt-timestamp" data-t="10:47:00">[10:47:00]</a>. This section covers [[understanding_pdfoutput_subscription_plans_and_features | understanding PDFOutput subscription plans and features]].
*   **Settings**: This tab allows users to select different page formats for their PDFs <a class="yt-timestamp" data-t="11:01:00">[11:01:00]</a>. Users can also add more templates and databases to their [[introduction_to_pdfoutput_tool | PDFOutput]] account after the initial setup <a class="yt-timestamp" data-t="11:15:00">[11:15:00]</a>. These options are part of [[understanding_pdf_output_settings_and_features | understanding PDF output settings and features]].
*   **Feedback**: Provides a section to submit feedback to the developer <a class="yt-timestamp" data-t="11:30:00">[11:30:00]</a>. This is a [[troubleshooting_and_customization_options_in_pdf_output | customization option in PDF Output]].
*   **Help**: Contains the demonstration video provided for user guidance <a class="yt-timestamp" data-t="11:43:00">[11:43:00]</a>.

Users can also close the sidebar to maximize screen space <a class="yt-timestamp" data-t="11:54:00">[11:54:00]</a>.