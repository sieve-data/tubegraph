---
title: Using PDF Output interface for exporting documents
videoId: XPSQBVl9mKs
---

From: [[theaccountantguy]] <br/> 

[[introduction_to_pdfoutput_tool | PDF Output]] is a tool designed to [[bulk_export_of_pdf_documents | generate PDF documents]] in bulk using a Notion database and template <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. This article outlines the process of [[exporting_bulk_pdfs_with_pdf_output_tool | generating PDF documents]] using the [[introduction_to_pdfoutput_tool | PDF Output]] interface.

## Accessing and Preparing Templates

To begin, navigate to PDFoutput.com <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.

### Selecting a Template
On the [[introduction_to_pdfoutput_tool | PDF Output]] website, click on the "Templates" section <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>. This page displays all available templates <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>. You can use the search, sorting, and filtration options to find a specific template <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>. For example, an [[using_pdf_output_software_for_invoice_creation | invoice template]] is demonstrated, which uses curly braces to indicate placeholder elements <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>. These placeholders will be replaced by data from a Notion database <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>.

### Duplicating the Template to Notion
To use a template, click the "Download" link next to it <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>. This opens the template page in a new tab, showing both the database and template elements <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>. You must duplicate this template to your own Notion workspace <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>. Click "Start with this template" and select your desired Notion workspace to add the template <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.

## Connecting Notion to PDF Output

After duplicating the template to Notion, return to PDFoutput.com and go to "Settings" <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.
1.  Click the "Click here to add templates" option <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.
2.  You will be redirected to Notion to choose the templates <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>.
3.  Ensure you select the same Notion account where you duplicated the templates <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.
4.  Click "Select Pages" and choose the specific Notion page containing your duplicated template and database <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>.
5.  Click "Allow access" to complete the authentication <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>. This will redirect you back to [[introduction_to_pdfoutput_tool | PDF Output]] <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.

## Configuring Export Settings

Once authenticated, you can fetch your Notion database and template <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>.
1.  Select your Notion database (e.g., "Professional Invoice Database") from the dropdown <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>.
2.  Select your Notion template (e.g., "Invoice Template") <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>.
3.  Provide a name for your export (e.g., "My Invoice Generation"). Note that the name has a 20-character limit <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.
4.  Click "Next" <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>.

### Mapping Notion Properties to Template Elements
[[customizing_and_exporting_pdf_documents_with_pdf_output_tool | PDF Output]] will load all elements from your database and template <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>.
*   **Automatic Mapping**: Notion properties (columns in your database) are automatically mapped to template elements (placeholders in curly braces) <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>.
*   **Manual Mapping**: If a mapping is not visible (e.g., in gray color), it indicates a discrepancy in naming <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>. Ensure that the names in your template exactly match the column names in your Notion database <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>. You can manually map by clicking the element and selecting the corresponding Notion property <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.
*   **Search, Sort, and Filter**: Options are available to search for specific elements, sort the list, or filter to show unmapped properties <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>.

## Preparing Notion Database for Export

Before initiating the export, check the "PDF status" column in your Notion database <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>.
*   For the first export, this column will be unchecked by default <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>.
*   Ensure that the "PDF status" checkbox is unchecked for any row you want to generate in the [[bulk_pdf_document_export_process | PDF output]] <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>.
*   Once a document is generated, this checkbox will automatically become checked <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>.

## Exporting Documents

After mapping is complete and your Notion database is prepared, click "Export" <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>.
*   [[bulk_pdf_document_export_process | PDF Output]] will start processing the documents <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a>.
*   During generation, the "PDF status" column in your Notion database will show a tick, indicating the document was generated <a class="yt-timestamp" data-t="00:07:19">[00:07:19]</a>.
*   Once the export is successful, you have two options:
    *   **Preview Sample**: View a sample [[generating_pdf_invoices_using_pdf_output_service | invoice]] generated from one of the database rows <a class="yt-timestamp" data-t="00:07:46">[00:07:46]</a>. This allows you to verify that all placeholders have been correctly replaced with data from your Notion database <a class="yt-timestamp" data-t="00:07:53">[00:07:53]</a>.
    *   **Download All**: Download all generated [[bulk_export_of_pdf_documents | PDF documents]] in a folder <a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a>. Each row from your Notion database corresponds to a unique [[bulk_export_of_pdf_documents | PDF document]] <a class="yt-timestamp" data-t="00:08:51">[00:08:51]</a>.

## Managing Connections and Additional Settings

### Re-exporting with Connections
After a successful export, your configuration is saved in the "Connections" window <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>.
*   To use the same database and template again, simply go to "Connections" and choose your saved connection <a class="yt-timestamp" data-t="00:09:34">[00:09:34]</a>.
*   The system will automatically load all elements <a class="yt-timestamp" data-t="00:09:45">[00:09:45]</a>.
*   If you need to regenerate specific rows, remember to untick their "PDF status" checkboxes in Notion before clicking "Next" and exporting again <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>.

### [[understanding_pdf_output_settings_and_features | PDF Output Settings and Features]]
Under the "Settings" tab, you can adjust:
*   **Subscription**: View your current plan, renewal date, and upgrade your subscription to remove watermarks from [[bulk_export_of_pdf_documents | PDF output]] <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>. Watermarks are visible for free users but not for paid plans <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>.
*   **Page Format**: Choose from different [[using_pdfoutput_features_and_settings | page format]] options (e.g., A4, Letter) for your [[bulk_export_of_pdf_documents | PDF documents]] <a class="yt-timestamp" data-t="00:10:37">[00:10:37]</a>. You can search for and select a specific format <a class="yt-timestamp" data-t="00:10:44">[00:10:44]</a>.
*   **Feedback**: Send a message for any questions or issues <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>.
*   **Help**: Access the demonstration video to re-watch the process <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a>.

For further assistance, you can contact notionformyuse@gmail.com <a class="yt-timestamp" data-t="00:11:35">[00:11:35]</a>.