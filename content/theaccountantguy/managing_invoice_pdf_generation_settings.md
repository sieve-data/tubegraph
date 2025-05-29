---
title: Managing Invoice PDF Generation Settings
videoId: r6IYxPK0iz8
---

From: [[theaccountantguy]] <br/> 

[[Using PDFOutput software for invoice creation | PDFoutput.com]] facilitates the creation of professional invoice PDF documents in bulk using Notion templates and databases <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. This guide outlines the key settings and management features available within the software for efficient document generation.

## Template and Database Integration

The core of [[generating_pdf_invoices_using_pdf_output_service | PDF generation]] relies on a Notion template and a Notion database <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>.
*   **Template Elements**: Any element placed inside curly braces `{}` within the template will be replaced by corresponding items from a Notion database <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. For example, `{client name}`, `{client company}`, and `{client address}` are placeholders <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.
*   **Database Correspondence**: The Notion database must contain properties with the exact same names as the placeholders in the template <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.

## Connecting Notion Workspace

To begin, you need to connect your Notion workspace to PDFoutput.com <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.
1.  **Login**: Access PDFoutput.com and log in <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.
2.  **Duplicate Templates**: Before connecting, copy the desired template and database to your local Notion workspace <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.
    *   Navigate to the "Templates" section on PDFoutput.com <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.
    *   Search for the relevant template (e.g., "invoice") <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.
    *   Click on both the database link and template link <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.
    *   For each, click the "Duplicate" option in the top right corner and select your Notion workspace to add them <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.
3.  **Add Database/Template**: On the PDFoutput.com "Connection Details" screen, click "Add template" or "Add database" <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.
    *   Select your Notion workspace <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>.
    *   Choose the duplicated template and database <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.
    *   Click "Allow access" to automatically add them to the PDFoutput portal <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.
4.  **Define Connection Name**: Provide a name for your connection (e.g., "Invoice Template") <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.

## Mapping Database Properties

Once the database and template are connected, PDFoutput.com automatically maps database properties to template elements <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
*   **Automatic Mapping**: If the property names in your Notion database exactly match the names inside the curly braces in your template, they will map automatically <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>.
*   **Manual Mapping**: If names differ, elements will appear unmapped (gray icon) <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>. You must manually select the corresponding property from the dropdown list <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.

## General [[understanding_pdf_output_settings_and_features | PDF Output Settings and Features]]

The sidebar in PDFoutput.com provides several management options:

### Connections
*   This section displays all previously created connections, allowing you to quickly reload a configured database and template for [[using_pdf4put_for_bulk_invoice_generation | bulk PDF generation]] without redefining them <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>.

### Templates
*   Access a list of pre-added templates for various use cases <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>. Remember to duplicate both the database and template links to your Notion workspace before use <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>.

### Upgrade
*   Manage your subscription <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>. The free plan includes a "Made with PDF output" watermark, which is removed with paid subscriptions <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>.

### Settings
*   **Page Format**: Define the specific page format for your documents, such as A4 size (default) <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>.
*   **Add More Databases/Templates**: Subsequently add more Notion databases and templates to your PDFoutput portal for future use <a class="yt-timestamp" data-t="00:09:33">[00:09:33]</a>. This is useful after the initial setup <a class="yt-timestamp" data-t="00:09:46">[00:09:46]</a>.

### Feedback
*   Send messages or queries to the support team for assistance <a class="yt-timestamp" data-t="00:09:58">[00:09:58]</a>.

### Help
*   Find detailed instructions on how to connect and use your own [[customizing_document_settings_and_layout_in_pdf_generation | custom PDF document]] and database <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>.

## Customization Tips and Considerations

*   **Template Customization**: The template is fully [[customizing_document_settings_and_layout_in_pdf_generation | customizable]] <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>. Ensure that any data you want pulled from the database is enclosed in curly braces `{}` and uses the exact corresponding name from the database <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>.
*   **Relational Properties**: If your Notion database uses relational properties (meaning it's linked to another database), ensure that all related databases are also connected within PDFoutput.com when setting up your connection <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>.
*   **Refreshing**: If the database and template don't immediately appear after duplication, refresh the webpage <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>.