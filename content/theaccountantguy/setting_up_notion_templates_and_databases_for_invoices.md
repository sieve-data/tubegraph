---
title: Setting up Notion templates and databases for invoices
videoId: r6IYxPK0iz8
---

From: [[theaccountantguy]] <br/> 

This article outlines how to generate professional invoice PDF documents in bulk using a [[creating_templates_and_databases_in_notion | Notion template]] and a [[creating_and_setting_up_a_notion_database | Notion database]] via PDF output.com <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>.

## Core Concepts

The process involves using a Notion template where specific elements are defined within curly braces (e.g., `{client name}`, `{client company}`, `{client address}`) <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. These bracketed elements act as placeholders that are automatically replaced by corresponding items from a [[setting_up_and_using_databases_in_notion | Notion database]] <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. For every element in the database, there should be a corresponding element in the template enclosed in curly braces <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.

The system will generate individual PDF documents for each row of data present in the database <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.

## Setting up on PDFoutput.com

1.  **Log in to PDF output.com** <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.
2.  **Duplicate Templates and Databases**:
    *   Once logged in, navigate to the "Templates" section <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.
    *   Search for the desired template, such as "invoice" <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.
    *   Click on both the database link and the template link provided <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.
    *   In the new tabs that open, click the "Duplicate" option (top right) for both the template and the database <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.
    *   Select your Notion workspace to duplicate them to your local Notion environment <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>. This will copy the professional invoice template and database into your workspace <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>.

3.  **[[connecting_notion_database_and_templates | Connect Notion Database and Template]]**:
    *   Back on PDF output.com, on the connection details screen, click "Add database" or "Add template" <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.
    *   Select your Notion workspace, then select the duplicated invoice template and database from your Notion pages <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.
    *   Click "Allow access" <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>. The portal will automatically load the [[connecting_a_database_to_a_template_in_notion | connected database and template]] <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.
    *   Define a connection name (e.g., "Invoice Template") <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.
    *   Click "Next" <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>.

4.  **Mapping Properties**:
    *   The system will display database properties on the left, which automatically map to elements in the template if their names match (e.g., `invoice number` in database maps to `{invoice number}` in template) <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
    *   If names do not match, an element will appear with a gray icon <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>. Click on it and manually search for the correct corresponding element to map it <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.

## Generating PDF Documents

1.  After mapping is complete, click "Create PDF" <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.
2.  The software will generate a PDF document for each row in your database <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>.
3.  Once generated, you can preview a sample PDF <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a> or download all the generated documents <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>. The downloaded files will include separate PDFs for each invoice <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>.

## Customization and Best Practices

*   The template is entirely customizable <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>.
*   Ensure that any data you want to pull from the database into the template is placed inside curly braces <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>.
*   Use the exact same name for the property in the Notion database as for the placeholder in the template to enable automatic mapping <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>. If names differ, manual mapping will be required <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>.
*   As you add more items to your database, simply click "generate" to create new PDFs using the existing template <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>.

## PDF output.com Features

*   **Connections**: This section shows all previously created connections for PDF generation <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>. You can reload an existing connection to quickly regenerate documents without re-defining the template and database <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>.
*   **Templates**: Provides a library of pre-added templates for various use cases <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>.
*   **Upgrade**: Allows upgrading your subscription <a class="yt-timestamp" data-t="00:08:59">[00:08:59]</a>. Free plans include a "Made with PDF output" watermark, which is removed in paid tiers <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>.
*   **Settings**: Configure page format (default A4) <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a> and add more databases and templates <a class="yt-timestamp" data-t="00:09:33">[00:09:33]</a>.
*   **Feedback**: Send messages or queries <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>.
*   **Help**: Provides detailed instructions on connecting custom PDF documents and databases to generate PDFs in bulk <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>.

### Handling Relational Properties

If your Notion database uses relational properties (meaning elements in the invoice database are linked to another database), ensure you also allow access to that linked database during the connection setup process <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>. You must select all relevant databases when setting up the connection to ensure smooth document generation <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>.