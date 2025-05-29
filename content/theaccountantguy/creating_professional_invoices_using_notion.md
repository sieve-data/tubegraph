---
title: Creating professional invoices using Notion
videoId: n1_fpSFcf3k
---

From: [[theaccountantguy]] <br/> 

This guide demonstrates how to [[using_a_notion_database_and_templates_to_create_pdf_invoices | utilize a Notion page and template to generate PDF documents]], specifically focusing on [[generating_professional_invoices_from_notion_database | creating professional invoices]] using a Notion database <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. The process involves leveraging PDF Output, a web-based tool, to connect your Notion database and template for automated PDF generation <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.

## Getting Started with PDF Output

To begin, navigate to PDFoutput.com <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. Once logged in, you'll see an interface that allows you to manage your documents <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>.

### Obtaining the Invoice Template

1.  From the main interface, proceed to the "Templates" section <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.
2.  A list of available templates will be displayed <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>. For invoices, locate the "invoices template" and click its "download" link <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.
3.  You can use the search, sorting, or filter options to find specific templates if needed <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.
4.  Clicking the download link will open a new page displaying both the template and a corresponding Notion database <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.

### Understanding the Template and Database Structure

The displayed template features placeholder text elements enclosed in curly braces (e.g., `{client name}`, `{invoice number}`) <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>. These placeholders are designed to be replaced by data from your Notion database <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.

Crucially, the Notion database linked with the template contains columns (e.g., Invoice Number, Date, Client Name) that correspond directly to these placeholder names in the template <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>. For each row in your database, these elements will populate the respective fields in the generated PDF invoice <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.

> [!warning] Naming Convention
> Ensure that any modifications to placeholder names in the template (within curly braces) are exactly matched by the column names in your Notion database to prevent mapping errors <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.

## Integrating with Your Notion Workspace

1.  On the PDF Output page showing the template and database, click the "Start with this template" option <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.
2.  This action will prompt you to duplicate the template to your Notion workspace <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>. Select your desired Notion workspace from the dropdown and click "Add to Private" <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>. The template and its associated database will then appear in your Notion <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.
3.  Return to PDF Output and go to "Settings" <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.
4.  Click "Add Template" <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.
5.  Select the Notion workspace where you duplicated the template <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>.
6.  Click "Select Pages" and choose the "Invoice Generator Template" from the list <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
7.  Click "Allow Access" to authenticate and add the template to your PDF Output setup <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.

## Generating PDF Invoices

Once the template is successfully added and synced, you can proceed to generate your invoices <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>.

1.  On the PDF Output screen, select your Notion database (e.g., "Invoice") and the "Professional Invoice Template" <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>.
2.  Provide a name for your generation (e.g., "Invoice Generator") <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>.
3.  Click "Next" <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>. The system will then sync the elements of your database and template <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>.
4.  On the mapping screen, Notion properties (database column headers) will be listed on the left <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>. The tool automatically maps these to corresponding template elements <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>.
5.  If any property is unmapped, you can manually click on it and search for the correct element to map it <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a>. Sorting, searching, and filtering options are available to manage properties <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>.
6.  Once mapping is complete, click "Export" <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>.

### Monitoring and Downloading

As the documents are processed, a "PDF Status" column in your Notion database will automatically tick rows as their respective PDFs are generated <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>.

Once the export is successful <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>:
*   You can click "Preview Sample" to view a sample of the generated PDF <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>.
*   Click "Download All" to download all generated PDF invoices <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>. Each row from your Notion database will result in a separate PDF <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>.

## Customization and Best Practices

*   **Template and Database Customization**: Both the invoice template and the Notion database are fully customizable. You can add, delete, or modify elements and values as needed <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>. Remember to maintain consistent naming between template placeholders and database column names <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.
*   **PDF Status Column**: Before [[generating_pdf_invoices_from_notion_data | generating PDF invoices]], ensure that the "PDF Status" column in your Notion database is unticked for the rows you wish to process <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>. Ticked rows will be ignored during generation <a class="yt-timestamp" data-t="00:08:51">[00:08:51]</a>.
*   **Watermarks**: On the free plan, generated PDFs will include a watermark. To remove this, consider upgrading to a paid plan <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>.
*   **Reusing Connections**: After generating and exporting, your connection settings (database and template selection) are saved. You can access them under the "Connections" section to quickly reload and generate more PDFs without remapping <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.
*   **Support**: For any questions or feedback, you can reach out via email to notionforuse@gmail.com <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>. The "Help" section also provides setup guidance <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>.

By following these steps, you can effectively [[invoicing_and_workflow_management_in_notion | manage your invoicing workflow]] and [[using_notion_templates_for_invoice_pdfs | generate professional invoice PDFs]] directly from your Notion data <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.