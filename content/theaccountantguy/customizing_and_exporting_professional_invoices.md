---
title: Customizing and exporting professional invoices
videoId: n1_fpSFcf3k
---

From: [[theaccountantguy]] <br/> 

This guide demonstrates how to [[generating_pdf_documents_from_invoices | generate PDF documents]] from Notion pages and templates, specifically focusing on [[creating_professional_invoice_templates | invoice templates]] <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. The process involves utilizing a Notion database to populate an invoice template and produce corresponding PDF outputs <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.

## Getting Started with PDF Output

To begin, you need to log into PDFOutput.com <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. After logging in, navigate to the "template" section <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. Here, you'll find a list of pre-created templates compatible with PDF Output <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. For invoices, click the download link next to the invoices template <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>. A search, sort, and filter option is available to find other specific templates <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.

### Understanding the Invoice Template and Database

Upon downloading, a new page will open showing both the invoice template and its associated database <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.

*   **Template**: The template contains placeholder text elements, such as `client name`, `client company address`, `invoice number`, `date`, `terms`, and `due date` <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>. These are enclosed in curly braces, indicating they will be replaced by data from the connected database <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.
*   **Database**: The database is a Notion database with columns that correspond to the placeholder elements in the template (e.g., `invoice number`, `date`, `client name`, `client company`, `client address`) <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>. Each row in the database represents a distinct invoice, and its data will populate the respective elements in the template <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.

### Duplicating the Template to Notion

To start, click the "start with this template" option <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>. This will prompt you to duplicate the template into your personal Notion workspace <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>. Select your desired Notion workspace from the dropdown and click "add to private" <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>. The template and its database will then appear in your Notion workspace <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>. This establishes a [[creating_a_professional_invoice_template_in_notion | professional invoice template in Notion]].

## Connecting and Customizing

### Adding the Template to PDF Output Settings

After duplicating, return to PDF Output and go to the "settings" section <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>. Here, you'll find an option to "add the template" <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>. Select the Notion workspace where you duplicated the template, then choose the "invoice generator template" from the list of available pages and click "allow access" <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>. The template will be authenticated and added to your PDF Output setup <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.

### [[customizing_invoice_templates_in_notion | Customizing Invoice Templates in Notion]]

The Notion template is fully [[customizing_and_exporting_generated_pdf_files | customizable]] <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>. You can add, delete, or modify elements as needed <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.

*   **Template Customization**: When [[customizing_invoice_details_in_notion | customizing invoice details in Notion]], ensure that all placeholder text elements remain inside curly braces <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>.
*   **Database Customization**: The exact same naming convention used for the placeholder text in the template must be used for the corresponding column names in the Notion database <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>. For example, if your template has `{Invoice Number}`, your database column must also be named `Invoice Number` <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>. This ensures correct mapping and successful PDF generation <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.

## Generating the PDF Output

1.  **Select Database and Template**: In PDF Output, select the Notion database and the "professional invoice template" you've set up <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>. Give your connection a name, then click "next" <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>.
2.  **Mapping Properties**: PDF Output will sync the database and template elements <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>. Notion properties (database columns) will be listed on the left, automatically mapped to their corresponding elements in the template (shown in green) <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>. If any property is not mapped, you can manually click and search to map it <a class="yt-timestamp" data-t="00:06:32">[00:06:32]</a>.
3.  **Exporting**: Once all elements are correctly mapped, click "export" <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>. As the documents process, a "PDF status" column in your Notion database will automatically get checked, indicating that the document for that row is being generated <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>.
4.  **Preview and Download**:
    *   After a successful export, you can click "preview sample" to view one of the generated invoices <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>.
    *   To download all generated PDF invoices, click "download all" <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>. This will download all PDF outputs corresponding to each row in your database <a class="yt-timestamp" data-t="00:08:13">[00:08:13]</a>.

## Important Considerations

*   **Regenerating Documents**: If you make changes to a database row and wish to regenerate its PDF, ensure the "PDF status" column for that row is unticked (unchecked) before generating the output <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>. Ticked rows will be ignored <a class="yt-timestamp" data-t="00:08:51">[00:08:51]</a>.
*   **Watermarks**: Free plans will generate templates with a PDF Output watermark <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>. To remove the watermark, an upgrade to a paid plan is required <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>.

## Reusing Connections and Help

Once you have generated and exported files, the connection details are saved. You can access them under the "connections" section <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>. This allows you to automatically load the same database and template without re-mapping <a class="yt-timestamp" data-t="00:09:39">[00:09:39]</a>. The "help" section provides a full demonstration for setting up the process for the first time <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>. For questions or feedback, you can reach out via notionforuse@gmail.com <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>.