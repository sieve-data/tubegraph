---
title: Automatically mapping database properties to template elements
videoId: lCyhl8mofjE
---

From: [[theaccountantguy]] <br/> 

This tutorial demonstrates how to use PDF Output to generate PDF documents, such as lease agreements, from a Notion database and Notion page. <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a> The process involves using a template with placeholder text and a database containing the values to [[replacing_placeholder_text_in_templates_with_database_values | replace those placeholders]]. <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a> The tool then [[mapping_database_properties_to_template_placeholders | automatically maps database properties to template elements]] to generate the PDFs.

## Template and Database Structure

A lease agreement template is used, which includes details like landlord name, tenant name, and street address. <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a> Within this template, specific information is designated as placeholder text elements, enclosed in curly braces (e.g., `{landlord name}`, `{tenant name}`, `{street address}`). <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>

Correspondingly, a Notion database contains the actual values for these placeholders, with properties like "landlord name," "tenant name," and "street address." <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a> These values from each row of the database will be imported into the template to [[replacing_placeholder_text_in_templates_with_database_values | replace the placeholder text elements]]. <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>

## Initial Setup

Before generating documents, users need to log into PDF Output. <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a> It is essential to visit the "Help" section to follow the tutorial on setting up PDF Output, including configuring API keys. <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>

## Connecting Notion Databases and Templates

1.  **Define Connection Name**: After setup, specify a connection name (e.g., "Lease Agreement"). <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>
2.  **Select Database**: From the dropdown menu, choose the relevant Notion database connected via API key (e.g., "Lease"). <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>
3.  **Select Template**: Similarly, select the corresponding template (e.g., "Lease Template"). <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>
4.  **Proceed**: Click "Next." <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>

## Automatic Mapping of Elements

Upon proceeding, the tool loads the database properties and template elements. <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a> It then automatically [[mapping_notion_database_elements_to_template_placeholders | maps these elements to each other]] if their names match. <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>

*   **Notion Properties**: On the left side, all Notion properties from the database (e.g., "landlord name," "tenant name," "street address") are listed. <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>
*   **PDF Elements**: Correspondingly, the PDF template elements are mapped to these properties. <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a> For example, "landlord name" in the Notion database is mapped to "landlord name" in the template. <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>
*   **Unmapped Elements**: If an element is not automatically mapped, it will appear in gray. Clicking on it reveals all properties, with unmapped ones listed in red, allowing for manual mapping. <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>

## Generating PDF Documents

1.  **Export**: After verifying the mappings, click "Export." <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>
2.  **PDF Status Column**: A "PDF status" column appears in the Notion database. <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a> This column indicates which rows are generated; unticked rows are processed, and a tick mark is added once a PDF is generated for that row. <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>
3.  **Preview and Download**:
    *   Once generation is complete, a "Preview Sample" option allows viewing a single generated PDF. <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a> The preview will show how the database values (e.g., Tom Green as landlord, Sarah Blue as tenant) have [[replacing_placeholder_text_in_templates_with_database_values | replaced the placeholders in the template]]. <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>
    *   Clicking "Download All" downloads all generated PDFs in a single go. <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>

## Best Practices

*   **Customization**: Users can [[customizing_and_mapping_database_elements_for_pdf_output | customize the template]] and database as needed. <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>
*   **Naming Convention**: Ensure that the naming convention between the database properties and the template placeholders matches exactly. <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a> This ensures the automatic [[mapping_and_managing_data_fields_between_notion_database_and_pdf_templates | mapping of data fields]] works smoothly. <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>
*   **Re-download**: Files can be re-downloaded if needed. <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>
*   **Help Section**: Always refer to the "Help" section for preliminary setup instructions. <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>