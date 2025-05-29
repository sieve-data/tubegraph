---
title: Setting up and customizing Notion database for invoices
videoId: n1_fpSFcf3k
---

From: [[theaccountantguy]] <br/> 

This guide demonstrates how to [[setting_up_a_database_in_notion | utilize a Notion page and template]] to [[generating_pdf_invoices_from_notion_database | generate PDF invoices]] from a [[setting_up_notion_databases_for_pdf_generation | Notion database]] using PDF Output.com <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>.

## Accessing PDF Output

To begin, log in to PDFoutput.com <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. After logging in, navigate to the "template section" <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>, where you will find a list of available templates <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.

## Downloading the Invoice Template

1.  From the "templates" list, locate the "invoices template" and click its "download link" <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.
    *   You can use the search, sorting, or filter options to find specific templates <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.
2.  Clicking the download link will open a new page displaying both the template and its associated database <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.

## Understanding the Template and Database Structure

The Notion template includes elements such as client name, client company, address, invoice number, date, and terms <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>. These elements are enclosed in curly braces (e.g., `{Client Name}`), indicating they are placeholder text <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>. These placeholders will be replaced by data from the connected database <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>.

The corresponding database contains columns with the exact same names as the placeholder elements in the template (e.g., "Invoice Number", "Date", "Client Name", "Client Company", "Client Address") <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>. Each row in the database represents an invoice, and its column values will populate the template's placeholders <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.

## Duplicating the Template to Notion

1.  On the PDF Output page displaying the template and database, click the "Start with this template" option <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.
2.  You will be prompted to duplicate the template to your Notion workspace <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.
3.  Select your desired Notion workspace from the dropdown menu and click "Add to private" <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>.
    *   This will add the [[creating_and_using_an_invoice_template_in_notion | invoice template]] and its database to your Notion workspace <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.

## Connecting Notion to PDF Output

1.  Return to PDF Output and click "settings" <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.
2.  Click the option to "add the template" <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.
3.  Select the Notion workspace where you duplicated the template <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>.
4.  Click "Select pages" and choose the "invoice generator template" <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
5.  Click "Allow access" to authenticate and add the template to your PDF Output setup <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.

## Customizing the Template and Database

Both the Notion template and its database are fully customizable <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.
*   You can add, delete, or modify values in the template <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.
*   **Crucially**, ensure that any placeholder text elements in the template (inside curly braces) have exact matching column names in the Notion database <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>, <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>. For example, `{Invoice Number}` in the template must correspond to a database column named "Invoice Number" <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.

## Generating PDF Invoices

1.  In PDF Output, select the [[creating_a_database_in_notion | database]] and the [[creating_professional_invoice_templates_in_notion | professional invoice template]] you wish to use <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>. Give the generation a name <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>.
2.  Click "Next". PDF Output will sync all elements <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>.
3.  The Notion properties (database column names) will be listed on the left, automatically mapped to the corresponding template elements (placeholder text) <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>.
    *   Mapped elements are shown in green <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>.
    *   If any property is not mapped, it will be indicated, and you can manually search for and map it <a class="yt-timestamp" data-t="00:06:32">[00:06:32]</a>.
    *   Filter options exist to show unmapped properties <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>.
4.  Once mapped, click "Export" <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>.
5.  In your Notion database, a "PDF status" column will automatically get checked as documents are generated <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>.
6.  Upon successful export, you can "preview sample" to view a generated invoice <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>.
7.  Click "Download all" to download all generated PDF invoices <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>.

### Important Considerations for Generation

*   Before generating, ensure the "PDF status" column in your Notion database for the desired rows is unticked <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>. Ticked rows will be ignored <a class="yt-timestamp" data-t="00:08:51">[00:08:51]</a>.
*   The free plan generates documents with a "PDF Output watermark" <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>. To remove it, upgrade to a paid plan <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>.

## Reusing Connections

After exporting files, click on the "connections" section <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>. This will show your previously saved connection with all values <a class="yt-timestamp" data-t="00:09:34">[00:09:34]</a>. Clicking on a saved connection will automatically load the same database and template, allowing you to quickly proceed without re-mapping <a class="yt-timestamp" data-t="00:09:39">[00:09:39]</a>.

## Help and Support

Under the "help" section, you can find a demonstration of the initial setup process <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>. For further questions or feedback, you can reach out via email at notionforuse@gmail.com <a class="yt-timestamp" data-t="00:09:59">[00:10:00]</a>.