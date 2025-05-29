---
title: Generating Purchase Order PDFs with Notion
videoId: 70hk3h7f_o8
---

From: [[theaccountantguy]] <br/> 

This article explains how to [[generating_purchase_order_pdfs_in_bulk_using_notion | generate purchase order PDF documents]] using a Notion database and a Notion template, leveraging the PDF Output platform <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>.

## Getting Started with PDF Output

The first step is to log into PDF Output (PDFoutput.com) <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. Upon logging in, you will see an interface with options for connection name, Notion database, and Notion template <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>.

## Finding and Duplicating the Purchase Order Template

1.  **Access Templates**: On the right sidebar, click "Templates" <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.
2.  **Search for "Purchase Order"**: This will display a list of predefined templates, including invoices, payment receipts, and purchase orders <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>. You can use the search icon to quickly find the desired "purchase order" template <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.
3.  **Download the Template**: Click the "Download" link next to the purchase order template <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. This opens a new page for the purchase order PDF generator, containing both a database and a template <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>.

### Understanding the Template and Database Structure

*   **Template**: The purchase order template includes elements like purchase order number, date, supplier, buyer, and item descriptions <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. Key elements intended for replacement are enclosed in curly braces, e.g., `{purchase order number}`, `{date}`, `{supplier name}`, `{buyer name}` <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>.
*   **Database**: The accompanying database contains predefined fields such as supplier name, buyer name, date, and purchase order number <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. The system will generate PDF documents for each row of information in the database, replacing the placeholder text in the template with the corresponding column values <a class="yt-timestamp" data-t="00:01:55">[00:02:00]</a>.

### Duplicating to Notion Workspace

1.  **Duplicate the Page**: On the purchase order PDF generator page, click the "Duplicate" option (or "Start with this template" if published) <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.
2.  **Select Workspace**: Choose your Notion workspace where you want to add the page <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.
3.  **Add to Private**: Click "Add to Private" to duplicate the page into your selected Notion workspace <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>. This will add the "purchase order PDF generator" page, including its database and template, to your Notion <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.

## Connecting Notion to PDF Output

1.  **Go to Settings**: Return to PDF Output and click on "Settings" <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.
2.  **Configure Page Format**: You can select your desired page format for the PDF <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.
3.  **Add Templates**: Click "Click here to add templates" <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.
4.  **Connect Workspace**: Select the Notion workspace where you duplicated the template <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.
5.  **Select Pages**: Click "Select Pages" and choose the "purchase order PDF generator" page <a class="yt-timestamp" data-t="00:03:45">[00:03:50]</a>.
6.  **Allow Access**: Click "Allow Access" to connect the Notion page with PDF Output <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>. After successful authentication, you will be redirected back to the PDF Output page <a class="yt-timestamp" data-t="00:04:01">[00:04:12]</a>.

### Mapping Database and Template Elements

1.  **Select Database and Template**: After refreshing the PDF Output page, select the "Purchase Order Database" from the dropdown <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a> and then select the "template" page (not the "purchase order PDF generator" page) from the template dropdown <a class="yt-timestamp" data-t="00:05:25">[00:05:27]</a>.
2.  **Name the Connection**: Give the connection a name, e.g., "Purchase Order" <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>.
3.  **Proceed to Mapping**: Click "Next" <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>. PDF Output will automatically match most elements <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.
4.  **Handle Unmatched Properties**:
    *   If an element is unmatched (e.g., "Total Amount" in the template vs. "Total Amount" with a space in the database) <a class="yt-timestamp" data-t="00:05:49">[00:06:02]</a>, you will need to manually map it.
    *   Use the "Filter unmapped properties" option to quickly identify unmatched items <a class="yt-timestamp" data-t="00:06:12">[00:06:14]</a>.
    *   Click on the unmatched template element and search for the corresponding Notion property in the database <a class="yt-timestamp" data-t="00:06:21">[00:06:23]</a>.
    *   Ensure exact naming in Notion database columns to match the curly brace placeholders in the template (no extra commas or spaces) <a class="yt-timestamp" data-t="00:04:44">[00:04:47]</a>.

> ##### Customization Tip
> Both the template and database elements are customizable. You can add, delete, or modify values, as long as the values you want to replace are placed inside curly braces in the template and the database column names exactly match these placeholder names <a class="yt-timestamp" data-t="00:04:25">[00:04:43]</a>.

## Generating and Downloading PDFs

1.  **Export**: Once all elements are mapped, click "Export" <a class="yt-timestamp" data-t="00:06:53">[00:06:54]</a>.
2.  **PDF Status Column**: During export, a "PDF Status" column will be automatically added to your Notion database <a class="yt-timestamp" data-t="00:06:58">[00:07:01]</a>. When a PDF document is generated for a row, its checkbox in this column will be ticked <a class="yt-timestamp" data-t="00:07:07">[00:07:09]</a>. To regenerate a PDF for a specific row, ensure this checkbox is unticked <a class="yt-timestamp" data-t="00:07:12">[00:07:15]</a>.
3.  **Preview and Download**: After successful export, you can click "Preview Sample" to view a generated PDF <a class="yt-timestamp" data-t="00:07:20">[00:07:23]</a>. To download all generated documents, click "Download all documents" <a class="yt-timestamp" data-t="00:07:55">[00:07:57]</a>. The downloaded documents will be named according to the purchase order number (e.g., "purchase order number two", "purchase order number one", "purchase order number three") <a class="yt-timestamp" data-t="00:08:06">[00:08:15]</a>.

## Additional Features of PDF Output

*   **Connections Tab**: Automatically saves created connections, allowing you to quickly regenerate documents without re-entering database and page information <a class="yt-timestamp" data-t="00:08:32">[00:08:38]</a>.
*   **Upgrade**: Paid plans remove watermarks from generated templates, which are present on the free plan <a class="yt-timestamp" data-t="00:09:01">[00:09:09]</a>.
*   **Settings**: Allows defining page format and connecting templates <a class="yt-timestamp" data-t="00:09:18">[00:09:23]</a>.
*   **Feedback**: Provides an option to send feedback or report issues <a class="yt-timestamp" data-t="00:09:27">[00:09:33]</a>.
*   **Help Section**: Contains a complete demonstration video for troubleshooting <a class="yt-timestamp" data-t="00:09:39">[00:09:41]</a>.

For any other solutions or specific PDF document use cases, you can reach out to notionformyuse@gmail <a class="yt-timestamp" data-t="00:09:51">[00:09:56]</a>.