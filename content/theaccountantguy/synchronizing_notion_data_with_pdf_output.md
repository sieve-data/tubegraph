---
title: Synchronizing Notion data with PDF output
videoId: n1_fpSFcf3k
---

From: [[theaccountantguy]] <br/> 

This article demonstrates how to [[integrating_notion_with_pdf_output_tool | integrate Notion with a PDF output tool]] to [[generating_pdf_documents_from_notion_database | generate PDF documents]] from a Notion page and database template <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. The demonstration focuses on [[integrating_notion_with_pdf_output_for_invoices | generating invoice PDFs]] from a Notion database <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.

## Accessing the PDF Output Tool

To begin [[using_pdf_output_tool_with_notion | using the PDF output tool with Notion]], you must first log in to PDFoutput.com <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. After logging in, navigate to the "Template" section <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. This section displays a list of pre-created templates available for use with PDF Output <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. Users can search, sort, or filter templates to find a specific one, such as an invoice template <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.

## Understanding Notion Templates and Databases

When you select a template, a new page opens, displaying both the template and a corresponding Notion database <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.

### Template Structure
The Notion template, used for [[generating_pdf_documents_from_notion_database | generating PDF documents]], contains placeholder text elements enclosed in curly braces (e.g., `{client name}`, `{invoice number}`) <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>. These placeholders will be replaced with data from the connected Notion database <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.

### Database Structure
The associated Notion database features columns with names that directly correspond to the placeholder text elements in the template (e.g., `invoice number`, `date`, `client name`) <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>. Each row in the database represents a unique record (e.g., an invoice) that will populate the template when a PDF is generated <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.

## [[setting_up_notion_databases_for_pdf_generation | Setting up Notion Databases for PDF Generation]]

To prepare the Notion template for PDF generation:

1.  **Duplicate the Template:** Click the "Start with this template" option on the PDF Output website <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>. This prompts you to duplicate the template into your personal Notion workspace <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>. Select your desired Notion workspace and confirm the duplication <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>. The template and its associated database will then appear in your Notion workspace <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.
2.  **Add Template to PDF Output:** Return to PDF Output and navigate to the "Settings" section <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>. Here, you can add the specific template you just duplicated <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>. Ensure you select the correct Notion workspace where the template was duplicated <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>. After selecting the template (e.g., "Invoice Generator Template"), click "Allow access" to authenticate and add it to your PDF Output setup <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.

### Customizing Templates and Databases
Both the Notion template and its database are fully customizable <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>. You can add, delete, or modify elements <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>. It is crucial to ensure that any placeholder text elements in the template (those in curly braces) have exact matching column names in the Notion database to ensure proper data synchronization <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>. For instance, if the template has `{invoice number}`, the database must have a column named `Invoice Number` <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.

## [[mapping_and_managing_data_fields_between_notion_database_and_pdf_templates | Mapping and Managing Data Fields Between Notion Database and PDF Templates]]

After selecting the Notion database and template within PDF Output, the system syncs their elements <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>. Notion properties (columns from the database) are listed on the left, and corresponding template elements are automatically mapped <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>. Mapped elements are indicated by a green bar <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>. If an element is not automatically mapped, you can manually select and map it <a class="yt-timestamp" data-t="00:06:32">[00:06:32]</a>. Search, sort, and filter options are available to manage these mappings <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>.

## [[generating_pdf_documents_in_bulk_using_notion_and_pdf_output | Generating PDF Documents in Bulk Using Notion and PDF Output]]

Once all elements are correctly mapped, you can proceed to export the documents <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>.

### Export Process
Click "Export" to start the process <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>. In your Notion database, a "PDF Status" column will automatically update, ticking each row as its corresponding PDF document is generated <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>.

### [[exporting_and_previewing_pdf_documents_generated_in_notion | Exporting and Previewing PDF Documents Generated in Notion]]
After successful export, you can:
*   **Preview Sample:** Click "Preview sample" to view a single generated PDF (e.g., Invoice One) <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>. You can verify details like invoice number, date, and client name match the Notion database <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>.
*   **Download All:** Click "Download all" to download all generated PDF documents, corresponding to each row in your Notion database <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>.

### Important Considerations
*   Before [[creating_pdf_documents_from_a_notion_database | creating PDF documents from a Notion database]], ensure the "PDF Status" column for each row in your Notion database is unticked <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>. Ticked rows will be ignored during generation <a class="yt-timestamp" data-t="00:08:51">[00:08:51]</a>.
*   The free plan generates PDFs with a watermark. To remove the watermark, an upgrade to a paid plan is required <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>.

## Reusing Connections and Support

Once a connection is established and a file is exported, the tool automatically saves the connection details <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>. You can access these saved connections under the "Connections" section, which will automatically load the associated database and template, eliminating the need for remapping <a class="yt-timestamp" data-t="00:09:39">[00:09:39]</a>.

For further assistance, the "Help" section provides setup demonstrations <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>. Feedback and questions can be sent to notionforuse@gmail.com <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>.