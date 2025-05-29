---
title: Customizing PDF templates in Notion
videoId: hfHjnNxqo4o
---

From: [[theaccountantguy]] <br/> 

This article explains how to [[customizing_pdf_templates_with_notion | customize PDF templates]] using Notion pages and databases to [[generating_pdf_documents_with_notion | generate PDF documents in bulk]] via PDF output services <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. The process involves creating a template with placeholder fields and a database with corresponding data.

## Understanding the Template

A PDF template, such as a purchase order template, includes all relevant details like purchase order number, date, supplier, and buyer name <a class="yt-timestamp" data-t="00:17:28">[00:17:28]</a>. Key to [[customizing_notion_templates | customizing Notion templates]] for PDF output are *placeholder items* <a class="yt-timestamp" data-t="00:28:05">[00:28:05]</a>.

*   **Placeholder Fields**: These are items placed inside curly braces (e.g., `{purchase order number}`, `{date field}`, `{supplier name}`, `{buyer name}`) <a class="yt-timestamp" data-t="00:27:06">[00:27:06]</a>.
*   **Purpose**: These curly-braced items will be automatically replaced with data from a Notion database when the PDF is generated <a class="yt-timestamp" data-t="00:38:09">[00:38:09]</a>.

## Preparing Your Notion Database

The Notion database acts as the data source for your PDF documents, working in tandem with the template for [[using_notion_as_a_template_and_database_for_pdfs | generating PDFs]] <a class="yt-timestamp" data-t="00:40:02">[00:40:02]</a>.

*   **Matching Properties**: The database must contain properties (columns) with the exact same names as the placeholder fields defined within the curly braces in your template <a class="yt-timestamp" data-t="00:50:57">[00:50:57]</a>, <a class="yt-timestamp" data-t="01:01:21">[01:01:21]</a>.
*   **Data Rows**: Each row in the database represents a unique PDF document to be generated, with specific values for each property <a class="yt-timestamp" data-t="01:09:07">[01:09:07]</a>, <a class="yt-timestamp" data-t="01:13:00">[01:13:00]</a>.

## Customization and Mapping

The template is fully [[customizing_notion_templates | customizable]], allowing for edits, modifications, and any desired changes once it has been duplicated into your Notion workspace <a class="yt-timestamp" data-t="05:17:15">[05:17:15]</a>, <a class="yt-timestamp" data-t="05:21:09">[05:21:09]</a>.

*   **Editing the Template**: You can modify the layout, add or remove elements, or change the styling of the template <a class="yt-timestamp" data-t="05:18:03">[05:18:03]</a>.
*   **Placeholder Rule**: Always ensure that any text you want to be dynamically populated from the database is enclosed in curly braces <a class="yt-timestamp" data-t="05:25:21">[05:25:21]</a>.
*   **Naming Consistency**: It is crucial to use the exact same naming convention for properties in your database as the placeholder names in your template. This allows for automatic mapping of fields <a class="yt-timestamp" data-t="05:30:38">[05:30:38]</a>, <a class="yt-timestamp" data-t="00:30:17">[00:30:17]</a>, <a class="yt-timestamp" data-t="00:38:12">[00:38:12]</a>.
*   **Manual Mapping**: If the naming conventions do not match, you may need to manually map the database properties to the template fields within the PDF output service <a class="yt-timestamp" data-t="04:47:04">[04:47:04]</a>.

## Key Considerations

*   **Duplicating Templates**: Begin by duplicating predefined templates and databases into your Notion workspace from the PDF output service's template section <a class="yt-timestamp" data-t="01:41:09">[01:41:09]</a>, <a class="yt-timestamp" data-t="02:15:00">[02:15:00]</a>.
*   **Connecting Notion**: Once duplicated, connect your Notion database and template to the PDF output service by granting access <a class="yt-timestamp" data-t="02:47:09">[02:47:09]</a>, <a class="yt-timestamp" data-t="03:04:19">[03:04:19]</a>.
*   **Relation Properties**: If your Notion database uses relation properties, ensure you grant access to all related databases during the connection process so that all linked elements are correctly reflected in the PDF output <a class="yt-timestamp" data-t="09:01:00">[09:01:00]</a>, <a class="yt-timestamp" data-t="09:15:00">[09:15:00]</a>.
*   **Watermarks**: Free plans may include a watermark on generated documents, which can be removed by upgrading to a subscription <a class="yt-timestamp" data-t="07:29:03">[07:29:03]</a>.
*   **Page Format**: The default page format for PDF output is A4 <a class="yt-timestamp" data-t="07:49:15">[07:49:15]</a>.
*   **Adding More Templates**: After the initial setup, additional templates and databases can be added through the settings section <a class="yt-timestamp" data-t="08:04:00">[08:04:00]</a>.

For assistance or specific issues, you can use the feedback option within the service or reach out via email <a class="yt-timestamp" data-t="08:10:00">[08:10:00]</a>, <a class="yt-timestamp" data-t="09:26:00">[09:26:00]</a>.