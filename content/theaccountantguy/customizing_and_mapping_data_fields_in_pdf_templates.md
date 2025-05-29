---
title: Customizing and mapping data fields in PDF templates
videoId: hfHjnNxqo4o
---

From: [[theaccountantguy]] <br/> 
The PDFOutput tool enables bulk generation of PDF documents, such as purchase orders, by leveraging a template and a Notion database <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. This process involves [[creating_and_using_templates_for_pdf_generation | creating and using templates]] with specific placeholders and [[using_templates_and_databases_for_pdf_generation | using templates and databases for PDF generation]] by mapping database fields to these placeholders.

### Understanding PDF Templates and Placeholders

A PDF template, such as a purchase order template, includes all necessary details like the purchase order number, date, supplier name, and buyer name <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. For data fields that will change with each generated document, placeholders are used. These placeholders are text items enclosed within curly braces, for example, `{purchase order number}`, `{date field}`, `{supplier name}`, and `{buyer name}` <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>. When a PDF is generated, these curly-braced placeholders are automatically replaced with corresponding data from a linked database <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>.

### Notion Database Structure for Mapping

The Notion database used for PDF generation must contain properties (columns) that correspond to the placeholders in the PDF template <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. For instance, if the template has a `{purchase order number}` placeholder, the database should have a column named "purchase order number" <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>. Each row in the database represents a unique set of data for a single PDF document to be generated <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>. Values are populated in each row for every property that will be mapped <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>.

### [[mapping_database_elements_to_template_placeholders_in_pdfoutput | Mapping Database Elements to Template Placeholders]] in PDFOutput

After connecting your Notion database and template to PDFOutput, the system initiates a mapping step <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>. In this stage, the database properties (displayed on the left) are matched with the template elements (placeholders defined in curly braces) <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.

#### Automatic vs. Manual Mapping

*   **Automatic Mapping**: If the naming convention in your database properties exactly matches the naming convention of the placeholders within the curly braces in your template, PDFOutput will automatically map these elements <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>. This ensures precise data insertion without manual intervention <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.
*   **Manual Mapping**: If the names do not match, the mapping will appear in gray <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>. In this case, you can manually click on the unmatched field and select the correct database property to map it to the template element <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>.

### [[customizing_pdf_templates_for_specific_needs | Customizing PDF Templates]]

The templates provided by PDFOutput are [[customizing_pdf_templates_for_specific_needs | customizable from your end]] <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>. Once a template is duplicated to your Notion workspace, you can edit, modify, or make any desired changes to its layout and content <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>.

#### Key Customization Rules:
*   **Placeholders**: Always ensure that any text you want to be replaced by database data is enclosed in curly braces <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>.
*   **Naming Convention**: Adhere to the exact same naming convention for both the placeholder within the template (e.g., `{Field Name}`) and the corresponding property (column name) in your Notion database (e.g., "Field Name") <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>. This consistency is crucial for successful automatic [[mapping_notion_database_fields_to_pdf_templates | mapping Notion database fields to PDF templates]] <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.

### Handling Relation Properties

If your Notion database uses any relation properties, it is essential to grant access to all related databases during the connection process <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>. When selecting pages for duplication or access, ensure you choose the main database along with any relational databases associated with it <a class="yt-timestamp" data-t="00:09:13">[00:09:13]</a>. Providing access to all linked databases will ensure that all elements are correctly reflected in the generated PDF output <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>.

For specific requirements, users can also use [[custom_pdf_template_requests_and_feedback | custom PDF template requests and feedback]] or create a template from scratch <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>.