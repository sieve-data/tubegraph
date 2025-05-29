---
title: Integrating databases with PDF templates
videoId: hfHjnNxqo4o
---

From: [[theaccountantguy]] <br/> 

[[integration_with_pdf_output_com_for_document_generation | PDF output.com]] facilitates [[generating_pdf_documents_for_business_needs | generating PDF documents]] in bulk by [[integrating_databases_with_templates | integrating databases with PDF templates]], specifically using Notion pages and Notion databases to populate pre-designed templates <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>.

## Template and Database Structure

A typical template, such as a purchase order, includes fields like purchase order number, date, supplier, and buyer name <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. These fields are defined within curly braces (e.g., `{purchase order number}`) in the template <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>. The content inside these curly braces will be replaced with data from a database <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>.

The accompanying database contains columns with the exact same naming conventions as the template's curly-braced fields, storing values for each row that will be used to generate individual PDF documents <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>. For example, a "purchase order number" column in the database would correspond to the `{purchase order number}` field in the template <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.

## [[setting_up_notion_templates_and_databases_for_pdf_generation | Setting Up Notion Templates and Databases for PDF Generation]]

To begin, users need to log in to [[integration_with_pdf_output_com_for_document_generation | PDF output.com]] <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>. The interface prompts users to [[connecting_notion_database_and_template_for_pdfs | connect a Notion database and a Notion template]] <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.

### Acquiring Templates and Databases

1.  Navigate to the "Templates" section in the sidebar navigation on [[integration_with_pdf_output_com_for_document_generation | PDF output.com]] <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.
2.  Search for the desired template, such as "purchase order" <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.
3.  Click on both the database link and the template link provided <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.
4.  Select the "Start with this template" option to duplicate the database and template onto your personal Notion workspace <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.
5.  During the duplication prompt, select your Notion workspace and click "Add to private" <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>. This process should be repeated for both the database and the template <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.

### [[connecting_notion_database_and_template_for_pdfs | Connecting Notion Database and Template]]

Once the templates are duplicated to Notion:
1.  Return to [[integration_with_pdf_output_com_for_document_generation | PDF output.com]] <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.
2.  Click on "click here to add database" or "click here to add template" <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
3.  Grant permission by selecting your Notion workspace and then choosing the specific database and template you duplicated <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>.
4.  Click "Allow access" to authorize the connection <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
5.  If the database and template don't appear immediately, click the "refresh" option <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.

## [[mapping_database_elements_to_pdf_templates | Mapping Database Elements to PDF Templates]]

After [[connecting_notion_database_and_template_for_pdfs | connecting the Notion database and template]], assign a name to the connection (e.g., "purchase order") and click "Next" <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>. The system will then load all database elements and template elements defined within curly braces <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.

### Automatic vs. Manual Mapping

*   **Automatic Mapping**: If the database property names exactly match the naming convention used inside the curly braces in the templates, elements will be automatically mapped <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>.
*   **Manual Mapping**: If names do not match, the system will display elements in gray, requiring manual selection <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>. Users can click on a grayed-out field and choose the corresponding element from the template <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>.

### Customizing Templates

Templates are customizable, allowing users to edit, modify, or make any changes once they have been duplicated <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>. When [[creating_and_exporting_custom_pdf_templates | customizing a template]], ensure that any data intended to be populated from the database is enclosed in curly braces and follows the exact naming convention used in the database <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>.

## Generating PDF Documents

Once the mapping is complete, click "Create PDF" <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>. The system will process each row in the database, generating a separate PDF document for each <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>.

After successful export, users can preview a sample PDF <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>, and then download all generated documents <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>.

## [[managing_connections_and_subscriptions_in_pdf_creation_tools | Managing Connections and Subscriptions]]

### Connections

The "Connections" option allows users to view and reuse previously created connections, such as a "purchase order" connection <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>. Clicking on a saved connection will automatically load the associated database and template, simplifying future document exports <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>.

### Subscriptions

Under the free plan, exported PDF documents will include a "Made with PDF output" watermark <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>. Users can upgrade to a paid subscription to remove the watermark and eliminate limits on PDF generation <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>.

### Settings

The settings section allows users to:
*   Set the default page format, typically A4 <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>.
*   Add more databases and templates beyond the initial setup <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>.

### Relational Properties

If using relational properties in the Notion database, ensure that access is also granted to the related databases during the connection process <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>. This ensures all elements are correctly reflected in the PDF output <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a>.