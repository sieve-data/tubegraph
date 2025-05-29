---
title: Working with purchase order templates in PDF generation
videoId: hfHjnNxqo4o
---

From: [[theaccountantguy]] <br/> 

This guide explains how to [[automating_pdf_generation_with_userdefined_templates | automate PDF generation]] of [[generating_pdf_documents_for_purchase_orders | purchase orders]] in bulk using a [[using_notion_templates_for_pdf_generation | Notion page]] and [[using_notion_templates_for_pdf_generation | Notion database]] with the [[using_pdf_output_software_for_invoice_creation | PDF Output]] service <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>.

## Template and Database Structure

A [[generating_pdf_documents_for_purchase_orders | purchase order template]] is used, featuring fields like purchase order number, date, supplier, buyer name, and other relevant details, which are enclosed in curly braces (e.g., `{Purchase Order Number}`) <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. These curly-braced items are placeholders that will be replaced with data from a Notion database <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>.

The Notion database must contain columns with the exact same naming convention as the curly-braced fields in the template <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. Each row in the database represents a unique [[generating_pdf_documents_for_purchase_orders | purchase order]] for which a [[generating_pdf_documents_for_purchase_orders | PDF document]] will be generated <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

## Step-by-Step PDF Generation Process

To [[generating_purchase_order_pdfs_in_bulk_using_notion | generate purchase order PDFs in bulk]]:

### 1. Log in to [[using_pdf_output_software_for_invoice_creation | PDF Output]].com <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>

Upon logging in, the interface will prompt you to connect a Notion database and a Notion template <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>.

### 2. Duplicate Predefined Templates <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>

*   Navigate to the "Templates" section in the sidebar <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.
*   Search for the "purchase order template" <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.
*   Click on both the database link and the template link presented <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.
*   Click "Start with this template" to duplicate both the database and the template into your Notion workspace <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>. Select your Notion workspace and click "Add to private" to complete duplication <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.

### 3. Connect Notion Database and Template to [[using_pdf_output_software_for_invoice_creation | PDF Output]] <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>

*   Back in [[using_pdf_output_software_for_invoice_creation | PDF Output]], click "click here to add database" or "click here to add template" <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
*   Grant permission by selecting your Notion workspace and choosing the duplicated database and template <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>. Click "Allow access" <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
*   Once authorized, both the database and template will appear in the [[using_pdf_output_software_for_invoice_creation | PDF Output]] interface <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>. If not immediately visible, click "Refresh" <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.

### 4. Map Fields <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>

*   Define a name for the export, such as "Purchase Order" <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>.
*   Click "Next" <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>. The system will load the database elements and template elements (those defined in curly braces) <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.
*   If the naming conventions between the Notion database and template are exact, the elements will automatically map <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>. Otherwise, manual mapping is required by clicking on a greyed-out field and selecting the corresponding database element <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.

### 5. Generate and Download PDFs <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>

*   Click "Create PDF" <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>.
*   The system will process and [[generating_pdf_documents_for_purchase_orders | generate PDF documents]] for each row in your database <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
*   After successful export, you can "Preview sample" to review one of the generated files <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>.
*   Click "Download all" to download all the generated [[generating_pdf_documents_for_purchase_orders | PDF documents]] <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>. Each document will accurately reflect the data from its respective database row <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>.

## Customization and Additional Features

*   **Template Customization**: The entire template is customizable; you can edit, modify, or make any changes once it's duplicated to your Notion workspace <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>. Ensure that any data you want to replace from the database remains within curly braces and follows the exact naming convention in both the template and the database <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>.
*   **Connections**: The "Connections" option on the right sidebar shows previously created connections, allowing you to quickly reload the database and template without re-entering them for future exports <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>.
*   **Upgrade Options**: Free plans include a "Made with [[using_pdf_output_software_for_invoice_creation | PDF Output]]" watermark <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>. Upgrading to a paid subscription removes the watermark and any limits on [[generating_pdf_documents_for_purchase_orders | PDF document]] generation <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>.
*   **Settings**: Default page format is A4 <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>. You can add more databases and templates via the settings if needed after the initial setup <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.
*   **Relational Properties**: If your Notion database uses relation properties, ensure you grant access to those related databases during the connection process so all elements are reflected correctly in the [[generating_pdf_documents_for_purchase_orders | PDF output]] <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>.
*   **Custom Templates**: A separate help video demonstrates how to use a custom template from scratch if you prefer not to use the predefined templates <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>.

## Support and Feedback

*   For any issues or feedback, use the "Feedback" option in the sidebar to send a message <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>.
*   You can also reach out for assistance at notionformyuse@gmail.com <a class="yt-timestamp" data-t="00:09:26">[00:09:26]</a>.