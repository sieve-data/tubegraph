---
title: Replacing placeholder text in templates with database values
videoId: lCyhl8mofjE
---

From: [[theaccountantguy]] <br/> 

This article outlines how to generate PDF documents, such as lease agreements, by replacing placeholder text in a Notion page template with values from a Notion database using PDF output software <a class="yt-timestamp" data-t="00:00:01">[00:00:01]</a>. This process enables [[connecting_notion_databases_and_templates | connecting Notion databases and templates]] to [[personalizing_templates_with_notion_data | personalize templates with Notion data]].

## Template Preparation

A lease agreement template serves as an example, containing details like landlord and tenant names <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. Key information within this template is inserted as placeholder text elements, typically enclosed in curly braces, for instance, `{{landlord name}}`, `{{tenant name}}`, and `{{street address}}` <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. These placeholders are designed to be replaced by dynamic data <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.

## Database Integration

A Notion database stores the actual values for these placeholders, such as landlord name, tenant name, and street address, with each row representing a unique set of data <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>. The system utilizes these values from individual rows to populate the template and substitute the placeholder text elements <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. This is a core component of [[mapping_notion_database_elements_to_templates | mapping Notion Database Elements to Templates]].

## The Process with PDF Output

To begin, users must log into the PDF output platform <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>. It is crucial to follow the setup instructions in the help section, which includes setting up API keys, before generating PDF documents <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.

### Connecting Database and Template

1.  **Name the Connection**: Assign a connection name, e.g., "Lease Agreement" <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.
2.  **Select Database**: Choose the relevant Notion database from a dropdown menu, which lists all databases connected via the API key <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.
3.  **Select Template**: Choose the desired template, such as the lease template, from the template set <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.
4.  **Proceed**: Click "Next" to load the database and template elements <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.

### Mapping Database Properties to Template Elements

The system will then [[automatically_mapping_database_properties_to_template_elements | automatically map database properties to template elements]] if their names match <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>.

*   On the left side, all Notion database properties (e.g., landlord name, tenant name, street address) are listed <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.
*   Corresponding PDF elements (template elements) are mapped to these properties <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>. For example, "landlord name" in the database is mapped to "landlord name" in the template <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>.
*   If a property is not automatically mapped, it will appear in a gray color <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>. Clicking on it will display all available properties, with unmapped ones listed in red, allowing for manual correction <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>. This demonstrates [[mapping_database_properties_to_template_placeholders | mapping database properties to template placeholders]] and [[mapping_notion_database_elements_to_template_placeholders | mapping Notion database elements to template placeholders]].

### Generating PDFs

After mapping, click "Export" <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.

*   A "PDF Status" property will appear in the Notion database <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.
*   The system generates PDFs for any unticked rows <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.
*   Once a PDF is generated for a row, it automatically places a tick mark in the "PDF Status" column <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.

### Preview and Download

*   After generation, a "Preview Sample" option becomes available, allowing users to view a sample PDF with data from a specific row <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>. For example, a sample PDF might show information for "Tom Green" as the landlord and "Sarah Blue" as the tenant, with all relevant details correctly replaced <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.
*   Users can then click "Download All" to download all generated files in one go <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>. The downloaded files will be exact replicas of the agreement template, populated with unique database information <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>.

## Key Considerations

To ensure smooth and automatic mapping, it is essential that the naming convention of the database properties and the template placeholders matches exactly <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>. This process allows users to [[customizing_templates_and_calculating_sales_data | customize templates]] according to their specific use cases <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.

For any questions or further assistance, users can reach out via email <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.