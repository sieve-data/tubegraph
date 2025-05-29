---
title: Customizing templates for purchase order PDFs
videoId: 70hk3h7f_o8
---

From: [[theaccountantguy]] <br/> 

This article outlines how to [[generating_purchase_order_pdfs_using_notion | generate purchase order PDF documents using a Notion database and a Notion template]] with PDF output.com, including steps for [[customizing_purchase_order_templates | customizing purchase order templates]] and connecting them to a database.

## Getting Started with PDF output.com
To begin, users need to log in to PDF output.com <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. The interface displays options for connection name, Notion database, and Notion template <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>.

### Accessing Predefined Templates
Predefined templates, including invoices, payment receipts, and purchase orders, are available by clicking on the "templates" sidebar element <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>. Users can search for specific templates using the search icon <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a> or utilize sorting and filter options <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.

To use a template, click the "download" link next to the desired template <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. This opens a new page, which serves as the [[generating_purchase_order_pdfs_using_notion | purchase order PDF generator]] page <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.

## Understanding Templates and Databases
The purchase order template includes elements like purchase order number, date, supplier, buyer, and item description <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.
Key aspects to note:
*   **Placeholders**: Elements within curly braces (e.g., `{purchase order number}`, `{date}`, `{supplier name}`, `{buyer name}`) are placeholder texts <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>. These will be replaced by data from the connected Notion database <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.
*   **Database Structure**: The corresponding database contains columns such as supplier name, buyer name, date, and purchase order number, with predefined values <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. The system can [[using_templates_to_create_pdf_documents_in_bulk | generate PDF documents for multiple rows of information]] within the database <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.

### [[customizing_purchase_order_templates | Customizing Templates]] and Databases
Both the template and the database are fully [[customizing_purchase_order_templates | customizable]] <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>. Users can add, delete, or modify any values <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>.
**Important Customization Rules**:
*   All values intended for replacement must be enclosed in curly braces within the template <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.
*   The name of the database column must *exactly* match the placeholder name in the template, without extra commas or spaces, to ensure proper linking <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>.

## Connecting Notion to PDF output.com
1.  **Duplicate the Template**: On the PDF generator page, click "duplicate" (or "start with this template" if published) <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>. Select your Notion workspace to add the page <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>. This duplicates the purchase order PDF generator page, including its database and template, into your Notion workspace <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.
2.  **Connect in PDF output.com Settings**:
    *   Navigate to "settings" in PDF output.com <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.
    *   Select the desired page format for the PDF <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.
    *   Click "click here to add templates" <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.
    *   Select your Notion workspace and the specific Notion page (e.g., "purchase order PDF generator") that was duplicated <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.
    *   Click "allow access" to connect the Notion page with PDF output.com <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>. A successful authentication redirects back to PDF output.com <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.

## Mapping Database Properties to Template Elements
After successful connection and a quick refresh <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>:
*   Select the purchase order database from the drop-down menu <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>.
*   Select the template page from the other drop-down menu <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>.
*   Give the connection a name (e.g., "purchase order") <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>.
*   Click "next" to automatically load and match database properties to template elements <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>.

### Resolving Unmatched Properties
If any properties are unmatched (e.g., due to a space difference in names between the database and template) <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>:
*   Use the "filter unmapped properties" option to quickly identify them <a class="yt-timestamp" data-t="00:06:12">[00:06:12]</a>.
*   Manually map the unmatched property by clicking on it and searching for the correct corresponding name in the template side <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.
*   The left side displays Notion database properties, and the right side shows template elements <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>. Search and sorting options are available <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>.

## Generating and Exporting Purchase Order PDFs
1.  **Export**: Click "export" <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>.
2.  **PDF Status**: A "PDF status" column will be automatically added to the Notion database, indicating PDF generation progress <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>. A checked box in this column means the PDF has been generated for that row <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>. To regenerate a PDF, ensure this checkbox is unticked <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>.
3.  **Preview and Download**: After successful export, users can preview a sample of the generated PDF <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a> and download all generated documents <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>. The downloaded documents will reflect the data from the database <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.

## Additional PDF output.com Features
*   **Connections**: Once a PDF document is generated, a connection is created and stored, allowing users to regenerate documents directly without re-filling database and page information <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a>.
*   **Upgrade**: Free plans include a watermark on generated templates, which can be removed by upgrading to a paid subscription <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>.
*   **Settings**: Define page format and add templates <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>.
*   **Feedback**: Report issues or provide suggestions through the feedback option <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>.
*   **Help**: Access a complete setup video demonstration for troubleshooting <a class="yt-timestamp" data-t="00:09:39">[00:09:39]</a>.

For further assistance with PDF document solutions, contact notionformyuse@gmail.com <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>.