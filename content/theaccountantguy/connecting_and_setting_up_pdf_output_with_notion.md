---
title: Connecting and setting up PDF output with Notion
videoId: n1_fpSFcf3k
---

From: [[theaccountantguy]] <br/> 

This article provides a demonstration on how to [[integration_of_notion_with_pdf_generation | integrate Notion with PDF generation]] by utilizing a Notion page and a Notion template to [[generating_pdfs_from_notion_using_pdfoutput | generate PDF documents]] <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. The specific example used is an invoice template, showing how to [[generating_pdf_documents_in_bulk_using_notion_and_pdfoutput | generate invoice PDFs]] using a Notion database <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>.

## Getting Started with PDF Output

To begin, you need to log in to PDFoutput.com <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. Once logged in, navigate to the "Templates" section <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.

### Selecting a Template

The "Templates" section displays a list of pre-created templates that can be used with PDF Output <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. For the invoice demonstration, download the invoice template by clicking its download link <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>. You can use search, sort, or filter options to find specific templates <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.

After clicking the download link, a new page will open, displaying both the template and its corresponding database <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.

## Understanding Notion Templates and Databases for PDF Generation

The template is designed to generate PDF output from a connected database <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.
It contains elements such as client name, client company, address, invoice number, date, terms, and due date <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>. These elements are enclosed in curly braces, indicating they are placeholder text elements that will be replaced by data from the connected database <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.

The Notion database contains the same elements listed as columns, such as invoice number, date, client name, client company, and client address <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>. Each row in the database will provide the data to replace the corresponding placeholders in the template <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.

## Setting Up the Notion Template and Database

### Duplicating the Template to Notion

1.  From the template page on PDF Output, click "Start with this template" <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.
2.  This will prompt you to duplicate the template into your own Notion workspace <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.
3.  Select your Notion workspace from the dropdown <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>.
4.  Click "Add to Private" (or your chosen workspace) <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>. The template, including its associated database, will now appear in your Notion workspace <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>. This is part of [[setting_up_notion_templates_and_databases_for_pdf_generation | setting up Notion templates and databases for PDF generation]].

### Adding the Template to PDF Output Settings

1.  Return to PDF Output and click on "Settings" <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.
2.  Select the option to "Add the template" <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.
3.  Choose the specific template that was duplicated into your Notion workspace earlier <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>. Ensure you select the correct Notion workspace <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>.
4.  Click "Select pages" and then choose your "Invoice generator template" from the list <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
5.  Click "Allow access" to authenticate and add the template to your PDF Output setup <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>. This completes the [[connecting_notion_templates_with_pdf_output | connecting Notion templates with PDF output]] step.

### Customizing Templates and Databases

The Notion template is fully customizable; you can add, delete, or modify any elements <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>. It is crucial that all placeholder text elements inside curly braces in the template exactly match the names of the corresponding columns in your Notion database <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>. For instance, "Invoice number" in the template must match the "Invoice number" column in the database <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>. This ensures accurate data replacement when [[using_pdf_output_with_notion_templates | using PDF Output with Notion templates]].

## Connecting and Generating PDFs

### Connecting Database and Template

1.  Back in PDF Output, refresh the page and select the duplicated database (e.g., "Professional Invoice Database") <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>.
2.  Select the corresponding template (e.g., "Professional Invoice Template") <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>.
3.  Give the connection a name, like "Invoice Generator" <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>.
4.  Click "Next" to begin syncing the database and template elements <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>. This is a key step in [[connecting_notion_database_and_templates_to_pdf_output | connecting Notion database and templates to PDF output]].

### Mapping Properties

PDF Output will automatically map Notion properties (database column names) to the template's placeholder elements <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>. Mapped elements will be shown in green <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>. If an element is not mapped, you can manually click on it, search for the correct property, and map it <a class="yt-timestamp" data-t="00:06:32">[00:06:32]</a>. Filter options are available to show unmapped properties <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>.

### Generating the PDF Output

1.  Once all properties are mapped, click "Export" <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>.
2.  In your Notion database, a "PDF Status" column will be present <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>. As documents are generated, this column will automatically get checked for each row <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a>.
3.  After processing, PDF Output will confirm the export was successful <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>.

### Viewing and Downloading PDFs

*   You can click "Preview Sample" to view a single generated PDF (e.g., Invoice 1) <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>.
*   To download all generated PDFs, click "Download All" <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>. Each row from the database will result in a separate PDF document <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>.

## Important Considerations

*   **Customization**: Both the template and database can be customized to your needs <a class="yt-timestamp" data-t="00:08:38">[00:08:38]</a>.
*   **Re-generation**: Before re-generating documents, ensure the "PDF Status" column for the desired rows in your Notion database is unchecked. Ticked rows will be ignored <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>.
*   **Watermarks**: On the free plan, generated PDFs will include a "PDF Output" watermark <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>. Upgrade to a paid plan to remove the watermark <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>.
*   **Saved Connections**: After generating an output, the connection details are saved under the "Connections" section <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>. Clicking on a saved connection will automatically load the same database and template, allowing you to proceed without re-mapping <a class="yt-timestamp" data-t="00:09:39">[00:09:39]</a>. This streamlines the [[managing_pdf_export_and_connections_in_notion | managing PDF export and connections in Notion]] process.

For further assistance, the "Help" section provides a setup demonstration <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>. You can also send feedback or questions to notionforuse@gmail.com <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>.