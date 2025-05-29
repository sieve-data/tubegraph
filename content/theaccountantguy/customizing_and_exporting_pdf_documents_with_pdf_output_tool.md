---
title: Customizing and exporting PDF documents with PDF output tool
videoId: hfHjnNxqo4o
---

From: [[theaccountantguy]] <br/> 

The PDF Output tool facilitates the [[exporting and managing PDF documents for business | bulk export of PDF documents]] using a Notion page as a template and a Notion database for data <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. This process allows for the [[customizing_document_settings_and_layout_in_pdf_generation | customization of documents]] based on specific data entries.

## Setting Up Templates and Databases

To generate PDF documents, you need a purchase order template and a Notion database <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>.
*   **Template Structure**: The template includes relevant details like purchase order number, date, supplier, and buyer name <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. Items intended to be replaced with database information are placed inside curly braces `{{}}` (e.g., `{{purchase order number}}`, `{{date field}}`, `{{supplier name}}`) <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. These "curly braces" items will be dynamically replaced by data from the database <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>.
*   **Database Structure**: The Notion database contains corresponding fields with the exact same naming convention as the curly brace items in the template <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>. Each row in the database represents a unique document to be generated <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

## Connecting to PDF Output

The process begins by logging into PDFoutput.com <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>. The interface prompts you to connect to a Notion database and a Notion template <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>.

### Duplicating Templates
1.  Navigate to the "template" section in the sidebar navigation <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.
2.  Search for a predefined template, such as "purchase order" <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.
3.  Click on the provided database link and template link <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.
4.  Select "start with this template" to duplicate both the database and template into your Notion workspace <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>. This requires selecting your Notion workspace and clicking "add to private" <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.

### Granting Access
1.  Once duplicated, return to PDF Output and click "click here to add database" or "click here to add template" <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
2.  Select your Notion workspace, choose the specific database and template you duplicated, and click "allow access" <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.
3.  The tool will then authenticate and connect to your chosen database and template <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>. If they don't appear immediately, click the refresh button <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.

## Mapping Database Fields to Template Fields

After adding the template and database, you'll name the export (e.g., "purchase order") and click "next" <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>. The tool will then load the database elements and template elements <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.
*   **Automatic Mapping**: If the naming conventions in your database exactly match the curly brace items in your template, the fields will automatically map <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.
*   **Manual Mapping**: If names do not match, fields will appear in gray. You can manually click and choose the corresponding element to map <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>.

## Generating and Exporting PDFs

After mapping, click "create PDF" <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>. The tool will process documents for each row in your database <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
*   **Preview**: You can preview a sample of the generated PDFs <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>.
*   **Download**: Click "download all" to download all generated PDF files, typically as a zipped archive <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>. If you miss the download, you can click "download PDF again" <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>.

## Customization and Tool Settings

The template, once duplicated to Notion, is fully customizable. You can edit, modify, or make any changes to it <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>. Just ensure that any elements you want to populate from the database remain within curly braces `{{}}` and maintain the exact naming convention <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>. This falls under [[customizing_document_settings_and_layout_in_pdf_generation | customizing document settings and layout]] and [[understanding_pdf_output_settings_and_features | understanding PDF output settings]].

### Connections
The "connections" option on the right sidebar shows recently created connections, allowing you to quickly reload the associated database and template for future exports without needing to re-select them <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>. This streamlines the [[using_pdf_output_interface_for_exporting_documents | export process]].

### Upgrade Options
*   **Watermark**: The free plan includes a "Made with PDF Output Watermark" on exported documents <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>.
*   **Subscription**: Upgrading to a paid subscription removes the watermark and any limits on PDF generation <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>.

### Settings
*   **Page Format**: By default, the page format is set to A4 <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>.
*   **Adding More Templates/Databases**: After the initial setup, you can add more databases and templates via the "settings" section <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.
*   **Relation Properties**: If your Notion database uses relation properties, ensure you grant access to the relational database(s) along with the primary database during the access permission step so all elements reflect correctly in the PDF output <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>.

### Help and Feedback
*   **Feedback**: Users can provide feedback on difficulties or issues through a dedicated feedback option <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>.
*   **Help Section**: A video is available in the help section demonstrating how to use a custom template from scratch, if you prefer not to use the predefined templates <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>.

For any further questions, you can reach out via email at notionformyuse@gmail.com <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>.