---
title: Using Notion database and templates for PDF generation
videoId: hfHjnNxqo4o
---

From: [[theaccountantguy]] <br/> 

This article describes how to [[using_notion_templates_and_databases_for_pdf_creation | use Notion pages and databases]] with PDF Output.com to [[generating_pdf_invoices_in_bulk_using_a_notion_database | generate PDF documents in bulk]], such as purchase orders <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>.

## Template and Database Structure

To generate PDFs, you'll need a Notion template and a Notion database <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>.

### Notion Template Structure
The template contains placeholders for dynamic data, indicated by items placed inside curly braces (e.g., `{purchase order number}`, `{date field}`, `{supplier name}`, `{buyer name}`) <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>. These placeholders will be replaced with data from your Notion database <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.

The template is fully customizable, meaning you can edit, modify, or make any changes to it once duplicated <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>. Just ensure that any elements intended to be populated from the database remain within curly braces <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>.

### Notion Database Structure
The Notion database holds the data that will populate the template placeholders <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>. The names of the properties in the database must exactly match the naming convention used within the curly braces in your template (e.g., "purchase order number," "date field," "supplier name") <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>, <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>, <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>. Each row in the database will generate a separate PDF document <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

## [[setting_up_notion_templates_and_databases_for_pdf_generation | Setting Up Notion Templates and Databases for PDF Generation]]

### Logging In
Begin by logging into PDFOutput.com <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>.

### Duplicating Templates and Databases
1.  Navigate to the "Template" section in the sidebar navigation <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.
2.  Click on "Templates" to view predefined templates <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>.
3.  Use the search field to find a specific template, such as "purchase order" <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.
4.  Click on the provided database link and template link <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.
5.  On the opened pages, click "Start with this template" to duplicate both the database and the template into your Notion workspace <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>. Select your Notion workspace and click "Add to private" when prompted <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>.

### [[connecting_notion_database_and_templates_to_pdf_output | Connecting Notion to PDF Output]]
After duplicating, return to PDFOutput.com and click "click here to add database" or "click here to add template" <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
1.  Select your Notion workspace <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.
2.  Click "Select pages" and choose the duplicated database and template <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.
3.  Click "Allow access" to authorize the connection <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
4.  Once authenticated, the database and template will appear on the PDF Output screen <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>. If they don't, click the refresh button <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.

## [[generating_pdf_invoices_in_bulk_using_a_notion_database | Generating PDF Documents]]

### Mapping Database Elements
1.  Define a name for the PDF generation process (e.g., "purchase order") <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>.
2.  Click "Next" <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>. The system will load the database properties and the template elements (items inside curly braces) <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.
3.  If the naming conventions between the template and database are exact, the elements will be automatically mapped <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.
4.  If not automatically mapped, elements will appear in gray. You can manually select the corresponding element from the template <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>.

### Creating and Downloading PDFs
1.  Click "Create PDF" <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>. The system will process each row in your Notion database to generate individual PDF documents <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
2.  Once the export is successful, you can "Preview sample" to view one of the generated files <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.
3.  Click "Download all" to download all the generated PDFs <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>. You can click "Download PDF again" if you missed the initial download <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>.

## PDF Output Features

### Connections
The "Connections" option on the right panel shows previously created connections, allowing you to quickly reload a specific database and template without re-entering details <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>. This means you don't need to fill out the database and template information repeatedly for future exports <a class="yt-timestamp" data-t="00:07:24">[00:07:24]</a>.

### Upgrade Options
Free plan exports will include a "Made with PDF Output" watermark <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>. Upgrading to a subscription plan removes the watermark and any limits on PDF generation <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>.

### Settings
*   **Page Format:** The default page format is A4 <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>.
*   **Add More Templates:** You can add additional databases and templates via the settings once your initial connection is established <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>.

### Feedback and Help
*   **Feedback:** If you encounter difficulties or issues, use the feedback option to report them <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>.
*   **Help:** A video is available under the help section demonstrating how to [[creating_notion_templates_and_databases_for_pdf_generation | create a custom template]] from scratch <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>.

## Important Considerations

*   **Naming Conventions:** Always use the exact same naming convention for properties in your Notion database and the corresponding placeholders in curly braces within your template <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>. This ensures automatic mapping.
*   **Relation Properties:** If your database uses any relation properties, ensure you grant access to those related databases during the Notion access selection process so all elements reflect correctly in the PDF output <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>.

For further assistance, you can reach out to notionformyuse@gmail.com <a class="yt-timestamp" data-t="00:09:26">[00:09:26]</a>.