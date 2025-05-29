---
title: Connecting Notion databases and templates for PDF creation
videoId: hfHjnNxqo4o
---

From: [[theaccountantguy]] <br/> 

This guide explains how to use Notion pages and databases to [[generating_pdf_documents_from_notion_database | generate PDF documents]] in bulk, specifically using a purchase order example with PDF output.com <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>.

## Template and Database Setup

To [[generating_pdf_documents_from_notion_database | generate PDF documents]], you will need both a template and a database in Notion <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>.

### Understanding the Template
The template contains relevant details like purchase order number, date, supplier, and buyer name <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. Key fields that will be replaced by database information are enclosed in curly braces, for example, `{{purchase order number}}` <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. These "curly brace" items are filled automatically from the database <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.

### [[setting_up_notion_databases_for_pdf_generation | Setting up Notion Databases]]
The Notion database holds the data that will populate the template fields <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. The database property names (column headers) must match the exact naming convention of the fields within the curly braces in your template <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. Each row in the database will correspond to a separate PDF document generated <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

### Customizing Templates
The entire template is customizable; you can edit or modify it after duplication <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>. Remember to keep any data fields you want to pull from the database inside curly braces and use the exact same naming convention in both the template and the database <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>.

## [[connecting_notion_databases_via_api | Connecting Notion Databases via API]] to PDF Output
The process involves logging into PDF output.com and [[connecting_notion_databases_and_templates | connecting your Notion database and template]] <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.

1.  **Log in to PDF output.com** <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.
2.  **Access Templates:** Head to the "Template" section in the sidebar navigation <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.
3.  **Search for Template:** Search for your desired template, e.g., "purchase order" <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.
4.  **Duplicate Template and Database:** Click on the database and template links provided <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>. Then, click "Start with this template" to duplicate them to your Notion workspace <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>. Select your Notion workspace and click "Add to private" <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>.
5.  **Add to PDF Output:** Once duplicated, go back to PDF output.com and click "Click here to add database" or "Click here to add template" <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.
6.  **Grant Notion Access:** Select your workspace and choose the specific database and template you just duplicated <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>. Click "Allow access" <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
    *   If using Notion relation properties in your database, ensure you also grant access to the related databases during this step <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>.
7.  **Verify Connection:** After authentication, both the database and template should appear on the PDF output screen <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>. If they don't, click the refresh button <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>.

## [[mapping_and_managing_data_fields_between_notion_database_and_pdf_templates | Mapping Data Fields]]
After [[connecting_notion_databases_and_templates | connecting your Notion database and template]], you'll proceed to [[mapping_and_managing_data_fields_between_notion_database_and_pdf_templates | map data fields]]:

1.  **Name the Connection:** Define a name for this connection, e.g., "purchase order" <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>.
2.  **Review Mappings:** The system will load all database properties and template elements (those within curly braces) <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.
    *   **Automatic Mapping:** If your database property names exactly match the template field names, the elements will map automatically <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.
    *   **Manual Mapping:** If names don't match, the mapping will appear in gray <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>. You'll need to manually select the correct database element to map to the template field <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.

## [[creating_pdf_documents_from_a_Notion_database | Creating PDF Documents]]
Once fields are mapped, you can [[creating_pdf_documents_from_a_Notion_database | create PDF documents]]:

1.  **Generate PDFs:** Click "Create PDF" <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>. The tool will process all documents based on the rows in your database <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
2.  **Preview and Download:** After successful export, you can "Preview sample" to view a generated PDF <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>, and then "Download all" to get all generated files <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>.

## Managing Connections and Settings

### Reusing Connections
Under the "Connections" option, you can see all previously created connections <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>. Clicking on a saved connection will automatically load the associated database and template, allowing you to proceed directly to generation without re-selecting them <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>.

### Subscription Options
The free plan includes a "Made with PDF output" watermark on exported documents <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>. Upgrading to a paid subscription removes the watermark and any limits on PDF generation <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>.

### Page Format
In "Settings," the default page format for PDFs is A4 <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>. You can also add more databases and templates from this section <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.

### Support
*   **Feedback:** Use the "Feedback" option to report issues or provide suggestions <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>.
*   **Help:** The "Help" section includes a video demonstrating how to use custom templates from scratch, if you prefer not to use predefined ones <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>.
*   **Contact:** For further assistance, you can reach out via email at notionformyuse@gmail.com <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>.