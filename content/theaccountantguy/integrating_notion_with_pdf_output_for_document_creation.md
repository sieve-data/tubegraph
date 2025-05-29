---
title: Integrating Notion with PDF Output for document creation
videoId: hfHjnNxqo4o
---

From: [[theaccountantguy]] <br/> 

[[using_pdf_output_tool_with_notion | PDF Output]] is a tool designed to [[generating_pdf_documents_from_notion_using_pdfoutput | generate PDF documents]] in bulk by [[integrating_notion_pages_and_databases_with_pdfoutput | integrating Notion pages and databases]] with predefined templates <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. This process involves using a Notion page as a template and a Notion database to supply the data for each PDF <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>.

## Core Concept: Template and Database Interaction

The system relies on a template where specific items are enclosed within curly braces, for example, `{Purchase Order Number}` <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>. These bracketed items are placeholders that will be replaced with data from a Notion database <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>. The database must contain columns (properties) with names that exactly match the placeholders in the template <a class="yt-timestamp" data-t="01:05:00">[01:05:00]</a>.

For instance, a purchase order template might include:
*   `{Purchase Order Number}` <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>
*   `{Date}` <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>
*   `{Supplier Name}` <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>
*   `{Buyer Name}` <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>

The corresponding [[integrating_notion_database_with_pdfoutput_tool | Notion database]] would then have columns titled "Purchase Order Number", "Date", "Supplier Name", and "Buyer Name", with specific values for each row <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. Each row in the database will be used to [[generating_pdf_documents_from_notion_using_pdfoutput | generate a separate PDF document]] <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

## Step-by-Step Guide to [[generating_pdf_documents_from_notion_using_pdfoutput | Generating PDF Documents]]

1.  **Log In:** Access [[using_pdf_output_tool_with_notion | PDF output.com]] <a class="yt-timestamp" data-t="01:19:54">[01:19:54]</a>.
2.  **Duplicate Templates:**
    *   Navigate to the "Template" section in the sidebar <a class="yt-timestamp" data-t="01:38:00">[01:38:00]</a>.
    *   Search for the desired template (e.g., "purchase order") <a class="yt-timestamp" data-t="01:52:00">[01:52:00]</a>.
    *   Click on both the database link and the template link provided <a class="yt-timestamp" data-t="02:04:00">[02:04:00]</a>.
    *   Use the "Start with this template" option to duplicate both the database and the template into your Notion workspace <a class="yt-timestamp" data-t="02:15:00">[02:15:00]</a>. Select your Notion workspace and click "Add to private" <a class="yt-timestamp" data-t="02:29:00">[02:29:00]</a>.
3.  **Connect Notion to [[using_pdf_output_tool_with_notion | PDF Output]]:**
    *   On the [[using_pdf_output_tool_with_notion | PDF Output]] main screen, click "Click here to add database" or "Click here to add template" <a class="yt-timestamp" data-t="02:50:00">[02:50:00]</a>.
    *   Grant permission by selecting your Notion workspace and choosing the duplicated database and template <a class="yt-timestamp" data-t="03:05:00">[03:05:00]</a>.
    *   Click "Allow access" to connect <a class="yt-timestamp" data-t="03:26:00">[03:26:00]</a>.
    *   If the database and template don't appear immediately, click the "refresh" button <a class="yt-timestamp" data-t="03:51:00">[03:51:00]</a>.
4.  **Name and Map Elements:**
    *   Define a name for the output (e.g., "purchase order") <a class="yt-timestamp" data-t="04:12:00">[04:12:00]</a>.
    *   The system will load database properties and template elements <a class="yt-timestamp" data-t="04:19:00">[04:19:00]</a>.
    *   If naming conventions are consistent between the database and template, elements will automatically map <a class="yt-timestamp" data-t="04:43:00">[04:43:00]</a>.
    *   For manual mapping, click on the gray-colored elements and select the correct database property <a class="yt-timestamp" data-t="04:48:00">[04:48:00]</a>.
5.  **[[exporting_pdf_documents_from_notion | Exporting PDF Documents]]:**
    *   Click "Create PDF" <a class="yt-timestamp" data-t="05:02:00">[05:02:00]</a>.
    *   Once the export is successful, you can "Preview sample" to review one of the generated files <a class="yt-timestamp" data-t="05:41:00">[05:41:00]</a>.
    *   Click "Download all" to [[exporting_notion_data_to_pdf | download all the generated PDF documents]] <a class="yt-timestamp" data-t="06:07:00">[06:07:00]</a>.

## Customization and Best Practices

*   **Template Customization:** The duplicated template is fully customizable <a class="yt-timestamp" data-t="05:17:00">[05:17:00]</a>. Ensure that any data intended to be replaced from the database remains within curly braces <a class="yt-timestamp" data-t="05:25:00">[05:25:00]</a>.
*   **Naming Convention:** For automatic mapping, use the exact same naming convention for properties in your Notion database as the placeholders in curly braces within your template <a class="yt-timestamp" data-t="05:31:00">[05:31:00]</a>.
*   **Relation Properties:** If your Notion database uses relation properties, ensure that the related databases are also given access permissions during the connection process so all elements reflect correctly in the PDF output <a class="yt-timestamp" data-t="09:02:00">[09:02:00]</a>.

## [[using_pdf_output_tool_with_notion | PDF Output]] Features

*   **Connections:** Saved connections appear under the "Connections" option, allowing you to quickly reload previously configured database and template links without re-entering them <a class="yt-timestamp" data-t="06:57:00">[06:57:00]</a>.
*   **Upgrade Option:** Free plans include a "Made with [[using_pdf_output_tool_with_notion | PDF Output]]" watermark <a class="yt-timestamp" data-t="07:29:00">[07:29:00]</a>. Upgrading to a paid subscription removes the watermark and any limits on PDF generation <a class="yt-timestamp" data-t="07:34:00">[07:34:00]</a>.
*   **Settings:**
    *   **Page Format:** Default is A4 <a class="yt-timestamp" data-t="07:49:00">[07:49:00]</a>.
    *   **Add More Templates/Databases:** After initial setup, you can add more templates and databases via the settings <a class="yt-timestamp" data-t="07:56:00">[07:56:00]</a>.
*   **Feedback:** A feedback option is available to report issues or provide suggestions <a class="yt-timestamp" data-t="08:10:00">[08:10:00]</a>.
*   **Help:** A help section includes a video demonstrating how to use a custom template from scratch <a class="yt-timestamp" data-t="08:24:00">[08:24:00]</a>.

For any further questions, you can reach out via email at notionformyuse@gmail.com <a class="yt-timestamp" data-t="09:27:00">[09:27:00]</a>.