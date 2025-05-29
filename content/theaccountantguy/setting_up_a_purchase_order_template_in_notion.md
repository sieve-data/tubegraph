---
title: Setting up a purchase order template in Notion
videoId: hfHjnNxqo4o
---

From: [[theaccountantguy]] <br/> 

A purchase order template can be used to [[generating_purchase_order_pdfs_using_notion | generate purchase order PDF documents]] in bulk, utilizing a Notion page and a Notion database <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>.

## Overview of the Purchase Order Template

The template contains fields for essential information such as the purchase order number, date, supplier, buyer name, and other relevant details required for a purchase order document <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.

### Key Features of the Template
- **Placeholders**: Items within the template that are meant to be dynamically populated from a database are enclosed in curly braces, e.g., `{purchase order number}`, `{date field}`, `{supplier name}`, `{buyer name}` <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.
- **Database Integration**: These placeholders are automatically replaced with corresponding values from a Notion database <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>.
- **Naming Convention**: It is crucial that the naming convention for properties (columns) in your Notion database exactly matches the names used within the curly braces in the template <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>. This ensures automatic mapping when generating PDFs <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.
- **Bulk Generation**: A PDF document is generated for each row of data in the connected Notion database <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

## Setting Up Your Template and Database

To begin, you will need to log in to PDFoutput.com <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>.

### Duplicating the Template and Database
1.  **Access Templates**: From the PDFoutput.com interface, navigate to the "Templates" section located in the right sidebar <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.
2.  **Search for Purchase Order**: Use the search field to find the "purchase order" template <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.
3.  **Duplicate to Notion**: Click on both the "database link" and the "template link" provided <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.
    *   Click "Start with this template" to duplicate the database and template into your own Notion workspace <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.
    *   When prompted, select your desired Notion workspace and click "Add to private" to complete the duplication <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.

### Connecting to PDF Output
1.  **Add Database/Template**: Once the template and database are duplicated in Notion, return to PDFoutput.com <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>. Click on "click here to add database" or "click here to add template" <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
2.  **Grant Notion Access**:
    *   Select your Notion workspace <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.
    *   Click "Select pages" and choose the duplicated purchase order database and template <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.
    *   Click "Allow access" to authorize the connection between PDF output and your Notion pages <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
3.  **Verify Connection**: After authentication, the selected database and template should appear on the PDF output screen <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>. If not, click "Refresh" <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>. You can use the dropdowns to select different databases or templates if needed <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.
4.  **Name Your Export**: Provide a name for this PDF generation process (e.g., "purchase order") and click "Next" <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>.

### Mapping Database Elements to Template Fields
The next step will load the database properties (columns) from your Notion database and the template elements (curly-braced fields) from your Notion template <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.
- **Automatic Mapping**: If the naming conventions in your database and template are identical, the elements will map automatically <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.
- **Manual Mapping**: If elements are not automatically mapped (indicated by a gray color), you will need to manually click on each unmapped field and select the corresponding database property from the dropdown <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.

## Generating and Downloading Purchase Order PDFs
1.  **Create PDF**: Once mapping is complete, click "Create PDF" <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>. The system will process each row in your database to generate individual PDF documents <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
2.  **Preview Sample**: After successful export, you can click "Preview sample" to review one of the generated PDF files <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>.
3.  **Download All**: Click "Download all" to download all the generated purchase order PDFs as a compressed file <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>. If you miss the download, you can click "Download PDF again" <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>.

## Customization and Advanced Options

*   **Template Customization**: The entire template is customizable. You can edit, modify, or make any changes to the template once it's duplicated in your Notion workspace <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>. Just ensure that any elements you want to populate from the database remain inside curly braces and maintain the exact naming convention <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>.
*   **Saved Connections**: Under the "Connections" option, you can find previously created connections, allowing you to quickly reload the database and template without re-entering details for future exports <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>.
*   **Upgrade Options**: If using a free plan, exported documents will have a "Made with PDF output" watermark <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>. Upgrading to a paid subscription removes the watermark and limits <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>.
*   **Settings**:
    *   The default page format is A4 <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>.
    *   You can add more databases and templates via the settings section <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.
*   **Relational Properties**: If your Notion database uses [[setting_up_customer_and_vendor_details_in_notion | relation properties]] (e.g., linking to a customer or vendor database), ensure you grant access to both the main database and any related databases when connecting to PDF output <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>. This ensures all elements are reflected correctly in the PDF output <a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a>.
*   **Custom Templates**: If you prefer not to use the predefined templates, you can learn how to [[creating_and_using_templates_in_notion | use a custom template from scratch]] by referring to the video provided in the "Help" section <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>.

## Support and Feedback
For any difficulties, issues, or feedback, use the "Feedback" option to send a message <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>. You can also reach out for assistance at notionformyuse@gmail.com <a class="yt-timestamp" data-t="00:09:26">[00:09:26]</a>.