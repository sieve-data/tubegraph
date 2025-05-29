---
title: Using templates to automate PDF creation
videoId: hfHjnNxqo4o
---

From: [[theaccountantguy]] <br/> 

PDF Output allows users to generate PDF documents in bulk using a Notion page and a Notion database <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. This process leverages templates to automate the insertion of data from a database into a PDF document <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.

## Template and Database Structure

A template for PDF generation, such as a purchase order template, includes specific items placed inside curly braces <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>. These items, like purchase order number, date field, supplier name, and buyer name, are placeholders that will be replaced with data from a database <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. The database contains corresponding fields with the exact same naming convention as the placeholders in the template <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. Each row in the database will be used to generate a separate PDF document <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

> [!INFO] Template Customization
> The entire template is [[customizable_pdf_templates | customizable]], allowing users to edit or modify it once duplicated <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>. Ensure that any data to be pulled from the database is enclosed in curly braces within the template <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>. It is crucial to follow the exact same naming convention in both the template and the database for proper mapping <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>.

## Steps to Automate PDF Generation

To [[creating_and_using_templates_for_pdf_generation | generate PDF documents]] in bulk:

1.  **Log in to PDF output.com**: Upon logging in, an interface prompts for connecting a Notion database and a Notion template <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.
2.  **Access Predefined Templates**: Navigate to the "Template" section in the sidebar <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>. This section lists predefined templates for various use cases <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>. For example, search for "purchase order" to find the purchase order PDF generator <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.
3.  **Duplicate Template and Database**: Click on the database and template links provided for the chosen template (e.g., purchase order) <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>. Then, click "Start with this template" to duplicate them to your Notion workspace <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.
4.  **Connect Notion to PDF Output**: Once templates are duplicated, return to PDF Output and click "click here to add database" or "click here to add template" <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>. Grant permission by selecting your Notion workspace and choosing the duplicated database and template pages <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>. Click "Allow access" to authorize the connection <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>. If the connection isn't immediately visible, click "refresh" <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
    *   For relational properties in the database, ensure access is given to all linked databases during the connection process <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>.
5.  **Name the Export**: Define a name for the PDF export, such as "purchase order" <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>.
6.  **[[mapping_database_elements_to_templates_for_pdf_generation | Map Elements]]**: The system will load database and template elements <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>. If naming conventions are exact, elements will map automatically <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>. Otherwise, manual mapping is required by selecting the corresponding elements <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.
7.  **Generate PDFs**: Click "Create PDF" to process the documents <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>. Once processing is complete, the export is successful <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.
8.  **Preview and Download**: Users can preview a sample file <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>, ensuring data is mapped precisely <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>. Then, click "Download all" to download all generated PDFs <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>. The download PDF option remains available if documents were missed in the first attempt <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>.

## [[managing_connections_and_templates_in_pdf_output | Managing Connections and Templates]]

*   **Connections**: The "Connections" option on the right sidebar displays previously created connections <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>. Clicking on a saved connection will automatically load the associated database and template, allowing for quicker re-exports without needing to re-enter details <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>.
*   **Upgrade Option**: Free plans include a "Made with PDF Output" watermark on exported documents <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>. Upgrading to a paid subscription removes the watermark and any limits on PDF generation <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>.
*   **Settings**: The "Settings" section allows users to define the page format (default A4) <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>. It also provides an option to add more databases and templates beyond the initial setup <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.
*   **Feedback and Help**: Users can provide feedback or report issues via the "Feedback" option <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>. The "Help" section includes a video demonstrating how to use a [[creating_and_utilizing_pdf_templates | custom template from scratch]] instead of predefined ones <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>.

For further assistance, users can reach out to notionformyuse@gmail.com <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>.