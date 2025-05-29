---
title: Creating bulk invoices with Notion
videoId: n1_fpSFcf3k
---

From: [[theaccountantguy]] <br/> 

This guide provides a quick demonstration on how to [[bulk_document_generation_in_notion | generate PDF documents]] using a Notion page and template, specifically focusing on [[generating_professional_invoices_using_notion | generating invoice PDFs]] from a Notion database <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>.

## Getting Started with PDF Output.com

To begin, navigate to PDF output.com <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. After logging in, you will see an interface that allows you to create documents <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.

## Obtaining the Invoice Template

1.  **Access Templates**: Proceed to the "template" section on PDF output.com <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>. This section displays a list of templates compatible with PDF Output <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.
2.  **Download Invoice Template**: For [[generating_professional_invoices_using_notion | invoices]], click on the download link next to the invoices template <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>. A search, sort, or filter option is available to find specific templates <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.
3.  **Review Template and Database**: Clicking the download link opens a new page showcasing the template and its corresponding database <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.
    *   The [[professional_invoice_template_in_notion | Notion invoice template]] includes elements like client name, company, address, invoice number, date, terms, and due date <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.
    *   These elements are placeholder text, enclosed in curly braces, which will be replaced by data from the connected Notion database <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.
    *   The Notion database contains columns (e.g., invoice number, date, client name, client company, client address) that match the template's placeholder elements <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>. Each row in the database corresponds to an invoice <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.

## Duplicating the Template to Notion

1.  **Start with Template**: On the template page, click "Start with this template" <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.
2.  **Duplicate to Workspace**: You will be prompted to duplicate the template to your Notion workspace <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>. Select your desired Notion workspace and click "Add to private" <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>.
3.  **Verify Duplication**: The template, including the invoice database, will now appear in your Notion workspace <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.

## Connecting Notion to PDF Output

1.  **Go to Settings**: Return to PDF output.com and click on "Settings" <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.
2.  **Add Template**: Select the option to "Add the template" <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.
3.  **Select Notion Workspace**: Choose the Notion workspace where you duplicated the template <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.
4.  **Select Pages**: Click "Select pages" and choose the "Invoice generator template" from your workspace <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
5.  **Allow Access**: Click "Allow access" to authenticate the template with PDF Output <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>. The template will be added to your PDF Output setup <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>.

## Customizing Templates and Databases

*   **Template Customization**: The template in Notion is fully customizable. You can add, delete, or modify content <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>. Ensure that all placeholder text elements remain inside curly braces <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>.
*   **Database Naming Convention**: Crucially, the column names in your Notion database must exactly match the placeholder names (inside curly braces) used in the template <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>. For example, `Invoice Number` in the template must correspond to an `Invoice Number` column in the database <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.

## [[generating_professional_invoices_from_notion_database | Generating Professional Invoices from Notion Database]]

1.  **Select Database and Template**: In PDF Output, select the Notion database and the [[professional_invoice_template_in_notion | professional invoice template]] you want to use <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>. Give the generation a name <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>.
2.  **Map Properties**: Click "Next" <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>. PDF Output will sync the database and template elements <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>.
    *   Notion properties (database column names) will be listed on the left <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>.
    *   These properties are automatically mapped to corresponding elements from the template <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>. Mapped properties appear in green <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>.
    *   If any property is unmapped, you can manually click and search to map it <a class="yt-timestamp" data-t="00:06:32">[00:06:32]</a>. Filtering options are available to view unmapped properties <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>.
3.  **Export Documents**: Click "Export" <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>.
    *   As documents are generated, a "PDF Status" column in your Notion database will automatically get checked for each row <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>.
    *   Ensure the "PDF Status" column in your Notion database is unticked for any row you want to generate a document for; ticked rows will be ignored <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>.
4.  **Preview and Download**:
    *   Once processing is successful, you can click "Preview sample" to view a generated PDF <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>.
    *   Click "Download all" to download all generated [[creating_bulk_invoice_pdfs | PDF invoices]] <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>.

## Additional Considerations

*   **Watermarks**: On the free plan, generated PDFs will have a PDF Output watermark <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>. To remove it, you need to upgrade to a paid plan <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>.
*   **Reusing Connections**: After generating an output, the connection details are saved. You can access saved connections under the "Connections" section, which will automatically load the same database and template, allowing you to quickly re-generate without re-mapping <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.
*   **Help and Support**: The "Help" section provides setup demonstrations <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>. For questions or feedback, you can contact notionforuse@gmail.com <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>.