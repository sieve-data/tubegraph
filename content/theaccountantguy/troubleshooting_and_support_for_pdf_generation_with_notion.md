---
title: Troubleshooting and support for PDF generation with Notion
videoId: 70hk3h7f_o8
---

From: [[theaccountantguy]] <br/> 

When [[pdf_document_creation_with_notion_and_pdf_output | generating PDF documents]] using Notion templates and databases with PDF output, several features and guidelines can assist with troubleshooting and support.

## Common Issues and Solutions

### Unmapped Properties
One common issue encountered during [[how_to_integrate_notion_with_pdf_generation_tools | Notion integration]] for PDF generation is unmapped properties <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>. This typically occurs when there is a mismatch between the database column name and the placeholder text in the template <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.

*   **Exact Naming:** Ensure that the name of the database column exactly matches the placeholder text within the curly braces in your Notion template <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>. Avoid adding any extra commas or spaces, as these can cause mismatches <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>.
*   **Identifying Unmapped Items:** To quickly identify unmapped properties, use the filter option "filter unmapped properties" within the PDF output interface <a class="yt-timestamp" data-t="00:06:12">[00:06:12]</a>.

### Regenerating PDFs
If you need to regenerate a PDF document for a specific entry, ensure that the "PDF status" column in your Notion database is unticked <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>. This column is automatically added by PDF output and gets ticked once a PDF has been generated for that row <a class="yt-timestamp" data-t="00:06:59">[00:06:59]</a>.

## Customizing Templates
While predefined templates are available, you can customize your Notion template and database as needed <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>.

*   **Placeholder Format:** Any values that you intend to replace with data from your database must be enclosed within curly braces in your template <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>. For example, `{{Purchase Order Number}}` <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.
*   **Database Fields:** Your Notion database should contain columns that correspond to these placeholder names (e.g., "Purchase Order Number" as a column name) <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.

## PDF Output Features for Support

### Connections
The "Connections" tab within PDF output stores previously generated [[generating_pdf_documents_using_notion | PDF documents]] <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a>. This allows you to quickly regenerate documents without having to re-select the database and template every time <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>. Clicking on a saved connection will automatically fill in the database and template elements, allowing you to proceed directly to export <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>.

### Upgrade Options
If you are on the free plan, all [[using_notion_for_generating_pdf_documents | generated PDF documents]] will include a watermark <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>. Upgrading to a paid plan will remove this watermark from your [[generating_pdf_invoices_from_notion | generated templates]] <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>.

### Settings
The "Settings" section allows you to define the page format for your PDFs <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>. It's also where you initially connect duplicated Notion templates to the PDF output platform <a class="yt-timestamp" data-t="00:09:23">[00:09:23]</a>.

### Feedback
For any issues or problems encountered with [[setting_up_and_connecting_notion_database_for_pdf_creation | connections]] or other functionalities, a feedback option is available <a class="yt-timestamp" data-t="00:09:28">[00:09:28]</a>. Users can select the specific issue from a dropdown and send feedback for assistance <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.

### Help Section
A comprehensive demonstration video for the setup process is available under the "Help" section <a class="yt-timestamp" data-t="00:09:39">[00:09:39]</a>. This serves as a quick resource for troubleshooting and understanding the [[setting_up_and_managing_notion_databases_for_pdf_generation | setup process]] <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>.

## Contact for Further Assistance
For additional solutions or specific use cases related to [[generating_pdf_documents_in_bulk_with_notion | PDF document generation]] with Notion, you can reach out via email at `notionformyuse@gmail.com` <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>.