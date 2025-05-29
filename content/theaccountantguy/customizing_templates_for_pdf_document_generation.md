---
title: Customizing templates for PDF document generation
videoId: XPSQBVl9mKs
---

From: [[theaccountantguy]] <br/> 

PDF Output is a tool designed to [[bulk_pdf_document_generation_process | generate PDF documents in bulk]] using a Notion database and a Notion template <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. This process involves replacing placeholder elements within a template with corresponding data from a Notion database <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>.

## How Templates Work <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>

Templates, such as an invoice template, contain placeholder text elements enclosed in curly braces <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. These placeholders represent specific fields like invoice number, date, due date, and terms <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. The PDF Output tool fetches information from each row of a Notion database, replacing these placeholder elements with the corresponding data from the database columns <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.

## [[Creating and utilizing PDF templates | Creating and Utilizing Templates]] <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>

### Accessing Pre-made Templates <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>
To begin, users navigate to PDF Output's template section <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>. This section lists various pre-added templates for different use cases <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>. Users can search, sort, or filter to find a specific template, such as an invoice template <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.

### Duplicating Templates to Notion <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>
Once a template is selected, it must be duplicated to the user's Notion workspace <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>. This involves clicking "Start with this template" and choosing the desired Notion workspace <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>. After duplication, the template page, which includes both the database and template elements, will appear in the Notion workspace <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.

### Connecting Notion to PDF Output <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>
In PDF Output, users go to settings and select the option to add templates <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>. This redirects to the Notion workspace to choose the specific template and database pages <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>. It's crucial to select the correct Notion account where the templates were duplicated <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>. After selecting the pages (e.g., the "Invoice Generator Template" page which contains both the database and template) and allowing access, PDF Output will authenticate the connection and fetch the Notion database and template <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.

### [[Customizing templates and databases for document generation | Customizing Templates and Databases]] <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>
Users can [[customizable_pdf_templates | customize]] the duplicated template in Notion by adding, deleting, or modifying any elements <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>. When [[customizing invoice templates for bulk generation | customizing invoice templates for bulk generation]] or any other template, ensure that any new elements added within curly braces in the template correspond exactly to column names in the Notion database <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>.

### Mapping Template Elements to Database Properties <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>
Once the template and database are selected in PDF Output, the tool automatically attempts to map Notion properties (database columns) to template elements <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>.

*   **Automatic Mapping**: If the names of template elements (inside curly braces) exactly match the Notion database column names, mapping occurs automatically and is indicated by a green color <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.
*   **Manual Mapping**: If there's a discrepancy in naming, the mapping might appear gray or unmapped <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>. Users can click on these elements and manually map them to the correct Notion property <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>.
*   **Search and Filter**: Search, sorting, and filtration options are available to help manage and review the mapped elements <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>.

## [[Using templates to automate PDF creation | Generating PDF Documents]] <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>

### PDF Status Column <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>
Before exporting, confirm that the "PDF Status" column in the Notion database is unchecked for the rows you wish to generate <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>. If a row is checked, it will not be included in the PDF output <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>. This column is unchecked by default upon initial integration and automatically checks once a document is generated for that row <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>.

### Exporting and Downloading <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>
After mapping and ensuring the "PDF Status" is set correctly, click "Export" to begin the [[bulk_pdf_document_generation_process | bulk PDF document generation process]] <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>. Once successful, users can preview a sample PDF or download all generated documents as a zipped folder <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>. Each generated PDF will reflect the specific data from its corresponding Notion database row <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>.

## [[Managing PDF Output templates and settings | Managing Settings and Connections]] <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>

### Connections <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>
After the first successful export, the connection (linking a specific database and template) is saved in the "Connections" window <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>. For subsequent generations using the same setup, users can simply select the saved connection, and it will load all previously mapped elements <a class="yt-timestamp" data-t="00:09:34">[00:09:34]</a>.

### Page Format <a class="yt-timestamp" data-t="00:10:37">[00:10:37]</a>
Under the settings tab, users can choose different page formats for the PDF output from a list of elements <a class="yt-timestamp" data-t="00:10:39">[00:10:39]</a>.

### Subscription and Watermarks <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>
New users or those on a free plan will see a watermark in the generated PDF output <a class="yt-timestamp" data-t="00:10:22">[00:10:22]</a>. Upgrading to a paid plan removes this watermark <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>.

### Support and Help <a class="yt-timestamp" data-t="00:10:53">[00:10:53]</a>
Users can provide feedback or ask questions via the feedback option, which directly sends a message to the support inbox <a class="yt-timestamp" data-t="00:10:55">[00:10:55]</a>. A help section is also available, which may contain demonstration videos to guide users <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a>.