---
title: Customizing PDF templates with Notion
videoId: zrr8DW4PWz0
---

From: [[theaccountantguy]] <br/> 

[[Using Notion with PDF output | PDFoutput.com]] allows users to [[generating_pdf_documents_with_notion | generate PDF documents]] using a Notion database and template <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. This process involves leveraging Notion as a structured database and template for creating customized PDF outputs, such as payment receipts <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>.

## Accessing and Duplicating Templates

To begin, users need to log into PDFoutput.com <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. From the interface, navigate to the "Templates" section, which lists all available templates for PDF output <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. Users can search for specific templates, such as the "payment receipts PDF generator," or use filter and sorting options <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.

Once a template is selected, click on its download link <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>. This action opens a new page displaying both the associated Notion database and the template <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>. To [[setting_up_notion_templates_and_databases_for_pdf_generation | use the template]] with [[Using Notion with PDF output | PDFoutput]], it must be duplicated to a Notion workspace <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>. If the template is not yet published to the Notion Gallery, users will see a "duplicate" option <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>. If it's published, they will see a "start with this template" option <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.

## Understanding Template and Database Structure

A Notion template is predefined with elements intended for PDF generation <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. Key to [[customizing_pdf_templates_in_notion | customizing Notion templates]] for PDF output are *placeholder text elements* <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>. These placeholders are enclosed in curly braces, such as `{{receipt number}}`, `{{receipt date}}`, `{{customer name}}`, and `{{amount paid}}` <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.

These placeholder elements are designed to be replaced by corresponding data from a Notion database <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. For successful mapping, the text inside the curly braces in the template must *exactly match* the column names in the Notion database <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>. This ensures proper syncing and accurate PDF generation <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.

## [[Customizing Notion templates | Customizing Notion Templates]]

The entire template is customizable to fit specific requirements <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>. Users can:
*   Make elements bold <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>.
*   Add spacing as needed <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>.
*   Adjust any element as desired <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>.

The crucial aspect of [[customizing_pdf_templates_in_notion | customizing PDF templates]] is to ensure that any placeholder elements intended to be replaced from a database are kept within curly braces <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>. It is also important to maintain consistent naming conventions between the template placeholders and the database column names <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.

## Connecting and Generating PDFs

After duplicating the template to a Notion workspace, the next step is to connect it to PDFoutput.com:
1.  Go to the "Settings" section within [[Using Notion with PDF output | PDFoutput]] <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.
2.  Click "Click here to add templates" <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.
3.  Choose the Notion workspace where the template was duplicated <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>.
4.  Select the specific template (e.g., "payment receipts PDF generator file") and click "Allow access" <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>.

Once authentication is successful, [[Using Notion with PDF output | PDFoutput]] will load the database and template elements <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>. Users then select the appropriate database and template from dropdown menus <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>. The system will automatically map Notion database properties (columns) to the template elements if the naming conventions match <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>. If any elements are mismatched, they can be manually searched for and mapped <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>.

To [[generating_pdf_documents_with_notion | generate PDFs]], click "Export" <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>. [[Using Notion with PDF output | PDFoutput]] will add a "PDF status" column to the Notion database to indicate which rows have been processed <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>. After a successful export, users can preview a sample PDF or download all generated files <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>. Each generated PDF file corresponds to a specific row in the Notion database <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>.

## Additional Features

*   **Connections:** The "Connections" section keeps a record of past template and database pairings, allowing users to quickly load them for future generations without manual setup <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.
*   **Multiple Templates:** Users can select multiple templates if needed <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>.
*   **Watermark:** Free plans will include a watermark, which can be removed by upgrading to a paid subscription <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>.
*   **Settings:** The settings allow changing the page format of the PDF <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>.
*   **Feedback & Help:** Options are available to send feedback or access demonstration videos for setup assistance <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>.