---
title: Synchronizing database elements with templates
videoId: n1_fpSFcf3k
---

From: [[theaccountantguy]] <br/> 

This article demonstrates how to synchronize database elements with templates to generate PDF documents using PDFOutput.com. The process involves leveraging a Notion database and a Notion template to create custom documents, such as invoices <a class="yt-timestamp" data-t="00:00:04">00:00:04</a>.

## Getting Started with PDFOutput

1.  **Access PDFOutput**: Navigate to PDFOutput.com and log in <a class="yt-timestamp" data-t="00:00:18">00:00:18</a>.
2.  **Select a Template**: Go to the "Template" section within the interface <a class="yt-timestamp" data-t="00:00:27">00:00:27</a>. For this demonstration, an invoice template is used <a class="yt-timestamp" data-t="00:00:39">00:00:39</a>. Templates can be searched, sorted, or filtered if needed <a class="yt-timestamp" data-t="00:00:47">00:00:47</a>.
3.  **Download/Duplicate Template**: Download the desired template, which opens a new page showing both the template and its associated database <a class="yt-timestamp" data-t="00:01:07">00:01:07</a>.
4.  **Understand Template and Database Structure**:
    *   **Template**: Contains placeholder text elements enclosed in curly braces (e.g., `{{client_name}}`, `{{invoice_number}}`, `{{date}}`, `{{terms}}`) <a class="yt-timestamp" data-t="00:01:41">00:01:41</a>. These placeholders will be replaced by data from the connected database <a class="yt-timestamp" data-t="00:01:52">00:01:52</a>.
    *   **Database**: Features columns with names that exactly match the placeholder text elements in the template (e.g., "Invoice Number", "Date", "Client Name") <a class="yt-timestamp" data-t="00:01:59">00:01:59</a>. Each row in the database corresponds to a separate document to be generated <a class="yt-timestamp" data-t="00:02:09">00:02:09</a>.

## Connecting Notion to PDFOutput

1.  **Duplicate Template to Notion**: Click "Start with this template" to duplicate the chosen template into your Notion workspace <a class="yt-timestamp" data-t="00:02:22">00:02:22</a>. Ensure you select the correct workspace <a class="yt-timestamp" data-t="00:02:36">00:02:36</a>.
2.  **Add Template to PDFOutput Settings**: Go back to PDFOutput and click "Settings" <a class="yt-timestamp" data-t="00:02:57">00:02:57</a>. Select the duplicated Notion template from your workspace and grant access <a class="yt-timestamp" data-t="00:03:01">00:03:01</a>. This authenticates and adds the template to your PDFOutput setup <a class="yt-timestamp" data-t="00:03:36">00:03:36</a>.
3.  **Syncing Elements**: PDFOutput will sync the database and template elements <a class="yt-timestamp" data-t="00:03:53">00:03:53</a>.

### Customization and Mapping

*   **Template Customization**: The template is fully customizable. You can add, delete, or modify content. However, ensure all placeholder text elements remain inside curly braces and that their names precisely match the corresponding column names in your Notion database <a class="yt-timestamp" data-t="00:04:01">00:04:01</a>. For example, if your template has `{{Invoice Number}}`, your database must have a column named "Invoice Number" <a class="yt-timestamp" data-t="00:04:34">00:04:34</a>.
*   [[mapping_notion_database_elements_to_template_placeholders | Mapping Notion database elements to template placeholders]]: Once the template and database are selected, PDFOutput automatically [[mapping_database_elements_to_template_elements | maps]] Notion properties (database columns) to the template's placeholder elements <a class="yt-timestamp" data-t="00:06:02">00:06:02</a>. Successfully [[mapping_database_elements_to_template_placeholders | mapped]] elements are indicated by a green bar <a class="yt-timestamp" data-t="00:06:28">00:06:28</a>.
*   **Manual Mapping**: If any property is not automatically [[mapping_database_elements_to_template_placeholders | mapped]], it will be indicated. You can manually select and [[mapping_database_elements_to_template_placeholders | map]] it by searching for the corresponding element <a class="yt-timestamp" data-t="00:06:32">00:06:32</a>.

## Generating PDF Documents

1.  **Export**: After confirming all elements are [[mapping_database_elements_to_template_placeholders | mapped]], click "Export" <a class="yt-timestamp" data-t="00:07:03">00:07:03</a>.
2.  **PDF Status**: As documents are generated, a "PDF Status" column in your Notion database will automatically be checked for each processed row <a class="yt-timestamp" data-t="00:07:12">00:07:12</a>.
3.  **Preview and Download**: Once successful, you can preview a sample of the generated PDF <a class="yt-timestamp" data-t="00:07:31">00:07:31</a>. You can also "Download All" to get all generated PDF documents <a class="yt-timestamp" data-t="00:08:08">00:08:08</a>. Each PDF output will correspond to a row in your database <a class="yt-timestamp" data-t="00:08:31">00:08:31</a>.

### Important Considerations for [[using_notion_templates_and_databases_for_pdf_creation | Using Notion Templates and Databases for PDF Creation]]

*   **Regenerating Documents**: If you want to regenerate a PDF for a specific row, ensure the "PDF Status" column for that row is unticked in your Notion database before exporting again. Ticked rows will be ignored <a class="yt-timestamp" data-t="00:08:44">00:08:44</a>.
*   **Saved Connections**: Once a connection between a template and database is established and documents are exported, PDFOutput saves this connection. Future generations will automatically load the same database and template, eliminating the need to re-map <a class="yt-timestamp" data-t="00:09:31">00:09:31</a>. This streamlines the process of [[managing_templates_and_databases_within_pdfoutput | managing templates and databases within PDFOutput]] for repeated document generation.
*   **Watermarks**: Free plans may include a watermark. Upgrading to a paid plan removes the watermark <a class="yt-timestamp" data-t="00:09:05">00:09:05</a>.

This process facilitates [[creating_and_using_templates_for_document_generation | creating and using templates for document generation]] by effectively [[using_templates_and_placeholders_for_document_creation | using templates and placeholders for document creation]] and [[connecting_notion_database_and_templates_to_pdf_output | connecting Notion database and templates to PDF output]].