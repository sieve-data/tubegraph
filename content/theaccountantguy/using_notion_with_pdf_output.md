---
title: Using Notion with PDF output
videoId: n1_fpSFcf3k
---

From: [[theaccountantguy]] <br/> 

This guide provides a demonstration of how to [[using_pdfoutput_tool_for_notion | utilize a Notion page and template]] to [[pdf_document_generation_from_notion | generate PDF documents]] using PDFOutput.com <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. The process is illustrated with an invoice template <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.

## Getting Started with PDFOutput.com

To begin, you need to log in to PDFOutput.com <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. Upon logging in, you will see an interface that allows you to proceed to the "Templates" section <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.

## Template Selection

The "Templates" section displays a list of templates compatible with PDFOutput <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>. For demonstrations, an "invoices template" is used <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.

*   You can use search, sorting, or filter options to find specific templates <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.
*   Click the "Download" link next to the desired template (e.g., invoices template) <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>. This opens a new page displaying both the template and its corresponding database <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.

## Understanding Notion Templates and Databases

The template is designed to [[pdf_document_generation_from_notion | generate PDF output]] from a connected Notion database <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.

### Template Structure

*   Templates contain placeholder text elements enclosed in curly braces, such as `{{client name}}`, `{{client company address}}`, `{{invoice number}}`, `{{date}}`, and `{{terms}}` <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.
*   These placeholder texts are automatically replaced with data from the connected Notion database <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.

### Database Structure

*   The Notion database contains columns with names that exactly match the placeholder text elements in the template (e.0g., "Invoice Number", "Date", "Client Name", "Client Company", "Client Address") <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>.
*   Each row in the database corresponds to a unique PDF document that will be generated <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.

### Customization

The Notion template is fully customizable; you can add, delete, or modify elements <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.

*   **Key Rule**: Ensure all placeholder text elements in the template are placed inside curly braces <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.
*   **Matching Names**: The column names in your Notion database must exactly match the placeholder names in the template <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>. This ensures proper data mapping for [[creating_pdf_documents_from_notion_database | creating PDF documents from the Notion database]] <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.

## Setting Up Your Notion Workspace

1.  Click "Start with this template" on PDFOutput.com <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.
2.  Duplicate the template onto your own Notion workspace <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.
3.  Select your Notion workspace from the dropdown and click "Add to private" <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>.
4.  The template, including its database, will be added to your Notion account <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.

## [[connecting_notion_with_pdf_output_via_api | Connecting Notion with PDF Output via API]]

1.  Return to PDFOutput.com and navigate to "Settings" <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.
2.  Click on the option to "Add the template" <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.
3.  Select the specific template you duplicated earlier from the list <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>.
4.  Ensure you select the same Notion workspace where you duplicated the template <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>.
5.  Click "Select pages" and then choose your "Invoice Generator Template" <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
6.  Click "Allow access" to authenticate and add the template to your PDFOutput setup <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.

## [[notion_database_integration_with_pdf_generation | Notion Database Integration with PDF Generation]]

Once the template is added and synced, you will need to map the Notion properties.

### Mapping Properties

1.  Go to the "Database" section on PDFOutput.com and select your Notion database <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>.
2.  Select the corresponding Notion template (e.g., "Professional Invoice Template") <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>.
3.  Give the connection a name (e.g., "Invoice Generation") <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>.
4.  Click "Next." PDFOutput will sync the elements of the database and template <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>.
5.  On the mapping screen, Notion properties (database column names) are listed on the left <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>.
6.  These properties are automatically mapped to the corresponding elements from the template (the placeholder texts in curly braces) <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>.
7.  Mapped elements are shown with a green bar <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>. If an element is not mapped, you can manually click on it and search for the correct property to map it <a class="yt-timestamp" data-t="00:06:32">[00:06:32]</a>.
8.  You can use filter options to show only unmapped properties or use search/sort for specific elements <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>.

## [[process_of_exporting_pdfs_from_notion | Process of Exporting PDFs from Notion]]

1.  Once mapping is complete, click "Export" <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>.
2.  PDFOutput will start processing the documents <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>.
3.  In your Notion database, a "PDF Status" column will be present; it will automatically tick as each document is generated <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>.
4.  Once the export is successful, you can click "Preview Sample" to view a single generated PDF <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>.
5.  Click "Download All" to download all [[generating_pdf_documents_from_a_notion_database | generated PDF documents from the Notion database]] <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>. Each row in your Notion database will produce a separate PDF output <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>.

### Important Notes for Generation:

*   Before generating, ensure the "PDF Status" checkbox for the specific row in your Notion database is unticked <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>.
*   If a row is already ticked, it will be ignored during the generation process <a class="yt-timestamp" data-t="00:08:51">[00:08:51]</a>.

## Additional Features and Support

*   **Templates**: You can explore other templates available on PDFOutput.com <a class="yt-timestamp" data-t="00:08:58">[00:08:58]</a>.
*   **Watermark**: On a free plan, generated PDFs will include a watermark <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>. To remove it, upgrade to a paid plan <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>.
*   **Saved Connections**: After generating output, the connection with all values is saved under the "Connections" section <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>. This allows you to quickly load the same database and template for future generations without re-mapping <a class="yt-timestamp" data-t="00:09:38">[00:09:38]</a>.
*   **Help Section**: A detailed demonstration on initial setup is available in the help section <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>.
*   **Feedback**: For questions or feedback, you can reach out via email at notionforuse@gmail.com <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>.