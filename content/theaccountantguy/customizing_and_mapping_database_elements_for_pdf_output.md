---
title: Customizing and mapping database elements for PDF output
videoId: zrr8DW4PWz0
---

From: [[theaccountantguy]] <br/> 

This guide explains how to generate PDF documents by [[mapping_and_managing_data_fields_between_notion_database_and_pdf_templates | mapping and managing data fields between Notion database and PDF templates]] using a Notion database and a Notion template with PDF Output.

## Getting Started with PDF Output
To begin, log in to PDFoutput.com. This will display the main interface <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.

### Accessing and Duplicating Templates
1.  Click on the "Templates" section within the PDF Output interface <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. This will open a new page listing various templates available for PDF Output <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.
2.  You can use the search option to find a specific document template <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>, or utilize the filter and sorting options <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.
3.  Once you've found the desired template (e.g., "payment receipts PDF generator"), click on its download link <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.
4.  If the template is not yet published to the Notion Gallery, you'll see a "duplicate" option <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>. Click on "Duplicate" and choose the Notion workspace where you want to duplicate it <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>. If it is published, click "Start with this template" <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>. The template needs to be duplicated to a Notion workspace to be used with PDF Output <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.

## Understanding and Customizing Templates
After duplicating, open both the Notion database and the template.

### Placeholder Elements
The template contains predefined elements, with some enclosed in curly braces (e.g., `{receipt number}`, `{customer name}`) <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. These are "placeholder text Elements" that will be replaced by corresponding data from your Notion database <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.

For instance, the `{customer name}` in the template will be replaced by the data from the "customer name" column in your database <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. This applies to all elements like amount paid, company address, company email, etc. <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>.

> ⚠️ **Important:** The exact naming convention within the curly braces in the template **must match** the corresponding column names in your Notion database <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>. This ensures proper synchronization and error-free PDF generation <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.

### Template Customization
You can [[customizing_document_settings_and_layout_in_pdf_generation | customize the template]] to fit your specific requirements directly within Notion <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>. This includes making elements bold or adding spacing <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>. When [[customizing_document_settings_and_layout_in_pdf_generation | customizing document settings and layout in PDF generation]], ensure that placeholder elements you want to replace from the database remain inside curly braces for proper syncing <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.

## Connecting and Mapping in PDF Output
After customizing your Notion template and database, connect them to PDF Output. This involves [[understanding_pdf_output_settings_and_features | understanding PDF output settings and features]] and using the [[using_pdf_output_interface_for_exporting_documents | PDF Output interface for exporting documents]].

1.  Go to PDF Output and click on "Settings" <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>.
2.  Click "Click here to add templates" to add your duplicated template to PDF Output <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.
3.  Choose the specific Notion workspace where you duplicated the template <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>, then select the generated PDF generator file <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>.
4.  Click "Allow access" to enable PDF Output to read your template and database elements <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.

### Selecting Database and Template
Once authentication is successful, you'll need to select your Notion database and template within PDF Output:
1.  From the dropdown menus, select your "payment receipts database" and the corresponding "payment receipt template" <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>.
2.  Give your connection a name (e.g., "payment receipt") and click "Next" <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.

### Automatic and Manual Mapping
PDF Output will load all elements from your database and template. It will [[automatically_mapping_database_properties_to_template_elements | automatically map database properties to template elements]] if their names match <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>.
*   **Notion Properties:** These are your database column names, listed on the left <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>.
*   **Template Elements:** These are the placeholder texts from your template, which PDF Output attempts to map automatically <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>.

If any elements are mismatched or not automatically mapped, they will be indicated <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>. You can manually search for and select the correct corresponding element to map it <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>. The mapping view also includes filter, search, and sorting options <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>.

## Generating PDF Output
Once all elements are correctly mapped, click "Export" <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>.
1.  A "PDF status" column will automatically be added to your Notion database to track which rows have been generated <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>.
2.  As PDFs are generated, the corresponding rows in Notion will be marked as "ticked" <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>.
3.  Upon successful export, you can preview a sample file <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a> or download all generated files <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>. Each generated file corresponds to a row in your Notion database <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>.

This process demonstrates how to use PDF Output to [[customizing_and_exporting_pdf_documents_with_pdf_output_tool | customize and export PDF documents with PDF Output tool]].

## Additional Features and Customization
*   **Connections:** In the "Connection" section, you can view past connections you've created <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>. Clicking on a past connection will automatically load the database and template, allowing you to quickly regenerate documents without re-adding them manually <a class="yt-timestamp" data-t="00:08:05">[00:08:05]</a>.
*   **Multiple Templates:** You can select and manage multiple templates <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>.
*   **Watermark:** Free plans include a PDF Output watermark on generated templates <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>. Upgrading to a paid plan removes the watermark <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>.
*   **Page Format:** Under "Settings," you can change the page format for your PDF output <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>.
*   **Feedback & Help:** A feedback option is available to send messages directly to support <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>. The "Help" section provides a demonstration video to assist with setup <a class="yt-timestamp" data-t="00:08:59">[00:08:59]</a>.