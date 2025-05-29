---
title: Customizing document settings and layout in PDF generation
videoId: 5lnQYIpvjnM
---

From: [[theaccountantguy]] <br/> 

When generating [[understanding_pdf_output_settings_and_features | PDF documents]] using a [[customizing_notion_templates_for_pdf_documents | Notion page]] and a [[customizing_and_mapping_database_elements_for_pdf_output | database]], several settings and layout options can be customized to achieve the desired output. This process involves configuring the source template, connecting the [[customizing_and_mapping_database_elements_for_pdf_output | database]], and setting output preferences within the [[pdfoutput_software_setup_for_document_generation | PDFOutput]] tool.

## Preparing the Notion Template
To ensure proper data mapping and layout, the [[customizing_notion_templates_for_pdf_documents | Notion page]] serving as the template must be prepared correctly.
*   Information intended to be replaced from the [[customizing_and_mapping_database_elements_for_pdf_output | database]] should be placed inside curly brackets within the [[customizing_notion_templates_for_pdf_documents | Notion template]] (e.g., `{client name}`, `{client company}`, `{client address}`) <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>. These bracketed fields correspond to column names in your [[customizing_and_mapping_database_elements_for_pdf_output | database]] <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.
*   Ensure the [[customizing_notion_templates_for_pdf_documents | Notion page]] is shared and made public for accessibility by the [[pdfoutput_software_setup_for_document_generation | PDFOutput]] tool <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>, <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.

## Connecting Database for Data Mapping
The [[customizing_and_mapping_database_elements_for_pdf_output | database]] provides the dynamic content for the [[understanding_pdf_output_settings_and_features | PDF documents]].
*   The [[customizing_and_mapping_database_elements_for_pdf_output | database]] must be connected to the [[customizing_and_mapping_database_elements_for_pdf_output | Notion API key]] created for the [[pdfoutput_software_setup_for_document_generation | PDFOutput]] integration <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>, <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.
*   If your [[customizing_and_mapping_database_elements_for_pdf_output | database]] uses any relation properties, ensure that the *related* [[customizing_and_mapping_database_elements_for_pdf_output | databases]] are also connected to the same [[customizing_and_mapping_database_elements_for_pdf_output | API key]] for seamless data fetching <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>, <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.

## Output Settings and Customization Options
Once the template and [[customizing_and_mapping_database_elements_for_pdf_output | database]] are linked, you can configure the [[troubleshooting_and_customization_options_in_pdf_output | PDF output settings]]:

### File Naming
*   You can select a specific column from your [[customizing_and_mapping_database_elements_for_pdf_output | database]] to automatically name the generated [[customizing_and_exporting_pdf_documents_with_pdf_output_tool | PDF documents]] <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>. For example, using an "Invoice Number" column ensures each [[customizing_and_exporting_pdf_documents_with_pdf_output_tool | PDF document]] is saved with its corresponding invoice number <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>, <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>.

### Row Selection for Generation
*   **All Rows:** Generate a [[customizing_and_exporting_pdf_documents_with_pdf_output_tool | PDF document]] for every record in the [[customizing_and_mapping_database_elements_for_pdf_output | database]] <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.
*   **Custom Rows:** Specify a range of rows (e.g., 4th through 7th) to generate [[customizing_and_exporting_pdf_documents_with_pdf_output_tool | PDFs]] only for those specific records <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.
*   **Specific Row:** Generate a [[customizing_and_exporting_pdf_documents_with_pdf_output_tool | PDF document]] for a single, particular row <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>.

### Page Layout Settings
The [[pdfoutput_software_setup_for_document_generation | PDFOutput]] tool provides options to adjust the layout of the generated [[customizing_and_exporting_pdf_documents_with_pdf_output_tool | PDF document]] <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.
*   **Paper Size:** Select from various predefined paper sizes to fit your document needs <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>.
*   **Orientation:** Choose between portrait and landscape modes for the document's orientation <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>.
*   **Pages to Print:** Specify whether to print all pages of the Notion template or a subset of pages <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>.

By configuring these settings, users can effectively manage [[managing_invoice_pdf_generation_settings | invoice PDF generation settings]] and tailor the appearance and content of their [[bulk_pdf_document_generation | bulk PDF document generation]].