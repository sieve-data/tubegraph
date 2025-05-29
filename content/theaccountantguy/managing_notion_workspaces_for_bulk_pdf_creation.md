---
title: Managing Notion workspaces for bulk PDF creation
videoId: zrr8DW4PWz0
---

From: [[theaccountantguy]] <br/> 

This article outlines how to [[generating_pdf_documents_using_notion | generate payment receipt documents]] using a [[generating_pdf_documents_using_notion_databases | Notion database]] and a [[creating_and_using_notion_templates_for_pdfs | Notion template]] via PDF output.com <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This process facilitates [[generating_pdf_documents_in_bulk_with_notion | generating PDF documents in bulk]].

## Accessing PDF output Templates

To begin, log in to PDF output.com <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. Once logged in, navigate to the "templates" section <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. This page lists all available templates for PDF output <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. For payment receipts, specifically look for the "payment receipts PDF generator" template <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.

### Searching and Filtering Templates

Templates can be located using a search option <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. Typing a name will automatically display the relevant template <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. Filter and sorting options are also available to streamline template selection <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.

## Duplicating Templates to Notion Workspace

After locating the "payment receipts PDF generator" template, click on its download link <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>. This opens a new page containing both the database and the template for the payment receipts PDF generator <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.

If the template has not been published to the Notion Gallery, an option to "start with this template" will appear <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>. Otherwise, click on the "duplicate" option <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>. When duplicating, you will be prompted to choose a [[notion_workspace_integration | Notion Workspace Integration]] to which the template will be added <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>. This step is essential for using the template with PDF output <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.

## Understanding Notion Templates and Databases

The payment receipt template contains predefined elements for PDF output <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. Key elements such as receipt number, date, time, customer name, and email are enclosed in curly braces, acting as placeholder text elements <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. These placeholders will be replaced by corresponding data from the linked Notion database <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.

For example, the `{customer name}` placeholder in the template corresponds to the "customer name" column in the database <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. Similarly, "amount paid," "company address," and "company email" will replace their respective template elements <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>. It is crucial that the exact naming of placeholder information in the template matches the corresponding column names in the Notion database <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>.

### Customizing Templates

Templates are fully customizable to meet specific requirements <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>. You can bold elements, add spacing, or make other design changes <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>. The key is to ensure that all placeholder elements intended for replacement from the database remain within curly braces for proper syncing and output generation <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.

## Integrating Notion with PDF Output

After duplicating the template to your Notion workspace, navigate to the settings section of PDF output.com <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>.

### Adding Templates to PDF Output

Click "click here to add templates" to integrate the Notion template with PDF output <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>. You must select the same Notion workspace where you duplicated the template <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>. After selecting the workspace and allowing access, PDF output will read all template and database elements <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>.

## Mapping Notion Database Properties to Template Elements

Upon successful authentication, the system will load the database and template elements <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>.

1.  From the drop-down menu in PDF output, select the "payment receipts database" <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>.
2.  Next, select the corresponding "payment receipt template" <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.
3.  Give your setup a name, e.g., "payment receipt," and click "next" <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.

The system will automatically map Notion properties (database elements) to the template elements if the naming conventions match correctly <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>. If any element is mismatched, you can manually search for and map the correct element <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>. Filtering, searching, and sorting options are available to assist with mapping <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>.

## [[generating_pdf_documents_using_notion_databases | Generating PDF Documents]]

Once all elements are correctly mapped, click "export" <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>.

### Export Process and Status

Upon export, a "PDF status" column is automatically added to your Notion database <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>. This column indicates which rows have had PDFs generated; by default, nothing is ticked, but as PDFs are generated, the corresponding rows will be ticked <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>.

### Previewing and Downloading PDFs

After a successful export, you can click "preview sample" to view a sample of the generated PDF <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>. The "download all" option allows you to download all generated PDF files, with each file corresponding to a row in your Notion database <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>.

## Managing Connections and Customization

PDF output saves past connections, allowing you to quickly reload the database and template without manually adding them each time <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>. Simply click on the saved connection to load the setup and continue generating PDFs <a class="yt-timestamp" data-t="00:08:05">[00:08:05]</a>.

Additional features include:
*   **Multiple Templates:** The ability to select and manage multiple templates <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>.
*   **Watermarks:** Free plans include a watermark on generated PDFs, which can be removed by upgrading to a paid subscription <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>.
*   **Page Format:** Options to change the page format in settings <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>.
*   **Feedback:** A feedback option to send messages directly to support <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>.
*   **Help Section:** A demonstration video to guide setup is available under the help section <a class="yt-timestamp" data-t="00:08:59">[00:08:59]</a>.

For further assistance, you can reach out via email <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>.