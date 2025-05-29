---
title: Generating PDF documents in bulk using Notion and PDF Output
videoId: XPSQBVl9mKs
---

From: [[theaccountantguy]] <br/> 

[[PDF Output]] is a tool designed to [[Generating PDF documents from Notion database | generate PDF documents in bulk]] using a [[Notion database]] in conjunction with a [[Notion templates for PDF generation | Notion template]] <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>.

## How it Works <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>

The process involves replacing placeholder text within a template with corresponding data from a [[Notion database]] <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>. For example, an invoice template might have fields like invoice number, date, due date, and terms enclosed in curly braces (e.g., `{invoice_number}`, `{date}`) <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. [[PDF Output]] fetches information from each row and column of the [[Notion database]] and uses it to replace these placeholder elements, thereby [[Generating PDF documents in bulk using Notion | generating PDF documents]] <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.

## Step-by-Step Guide to [[Bulk PDF document generation using Notion | Bulk PDF Generation]] <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>

### 1. Accessing PDF Output <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>

Navigate to PDFoutput.com <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.

### 2. Selecting and Duplicating a Template <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>

*   From the [[PDF Output]] interface, click on "Templates" <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>.
*   Browse or search for the desired template (e.g., an invoice template) <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.
*   Click the "Download link" next to the chosen template <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.
*   On the template page, click "Start with this template" to duplicate it to your personal Notion workspace <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>. Ensure you select the correct Notion account and workspace <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.

### 3. Connecting Notion to PDF Output <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>

*   Go back to PDFoutput.com and navigate to "Settings" <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.
*   Click "Click here to add templates" to redirect to your Notion workspace <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.
*   Choose the duplicated template page (which contains both the [[Notion database]] and the template) <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>.
*   Click "Allow access" to authenticate the connection <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>.

### 4. Selecting Database and Template in PDF Output <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>

*   Once redirected back to [[PDF Output]], select your [[Notion database]] (e.g., "Professional Invoice Database") <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.
*   Select your [[Notion template]] (e.g., "Invoice Template") <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>.
*   Give a short name (20-character limit) to your generation process <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.
*   Click "Next" <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>.

### 5. Mapping Notion Properties to Template Elements <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>

*   [[PDF Output]] automatically loads and maps [[Notion database]] properties (columns) to template elements (placeholders) <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>.
*   Ensure the names in the template (e.g., `{Invoice Number}`) exactly match the column names in the [[Notion database]] (e.g., "Invoice Number") for automatic mapping <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.
*   If a mapping is not automatic (indicated by gray color), you can manually map properties <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>.
*   Search, sorting, and filtering options are available to manage mappings <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>.

### 6. Exporting and Downloading PDFs <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>

*   Before exporting, check the `PDF Status` column in your [[Notion database]] <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>. Rows with this column unchecked will be generated <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>. After generation, it will be checked <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>.
*   Click "Export" <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>.
*   Once processing is complete, you can "Preview Sample" to see a single generated document <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a> or "Download All" to get all generated PDFs in a zip file <a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a>.

## Additional Features and Considerations

*   **Template Customization**: You can customize your [[Notion template]] by adding, deleting, or modifying elements. Ensure any new placeholder elements (in curly braces) have corresponding columns in your [[Notion database]] <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.
*   **Reusing Connections**: After the first export, your setup is saved as a "Connection" <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>. The next time, simply select your connection from the "Connections" window to quickly regenerate documents using the same database and template <a class="yt-timestamp" data-t="00:09:34">[00:09:34]</a>.
*   **Regeneration**: To regenerate a specific row, uncheck its `PDF Status` column in the [[Notion database]] before initiating the export <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>.
*   **Subscription Plans**: Free users will see a watermark on generated PDFs <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>. Paid plans remove the watermark <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>.
*   **Page Format**: Under settings, you can choose different page formats for your PDF output <a class="yt-timestamp" data-t="00:10:37">[00:10:37]</a>.
*   **Support**: For questions or feedback, use the feedback option within the tool <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a> or contact notionformyuse@gmail.com <a class="yt-timestamp" data-t="00:11:35">[00:11:35]</a>. A help section with video demonstrations is also available <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a>.