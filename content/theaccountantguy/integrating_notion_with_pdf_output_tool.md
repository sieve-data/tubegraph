---
title: Integrating Notion with PDF Output Tool
videoId: 70hk3h7f_o8
---

From: [[theaccountantguy]] <br/> 

This guide demonstrates how to [[using_pdf_output_tool_with_notion | integrate Notion with PDF Output]] to [[generating_pdf_documents_from_notion_database | generate PDF documents]] from a Notion database and template, specifically using a purchase order contract template as an example <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>.

## Getting Started with PDF Output

To begin, log in to PDFoutput.com <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. The interface will display options for connection name, Notion database, and Notion template <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>.

### Finding and Duplicating Predefined Templates

1.  **Access Templates**: On the right sidebar, click on "Templates" <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>. This will load a list of predefined templates such as invoices, payment receipts, and purchase orders <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. (e.g., [[integrating_notion_with_pdf_output_for_invoices | Invoices]])
2.  **Search for Templates**: Use the search icon to quickly find a required template <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.
3.  **Download/Duplicate**: Click the "Download" link next to the desired template <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. This opens a new page, like the "Purchase Order PDF generator page," which contains a database and a template <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>.
4.  **Duplicate to Notion**: On the Notion page, click "Duplicate" (or "Start with this template" if published) to add the page to your Notion workspace <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>. Select your Notion workspace where you want to add the page <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.

## Understanding Templates and Databases

*   **Template Structure**: The template features elements like purchase order number, date, supplier, and buyer name <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.
    *   **Placeholders**: Elements enclosed in curly braces (e.g., `{purchase order number}`, `{date}`, `{supplier name}`) are placeholder texts that will be replaced with data <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>.
*   **Database Structure**: The Notion database contains pre-defined fields such as supplier name, buyer name, date, and purchase order number, with multiple rows of information <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.
    *   The goal is to [[synchronizing_notion_data_with_pdf_output | synchronize Notion data with PDF output]] by replacing the template's placeholder text with corresponding column values from the database <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.

## Connecting Notion to PDF Output

After duplicating the template to your Notion workspace:

1.  **Go to Settings**: In PDF Output, navigate to the "Settings" section <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.
2.  **Page Format**: Select your desired page format for the PDF <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.
3.  **Add Templates**: Click "Click here to add templates" <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.
4.  **Select Workspace**: Choose the Notion workspace where you duplicated the template <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.
5.  **Select Pages**: Select the specific Notion page (e.g., "Purchase order PDF generator") that contains your template and database <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>.
6.  **Allow Access**: Click "Allow Access" to connect the Notion page with PDF Output <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>. A successful authentication will redirect you back to the PDF Output page <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.

## Mapping Database Fields to Template Placeholders

Once connected, PDF Output will load the database and template elements:

1.  **Select Database and Template**: From the dropdowns, select your Notion database (e.g., "purchase order database") and the template page <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>. Give your connection a name <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>.
2.  **Match Properties**: The system will automatically try to match Notion database properties (on the left) with template elements (on the right) <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.
    *   **Troubleshooting Mismatches**: If elements are unmatched (e.g., "total amount" in the template vs. "Total Amount" in the database due to spacing differences), click the "Filter unmapped properties" option to identify them <a class="yt-timestamp" data-t="00:06:12">[00:06:12]</a>. Manually select the correct matching property <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>.
    *   **Customization Note**: Ensure that the names of the database properties exactly match the names within the curly braces in your template (e.g., `{TotalAmount}` should match a database column named "TotalAmount" or "Total Amount" that you manually map) <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>.

## Generating and Exporting PDF Documents

This tool enables [[generating_pdf_documents_in_bulk_using_notion_and_pdf_output | generating PDF documents in bulk]].

1.  **Export**: Click the "Export" button <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>.
2.  **PDF Status Column**: PDF Output will automatically add a "PDF status" column to your Notion database. When a row's checkbox in this column is ticked, it indicates the PDF document has been generated for that row <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>. To regenerate a PDF, ensure this checkbox is unticked <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>.
3.  **Preview**: After successful export, click "Preview Sample" to view a sample of the generated PDF <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>. The generated PDF will show the data correctly populated from the Notion database <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>.
4.  **Download**: Click "Download all documents" to save all generated PDFs to your local system <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>. You can then open and review the individual [[exporting_and_previewing_pdf_documents_generated_in_notion | exported PDF documents]] <a class="yt-timestamp" data-t="00:08:05">[00:08:05]</a>.

## Additional Features

*   **Connections**: The "Connections" tab stores generated PDF document configurations, allowing you to quickly regenerate documents without re-entering database and page information <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a>.
*   **Upgrade**: Free plans will generate PDFs with a watermark; paid plans remove it <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>.
*   **Settings**: Define page format and add new templates to your workspace here <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>.
*   **Feedback**: Use the feedback option to report any issues or seek assistance with connections <a class="yt-timestamp" data-t="00:09:28">[00:09:28]</a>.
*   **Help**: The "Help" section provides a complete demonstration video for setup and troubleshooting <a class="yt-timestamp" data-t="00:09:39">[00:09:39]</a>.

For any other solutions or PDF document use cases, you can reach out to notionformyuse@gmail.com <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>.