---
title: Using templates and databases for PDF generation
videoId: hfHjnNxqo4o
---

From: [[theaccountantguy]] <br/> 

PDF Output allows users to [[generating_pdf_documents_for_business_needs | generate PDF documents]] in bulk using a Notion page as a template and a Notion database for data input <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. This process streamlines the creation of documents like purchase orders <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>.

## Template and Database Preparation

### Template Structure
A template, such as a purchase order, includes relevant details like the purchase order number, date, supplier, and buyer name <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. Key elements intended for replacement with database information are placed inside curly braces (e.g., `{purchase order number}`, `{date field}`, `{supplier name}`, `{buyer name}`) <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. These placeholders will be automatically filled by data from the database <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>.

### Database Structure
The Notion database must contain properties (columns) with the exact same naming convention as the placeholders defined in the template <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>. Each row in the database represents a unique set of data for one PDF document <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>, allowing for bulk PDF generation <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

## Connecting Notion to PDF Output

1.  **Log In**: Access PDFOutput.com <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>.
2.  **Access Templates**: Navigate to the "Template" section in the sidebar <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.
3.  **Search for Templates**: Search for specific templates, such as "purchase order" <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.
4.  **Duplicate to Notion**: Click on the database and template links provided <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>, then select "Start with this template" to duplicate them to your Notion workspace <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>. This will prompt you to select your Notion workspace and add them <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.
5.  **Connect in PDF Output**: Once duplicated, return to PDF Output and click "click here to add database" or "click here to add template" <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>. Select your Notion workspace and choose the duplicated database and template, then click "Allow access" <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>. This authorizes PDF Output to connect to your Notion data <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>.
    *   If templates/databases don't appear, click the "refresh" button <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.
    *   You can select multiple databases and templates from the dropdown menus <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.

## [[mapping_database_elements_to_template_placeholders_in_pdfoutput | Mapping Data Fields]]

After connecting the database and template, name the process (e.g., "purchase order") and click "next" <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>. PDF Output will load both database properties and template placeholders <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.
*   **Automatic Mapping**: If the naming conventions in the database and template exactly match, the elements will be automatically mapped <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.
*   **Manual Mapping**: If there are naming discrepancies, elements will appear in gray <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>, and you will need to manually select the corresponding database property for each template element <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>.

## [[generating_pdf_documents_for_business_needs | Generating and Exporting PDFs]]

1.  **Create PDF**: Click "Create PDF" to begin processing the documents <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>. PDF Output will generate a PDF document for each row in your connected Notion database <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
2.  **Preview**: Once the export is successful, you can click "preview sample" to view one of the generated PDF files <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>. This allows you to verify that all data has been accurately mapped and the document appears as intended <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.
3.  **[[exporting_and_managing_generated_pdf_documents | Download All]]**: Click "download all" to download all the generated PDF documents to your device <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>. If you miss the initial download, you can click "download PDF again" <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>.

## Managing Connections and Customization

### Connections
The "Connections" section on the right sidebar shows recently created connections <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>. Clicking on a connection (e.g., "purchase order") will automatically load the associated database and template, allowing you to quickly regenerate documents without re-entering details <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>.

### [[customizing_pdf_templates_for_specific_needs | Customizing Templates]]
The duplicated template is fully customizable <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>. You can edit or modify any aspect of the template <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>. The only requirements are to keep the data placeholders inside curly braces and ensure their names match the database properties exactly <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.

### Upgrade Options
On the free plan, generated PDF documents will include a "Made with PDF Output" watermark <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>. Upgrading to a paid subscription removes the watermark and any limits on PDF generation <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>.

## Additional Features and Support

*   **Settings**: The "Settings" section allows you to define the default page format (e.g., A4) <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a> and add additional databases and templates beyond the initial setup <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.
*   **Feedback**: For any issues or suggestions, use the "Feedback" option to send a message to support <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>.
*   **Help**: The "Help" section provides a video demonstration on [[creating_and_using_templates_for_pdf_generation | how to use a custom template from scratch]] if you prefer not to use the predefined templates <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>.
*   **Relation Properties**: If your Notion database utilizes relation properties, it's crucial to grant PDF Output access to those related databases during the connection process to ensure all elements are correctly reflected in the generated PDFs <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>.