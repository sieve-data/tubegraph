---
title: Integrating databases with templates
videoId: n1_fpSFcf3k
---

From: [[theaccountantguy]] <br/> 

This article demonstrates how to [[using_notion_for_templates_and_databases | utilize a Notion page and a Notion template]] to generate PDF documents, using an invoice template as an example <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. The process involves [[connecting_notion_databases_with_templates | connecting a Notion database]] to a template via the PDFOutput.com platform <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>.

## Getting Started with PDF Output

To begin, users need to log in to PDFOutput.com <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. Upon logging in, an interface appears, prompting users to navigate to the "template" section <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>.

### Selecting a Template

The "templates" section displays a list of pre-created templates compatible with PDF Output <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. For this demonstration, the "invoices template" is used <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>. Users can download a specific template by clicking its download link <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. Search, sorting, and filter options are available to find specific templates <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.

## Understanding Template and Database Structure

After selecting a template, a new page opens, displaying both the template and its corresponding database <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.

### Template Elements

The template, such as an invoice, contains placeholder text elements enclosed within curly braces (e.g., `{{client name}}`, `{{invoice number}}`, `{{date}}`, `{{terms}}`, `{{due date}}`) <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>. These placeholders will be replaced by data from the connected database <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.

### Database Columns

The associated [[managing_sales_data_with_databases | database]] contains columns with the same names as the placeholder elements in the template (e.g., "Invoice Number", "Date", "Client Name", "Client Company", "Client Address") <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>. Each row in the database represents a distinct record (e.g., an invoice) whose values will populate the corresponding placeholders in the template <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.

## Integrating Notion with PDF Output

The next step involves [[linking_databases_and_creating_templates_in_notion | linking the Notion template]] to the PDF Output platform.

### Duplicating the Template to Notion

1.  Click the "start with this template" option on PDFOutput.com <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.
2.  This prompts the user to duplicate the template to their Notion workspace <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.
3.  Select the desired Notion workspace from the dropdown <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>.
4.  Click "add to private" to add the template to the Notion workspace <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>. The duplicated template, including the invoice database, will now appear in Notion <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.

### Adding the Template to PDF Output Settings

1.  Return to PDF Output and navigate to the "settings" section <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.
2.  Click "add the template" <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.
3.  Select the Notion workspace where the template was duplicated <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.
4.  Click "select pages" and choose the "invoice generator template" <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
5.  Click "allow access" to authenticate the template <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>. Once successful, the template is added to the PDF Output setup <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>.

### Customizing and [[mapping_notion_database_to_templates | Mapping Notion Database to Templates]]

The template is fully customizable; users can add, delete, or modify elements <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>. It's crucial that any placeholder text elements in curly braces have exact matching names as the columns in the Notion database <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>. This ensures correct [[mapping_database_elements_to_template_naming_conventions | mapping of database elements to template naming conventions]] during PDF generation <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>.

Once synced, PDF Output displays "notion properties" (database column names) on the left, and these are automatically [[mapping_database_elements_to_template_placeholders | mapped to the template's placeholder elements]] <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>. Mapped elements are shown in green <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>. If an element is not mapped, it can be manually selected and mapped using the search, sort, or filter options <a class="yt-timestamp" data-t="00:06:32">[00:06:32]</a>.

## Generating PDF Documents

With the database and template mapped, PDFs can be generated.

### Exporting and Downloading

1.  Select the database and the professional invoice template <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.
2.  Provide a name for the output <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>.
3.  Click "next" to start syncing the database and template elements <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>.
4.  Click "export" to begin processing the documents <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>.

While processing, a "PDF Status" column in the Notion database will automatically become checked as each document is generated <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>. After successful export, users can preview a sample document <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>. The sample will reflect the data from the first row of the database <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>. All generated PDFs can be downloaded by clicking "download all" <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>.

### Important Considerations for Regeneration

*   Before regenerating an output, ensure the "PDF Status" column in the Notion database is *unticked* for the relevant rows <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>.
*   If a row's "PDF Status" is ticked, it will be ignored during the generation process <a class="yt-timestamp" data-t="00:08:51">[00:08:51]</a>.

## Additional Features

*   **Template Library:** Users can explore and utilize other templates available on the platform <a class="yt-timestamp" data-t="00:08:58">[00:08:58]</a>.
*   **Watermark:** On the free plan, generated templates will include a "PDF Output" watermark; upgrading to a paid plan removes this <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>.
*   **Connections:** After an initial export, the connection settings (database and template mapping) are saved <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>. This allows users to quickly reload the same setup without re-mapping <a class="yt-timestamp" data-t="00:09:39">[00:09:39]</a>.
*   **Help Section:** A detailed demonstration on setting up the integration for the first time is available <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>.
*   **Feedback:** Users can provide feedback or send messages to notionforuse@gmail.com <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>.