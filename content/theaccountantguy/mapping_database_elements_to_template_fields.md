---
title: Mapping database elements to template fields
videoId: r6IYxPK0iz8
---

From: [[theaccountantguy]] <br/> 

This article explains how to [[mapping_database_elements_to_template_placeholders_in_pdfoutput|map database elements to template placeholders]] to generate professional PDF documents in bulk using a Notion template and a Notion database with PDFOutput.com <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>.

## Template and Database Structure

A professional invoice template is used as an example <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. In this template, elements that need to be dynamically populated are defined within curly braces `{{ }}` <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.

For instance, placeholders like `{{client name}}`, `{{client company}}`, and `{{client address}}` are used <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.

A Notion database is then created with corresponding fields that contain the exact same information, such as "Client Name", "Client Company", and "Client Address" <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. For every element in the database, there is a corresponding element in the template enclosed in curly braces <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. These elements are then replaced by data from the database to generate PDF documents in bulk <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.

## Connecting Notion Database and Templates

The process involves using PDFOutput.com <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.

1.  **Log In:** Access PDFOutput.com and log in <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.
2.  **Duplicate Template and Database:** Before [[connecting_notion_database_and_templates|connecting a database and template]], you must copy them to your local Notion workspace <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.
    *   Navigate to the "Templates" section in PDFOutput.com <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.
    *   Search for the desired template (e.g., "invoice") <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.
    *   Click on the provided database link and template link <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.
    *   In the new tabs that open, click the "Duplicate" option (usually in the top right) for both the template and the database <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.
    *   Select your Notion workspace to duplicate them to <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>. This will add the template and database to your private Notion workspace <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>, <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.
3.  **Add to PDFOutput:** Once duplicated, add them to PDFOutput.
    *   Click "Add database" or "Add template" in PDFOutput <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.
    *   Select your Notion workspace and then select the specific template and database pages you just duplicated <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>, <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.
    *   Allow access, and PDFOutput will load both the database and the template <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.
    *   You can define a connection name, such as "invoice template" <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.

## Customizing and Mapping Data Fields

After [[notion_template_and_database_integration|Notion template and database integration]], PDFOutput will automatically attempt to map the database properties to the template elements <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.

*   **Automatic Mapping:** If the names used in the database properties exactly match the names inside the curly braces in the template (e.g., "Client Name" in the database and `{{client name}}` in the template), the mapping will occur automatically <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>.
*   **Manual Mapping:** If the names differ, the mapping will not be automatic, and an unmapped element will appear with a gray icon <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>. You will need to click on it and search for the correct corresponding element to map it manually <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.

Once all elements are correctly mapped, you can click "Create PDF" to generate documents in bulk <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>. For example, three PDF documents can be generated from three rows in the database <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>.

### Customization Tips

*   The template is entirely customizable <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>.
*   Ensure that any data you want to pull from the database is placed inside curly braces in the template, using the exact same name as the corresponding database field <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>. This ensures automatic mapping <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>.
*   If using relational properties in the database (where one database field is connected to another database), ensure all related databases are also connected during the setup process <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>.
*   After the initial connection, you can manage and regenerate PDFs using the "Connections" sidebar option without redefining the template and database every time <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>.