---
title: Mapping Notion database fields to PDF templates
videoId: lCyhl8mofjE
---

From: [[theaccountantguy]] <br/> 

This article describes how to [[integrating_notion_databases_with_pdfoutput | PDFOutput]] can be used to generate [[creating_pdf_documents_with_notion_templates | PDF documents]], specifically lease agreements, by [[mapping_notion_database_fields_to_templates | mapping]] data from a [[creating_templates_and_databases_in_notion_for_pdf_generation | Notion database]] to a [[creating_templates_and_databases_in_notion_for_pdf_generation | Notion page template]] <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>.

## Preparing the Notion Template

A lease agreement [[creating_templates_and_databases_in_notion_for_pdf_generation | template]] is used, which includes details like landlord name and tenant name <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>. This [[creating_templates_and_databases_in_notion_for_pdf_generation | template]] uses placeholder text elements, such as `{{landlord name}}` or `{{tenant name}}`, enclosed in curly braces <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>. These placeholders are designed to be replaced by data from a [[creating_templates_and_databases_in_notion_for_pdf_generation | database]] <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.

## Preparing the Notion Database

A [[creating_templates_and_databases_in_notion_for_pdf_generation | Notion database]] contains the specific values, such as "landlord name," "tenant name," and "street address," that will be used to populate the [[creating_templates_and_databases_in_notion_for_pdf_generation | template]]'s placeholders <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>. Each row in the [[creating_templates_and_databases_in_notion_for_pdf_generation | database]] corresponds to a separate document to be generated <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.

## Connecting Notion to PDFOutput

To begin the [[mapping_notion_database_fields_to_templates | mapping]] process:
1.  Log in to the [[integrating_notion_databases_with_pdfoutput | PDFOutput]] application <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.
2.  Consult the help section to ensure API keys and initial setup are completed <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.
3.  Specify a "connection name" (e.g., "lease agreement") <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.
4.  Select the relevant [[creating_templates_and_databases_in_notion_for_pdf_generation | Notion database]] (e.g., "lease") from the dropdown menu, which displays all databases connected via the API key <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.
5.  Select the corresponding [[creating_templates_and_databases_in_notion_for_pdf_generation | Notion template]] (e.g., "lease template") <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.
6.  Click "next" to initiate the loading and [[mapping_notion_database_fields_to_templates | mapping]] of [[notion_template_and_database_integration | database properties]] and [[notion_template_and_database_integration | template elements]] <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.

## Automatic and Manual Mapping

[[integrating_notion_databases_with_pdfoutput | PDFOutput]] attempts to automatically map [[notion_template_and_database_integration | Notion properties]] from the [[creating_templates_and_databases_in_notion_for_pdf_generation | database]] to the corresponding [[notion_template_and_database_integration | template elements]] if their names match (e.g., "landlord name" in the [[creating_templates_and_databases_in_in_notion_for_pdf_generation | database]] to `{{landlord name}}` in the [[creating_templates_and_databases_in_notion_for_pdf_generation | template]]) <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>.

*   On the left, all [[notion_template_and_database_integration | Notion properties]] from the [[creating_templates_and_databases_in_notion_for_pdf_generation | database]] are listed <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.
*   On the right, the corresponding [[notion_template_and_database_integration | PDF template elements]] are displayed <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.
*   If a field is not automatically mapped, it will appear with a gray color <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>. Clicking on a gray element reveals all available [[notion_template_and_database_integration | properties]], with unmapped ones highlighted in red, allowing for manual selection <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.

> [!TIP]
> Ensure that the naming convention of your [[creating_templates_and_databases_in_notion_for_pdf_generation | Notion database]] columns and your [[creating_templates_and_databases_in_notion_for_pdf_generation | Notion template]] placeholders matches exactly to facilitate automatic [[mapping_notion_database_fields_to_templates | mapping]] <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.

## Exporting and Managing Generated PDFs

Once [[mapping_notion_database_fields_to_templates | mapping]] is complete, click "Export" <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>. [[integrating_notion_databases_with_pdfoutput | PDFOutput]] will then:
1.  Add a "PDF Status" column to your [[creating_templates_and_databases_in_notion_for_pdf_generation | Notion database]] <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>. This column tracks which rows have had PDFs generated <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.
2.  Rows that are unticked in the "PDF Status" column will be processed <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.
3.  As PDFs are generated for each row, a tick mark automatically appears in the "PDF Status" column <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.

After generation, you can:
*   Click "preview sample" to view one of the generated [[creating_pdf_documents_with_notion_templates | PDF documents]] <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>. This sample demonstrates how the [[creating_templates_and_databases_in_notion_for_pdf_generation | database]] information has replaced the template placeholders <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.
*   Click "download all" to download all generated [[creating_pdf_documents_with_notion_templates | PDF documents]] in a single file <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>. Individual PDF files can then be opened and reviewed <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.
*   The "download" option remains available if you need to download the files again later <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>.