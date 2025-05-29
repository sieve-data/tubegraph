---
title: Customizing PDF Templates with Placeholder Elements
videoId: zrr8DW4PWz0
---

From: [[theaccountantguy]] <br/> 

PDF templates can be extensively customized to generate documents such as payment receipts, by integrating Notion databases with placeholder elements <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. This process leverages placeholder text to dynamically populate PDF documents with data from a Notion database <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.

## Understanding Placeholder Elements

Placeholder elements are specific text segments within a template that are designed to be replaced by actual data from a corresponding database <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.

### Identifying Placeholders
In PDF output templates, placeholder elements are enclosed in curly braces, for example:
*   `{receipt number}` <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>
*   `{receipt date}` <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>
*   `{receipt time}` <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>
*   `{customer name}` <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>
*   `{customer email}` <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>
*   `{amount paid}` <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>
*   `{company address}` <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>
*   `{company email}` <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>

These elements act as dynamic fields that will be filled in during the PDF generation process <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.

### Matching Placeholders to Database Elements
For successful PDF generation, the placeholder text within the template (e.g., `{customer name}`) must precisely match the corresponding column name in your Notion database (e.g., "customer name") <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>, <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>. This ensures that the data is correctly synced and mapped <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.

## Customizing Templates

Templates are highly customizable to fit specific requirements <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>.

### Formatting and Layout
Users can adjust the appearance of the template, including:
*   Making elements bold <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>
*   Adding spacing <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>

The format can be customized as desired, as long as placeholder elements remain correctly enclosed in curly braces <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.

### Workflow for Customization and Generation
1.  **Duplicate the Template**: Start by duplicating the desired template (e.g., "payment receipts PDF generator") to your Notion workspace <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>. If the template is published, use the "Start with this template" option <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.
2.  **Add to PDF Output**: In PDFoutput.com, navigate to settings and click "Add templates" <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>. Select the Notion workspace where the template was duplicated and grant access <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>.
3.  **Select Database and Template**: Choose the Notion database (e.g., "payment receipts database") and the corresponding template (e.g., "payment receipt template") within the PDF output interface <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>.
4.  **Map Elements**: The system will automatically map Notion database properties to the template's placeholder elements if the naming conventions match <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>. If there are mismatches, you can manually select the correct elements <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>. Filter, search, and sort options are available to assist with mapping <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>.
5.  **Export PDF**: Click "Export" to generate the PDF documents <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>. A "PDF status" column will be added to your Notion database, indicating which rows have been generated <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>.
6.  **Review and Download**: Preview a sample generated file or download all generated PDFs <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>. Each generated file corresponds to a specific row in the Notion database, with all placeholder elements correctly replaced <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>.

[[using_templates_and_placeholders_for_document_creation | Using templates]] and [[using_templates_to_generate_pdf_documents | placeholders]] allows for dynamic [[customizing_pdf_documents_using_notion_database_elements | PDF customization]] based on Notion database elements <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. The key to successful generation is to ensure that the [[mapping_database_elements_to_template_placeholders | naming convention of the placeholder elements in the template exactly matches the column names in the database]] <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>. For more information on [[customizing_and_exporting_generated_pdf_files | customizing and exporting generated PDF files]], refer to the additional resources.