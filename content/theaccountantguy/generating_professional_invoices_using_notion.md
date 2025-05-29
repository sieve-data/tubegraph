---
title: Generating professional invoices using Notion
videoId: n1_fpSFcf3k
---

From: [[theaccountantguy]] <br/> 

This article details how to [[generating_professional_invoice_pdfs_using_notion | generate PDF documents]] from Notion pages and databases, specifically focusing on [[professional_invoice_template_in_notion | invoice templates]] <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a> <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. The process leverages the PDF Output platform to facilitate [[creating_pdf_documents_with_notion_templates | PDF document creation with Notion templates]] <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>.

## Getting Started with PDF Output

To begin, you need to access PDF Output's website <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. After logging in, navigate to the "Template" section <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a> <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>.

### Obtaining the Invoice Template

PDF Output provides a list of pre-created templates <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>. For invoices, you can download the specific invoice template by clicking the download link next to it <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a> <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>. A search, sort, or filter option is available to find other templates if needed <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.

### Duplicating the Notion Template

Once you've selected the template, click "Start with this template" <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>. This will prompt you to duplicate the template into your own Notion workspace <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a> <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>. Select your desired Notion workspace and add the template to your private pages <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a> <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a> <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>. This will add both the [[professional_invoice_template_in_notion | invoice template]] and its corresponding database to your Notion <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a> <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>.

### Connecting Notion to PDF Output

After duplicating the template in Notion, return to PDF Output and go to the "Settings" section <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a> <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>. Here, you'll find an option to "Add Template" <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>. Select the Notion workspace where you duplicated the template, then choose the "Invoice Generator Template" from the list of available pages, and click "Allow Access" <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a> <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a> <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a> <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>. This authenticates and adds the template to your PDF Output setup <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a> <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>.

## Template and Database Structure

The Notion invoice template contains placeholder text elements, such as `client name`, `client company address`, `invoice number`, `date`, `terms`, and `due date` <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a> <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>. These are enclosed in curly braces `{}` and are designed to be replaced by data from a connected database <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a> <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.

The corresponding Notion database has columns that match these placeholder names, such as "invoice number", "date", "client name", "client company", and "client address" <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a> <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a> <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>. Each row in the database provides the specific data that will populate a unique invoice PDF <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a> <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a> <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.

For successful generation, ensure that the placeholder names in the template exactly match the column names in the database <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a> <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a> <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a> <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>.

## Generating Invoices

After syncing the database and template, PDF Output will display the mapping of Notion properties (database columns) to the template elements <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a> <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>. Mapped elements will appear in a green bar <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a> <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>. If any properties are not mapped, they will be indicated, and you can manually search and map them <a class="yt-timestamp" data-t="00:06:32">[00:06:32]</a> <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>.

To [[generating_professional_invoices_from_a_notion_database | generate professional invoices from a Notion database]], click "Export" <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a> <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>. As documents are generated, a "PDF Status" column in your Notion database will automatically be checked for each processed row <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a> <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a>. Once the export is successful, you can preview a sample invoice <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a> <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a> or download all generated PDFs <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a> <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>. This allows for [[generating_pdf_invoices_in_bulk_with_notion | generating PDF invoices in bulk with Notion]] based on your database entries.

## Customization and Tips

*   **Template Customization**: The invoice template is fully customizable <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>. You can add, delete, or modify elements <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>. Remember that any placeholder text elements that need to be dynamically populated must remain inside curly braces `{}` and match a corresponding column name in your database <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a> <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a> <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a> <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>.
*   **Database Customization**: You can also customize the database columns and entries as per your requirements <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a> <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>.
*   **Re-generation**: For re-generating a document, ensure the "PDF Status" column for that specific row in your Notion database is *unticked* before starting the generation process <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a> <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>. Ticked rows will be ignored <a class="yt-timestamp" data-t="00:08:51">[00:08:51]</a> <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>.
*   **Watermarks**: Free plans may include a watermark on generated PDFs <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a> <a class="yt-timestamp" data-t="00:09:07">[00:09:07]</a>. To remove it, consider upgrading to a paid plan <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a> <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>.
*   **Saved Connections**: After an initial export, your database and template connection settings are saved <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a> <a class="yt-timestamp" data-t="00:09:34">[00:09:34]</a> <a class="yt-timestamp" data-t="00:09:35">[00:09:35]</a>. You can easily reload them without re-mapping for future generations <a class="yt-timestamp" data-t="00:09:39">[00:09:39]</a> <a class="yt-timestamp" data-t="00:09:40">[00:09:40]</a> <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>.

## Support

The "Help" section within PDF Output provides a full demonstration of the setup process <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a> <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>. For questions or feedback, you can contact notionforuse@gmail.com <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a> <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>.