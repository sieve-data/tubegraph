---
title: Managing connections and settings in PDF output
videoId: zrr8DW4PWz0
---

From: [[theaccountantguy]] <br/> 

[[using_pdf_output_com_for_pdf_generation | PDF Output]] is a tool that enables the generation of PDF documents from a Notion database using Notion templates <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. This article outlines how to manage connections, templates, and various settings within the [[using_pdf_output_com_for_pdf_generation | PDF Output]] platform.

## Accessing PDF Output
To begin, users must log in to PDFoutput.com <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. Upon logging in, an interface will be visible, providing access to different features, including templates <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.

## Template Management
The "Templates" section lists all available templates for [[using_pdf_output_com_for_pdf_generation | PDF Output]] <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.
- **Searching and Filtering**: Users can search for specific templates using a search bar <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. Filter and sorting options are also available to refine template searches <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.
- **Duplicating Templates**: To use a template, it must be duplicated to a Notion workspace <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>. If a template is not yet published to the Notion Gallery, users will see a "duplicate" option <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>. If published, select "start with this template" <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.

## Connecting Notion to PDF Output
After duplicating a template to a Notion workspace, it needs to be added to [[setting_up_pdfoutput_for_document_generation | PDF Output]]:
1.  Navigate to the "Settings" section in [[setting_up_pdfoutput_for_document_generation | PDF Output]] <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>.
2.  Click "click here to add templates" <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.
3.  Choose the specific Notion workspace where the template was duplicated <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.
4.  Select the desired template file (e.g., "payment receipts PDF generator") <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.
5.  Click "allow access" to enable [[setting_up_pdfoutput_for_document_generation | PDF Output]] to read template and database elements <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>. Authentication success will return to the [[setting_up_pdfoutput_for_document_generation | PDF Output]] interface <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.

### Understanding Template Placeholders
Templates in Notion contain predefined elements. Placeholder text, enclosed in curly braces (e.g., `{receipt number}`, `{customer name}`), will be replaced by corresponding data from the Notion database <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>. It's crucial that the placeholder names in the template exactly match the column names in the Notion database for proper syncing and PDF generation <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.

## Customization and Mapping
Templates are customizable within Notion; users can modify formatting (e.g., bolding, spacing) as needed <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.
1.  **Selecting Database and Template**: In [[setting_up_pdfoutput_for_document_generation | PDF Output]], use the dropdowns to select the Notion database (e.g., "payment receipts database") and the corresponding template <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>.
2.  **Automatic Mapping**: [[setting_up_pdfoutput_for_document_generation | PDF Output]] automatically maps Notion properties (database columns) to template elements if names correctly match <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>.
3.  **Manual Mapping**: If elements are mismatched or unmapped, users can manually select the correct corresponding element using search, filter (e.g., "unmapped properties"), and sorting options <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>.

## Exporting Documents
Once mapping is complete, click "Export" <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>. [[bulk_export_of_pdf_documents_using_pdf_output | PDF Output]] automatically adds a "PDF status" column to the Notion database to track generated rows <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>. Each row is ticked as its PDF is generated <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>.
Users can preview a sample PDF or [[bulk_export_of_pdf_documents_using_pdf_output | download all]] generated files <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>. Each generated file corresponds to a row in the Notion database <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>.

## [[managing_connections_and_subscriptions_in_pdf_creation_tools | Tool Settings and Features]]

### Connections
The "Connections" section displays past connections, allowing users to quickly load previously configured databases and templates without manual re-addition <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>.

### Subscriptions
Users on the free plan will find a [[managing_connections_and_subscriptions_in_pdf_creation_tools | PDF Output]] watermark on generated PDFs <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>. Upgrading to a paid plan removes this watermark <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>.

### Page Format
Within "Settings," the page format (e.g., A4, Letter) can be changed <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>. Remember to click "save" after making changes <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>.

### Feedback and Help
-   **Feedback**: A feedback option allows users to send messages directly to the support team <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>.
-   **Help Section**: The "Help" section includes a demonstration video that guides users through the setup process for generating PDF documents <a class="yt-timestamp" data-t="00:08:59">[00:09:02]</a>.