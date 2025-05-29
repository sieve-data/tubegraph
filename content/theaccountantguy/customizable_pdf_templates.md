---
title: Customizable PDF templates
videoId: hfHjnNxqo4o
---

From: [[theaccountantguy]] <br/> 

Customizable PDF templates are structured documents used to generate PDF files in bulk by pulling data from a Notion database <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. They allow for the creation of standardized documents, such as purchase orders, with variable information automatically populated from a database <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.

## Template Structure and Placeholders

A customizable PDF template includes specific fields enclosed in curly braces (e.g., `{purchase order number}`, `{date field}`, `{supplier name}`, `{buyer name}`) <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>. These curly-braced items act as placeholders that will be replaced by corresponding data from a database during the PDF generation process <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>.

## Integration with Notion Databases

For seamless integration, the Notion database used with the template must have properties (columns) with the exact same naming convention as the placeholders defined within the template's curly braces <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>, e.g., `purchase order number`, `date field`, `supplier name`, `buyer name` <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>. Each row in this database contains values for these properties, and a separate PDF document will be generated for each row <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>.

## Utilizing PDF Output for Generation

To [[using_templates_to_automate_pdf_creation | automate PDF creation]] using these templates:

1.  **Log In**: Access PDF output.com <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>. The platform will prompt you to connect a Notion database and a Notion template <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>.
2.  **Select a Template**:
    *   Go to the "Templates" section in the right sidebar navigation <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.
    *   Search for specific templates, such as "purchase order" <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.
    *   Click on both the database link and the template link provided <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.
    *   Duplicate both the database and the template into your own Notion workspace by clicking "Start with this template" <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.
    *   Select your Notion workspace and click "Add to private" <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.
3.  **Connect Database and Template**:
    *   Return to PDF output.com and click on "Click here to add database" or "Click here to add template" <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
    *   Grant permission by selecting your workspace, choosing the duplicated database and template, and clicking "Allow access" <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>.
    *   Once authenticated, the database and template will appear on the screen <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>. If not visible, click the refresh button <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
    *   You can select multiple databases or templates using the dropdowns, or search for specific ones <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>.
4.  **Define Output Name and Map Fields**:
    *   Give a name to the output (e.g., "purchase order") <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>.
    *   Click "Next" <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.
    *   The platform will load and automatically map database properties to template placeholders if the naming conventions match <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.
    *   If manual mapping is required (indicated by gray color), click the field and choose the corresponding database element <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.
5.  **Generate PDFs**: Click "Create PDF" <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>. The platform will process the documents <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
6.  **Preview and Download**:
    *   After successful export, click "Preview sample" to view one of the generated files <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.
    *   Click "Download all" to download all generated PDF documents <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>. If missed, click "Download PDF again" <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>.

## [[customizing_templates_for_pdf_document_generation | Customizing Templates for PDF Document Generation]]

The duplicated templates are fully customizable <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>. You can edit, modify, or make any changes to the template within Notion <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>.

**Key Customization Rules**:
*   Ensure that any data you want to be replaced by the database is kept inside curly braces <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>.
*   Maintain the exact same naming convention for properties in both the Notion template and the Notion database <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.

## Managing Connections and Settings

*   **Connections**: The "Connections" option on the right sidebar shows previously created connections, allowing you to quickly reload the database and template without re-entering them for subsequent exports <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>.
*   **Upgrading**: Free plan exports include a "Made with PDF Output" watermark <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>. Upgrading to a paid subscription removes the watermark and usage limits <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>.
*   **Settings**:
    *   **Page Format**: The default page format is A4 <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>.
    *   **Adding More Templates**: After initial setup, additional databases and templates can be added via the "Settings" section <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>.
*   **Feedback**: A feedback option is available to report issues or provide suggestions <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>.
*   **Help Section**: Includes a video demonstrating how to use [[custom_pdf_document_solutions | custom templates]] from scratch if you prefer not to use predefined ones <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>.

## Important Considerations

*   **Relational Properties**: If using relation properties in your Notion database, ensure you grant access to those related databases when connecting your main database and template <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>. This ensures all relevant elements are correctly reflected in the PDF output <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a>.