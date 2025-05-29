---
title: Using PDF output com for PDF generation
videoId: zrr8DW4PWz0
---

From: [[theaccountantguy]] <br/> 

This article provides an [[introduction_to_pdf_output_tool | introduction to the PDF Output tool]] and outlines the process of generating PDF documents, specifically payment receipts, using a Notion database and template with PDF Output.com <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>.

## Getting Started with PDF Output.com

To begin, users need to log in to PDF Output.com, which presents an interface for managing templates and generating PDFs <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.

### Accessing Templates
Templates available for PDF output are listed under the "Templates" section <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. Users can search for specific templates using a search option or refine results using filter and sorting options <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>.

For instance, the "payment receipts PDF generator" template is available for [[using_pdf_output_for_invoice_generation | invoice generation]] <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.

## Duplicating and Customizing Notion Templates

Once a template, such as the "payment receipts PDF generator," is selected, it can be downloaded, opening a page that includes both the database and the template <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.

### Understanding Template Elements
Templates contain predefined elements, some of which are placeholder text enclosed in curly braces (e.g., `{receipt number}`, `{customer name}`). These placeholders are designed to be replaced by corresponding data from a Notion database <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.

### Customization and Matching
The entire template is customizable to meet specific requirements, allowing users to modify formatting like making elements bold or adjusting spacing <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>. However, it is crucial that the placeholder elements in the template exactly match the column names in the Notion database to ensure proper syncing and error-free PDF generation <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.

### Duplicating to Notion Workspace
If a template isn't yet published to the Notion Gallery, users will need to click "Duplicate" to add it to their Notion workspace <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>. If it is published, the "Start with this template" option will duplicate it directly to a Notion workspace, which is necessary for [[setting_up_pdfoutput_for_document_generation | setting up PDFOutput for document generation]] <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.

## [[integration_with_pdf_output_com_for_document_generation | Integrating with PDF Output.com]]

After duplicating the template to a Notion workspace, the next step is to connect it with PDF Output.com <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.

### Adding Templates to PDF Output
1.  Navigate to the "Settings" section in PDF Output.com <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>.
2.  Click "Click here to add templates" <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.
3.  Choose the Notion workspace where the template was duplicated <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.
4.  Select the specific template (e.g., "payment receipts PDF generator file") and click "Allow access" <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>. This initiates the authentication process, allowing PDF Output to read the template and database elements <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.

### Mapping Database Properties to Template Elements
Once authentication is successful and elements are loaded:
1.  Select the correct database (e.g., "payment receipts database") from the dropdown <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>.
2.  Select the corresponding template (e.g., "payment receipt template") <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.
3.  Give the connection a name <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.

PDF Output will automatically map Notion properties (database column names) to the corresponding template elements if their names match <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>. If there's a mismatch, users can manually search and select the correct element to map <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>. Filtering, searching, and sorting options are available to assist with mapping <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>.

## Generating PDF Documents

With everything set up, users can proceed to [[bulk_export_of_pdf_documents_using_pdf_output | bulk export of PDF documents using PDF Output]] or generate individual files.

### The Export Process
Clicking "Export" triggers the generation of PDFs <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>. A "PDF status" column is automatically added to the Notion database, and each row's status is ticked as its corresponding PDF is generated <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>.

### Reviewing and Downloading Output
After a successful export, users can preview a sample file <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a> or download all generated files <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>. Each generated PDF corresponds to a specific row in the Notion database, with all elements placed correctly <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>.

## Additional Features and Support

### Connections
The "Connections" section in PDF Output.com allows users to quickly load previously configured database and template setups, eliminating the need to manually add them each time <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.

### Plans and Watermarks
Free plan users will have a watermark of PDF Output on their generated PDFs <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>. Upgrading to a paid plan removes the watermark <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>.

### Settings and Support
*   **Page Format:** Users can change the page format in the settings <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>.
*   **Feedback:** A feedback option is available to send messages directly to the developer for assistance <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>.
*   **Help Section:** The help section contains a demonstration video to guide users through the setup process <a class="yt-timestamp" data-t="00:08:59">[00:08:59]</a>.

For any questions or assistance regarding [[utilizing_pdf_output_for_document_generation | utilizing PDF output for document generation]], users can reach out via email at notionformyuse@gmail.com <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>.