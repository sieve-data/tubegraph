---
title: Connecting Notion templates with PDF output
videoId: hfHjnNxqo4o
---

From: [[theaccountantguy]] <br/> 
## Connecting Notion Templates with PDF Output

### Overview
PDF Output is a tool that allows users to [[generating_pdfs_from_notion_using_pdfoutput | generate PDF documents in bulk]] using a Notion page and a Notion database <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. This process involves [[setting_up_notion_templates_and_databases_for_pdf_generation | setting up a Notion template]] with placeholders and a corresponding Notion database containing the data to fill those placeholders <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>.

### Template and Database Structure
To effectively [[using_notion_templates_and_databases_for_pdf_creation | use Notion templates for PDF creation]], specific conventions must be followed:

*   **Template Design**: The Notion template (e.g., a purchase order template) should include specific items placed inside curly braces (e.g., `{Purchase Order Number}`, `{Date Field}`, `{Supplier Name}`) <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. These curly-braced items act as placeholders that will be replaced by data from the Notion database <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>.
*   **Database Setup**: The Notion database must contain properties (columns) with the exact same naming convention as the curly-braced items in the template <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. Each row in the database represents a unique PDF document to be generated <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>. For instance, if the template has `{Purchase Order Number}`, the database needs a property named "Purchase Order Number" <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.

### Steps for Generating PDFs
To [[connecting_notion_database_and_templates_to_pdf_output | connect a Notion database and templates to PDF output]] and generate documents:

1.  **Log In**: Access PDF output.com and log in <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>.
2.  **Access Templates**: Navigate to the "Template" section in the sidebar <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>. Here, you can search for predefined templates like a "Purchase Order" PDF generator <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.
3.  **Duplicate to Notion**: Click on the database and template links provided and select "Start with this template" to duplicate them into your Notion workspace <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a> <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>. Choose your Notion workspace and click "Add to private" <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.
4.  **[[connecting_and_setting_up_pdf_output_with_notion | Connect Notion to PDF Output]]**: Back in PDF Output, click on "Click here to add database" or "Click here to add template" <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>. This will prompt you to select your Notion workspace and then choose the duplicated database and template <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>. Click "Allow access" to authorize the connection <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
    *   If you're [[using_notion_database_and_templates_for_pdf_generation | using Notion database and templates for PDF generation]] that include relation properties, ensure you grant access to the related databases as well during this step <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>.
5.  **Name the Connection**: Define a name for your connection (e.g., "Purchase Order") and click "Next" <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>.
6.  **Map Elements**: The system will load database properties and template elements (those inside curly braces) <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>. If the naming conventions are consistent between the template and database, the elements will map automatically <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>. Otherwise, you may need to manually map them <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.
7.  **Create PDF**: Click "Create PDF" <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>. The system will process and generate PDF documents for each row in your database <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
8.  **Preview and Download**: Once the export is successful, you can preview a sample PDF <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>. Then, click "Download All" to download all generated PDF documents <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>.

### Customization and Features
*   **Template Customization**: The entire template is customizable. You can edit, modify, or make any changes to the template after it's duplicated, just ensuring that the dynamic content you want from the database remains within curly braces and follows the exact naming convention <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>.
*   **Saved Connections**: Once a connection is created, it appears under the "Connections" option <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>. Clicking on a saved connection will automatically load the associated database and template, allowing for quicker future exports without re-filling the details <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>.
*   **Upgrade Options**: Users on the free plan will see a "Made with PDF Output" watermark on generated documents <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>. Upgrading to a paid subscription removes this watermark and any generation limits <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>.
*   **Settings**: The default page format is A4 <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>. You can also add more databases and templates from the settings section after the initial setup <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.
*   **Feedback and Help**: Users can provide feedback or report issues via the "Feedback" option <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>. A "Help" section includes a video demonstrating how to [[creating_notion_templates_and_databases_for_pdf_generation | create Notion templates and databases for PDF generation]] from scratch if you prefer not to use predefined ones <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>.

For support, you can reach out to notionformyuse@gmail.com <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>.